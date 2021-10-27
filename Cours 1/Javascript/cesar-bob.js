function dechiffre_message(message){
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for(j of alphabet){
        message_final="";
        for(i of message){
            position_lettre=i.charCodeAt(0)-65;
            position_decalage=decalage.charCodeAt(0)-65;
            position_finale=(position_lettre-position_decalage)%26;
            message_final+=String.fromCharCode(position_finale+65);
        }
        console.log(message_final);
    }
}