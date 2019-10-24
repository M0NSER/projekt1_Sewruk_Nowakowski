def makeDict(data_text):
    information={}
    length=len(data_text)
    letters=[]
    big_letters = data_text.upper()
    small_letters= data_text.lower()
    for i in data_text:
        letters.append(i)
    information["length"]=length
    information["letters"] = letters
    information["big_letters"] = big_letters
    information["small_letters"] = small_letters

    return information
