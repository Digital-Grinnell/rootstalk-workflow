import os
import sys
import traceback
import re
import yaml
import logging
from datetime import datetime
from markdownify import markdownify as md

file_pattern = r"^\d{4}-(spring|fall)\.md$"
year_term_pattern = r"(\d{4})-(spring|fall)"
image_pattern = r".{3}\(.+/image/(.+)\)$"
header_pattern = r"^.+ \| .+$"


# Open the year-term.html file and run the "markdownify" package
#   (https://github.com/matthewwithanm/python-markdownify) on it.
# This produces a new .md file with the same name.
def rootstalk_markdownify(issue):
  filepath = "{}.html".format(issue)
  
  try:
    with open(filepath, "r") as html:
      html_string = html.read()
      # Open a new .md file to receive translated text
      new_file = '{}.md'.format(issue)
      logging.info("Creating new .md file: " + new_file)
      try:
        with open(new_file, "w") as mdf:
          markdown_text = md(html_string)
          print(markdown_text, file=mdf)
  
      except Exception as e:
        logging.error(traceback.format_exc())
        sys.exit(e)

  except Exception as e:
    logging.error(traceback.format_exc())
    sys.exit(e)


def rootstalk_azure_media(issue):
  replacement = '{{% figure_azure pid="xPIDx" caption="" %}}'
  
  ytmd = "{}.md".format(issue)
  logging.info("Attempting to open markdown file: " + ytmd)

  # Open the issue's year-term.md file...
  try:
    with open(ytmd, "r") as issue_md:
      azure_path = "{}-azure.md".format(issue)
      logging.info("Creating new Azure .md file at '{}'.".format(azure_path))

      # Open and write a new year-term-azure.md file...
      try:
        with open(azure_path, "w") as azure_md:
          lines = issue_md.readlines()

          # Clean-up...
          # - translate any year-term-web-resources folder references to new Azure format.
          # - remove all repeated blank lines (reduces whitespace)
          # - remove any line that entirely matches the pattern:  ^.+ | .+$

          previous_blank = False
          removed = 0

          for l in lines:
            line = l.strip()
            if re.match(header_pattern, line):
              previous_blank = True
              logging.info("Removed page header line '{}'".format(line))
              removed = removed + 1
            else:
              match_image = re.match(image_pattern, line)
              if match_image:  # transform image references
                new_line = replacement.replace("xPIDx", match_image.group(1))
                print(new_line, end='\n', file=azure_md)
                previous_blank = False
                logging.info("Replaced image reference '{}' with new line '{}'".format(line, new_line))
                if removed > 0:
                  logging.info("A group of {} redundant blank lines were removed".format(removed))
                  removed = 0
              elif previous_blank and len(line) == 0:  # skip redundant blank lines
                previous_blank = True
                removed = removed + 1
              else:
                print(line, file=azure_md)  # write the line out
                if removed > 0:
                  logging.info("A group of {} redundant blank lines were removed".format(removed))
                  removed = 0
                if len(line) == 0:
                  previous_blank = True
                else:
                  previous_blank = False
    
      except Exception as e:
        logging.error(traceback.format_exc())
        sys.exit(e)

  except Exception as e:
    logging.error(traceback.format_exc())
    sys.exit(e)


def rootstalk_make_articles(issue, file):
  frontmatter = '---\n' \
                'title: \n' \
                'index: \n' \
                'description: \n' \
                'date: \n' \
                'draft: false \n' \
                'authors: \n' \
                '  - name: \n' \
                '    headshot: \n' \
                '    caption: \n' \
                '    bio: " "\n' \
                '  - name: \n' \
                '    headshot: \n' \
                '    caption: \n' \
                '    bio: " "\n' \
                'articletype: \n' \
                'tags: [" "," "] \n' \
                'azure_dir: \n' \
                "azure_headerimage: \n" \
                "---\n"
  
  logging.info("Making article.md files for {}.".format(issue))
  
  # # Look for a year-term.yml file...
  # if not os.path.exists(ytyml):
  #   logging.error("ERROR: No {} YAML file found! You need to create this file if you wish to proceed with the {}-{} issue!".format(ytyml, year, term))
  # else:
  #   logging.info("Processing the {} file.".format(ytyml))
  #
  #   # Check for corresponding .html and -azure.md files in the same directory
  #   html_file = '{}-{}{}'.format(year, term, '.html')
  #   azure_md = '{}-{}{}'.format(year, term, '-azure.md')
  #   if not os.path.exists(html_file):
  #     logging.error(
  #           "ERROR: No HTML file '{}' found! You may need to export HTML from InDesign before proceeding.".format(
  #             html_file))
  #   if not os.path.exists(azure_md):
  #     logging.error(
  #           "ERROR: No Azure-formatted markdown file '{}' found! You may need to run the 'rootstalk_azure_media' scripts before proceeding.".format(
  #             azure_md))
        
  # Everything is in place, read the year-term.yml file...
  with file:
    try:
      yml = yaml.safe_load(file)
    except yaml.YAMLError as exc:
      sys.exit(exc)
      
    for key, value in yml.items():
      logging.debug("{}: {}".format(key, value))
          
    # Read each article name/index and create a new article-name.md file if one does not already exist
    for name in yml["articles"]:
      md_path = '{}-web-resources/{}.md'.format(issue, name)
      logging.info("Creating article markdown file '{}'...".format(md_path))
      if os.path.exists(md_path):
        logging.warning("Markdown file '{}' already exists and will not be replaced! Be sure to move or remove the existing file if you wish to generate a new copy.".format(
                md_path))
      else:
        with open("{}-azure.md".format(issue), "r") as md:
          issue_md_content = md.read()
                
          # Customize the front matter before inserting it...
          fm = frontmatter.replace("index: ", "index: {}".format(name))\
            .replace("azure_dir: ", "azure_dir: rootstalk-{}".format(issue))\
            .replace("date: ", "date: '{}'".format(datetime.now().strftime('%d/%m/%Y %H:%M:%S')))\
            .replace("azure_header: ", "azure_header: {}-header.jpg".format(name))

          # Write the front matter and content to the article.md file
          with open(md_path, "w") as article_md:
            print(fm, file=article_md)
            print(issue_md_content, file=article_md)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  
  print('Number of arguments:', len(sys.argv), 'arguments.')
  print('Argument List:', str(sys.argv))
  
  if not len(sys.argv) == 3:
    sys.exit("ERROR: You must specify exactly 2 command line arguments, the YEAR and TERM to be processed.")

  year = sys.argv[1]
  term = sys.argv[2]
  issue = "{}-{}".format(year, term)

  FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
  logging.basicConfig(filename="{}.log".format(issue), level=logging.DEBUG, format=FORMAT)
  print("INFO: New logfile {}.log has been opened in the working directory.".format(issue))
  logging.info(datetime.now( ))

  if not os.path.exists("{}.yml".format(issue)):
    msg = "ERROR: No {}.yml YAML file found! You need to create this file if you wish to proceed with the {} issue!".format(issue, issue)
    logging.error(msg)
    sys.exit(msg)
    
  try:
    with open("{}.yml".format(issue), "r") as file:
      logging.info("{}.yml file found and opened.".format(issue))
      rootstalk_markdownify(issue)
      rootstalk_azure_media(issue)
      rootstalk_make_articles(issue, file)
      
  except Exception as e:
    logging.error(traceback.format_exc())
    sys.exit(e)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
