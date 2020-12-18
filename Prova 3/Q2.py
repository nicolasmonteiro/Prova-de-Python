'''
[ Questão criada por Deyvid Gonçalves (adaptado)] Faça um programa que faça
 pesquisa do produto de um supermercado, preço e a quantidade em estoque. 
 Para fazer esse programa use tupla e pelo menos duas funções. Para sair do 
 programa será preciso digitar 0. A tupla deve ter no mínimo 5 produtos. 
 '''
import os
 
produtos = ('Farinha(1kg)','Flocão (1kg)','Arroz branco(1kg)','Feijão (1kg)','Café em pó (500 g)','Leite em pó (500g)')
precos = (3.59,1.50,5.00,8.50,9.00,6.99)
quantidade = (150,125,100,85,60,55)
cont = 0
esc = 1
sair = 0

def inicio():
    cont = 0
    print('Seja bem vindo ao Supermercados Medlin')
    for p in produtos:
        print(cont,'-',p)
        cont += 1
    cont = 0  

def meio():
    print('§-'*30)
    esc = int(input('Informe o produto que deseja consultar: '))
    for c in range(6):
        if esc == c:
            print('Preço: R$',precos[esc], 'Quantidade: ',quantidade[esc])
    
    
while True:
    inicio()  
    meio()
    print('§-'*30)
    sair = int(input('Se desejar sair informe 0: '))
    os.system('cls' if os.name == 'nt' else 'cls')
    if sair == 0:
        break
print('Consulta concluída, obrigado!')          
        