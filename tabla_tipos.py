

tabla_tipos= {

    "Fuego": {
        "Agua" : 0.5,
        "Fuego" : 0.5,
        "Roca" : 0.5,
        "Planta" : 2.0,
        "Electrico" : 1.0
    },

    "Agua": {
        "Agua" : 0.5,
        "Fuego" : 2.0,
        "Roca" : 2.0,
        "Planta" : 0.5,
        "Electrico" : 0.5
    },

    "Planta": {
        "Agua" : 2.0,
        "Fuego" : 0.5,
        "Roca" : 2.0,
        "Planta" : 0.5,
        "Electrico" : 0.05
    },

    "Roca": {
        "Agua" : 0.5,
        "Fuego" : 1.0,
        "Roca" : 0.5,
        "Planta" : 0.5,
        "Electrico" : 2.0
    },

    "Electrico": {
        "Agua" : 2.0,
        "Fuego" : 0.5,
        "Roca" : None,
        "Planta" : 0.5,
        "Electrico" : 0.5
    }
}