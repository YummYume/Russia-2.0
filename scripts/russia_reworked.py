import os

if __name__ == '__main__':

    try:
        # Put this file in the root folder of HOI4
        directory = r".\history\countries"

        f = open("save.txt", "w")

        for filename in os.listdir(directory):
            tag = filename.split()
            f.write("add_to_array = { global.russia_reworked_countries = %s }\n" % tag[0])

        f.close

        print("Success")

    except:
        print("Something went wrong")