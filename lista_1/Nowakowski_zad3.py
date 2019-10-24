class Person ():
    name="Szymon"
    surname="Nowakowski"
    age=13
    indeks="123456"

print('{} {} {:>3} {}'.format(Person().surname,Person().name, Person.age, '81-111'))

print('{:.3}{:.3}{:>3}'.format(Person().surname,Person().name, Person.indeks))
