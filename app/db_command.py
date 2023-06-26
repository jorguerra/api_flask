import click
import subprocess

@click.command('migrate')
def migrate_command():
    cmd = subprocess.Popen(["alembic","upgrade","head"], stdout=subprocess.PIPE)
    click.echo(cmd.communicate()[0])

def init_app(app):
    app.cli.add_command(migrate_command)