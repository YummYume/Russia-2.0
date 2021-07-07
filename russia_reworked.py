import os

directory = r".\history\countries"

f = open("save.txt", "w")

for filename in os.listdir(directory):
    tag = filename.split()
    f.write("add_to_array = { global.russia_reworked_countries = %s }\n" % tag[0])

f.close