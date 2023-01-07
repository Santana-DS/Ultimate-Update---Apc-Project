def IEC60062(resistencia):
    algarismo = {'Nenhuma': '-', 'Rosa': '-', 'Prata':'-', 'Dourada':'-', 'Preta':'0', 'Marrom':'1', 'Vermelha':'2',
                 'Laranja':'3', 'Amarela':'4', 'Verde':'5', 'Azul':'6', 'Violeta':'7', 'Cinza':'8', 'Branca':'9'}
    multiplicador = {'Nenhuma': '-', 'Rosa': '-3', 'Prata':'-2', 'Dourada':'-1', 'Preta':'0', 'Marrom':'1', 'Vermelha':'2',
                     'Laranja':'3', 'Amarela':'4', 'Verde':'5', 'Azul':'6', 'Violeta':'7', 'Cinza':'8', 'Branca':'9'}
    tolerancia = {'Nenhuma': '20', 'Rosa': '-', 'Prata':'10', 'Dourada':'5', 'Preta':'-', 'Marrom':'1', 'Vermelha':'2',
                  'Laranja':'0.05', 'Amarela':'0.02', 'Verde':'0.5', 'Azul':'0.25', 'Violeta':'0.1', 'Cinza':'0.01', 'Branca':'-'}
    FM, T = resistencia.split()
    lista_final = list()
    import re
    x = re.findall('[0-9]', FM)        # checar algarismos
    y = re.findall('[mKMG-]', FM)      # checar multiplicador
    alg = len(x)                       # checar quantos algarismos há
    for i in x[0:3]:                   # --- Primeira parte: cores pelos algarismos ---
        for k, v in algarismo.items():
            if i == v:
                lista_final.append(k)   
    a = 0
    if alg == 1:                       # checar quantidade de alg. significativos
        lista_final.append('Preta')
        a = -1
    elif alg == 2:
        if FM[1] == '.':
            a = -1
    elif alg == 3:
        if FM[1] == '.':
            a = -2
        if FM[2] == '.':
            a = -1
    elif alg > 3:
        a = alg - 3
    if y == ['m']:                     # m == 10^-3
        multi = -3 + a
    elif y == ['-']:                   # - == 1
        multi = 0 + a
    elif y == ['K']:                   # K == 10^3
        multi = 3 + a
    elif y == ['M']:                   # M == 10^6
        multi = 6 + a
    elif y == ['G']:                   # G == 10^9
        multi = 9 + a
    multi = str(multi)      
    for k, v in multiplicador.items(): # --- Segunda parte: cores pelo multiplicador ---
        if multi == v:
            lista_final.append(k)
    for k, v in tolerancia.items():    # --- Terceira parte: cores pela tolerância ---
        if T == v:
            lista_final.append(k)
            return lista_final

# TESTAR CÓGIDO:
# P/ INPUT ==
'''
print(IEC60062('1- 10'))
print(IEC60062('2.70M 0.01'))
print(IEC60062('13m 0.02'))
print(IEC60062('2.26K 0.05'))
print(IEC60062('2.7M 1'))
print(IEC60062('2.2K 2'))
print(IEC60062('2260- 1'))
'''
# OUTPUT DEVE SER:
#['Marrom', 'Preta', 'Dourada', 'Prata']
#['Vermelha', 'Violeta', 'Preta', 'Amarela', 'Cinza']
#['Marrom', 'Laranja', 'Rosa', 'Amarela']
#['Vermelha', 'Vermelha', 'Azul', 'Marrom', 'Laranja']
#['Vermelha', 'Violeta', 'Verde', 'Marrom']
#['Vermelha', 'Vermelha', 'Vermelha', 'Vermelha']
#['Vermelha', 'Vermelha', 'Azul', 'Marrom', 'Marrom']