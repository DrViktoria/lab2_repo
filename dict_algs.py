ivan = {
    "name": "Ivan",
    "age": 28,
    "children": [{
        "name": "Andrey",
        "age": 12,
    }, {
        "name": "Alina",
        "age": 10,
    }],
}

darja = {
    "name": "Darja",
    "age": 35,
    "children": [{
        "name": "Olya",
        "age": 19,
    }, {
        "name": "Pavel",
        "age": 7,
    }],
}


emps = [ivan, darja]

for el in emps:
    for i in el['children']:
        if i['age' ] >18:
            print (el['name'])
            break
