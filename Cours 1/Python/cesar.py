import unidecode
message=input("Saisissez un message a chiffrer : ")
decalage=input("Saisissez le decalage : ").upper()
message=unidecode.unidecode(message).replace(" ","").upper()
def chiffre(lettre,decal):
    position_lettre=ord(lettre)-65
    position_decal=ord(decal)-65
    position_finale=(position_lettre+position_decal)%26
    return chr(65+position_finale)
message_chiffre=""
for i in message:
    message_chiffre+=chiffre(i,decalage)
print(message_chiffre)