'''
[Questão criada por Willemberg Bruno (adaptada)] Faça um sistema de cadastro de entrada dos pacientes no hospital,
utilizando dicionário guarde as informações do nome, o estado do paciente é (Leve, Grave ou Critico).
Se o paciente estiver em estado leve receberá a pulseira verde, se estiver em estado grave receberá a pulseira 
amarela e em estado crítico receberá a pulseira vermelha, por fim exiba todos os pacientes cadastrados, o seu 
estado e qual pulseira ele receberá. Para seu programa use pelo menos duas funções. 
'''

upa = dict()
verde = list()
amarela = list()
vermelha = list()
ficha = []
estado =['leve', 'grave' ,'critico']
cont = 0
pulseira = []
pulseira.append(verde)
pulseira.append(amarela)
pulseira.append(vermelha) 
sair = None

def nome():
    upa ['Nome'] = input('Informe seu nome: ')
    for s in estado:
        print(s)
        
def estados():
    upa ['Estado'] = (input('Qual seu estado?'))
    ficha.append(upa.copy())
    for e in range(3):
        if upa['Estado'] == estado [e]:
            pulseira[e].append(upa.copy())        
    
    
    
def resultado():
    print('Foram cadastrados:', len(ficha), 'pacientes com os seguintes dados' )
    print("§-"*25)  
    for f in ficha:
        print(f)
    print("§-"*25) 
    print('Foram cadastrados:', len(verde), 'pacientes com a pulseira verde' )   
    for f in verde:
        print (f)
    print("§-"*25)    
    print('Foram cadastrados:', len(amarela), 'pacientes com a pulseira amarela' )   
    for f in amarela:
        print (f)  
    print("§-"*25) 
    print('Foram cadastrados:', len(vermelha), 'pacientes com a pulseira vermelha' )   
    for f in vermelha:
        print (f)  
    print("§-"*25)          

while sair!= 'n':
    '''
#Forma alternativa, basta remover o while e o sair.   
quant = int(input('Quantos pacientes irão se cadastrar?'))
    for c in range(quant):
    '''
    nome()
    estados()
    sair = input('Deseja cadastrar outro paciente? (s/n)') 
    
resultado()            

      