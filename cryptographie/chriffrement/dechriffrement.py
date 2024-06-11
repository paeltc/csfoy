import chriffrement
import keyMapping

def generate_dkey(n, secret):
    """
    dkey(key, messageCripte)
    Fonction qui génère une clé pour le chiffrement
    On passe un une cle de chriffrage et le message chriffe.

    Paramètres:
    dkey (string) : chaine de caractere, clé de chiffrement
    messageCripte (string): chaine de caractere, message chriffre

    Return
    Dictionnaire : la clé de mappage
    """
    dkey = keyMapping.generate_key(26-n)
    dsecret = chriffrement.encrypt(dkey,secret)

    return dsecret

# Verifions la cle  de mappage
#key = generate_key(3)
#print(key)

# Chriffrement du message
key = keyMapping.generate_key(3)
message = "paul elvis"
secret = chriffrement.encrypt(key,message)
print("Message chriffre: " + secret)

# Dechriffrement du message
dsecret = generate_dkey(3,secret)
print("Message dechriffre: " + dsecret)
