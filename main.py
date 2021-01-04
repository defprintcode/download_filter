import os
import time
import datetime
import shutil
import json
import re


def read_download():
    with open('data.json', 'r') as f:
        extensions_dic = json.load(f)

    home = os.path.expanduser("~")
    folder = os.path.join(home, "Downloads")
    original_path = folder + '\\' + extensions_dic[0]['folder_name']

    def add_version(path, version):
        xx = file.name
        old_ext = re.findall(r'\(\d\)\.\w+\S+$', xx)

        if not len(old_ext):
            x = xx.find(".")
            version = "(" + str(version) + ")"
            output_line = file.name[:x] + version + file.name[x:]
            scan_coincidences(path, output_line)

        else:

            old_version = re.findall(r'\d', old_ext[0])
            new_version = int(old_version[0]) + 1
            new_ext = str(old_ext[0]).replace(str(old_version[0]), str(new_version))
            new_file = xx.replace(old_ext[0], new_ext)
            scan_coincidences(path, new_file)

    def scan_coincidences(path, name):
        i = 1
        with os.scandir(path) as path_files:
            for path_file in path_files:
                if path_file.name == name:
                    i += i
        i = i - 1

        if i > 0:

            add_version(path, i)
        else:

            new_version_path = path + '\\' + name
            print(new_version_path)
            shutil.move(original_path, new_version_path)

    for extension in extensions_dic:

        with os.scandir(folder) as files:

            for file in files:

                if extension['name'] != "inactive":

                    if not os.path.isdir(original_path + '\\' + extension['path']):
                        os.mkdir(original_path + '\\' + extension['path'])
                        print("Making folder for " + extension['name'])

                    if file.name.endswith(tuple(extension['extensions'])) or extension['name'] == "other":
                        # file.name
                        # Get modified time
                        modified = os.path.getmtime(file)
                        x = datetime.datetime.strptime(time.ctime(modified), "%a %b %d %H:%M:%S %Y")
                        y = datetime.datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")
                        lastime = y - x

                        if lastime > datetime.timedelta(extensions_dic[0]['days']):
                            print(file.name)
                            print("Modified")
                            print(lastime)
                            # shutil.move(folder + '\\' + file.name,
                            #            original_path + '\\' + extension['path'] + '\\' + file.name)
                            # seacrh coincidences
                            print(folder + '\\' + file.name)
                            print(original_path + '\\' + extension['path'] + '\\' + file.name)

                            scan_coincidences(folder + '\\' + file.name,
                                              original_path + '\\' + extension['path'] + '\\' + file.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_download()
