def foo3(text, letter):
    result = []
    for i in text:
        if(i != letter):
            result.append(i)
    return ''.join(result)


print(foo3("Ula jest suuuuuuper", "u"))