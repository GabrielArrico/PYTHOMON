from pokedex import habilidades, Pokemones
from tabla_tipos import tabla_tipos
from cls import Pokemon, Habilidades
import random

def batalla (p1, p2):

    print(f"\n[!] La Batalla entre\n {p1.nombre.upper()} 🆚 {p2.nombre.upper()}")

    while p1.hp_actual > 0 and p2.hp_actual > 0:

        if p1.velocidad > p2.velocidad:
            orden = [[p1, p2, True], [p2, p1, False]]
        else:
            orden = [[p2, p1, False], [p1, p2, True]]

    
        for atacante, oponente, es_jugador in orden:
            #si alguien ya se debilito en este turno, el otro no ataca
            if atacante.hp_actual <= 0 or oponente.hp_actual <= 0:
                continue

            if es_jugador:
                print(f"Turno de {atacante.nombre}")
            #enumera las habiliaddes y elije alguna
                for i, m in enumerate(atacante.habilidades):
                    print(f"{i} - {m.nombre} [POTENCIA: {m.potencia}] [TIPO: {m.tipo}]")

            #el jugor elige

                try:
                    eleccion = int(input("..."))
                    mov_elegido = atacante.habilidades[eleccion]
                except (ValueError, IndexError):
                    print(f"Seleccion no valida, usando el primer movimiento por defecto")
                    mov_elegido = atacante.habilidades[0]
            else:

                mov_elegido = random.choice(atacante.habilidades)

        
            atacante.atacar(oponente, mov_elegido)
        

            if oponente.hp_actual <= 0:
                print(f"🏆 ¡EL GANADOR ES {atacante.nombre.upper()}!")
                return
        

# import copy

# # Crea una copia independiente del objeto
# p1 = copy.deepcopy(Pokemones.get("venusaur"))
# p2 = copy.deepcopy(Pokemones.get("venusaur"))

# Ahora p1 puede golpear a p2 sin herirse a sí mismo

p1 = Pokemones.get("zapdos")
p2 = Pokemones.get("charizard")
batalla(p1, p2)
