# Trabalho-Pr-tico-Desenvolvimento-de-uma-Landing-Page-com-FastAPI

---

# Loja de Roupas - Landing Page

Este projeto tem como objetivo desenvolver uma landing page funcional para uma loja de roupas local, utilizando o framework **FastAPI**. A página foi projetada para ser atrativa e responsiva, com foco na apresentação da loja e seus produtos. O design foi inspirado em referências visuais do Pinterest e utiliza o **Bootstrap** como base para garantir uma experiência agradável em diferentes dispositivos.

## 📜 Objetivo

O objetivo é apresentar informações sobre a loja de roupas, com quatro áreas principais:

- **Home**: Página inicial com uma breve apresentação da loja e um banner atrativo.
- **Sobre**: Informações sobre a história, missão, visão e valores da loja.
- **Produtos**: Detalhes dos produtos oferecidos pela loja, com imagens e descrições.
- **Contato**: Formulário funcional para envio de mensagens, com informações de contato.

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Backend**: FastAPI (para servir as páginas HTML e processar o envio de dados do formulário)
- **Frontend**: HTML, CSS (com Bootstrap), JavaScript (se necessário)
- **Design**: Utilizamos o Pinterest como referência para o design da landing page, buscando inspiração para garantir uma interface bonita e funcional.
- **Servidor Local**: FastAPI para hospedar a página localmente.

## 📂 Estrutura do Projeto

O projeto contém os seguintes arquivos e pastas:

```
/loja-roupas-landing-page/
│
├── /static/                    # Arquivos estáticos (CSS, JS, imagens)
├── /templates/                 # Arquivos HTML para as páginas
│   ├── home.html               # Página inicial
│   ├── sobre.html              # Página sobre a loja
│   ├── produtos.html           # Página de produtos
│   └── contato.html            # Página de contato
├── app.py                      # Arquivo principal do FastAPI
└── README.md                   # Arquivo de documentação do projeto
```

## 🚀 Como Rodar o Projeto Localmente

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seuusuario/loja-roupas-landing-page.git
cd loja-roupas-landing-page
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Execute o servidor FastAPI:

```bash
uvicorn app:app --reload
```

4. Acesse a landing page no seu navegador através de:

```
http://localhost:8000
```

## 🏪 Sobre a Loja

A loja escolhida para este projeto é a **"ArthurMultimarcas"**, uma boutique de roupas femininas localizada no centro da cidade. A loja oferece uma grande variedade de roupas, acessórios e calçados, com foco em tendências atuais e produtos de alta qualidade. A missão da loja é proporcionar uma experiência de compra única, com peças que fazem a cliente se sentir ainda mais bonita e confiante.

### Missão:
"Proporcionar aos nossos clientes um estilo único e exclusivo, trazendo as últimas tendências da moda com conforto e qualidade."

### Visão:
"Ser referência no mercado de moda feminina na cidade, oferecendo sempre o melhor atendimento e os produtos mais desejados."

### Valores:
- Compromisso com a qualidade.
- Respeito e empatia com o cliente.
- Valorização da diversidade no estilo pessoal.


  
## 📝 Funcionalidade do Formulário de Contato

O formulário na página de **Contato** permite que os visitantes enviem mensagens para a loja. Ao preencher o formulário e clicar em "Enviar", os dados são processados pelo FastAPI, e uma mensagem de sucesso ou erro é exibida para o usuário.

---

