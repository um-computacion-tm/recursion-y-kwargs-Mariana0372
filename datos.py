def buscar_datos(*args, **kwargs):
    for key, persona in database.items():
        match = True
        for arg in args:
            if arg not in persona.values():
                match = False
                break
        if match:
            return key
    return None


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
    } ,
    4: {
        "nombre1": "Facundo",
        "nombre2": "Lucas",
        "apellido1": "Gustamente",
        "apellido2": "Huanca"
    } ,
    5: {
        "nombre1": "Luis",
        "nombre2": "Fernando",
        "apellido1": "Sombra",
        "apellido2": "Lopez"
    } ,
}


resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo" , "Gonzalez")
if resultado is not None:
    print(f"La persona se encuentra en la base de datos con el ID: {resultado}")
else:
    print("La persona no se encuentra en la base de datos.")





