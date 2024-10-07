def reveal_letters(letter, secret_word, discovered_word):

    discovered_word = list(discovered_word)

    for x in range(len(secret_word)):
        
        if secret_word[x].casefold() in "áàâãäa" and letter.casefold() in "áàâãäa":
            discovered_word[x] = secret_word[x]
            continue

        elif secret_word[x].casefold() in "éèêëe" and letter.casefold() in "éèêëe":
            discovered_word[x] = secret_word[x]
            continue

        elif secret_word[x].casefold() in "íìîïi" and letter.casefold() in "íìîïi":
            discovered_word[x] = secret_word[x]
            continue

        elif secret_word[x].casefold() in "óòôõöo" and letter.casefold() in "óòôõöo":
            discovered_word[x] = secret_word[x]
            continue

        elif secret_word[x].casefold() in "úùûüu" and letter.casefold() in "úùûüu":
            discovered_word[x] = secret_word[x]
            continue

        elif secret_word[x].casefold() in "çc" and letter.casefold() in "çc":
            discovered_word[x] = secret_word[x]
            continue
        
        elif letter.casefold() == secret_word[x].casefold():
            discovered_word[x] = secret_word[x]

    discovered_word = ''.join(discovered_word)

    return discovered_word