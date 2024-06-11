import keyMapping


def encrypt(key, message):
    """
    Fonction qui chiffre le message.
    encrypt(key, message)

    Paramètres :
    key (dict): clé de mappage.
    message (string): mesage à chiffrer

    Return :
    string : le message chiffré
    """
    # Va contenir le message chiffré
    secret = ""
    for c in message:
        # On mappe seulement les caracteres
        # de notre alphabete
        if c in key:
           secret += key[c]
        else:
           secret += c
    # Vous devez créer une boucle for qui vérifie si le caractère est dans
    # dans la clé de mappage. Si oui, on le substitue. Sinon, on le
    # le remet tel quel.
    #--- code à ajouter ---
    return secret

