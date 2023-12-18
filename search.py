import re

def process_files(archivo_a, archivo_b, salida_a, salida_b, inverse=False):
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
                coincidencias_a.append(linea_a)
                # if i want an inverse search use this: 
                # coincidencias_b.append(linea_a)

        s1.writelines(coincidencias_a)
        s2.writelines(coincidencias_b + lineas_b)

def get_hex_values(input_file, output_file):
    patron_hex = re.compile(r'#(?:[0-9a-fA-F]{3}){1,2}\b')
    hex_colors = set()

    with open(input_file, 'r') as f:
        contenido = f.read()
        hex_colors.update(patron_hex.findall(contenido))

    with open(output_file, 'w') as o:
        # o.writelines(color + '\n' for color in hex_colors)
        o.writelines(hex_colors)

if __name__ == '__main__':
    # file A: contains the base, file B: contains the new inputs
    file_a, file_b  = 'list1.txt','list2.txt'
    output_a, output_b = 'out1.txt', 'out2.txt'
    output_c = 'hex.txt'
    process_files(file_a, file_b, output_a, output_b)
    get_hex_values(file_b, output_c)
