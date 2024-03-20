def uncensor(frase, vocali):
    output = "".join(vocali[idx] if lettera == '*' else lettera
                     for idx, lettera in enumerate(frase))
    output = []
    idx = 0
    for char in frase:
        if char == '*':
            output.append(vocali[idx])
            idx += 1
        else:
            output.append(char)

    return "".join(output)


uncensor("H*ll* W*rld", "eoo")
