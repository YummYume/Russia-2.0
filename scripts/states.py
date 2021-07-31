# Created by Yam for the Russia Reworked mod. Free to use.

import os
import json
import sys
import re
import yaml
from datetime import date

if __name__ == '__main__':

    try:
        # Put this file in the root folder of HOI4 along with run_states.bat and simply run it
        filepath = sys.path[0]
        directory = r".\history\states"
        localisation = r".\localisation\state_names_l_english.yml"
        fullcwd = os.chdir(filepath + directory)
        localisationpath = filepath + localisation

        statecount = 0
        data = {
            "statecount": statecount
        }

        with open(localisationpath, 'r', encoding='utf-8-sig') as yml:
            statelocalisation = yaml.load(yml)
            statelocalisation = statelocalisation['l_english'].split()

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

                if name + ":0" in statelocalisation:
                    nameloca = statelocalisation[statelocalisation.index(name + ":0") + 1]
                elif name + ":1" in statelocalisation:
                    nameloca = statelocalisation[statelocalisation.index(name + ":1") + 1]
                elif name + ":2" in statelocalisation:
                    nameloca = statelocalisation[statelocalisation.index(name + ":2") + 1]
                nameloca = nameloca.strip("\"")

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

        os.chdir(sys.path[0])

        jsonfilename = "states_%s.json" % date.today()
        with open(jsonfilename, 'w', encoding='utf-8-sig') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Success")
        print("Saved as %s" % jsonfilename)
    
    except:
        print("An error occurred")
        print("Cancelling...")