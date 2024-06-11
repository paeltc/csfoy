def generate_key(n):
    """
    generate_key(n)
    Fonction qui genere une cle pour le chriffrement
    On passe un entier qui en fait la vrai cle

    Parametre
    n (int) : entier, cle de chriffrement

    Return
    Dictionnaire : la cle de mappagae 
    """
    # Lettre utiliser pour le mappage
    lettres = "abcdefghijklmnopqrstuvwxyz"

    # Nous allons utiliser un dictionnaire pour faire le mapage
    key  = {}
    cnt = 0
    # Genere la clé
    for c in lettres:
        # le module permet de gerer un nombre qui deborde du nombre du  nombre de lettre
        # le module permet de redemarrer au debut si la valeur de c est
        # grand que 25
        key[c] = lettres[(cnt + n)  % len(lettres)]
        cnt += 1
    return key
