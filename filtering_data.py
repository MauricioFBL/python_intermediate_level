DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    python_devs = [pearson['name'] for pearson in DATA if pearson['language'] =='python']
    print(python_devs)
    platzi_workers = [pearson['name'] for pearson in DATA if pearson['organization'] =='Platzi']
    print(platzi_workers)
    adult_people = list(filter(lambda worker: worker['age'] > 18 , DATA))
    adult_people = list(map(lambda worker: worker['name'] , adult_people))
    print(adult_people)
    adult_people = [pearson['name'] for pearson in DATA if pearson['age'] > 18]
    print(adult_people)
    # SOLO FUNCIONA N PYTHON3.9 O POSTERIOR
    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 60 } , DATA))c
    old_people = list(filter(lambda worker: worker['age'] > 60 , DATA))
    old_people = list(map(lambda worker: worker['name'] , old_people))
    print(old_people)
    old_people = [pearson['name'] for pearson in DATA if pearson['age'] > 70]
    print(old_people)
    python_devs = list(filter(lambda worker: worker['language'] =='python', DATA))
    python_devs = list(map(lambda worker: worker['name'] , python_devs))
    print(python_devs)
    platzi_workers = list(filter(lambda worker: worker['organization'] =='Platzi', DATA))
    platzi_workers = list(map(lambda worker: worker['name'] , platzi_workers))
    print(platzi_workers)



if __name__ == '__main__':
    run()