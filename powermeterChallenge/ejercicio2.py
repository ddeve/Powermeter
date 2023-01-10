import json

repetidos = [1, 2, 3, "1", "2", "3", 3, 4, 5]
r = [1, "5", 2, "3"]
d_str = '{"valor":125.3,"codigo":123}'

# 1. Genere una lista con los valores no repetidos de la lista ‘repetidos’.
no_repetidos = [valor for valor in repetidos if repetidos.count(valor) == 1]

# 2. Genere una lista con los valores en común entre la lista ‘r’ y ‘repetidos’
valores_comunes = [valor for valor in repetidos if valor in r]

# 3. Transforme ‘d_str’ en un diccionario.
dict_d_str = json.loads(d_str)
