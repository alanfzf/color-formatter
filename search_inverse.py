
def procesar_archivos(archivo_a, archivo_b, salida_a, salida_b):
    with open(archivo_a, 'r') as f1, open(archivo_b, 'r') as f2, open(salida_a, 'w') as s1, open(salida_b, 'w') as s2:
        lineas_a = f1.readlines()
        lineas_b = f2.readlines()

        coincidencias_a = []
        coincidencias_b = []

        for linea_a in lineas_a:
            palabra_a = linea_a.split('{')[0].strip()

            for linea_b in lineas_b[:]:
                palabra_b = linea_b.split('{')[0].strip()

                if palabra_a == palabra_b:
                    contenido_b = linea_b.split('{', 1)[1].rsplit('}', 1)[0].strip()
                    nueva_linea_a = f"{palabra_a} {{ {contenido_b} }}, {linea_a.split(',', 1)[1]}"
                    coincidencias_a.append(nueva_linea_a)
                    lineas_b.remove(linea_b)
                    break
            else:
                coincidencias_b.append(linea_a)

        s1.writelines(coincidencias_a)
        s2.writelines(coincidencias_b + lineas_b)

if __name__ == '__main__':
    archivo_a = 'list1.txt'  # Reemplaza con el nombre de tu primer archivo
    archivo_b = 'list2.txt'  # Reemplaza con el nombre de tu segundo archivo
    salida_a = 'salida_a.txt'    # Nombre del primer archivo de salida
    salida_b = 'salida_b.txt'    # Nombre del segundo archivo de salida

    procesar_archivos(archivo_a, archivo_b, salida_a, salida_b)
