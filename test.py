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
trainer_class()