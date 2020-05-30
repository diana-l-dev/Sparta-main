people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

for person in people:
    print(person['name'], person['age'])

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return

print(get_age('john'))
print(get_age('carry'))
print(get_age('bob'))

