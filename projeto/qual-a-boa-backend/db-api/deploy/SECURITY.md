# Qual a Boa - Segurança em Produção

Este documento descreve as melhores práticas de segurança implementadas neste projeto e as configurações necessárias para um ambiente de produção seguro.

## Configurações Essenciais de Segurança

### 1. Variáveis de Ambiente

Todas as chaves secretas e configurações sensíveis devem ser armazenadas em variáveis de ambiente. **Nunca** cometa o arquivo `.env` para o repositório.

Requisitos mínimos para o arquivo `.env` em produção:
- Chaves secretas fortes para `SECRET_KEY` e `JWT_SECRET_KEY`
- Configuração de banco de dados segura
- API_KEY exclusiva para produção
- CORS_ORIGINS limitado apenas aos domínios de frontend necessários

### 2. HTTPS

A aplicação **deve** ser executada sobre HTTPS em produção. Configuramos o Nginx para:
- Redirecionar tráfego HTTP para HTTPS
- Usar apenas TLS 1.2 e 1.3
- Configurar cabeçalhos de segurança adequados

### 3. Proteção CSRF

A proteção CSRF está configurada nos endpoints de formulário. Os endpoints da API autenticados por JWT são isentos da proteção CSRF.

### 4. Cabeçalhos de Segurança

Os seguintes cabeçalhos de segurança são implementados:
- X-Content-Type-Options: nosniff
- X-Frame-Options: DENY
- X-XSS-Protection: 1; mode=block
- Strict-Transport-Security: max-age=31536000; includeSubDomains
- Content-Security-Policy: default-src 'self'

### 5. Rate Limiting

Rate limiting está configurado para prevenir abusos:
- 100 requisições por minuto por IP por padrão
- Configurável através de `RATELIMIT_DEFAULT` e `RATELIMIT_STORAGE_URL`

## Implementando em Produção

1. Gere novas chaves secretas para todas as variáveis de ambiente
2. Configure um domínio com SSL (use Let's Encrypt)
3. Configure o Nginx como proxy reverso
4. Use o systemd para gerenciar o serviço
5. Implemente monitoramento e alertas

## Backup e Recuperação

1. Configure backups diários do banco de dados
2. Teste regularmente a restauração dos backups
3. Mantenha backups em locais fisicamente separados

## Compliance e Auditorias

Recomendamos realizar auditorias de segurança regulares e escanear vulnerabilidades utilizando ferramentas como:
- OWASP ZAP
- SQLMap
- Bandit (para código Python)

## Atualizações e Manutenção

1. Mantenha todas as dependências atualizadas
2. Revise regularmente o código para vulnerabilidades
3. Implemente um processo para atualização emergencial em caso de vulnerabilidades críticas 