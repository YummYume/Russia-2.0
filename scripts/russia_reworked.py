# Created by Yam for the Russia Reworked mod. Free to use.

import os

if __name__ == '__main__':

    try:
        # Put this file in the root folder of HOI4 or the root folder of your mod
        directory = r".\history\countries"

        f = open("save.txt", "w")

        #for filename in os.listdir(directory):
        #    tag = filename.split()
        #    f.write("add_to_array = { global.russia_reworked_countries_load = %s }\n" % tag[0])

        currentid = 557
        while currentid <= 591:
            f.write(" soviets.%s.t:0 \"The Great Purge - \"\n" % currentid)
            f.write(" soviets.%s.d:0 \"\"\n" % currentid)
            f.write(" soviets.%s.a:0 \"He has to go.\"\n" % currentid)
            f.write(" soviets.%s.b:0 \"He is not guilty.\"\n" % currentid)
            currentid += 1

        f.close

        print("Success")

    except:
        print("Something went wrong")