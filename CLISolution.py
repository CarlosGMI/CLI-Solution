#Librerías a utilizar
import click

__author__ = "Carlos Maldonado"

@click.command()
@click.argument('path_to_read')
@click.option('--name')
@click.option('--path')
def main(path_to_read, name, path):
    click.echo('El path a leer es: %s' % path_to_read)
    if name and path:
        click.echo('--name = %s' % name)
        click.echo('--path = %s' % path)

if __name__ == "__main__":
    main()