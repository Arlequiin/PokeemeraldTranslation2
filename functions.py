def error(n):
    errors=["Uncaught exception, please contact Arlequiin#1853 or open an issue in https://github.com/Arlequiin/PokeemeraldTranslation2",
    "You shoud choose a number between 1 and 7",
    "You shoud choose Y or N"
    ]
    print(colored("/!\ Error, "+errors[n],255,0,0))
def colored(text,r=200,g=200,b=200):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)
autonames = {
    "Blindépique":"Blindpique",
    "Excavarenne":"Excavarene",
    "Lépidonille":"Lépidonile",                   
    "Cabriolaine":"Cabrioline",
    "Pandespiègle":"Pandspiègl",
    "Cupcanaille":"Cupcanaile",
    "Desséliande":"Dessliande",
    "Banshitrouye":"Banshtroye",
    "Sonistrelle":"Sonstrelle",
    "Crabominable":"Crabminabl",
    "Froussardine":"Froussrdin",
    "Prédastérie":"Prédastrie",
    "Floramantis":"Flormantis",
    "Trépassable":"Trépassble",
    "Concombaffe":"Concombafe",
    "Denticrisse":"Dentcrisse",
    "Bamboiselle":"Bamboisele",
    "Engloutyran":"Engloutran",
    "Pierroteknik":"Pierotknik",
    "Rongourmand":"Rongourmnd",
    "Tournicoton":"Tourncoton",
    "Monthracite":"Montracite",
    "Grillepattes":"Grilepates",
    "Scolocendre":"Sclocendre",
    "Polthégeist":"Polthégest",
    "M. Glaquette":"M.Glaquete",
    "Frissonille":"Frisonille",
    "Pachyradjah":"Pachyradjh",
    "Dispareptil":"Dispareptl"
}