def desafio1():
    file = open("./usuarios.txt", 'r')

    list_usuarios, list_espacos = zip(*[linha.split() for linha in file])

    list_espacos = [ bytes_para_megas(int(x)) for x in list_espacos ]

    total_espaco_ocupado = float(sum(list_espacos))

    media_espaco_ocupado = float("{:.2f}".format(total_espaco_ocupado/len(list_espacos)))

    list_porcentagem = porcentagem(list_espacos, total_espaco_ocupado)

    f = open('./relatório.txt','w')
    f.write('ACME Inc.           Uso do espaco em disco pelos usuarios\n')
    f.write('------------------------------------------------------------------------\n')
    f.write('Nr.  Usuario        Espaco utilizado     % do uso\n\n')

    for x in range(len(list_usuarios)):
            f.write('{:<4} {:<10} {:>14.2f} MB {:>14.2f}%\n'.format(x+1, list_usuarios[x], list_espacos[x], list_porcentagem[x]))
    f.write('\nEspaco total ocupado: {:.2f} MB'.format(total_espaco_ocupado))
    f.write('\nEspaco medio ocupado: {:.2f} MB'.format(media_espaco_ocupado))

def bytes_para_megas(bytes):
    return float("{:.2f}".format((bytes / 1024) / 1024))

def porcentagem(list_espacos, total_espaco_ocupado):
    return [float("{:.2f}".format((percent/total_espaco_ocupado)*100)) for percent in list_espacos]

if(__name__ == "__main__"):
    desafio1()