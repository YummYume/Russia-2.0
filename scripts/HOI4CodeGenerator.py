import json
import os
import pathlib
import textwrap
import sys

def setup():
    print("Setting up...")

    path = "/save"
    cwd = os.getcwd()
    fullPath = cwd + path

    try:
        pathlib.Path(fullPath).mkdir(parents=True, exist_ok=True)
    except:
        print("Creation of the directory %s in %s failed." % (path, cwd))
        return None
    

def readFile(filePath="data.json"):
    print("Reading file %s..." % filePath)

    try:
        jsonData = open(filePath)
    except:
        print("Error : json file %s not found." % (filePath))
        return None

    try:
        data = json.load(jsonData)
    except:
        print("Error : couldn't read json file %s. Make sure it does not contain invalid data." % (filePath))
        return None

    return data

def generateFocuses(focus, focusNameFile, focusId, tag, continuousFocusPositionX, continuousFocusPositionY, indent):
    print("Generating focuses...\n")
    path = "/save/common/national_focus"
    cwd = os.getcwd()
    fullPath = cwd + path
    indent *= " "

    if type(focus) is not dict:
        print("Error : cannot generate focuses. Expected a dictionary, got %s." % type(focus).__name__)
        return None

    try:
        pathlib.Path(fullPath).mkdir(parents=True, exist_ok=True)
    except:
        print("Error : Creation of the directory %s in %s failed." % (path, cwd))
        return None

    if type(focusNameFile) is not str:
        focusFileName = "default.txt"
        print("Warning : focus_name_file is not defined in data.json file. Defaulting to default.txt.")
    else:
        focusFileName = focusNameFile + ".txt"

    fullPath += "/" + focusFileName
        
    if os.path.isfile(fullPath):
        print("WARNING : %s.txt already exists in %s !" % (focusNameFile, path))
        if input("Overwrite file? (y/n) ") != "y":
            return None

    try:
        f = open(fullPath, "w")

        f.write("focus_tree = {\n")
        f.write(textwrap.indent("id = %s_focus\n" % focusId, indent))
        f.write(textwrap.indent("continuous_focus_position = { x = %s y = %s }\r\n" % (continuousFocusPositionX, continuousFocusPositionY), indent))
        f.write(textwrap.indent("country = {\n", indent))
        f.write(textwrap.indent("factor = 0\r\n", indent * 2))
        f.write(textwrap.indent("modifier = {\n", indent * 2))
        f.write(textwrap.indent("add = 1000\n", indent * 3))
        f.write(textwrap.indent("tag = %s\n" % tag, indent * 3))
        f.write(textwrap.indent("}\n", indent * 2))
        f.write(textwrap.indent("}\n", indent))

        idList = []
        for key, value in focus.items():
            if type(value) is not dict:
                print("Warning : %s should be an object, %s given." % (key, type(value)))
            else:
                focusName = key
                fatalError = False

                if "id" in value:
                    id = value["id"]
                    if type(id) is not str:
                        print("Warning : id in focus %s should be a string, %s given." % (focusName, type(id).__name__))
                        fatalError = True
                    else:
                        if id in idList:
                            print("Warning : id %s for focus %s already exists!" % (id, focusName))
                            fatalError = True
                        else:
                            idList.append(id)
                else:
                    print("Warning : focus %s is missing an id!" % focusName)
                    fatalError = True

                if "cost" in value:
                    cost = value["cost"]
                    if type(cost) is not int:
                        print("Warning : cost in focus %s should be an integer, %s given." % (focusName, type(cost).__name__))
                        fatalError = True
                else:
                    print("Warning : focus %s is missing a cost!" % focusName)
                    fatalError = True

                if "icon" in value:
                    icon = value["icon"]
                    if type(icon) is not str and icon is not None:
                        print("Warning : icon in focus %s should be either null or a string, %s given." % (focusName, type(icon).__name__))
                        fatalError = True
                    elif icon is None:
                        icon = ""
                else:
                    icon = ""

                if "x" in value:
                    x = value["x"]
                    if type(x) is not int:
                        print("Warning : x value in focus %s should be an integer, %s given." % (focusName, type(x).__name__))
                        fatalError = True
                else:
                    print("Warning : focus %s is missing an x value!" % focusName)
                    fatalError = True

                if "y" in value:
                    y = value["y"]
                    if type(y) is not int:
                        print("Warning : y value in focus %s should be an integer, %s given." % (focusName, type(y).__name__))
                        fatalError = True
                else:
                    print("Warning : focus %s is missing an y value!" % focusName)
                    fatalError = True

                if "ai_factor" in value:
                    aiFactor = value["ai_factor"]
                    if type(aiFactor) is not int:
                        print("Warning : ai_factor in focus %s should be an integer, %s given." % (focusName, type(aiFactor).__name__))
                        fatalError = True
                else:
                    aiFactor = 1

                if "prerequisite" in value:
                    prerequisite = value["prerequisite"]
                    if type(prerequisite) is not dict and prerequisite is not None:
                        print("Warning : prerequisite in focus %s should be an object or null, %s given." % (focusName, type(prerequisite).__name__))
                        fatalError = True
                    else:
                        if type(prerequisite) is dict:
                            for pKey, pValue in prerequisite.items():
                                if type(pValue) is dict:
                                    for fpKey, fpValue in pValue.items():
                                        if type(fpValue) is not str:
                                            print("Warning : prerequisite %s in prerequisite %s in focus %s should be a string, %s given." % (fpKey, pKey, focusName, type(fpValue).__name__))
                                            fatalError = True
                                elif type(pValue) is not dict and type(pValue) is not str:
                                    print("Warning : prerequisite %s in focus %s should be a string or an object, %s given." % (fpKey, focusName, type(pValue).__name__))
                                    fatalError = True
                else:
                    prerequisite = None

                if fatalError == False:
                    # Focus name (commented out)
                    f.write(textwrap.indent("\n# %s\n" % focusName, indent))
                    f.write(textwrap.indent("focus = {\n", indent))

                    # id
                    f.write(textwrap.indent("id = %s_%s\n" % (tag, id), indent * 2))

                    # x
                    f.write(textwrap.indent("x = %s\n" % x, indent * 2))

                    # y
                    f.write(textwrap.indent("y = %s\n" % y, indent * 2))

                    # prerequisite
                    if type(prerequisite) is dict:
                        for pKey, pValue in prerequisite.items():
                            f.write(textwrap.indent("prerequisite = { ", indent * 2))
                            if type(pValue) is dict:
                                for fpKey, fpValue in pValue.items():
                                    f.write("focus = %s_%s " % (tag, fpValue))
                            elif type(pValue) is str:
                                f.write("focus = %s_%s " % (tag, pValue))
                            else:
                                f.write("")
                            f.write("}\n")
                    else:
                        f.write(textwrap.indent("prerequisite = {  }\n", indent * 2))
            
                    # icon
                    f.write(textwrap.indent("icon = GFX_%s\n" % icon, indent * 2))

                    # cost
                    f.write(textwrap.indent("cost = %s\n" % cost, indent * 2))

                    # ai_will_do
                    f.write(textwrap.indent("ai_will_do = {\n", indent * 2))
                    f.write(textwrap.indent("factor = %s\n" % aiFactor, indent * 3))
                    f.write(textwrap.indent("}\n", indent * 2))

                    # bypass
                    f.write(textwrap.indent("bypass = {\n", indent * 2))
                    f.write(textwrap.indent("\n", indent * 3))
                    f.write(textwrap.indent("}\n", indent * 2))

                    # available
                    f.write(textwrap.indent("available = {\n", indent * 2))
                    f.write(textwrap.indent("\n", indent * 3))
                    f.write(textwrap.indent("}\n", indent * 2))

                    # search_filters
                    f.write(textwrap.indent("search_filters = {  }\n", indent * 2))

                    # completion_reward
                    f.write(textwrap.indent("completion_reward = {\n", indent * 2))
                    f.write(textwrap.indent("\n", indent * 3))
                    f.write(textwrap.indent("}\n", indent * 2))
                    f.write(textwrap.indent("}\n", indent))
                else:
                    print("Focus %s cancelled.\n" % focusName)

        f.write("}")
        f.close
        return "Focuses generated successfully!\n"
    except:
        print("Error : A problem occured during the generation of focuses.\n")
        return None

def generateEvents(events, eventNameFile, namespace, indent):
    print("Generating Events...\n")
    path = "/save/events"
    cwd = os.getcwd()
    fullPath = cwd + path
    indent *= " "

    if type(events) is not dict:
        print("Error : cannot generate events. Expected a dictionary, got %s." % type(events).__name__)
        return None

    try:
        pathlib.Path(fullPath).mkdir(parents=True, exist_ok=True)
    except:
        print("Error : Creation of the directory %s in %s failed." % (path, cwd))
        return None

    if type(eventNameFile) is not str:
        eventNameFile = "default.txt"
        print("Warning : event_name_file is not defined in data.json file. Defaulting to default.txt.")
    else:
        eventNameFile = eventNameFile + ".txt"

    fullPath += "/" + eventNameFile
        
    if os.path.isfile(fullPath):
        print("WARNING : %s already exists in %s !" % (eventNameFile, path))
        if input("Overwrite file? (y/n) ") != "y":
            return None

    try:
        f = open(fullPath, "w")

        f.write("add_namespace = %s\n" % namespace)

        idList = []
        for key, value in events.items():
            if type(value) is not dict:
                print("Warning : %s should be an object, %s given." % (key, type(value)))
            else:
                eventName = key
                fatalError = False

                if "event_type" in value:
                    eventType = value["event_type"]
                    if type(eventType) is not str:
                        print("Warning : event_type in event %s should be a string, %s given." % (eventName, type(eventType).__name__))
                        fatalError = True
                    else:
                        if eventType != "country" and eventType != "state":
                            print("Warning : unrecognized event_type %s in event %s, should either be country or state." % (eventType, eventName))
                            fatalError = True
                else:
                    print("Warning : event %s is missing an event_type!" % eventName)
                    fatalError = True

                if "id" in value:
                    id = value["id"]
                    if type(id) is not int:
                        print("Warning : id in event %s should be an integer, %s given." % (eventName, type(id).__name__))
                        fatalError = True
                    else:
                        if id in idList:
                            print("Warning : id %s for event %s already exists!" % (id, eventName))
                            fatalError = True
                        else:
                            idList.append(id)
                else:
                    print("Warning : event %s is missing an id!" % eventName)
                    fatalError = True

                if "picture" in value:
                    picture = value["picture"]
                    if type(picture) is not str and picture is not None:
                        print("Warning : picture in event %s should be either null or a string, %s given." % (eventName, type(picture).__name__))
                        fatalError = True
                    elif picture is None:
                        picture = ""
                else:
                    picture = ""

                if "hidden" in value:
                    hidden = value["hidden"]
                    if type(hidden) is not bool and hidden is not None:
                        print("Warning : hidden in event %s should be either null or a boolean, %s given." % (eventName, type(hidden).__name__))
                        fatalError = True
                    else:
                        if hidden == True:
                            hidden = "yes"
                        else:
                            hidden = None
                else:
                    hidden = None

                if "is_triggered_only" in value:
                    triggeredOnly = value["is_triggered_only"]
                    if type(triggeredOnly) is not bool:
                        print("Warning : is_triggered_only in event %s should be a boolean, %s given." % (eventName, type(triggeredOnly).__name__))
                        fatalError = True
                    else:
                        if triggeredOnly == True:
                            triggeredOnly = "yes"
                        else:
                            triggeredOnly = "no"
                else:
                    print("Warning : event %s is missing a is_triggered_only!" % eventName)
                    fatalError = True

                if "fire_only_once" in value:
                    fireOnlyOnce = value["fire_only_once"]
                    if type(fireOnlyOnce) is not bool and fireOnlyOnce is not None:
                        print("Warning : fire_only_once in event %s should be either null or a boolean, %s given." % (eventName, type(fireOnlyOnce).__name__))
                        fatalError = True
                    else:
                        if fireOnlyOnce == True:
                            fireOnlyOnce = "yes"
                        elif fireOnlyOnce == False:
                            fireOnlyOnce = "no"

                        if fatalError == False and type(fireOnlyOnce) is str and triggeredOnly == "yes":
                            print("Warning : event %s contains a fire_only_once = %s value with a is_triggered_only = \"yes\". Those should not be used together." % (eventName, fireOnlyOnce))
                else:
                    fireOnlyOnce = None

                if "mean_time_to_happen" in value:
                    meanTimeToHappen = value["mean_time_to_happen"]
                    if type(meanTimeToHappen) is not int and meanTimeToHappen is not None:
                        print("Warning : mean_time_to_happen in event %s should be either null or an integer, %s given." % (eventName, type(meanTimeToHappen).__name__))
                        fatalError = True
                    else:
                        if fatalError == False and type(meanTimeToHappen) is int and triggeredOnly == "yes":
                            print("Warning : event %s contains a mean_time_to_happen = %s value with a is_triggered_only = \"yes\". Those should not be used together." % (eventName, meanTimeToHappen))
                else:
                    meanTimeToHappen = None

                if "immediate" in value:
                    immediate = value["immediate"]
                    if type(immediate) is not bool and immediate is not None:
                        print("Warning : immediate in event %s should be either null or a boolean, %s given." % (eventName, type(immediate).__name__))
                        fatalError = True
                else:
                    immediate = None

                if "options" in value:
                    options = value["options"]
                    if type(options) is not dict:
                        print("Warning : options in event %s should be an object, %s given." % (eventName, type(options).__name__))
                        fatalError = True
                    else:
                        if fatalError == False:
                            optionIds = []
                            optionCount = 0

                            for oKey, oValue in options.items():
                                optionCount += 1
                                if optionCount == 5:
                                    print("Warning : event %s contains more than 4 options, which is not recommended." % eventName)

                                optionName = oKey

                                if "id" in oValue:
                                    optionId = oValue["id"]
                                    if type(optionId) is not str:
                                        print("Warning : id in option %s in event %s should be a string, %s given." % (optionName, eventName, type(optionId).__name__))
                                        fatalError = True
                                    else:
                                        if optionId in optionIds:
                                            print("Warning : id %s for option %s in event %s already exists!" % (optionId, optionName, eventName))
                                            fatalError = True
                                        else:
                                            optionIds.append(optionId)
                                else:
                                    print("Warning : option %s in event %s is missing an id!" % (optionName, eventName))
                                    fatalError = True

                                if "add_trigger" in oValue:
                                    addTrigger = oValue["add_trigger"]
                                    if type(addTrigger) is not bool:
                                        print("Warning : add_trigger in option %s in event %s should be a boolean, %s given." % (optionName, eventName, type(addTrigger).__name__))
                                        fatalError = True
                                else:
                                    print("Warning : option %s in event %s is missing an add_trigger!" % (optionName, eventName))
                                    fatalError = True

                                if "ai_factor" in oValue:
                                    aiFactor = oValue["ai_factor"]
                                    if type(aiFactor) is not int:
                                        print("Warning : ai_factor in option %s in event %s should be an integer, %s given." % (optionName, eventName, type(aiFactor).__name__))
                                        fatalError = True
                                else:
                                    print("Warning : option %s in event %s is missing an ai_factor!" % (optionName, eventName))
                                    fatalError = True
                                
                else:
                    print("Warning : event %s is missing options!" % eventName)
                    fatalError = True

                if fatalError == False:
                    # Event name (commented out)
                    f.write("\n# %s\n" % eventName)
                    f.write("%s_event = {\n" % eventType)

                    # id
                    f.write(textwrap.indent("id = %s.%s\n" % (namespace, id), indent))

                    # title
                    f.write(textwrap.indent("title = %s.%s.t\n" % (namespace, id), indent))

                    # desc
                    f.write(textwrap.indent("desc = %s.%s.d\n" % (namespace, id), indent))

                    # picture
                    f.write(textwrap.indent("picture = GFX_%s\n\n" % picture, indent))

                    # is_triggered_only
                    f.write(textwrap.indent("is_triggered_only = %s\n" % triggeredOnly, indent))

                    # hidden
                    if hidden is not None:
                        f.write(textwrap.indent("hidden = %s\n" % hidden, indent))

                    # fire_only_once
                    if fireOnlyOnce is not None:
                        f.write(textwrap.indent("fire_only_once = %s\n" % fireOnlyOnce, indent))

                    # mean_time_to_happen
                    if meanTimeToHappen is not None:
                        f.write(textwrap.indent("mean_time_to_happen = {\n", indent))
                        f.write(textwrap.indent("days = %s\n" % meanTimeToHappen, indent * 2))
                        f.write(textwrap.indent("}\n", indent))

                    # immediate
                    if immediate == True:
                        f.write(textwrap.indent("immediate = {\n", indent))
                        f.write(textwrap.indent("\n", indent * 2))
                        f.write(textwrap.indent("}\n", indent))

                    # options
                    for oKey, oValue in options.items():
                        optionName = oKey
                        optionId = oValue["id"]
                        addTrigger = oValue["add_trigger"]
                        aiFactor = oValue["ai_factor"]

                        # Option name (commented out)
                        f.write(textwrap.indent("\n# %s\n", indent) % (optionName))
                        f.write(textwrap.indent("option = {\n", indent))
                        f.write(textwrap.indent("name = %s.%s.%s\n", indent * 2) % (namespace, id, optionId))

                        # trigger
                        if addTrigger == True:
                            f.write(textwrap.indent("trigger = {\n", indent * 2))
                            f.write(textwrap.indent("\n", indent * 3))
                            f.write(textwrap.indent("}\n", indent * 2))

                        # ai_chance
                        f.write(textwrap.indent("ai_chance = {\n", indent * 2))
                        f.write(textwrap.indent("factor = %s\n", indent * 3) % aiFactor)
                        f.write(textwrap.indent("}\n\n", indent * 2))
                        f.write(textwrap.indent("}\n", indent))
            
                    f.write("}\n")
                else:
                    print("Event %s cancelled.\n" % eventName)

        f.close
        return "Events generated successfully!\n"

    except:
        print("Error : A problem occured during the generation of events.\n")
        return None

# Main
if __name__ == "__main__":
    setup()
    data = readFile()

    # Focuses
    fatalError = False
    if type(data) is dict:
        if "focus" in data:
            focusValue = data["focus"]
            if type(focusValue) is not dict:
                print("Warning : focus should be an object, %s given." % type(focusValue).__name__)
                fatalError = True
        else:
            print("Warning : focus data is missing!")
            fatalError = True

        if "focus_name_file" in data:
            focusNameFileValue = data["focus_name_file"]
            if type(focusNameFileValue) is not str:
                print("Warning : focus_name_file should be a string, %s given." % type(focusNameFileValue).__name__)
                fatalError = True
        else:
            print("Warning : focus_name_file data is missing!")
            fatalError = True

        if "focus_id" in data:
            focusIdValue = data["focus_id"]
            if type(focusIdValue) is not str:
                print("Warning : focus_id should be a string, %s given." % type(focusIdValue).__name__)
                fatalError = True
        else:
            print("Warning : focus_id data is missing!")
            fatalError = True

        if "tag" in data:
            tagValue = data["tag"]
            if type(tagValue) is not str:
                print("Warning : tag should be a string, %s given." % type(tagValue).__name__)
                fatalError = True
        else:
            print("Warning : tag data is missing!")
            fatalError = True

        if "continuous_focus_position_x" in data:
            continuousFocusPositionXValue = data["continuous_focus_position_x"]
            if type(continuousFocusPositionXValue) is not int:
                print("Warning : continuous_focus_position_x should be an integer, %s given." % type(continuousFocusPositionXValue).__name__)
                fatalError = True
        else:
            print("Warning : continuous_focus_position_x data is missing!")
            fatalError = True

        if "continuous_focus_position_y" in data:
            continuousFocusPositionYValue = data["continuous_focus_position_y"]
            if type(continuousFocusPositionYValue) is not int:
                print("Warning : continuous_focus_position_y should be an integer, %s given." % type(continuousFocusPositionYValue).__name__)
                fatalError = True
        else:
            print("Warning : continuous_focus_position_y data is missing!")
            fatalError = True

        if "indent" in data:
            indentValue = data["indent"]
            if type(indentValue) is not int:
                print("Warning : indent should be an integer, %s given." % type(indentValue).__name__)
                fatalError = True
        else:
            print("Warning : indent data is missing!")
            fatalError = True

        if fatalError == False:
            if input("Generate focuses? (y/n) ") == "y":
                generateStatus = generateFocuses(focus = focusValue, focusNameFile = focusNameFileValue, focusId = focusIdValue, tag = tagValue, continuousFocusPositionX = continuousFocusPositionXValue, continuousFocusPositionY = continuousFocusPositionYValue, indent = indentValue)
                if generateStatus is None:
                    print("Focus generation cancelled.\n")
                else:
                    print(generateStatus)
        else:
            print("Cannot generate focuses, data is missing or invalid. Please check errors and retry.\n")

    # Events
    fatalError = False
    if type(data) is dict:
        if "events" in data:
            eventsValue = data["events"]
            if type(eventsValue) is not dict:
                print("Warning : events should be an object, %s given." % type(eventsValue).__name__)
                fatalError = True
        else:
            print("Warning : events data is missing!")
            fatalError = True

        if "event_name_file" in data:
            eventNameFileValue = data["event_name_file"]
            if type(eventNameFileValue) is not str:
                print("Warning : event_name_file should be a string, %s given." % type(eventNameFileValue).__name__)
                fatalError = True
        else:
            print("Warning : event_name_file data is missing!")
            fatalError = True

        if "namespace" in data:
            namespaceValue = data["namespace"]
            if type(namespaceValue) is not str:
                print("Warning : namespace should be a string, %s given." % type(namespaceValue).__name__)
                fatalError = True
        else:
            print("Warning : namespace data is missing!")
            fatalError = True

        if "indent" in data:
            indentValue = data["indent"]
            if type(indentValue) is not int:
                print("Warning : indent should be an integer, %s given." % type(indentValue).__name__)
                fatalError = True
        else:
            print("Warning : indent data is missing!")
            fatalError = True

        if fatalError == False:
            if input("Generate events? (y/n) ") == "y":
                generateStatus = generateEvents(events = eventsValue, eventNameFile = eventNameFileValue, namespace = namespaceValue, indent = indentValue)
                if generateStatus is None:
                    print("Events generation cancelled.\n")
                else:
                    print(generateStatus)
        else:
            print("Cannot generate events, data is missing or invalid. Please check errors and retry.\n")