def count_letters(letter, text):
    result = 0
    for i in text:
        if (i == letter):
            result += 1
    return result


imie = "Tomasz"
nazwisko = "Sewruk"

text = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print("W tekście jest ", count_letters(imie[2], text), "liter", imie[2], "oraz", count_letters(nazwisko[3], text),
      "liter", nazwisko[3])
