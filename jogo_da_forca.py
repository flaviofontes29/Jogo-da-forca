import random
from lista_times import lista_palavras
from ascii import logo, estagio

print(logo)
print("")
print("")

regra = """
 O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui.
 A cada rodada, os jogadores irão simultaneamente escolher uma letra que suspeitem fazer parte
 da palavra. Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. 
 Entretanto, caso esta letra não exista na palavra, será desenhada uma parte do corpo do boneco
 do jogador. Se todas as 6 partes do corpo do boneco estiverem desenhadas, o jogador estará fora
 da partida.
"""
print(regra)

print("Dica: São uns dos times da série A e B")
print("Se a palavra for composta ex: Sao Paulo o espaço também é contado.")

palavra = random.choice(lista_palavras).lower()
vidas = 6
coracao = "\u2764\uFE0F" * 6
tela = []
tam_palavra = len(palavra)

for _ in range(tam_palavra):
    tela += "_"

print("")
print(coracao)
fim_do_jogo = False
while not fim_do_jogo:
    adivinha = input("Adivinhe uma letra: ").lower()
    print("")

    for posicao in range(tam_palavra):
        letra = palavra[posicao]
        if letra == adivinha:
            tela[posicao] = letra

    if adivinha not in palavra:
        print(
            f"Você digitou '{adivinha}' essa letra não esta na palavra, Você perdeu 1 vida :( "
            + coracao
        )
        vidas -= 1
        coracao = "\u2764\uFE0F" * vidas
        if vidas == 0:
            fim_do_jogo = True
            print("Você perdeu")
            print(f"A palavra era {palavra}")

    print(f"{' '.join(tela)}")

    if "_" not in tela:
        fim_do_jogo = True
        print("Você venceu!")
    print(estagio[vidas])
