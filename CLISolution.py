#Librerías a utilizar
import click
from os import listdir, environ, path
from os.path import isfile, join, exists

__author__ = "Carlos Maldonado"

def readPath(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if len(files) == 0:
        raise click.ClickException('La ruta especificada por usted no contiene ningún archivo o está compuesta por otras carpetas')
    else:
        click.echo('Se procederá a copiar los nombres de %d archivos...' % len(files))
        #print(files)
        return files

def copyFilesInTextFile(files,name,path):
    #print("Procederé a copiar los archivos en {} en: {}".format(name,path))
    try:
        textFile = open(join(path,name),'w')
        with click.progressbar(files) as bar:
            for f in bar:
                textFile.write(f+'\n')
        textFile.close()
    except:
        raise click.ClickException("Ha ocurrido algún error durante la creación del archivo")
        
def validateFile(path, name):
    if not name.endswith('.txt'):
        raise click.BadParameter('El nombre del archivo debe ser .txt')
    else:
        if exists(join(path,name)):
            raise click.ClickException('{} ya existe en {}'.format(name,path))
        else:
            return(path,name)

@click.command()
@click.argument('path_to_read', type=click.Path(exists=True))
@click.option('--name', '-n', help='El nombre del archivo txt donde se guardarán los nombres de los archivos analizados. Por defecto el nombre es "result.txt"',
                default='result.txt')
@click.option('--path', '-p', help='La ruta específica donde se guardará el archivo txt. Por defecto la ruta es en el escritorio', type=click.Path(exists=True, file_okay=False),
                default=path.join(path.join(environ['USERPROFILE']), 'Desktop'))
def main(path_to_read, name, path):
    validateFile(path, name)
    copyFilesInTextFile(readPath(path_to_read),name,path)


if __name__ == "__main__":
    main()