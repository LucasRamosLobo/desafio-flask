# Gerenciamento de Tarefas - API Flask

## Descrição

Esta é uma API simples de gerenciamento de tarefas desenvolvida com Flask.

## Instalação

1. Clone o repositório:
    ```bash
   https://github.com/LucasRamosLobo/desafio-flask.git
    cd desafio-flask
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o servidor Flask:
    ```bash
    python app.py
    ```
5. teste o endpoint /tasks:
    ```bash
    POST http://localhost:5000/tasks
    GET http://localhost:5000/tasks
    DELETE POST http://localhost:5000/tasks/{id}
    PUT http://localhost:5000/tasks/{id}
    ```
6. Exemplo corpo da requisição para POST/PUT/PATCH:
    ```json
    {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa."
    }
    ```

## Testes

Para rodar os testes automatizados, execute o comando:
```bash
python tests.py

