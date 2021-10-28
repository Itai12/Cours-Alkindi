message_chiffre=input("Saisissez un message a déchiffrer : ")
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import unidecode
message_chiffre=unidecode.unidecode(message_chiffre).replace(" ","").upper()
def dechiffre(lettre,clef):
     position_lettre=ord(lettre)-65
     position_clef=ord(clef)-65
     position_finale=(position_lettre-position_clef)%26
     return chr(65+position_finale)
for lettre in alphabet:
    message_dechiffre=""
    for i in message_chiffre:
        message_dechiffre+=dechiffre(i,lettre)
    print(message_dechiffre)
