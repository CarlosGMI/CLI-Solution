#Librerías a utilizar
import click
import eyed3
from eyed3 import mp3
import errno
from os import listdir, environ, path
from os.path import isfile, join, exists

__author__ = "Carlos Maldonado"

#Lee el path dado por el usuario y lo transforma en un array con solo los nombres de los archivos conseguidos en ese path
#PARÁMETROS:
# - path: El path o la ruta del directorio a leer.
#RETURNS: El array con los nombres de los archivos en path.
def readPath(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    if len(files) == 0:
        raise click.ClickException('La ruta especificada por usted no contiene ningún archivo o está compuesta por otras carpetas')
    else:
        click.echo('Se procederá a copiar los nombres de %d archivos...' % len(files))
        return files

#Dado el array con los nombres de los archivos en el path, se separan en 2 arrays que contienen los archivos .mp3 y .* respectivamente
#PARÁMETROS:
# - path: El path o la ruta del directorio a leer.
# - files: El array con los nombres de los archivos del path.
#RETURNS: Los 2 arrays creados para separar los tipos de archivos.
def separateFileExtension(path,files):
    otherFiles = []
    mp3Files = []
    for f in files:
        if f.endswith('.mp3'):
            mp3Files.append(f)
        else:
            otherFiles.append(f)
    return(mp3Files,otherFiles)

def copyFilesInTextFile(pathToRead,files,name,path):
    try:
        textFile = open(join(path,name),'w')
        mp3Files, otherFiles = separateFileExtension(pathToRead,files)
        textFile.write('==========================================CANCIONES==========================================\n')
        for f in mp3Files:
            audio = eyed3.load(join(pathToRead,f))
            textFile.write('  - Nombre del archivo: '+f+'\n')
            if audio.tag.title:
                textFile.write('  - Titulo: '+audio.tag.title+'\n')
            else:
                textFile.write('  - Titulo: --\n')
            if audio.tag.artist:
                textFile.write('  - Artista: '+audio.tag.artist+'\n')
            else:
                textFile.write('  - Artista: --\n')
            textFile.write('=================================================================================\n')
        textFile.write('========================================OTROS ARCHIVOS=======================================\n')
        for o in otherFiles:
            textFile.write('  - Nombre del archivo: '+o+'\n')
        textFile.close()
    except IOError as e:
        if e.errno == errno.EACCES:
            raise click.ClickException('No tienes permiso de escritura en {}'.format(path))
        elif e.errno == errno.EIO:
            raise click.ClickException('{} está protegido contra escritura'.format(path))
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
    """Este script toma la ruta de algun directorio (PATH_TO_READ) y lee todos los archivos que ahi se encuentran para posteriormente copiar sus
    nombres en un archivo de texto (.txt) (-n) y guardarlo en una ruta (-p). Este archivo de texto puede ser especificado asi como la ruta 
    donde puede guardarlo.

    PATH_TO_READ: path o ruta del directorio que desea analizar -- En caso de que desee analizar un path con espacios de por medio recuerde colocar
    "path" i.e. "cliS C:\\folder with spaces\\" """
    validateFile(path, name)
    copyFilesInTextFile(path_to_read,readPath(path_to_read),name,path)


if __name__ == "__main__":
    main()