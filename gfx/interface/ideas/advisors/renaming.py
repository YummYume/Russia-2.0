# Created by Yam for the Russia Reworked mod. Free to use.
import traceback
import os.path
import sys

if __name__ == "__main__":

    try:
        cwd = os.getcwd()
        files = os.listdir(cwd)
        
        for file in files:
            if file.endswith(".dds") and not file.startswith("advisor_SOV_"):
                newname = file
                if file.startswith("idea_SOV_"):
                    newname = newname.replace("idea_SOV_", "")
                elif file.startswith("idea_"):
                    newname = newname.replace("idea_", "")
                
                print("Renaming %s to %s." % (file, "advisor_SOV_%s" % newname.lower()))
                os.rename(file, "advisor_SOV_%s" % newname.lower())

    except Exception:
        print("Something went wrong...")
        print(traceback.format_exc())
