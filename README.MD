# Desk Helper

O Desk Helper é um assistente de desktop que captura o conteúdo da sua tela e utiliza inteligência artificial para interpretá-lo, fornecendo uma explicação simples do que está sendo exibido.

## Funcionalidades

- **Leitura de Tela:** Captura a tela atual com um clique no botão "Ler Tela".
- **Interpretação com IA:** Analisa a imagem da tela para fornecer uma descrição em linguagem natural.
- **Interface Flutuante:** A janela do aplicativo permanece sempre visível para fácil acesso.
- **Transparência Inteligente:** A janela se torna semitransparente quando não está em foco para não atrapalhar a visão.

## Como Funciona

O projeto é dividido em duas partes principais:

1.  **Frontend (Electron):** A interface do usuário, que captura o clique no botão e envia uma requisição para o backend.
2.  **Backend (Python/Flask):** Um servidor que:
    - Tira um print da tela (`pyautogui`).
    - Extrai texto da imagem usando OCR (`pytesseract`).
    - Envia o texto para um modelo de IA local (`Ollama` com `gemma3`) para interpretação.
    - Retorna a descrição para o frontend.

## Pré-requisitos

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Ollama](https://ollama.ai/) (com o modelo `gemma3`)

## Instalação e Uso

1.  **Clone o repositório** e entre na pasta do projeto.

2.  **Instale as dependências do Frontend:**
    ```bash
    npm install
    ```

3.  **Instale as dependências do Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

4.  **Configure o Tesseract:**
    Ajuste o caminho para o executável do Tesseract no arquivo `backend/server.py` se ele não estiver no seu PATH.

5.  **Execute a Aplicação:**

    - **Inicie o servidor backend (em um terminal):**
      ```bash
      cd backend
      python server.py
      ```

    - **Inicie o frontend (em outro terminal):**
      ```bash
      npm start
      ```
