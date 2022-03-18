# Git/Atom/Hugo Configuration in Windows

The document provides a procedure for the installation and configuration, on a Windows 10 platform, of the three tools needed to effectively edit and publish _Rootstalk_ content.  The tools are:

  - Hugo - See the [Hugo](https://gohugo.io) project homepage for reference, instruction and download links.
  - Atom - See the [Atom](https://atom.io) project homepage for reference, instruction and download links.
  - Git - See the [Git](https://git-scm.com) project homepage and http://git-scm.com/download/win for download instructions.

I used the linked resources in mid-March 2022 to successfully install and configure the necessary workflow environment on a Windows 10 desktop computer.  

## Installation Sequence

The recommended installation sequence is:

  - `Hugo` - The easiest of the three to install (because it's just an executable) so let's tackle it first.
  - `Atom` - Should be installed before `git` to provide easy and seamless integration of the two packages.
  - `Git` - Should be installed only after `Atom` is working.  This is the most involved installation of the three so let's save it for the end.

### Hugo

_Hugo_ is the static web compiler/environment/platform that we use to publish the _Rootstalk_ website.  The production instance of [Rootstalk](https://rootstalk.grinnell.edu) is deployed into a _DigitalOcean_ host that runs _Hugo_ for us.  We also have development and testing instances of _Rootstalk_, like [our DEV instance](https://icy-tree-020380010.azurestaticapps.net) running on an _Azure_ host.  But perhaps the most powerful feature of _Hugo_ is that you can edit content locally on your workstation and preview it locally as well, that is, if you have it installed and working locally!

The following screen photos show the steps I've taken to install _Hugo_ on a Windows 10 workstation.

  - Follow the "Less technical users" portion of [this Windows installation tutorial](https://bwaycer.github.io/hugo_tutorial.hugo/tutorials/installing-on-windows/) as shown in the image below.

  - In my case the Windows machine was one that's owned/managed by Grinnell College, so I choose to install _Hugo_ on my home `G:` drive, not `C:`.  This seemed to really help with most user-permissions issues.

  - Step 7 in the install tutorial prompts you to change the `Path` environment variable **in the User variables section**, but if the Windows machine is managed by someone else, like Grinnell College ITS, then you will need to make sure you change the `Path` variable **in the administrator section** so that the change is visible to ALL users, including yourself!  _Note that You will need "admin rights" on your workstation in order to change the administrator `Path`!_

![Hugo Install Tutorial for Windows](./assets/images/IMG_0122.png)

  - Choose the latest Windows-64bit .zip archive as I did below.

![Choose the Latest Windows-64bit Zip File](./assets/images/IMG_0123.png)

  - Open the download to install it.

![Choose the Latest Windows-64bit Zip File](./assets/images/IMG_0124.png)

### Atom

_Atom_ is the open source editor-of-choice for the _Rootstalk_ team (and countless others), largely because it's awesome and works on virtually any workstation.

The following screen photos show the steps I've taken to install _Atom_ on a Windows 10 workstation.

  - Visit [the Atom home page](https:atom.io) and click the `Download` button as shown below.

![Atom Home Page with Download](./assets/images/IMG_0106.png)

  - Open the download to install it.

![Open the Download To Install It](./assets/images/IMG_0110.png)

  - Since my Windows machine was managed by the college, I got lots of errors and the installation failed as you can see below.

![Oops...What If There's An Error](./assets/images/IMG_0108.png)

  - If there were errors, try opening the download and "Run as administrator".  That worked for me.

![Run As Administrator](./assets/images/IMG_0109.png)

### Git

_Git_ is the distributed version control software that the _Rootstalk_ team (and countless others) use to manage the project.  Unfortunately for Windows users, _git_ was written to work natively in Linux, so setup in Windows requires a bit of work.

The following screen photos show the steps I've taken to install _Git_, and related tools, on a Windows 10 workstation.

  - Begin by opening [the `git` Download for Windows page](https://git-scm.com/download/win) and responding as in the images posted below.

![text](./assets/images/IMG_0100.png)
![text](./assets/images/IMG_0101.png)
![text](./assets/images/IMG_0102.png)
![text](./assets/images/IMG_0103.png)
![text](./assets/images/IMG_0104.png)

  - Note that if you haven't already installed _Atom_ you will see that it cannot be selected as your default editor.  In that case you need to backup a bit and get _Atom_ installed, then return here.

![text](./assets/images/IMG_0105.png)

- If you previously installed _Atom_ then you should see it as a valid choice for integration with `git`.  

![text](./assets/images/IMG_0111.png)

![text](./assets/images/IMG_0112.png)
