def mochila(pesoMax, enfeites):
    resposta = 0
    m = [-1 for _ in range(pesoMax + 1)]
    m[0] = 0

    for enfeite in enfeites:
        valor = enfeite[0]
        peso = enfeite[1]
        for i in range(pesoMax, peso - 1, -1):
            if(m[i - peso] != -1):
                m[i] = max(m[i], m[i - peso] + valor)
                resposta = max(resposta, m[i])

    return resposta


g = int(input())

for k in range(g):
    p = int(input())
    w = int(input())

    enfeites = []
    for _ in range(p):
        E, PC = [int(x) for x in input().split()]
        enfeites.append([E, PC])

    resposta = mochila(w, enfeites)

    print('Galho {}:'.format(k+1))
    print('Numero total de enfeites: {}'.format(resposta), end='\n\n')
