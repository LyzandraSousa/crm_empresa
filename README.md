Este é um projeto de CRM (Customer Relationship Management) construído como uma aplicação web full-stack em Python, HTML, CSS e JavaScript.

Ele foi pensado para:

✔️ Cadastrar e gerenciar dados de clientes
✔ Organizar interações comerciais
✔ Registrar informações importantes para vendas e relatórios
✔ Oferecer uma interface simples para uso pelos times da empresa

O projeto é ideal para quem quer um CRM funcional, customizável ou como base para evoluir com mais funcionalidades.
Estrutura do Repositório:
app.py              → Ponto de entrada ou configuração geral do app
main.py             → Controla fluxo principal da aplicação
cadastro.py         → Funções para cadastro de clientes/dados
database.py         → Conexão e manipulação de banco de dados
interface.py        → Lógicas da interface e templates
models.py           → Modelos de dados (classes/entidades)
relatorio.py        → Geração de relatórios e visualizações
static/             → Arquivos estáticos (CSS, JS, imagens)
templates/          → Templates de páginas HTML
requirements.txt    → Dependências do projeto

Tecnologias Usadas:
O sistema é construído com as seguintes tecnologias:

Área	Tecnologia
Linguagem	Python
Backend	(possivelmente Flask ou outro micro-framework — ajuste conforme seu código)
Frontend	HTML, CSS, JavaScript
Templates	Jinja2 ou similares
Banco de dados	Local / SQLite ou outro conforme configuração
Controle de versão	Git & GitHub

🧩 Funcionalidades (Planejadas / Existentes)

✅ Cadastro e gerenciamento de clientes
✅ Salvamento e leitura de informações do banco
✅ Visualização através de templates HTML
✅ Relatórios exportáveis ou visualizáveis
📌 (Você pode adicionar mais conforme implementa novas features)

📥 Pré-requisitos

Antes de rodar o projeto, você precisará:

✔ Python 3.x
✔ (Opcional) ambiente virtual
✔ Dependências definidas em requirements.txt

💻 Instalação & Configuração

1. Clone o repositório

git clone https://github.com/LyzandraSousa/crm_empresa.git


2. Entre na pasta

cd crm_empresa


3. Crie um virtualenv (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows


4. Instale as dependências

pip install -r requirements.txt

▶️ Iniciando o Projeto

Rode o servidor (ajuste se necessário):

python main.py


ou

python app.py


Abra no navegador:

http://localhost:5000


(A porta pode variar conforme a configuração que você definir.)

📌 Como Usar

Uma vez iniciado:

✔ Acesse as páginas para cadastrar clientes
✔ Visualize relatórios e dados salvos
✔ Navegue entre seções através da interface

🛠️ Próximas Melhorias Sugeridas

✨ Autenticação de usuários
✨ Dashboard com métricas de vendas
✨ Importação/Exportação de CSV
✨ Filtros avançados de pesquisa
✨ Integração com APIs externas

🤝 Contribuições

Contribuições são muito bem-vindas! 💛
Você pode:

🟢 Abrir Issues para bugs ou ideias
🟢 Enviar Pull Requests com melhorias
🟢 Sugerir novas funcionalidades
