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
@click.option('-l', '--locally', is_flag=True, help='Initiate a git repository locally and commit all existing files of the current directory.')
@click.option('-g', '--github-repo', is_flag=True,
              help='Create a remote repository on GitHub. '
                   'To create a new remote GitHub repo, please provide your registered --gh-user (GitHub username) and your new --repo-name')
@click.option('--gh-user', default=None, help='User name of the owner of the new ')
@click.option('--repo-name', help='Your new repository name.')
@click.option('-i', '--ignore', help='Create a .gitignore file with files and names to ignore. '
                                     'Provide the technologies to ignore separated by come, e.g. eclipse,java etc. '
                                     'For full list of possible technologies refer to `mareposa info --ignore-list`. '
                                     'Please check the .gitignore file thoroughly to know exactly what will be ignored.')
def create(locally, github_repo, gh_user, repo_name, ignore):
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
            bash_execute(['git', 'init'], ['git', 'add', '.'], ['git', 'commit', '-m"start project"'])
    if ignore:
        ignorables = ignore.split(',')
        for technology in ignorables:
            bash_append_to_gitignore(technology)


@mareposa.command()
@click.option('--show-ignore-list', is_flag=True, help='Show all possible operating systems, programming languages and IDE input types that can be ignored in .gitignore')
def info(show_ignore_list):
    if show_ignore_list:
        bash_execute(['curl', '-s', 'https://www.gitignore.io/api/list'])


def bash_execute(*commands):
    for command in commands:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        click.echo(output)


def bash_append_to_gitignore(technology):
    """
    # Popen together with curl cannot deal with chaining `>>` to curl commands, that's why shell=True is used for subprocess.Popen
    # check if shell=True is not to be used everywhere
    :param technology: technologies to ignore separated by come, e.g. eclipse,java etc. For full list of possible technologies refer to --ignore-list. '
    """
    process = subprocess.Popen('curl https://www.gitignore.io/api/' + technology + ' >> .gitignore', shell=True)
    process.wait()
    process.terminate()


if __name__ == '__main__':
    main()
