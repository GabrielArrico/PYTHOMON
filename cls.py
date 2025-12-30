from tabla_tipos import tabla_tipos
import random

# Obtiene el multiplicador de ataque:
def obtener_multiplicador(tipo_ataque, tipo_oponente): #movimiento.tipo, oponente.tipo
    return tabla_tipos.get(tipo_ataque, {}).get(tipo_oponente, 1.0) # Si este no es encontrado devolvera un dmg neutro de 1.0


class Habilidades:

    def __init__(self, nombre, tipo, potencia, precision):
        self.nombre = nombre
        self.tipo = tipo
        self.potencia = potencia
        self.precision = precision


class Pokemon:

    def __init__(self, nombre, tipo, HP, ataque, defemsa, velocidad, habilidades):
        self.nombre = nombre
        self.tipo = tipo
        self.hp_total = HP
        self.hp_actual = HP
        self.ataque = ataque
        self.defensa = defemsa
        self.velocidad = velocidad
        self.habilidades = habilidades

    #Mostrar por consola brra de vida
    def mostrar_barra_vida(self):

        largo_total = 20 # Nimer de caracteres que mide la barra

        #Calculamos cuentos bloques llenar #aseguramos que el procentaje no sea menoa a 0
        porcentaje = max(0, self.hp_actual / self.hp_total)
        bloques_llenos = int(porcentaje * largo_total)

        #cREACION DE LA BARRA: caracteres llenos + cracteres vacios:
        barra = "█" * bloques_llenos
        fondo = "░" * (largo_total - bloques_llenos)

        # colores, verde si > 50 %,  amarillo < -50%, Rojo < 20%
        color = "\033[92m"
        if porcentaje < 0.5: color = "\033[93m"
        if porcentaje < 0.2: color = "\033[91m"
        reset = "\033[0m"

        print(f"\n{self.nombre.upper():<12} {color}[{barra}{fondo}]{reset} {self.hp_actual}/ {self.hp_total} HP\n")


    def atacar(self, oponente, habilidad):

        print(f" \n[+] {self.nombre.upper()} Utilizo {habilidad.nombre.upper()} contra {oponente.nombre.upper()}\n")

        oponente.mostrar_barra_vida()

        # sistema de Precision:
        if random.randint(1,100) > habilidad.precision:
            print(f"... {self.nombre} Fallo!")
            return
        
        # Multiplicador
        multiplicador = obtener_multiplicador(habilidad.tipo, oponente.tipo)
        # Saber si fue efectivo o no.
        if multiplicador >= 1: print(f"[+] Ha Sido SUPER EFECTIVO")
        if multiplicador < 1: print(f"[!] No ha sido muy EFICAZ")
        if multiplicador == 0: print(f"[X] No tiene EFECTO")

        # Calculo de dmg con variacion
        variacion = random.uniform(0.85, 1.0) # Calculo de una variacion aleatoria (0.85 a 1.0) para que no sea siempre igual
        dmg = int((self.ataque / oponente.defensa) * habilidad.potencia * multiplicador * variacion)
        
        # aplicar de dmg corregido
        oponente.hp_actual = max(0, oponente.hp_actual - dmg)
        
        # Interfaz
        oponente.mostrar_barra_vida()

        if oponente.hp_actual == 0:
            print(f"{oponente.nombre} ha sido debilitado.")


        

    
   
        
