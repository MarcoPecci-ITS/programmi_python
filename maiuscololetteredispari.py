def alternate_casing(text):

    return "".join([
        char.lower() if idx % 2 else char.upper()
        for idx, char in enumerate(text)])


print(alternate_casing("Ciao Mondo!"))