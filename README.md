# Product Name
> la maREPOsa automates creation of your remote GitHub & local git repositories, gitignore and README.md in one single line of code.

[![PyPI version](https://badge.fury.io/py/mareposa.svg)](https://badge.fury.io/py/mareposa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<a href="https://flattr.com/submit/auto?user_id=datagoodie&url=https%3A%2F%2Fgithub.com%2FRichStone%2Fmareposa" target="_blank"><img src="https://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0"></a>

![](header.jpg)

Almost every developer, who works with git, executes a certain algorithm to create projects. 
Probably hundreds of times throughout his career. 
The goal of maREPOsa is to replace this algorithm with one terminal command.

#### The old algorithm
```bash
- go to GitHub
- create project

# assuming that you already have files in your project's directory
- git init 
- git add .
- git commit -m"start project"
- git remote add origin https://github.com/USER/REPO
```

You might also want to generate a `.gitignore` file by going to [www.gitignore.io](https://www.gitignore.io) and look for a `README.md` template for your project. 
You see the tremendous work and web surfing you have to invest for setting up a project.

#### The new algorithm
```bash
# do this once
pip install mareposa

# do for example this the rest of your life
mareposa create -g -l --gh-user USER_NAME --repo-name REPO_NAME --ignore python,pycharm,linux --readme detailed
```

But you can also use maREPOsa e.g. to only create a configured `.gitignore` file or a `README.md` template.

## Installation

OS X & Linux & Windows:

The installation should be the same for everyone but by now it was only tested on OS X:

```bash
pip install mareposa
```

## Usage

To get an overview what mareposa can, start of with ...

```bash
$ mareposa create --help
```
```
areposa create --help
Usage: mareposa create [OPTIONS]

Options:
  -l, --locally                   Initiate a git repository locally and commit
                                  all existing files of the current directory.
  -g, --github-repo               Create a remote repository on GitHub. To
                                  create a new remote GitHub repo, please
                                  provide your registered --gh-user (GitHub
                                  username) and your new --repo-name
  --gh-user TEXT                  User name of the owner of the new
  --repo-name TEXT                Your new repository name.
  -i, --ignore TEXT               Create a .gitignore file with files and
                                  names to ignore. Provide the technologies to
                                  ignore separated by come, e.g. eclipse,java
                                  etc. For full list of possible technologies
                                  refer to `mareposa info --ignore-list`.
                                  Please check the .gitignore file thoroughly
                                  to know exactly what will be ignored.
  -r, --readme [blank|light|detailed]
                                  Create a README.md
  --help                          Show this message and exit.
```

Now you can for example do the complete initialization of your project in just one step:
```bash
$ mareposa create --github-repo --locally --gh-user USER_NAME --repo-name REPO_NAME --ignore python,pycharm,linux --readme detailed
```

You can also just generate a `.gitignore` file if you already have a project:
```
# create a .gitignore file with default ignorables from https://www.gitignore.io for the technologies you plan to work with
$ mareposa create --ignore python,pycharm,linux
```

Create a verbose README template, like the one you are reading right now:
```
$ mareposa create --readme detailed
```

Or just create a blank one to fill it later
```
$ mareposa create --readme blank
```

If you have already created a remote repo, you can also just add-commit-push:
```
$ mareposa create --locally --gh-user GUTHUB_USER_NAME --repo-name YOUR_REPO
```

**Please be aware that maREPOsa is in its early beta phase and can generate unexpected behaviour. 
The functionality has still to be tested on Windows and Linux.**

‼️
> Don't run `mareposa create --locally` by mistake in some existing repo as it will add-commit-push automatically.  

## Development setup if you like to contribute

Consider installing pipsi to install maREPOsa. It is another kind of `pip`. 
It will automatically install maREPOsa and its isolated venv dependencies in your /Users/USER_NAME/.local/ directory.

Here are the [installation instructions for pipsi](https://github.com/mitsuhiko/pipsi#readme).

If you installed maREPOsa with `pip` already, you may want to uninstall it first.

With pipsi you can then easily install maREPOsa locally and build the application after changes if you need:
```
git clone https://github.com/RichStone/mareposa
cd mareposa
pipsi install --editable .

# sometimes you will make some changes that need a fresh install of maREPOsa
# MAKE SICK CHANGES
# reinstall maREPOsa

pipsi uninstall maREPOsa
pipsi install --editable .
```
You may also be able to do all of this by just using `pip` but this is how my workflow was and I found it quite handy.

‼️
> Don't run `mareposa create --locally` by mistake in some existing repo as it will add-commit-push automatically.  

## Release History

* 1.0.0
    * ADD: Main functionallity
* 0.2.0
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/stonerichio) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/RichStone/)

## Future Features and Enhancements Ideas

> just some ideas and necessities that popped into my mind

- add license option
- add `mareposa push/-p -m “your new commit message”` command for git add-commit-push
- automate `mkdir new-project && cd new-project`
- prompt user if a .git repo/remote upstream already exists locally
- catch failed pushes
- summarize what was successful (and what maybe failed) as feedback for the user
- Fancy Welcome screen
- more detailed text on create command without locally or remotely?
- better visuals 
- set credentials
- set default license
- set default ignores
- set message, if no gitignore technology available
- Set your own default README.md

> let me know in the issues if you have new ideas or want some of the possible features interests you most at the moment.
