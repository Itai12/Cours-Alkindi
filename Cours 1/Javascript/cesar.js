function chiffre_message(message,decalage){
    message_final="";
    for(i of message){
        position_lettre=i.charCodeAt(0)-65;
        position_decalage=decalage.charCodeAt(0)-65;
        position_finale=(position_lettre+position_decalage)%26;
        message_final+=String.fromCharCode(position_finale+65);
    }
    return(message_final);
}