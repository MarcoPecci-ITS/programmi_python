def uncensor(frase, vocali):

    output = []
    idx = 0
    for char in frase:
        if char == '*':
            output.append(vocali[idx])
            idx += 1
        else:
            output.append(char)

    return "".join(output)


print(uncensor("H*ll* W*rld!", "eoo"))
