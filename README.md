# Product Name
> la maREPOsa automates creation of your remote GitHub & local git repositories, gitignore and README.md in one single line of code.

[![PyPI version](https://badge.fury.io/py/mareposa.svg)](https://badge.fury.io/py/mareposa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<a href="https://flattr.com/submit/auto?user_id=datagoodie&url=https%3A%2F%2Fgithub.com%2FRichStone%2Fmareposa" target="_blank"><img src="https://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0"></a>

Almost every developer, who works with git, executes a certain algorithm, probably hundreds of times throughout his career, to create projects. The goal of maREPOsa is to replace this algorithm with one terminal command.

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

You might also want to generate a .gitignore file by going to [gitignore.io](https://gitignore.io) and look for a README.md template for your project. You see the tremendous work and web surfing you have to invest for setting up a project.

#### The new algorithm
```bash
# do this once
pip install mareposa

# do for example this the rest of your life
mareposa create -g -l --gh-user USER_NAME --repo-name REPO_NAME --ignore python,pycharm,linux --readme detailed
```

But you can also use maREPOsa e.g. to only create a configured .gitignore file or a README.md template.

![](header.png)

## Installation

OS X & Linux & Windows:

The installation should be the same for everyone but by now it was only tested on Windows:

```bash
pip install mareposa
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/stonerichio) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/RichStone/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Future Features Ideas
- Feature One
- Feature Two

## Neccessary Refactorings
- refactor this 
- refactor that

Use **Future Features** and **Neccessary Refactorings** rather sparingly and only as long as collaboration and project size are overseeable.

## Code Metrics
Let people know how you worked on this project.
- How did you plan it?
- How much time did it take?
- What was easy, where did you struggle?
e.g.: [this project](https://datagoodie.com/blog/introducing-data-collection-tool/)

*this README.md template was originally created by [Dan Bader](https://twitter.com/dbader_org) and extend by [RichStone](https://github.com/RichStone/)*

*An example project that uses this extensive template is my [data collection tool](https://github.com/RichStone/data-collection-download-tool)*

> let me know if you need any translations of the template.

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
