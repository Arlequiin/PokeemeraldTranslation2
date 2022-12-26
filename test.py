#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Trainer class
import re
def trainer_class():
    with open("output/trainer_class.h") as f:
        content=f.read().replace('''("''','<').replace('''")''',">").replace("{PKMN}","√")
        result=re.findall('''= _<(.*)>,''',content)
        print(result)
        for name in result:
         content=content.replace("trainerName = _<"+name,"trainerName = _<"+name.lower().title())
    with open("output/trainer_class.h",'w') as f:
        content=(content.replace("<",'''("''').replace(">",'''")''').replace("√","{PKMN}"))
        f.write(content)


def trad_battle_message():
    with open("data/bmfr.h") as f:
        source=f.readlines()
    strings_source={}
    for row in source:
        try:
         result=re.search("Text_(.*) =",row)
         strings_source[result.group(1)]=row
        except:
            pass
    with open("input/battle_message.c") as f:
        to_translate=f.readlines()
    for i in range(len(to_translate)):
        try:
         result=re.search("Text_(.*) =",to_translate[i])
         to_translate[i]=strings_source[result.group(1)]
        except:
            pass
    with open("output/battle_message.c",'w') as f:
        f.write(''.join(to_translate))


def trad_strings():
    with open("data/str.c") as f:
        source=f.readlines()
    strings_source={}
    for row in source:
        try:
         result=re.search("gText_(.*) =",row)
         strings_source[result.group(1)]=row
        except:
            pass
    with open("input/strings.c") as f:
        to_translate=f.readlines()
    for i in range(len(to_translate)):
        try:
         result=re.search("gText_(.*) =",to_translate[i])
         to_translate[i]=strings_source[result.group(1)]
        except:
            pass
    with open("output/strings.c",'w') as f:
        f.write(''.join(to_translate).replace("{Pco}","PCo"))
trad_battle_message()