#Librerías a utilizar
import click
from os import listdir, environ, path
from os.path import isfile, join

__author__ = "Carlos Maldonado"

def readPath(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    click.echo('Se procederá a copiar los nombres de %d archivos...' % len(files))
    print(files)
    return files

def copyFilesInTextFile(files,name,path):
    print("Procederé a copiar los archivos en {} en: {}".format(name,path))

@click.command()
@click.argument('path_to_read', type=click.Path(exists=True))
@click.option('--name', '-n', help='El nombre del archivo txt donde se guardarán los nombres de los archivos analizados',
                type=click.File('wb'), default=click.File('result.txt'))
@click.option('--path', '-p', help='La ruta específica donde se guardará el archivo txt', type=click.Path(exists=True),
                default=path.join(path.join(environ['USERPROFILE']), 'Desktop') )
def main(path_to_read, name, path):
    #click.echo('El path a leer es: %s...' % path_to_read)
    copyFilesInTextFile(readPath(path_to_read),name,path)


if __name__ == "__main__":
    main()