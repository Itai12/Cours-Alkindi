function chiffre_message(message,substitution){
    subsitution_reciproque=Object.fromEntries(Object.entries(substitution).map(([ key, val ]) => [ val,key ]));
    message_final="";
    for(i of message){
        message_final+=substitution_reciproque[i];
    }
    return(message_final);
}