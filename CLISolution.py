#Librerías a utilizar
import click

__author__ = "Carlos Maldonado"

@click.command()
@click.argument('filename')
@click.option('-n')
def main(filename, n):
    click.echo('El filename es: %s' % filename)
    if n:
        click.echo('Hola %s' % n)

if __name__ == "__main__":
    main()