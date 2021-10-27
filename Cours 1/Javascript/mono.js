function chiffre_message(message,substitution){
    message_final="";
    for(i of message){
        message_final+=substitution[i];
    }
    return(message_final);
}