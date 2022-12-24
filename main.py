import re
import csv
from functions import *

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Questions
while True:
    try:
        release={'y':True,'n':False}[input("Would you like to use last releases (of rhh) files as input ? [y/n]\n>>> ").lower()]
        break
    except:
        error(2)
if release:
    with open("input/species.h",'w') as f:
        import requests
        f.write((requests.get('https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/master/src/data/text/species_names.h')).text)
while True:
    try:
        lc={"1":"5","7":"9","6":"1","5":"3","2":"6","4":"8","3":"7"}[input("Choose a language:\n_______\n1. French\n2. German\n3. Spanish\n4. Italian\n5. Korean\n6. Japanese\n7. English\n_______\n>>> ")]
        break
    except:
        error(1)
if lc=='5':
    print("French names already have reducted forms done so you wont have any further thing to change in this file. Don't worry if you chose 'no' for manual fix.")
while True:
    try:
        handfix={'y':True,'n':False}[input("Would you like to manually shorten the arrays that exceeds the max during the translation ? [y/n]\n>>> ").lower()]
        break
    except:
        error(2)
if not handfix:
   while True:
    try:
        savefile={'y':True,'n':False}[input("Would you like to save a file with all names that exceeds the limit ? [y/n]\n>>> ").lower()]
        break
    except:
        error(2)
else:
    savefile=False
if savefile:
    with open('excess_names.txt','w') as f:
     pass
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Species names
with open("input/species.h") as f:
    content=f.read()
    content=content.replace('''("''',"<").replace('''")''',">").replace("'","’").replace("Flechinder","Fletchinder").replace("Crabminabl","Crabominable").replace("Blacephaln","Blacephalon").replace("Corvisquir","Corvisquire").replace("Corviknigh","Corviknight").replace("Barraskewd","Barraskewda").replace("Centiskorc","Centiskorch").replace("Polteageis","Polteageist").replace("Stonjourne","Stonjourner")
    result=re.findall("_<(.*)>,",content)
del(result[0])
with open("data/species.csv",newline='',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    dico = {}
    for row in reader:
        if row['local_language_id'] == lc:
            if len(row['name'])>10:
              a = (row['name'])
              if handfix:
                while len(a)>10:
                    a=input(f"Actual name : {a} ; Exceeds by {len(a)-10}\nNew name : ")
              else:
                if lc=='5':
                  a=autonames[a]
                else:
                 if not savefile:
                  a=a[:-len(a)-10]
            else:
             a = (row['name'])
            dexs = row["pokemon_species_id"]
        if row['local_language_id'] == "9":
            dico[row['name'].replace("â™€","♂").replace("â™€","♀")] = a
for i in range(len(dico)):
      content = content.replace(result[i],dico[result[i]]).replace(">",'''")''').replace("<",'''("''')
if savefile:
    for name in dico.values():
        if len(name)>10:
            with open('excess_names.txt','a') as f:
                    f.write(f"- Name : {name} ; Exceeds by {len(name)-10}\n")
with open("output/species.h",'w') as f:
    f.write(content)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------