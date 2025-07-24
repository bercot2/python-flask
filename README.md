# 🍲 API - Flask

Este projeto é uma API REST desenvolvida em Flask.

---

# 🐍 Versão do Python

A API foi desenvolvida utilizando **Python 3.11.5**.

---

## ✅ Passo a passo para configuração do ambiente

### 1. Criar e ativar ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```
---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Configurar variáveis de ambiente

Crie um arquivo `server_config.env` na raiz do projeto `./` com o seguinte conteúdo:

```
# Conexão Banco de Dados
DATABASE_CONNECT=...
```

---

### Banco de dados

- Banco de dados utilizado - `PostgreSql`

---

### 4. Executar as migrações

```bash
flask db upgrade
```

Isso criará todas as tabelas necessárias no banco de dados.

---

🔍 **Informações adicionais sobre a API:**

- Todas as endpoints estão preparadas para **resposta paginada**, o que garante melhor desempenho e controle em grandes volumes de dados.

---

## 🧪 Rodando Aplicação localmente

Se estiver utilizando o VS Code, basta pressionar F5 para iniciar a aplicação automaticamente.
O projeto já possui a pasta `.vscode` configurada com o arquivo `launch.json`.

---