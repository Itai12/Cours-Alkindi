def plus_frequente_2(texte):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionnaire={texte.count(i):i for i in alphabet}
    return dictionnaire[max(dictionnaire)]
message_chiffre=input("Saisissez un message a déchiffrer : ")
import unidecode
message_chiffre=unidecode.unidecode(message_chiffre).replace(" ","").upper()
plus_frequente=plus_frequente_2(message_chiffre)
position_lettre=ord(plus_frequente)-65
position_e=4
position_finale=(position_lettre-position_e)%26
clef=chr(position_finale+65)
def dechiffre(lettre,clef):
     position_lettre=ord(lettre)-65
     position_clef=ord(clef)-65
     position_finale=(position_lettre-position_clef)%26
     return chr(65+position_finale)
message_dechiffre=""
for i in message_chiffre:
     message_dechiffre+=dechiffre(i,clef)
print(message_dechiffre)