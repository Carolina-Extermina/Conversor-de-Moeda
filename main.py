import requests

def converter(valor_brl, moeda_destino):
    url = f"https://api.exchangerate.host/latest?base=BRL&symbols={moeda_destino.upper()}"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if moeda_destino.upper() in dados['rates']:
            taxa = dados['rates'][moeda_destino.upper()]
            convertido = valor_brl * taxa
            return f"💰 {valor_brl:.2f} BRL = {convertido:.2f} {moeda_destino.upper()}"
        else:
            return "❌ Moeda não encontrada."

    except Exception as e:
        return f"Erro na requisição: {e}"

# --- Execução simples no terminal ---
if __name__ == "__main__":
    print("=== Conversor de Moedas ===")
    valor = float(input("Digite o valor em BRL: "))
    moeda = input("Para qual moeda deseja converter (ex: USD, EUR)? ")
    resultado = converter(valor, moeda)
    print(resultado)
