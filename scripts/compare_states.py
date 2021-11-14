# Created by Yam for the Russia Reworked mod. Free to use.
import jsondiff as jd
from jsondiff import diff
import traceback
import sys
import os
import json
from datetime import date

if __name__ == '__main__':

    try:
        file1 = input("Path to the old json states file : ")
        if not os.path.isfile(file1):
            print("Invalid path : %s " % file1)
            print("Cancelling...")
            sys.exit()

        file2 = input("Path to the new json states file : ")
        if not os.path.isfile(file2):
            print("Invalid path : %s " % file2)
            print("Cancelling...")
            sys.exit()

        showall = input("Show unmodified states? (yes/no) : ")
        if showall == "yes" or showall == "y" or showall == "":
            showall = True
        else:
            showall = False

        with open(file1, 'r', encoding='utf-8-sig') as file1r:
            json1 = json.load(file1r)

        with open(file2, 'r', encoding='utf-8-sig') as file2r:
            json2 = json.load(file2r)

        addedstates = 0
        modifiedstates = 0
        deletedstates = 0

        report = "New States :\n"
        print("\nAdded states (and keys) :")
        for key, value in json2.items():
            if key not in json1:
                if type(value) is dict:
                    addedstates += 1
                    report += f"""
    State { value["nameloca"] } ({ key }) was added :
        File name : { value["filename"] }
        ID : { value["id"] }
        Name : { value["name"] }
        Localistation name : { value["nameloca"] }
        Manpower : { value["manpower"] }
        Category : { value["category"] }
        Owner : { value["owner"] }
        provinces :
            """
                    report += '\n            '.join(map(str, value["provinces"]))
                    report += "\n"
                    print("\nState %s (%s) was added." % (value["nameloca"], str(key)))
                else:
                    print("\nKey %s was added." % key)

        if addedstates == 0:
            report += "    No new state detected."
            print("\n  No new state detected.")
        
        report += "\nModified States :\n"
        print("\nModified states (and keys) :")
        for key, value in json2.items():
            if key in json1:
                if showall:
                    if type(value) is dict:
                        print("\nState %s (%s) :" % (value["nameloca"], str(key)))
                    else:
                        print("\n%s :" % key)

                if value != json1[key]:
                    report += "\n    State %s (%s) was modified :\n" % (value["nameloca"], str(key))
                    if showall == False:
                        if type(value) is dict:
                            print("\nState %s (%s) :" % (value["nameloca"], str(key)))
                        else:
                            print("\n%s :" % key)

                    if type(value) is dict:
                        modifiedstates += 1

                        if value["filename"] != json1[key]["filename"]:
                            report += "        File name changed from %s to %s.\n" % (value["filename"], json1[key]["filename"])
                            print("  File name changed from %s to %s." % (value["filename"], json1[key]["filename"]))

                        #Never supposed to happen
                        if value["id"] != json1[key]["id"]:
                            report += "        ID changed from %s to %s.\n" % (value["id"], json1[key]["id"])
                            print("  ID changed from %s to %s." % (value["id"], json1[key]["id"]))

                        if value["name"] != json1[key]["name"]:
                            report += "        Name changed from %s to %s.\n" % (value["name"], json1[key]["name"])
                            print("  Name changed from %s to %s." % (value["name"], json1[key]["name"]))

                        if value["nameloca"] != json1[key]["nameloca"]:
                            report += "        Localisation changed from %s to %s.\n" % (value["nameloca"], json1[key]["nameloca"])
                            print("  Localisation changed from %s to %s." % (value["nameloca"], json1[key]["nameloca"]))

                        if value["manpower"] != json1[key]["manpower"]:
                            report += "        Manpower changed from %s to %s.\n" % (value["manpower"], json1[key]["manpower"])
                            print("  Manpower changed from %s to %s." % (value["manpower"], json1[key]["manpower"]))

                        if value["category"] != json1[key]["category"]:
                            report += "        Category changed from %s to %s.\n" % (value["category"], json1[key]["category"])
                            print("  Category changed from %s to %s." % (value["category"], json1[key]["category"]))

                        if value["owner"] != json1[key]["owner"]:
                            report += "        Owner changed from %s to %s.\n" % (value["owner"], json1[key]["owner"])
                            print("  Owner changed from %s to %s." % (value["owner"], json1[key]["owner"]))

                        if value["provinces"] != json1[key]["provinces"]:
                            report += "        Provinces changed :\n"
                            report += "            Old provinces :"
                            for v in value["provinces"]:
                                report += "\n                " + v
                            report += "\n            New provinces :"
                            for v in json1[key]["provinces"]:
                                report += "\n                " + v
                            report += "\n"
                            print("  Provinces changed from %s to %s." % (', '.join(map(str, value["provinces"])), ', '.join(map(str, json1[key]["provinces"]))))
                    else:
                        if value != json1[key]:
                            print("  %s changed from %s to %s." % (str(key), value, json1[key]))
                else:
                    if showall:
                        print("  No changes detected.")

        if modifiedstates == 0:
            report += "    No modified state detected."
            print("\n  No modified state detected.")

        report += "\nDeleted States :\n"
        print("\nDeleted states (and keys) :")
        for key, value in json1.items():
            if key not in json2:
                if type(value) is dict:
                    deletedstates += 1
                    report += "\n    State %s (%s) was deleted." % (value["nameloca"], str(key))
                    print("\nState %s (%s) was deleted." % (value["nameloca"], str(key)))
                else:
                    print("\nKey %s was deleted." % key)

        if deletedstates == 0:
            report += "    No deleted state detected."
            print("\n  No deleted state detected.")

        print("\nNumber of new states : %s" % addedstates)
        print("Number of modified states : %s" % modifiedstates)
        print("Number of deleted states : %s\n" % deletedstates)

        file1name = file1.split(".")
        file2name = file2.split(".")
        data = diff(json1, json2, marshal=True)

        jsonfilename = "%s-compare_%s_and_%s.json" % (date.today(), file1name[0], file2name[0])
        if os.path.isfile(jsonfilename):
            overwrite = input("Warning : File %s already exist. Replace? (yes/no) : " % jsonfilename)
            if overwrite == "yes" or overwrite == "y" or overwrite == "":
                with open(jsonfilename, 'w', encoding='utf-8-sig') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                print("Json report generated as %s" % jsonfilename)
        else:
            with open(jsonfilename, 'w', encoding='utf-8-sig') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

            print("Json report generated as %s" % jsonfilename)

        reportstr = f"""This file was generated at { date.today() } with { file1 } as old file and { file2 } as new file.

Number of states for { file1 } : { json1["statecount"] }
Number of states for { file2 } : { json2["statecount"] }

Number of new states : { addedstates }
Number of modifier states : { modifiedstates }
Number of deleted states : { deletedstates }

"""
        reportstr += report

        reportfilename = "%s-report_%s_and_%s.txt" % (date.today(), file1name[0], file2name[0])
        if os.path.isfile(reportfilename):
            overwrite = input("Warning : File %s already exist. Replace? (yes/no) : " % reportfilename)
            if overwrite == "yes" or overwrite == "y" or overwrite == "":
                with open(reportfilename, 'w', encoding='utf-8-sig') as f:
                    f.write(reportstr)

                print("Detailed report generated as %s" % reportfilename)
        else:
            with open(reportfilename, 'w', encoding='utf-8-sig') as f:
                f.write(reportstr)

            print("Detailed report generated as %s" % reportfilename)
    
    except Exception:
        print("\nAn error occurred :", end="\n\n")
        print(traceback.format_exc())
        print("Cancelling...")
