import os
from generative_model import GenerativeModel
from google.genai.errors import ClientError

from dotenv import load_dotenv
from google import genai

load_dotenv()
CHAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODELO = "gemini-3.5-flash"
MODELO_ALTERNATIVO = "gemini-3.5-flashs"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")

def analisador_sentimentos(nome_produto, modelo=MODELO):
    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    prompt_usuario = carrega(f"dados/avaliacoes-{nome_produto}.txt")

    print(f"Iniciando a análise de sentimentos do produto: {nome_produto}")

    try:            
        llm = GenerativeModel(
            client=client,
            model_name = modelo,
            system_instruction=prompt_sistema
        )

        resposta = llm.generate_content(prompt_usuario)
        texto_resposta = resposta.text

        salva(f"dados/resposta-{nome_produto}", texto_resposta)
    except ClientError as e:
        if e.code != 404:
            raise

        if modelo == MODELO_ALTERNATIVO:
            print(f"Modelo inválido: {modelo}. {e}")
            return

        print(f"Modelo inválido: {modelo}. Usando {MODELO_ALTERNATIVO}.")
        analisador_sentimentos(nome_produto, MODELO_ALTERNATIVO)

def main():
    lista_de_produtos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]

    for um_produto in  lista_de_produtos:
        analisador_sentimentos(um_produto)

if __name__ == "__main__":
    main()
