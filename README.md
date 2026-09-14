# API Biblioteca — Atividade Prática Django

Projeto criado para atender à atividade prática: **3 tabelas em 3 apps separados**, models com campos variados, relacionamento `ForeignKey`, registro no Django Admin, migrações e endpoint de listagem em JSON.

## Estrutura

- `autores` → model `Autor`
- `categorias` → model `Categoria`
- `livros` → model `Livro`

O model `Livro` possui relacionamento `ForeignKey` com `Autor` e `Categoria`. A justificativa do relacionamento está comentada diretamente em `livros/models.py`.

## Como executar

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Linux/macOS

```bash
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rotas

- `http://127.0.0.1:8000/` → informações do projeto
- `http://127.0.0.1:8000/admin/` → Django Admin
- `http://127.0.0.1:8000/api/livros/` → listagem de livros em JSON

## Como testar a API

1. Execute as migrações.
2. Crie um superusuário.
3. Entre em `/admin/`.
4. Cadastre pelo menos um Autor e uma Categoria.
5. Cadastre um Livro vinculado a eles.
6. Abra `/api/livros/`.

Exemplo de retorno:

```json
[
  {
    "id": 1,
    "titulo": "Dom Casmurro",
    "isbn": "9781234567890",
    "ano_publicacao": 1899,
    "disponivel": true,
    "autor": {
      "id": 1,
      "nome": "Machado de Assis"
    },
    "categoria": {
      "id": 1,
      "nome": "Literatura Brasileira"
    }
  }
]
```

## GitHub

O `.gitignore` já está configurado para não enviar `venv`, `db.sqlite3` e `__pycache__`.

```bash
git init
git add .
git commit -m "Atividade pratica Django - API Biblioteca"
git branch -M main
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
```

> Não altere datas de arquivos ou histórico para simular entrega anterior. Envie o projeto com o histórico real do seu trabalho.
git init