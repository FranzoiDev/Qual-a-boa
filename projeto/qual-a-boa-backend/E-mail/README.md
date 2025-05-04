
# 📧 Meu Projeto Email

Projeto backend desenvolvido em **Node.js** com **NestJS**, focado no envio de emails utilizando o módulo **@nestjs-modules/mailer** e o **Nodemailer**.

## 📦 Tecnologias Utilizadas

- [NestJS](https://nestjs.com/)
- [Nodemailer](https://nodemailer.com/about/)
- [TypeScript](https://www.typescriptlang.org/)
- [Jest](https://jestjs.io/) — para testes
- [ESLint](https://eslint.org/) + [Prettier](https://prettier.io/) — para padronização de código
- [dotenv](https://github.com/motdotla/dotenv) — para variáveis de ambiente

## 📂 Estrutura de Pastas

```
E-mail/
├── dist/               # Arquivos compilados
├── node_modules/       # Dependências instaladas
├── src/                # Código-fonte principal
│   └── ...             # Seus módulos e serviços
├── test/               # Testes automatizados
├── .env                # Variáveis de ambiente
├── package.json        # Configurações de dependências e scripts
├── tsconfig.json       # Configurações do TypeScript
├── nest-cli.json       # Configuração do Nest CLI
└── README.md           # Documentação do projeto
```

## 📜 Scripts disponíveis

| Comando        | Descrição                         |
|:---------------|:----------------------------------|
| `yarn start`          | Inicia o servidor |
| `yarn start:dev`      | Inicia em modo desenvolvimento (hot-reload) |
| `yarn build`          | Compila o projeto |
| `yarn test`           | Executa os testes unitários |
| `yarn test:watch`     | Executa os testes em modo observação |
| `yarn lint`           | Faz análise estática de código com ESLint |
| `yarn format`         | Formata o código usando Prettier |

## ⚙️ Como rodar o projeto

1. **Instalar dependências:**

```bash
yarn install
```

2. **Configurar as variáveis de ambiente:**

Copie o arquivo `.env.example` (se houver) ou configure um `.env` com as credenciais necessárias para o serviço de email:

```env
EMAIL_HOST=smtp.seuprovedor.com
EMAIL_PORT=587
EMAIL_USER=seu-email@dominio.com
EMAIL_PASS=sua-senha
```

3. **Executar em modo desenvolvimento:**

```bash
yarn start:dev
```

## 🧪 Testes

Para rodar os testes automatizados:

```bash
yarn test
```

## 📄 Licença

Este projeto está sob a licença **UNLICENSED** — uso interno.

---

## ✨ Autor

Desenvolvido por [Seu Nome Aqui] 🚀
