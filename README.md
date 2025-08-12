# 📲 Automação de WhatsApp com Supabase + Z-API

Script Python que envia mensagens personalizadas pelo WhatsApp usando contatos cadastrados no Supabase.

<br>

## ✅ Funcionalidades
- Busca até 3 contatos no Supabase
- Envia mensagens personalizadas via Z-API
- Verifica se foi entregue
- Inclui tratamento de erros

<br>

## 📋Pré-Requisitos
- Python 3.8+
- Conta e criação do banco no [Supabase](https://supabase.com)
- Conta e criação da instancia no [Z-API](https://z-api.io)

<br>

## ⚙️ Configuração

### 1. Banco de Dados no Supabase
Crie uma tabela o nome de `contatos_zapi` no Supabase:
```sql
CREATE TABLE contatos_zapi (
  id int8 PRIMARY KEY,
  nome VARCHAR NOT NULL,
  telefone TEXT NOT NULL -- Formato: 5511999999999
);
```

### 2. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com:

```ini
SUPA_URL="sua-url.supabase.co"
SUPA_KEY="sua-chave-publica"
ZAPI_TOKEN="seu-token-zapi"
ZAPI_ID="sua-instancia-id"
```

### 3. Instalação das Dependências
```bash
pip install supabase python-dotenv requests
```

### 4. Execute o script principal
```bash
python main.py
```
<br>

## 🧩 Estrutura do Projeto

```plaintext
📂 python-zapi-supabase
├── 📄 main.py          # Lógica principal
├── 📄 .env             # Configurações (EXEMPLO ACIMA)
├── 📄 .gitignore       # Ignora .env e __pycache__
└── 📄 README.md        # Este arquivo
```


