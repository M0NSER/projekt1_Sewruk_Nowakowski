x =[i for i in range(10,1-1,-1)]


def foo7(text):
    result=""
    for i in range(len(text)-1,0-1,-1):
        result+=text[i]
    return result

print(foo7("Tomek"))