import re
def clean_type(string):

    if(re.search(r'\bpared',string, re.IGNORECASE) != None):
        return "Lamparas de pared"
    elif(re.search(r'\bpie',string, re.IGNORECASE) != None):
        return "Lamparas de pie"
    elif(re.search(r'\bterracota|cemento|base|kassl|madera|lino|asa|metal|bolas|cristal|lisa|cerámica|ratán',string, re.IGNORECASE) != None):
        return "Lamparas de mesa"
    else:
        return "Otros"


def clean_material(string):

    if(re.search(r'\bmetal|flexo',string, re.IGNORECASE) != None):
        return "Metal"
    elif(re.search(r'\bcemento',string, re.IGNORECASE) != None):
        return "Cemento"
    elif(re.search(r'\bmadera',string, re.IGNORECASE) != None):
        return "Madera"
    elif(re.search(r'\bratán',string, re.IGNORECASE) != None):
        return "Ratán"
    elif(re.search(r'\bterracota',string, re.IGNORECASE) != None):
        return "Terracota"
    elif(re.search(r'\bcerámica',string, re.IGNORECASE) != None):
        return "Cerámica"
    else:
        return "Otros"

def convert_to_float(x):
    return float(x.split(" ")[0].replace(",", ".")) 