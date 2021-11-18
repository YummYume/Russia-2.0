# Created by Yam for the Russia Reworked mod. Free to use.

import os

if __name__ == '__main__':

    try:
        directory = r"..\gfx\event_pictures\purge_pictures"
        file = os.listdir(directory)

        f = open("purge_pictures.txt", "w", encoding='utf-8-sig')

        for filename in sorted(file, key=lambda x: int(x.split('_')[0])):
            print("Working on %s" % filename)
            name = filename.split(".")

            f.write("spriteType = {\n")
            f.write("    name = \"GFX_%s\"\n" % name[0])
            f.write("    texturefile = \"gfx/event_pictures/purge_pictures/%s\"\n" % filename)
            f.write("}\n\n")

        print("Success")

    except Exception as e:
        print("Something went wrong\n")
        print(e)