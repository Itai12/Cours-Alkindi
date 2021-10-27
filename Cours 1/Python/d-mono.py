message=input("Saisissez un message a déchiffrer : ")
import unidecode
message=unidecode.unidecode(message).replace(" ","").upper()
permutation={"A":"M","B":"K"}
permutation_inverse={objet:clef for clef,objet in permutation.items()}
# à compléter en recopiant la permutation
message_final=""
for i in message:
    message_final+=permutation_inverse[i]
print(message_final)