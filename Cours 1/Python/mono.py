message=input("Saisissez un message a chiffrer : ")
import unidecode
message=unidecode.unidecode(message).replace(" ","").upper()
substitution={"A":"M","B":"K"}
# à compléter en recopiant la substitution
message_final=""
for i in message:
    message_final+=substitution[i]
print(message_final)