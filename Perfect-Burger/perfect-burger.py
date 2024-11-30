"""
Perfect Burger Solver

Este script implementa una solución para el problema de Perfect Burger, en el que Zlatan debe cocinar 
hamburguesas perfectamente. Cada lado de la carne debe cocinarse exactamente 'n' minutos, y Zlatan 
solo puede voltear la carne durante intervalos de tiempo específicos.

Autor:  Juan Sebastian Ospina Maya 2041554-2724
        Manuel Alejandro Parra Buitrago - 2043270-2724

Versión: 1.0

Descripción:
- Entrada: Archivos .in con casos de prueba que incluyen el tiempo requerido por lado, el número de 
  intervalos, y los intervalos disponibles para voltear la carne.
- Salida: Archivos .out indicando si es posible cocinar la hamburguesa perfectamente y, de ser posible, 
  el número mínimo de volteos necesarios.

Instrucciones:
1. Ejecutar este script con archivos de entrada y salida específicos.
2. Los casos se leen desde un archivo .in y los resultados se escriben en un archivo .out.
3. Requiere Python 3.7 o superior.

Estructura del Código:
1. `perfect_burger_solver`: Determina si es posible cocinar la hamburguesa perfectamente y calcula 
   el número mínimo de volteos necesarios.
2. `read_and_write_files`: Maneja la lectura de archivos de entrada (.in) y escritura de archivos de salida (.out).
3. `main`: Lógica principal para ejecutar el programa con argumentos específicos.


"""

def perfect_burger(cases):
    results = []
    for n, k, intervals in cases:
        # Estado inicial: los lados de la carne deben cocinarse exactamente n minutos cada uno.
        total_grill_time = 2 * n
        flip_count = 0
        current_time = 0
        grill_state = [0, 0]  # Tiempo cocinado para cada lado
        
        for start, end in intervals:
            if grill_state[0] < n:  # Si el primer lado no está listo
                time_to_flip = min(n - grill_state[0], end - max(start, current_time))
                if time_to_flip > 0:
                    grill_state[0] += time_to_flip
                    current_time = max(current_time, start) + time_to_flip
                    flip_count += 1
            
            if grill_state[1] < n:  # Si el segundo lado no está listo
                time_to_flip = min(n - grill_state[1], end - max(start, current_time))
                if time_to_flip > 0:
                    grill_state[1] += time_to_flip
                    current_time = max(current_time, start) + time_to_flip
                    flip_count += 1
            
            if grill_state[0] >= n and grill_state[1] >= n:
                results.append((True, flip_count))
                break
        else:
            # Si no logramos cocinar ambos lados correctamente
            results.append((False, 0))
    return results

def read_and_write_files(input_file, output_file):
    """
    Leer los datos desde un archivo .in y escribir los resultados en un archivo .out
    """
    with open(input_file, 'r') as fin:
        lines = fin.readlines()
    
    c = int(lines[0].strip())  # Número de casos de prueba
    cases = []
    index = 1
    
    for _ in range(c):
        n, k = map(int, lines[index].strip().split())
        index += 1
        intervals = []
        for _ in range(k):
            li, ri = map(int, lines[index].strip().split())
            intervals.append((li, ri))
            index += 1
        cases.append((n, k, intervals))
    
    # Resolver los casos
    results = perfect_burger(cases)
    
    with open(output_file, 'w') as fout:
        for success, flips in results:
            if success:
                fout.write("Perfect burger!\n")
                fout.write(f"{flips}\n")
            else:
                fout.write("Another bland and poorly cooked burger!\n")

if __name__ == "__main__":
    # Cambiar estos nombres de archivo para pruebas locales
    input_file = r"c:/Users/manue/OneDrive/Escritorio/Proyecto ADA/Perfect-Burger/B.in"
    output_file = r"c:/Users/manue/OneDrive/Escritorio/Proyecto ADA/Perfect-Burger/B.out"
    read_and_write_files(input_file, output_file)