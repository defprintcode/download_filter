import os
import time
import datetime
import shutil


def readdownload():
    home = os.path.expanduser("~")
    folder = os.path.join(home, "Downloads")
    old = folder + '\old'
    installers = old + '\Ejecutables'
    documents = old + '\Documentos'
    zipped = old + '\Comprimidos'
    with os.scandir(folder) as ficheros:
        for fichero in ficheros:

            if not os.path.isdir(old):
                os.mkdir(old)
                print("Creando fichero old")
            if not os.path.isdir(installers):
                os.mkdir(installers)
                print("Creando fichero para instaladores")
            if not os.path.isdir(documents):
                os.mkdir(documents)
                print("Creando fichero para documentos")
            if not os.path.isdir(zipped):
                os.mkdir(zipped)
                print("Creando fichero para comprimidos")

            if fichero.name.endswith(".exe") | fichero.name.endswith(".msi"):
                # fichero.name
                # Get modified time
                modified = os.path.getmtime(fichero)
                x = datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y")
                y = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                lastime = y - x

                if lastime > datetime.timedelta(30):
                    print(fichero.name)
                    print("Modified")
                    print(lastime)
                    shutil.move(folder + '\\' + fichero.name, installers + '\\' + fichero.name)

            if fichero.name.endswith(".pdf") | fichero.name.endswith(".doc") | fichero.name.endswith(
                    ".docx") | fichero.name.endswith(".odx"):
                # fichero.name
                # Get modified time

                modified = os.path.getmtime(fichero)
                x = datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y")
                y = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                lastime = y - x

                if lastime > datetime.timedelta(30):
                    print(fichero.name)
                    print("Modified")
                    print(lastime)
                    shutil.move(folder + '\\' + fichero.name, documents + '\\' + fichero.name)

            if fichero.name.endswith(".zip") | fichero.name.endswith(".rar") | fichero.name.endswith(
                    ".7zip") | fichero.name.endswith(".odx"):
                # fichero.name
                # Get modified time

                modified = os.path.getmtime(fichero)
                x = datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y")
                y = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                lastime = y - x

                if lastime > datetime.timedelta(30):
                    print(fichero.name)
                    print("Modified")
                    print(lastime)
                    shutil.move(folder + '\\' + fichero.name, zipped + '\\' + fichero.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readdownload()
