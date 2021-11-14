# Created by Yam for the Russia Reworked mod. Free to use.
import os
import json
import sys
import re
import yaml
import traceback
from datetime import date

if __name__ == '__main__':

    try:
        # Either put this in the root folder of HOI4 or put the full path to your HOI4 folder
        directory = r".\history\states"
        localisation = r".\localisation\state_names_l_english.yml"
        filepath = input("Enter the path to your HOI4 installation folder (%s) : " % sys.path[0])
        if not os.path.isdir(filepath):
            print("Path given (%s) is not a valid directory" % filepath)
            print("Cancelling...")
            sys.exit()

        if filepath == "":
            filepath = sys.path[0]

        fullcwd = filepath + directory
        localisationpath = filepath + localisation

        if not os.path.isdir(fullcwd):
            print("Cannot find folder \"states\" (%s) " % fullcwd)
            print("Cancelling...")
            sys.exit()

        if not os.path.isfile(localisationpath):
            print("Cannot find file \"state_names_l_english.yml\" (%s) " % localisationpath)
            print("Cancelling...")
            sys.exit()

        fullcwd = os.chdir(fullcwd)
        statecount = 0
        data = {
            "statecount": statecount
        }

        with open(localisationpath, 'r', encoding='utf-8-sig') as yml:
            yml = yml.read()
            yml = yml.replace(":0", ":")
            yml = yml.replace(":1", ":")
            yml = yml.replace(":2", ":")
            statelocalisation = yaml.safe_load(yml)
            statelocalisation = statelocalisation['l_english']

        for filename in os.listdir(fullcwd):
            statecount += 1
            id = 0
            name = "UNKNOWN"
            nameloca = ""
            manpower = 0
            category = "UNKNOWN"
            owner = "UNKNOWN"
            provinces = []

            with open(filename) as f:
                provincefound = False
                for i, line in enumerate(f, 1):
                    if line.find("id") != -1:
                        find = line.split("=")
                        for word in find:
                            if re.search("^[0-9]+$", word):
                                id = word.strip("\n").strip("\"").strip()

                    if line.find("name") != -1:
                        find = line.split("\"")
                        name = find[1].strip("\n").strip("\"").strip()

                    if line.find("manpower") != -1:
                        find = line.split("=")
                        manpower = find[1].strip("\n").strip("\"").strip()

                    if line.find("state_category") != -1:
                        find = line.split("=")
                        category = find[1].strip("\n").strip("\"").strip()

                    if line.find("owner") != -1:
                        find = line.split("=")
                        owner = find[1].strip("\n").strip("\"").strip()

                    if line.find("provinces") != -1:
                        provincefound = True

                    if provincefound and re.search("^.*[0-9].*$", line):
                        find = line.split(" ")
                        for province in find:
                            if re.search("^[0-9]+$", province.strip()):
                                provinces.append(province.strip())

                            if re.search("^.*}.*$", province):
                                break

                        provincefound = False

                for key, value in statelocalisation.items():
                    if key == name:
                        nameloca = value
                        break

            state = {
                "filename": filename,
                "id": id,
                "name": name,
                "nameloca": nameloca,
                "manpower": manpower,
                "category": category,
                "owner": owner,
                "provinces": provinces
            }

            data[id] = state

            print("State added : %s %s" % (id, nameloca))

        data.update({
            "statecount": statecount
        })

        print("%s states added" % statecount)

        print("Success")

        os.chdir(sys.path[0])
        jsonfilename = "states_%s.json" % date.today()

        if os.path.isfile(jsonfilename):
            overwrite = input("Warning : File %s already exist. Replace? (yes/no) : " % jsonfilename)
            if overwrite == "yes" or overwrite == "y" or overwrite == "":
                with open(jsonfilename, 'w', encoding='utf-8-sig') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                print("Saved as %s" % jsonfilename)
        else:
            with open(jsonfilename, 'w', encoding='utf-8-sig') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print("Saved as %s" % jsonfilename)
    
    except Exception:
        print("\nAn error occurred :", end="\n\n")
        print(traceback.format_exc())
        print("Cancelling...")
