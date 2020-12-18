'''
[Questão criada por Myllena Laís (adaptada)] Um aluno deseja saber suas médias antes da postagem de seu professor para planejar
com antecedência as suas férias. O aluno deseja criar um sistema que receba os nomes das disciplinas ( no mínimo 5) e as médias.
Se o aluno tiver média maior ou igual a 7 o aluno em todas as matérias cadastradas ele está de férias. Se alguma média for menor 
que 7 ele não estará de férias. Use lista e função padrão para criar seu programa. O seu programa deve mostrar a situação do aluno 
como resultando, exibindo se ele está de férias ou não.
'''

medias = []
disciplinas = []
c = 0

def analise(num = 0):
    if num >= 1:
        print('Não está de férias ainda, estude mais !')
    else:
        print('Uhul! Está de férias !')
    


quant = int(input('Informe quantas materias e notas deseja conferir: '))

for n in range(quant):
    disc = input('Informe o nome da displina: ')
    media = int(input('Informe sua media: '))
    disciplinas.append(disc)
    medias.append(media)
    
for i in range(len(medias)):
    if medias[i] < 7 :
        c += 1

    for d in range(0, len(medias)):
        if medias[d] < 7:
            for i in range(len(medias)):
                c += 1
        
analise(c)            
            
                    