# rootstalk-workflow
Python scripts and documentation for the _Rootstalk_ project web (and print) workflow.

## Rootstalk, the Publication

_Rootstalk: A Prairie Journal of Science, Culture and the Arts_ is an online, multi-media, interdisciplinary journal published under the aegis of the Center for Prairie Studies at Grinnell College.  The journal is published as part of _Digital.Grinnell_ at [https://rootstalk.grinnell.edu](https://rootstalk.grinnell.edu).  Students, alumni, staff, and faculty of the College have all been involved in creating _Rootstalk_.

<!--- This is a comment. 
Only the paragraph above has been edited to pick up Mark B's comments saved in an MS Word document.  Everything between the opening < bracket and closing > bracket should be visible only when editing this document.
-->

_Rootstalk_ was launched in Spring 2015 as the product of a two-semester course sequence on journal publishing supported by the Wilson Program in Enterprise and Leadership. A three-year grant from the College’s Innovation Fund will allow us to explore ways to sustain the journal and further discussion about the prairie region.

_Rootstalk_ publishes original essays, fiction, poetry, visual art, music, and video aimed at a general audience. We especially hope to publish contributions from people whose views are not normally seen or heard in public forums.

## Volumes, Issues, Articles and Extras
Each publication run of _Rootstalk_ is an `issue` consisting of several `articles` and `extras`.  An article is one or more contiguous pages of text and media (photos, illustrations, poetry, audio, video, etc.) authored by one or more named individuals.  Extras often include images without significant text that are distributed throughout each issue.  Issues are created in corresponding academic ***fall*** or ***spring*** terms.  The issues created in a single academic year make up one `volume`, commonly expressed as a roman numeral.

### Year-Term Identifiers
Each issue has a key identifier composed of the `year` and `term` in which its production was "created". Note that an issue that's created during one term may not be published until later, so we use the term in which the issue was created to generate an identifier of the form: ***year-term***.  For example, the issue "created" in the Spring term of the 2015-2016 academic year, and formally published in the summer of 2016, is identified as `2016-spring`.  Likewise, the preceding issue created in the Fall of that same academic year is identified as `2015-fall`.

| Important! |
| --- |
| The adoption of directory and file names prefixed by a ***year-term*** identifier is critical to the web workflow!  Adopt this naming convention early and use it throughout to smooth all phases of the process. |

### Issue Title
Each issue has a distinct `title` which refers to its volume, a reference to the academic year, along with an indication of its sequence in that volume.  Our previous example issues, `2015-fall` and `2016-spring`, have titles of `Volume II, Issue 1` and `Volume II, Issue 2`, respectively.

## The Print Edition
The print-edition of each _Rootstalk_ issue is created using &copy;[Adobe InDesign](https://www.adobe.com/products/indesign.html).  _InDesign_ output comes in two forms, an `.indd` file where the content and layout are stored for use exclusively within _InDesign_, and one or more `.pdf` files used to generate printed, paper copies.

The `.indd` file created for a particular issue should follow the ***year-term*** naming convention.  For example, the Spring 2015-2016 academic term's file should be named `2016-spring.indd`.  This naming convention is important because once the print publication is complete and "final", _InDesign_ will be used to export (see section below for details) the issue to a `.html` file and corresponding content directory.  By default, the generated file and directory will have the same name as the `.indd` file.  So, for example, exporting the `2016-spring.indd` file to HTML will create a new `2016-spring.html` file and corresponding `2016-spring-web-resources` directory.

## The Online/Web Edition
The online-edition of each _Rootstalk_ issue is published using &copy;[Hugo](https://gohugo.io) as part of the [Rootstalk website](https://rootstalk.grinnell.edu).  Each online issue is composed of several articles, and each article is represented by a single [Markdown](https://en.wikipedia.org/wiki/Markdown) file coupled with media files housed in one of three web-accessible cloud storage services including &copy;[Azure BLOB Storage](https://azure.microsoft.com/en-us/services/storage/blobs/).

| Suggested Best Practice: Use Two Screens and _Atom_ |
| --- |
| Experience suggests it is easiest to work on the online/web edition of _Rootstalk_ using two or more screens. Display the print-version PDF of an issue on one screen for quick and easy reference, and engage the text editor of your choice on the other screen when organizing and editing web content. &copy;[Atom](https://atom.io) has been the editor-of-choice for many _Rootstalk_ editors and developers. |

### Website Rules
We enforce a couple of rules to smooth the transition from print to our website:

  - All file and directory names should be lowercase with NO spaces.  We commonly use a dash (`-`) separator in place of blanks or spaces in file and directory names.
  - Files composing a particular issue should be prefixed with the ***year-term*** identifier of that issue, or grouped inside a subdirectory prefixed by that ***year-term*** identifier.
  - Files composing a particular article or collection of extras should be prefixed by either:
    - an author's name with their last name listed first,
    - a subject name, or
    - the _Rootstalk_ role of the author

These rules are demonstrated through examples provided in subsequent sections of this document.

## Website Workflow
The process of creating one online-edition issue from a corresponding print-edition of _Rootstalk_ can be summarized as follows:

  - Save a local copy of the issue's _InDesign_ `.indd` file on your local disk. Rename it to be of the form *year*-*term*`.indd` if necessary.  For example, the `2016-spring` issue's `.indd` file must be named `2016-spring.indd`.
  - Open the `.indd` file in _InDesign_ and choose menu selections `File` | `Export...` | `HTML` accepting all default options to export the issue to HTML format.
    - This step will generate a new HTML file of the form ***year-term***`.html` and a corresponding content subdirectory of the form ***year-term***`-web-resources`.  Both will appear in your working directory alongside the `.indd` file.  For example, exporting the `2016-spring` issue will produce a file named `2016-spring.html` and a subdirectory named `2016-spring-web-resources`.
    - The export operation will also attempt to open the new HTML export in your default browser.
    - Browse through the new HTML pages in your browser.
  - In your working directory, create a new YAML text file using the text editor of your choice. The file name must be of the form ***year-term***`.yml`.  For example, the `2016-spring` issue must have a corresponding YAML file named `2016-spring.yml`. The format/content of this YAML file is detailed in the next section.
  - Once the YAML file is complete and saved alongside the corresponding `.html` file, ask the website administrator (digital@grinnell.edu) to run their `rootstalk-workflow/main.py` script on it.
    - The administrator will run a command of the form: `python3 ~/GitHub/rootstalk-workflow/main.py year term`
    - The script will produce a pair of intermediate outputs and a series of new article `.md` files.  The administrator will provide you with the article `.md` files for subsequent editing.


  - In all phases of editing for the web it's suggested that the web-editor

### Exporting Print to HTML
The _InDesign_ menu/commands used for export to HTML are:
  - File
  - Export...
  - HTML
All default settings should be accepted.

### Issue YAML File
The generation of website content from an issue's HTML export is controlled by a single YAML data file with a name of the form ***year-term***`.yml`.  For example, creation of website content for the `spring-2016` issue will be controlled by a file named `spring-2016.yml`.  Such files must reside in the same subdirectory as the issue's `.html` file and `-web-resources` subdirectory.  So, for example, the `spring-2016` issue must have files like this in a common directory:

```
drwxr-xr-x   4 mcfatem  1278142703   128B Nov  8 07:21 2016-spring-web-resources
-rwxrwxrwx@  1 mcfatem  staff        410K Nov  8 07:21 2016-spring.html
-rwxrwxrwx@  1 mcfatem  staff         62M Nov  4 11:31 2016-spring.indd
-rw-r--r--   1 mcfatem  1278142703   325B Nov  3 13:32 2016-spring.yml
```

Note that in the example above, the `2016-spring.indd` file is NOT REQUIRED since the issue's `.html` and `-web-resources` have already been exported.  However, keeping the `.indd` file here does no harm.

| Important! |
| --- |
| An issue's YAML (`.yml`) file is extremely important!  **Consider creating this file very early in the process, perhaps even during the early creation of the print-edition of the issue.** |

#### Issue YAML File Structure
The structure of a ***year-term***`.yml` file can best be demonstrated in this example from `spring-2016`:

```yaml
year: 2016
term: spring
title: Volume II, Issue 2, Spring 2016
articles:
  - editor
  - arena
  - snow
  - birds
  - weeks
  - duncombe-mills
  - johnson
  - kaiser
  - kyaruzi
  - thomasch-1
  - kincaid
  - thomasch-2
  - carl
  - harris-love
  - herrnstadt
  - wannamaker
  - atmore
  - dubbeldbee-kuhn
  - jiminez
  - kuhn
```

The required YAML keys are, as shown:

  - `year:` - This key holds the 4-digit year in which the issue was created.
  - `term:` - This key holds the academic term in which the issue was created, either `spring` or `fall`.
  - `title` - This key holds the formal title of the issue.
  - `articles` - This key holds a list of unique article identifiers.
    - An article identifier must be unique within the issue and it can take on one of three possible forms:
      - An **author's name** listed as their last name followed optionally by other names or an integer to distinguish articles by the same author. Note that in the example above, the author named `thomasch` has two articles, so the values `thomasch-1` and `thomasch-2` are used to distinguish them.
      - The _Rootstalk_ **role of the author**, commonly a value of `editor` or `publisher`.
      - The **subject of an article**, like `birds` in the example above.  In this example issue the name `birds` is used to identify an a recurring article titled "Birds of the Prairie".

### The `main.py` Script
`main.py` is a Python v3 script designed to glean information from an issue's `.yml` and `.html` files to produce a collection of article `.md` files suitable to constructing the online/website copy of the issue.  The script does this in three stages:

  - First, the script will `markdownify` the issue's `.html` file using a Python library published in [https://github.com/matthewwithanm/python-markdownify](https://github.com/matthewwithanm/python-markdownify).  This portion of the process will generate a new [Markdown](https://en.wikipedia.org/wiki/Markdown) file with a `.md` extension, named for the issue's year and term.  For example, running `python3 ~/GitHub/rootstalk-workflow/main.py 2016 spring` will first produce a Markdown file named `./2016-spring.md`.

  - Next, the script will edit the new issue `.md` file to add information specific to _Rootstalk_, including the path of the _Rootstalk_ website's _Azure_ BLOB Storage containers.  This portion of the script produces an intermediate Markdown file with `-azure` appended to the filename, like `2016-spring-azure.md`, for example.  All media (images, audio and video clips, etc.) references from the issue's `.md` file are translated to syntax compatible with our _Azure_ BLOB Storage.  For instance, an entry from the `2016-spring.md` file like `![](2016-spring-web-resources/image/haybales_on_a_picnic.jpg)` into a statement like `{{% figure_azure pid="haybales_on_a_picnic.jpg" caption="" %}}` in `2016-spring-azure.md`. This portion of the process also removes reduntant whitespace and unnecessary elements to conserve disk space and simplify subsequent editing.

  - Finally, the script will open and read the issue's `.yml` file to create new article `.md` files, one for each of the articles identified in the `articles` list within the issue's `.yml` file. All of these article `.md` files will be created in the issue's corresponding `-web-resources` subdirectory.  For example, the `2016-spring.yml` file that appeared previously in this document will generate a set of article `.md` files like these:

```
╭─mcfatem@MAC02FK0XXQ05Q ~/Downloads/rootstalk-data/2016-spring-web-resources
╰─$ ls -alh
total 9600
drwxr-xr-x  24 mcfatem  1278142703   768B Nov  8 09:35 .
drwxr-xr-x@ 33 mcfatem  1278142703   1.0K Nov  8 09:35 ..
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 arena.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 atmore.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 birds.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 carl.md
drwxr-xr-x   3 mcfatem  1278142703    96B Nov  8 07:21 css
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 dubbeldbee-kuhn.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 duncombe-mills.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 editor.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 harris-love.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 herrnstadt.md
drwxr-xr-x  85 mcfatem  1278142703   2.7K Nov  8 07:21 image
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 jiminez.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 johnson.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 kaiser.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 kincaid.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 kuhn.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 kyaruzi.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 snow.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 thomasch-1.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 thomasch-2.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 wannamaker.md
-rw-r--r--   1 mcfatem  1278142703   237K Nov  8 09:35 weeks.md
```

Note that the `image` and `css` subdirectories shown above were created earlier by the _InDesign_ HTML export process.

#### `main.py` Will NOT Overwrite Existing Article `.md` Files!
It's important to note that the `main.py` script will NOT overwrite or replace any existing article `.md` files!  If you want to generate new article `.md` files you must remove older files from the issue's `-web-resources` subdirectory first!

#### Logfile Output
Each run of the `main.py` script will create a corresponding `.log` file, or append timestamped output to an existing logfile is one already exists in the working directory. The name of the logfile will include the `year` and `term` of the issue that was processed.  So, the `python3 ~/GitHub/rootstalk-workflow/main.py 2016 spring` example used above will create or append to a logfile named `2016-spring.log`.

The logfile from each run of `main.py` contains specific information about outcomes produced by the script, including a count of all blank lines it removed from the `.md` file, and an echo of any heading lines that were deemed unnecessary and subsequently removed.

### Article `.md` Structure
The structure of an individual article's `.md` file is documented below with an abridged sample taken from the `editor.md` file listed above.  Each file consists of _Hugo_ `frontmatter` followed by `content` in Markdown format.  **Important: Note that the `main.py` script cannot reliably distinguish one article in an issue from all others, so the `content` portion of every article `.md` file in an issue will initially be IDENTICAL.**  It is responsibility of the issue's web-editor to reduce each initial file to a single article using a series of cut-and-paste edit operations!

#### Frontmatter
_Hugo_ uses data expressed in YAML format at the top of an article to help with control of the corresponding web output.  A block of such data, called the `frontmatter`, must appear at the top of the file delimited by an opening and closing set of three dashes. The portion of our sample from `editor.md` looks like this:

```
---
title:
index: editor
description:
date: '08/11/2021 13:16:02'
draft: false
contributors:
  - role: author
    name:
    headshot:
    caption:
    bio: " "
  - role: photographer
    name:
    headshot:
    caption:
    bio: " "
articletype:
tags: [" "," "]
azure_dir: rootstalk-2016-spring
azure_headerimage:
---
```

Note that the `main.py` script has pre-populated the `index:`, `date:`, `draft:`, `azure_dir:`, `azure_headerimage:` keys in the frontmatter, and two "sample" `role:` keys under `contributors:`.  All other keys are left blank and must be completed by the issue's web-editor. Briefly, the pre-populated key|value pairs are:

  - index: - The article's unique identifier pulled from the `articles` list of the corresponding issue's `.yml` file.
  - date: - The date and time when the article `.md` file was generated.
  - draft: false - A pre-populated `draft` key.  Changing the value to `true` will cause the article to be temporarily ignored by _Hugo_.
  - contributors|role: - A pair of pre-populated keys, one for an 'author' of the piece, and another for a contributing 'photographer'.
  - azure_dir: - The name of the container in _Azure BLOB Storage_ where the article's media must be stored.
  - azure_headerimage: - The name of the article's "header image" file as it appears in the corresponding `azure_dir`.

Note that it is acceptable to add or remove `contributor:` elements, and it's acceptable to list more than one 'author', or other roles, per article when necessary.  Possible roles might include:  `artist`, `author`, `editor`, `illustrator`, `interviewer`, `photographer`, `poet`, `publisher` or any other reasonable term used to indicate a contributor's role.

#### Content
The content portion of the issue appears after the frontmatter and occupies the remainder of the article's `.md` file.  Initially the content will include **ALL of the Markdown** for the entire issue. **Again, it is responsibility of the issue's web-editor to reduce each initial file to a single article using a series of cut-and-paste (mostly CUT) operations!**

A significantly abridged sample of the content from `editor.md` looks like this:

```markdown
Untitled photo 97

Justin Hayworth

Editors’ Note

In our ongoing effort to inspire an appreciation for and experience with the prairie region, we invite you to enjoy our third issue of Rootstalk. We’ve assembled a wide-ranging collection of thought-provoking pieces, covering subjects from barn quilts (“Barn Quilts in Poweshiek County’) to bird-song (“Birds of the Prairie”), from the experiences of a youth new to the prairie (“What I Learned at the White Horse Ranch”) to the lifetime of experience garnered by those who’ve spent their lives in intimate contact with the land (“We Lived There Ourselves for Forty-some Years”). From undocumented immigration to water safety, the stories in this issue give you multiple themes and destinations to visit; we hope you’ll visit them all.

All of the pieces in this issue—poetry, essays, short stories, videos and digital art—share similar roots. In bringing them together, we’ve striven to create a synergy of science and art, and to promote meaningful dialogue. It’s worth mentioning that the team of diligent editors who put this content together is every bit as diverse as the authors. These students come from around the world. They have diverse academic backgrounds and areas of interest, and have come together around Rootstalk’s central idea: that nurturing a sense of place—in our case, a prairie place—is vital in our busy lives. It isn’t every day or everywhere that you get to see differences blend together so seamlessly—and richly.

Rootstalk Student Editors, Spring 2016

Back row from left: Kenneth Wee, Sarah Arena, Ben Brosseau, Ivy Kuhn, Emma Thomasch

Front row from left: Kate Strain, Ajuna Kyaruzi, Jane Carlson, Debbie Msekela, Rita Clark

{{% figure_azure pid="Rootstalk_students_crop.jpg" caption="" %}}

{{% figure_azure pid="story_IX.jpg" caption="" %}}

Story IX, photograph by Steven Herrnstadt

{{% figure_azure pid="AA_BikeaBee_JanaPortrait_02_(1).jpg" caption="" %}}

Jana Kinsman is a beekeeper and illustrator living in Chicago, IL. She has been beekeeping for five years, enjoys teaching and collaborating, and believes beekeeping is best when it’s shared with the community. When she isn’t keeping bees, she’s traveling by train or bike to nature-filled destinations, or sending emails and petting her roommate’s dog.

This piece was written based on an interview with Jana Kinsman, founder of Bike a Bee. More information about Bike a Bee can be found at its website: [www.bikeabee.com](http://www.bikeabee.com), or Facebook page: [www.facebook.com/bikeabee](http://www.facebook.com/bikeabee).

Photo courtesy of Adam Alexander
```

Note that in this sample there are paragraphs of text and media references **not related** to the `editor` article, both before and after the relevant information!  The unrelated information must be removed by the issue's web-editor.

# Rootstalk's Git Workflow in Windows

| Important: This Section is Pending Revision! |
| --- |
| The remainder of this document is ***PENDING REVISION***.  An _Ubuntu_ virtual machine is NO LONGER REQUIRED nor is it recommended! |

This workflow assumes you are working in a non-Mac environment, like Windows, and that you have an Ubuntu virtual machine installed and running in that environment.  Additional sections of this document may provide guidance for one-time tasks or optional configuration activities.

## Cloning the Repository

In order to work effectively on _Rootstalk_ content or code, you should have a "local" copy of the project inside your Ubuntu virtual machine.  To set that up, one time only, use `git clone` like so:

- Open a terminal into your Ubuntu virtual machine.
- Navigate to a directory where you will house local copies of _GitHub_ work.  I suggest creating a directory named `GitHub` for this purpose.  
  - If you already have a `GitHub` directory do this:
    - `cd GitHub`
  - If you don't yet have a `GitHub` directory you can create one and navigate to it using:
    - `mkdir GitHub; cd GitHub`
- Clone our GitHub repository.  Note that if you already have a `GitHub/rootstalk` directory this command will do no harm. If you don't yet have a `GitHub/rootstalk` directory this command will create one.  A valid _GitHub_ user account and authentication will be required to complete this step.
  - `git clone https://github.com/Digital-Grinnell/rootstalk.git`
- If all goes well the above command will have created a `GitHub/rootstalk` working directory populated with our project's content.

## The `main` Branch

Unless you take other action, by default you will be working in the `main` branch of the repository.  This is NOT recommended since any changes committed and pushed to `main` will be automatically reflected in our DEV website at https://icy-tree-020380010.azurestaticapps.net.  It is best if you routinely work in your own branch of the repository and the next section will guide you to do so.  

## Your Own Branch of the Repository

As mentioned above, it's best if you routinely work in your own copy or branch of the repository to avoid committing changes that might conflict with the effort of other collaborators.  It's suggested that you create your own branch using your last name as its identifier.  I've create such a branch for myself like so:

  - `cd GitHub/rootstalk`
  - `git pull`   <-- This is an essential step to guarantee that I'm starting with an up-to-date copy of the repo!
  - `git checkout -b mcfate`  <-- `mcfate` is the name of my new local branch
    - If there's already a local branch by this name you may see a fatal message like this: `fatal: A branch named 'mcfate' already exists.`  Don't worry, no harm done.  You can simply "activate" that existing branch using `git checkout mcfate`, without the `-b` flag.

## Routine/Daily Workflow

It's a good idea to follow this workflow for each routine or daily work session.  ALWAYS replace the example branch name, `mcfate`, with the name of YOUR branch!

- Open a terminal into your Ubuntu virtual machine.
- Navigate to your `rootstalk` source folder, something like `cd GitHub/rootstalk`.
- Check your project status with `git`, like so: `git status; git remote -v`
  - `git remote -v` output should be this:
      ```
      origin	https://github.com/Digital-Grinnell/rootstalk.git (fetch)
      origin	https://github.com/Digital-Grinnell/rootstalk.git (push)
      ```
  - `git status` should return no changes, but if it does that's OK too.
- Pull the latest changes, like so: `git pull origin mcfate`
- Check out your branch of the repo, like so: `git checkout mcfate`.
- Launch `hugo server` and in your browser visit the local site at `https://localhost:1313` to see your work
- Edit in necessary changes, mostly in `./content`.  As you **save changes** your local site should update automatically
- When your edits are complete and tested, commit them and create a `pull request` back to GitHub, like so:
  - `git add .`  This will stage any changes you have made to be committed
  - `git commit -m "brief unique message"`  Commits your changes with an attached message
  - `git push origin -u mcfate`  <-- be sure to replace `mcfate` with YOUR branch name

  | Suggestion: Temporarily Tag New Articles as `featured` |
  | --- |
  | You can make your work easier to access when testing the _Rootstalk_ site locally or in your "branch" version of the site, just add a `featured` tag to a new article, by inserting `tags: ["featured"]` in its frontmatter. Doing so will make the article appear prominently (and conveniently) on the site's "home" page.  8^) Just be sure to remove that tag before pushing to production, assuming it is not needed there. |

## Deploying YOUR Branch of the Repository

It's nice to have an automatically deployed copy of your work on the web for review by others.  To accommodate that I can help set this up in _Azure_, or elsewhere.  The key is to have YOUR branch of the repo pushed to _GitHub_ with an _Azure_ static web app configured to YOUR branch.

To demonstrate and document how that happens I'll create a branch named `gokcebel` and deploy it. Without repeating many of the details shown above...

```
cd ~/GitHub/rootstalk
git pull
git checkout -b gokcebel
atom .   <-- on my workstation this opens the new branch of the project in my Atom editor
```

At this point I made changes to this document and saved them in _Atom_.

```
git status  
```
The `git status` command returned this:

```
╭─mcfatem@MAC02FK0XXQ05Q ~/GitHub/rootstalk ‹gokcebel›
╰─$ git status                      
On branch gokcebel
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   Git-Workflow-in-Windows.md

no changes added to commit (use "git add" and/or "git commit -a")
```

So I follow up with...

```
git add .
git commit -m "Creating the gokcebel branch"
git push origin -u gokcebel
```

Now that the `gokcebel` branch exists in _GitHub_, I'll visit my _Azure_ dashboard and link it to a new deployment. There's an article in my blog, [Moving Static Sites to Azure](https://ashy-hill-086e62810.azurestaticapps.net/posts/109-moving-static-sites-to-azure/), that describes this process in some detail.

The outcome of this deployment can be seen at https://delightful-stone-01bd98310.azurestaticapps.net.  Furthermore, any changes pushed to the `gokcebel` branch of the repository in _GitHub_ should trigger an updated deployment to this address! Since _Hugo_ is soooooooooo fast the update should be available in under 5 minutes.  If you check for an update in your browser please be sure to **refresh** your window so you get the latest content.

### Routine Workflow Example

When I open https://delightful-stone-01bd98310.azurestaticapps.net in my browser now I see the site with a "title" of "Rootstalk - DEV on Azure".  This string exists in the `config.toml` file.  To demonstrate the entire workflow from start-to-finish I'm going to change that text in the `gokcebel` branch to read "Rootstalk - gokcebel on Azure".

```
cd ~/GitHub/rootstalk
git pull
git checkout gokcebel
nano ./config.toml      <-- opens only the named file for editing.  Once edits are complete...
git add .
git commit -m "Changed site title to 'Rootstalk - gokcebel on Azure'"
git push origin gokcebel
```

Note that because the `gokcebel` branch already exists I was able to omit the `-b` flag on `git checkout...` and the `-u` option on `git push...`.

After a few minutes I'm able to open https://delightful-stone-01bd98310.azurestaticapps.net in my browser where I now see the site with a "title" of "Rootstalk - gokcebel on Azure"!

# Resources

A nice concise guide to using `git` can be found at [https://rogerdudler.github.io/git-guide/](https://rogerdudler.github.io/git-guide/).
Mark's blog post, [Collaborating on Hugo Site Development](https://static.grinnell.edu/blogs/McFateM/posts/095-collaborating-on-hugo-site-development/), could also prove helpful.
