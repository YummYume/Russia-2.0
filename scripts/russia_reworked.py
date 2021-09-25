# Created by Yam for the Russia Reworked mod. Free to use.

import os
import json
import statistics

def addSpace(n, numSpace = 3):
    n = str(n).split('.')
    n[0] = list(str(n[0]))
    charCount = 0
    r = ''

    for c in reversed(n[0]):
        r += c
        charCount += 1

        if charCount == numSpace:
            r += ' '
            charCount = 0

    r = r[::-1]

    if len(n) > 1:
        r += '.%s' % n[1]

    return r

if __name__ == '__main__':

    try:
        # Put this file in the root folder of HOI4 or the root folder of your mod, inside a "script" folder
        directory = r"..\history\countries"

        f = open("save.txt", "w")

        for filename in os.listdir(directory):
           tag = filename.split()
           f.write("add_to_array = { global.russia_reworked_countries_load = %s }\n" % tag[0])

        f.close

        print("Success")

        manpower = []
        longestName = ""

        with open('states_2021-07-31.json', encoding='utf-8-sig') as jsonFile:
            states = json.load(jsonFile)

            for key, state in states.items():
                if isinstance(state, dict) and "manpower" in state:
                    manpower.append(int(state["manpower"]))

                if isinstance(state, dict) and "nameloca" in state:
                    if len(longestName) < len(state["nameloca"]):
                        longestName = state["nameloca"]

        totalManpower = addSpace(sum(manpower))
        averageManpower = addSpace(statistics.mean(manpower))

        print("Total manpower : %s" % totalManpower)
        print("Average manpower : %s" % averageManpower)
        print("Longest state name : %s" % longestName)

    except Exception as e:
        print("Something went wrong")
        print(e)
