import os
import time
import datetime
import shutil
import json


def readdownload():
    with open('data.json', 'r') as f:
        extensions_dic = json.load(f)

    home = os.path.expanduser("~")
    folder = os.path.join(home, "Downloads")
    old = folder + '\\' + extensions_dic[0]['folder_name']

    for extension in extensions_dic:

        with os.scandir(folder) as ficheros:

            for fichero in ficheros:

                if extension['name'] != "inactive":

                    if not os.path.isdir(old + '\\' + extension['path']):
                        os.mkdir(old + '\\' + extension['path'])
                        print("Making folder for " + extension['name'])

                    if fichero.name.endswith(tuple(extension['extensions'])) or extension['name'] == "other":
                        # fichero.name
                        # Get modified time
                        modified = os.path.getmtime(fichero)
                        x = datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y")
                        y = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                        lastime = y - x

                        if lastime > datetime.timedelta(extensions_dic[0]['days']):
                            print(fichero.name)
                            print("Modified")
                            print(lastime)
                            shutil.move(folder + '\\' + fichero.name,
                                        old + '\\' + extension['path'] + '\\' + fichero.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readdownload()
