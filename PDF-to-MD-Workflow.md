Working with .md files on Atom:  

All the pieces belonging to the issue will exist in a .pending folder.  

Copy any piece [say `article.md`] from `.pending` folder and paste in the vol-x-issue-x folder (outside `.pending`).  

Rename the old file inside the pending folder to `article-pending.md`.

Use CTRL/Command + F to navigate to the author’s/piece’s name on issue PDF. Find the beginning and the ending of the article/piece (use rootstalk.grinnell.edu).  

Open the article markdown (article.md) on Atom text editor. All unedited markdown files include the entire content.  

Using the PDF as a guide, delete all content before and following the article/piece. BEWARE that pictures included in the article may precede the article text, or might be at the very end.  

Most text will already be formatted, yet still need to be checked. Using the pdf as a guide, check that:  

  - Header images,
  - headshot images,
  - title,  
  - name of author/other contributors  

are filled on the front matter.  

Tags in quote marks are added: [“essay”, “interview”, “photography”] etc.  

Figure formats are preserved:  

  `{{% figure_azure pid="Mustard_Seed_Farm_1.jpg" alt="This is a picture of the Mustard Seed Community Farm, in a farmland" %}}`  

Pull quotes have the proper formatting:  

  `{{% pullquote %}} Text to be shown {{% /pullquote %}}`  

There is a leaf bug at the end of the text:

  `{{% leaf-bug %}}`  

Pushing Changes onto the Website (For Windows Users)  

On Windows Powershell, use the following commands to ensure all the content is up to date and ready to be pushed:  

  - `git pull`  

** Before pushing any changes, I like to run `hugo server` to see if there are any mistakes on the website.  

  - `git add .`
  - `git commit -m “Made x changes on x file”`
  - `git push`
