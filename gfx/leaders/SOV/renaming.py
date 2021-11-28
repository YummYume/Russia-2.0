# Created by Yam for the Russia Reworked mod. Free to use.
import traceback
import os.path
import sys

if __name__ == "__main__":

    try:
        cwd = os.getcwd()
        files = os.listdir(cwd)
        
        for file in files:
            if file.endswith(".dds") and not file.startswith("Portrait_Russia_"):
                if file.startswith("Portrait_Soviet_"):
                    newname = file.replace("Soviet", "Russia")
                    newname = newname.replace("_", " ")
                    newname = newname.title()
                    newname = newname.replace(" ", "_")
                    newname = newname.replace(".Dds", ".dds")
                    print("Renaming %s to %s." % (file, newname))
                    os.rename(file, newname)

                elif file.startswith("Portrait_"):
                    newname = file.replace("Portrait_", "Portrait_Russia_")
                    newname = newname.replace("_", " ")
                    newname = newname.title()
                    newname = newname.replace(" ", "_")
                    newname = newname.replace(".Dds", ".dds")
                    print("Renaming %s to %s." % (file, newname))
                    os.rename(file, newname)

                else:
                    newname = "Portrait_Russia_%s" % file
                    newname = newname.replace("_", " ")
                    newname = newname.title()
                    newname = newname.replace(" ", "_")
                    newname = newname.replace(".Dds", ".dds")
                    print("Renaming %s to %s." % (file, newname))
                    os.rename(file, newname)

    except Exception:
        print("Something went wrong...")
        print(traceback.format_exc())
