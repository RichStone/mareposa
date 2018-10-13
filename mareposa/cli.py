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
def create(locally, github_repo, gh_user, repo_name):
    if locally is False and github_repo is False:
        click.echo('Create new repository locally, remotely or both? For more information type `mareposa create --help`')
    else:
        # if locally:
        #     bash_execute(['git', 'init'], ['git', 'add', '.'], ['git', 'commit', '-m"start project"'])
        if github_repo:
            if gh_user and repo_name:
                bash_execute(['curl', '-u', gh_user, 'https://api.github.com/user/repos', '-d', '{"name":"' + repo_name + '"}'])
            else:
                click.echo('Sorry, some parameters are missing.\n '
                           'Please provide all of these options when you plan to create a new remote GitHub repository:\n '
                           '--gh-user\n '
                           '--repo-name')


def bash_execute(*commands):
    for command in commands:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        click.echo(output)
        process.terminate()


if __name__ == '__main__':
    main()
