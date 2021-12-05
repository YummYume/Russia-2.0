# Created by Yam for the Russia Reworked mod. Free to use.

if __name__ == '__main__':

    try:
        directory = r"..\common\characters"
        filename = directory + r"\russia2_SOV.txt"

        print("Scanning...")
        input_file = open(filename, "r", encoding='utf-8-sig')
        output_file = open("recruit_character.txt", "w", encoding='utf-8-sig')
        lines = input_file.readlines()
        input_file.close()
        characters = []

        for line in lines:
            line = line.strip()

            if line.startswith("SOV_") and line.endswith(" = {"):
                key = line.replace(" = {", "")

                if key not in characters:
                    characters.append(key)
                    print("Found %s, writing." % key)

                    output_file.write("recruit_character = %s\n" % key)
                else:
                    print("WARNING: Key %s already exist. Skipping." % key)

        output_file.close()
        print("Success!")

    except Exception as e:
        print("Something went wrong\n")
        print(e)
