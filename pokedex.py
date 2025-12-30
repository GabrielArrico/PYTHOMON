from cls import Pokemon, Habilidades

habilidades = {
    "ascuas" : Habilidades("[(🔥) ascuas]", "Fuego", 40, 100),
    "latigo sepa" : Habilidades("[(🍃) Latigo Sepa]", "Planta", 40, 100),
    "hidro bomba" : Habilidades("[(🌊) Hidro Bomba]", "Agua", 110, 80),
    "trueno" : Habilidades("[⚡] Trueno", "Electrico", 110, 70)

}
Pokemones = {

    "venusaur" : Pokemon("venusaur", "Planta", 80, 82, 83, 80,[habilidades["latigo sepa"]]),
    "charizard" : Pokemon("charizard", "Fuego", 78, 84, 78, 100, [habilidades["ascuas"]]),
    "blastoise" : Pokemon("blastoise", "Agua", 79, 83, 100, 78, [habilidades["ascuas"]]),
    "zapdos" : Pokemon("Zapdos", "Electrico", 90, 90, 85, 100, [habilidades["trueno"]] )
}
