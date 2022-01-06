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

        f = open("russian_states_ai.txt", "w")
        russian_states = [
            "TAN",
            "UKR",
            "GEO",
            "KAZ",
            "AZR",
            "ARM",
            "BLR",
            "KYR",
            "TAJ",
            "TMS",
            "UZB",
            "KUB",
            "BUK",
            "ALT",
            "KAL",
            "KAR",
            "CRI",
            "TAT",
            "CIN",
            "DAG",
            "BYA",
            "CKK",
            "YAK",
            "VLA",
            "KKP",
            "YAM",
            "TAY",
            "OVO",
            "NEN",
            "ABK",
            "KBK",
            "NOA",
            "VGE",
            "BSK",
            "KHI",
            "UDM",
            "CHU",
            "MEL",
            "SIB",
            "CIR",
            "GPM",
            "NOV",
            "PRM",
            "ROS",
            "STP",
            "VLG",
            "URA",
            "KMI",
            "EFR",
            "VYA"
        ]

        for russian_state in russian_states:
            f.write(f"""
{ russian_state }_recover_core_territory = {{

	reversed = yes

	target_array = neighbors

	enable = {{
		NOT = {{
            is_in_faction_with = { russian_state }
            is_subject_of = { russian_state }
        }}
		strength_ratio = {{
			tag = { russian_state }
			ratio < 1.25
		}}
        if = {{
			limit = {{
				is_subject = yes
			}}
			OVERLORD = {{
				strength_ratio = {{
					tag = { russian_state }
					ratio < 1.25
				}}
			}}
		}}
		OR = {{
            any_owned_state = {{
				is_core_of = { russian_state }
			}}
			any_controlled_state = {{
				is_core_of = { russian_state }
			}}
        }}
	}}

	enable_reverse = {{
        NOT = {{
            has_global_flag = second_russian_civil_war_in_progress
        }}
		{ russian_state } = {{
			has_war = no
			is_subject = no
		}}
	}}

	abort_when_not_enabled = yes

	ai_strategy = {{
		type = conquer
		id = { russian_state }
		value = 9999
	}}

    ai_strategy = {{
		type = consider_weak
		id = { russian_state }
		value = 9999
	}}

	ai_strategy = {{
		type = antagonize
		id = { russian_state }
		value = 9999
	}}

	ai_strategy = {{
		type = declare_war
		id = { russian_state }
		value = 9999
	}}
}}
            """)

        f.close
        print("Success")

        f = open("anarchist_party.txt", "w", encoding='utf-8-sig')
        anarchist_party_names = [
            "intellect",
            "civilian_industry",
            "military_industry",
            "militarist",
            "aviation",
            "naval",
            "logistic",
            "internal_security",
            "countryside",
            "theorist"
        ]
        index = 0

        for anarchist_party in anarchist_party_names:
            title = anarchist_party.replace("_", " ").title().replace(" ", "")
            f.write(f"""
defined_text = {{
    name = GetCurrentAnarchistSupport{ title }Party
    text = {{
        trigger = {{
            check_variable = {{
                var = sov.sov_anarchist_election_parties^{ index }
                value = 100
                compare = greater_than_or_equals
            }}
        }}
        localization_key = LOC_anarchist_{ anarchist_party }_party_100
    }}
    text = {{
        trigger = {{
            check_variable = {{
                var = sov.sov_anarchist_election_parties^{ index }
                value = 75
                compare = greater_than_or_equals
            }}
        }}
        localization_key = LOC_anarchist_{ anarchist_party }_party_75
    }}
    text = {{
        trigger = {{
            check_variable = {{
                var = sov.sov_anarchist_election_parties^{ index }
                value = 50
                compare = greater_than_or_equals
            }}
        }}
        localization_key = LOC_anarchist_{ anarchist_party }_party_50
    }}
    text = {{
        trigger = {{
            check_variable = {{
                var = sov.sov_anarchist_election_parties^{ index }
                value = 25
                compare = greater_than_or_equals
            }}
        }}
        localization_key = LOC_anarchist_{ anarchist_party }_party_25
    }}
    text = {{
        localization_key = LOC_anarchist_{ anarchist_party }_party_0
    }}
}}
            """)
            index += 1

        index = 0

        for anarchist_party in anarchist_party_names:
            f.write(f"""
 LOC_anarchist_{ anarchist_party }_party_100:0 "§0[?sov_anarchist_election_parties^{ index }|1]%§!"
 LOC_anarchist_{ anarchist_party }_party_75:0 "§2[?sov_anarchist_election_parties^{ index }|1]%§!"
 LOC_anarchist_{ anarchist_party }_party_50:0 "§7[?sov_anarchist_election_parties^{ index }|1]%§!"
 LOC_anarchist_{ anarchist_party }_party_25:0 "§9[?sov_anarchist_election_parties^{ index }|1]%§!"
 LOC_anarchist_{ anarchist_party }_party_0:0 "§R[?sov_anarchist_election_parties^{ index }|1]%§!"
            """)
            index += 1

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
