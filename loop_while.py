"""""
Loop While
Forma geral:
while expressão_booleana:
        execução do looping

o bloco do while será repetido enquanto a expressão booleana for verdadeira
Ex: 
numero = 5
while numero <=10:
    print(numero)
    numero = numero + 1

OBS: é importante no loop while que cuidemos do critério de parada para nao causar um loop infinito


#Ex4
resposta = 'N'
while resposta != 'sim':
    resposta = input("Acabou?: ")
print('ok')
"""""

resposta = 'N'
while resposta != 'sim':
    resposta = input("Acabou?: ")
print('ok')