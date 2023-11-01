# Exercício Python 27: Crie um programa q ue leia uma frase qualquer e diga se ela é um palíndromo,

frase = str(input('Digite um nome'))
frase = frase.upper().replace(" ","") 
invertido = frase.upper() [::-1] 

invertido = invertido.replace(" ", "") #
if frase == invertido:
    print("palíndromo")
else:
    print("não é palíndromo")