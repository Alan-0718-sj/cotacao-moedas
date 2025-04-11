import requests
import os

real = "R$"

def clear():
    """Limpa a tela do terminal.
    Verifica o sistema operacional e usa o comando apropriado ('cls' para Windows, 'clear' para outros).
    """
    os.system("cls" if os.name == "nt" else "clear")

def title():
    """Exibe o título do programa centralizado e decorado no terminal."""
    print(" >>>>>Cotação de Moedas<<<<<".upper().center(70, "🪙"))
    print()

def pegar_cotacao(moeda_origem, moeda_destino):
    """Obtém a cotação de uma moeda de origem em relação a uma moeda de destino."""
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    requisicao = requests.get(link)
    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao

def main():
    """Função principal que exibe a cotação de algumas moedas em relação ao Real (BRL)."""
    clear()
    title()
    moedas = ["USD", "EUR", "BTC", "LTC"]
    for moeda in moedas:
        cotacao = pegar_cotacao(moeda, "BRL")
        print(f" 1 {moeda} = {real} {cotacao}")
        print("####################################")
        print()

if __name__ == "__main__":
    main()
