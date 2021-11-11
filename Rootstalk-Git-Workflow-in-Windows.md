# Rootstalk's Git Workflow in Windows

| Important: This Section is Pending Revision! |
| --- |
| This document is ***PENDING REVISION***.  An _Ubuntu_ virtual machine is NO LONGER REQUIRED nor is it recommended! |

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
