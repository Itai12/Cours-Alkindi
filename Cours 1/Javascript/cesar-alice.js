function plus_frequente(message){
    frequence_max=0;
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(i of alphabet){
        if((message.split(i).length - 1)>frequence_max){
            frequence_max=(message.split(i).length - 1);
            lettre=i;
        }
    }
    return(lettre);
}
function dechiffre_message(message){
    message_final="";
    decalage=plus_frequente(message);
    for(i of message){
        position_lettre=i.charCodeAt(0)-65;
        position_decalage=decalage.charCodeAt(0)-65;
        position_finale=(position_lettre-position_decalage)%26;
        message_final+=String.fromCharCode(position_finale+65);
    }
    return(message_final);
}