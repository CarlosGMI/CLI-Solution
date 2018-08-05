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
    try:
        textFile = open(join(path,name),'w')
        textFile.write("Estoy escribiendo en un txt :D")
        textFile.close()
    except:
        raise click.ClickException("Ha ocurrido algún error durante la creación del archivo")
        
def validateNameFile(ctx, param, value):
    if not value.endswith('.txt'):
        raise click.BadParameter('El nombre del archivo debe ser .txt')
    else:
        return value


@click.command()
@click.argument('path_to_read', type=click.Path(exists=True))
@click.option('--name', '-n', help='El nombre del archivo txt donde se guardarán los nombres de los archivos analizados. Por defecto el nombre es "result.txt"',
                default='result.txt', callback=validateNameFile)
@click.option('--path', '-p', help='La ruta específica donde se guardará el archivo txt. Por defecto la ruta es en el escritorio', type=click.Path(exists=True, file_okay=False),
                default=path.join(path.join(environ['USERPROFILE']), 'Desktop'))
def main(path_to_read, name, path):
    copyFilesInTextFile(readPath(path_to_read),name,path)


if __name__ == "__main__":
    main()