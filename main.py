import re
import csv
from functions import *
from webscrap import findmove
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Questions

while True:
    try:
        release={'y':True,'n':False}[input(colored("Would you like to use last releases (of rhh) files as input ? [y/n]\n>>> ",150,150,50)).lower()]
        break
    except:
        error(2)
if release:
    with open("input/species_names.h",'w') as f:
        import requests
        f.write((requests.get('https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/master/src/data/text/species_names.h')).text)
    with open("input/items.h",'w') as f:
        import requests
        f.write((requests.get('https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/master/src/data/items.h')).text)
    with open("input/move_names.h",'w') as f:
        import requests
        f.write((requests.get('https://raw.githubusercontent.com/rh-hideout/pokeemerald-expansion/master/src/data/text/move_names.h')).text)
while True:
    try:
        lc={"1":"5","7":"9","6":"1","5":"3","2":"6","4":"8","3":"7"}[input(colored("Choose a language:\n_______\n1. French\n2. German\n3. Spanish\n4. Italian\n5. Korean\n6. Japanese\n7. English\n_______\n>>> ",150,150,50))]
        break
    except:
        error(1)
if lc=='5':
    print(colored("French names already have reducted forms done so you wont have any further thing to change in this file. Don't worry if you chose 'no' for manual fix.",100,200,100))
while True:
    try:
        handfix={'y':True,'n':False}[input(colored("Would you like to manually shorten the arrays that exceeds the max during the translation ? [y/n]\n>>> ",150,150,50)).lower()]
        break
    except:
        error(2)
if not handfix:
   while True:
    try:
        savefile={'y':True,'n':False}[input(colored("Would you like to save a file with all names that exceeds the limit ? [y/n]\n>>> ",150,150,50)).lower()]
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
def trad_pokemon_names():
    print(colored("Translation of Pokémon names...",0,200,200))
    with open("input/species_names.h") as f:
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
                      pass
                else:
                 a = (row['name'])
                 dexs = row["pokemon_species_id"]
            if row['local_language_id'] == "9":
                dico[row['name'].replace("â™€","♂").replace("â™€","♀")] = a
    for i in range(len(dico)):
        content = content.replace(result[i],dico[result[i]]).replace(">",'''")''').replace("<",'''("''').replace("’","'")
    if savefile:
        for name in dico.values():
            if len(name)>10:
                with open('excess_names.txt','a') as f:
                        f.write(f"- Pokémon name : {name} ; Exceeds by {len(name)-10}\n")
    with open("output/species_names.h",'w') as f:
        f.write(content)
    print(colored("Done !",0,250,200))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Items names
def trad_items_names():
    print(colored("Translation of items names...",0,200,200))
    with open("input/items.h") as f:
        content=f.read()
    with open("data/items_names.csv",newline='',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        dico = {}
        for row in reader:
            if row['local_language_id']==lc:
                a=row['name']
            if row['local_language_id']=='9':
                dico[row['name']]=a
    content=content.replace('''("''',"<").replace('''")''',">")
    result=re.findall("_<(.*)>,",content)
    dico['????????']='????????'
    for item in result:
        if lc=='5':
         dico[item]=dico[item.replace("Feather"," Feather").replace("Capsle"," Capsule").replace("Yellw","Yellow ").replace("GreenAp","Green Ap").replace("WhiteAp","White Ap").replace("BlackAp","Black Ap").replace("Electrc","Electric ").replace("Fightng","Fighting ").replace("PsychicM","Psychic M").replace("iteX","ite X").replace("iteY","ite Y").replace("Poisinium Z","Poisonium Z").replace("U-N","Ultran").replace("DeepSea","Deep Sea ").replace("tIce","t Ice").replace("'","’").replace("Weaknss","Weakness ").replace("SafetyGoggles","Safety Goggles").replace("AdrenalineOrb","Adrenaline Orb").replace("TerainExtendr","Terrain Extender").replace("ProtectvePads","Protective Pads").replace("MCHN","Machine").replace("{POKEBLOCK}","Pokéblock").replace(" Ticket","Ticket").replace("S.S.Ticket","S.S. Ticket").replace("EonTicket","Eon Ticket").replace("Oak’s","Oak's").replace("PewtrCrnches","Pewter Crunchies").replace("RageCandyBar","Rage Candy Bar").replace("CasteliaCone","Casteliacone").replace("LumioseGlete","Lumiose Galette").replace("ShalourSable","Shalour Sable").replace("AbilityPatch","Ability Patch").replace("Exp.Candy","Exp. Candy").replace("DynamaxCandy","Dynamax Candy").replace("MaxMushrooms","Max Mushrooms").replace("GoldBottlCap","Gold Bottle Cap").replace("StrngeSouvnr","Strange Souvenir").replace("Fosslzed","Fossilized ").replace("Drke","Drake").replace("SurprseMulch","Surprise Mulch").replace("WishingPiece","Wishing Piece").replace("GalaricaTwig","Galarica Twig").replace("GalaricaCuff","Galarica Cuff").replace("GalrcaWreath","Galarica Wreath").replace("StrwbrySweet","Strawberry Sweet").replace("Rusted","Rusted ").replace("Heavy-DtyBts","Heavy-Duty Boots").replace("UtltyUmbrlla","Utility Umbrella").replace("BlundrPolicy","Blunder Policy").replace("CatchngCharm","Catching Charm").replace("RotomCatalog","Rotom Catalog").replace("ReinsOfUnity","Reins of Unity").replace("{PKMN} Box Link","Pokémon Box Link")].replace("’","'").replace("Poussière Étoile","Pouss. Étoile").replace("Morceau d'Étoile","Morc. Étoile").replace("CoquilleTréfonds","Coqu.Tréfonds").replace("Fossile Racine","FossileRacine").replace("Fossile Griffe","FossileGriffe").replace("Fossile Armure","FossileArmure").replace("Fossile Plaque","FossilePlaque").replace("Foss. Mâchoire","Foss.Mâchoire").replace("Foss. Nageoire","Foss.Nageoire").replace("Noigrume Rouge","NoigrumeRouge").replace("Noigrume Jaune","NoigrumeJaune").replace("Noigrume Blanc","NoigrumeBlanc").replace("Sachet Senteur","SachetSenteur").replace("Plaque Toxicité","PlaqueToxique").replace("Plaque Insecte","PlaqueInsecte").replace("Plaque Fantôme","PlaqueFantôme").replace("Joyau Électrik","JoyauÉlectrik").replace("Joyau Ténèbres","JoyauTénèbres").replace("Marshadozélite","Marshadzélite").replace("Ultranécrozélite","U-Nécrozélite").replace("Encens Bizarre","EncensBizarre").replace("Bracelet Macho","BraceletMacho").replace("Poignet Pouvoir","PoignePouvoir").replace("Ceinture Pouvoir","Ceint.Pouvoir").replace("Lentille Pouvoir","LentillePouv.").replace("Bandeau Pouvoir","Band. Pouvoir").replace("Chaîne Pouvoir","ChaînePouvoir").replace("Graîne Miracle","GraîneMiracle").replace("Glace Éternelle","GlacÉternelle").replace("Ceinture Noire","Ceint. Noire").replace("Cuillère Tordue","Cuill. Tordue").replace("Poudre Argentée","PoudrArgentée").replace("Lunettes Noires","Lun. Noires").replace("Lunettes Choix","Lun. Choix").replace("Mouchoir Choix","Mouch. Choix").replace("Graine Électrik","GraineÉlectrk").replace("Graine Psychique","Graine Psych.").replace("Lichen Lumineux","Lichen Lumin.").replace("Boule de Neige","BouleDeNeige").replace("Rune Purifiante","Rune Purif.").replace("Bandeau Muscle","BandeauMuscle").replace("Lunettes Sages","LunettesSages").replace("Ceinture Force","Ceint. Force").replace("Bande Étreinte","BandeÉtreinte").replace("Vulné-Assurance","Vulné-Assur.").replace("Veste de Combat","VesteDeCombat").replace("Lunettes Filtre","Lun. Filtre").replace("Vélo de Course","VéloDeCourse").replace("Boîte Pokéblocs","BoîtePokébloc").replace("Lettre à Pierre","Let. à Pierre").replace("Lunettes Sable","Lun. Sable").replace("Passe Concours","PasseConcours").replace("Carte Magnétique","Carte Magnét.").replace("Super Repousse","SuperRepousse").replace("Graine Miracle","GraineMiracle").replace("Galette","Gal. ").replace("Sablé","S. ").replace("Aromate","Arom.").replace("p. X","p.X").replace("Bonbon Dynamax","Bonbon Dynam.").replace("Capsule","Cap.").replace("Morceau","Morc. ").replace("Bibelot","Bib. ").replace("Fossile","Foss.").replace("Branche","B. ").replace("Pomme ","Pomme").replace("Théière","Thé.").replace("Bracelet","Brac.").replace(" en Sucre"," Sucre").replace("Couronne","Cour.").replace("Bouclier","Bouc.").replace("Grosses Bottes","GrossesBottes").replace("Assurance","Assur.").replace("Chariot ","Char.").replace("Parapluie","Parap.").replace("Stabilité","Stab.").replace("Moti-","Moti").replace("Rênes de l'Unité","Rêne Unité").replace("Poignet Dyn","Poig.Dyn").replace("Foss. M","Foss.M").replace("Foss. N","Foss.N")
         
        elif len(dico[item])>13 and handfix:
          while len(dico[item])>13:
           dico[item]=input(f"Actual name : {dico[item]} ; Exceeds by {len(dico[item])-13}\nNew name : ")
        if savefile:
          if len(dico[item])>13:
            with open("excess_names.txt",'a') as f:
                f.write(f"- Item name : {dico[item]} ; Exceeds by {len(dico[item])-13}\n")
        content=content.replace('<'+item+'>','''("'''+dico[item]+'''")''')
    contenu=content.replace("<",'''("''').replace(">",'''")''').replace('''")= GEN''',">= GEN").replace("_CS","_HM").replace("_CT","_TM").replace("description = sCT","description = sTM").replace("description = sCS","description = sHM")
    with open('output/items.h','w') as f:
        f.write(content)
    print(colored("Done !",0,250,200))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Move names
def trad_move_names():
    print(colored("Translation of moves names...",0,200,200))
    with open("input/move_names.h") as f:
        content=f.read()
        content=content.replace('''("''',"<").replace('''")''',">").replace("'","’")
        result=re.findall("_<(.*)>,",content)
    with open("data/moves_names.csv",newline='',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        dico = {}
        for row in reader:
            if row['local_language_id'] == lc:
                if len(row['name'])>12:
                 a = (row['name'])
                 if handfix:
                    while len(a)>10:
                        a=input(f"Actual name : {a} ; Exceeds by {len(a)-10}\nNew name : ")
                 else:
                    if lc=='5':
                     pass
                    else:
                     if not savefile:
                      pass
                else:
                 a = (row['name'])
                 dexs = row["move_id"]
            if row['local_language_id'] == "9":
                dico[row['name'].lower().replace(' ','').replace('-','')] = a
    dico['-']='-'
    if lc=='5':
        dico['direclaw']='Grif.Funstes'
        dico['psyshieldbash']='Sprint Bouc.'
        dico['powershift']='Éch. Force'
        dico['stoneaxe']='Hache Pierre'
        dico['ragingfury']='Gr. Courroux'
        dico['wavecrash']='Aquatacle'
        dico['chloroblast']='Herblast'
        dico['mountaingale']='Bise Glacia.'
        dico['victorydance']='DanseVictoir'
        dico['headlongrush']='Assa.Frontal'
        dico['barbbarrage']='Multitoxik'
        dico['esperwing']='Ailes Psycho'
        dico['bittermalice']='Cœur Rancœur'
        dico['shelter']='Mur Fumigène'
        dico['triplearrows']='TripleFlèche'
        dico['infernalparade']='Cort.Funèbre'
        dico['ceaslessedge']='VaguesÀLames'
        dico['blekwndstorm']='T. Hivernal'
        dico['wildbltstorm']='T. Fulgurant'
        dico['sndsearstorm']='T. Pyrosable'
        dico['sprngtidestorm']='T. Passionné'
        dico['mystcalpower']='Force Mystik'
        dico['lunarblessng']='Prière Lun.'
        dico['takeheart']='Extravaill.'
        dico['thunderpunch']='Poing-Éclair'
    result=[name.lower().replace(" ",'') for name in result]
    for i in range(len(result)):
        result[i]=result[i].lower().replace("hyprspace hole","hyperspace hole").replace("healng","healing")
        try:
         content = content.replace("<"+result[i]+">",'''("'''+dico[result[i].replace(' ','').replace('-','')]+'''")''')
        except:
          try:
           content = content.replace("<"+result[i]+">",'''("'''+findmove(result[i])+'''")''')
          except:
            print(result[i])
    if savefile:
        for name in dico.values():
            if len(name)>12:
                with open('excess_names.txt','a') as f:
                        f.write(f"- Move name : {name} ; Exceeds by {len(name)-12}\n")
    with open("output/move_names.h",'w') as f:
        f.write(content.replace("’","'"))
    print(colored("Done !",0,250,200))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#All
def all():
    trad_pokemon_names()
    trad_items_names()
    trad_move_names()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    try:
        files={'1':'trad_pokemon_names()','2':'trad_items_names()','3':'trad_move_names()','4':'all()'}[input(colored("Choose files that you want to translate :\n_______\n1. src/data/text/species_names.h\n2. src/data/items.h\n3. src/data/text/move_names.h\n4. All\n_______\n>>> ",150,150,50)).lower()]
        break
    except:
        error(2)
eval(files)
print(colored("End of the execution, thank you for using my script ! ~ Arlequiin",0,255,0))