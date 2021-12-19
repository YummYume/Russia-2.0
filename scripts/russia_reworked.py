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
        
        f = open("new_states.txt", "w")
        new_states = [
            "ABK",
            "ALT",
            "BSK",
            "BUK",
            "BYA",
            "CHU",
            "CIN",
            "CKK",
            "KBK",
            "KHI",
            "KKP",
            "MEL",
            "NEN",
            "NOA",
            "OVO",
            "TAY",
            "UDM",
            "VGE",
            "VLA",
            "YAK",
            "YAM",
        ]
        
        for new_state in new_states:
            f.write(f"""
{ new_state }_ai_behavior = {{
	name = "{ new_state }_AI_BEHAVIOR"
	group = "RULE_GROUP_AI_BEHAVIOR"
	default = {{
		name = DEFAULT
		text = "RULE_OPTION_DEFAULT"
		desc = "RULE_OPTION_DEFAULT_RUSSIAN_STATE_DESC"
	}}
	option = {{
		name = DEMOCRATIC
		text = "RULE_OPTION_DEMOCRATIC_RUSSIAN_STATE"
		desc = "RULE_OPTION_DEMOCRATIC_RUSSIAN_STATE_DESC"
	}}
	option = {{
		name = NEUTRALITY
		text = "RULE_OPTION_NEUTRALITY_RUSSIAN_STATE"
		desc = "RULE_OPTION_NEUTRALITY_RUSSIAN_STATE_DESC"
	}}
	option = {{
		name = COMMUNISM
		text = "RULE_OPTION_COMMUNISM_RUSSIAN_STATE"
		desc = "RULE_OPTION_COMMUNISM_RUSSIAN_STATE_DESC"
	}}
	option = {{
		name = FASCISM
		text = "RULE_OPTION_FASCISM_RUSSIAN_STATE"
		desc = "RULE_OPTION_FASCISM_RUSSIAN_STATE_DESC"
	}}
	option = {{
		name = RANDOM
		text = "RULE_OPTION_RANDOM_RUSSIAN_STATE"
		desc = "RULE_OPTION_RANDOM_RUSSIAN_STATE_DESC"
	}}
}}
            """)
            
        for new_state in new_states:
            f.write(" %s_AI_BEHAVIOR:0 \"@%s \"\n" % (new_state, new_state))
            
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
