# Created by Yam for the Russia Reworked mod. Free to use.

import os
import random

if __name__ == '__main__':

    try:
        directory = r"..\gfx\interface\decision_scripted_gui\purge_portraits"

        f_portraits = open("save_purge_portraits.txt", "w", encoding='utf-8-sig')
        f_gui = open("save_purge_portraits_gfx.txt", "w", encoding='utf-8-sig')
        f_scripted_gui = open("save_purge_portraits_scripted_gui.txt", "w", encoding='utf-8-sig')
        f_loc = open("save_purge_portraits_loc.txt", "w", encoding='utf-8-sig')
        f_scripted_loc = open("save_purge_portraits_scripted_loc.txt", "w", encoding='utf-8-sig')
        file = os.listdir(directory)

        xy_values = []

        for filename in sorted(file, key=lambda x: int(x.split('_')[0])):
            print("Working on %s" % filename)
            name = filename.split(".")
            nameloca = name[0].split("_")
            id = nameloca[0]

            f_portraits.write("spriteType = {\n")
            f_portraits.write("    name = \"GFX_%s\"\n" % name[0].lower())
            f_portraits.write("    texturefile = \"gfx/interface/decision_scripted_gui/purge_portraits/%s\"\n" % filename)
            f_portraits.write("    noOfFrames = 2\n")
            f_portraits.write("}\n\n")

            not_conflicting = False

            while not_conflicting == False:
                x = random.randint(0, 450)
                y = random.randint(0, 380)

                if (len(xy_values) > 1):
                    conflict = False

                    for values in xy_values:
                        if ((values[0] - 42) <= x <= (values[0] + 42)) and ((values[1] - 55) <= y <= (values[1] + 55)):
                            conflict = True
                            break

                    if not conflict:
                        not_conflicting = True

                else:
                    not_conflicting = True

            xy_values.append([x, y])
            
            f_gui.write("iconType = {\n")
            f_gui.write("    position = { x = %s y = %s }\n" % (x, y))
            f_gui.write("    orientation = upper_left\n")
            f_gui.write("    name = \"%s\"\n" % name[0].lower())
            f_gui.write("    spriteType = \"GFX_%s\"\n" % name[0].lower())
            f_gui.write("    alwaystransparent = no\n")
            f_gui.write("    pdx_tooltip = LOC_%s_tt\n" % name[0].lower())
            f_gui.write("    pdx_tooltip_delayed = LOC_%s_tt_desc\n" % name[0].lower())
            f_gui.write("}\n\n")

            f_scripted_gui.write("%s = {\n" % name[0].lower())
            f_scripted_gui.write("    frame = var:sov_great_purge_frame^%s\n" % id)
            f_scripted_gui.write("}\n\n")

            f_loc.write(" LOC_%s_tt:0 \"§Y%s§!\"\n" % (name[0].lower(), "%s %s" % (nameloca[2], nameloca[3])))
            f_loc.write(" LOC_%s_tt_desc:0 \"[Get%sPurgeStatus]\"\n" % (name[0].lower(), "%s%s" % (nameloca[2], nameloca[3])))
            f_loc.write(" LOC_%s_purged:0 \"Purged at [?sov_great_purge_date^%s.GetDateString]\"\n" % (name[0].lower(), id))

            f_scripted_loc.write("defined_text = {\n")
            f_scripted_loc.write("    name = Get%sPurgeStatus\n" % "%s%s" % (nameloca[2], nameloca[3]))
            f_scripted_loc.write("    text = {\n")
            f_scripted_loc.write("        trigger = {\n")
            f_scripted_loc.write("            check_variable = {\n")
            f_scripted_loc.write("                var = sov_great_purge_frame^%s\n" % id)
            f_scripted_loc.write("                value = 2\n")
            f_scripted_loc.write("                compare = equals\n")
            f_scripted_loc.write("            }\n")
            f_scripted_loc.write("        }\n")
            f_scripted_loc.write("        localization_key = LOC_%s_purged\n" % name[0].lower())
            f_scripted_loc.write("    }\n")
            f_scripted_loc.write("    text = {\n")
            f_scripted_loc.write("        localization_key = LOC_great_purge_not_purged\n")
            f_scripted_loc.write("    }\n")
            f_scripted_loc.write("}\n\n")

            print("%s completed\n" % filename)

        f_portraits.close
        f_gui.close
        f_scripted_gui.close
        f_loc.close
        f_scripted_loc.close
        print("Success")

    except Exception as e:
        print("Something went wrong\n")
        print(e)