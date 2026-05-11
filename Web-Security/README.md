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
