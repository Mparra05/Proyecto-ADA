"""
Level-Up Game Solver

Este script implementa una solución para el problema de Level-Up, en el que un jugador debe pasar por 
varios reinos enfrentándose a monstruos y optimizando su estrategia para alcanzar el nivel máximo 
con la mínima cantidad de vida inicial necesaria.

Autor:  Juan Sebastian Ospina Maya 2041554-2724
        Manuel Alejandro Parra Buitrago - 2043270-2724

Versión: 1.0

Descripción:
- Entrada: Archivos .in con casos de prueba que incluyen reinos, monstruos y niveles.
- Salida: Archivos .out con la mínima vida inicial requerida para cada caso.

Instrucciones:
1. Ejecutar este script con archivos de entrada y salida específicos.
2. Los casos se leen desde un archivo .in y los resultados se escriben en un archivo .out.
3. Requiere Python 3.7 o superior.

Estructura del Código:
1. `read_input_output`: Manejo de archivos .in y .out.
2. `simulate_game`: Simulación de los reinos para calcular la vida inicial mínima.
3. `main`: Ejecución principal.

Uso:
    python level_up.py

"""

def can_finish_game(n, m, heal, realms, initial_hp):
    """
    Función para verificar si se puede terminar el juego con un HP inicial dado.
    """
    current_hp = initial_hp
    current_level = 1  # Nivel inicial del jugador
    
    for mobs in realms:
        mobs.sort()  # Ordenar mobs por fuerza (estrategia óptima)
        damage = 0
        kills = 0
        
        for mob in mobs:
            damage += mob
            if current_hp - damage <= 0:  # No sobrevivimos este ataque
                return False
            kills += 1
            if kills + current_level >= m:  # Alcanzamos el nivel máximo
                current_level = m
                break
        
        # Actualizar el nivel después de matar todos los mobs
        current_level = min(m, current_level + kills)
        # Recuperar HP basado en el nivel actual
        current_hp += heal[current_level - 1]
    
    return current_level == m

def minimum_initial_hp(cases):
    """
    Calcula el HP inicial mínimo para cada caso de prueba.
    """
    results = []
    for n, m, heal, realms in cases:
        low, high = 1, 10**6
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_finish_game(n, m, heal, realms, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        results.append(answer)
    return results

def read_input_output(input_file, output_file):
    """
    Leer datos del archivo .in y escribir resultados en el archivo .out.
    """
    with open(input_file, 'r') as fin:
        c = int(fin.readline().strip())  # Número de casos de prueba
        cases = []
        for _ in range(c):
            n, m = map(int, fin.readline().strip().split())
            heal = list(map(int, fin.readline().strip().split()))
            realms = []
            for _ in range(n):
                mobs = list(map(int, fin.readline().strip().split()))[1:]  # Omitir el número de mobs
                realms.append(mobs)
            cases.append((n, m, heal, realms))
    
    results = minimum_initial_hp(cases)
    
    with open(output_file, 'w') as fout:
        for result in results:
            fout.write(f"{result}\n")

if __name__ == "__main__":

    # Cambiar los nombres de archivo según sea necesario para pruebas locales
    input_file = r"c:/Users/manue/OneDrive/Escritorio/Proyecto ADA/Level-Up/b.in"
    output_file = r"c:/Users/manue/OneDrive/Escritorio/Proyecto ADA/Level-Up/b.out"
    read_input_output(input_file, output_file)