# Created by Yam for the Russia Reworked mod. Free to use.
import traceback
import os.path
import sys

if __name__ == "__main__":

    try:
        cwd = os.getcwd()
        files = os.listdir(cwd)
        
        for file in files:
            if file.endswith(".dds") and not file.startswith("focus_"):
                print("Renaming %s to %s." % (file, "focus_SOV_%s" % file.lower()))
                os.rename(file, "focus_SOV_%s" % file.lower())

    except Exception:
        print("Something went wrong...")
        print(traceback.format_exc())
