# 🚀 Passo a passo – Criação do projecto FastAPI com Poetry

## 1️⃣ Atualização do sistema e verificação do Python

```bash
sudo apt update && sudo apt upgrade
python3 --version
```

> Objetivo: garantir sistema atualizado e confirmar versão do Python instalada.

---

## 2️⃣ Instalação do `pipx` e `poetry`

```bash
sudo apt install pipx
pipx ensurepath
pipx install poetry
poetry --version
```

📌 **Porquê pipx?**
Isola ferramentas globais (como Poetry) sem poluir o sistema.

---

## 3️⃣ Criação do projecto com Poetry

### Criar diretório de trabalho

```bash
cd ~/projectos
```

### Criar projecto base

```bash
poetry new fastz-api
cd fastz-api
```

### Criar estrutura flat para o pacote principal

```bash
poetry new --flat fastz_api
```

📂 Estrutura resultante:

```
fastz-api/
├── fastz_api/
│   ├── __init__.py
│   └── app.py
├── tests/
├── pyproject.toml
└── README.md
```

---

## 4️⃣ Configuração da versão do Python no Poetry

Listar versões disponíveis:

```bash
poetry python list
```

Definir Python 3.13:

```bash
poetry env use 3.13
```

Instalar dependências do projecto:

```bash
poetry install
```

Ativar ambiente virtual:

```bash
poetry shell
```

---

## 5️⃣ Instalação do FastAPI

```bash
poetry add fastapi[standard]
```

📦 Isso instala:

* FastAPI
* Uvicorn
* Pydantic
* Starlette
* Dependências recomendadas

---

## 6️⃣ Criação da aplicação FastAPI

📄 `fastz_api/app.py`

```python
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_zero():
    return {'message': 'Olá mundo antes de vc!'}
```

---

## 7️⃣ Executar a aplicação (modo desenvolvimento)

```bash
fastapi dev fastz_api/app.py
```

Ou via task:

```bash
task run
```

🌐 Acesso:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 8️⃣ Instalação das dependências de desenvolvimento

```bash
poetry add --group dev ruff pytest pytest-cov taskipy
```

📦 Função de cada uma:

* **ruff** → lint + format
* **pytest** → testes
* **pytest-cov** → cobertura
* **taskipy** → automação de tarefas

---

## 9️⃣ Configuração do Ruff (Lint & Format)

No `pyproject.toml`:

```toml
[tool.ruff]
line-length = 79
extend-exclude = ["migrations"]

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

[tool.ruff.format]
preview = true
quote-style = "single"
```

### Comandos

```bash
ruff check .
ruff format .
```

---

## 🔟 Configuração do Pytest

```toml
[tool.pytest.ini_options]
pythonpath = "."
addopts = "-p no:warnings"
```

Executar testes:

```bash
pytest -vv
```

Com cobertura:

```bash
pytest --cov=fastz_api -vv
coverage html
```

📂 Resultado:

```
htmlcov/index.html
```

---

## 1️⃣1️⃣ Configuração do Taskipy (automação)

```toml
[tool.taskipy.tasks]
lint = "ruff check ."
format = "ruff format ."
pre_format = "ruff check --fix"
test = "pytest -s -x --cov=fastz_api -vv"
pre_test = "task lint"
post_test = "coverage html"
run = "fastapi dev fastz_api/app.py"
```

### Usar tarefas

```bash
task lint
task format
task test
task run
```

---

## 1️⃣2️⃣ Configuração do Git

```bash
git config --global user.name "Jose de Almeida"
git config --global user.email "josedealmeida@gmail.com"
```

Gerar `.gitignore`:

```bash
pipx run ignr -p python > .gitignore
```

---

## 1️⃣3️⃣ Estrutura final do projecto

```
fastz-api/
├── fastz_api/
│   ├── __init__.py
│   └── app.py
├── tests/
│   └── test_app.py
├── htmlcov/
├── pyproject.toml
├── README.md
└── .gitignore
```
