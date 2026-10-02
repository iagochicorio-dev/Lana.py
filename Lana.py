import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

openai = OpenAI(api_key=OPENAI_API_KEY)
claude = Anthropic(api_key=ANTHROPIC_API_KEY)

NOME = "Lana"

def falar_com_gpt(mensagem):
    resposta = openai.responses.create(
        model="gpt-5-mini",
        input=f"""
Você é Lana, uma assistente pessoal de IA.
Responda de forma natural, objetiva e útil.

Usuário:
{mensagem}
"""
    )
    return resposta.output_text


def falar_com_claude(mensagem):
    resposta = claude.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""
Você é Lana, uma assistente pessoal de IA.
Responda de forma natural, objetiva e útil.

Usuário:
{mensagem}
"""
            }
        ]
    )

    return resposta.content[0].text


def lana(mensagem, modelo="gpt"):
    if modelo == "claude":
        return falar_com_claude(mensagem)

    return falar_com_gpt(mensagem)


if __name__ == "__main__":
    print(f"{NOME} está online.")
    print("Digite 'sair' para encerrar.")

    while True:
        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            print("Lana: Até mais.")
            break

        try:
            resposta = lana(mensagem)
            print(f"Lana: {resposta}")
        except Exception as erro:
            print(f"Erro: {erro}")
