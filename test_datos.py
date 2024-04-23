def buscar_datos(*args, **kwargs):
    for key, persona in kwargs.items():
        match = True
        for arg in args:
            if arg not in persona.values():
                match = False
                break
        if match:
            return key
    return None

def test_buscar_datos():
    database = {
        1: {
            "nombre1": "Pablo",
            "nombre2": "Diego",
            "apellido1": "Ruiz",
            "apellido2": "Picasso"
        },
        2: {
            "nombre1": "Gaston",
            "apellido1": "Comas"
        },
        3: {
            "nombre1": "Elias",
            "nombre2": "Marcos",
            "nombre3": "Luciano",
            "apellido1": "Marcelo",
            "apellido2": "Gonzalez"
        },
        4: {
        "nombre1": "Facundo",
        "nombre2": "Lucas",
        "apellido1": "Gustamente",
        "apellido2": "Huanca"
        },
        5: {
        "nombre1": "Luis",
        "nombre2": "Fernando",
        "apellido1": "Sombra",
        "apellido2": "Lopez"
    },
    
    }

    
    assert buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **{1: database[1]}) == 1
    assert buscar_datos("Gaston", "Comas", **{2: database[2]}) == 2
    assert buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", **{3: database[3]}) == 3
    assert buscar_datos("Facundo" , "Lucas" , "Gustamante" , "Huanca", **{4: database[4]}) == 4
    assert buscar_datos("Luis" , "Fernando" , "Sombra" , "Lopez", **{5: database[5]}) == 5
    assert buscar_datos("Nombre", "NoExistente", **database) == None

test_buscar_datos()


