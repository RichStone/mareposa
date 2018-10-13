import subprocess
import click


@click.group()
def main():
    """Fla maREPOsa allows you to go through all the initiation process of new git/GitHub projects with just a single terminal command."""
    pass


@main.group()
def mareposa():
    pass


@mareposa.command()
@click.option('-l', '--locally', is_flag=True, help='Create a git repository locally and commit all existing files.')
def create(locally):
    if locally is False:
        click.echo('Please decide if you want to create a local repository and commit your files.')
    else:
        # bash_execute('git init', 'git add .', 'git commit -m\"start project\"')
        bash_execute(['git', 'init'], ['git', 'add', '.'], ['git', 'commit', '-m"start project"'])


def bash_execute(*commands):
    for command in commands:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        process.terminate()


if __name__ == '__main__':
    main()
