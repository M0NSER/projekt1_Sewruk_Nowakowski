my_touple = (
    ("tomasz sewruk", "123123"), ("stefan nowak", "234234"), ("bogumil wars", "123456"), ("alicja kazamat", "987789"),
    ("michal", "675456"))

my_touple2 = (
    (("imie", "tomasz"), ("nazwisko", "sewruk"), ("nr_albumu", "123123")),
    (("imie", "stefan"), ("nazwisko", "nowak"), ("nr_albumu", "234234"))
)

#    (("imie", "stefan"), ("nazwisko", "nowak"), ("nr_albumu", "234234"))

# for i in my_touple:
#    print(i)

my_dict = dict(my_touple)
#print(my_dict)



for i in my_touple2:
    for j in i:
        print("-",j)

#print(dict(my_touple2))
