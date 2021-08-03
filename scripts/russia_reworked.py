# Created by Yam for the Russia Reworked mod. Free to use.

import os

if __name__ == '__main__':

    try:
        # Put this file in the root folder of HOI4 or the root folder of your mod
        directory = r".\history\countries"

        f = open("save.txt", "w")

        for filename in os.listdir(directory):
            tag = filename.split()
            f.write("add_to_array = { global.russia_reworked_countries_load = %s }\n" % tag[0])

        f.close

        print("Success")

    except:
        print("Something went wrong")