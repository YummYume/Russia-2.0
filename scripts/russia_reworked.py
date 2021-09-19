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

        # currentid = 557
        # while currentid <= 591:
        #     f.write(" soviets.%s.t:0 \"The Great Purge - \"\n" % currentid)
        #     f.write(" soviets.%s.d:0 \"\"\n" % currentid)
        #     f.write(" soviets.%s.a:0 \"He has to go.\"\n" % currentid)
        #     f.write(" soviets.%s.b:0 \"He is not guilty.\"\n" % currentid)
        #     currentid += 1

        f.close

        print("Success")

        manpower = []

        with open('states_2021-07-31.json', encoding='utf-8-sig') as jsonFile:
            states = json.load(jsonFile)

            for key, state in states.items():
                if isinstance(state, dict) and "manpower" in state:
                    manpower.append(int(state["manpower"]))

        totalManpower = addSpace(sum(manpower))
        averageManpower = addSpace(statistics.mean(manpower))

        print("Total manpower : %s" % totalManpower)
        print("Average manpower : %s" % averageManpower)

    except Exception as e:
        print("Something went wrong")
        print(e)
