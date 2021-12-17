# Created by Yam for the Russia Reworked mod. Free to use.

if __name__ == '__main__':

    try:
        directory = r"..\common\characters"
        filename = directory + r"\russia2_SOV.txt"

        print("Scanning...")
        input_file = open(filename, "r", encoding='utf-8-sig')
        output_file = open("character_loca.txt", "w", encoding='utf-8-sig')
        lines = input_file.readlines()
        input_file.close()

        for line in lines:
            if "name = " in line:
                key = line.strip().replace("name = ", "")
                name = key.replace("SOV_", "").replace("_", " ").title()
                print("Found %s, writing." % name)

                output_file.write(" %s:0 \"%s\"\n" % (key, name))
                output_file.write(" %s_desc:0 \"\"\n" % key)

        output_file.close()
        print("Success!")

    except Exception as e:
        print("Something went wrong\n")
        print(e)