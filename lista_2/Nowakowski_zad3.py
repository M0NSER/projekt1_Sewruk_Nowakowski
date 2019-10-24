def deleteLetter(text,letter):
    changedText=""
    for i in text:
        if i!=letter:
            changedText+=i
    return changedText
