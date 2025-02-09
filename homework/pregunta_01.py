"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt") as archivo:
      lines = archivo.readlines()
      new_lines = [line.strip() for line in lines if "---" not in line]
  
    header = re.split(r"\s{2,}",new_lines[0])
    header[1] += " palabras clave"
    header[2] += " palabras clave"
    data = []
    temporal = header
    for line in new_lines[2:]:
        new_line = re.split(r"\s{2,}",line)
        print(line)
        print(len(line))
        if len(line)==0:
            continue
        if new_line[0].isdigit():
            data.append(temporal)
            temporal = []
            temporal.append(int(new_line[0]))
            temporal.append(int(new_line[1]))
            temporal.append(float(new_line[2].split()[0].replace(',','.')))
            cadena = line.find("%")
            normalizar = re.sub(r'\s+',' ',line[cadena+1:].strip())
            temporal.append(normalizar)
        else:
            clean = re.sub(r'\s+',' ',line.strip())
            clean = clean.replace(".","")
            temporal[-1]+=" "+clean.strip()
    data.append(temporal)
    data[0]=[nombre.lower().replace(" ","_") for nombre in data[0]]
    df = pd.DataFrame(data=data[1:],columns=data[0])

    return df
  
"""
Construya y retorne un dataframe de Pandas a partir del archivo
'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

- El dataframe tiene la misma estructura que el archivo original.
- Los nombres de las columnas deben ser en minusculas, reemplazando los
  espacios por guiones bajos.
- Las palabras clave deben estar separadas por coma y con un solo
  espacio entre palabra y palabra.
"""
