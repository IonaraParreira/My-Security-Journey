# 🌐 CORS: Cross-Origin Resource Sharing

### 🧐 O que eu entendi:
Ele é um mecanismo de segurança que os navegadores usam para permitir (ou barrar) que um site acesse recursos de outro servidor. É o "segurança da festa" que verifica o convite (Header).

### 🛡️ Por que é importante em Cyber?
Sem o CORS, sites maliciosos poderiam fazer requisições para APIs privadas em nome do usuário. Ele previne ataques onde scripts tentam "fuxicar" dados de outros domínios sem autorização.

### 🛠️ Como aplicar no Node.js:
Quando o navegador barrar o acesso por falta de permissão, use o pacote `cors`:

```javascript
const cors = require('cors');
app.use(cors()); // Libera o acesso para as origens autorizadas
```
<br>

# 🧼 Sanitização de Dados (Input Sanitization)

**O que eu entendi:**
É o processo de "limpar" as entradas do usuário. Se alguém tentar enviar um código malicioso em um formulário (como um `<script>`), a sanitização remove ou transforma esse código em texto comum para que ele não seja executado pelo servidor ou pelo navegador.

**Por que é vital?**
Previne ataques graves como **XSS** e **SQL Injection**. É a primeira linha de defesa para garantir que o que entra no sistema é seguro.

### 🛡️ Resumo de Controles

* **CORS:** Controla **quem** pode acessar.
* **SANITIZAÇÃO:** Controla **o que** entra.

### 🔬 Laboratório Prático (Prova de Conceito)

Para consolidar esses conceitos de defesa, desenvolvi um filtro de segurança focado no tratamento de dados de entrada.

* **Projeto:** [Filtro de Segurança: Sanitizador e Validador de URL](https://github.com/IonaraParreira/Analise_de_Seguranca.git)
* **O que foi aplicado na prática:**
  * **Sanitização ativa:** Uso de métodos como `.strip()` para espaços, `.lower()` para padronização de caixa e `.rstrip('/')` para tratamento de barras residuais.
  * **Prevenção de XSS:** Implementação da biblioteca nativa `html` (`html.escape`) para neutralizar caracteres de marcação perigosos (transformando `<` e `>` em entidades seguras).
  * **Validação Estrita (Whitelisting):** Bloqueio rigoroso baseado em regras de negócio no backend para garantir conexões criptografadas (`https://`) e domínios corporativos válidos (`.com`).

> 💡 **Resultado:** O script funciona como um firewall rudimentar de aplicação (AppSec), impedindo que inputs maliciosos avancem para as camadas internas do sistema.
