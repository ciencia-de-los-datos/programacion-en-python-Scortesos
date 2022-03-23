"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

file = open('data.csv', 'r').readlines()
file = [e.replace('\n', '') for e in file]
file = [e.split('\t') for e in file]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum([int(row[1]) for row in file])


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    d = {}
    for letter in sorted([row[0] for row in file]):
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1
    
    return list(d.items())


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    d = {}
    for row in file:
        if row[0] in d.keys():
            d[row[0]] += int(row[1])
        else:
            d[row[0]] = int(row[1])

    result = list(d.items())

    return sorted(result, key=lambda tup: tup[0])


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    d = {}
    for month in sorted([row[2].split('-')[1] for row in file]):
        if month in d.keys():
            d[month] += 1
        else:
            d[month] = 1
    
    return list(d.items())


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    d = {}
    for row in file:
        if row[0] in d.keys():
            d[row[0]].append(int(row[1]))
        else:
            d[row[0]] = [int(row[1])]
    result = [(key, max(d[key]), min(d[key])) for key in d.keys()]
    
    return sorted(result, key=lambda tup: tup[0])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    lst = []
    for e in [row[4].split(',') for row in file]:
        lst.extend(e)
    d = {}
    for e in lst:
        if e.split(':')[0] in d.keys():
            d[e.split(':')[0]].append(int(e.split(':')[1]))
        else: 
            d[e.split(':')[0]] = [int(e.split(':')[1])]
    result = [(key, min(d[key]), max(d[key])) for key in d.keys()]
    
    return sorted(result, key=lambda tup: tup[0])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    d = {}
    for row in file:
        if int(row[1]) in d.keys():
            d[int(row[1])].append(row[0])
        else: 
            d[int(row[1])] = [row[0]]
    result = list(d.items())

    return sorted(result, key=lambda tup: tup[0])


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    d = {}
    for row in file:
        if int(row[1]) in d.keys():
            d[int(row[1])].append(row[0])
        else: 
            d[int(row[1])] = [row[0]]
    result = list(d.items())
    result = sorted(result, key=lambda tup: tup[0])
    result = [(e[0], sorted(list(set(e[1])))) for e in result]

    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    lst = []
    for e in [row[4].split(',') for row in file]:
        lst.extend(e)

    lst = [e.split(':')[0] for e in lst]

    d = {}
    for key in sorted(lst):
        if key in d.keys():
            d[key] += 1
        else:
            d[key] = 1

    return dict(list(d.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lst = []
    for row in file:
        lst.append((row[0], len(row[3].split(',')), len(row[4].split(',')))) 
    
    return lst


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    d = {}
    for row in file:
        for letter in row[3].split(','):
            if letter in d.keys():
                d[letter] += int(row[1])
            else:
                d[letter] = int(row[1])

    result = list(d.items())
    
    return dict(sorted(result, key=lambda tup: tup[0]))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
