# Created by Yam for the Russia Reworked mod. Free to use.

import os

if __name__ == '__main__':

    try:
        directory = r".\gfx\interfaces\decision_scripted_gui\purge_portraits"

        f = open("save_purge_portraits.txt", "w")

        for filename in os.listdir(directory):
           f.write("spriteType = {\n")
           f.write("    name = \"GFX_%s\"\n" % filename.lower())
           f.write("    texturefile = \"gfx/interfaces/decision_scripted_gui/purge_portraits/%s\"\n" % filename)
           f.write("    noOfFrames = 2\n")
           f.write("}\n\n")

        f.close

        print("Success")

    except:
        print("Something went wrong")