def cislo(soubor : str):
    with open(soubor, 'r') as file:
        cislo = int(file.read().strip())
    nove_cislo = cislo + 1
    with open(soubor, 'w') as file:
        file.write(str(nove_cislo))
    return str(cislo)