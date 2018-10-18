import os
import subprocess
import click


@click.group()
def main():
    """la maREPOsa allows you to go through all the initiation process of new git/GitHub projects with just a single terminal command."""
    pass


@main.group()
def mareposa():
    pass


@mareposa.command()
@click.option('-g', '--github-repo', is_flag=True,
              help='Create a remote repository on GitHub.\n '
                   'To create a new remote GitHub repo, please provide your registered\n --gh-user (GitHub username)\n and\n your new --repo-name')
@click.option('-l', '--locally', is_flag=True, help='Initiate a git repository locally, commit, and push all existing files of the current directory with the commit message "start project".')
@click.option('--gh-user', default=None, help='User name of the owner of the new ')
@click.option('--repo-name', help='Your new repository name.')
@click.option('-i', '--ignore', help='Create a .gitignore file with files and names to ignore. '
                                     'Provide the technologies to ignore separated by come, e.g. eclipse,java etc. '
                                     'For full list of possible technologies refer to `mareposa info --ignore-list`. '
                                     'Please check the .gitignore file thoroughly to know exactly what will be ignored.')
@click.option('-r', '--readme', type=click.Choice(['blank', 'light', 'detailed']), help='Create a README.md')
def create(locally, github_repo, gh_user, repo_name, ignore, readme):
    if ignore:
        ignorables = ignore.split(',')
        for technology in ignorables:
            url = 'https://www.gitignore.io/api/' + technology
            bash_execute_curl(url, options='-s', append_command=' >> .gitignore')
    if readme:
        bash_create_readme(readme)
    if locally is False and github_repo is False:
        click.echo('Create new repository locally, remotely or both? For more information type `mareposa create --help`')
    else:
        if github_repo:
            if gh_user and repo_name:
                bash_execute(['curl', '-u', gh_user, 'https://api.github.com/user/repos', '-d', '{"name":"' + repo_name + '"}'])
            else:
                click.echo('Sorry, some parameters are missing.\n '
                           'Please provide all of these options when you plan to create a new remote GitHub repository:\n '
                           '--gh-user\n '
                           '--repo-name')
        if locally:
            if os.path.exists('.git'):
                click.echo('--locally will not be executed because a .git folder already exists in this directory.')
            else:
                if gh_user and repo_name:
                    bash_execute(['git', 'init'],
                                 ['git', 'add', '.'],
                                 ['git', 'commit', '-m"start project"']
                                 )
                    bash_execute_shell('git remote add origin https://github.com/' + gh_user + '/' + repo_name)
                    bash_execute_shell('git push -u origin master')
                else:
                    click.echo('Please provide --gh-user and --repo-name because we will push it up directly.')


@mareposa.command()
@click.option('--show-ignore-list', is_flag=True, help='Show all possible operating systems, programming languages and IDE input types that can be ignored in .gitignore')
def info(show_ignore_list):
    if show_ignore_list:
        bash_execute(['curl', '-s', 'https://www.gitignore.io/api/list'])


def bash_execute(*commands):
    for command in commands:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        process.wait()
        output, error = process.communicate()
        click.echo(output)
        process.terminate()


def bash_execute_curl(url, options='', append_command=''):
    """
    # Popen together with curl cannot deal with chaining `>>` to curl commands, that's why shell=True is used for subprocess.Popen
    # check if shell=True is not to be used everywhere
    :param technology: technologies to ignore separated by come, e.g. eclipse,java etc. For full list of possible technologies refer to --ignore-list. '
    """
    process = subprocess.Popen('curl ' + options + ' ' + url + ' ' + append_command, shell=True)
    process.wait()
    process.terminate()


def bash_execute_shell(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
    process.terminate()


def bash_create_readme(readme):
    if readme == 'light':
        bash_execute_curl('https://raw.githubusercontent.com/RichStone/readme-template/master/types/light-README.md', '-o README.md')
    elif readme == 'detailed':
        bash_execute_curl('https://raw.githubusercontent.com/RichStone/readme-template/master/README.md', '-o "README.md"')
    elif readme == 'blank':
        bash_execute(['touch', 'README.md'])


if __name__ == '__main__':
    main()
