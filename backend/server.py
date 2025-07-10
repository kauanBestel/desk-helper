from flask import Flask, jsonify
import pyautogui
import pytesseract
import requests
from PIL import Image
import os
import datetime

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

PASTA_CAPTURAS = "capturas"

os.makedirs(PASTA_CAPTURAS, exist_ok=True)

@app.route("/captura", methods=["POST"])
def captura():

    nome_arquivo = datetime.datetime.now().strftime("captura_%Y-%m-%d_%H-%M-%S.png")
    caminho_completo = os.path.join(PASTA_CAPTURAS, nome_arquivo)

    screenshot = pyautogui.screenshot()
    screenshot.save(caminho_completo)

    # OCR com Tesseract (OPTIC CHARACTER RECOGNITION)
    texto = pytesseract.image_to_string(screenshot)

    interpretacao = interpretar(texto)

    return jsonify({
        "texto_extraido": texto.strip(),
        "interpretacao": interpretacao,
        "imagem_salva": caminho_completo
    })

def interpretar(texto):
    prompt = f"Analise o texto extraído da tela e explique o que está acontecendo de forma simples, como se você fosse um ajudante que esta aqui apenas para ajudar:\n\n{texto}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()
    return data.get("response", "Não foi possível interpretar.")

if __name__ == "__main__":
    app.run(port=5000)
