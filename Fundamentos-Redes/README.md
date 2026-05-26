<h1>Nenhuma rede é 100% segura</h1>

>foco deve ser a gestão de riscos, monitoramento contínuo, autenticação forte e conscientização de usuários.

Redes é a prática de proteger dispositivos, dados e sistemas contra acessos maliciosos, garantindo a tríade CIA: Confidencialidade, Integridade e Disponibilidade. 

Pontos Fundamentais de Redes e Cibersegurança:
Fundamentos de Redes (TCP/IP e Modelo OSI): Compreender o fluxo de dados, protocolos (como HTTP, HTTPS, DNS, IP) e como pacotes se movem é crucial para detectar anomalias.
Tríade CIA e Autenticidade:
Confidencialidade: Garantir que apenas pessoas autorizadas acessem os dados.
Integridade: Garantir que os dados não sejam alterados.
Disponibilidade: Garantir que os sistemas estejam acessíveis quando necessários.
Ameaças Comuns: Conhecer phishing, ransomware, ataques de negação de serviço (DDoS) e exploração de vulnerabilidades em softwares.
Defesa em Camadas (Segurança em Profundidade): Não confiar apenas em um firewall. Use antivírus, sistemas de detecção de intrusão (IDS), firewalls de aplicação e criptografia.
Gestão de Identidade e Acesso: Implementar autenticação multifator (MFA) e princípio do menor privilégio (usuários só acessam o necessário).
Segurança em Wi-Fi e Nuvem: Proteger redes sem fio com criptografia forte (WPA3) e configurar corretamente a segurança em ambientes de nuvem. 


>Entender o básico de sistemas operacionais, tanto Windows quanto Linux, além de virtualização, é essencial para configurar laboratórios e entender o ambiente a ser protegido.

<h3>Tipos de Redes</h3>
LAN - É focado no local

WAN - Adequado para comunicação de longa distância e cobertura global

>Protocolo mais importante para se comunicar e usar boa parte da internet é o protocolo TCP/IP

# 🌐 Guia Intuitivo de Redes e Protocolos para Back-end

Notas de estudo pessoais sobre a infraestrutura da internet, fluxos de comunicação e protocolos da camada de transporte.

---

## 📌 1. O Fluxo da Web (Cliente x Servidor)

Quando desenvolvemos localmente (`localhost`), estamos em um ambiente controlado e isolado. Ao publicar a aplicação na internet, passamos a lidar com uma infraestrutura global (roteadores, switches e cabos submarinos) e novos desafios como **latência**, **segurança** e **custo**.

A comunicação baseia-se no modelo **Cliente-Servidor**:
1. **Cliente (ex: Navegador, CURL):** Dispara uma **Requisição HTTP** utilizando as regras do protocolo para solicitar um recurso.
2. **Servidor:** Processa a requisição e devolve uma **Resposta HTTP** (HTML, CSS, JSON) que o cliente consegue interpretar.

---

## 🌍 2. Escopo Geográfico das Redes

| Tipo de Rede | Abrangência | Exemplo Prático | Características |
| :--- | :--- | :--- | :--- |
| **LAN** *(Local Area)* | Restrita (Salas, prédios) | Redes domésticas, LAN Houses | Altíssima velocidade, baixíssima latência, privada e barata. |
| **WAN** *(Wide Area)* | Países, continentes | Sistema de telefonia | Velocidade e latência variáveis, alto custo, mantida por teles. |
| **Internet** | Global | A rede mundial | Interconexão pública de várias redes do planeta. |

---

## 🥞 3. O Modelo TCP/IP na Prática

Para que máquinas diferentes conversem, utilizamos a padronização do modelo TCP/IP, organizado em camadas:

### 🚀 Camada de Aplicação (Onde o código roda)
* **HTTP / HTTPS:** Transferência de dados na web (HTTPS possui criptografia).
* **Ferramenta Útil:** `curl -v <url>` (permite inspecionar os cabeçalhos de uma requisição HTTP real).

### 🚚 Camada de Transporte (Como os dados viajam)
Responsável por pegar os dados da aplicação, dividi-los em pedaços e garantir a entrega.

* **TCP (Transmission Control Protocol):** Focado em **integridade**. Garante entrega ordenada e sem perdas (essencial para páginas web e APIs REST). Utiliza o *3-Way Handshake* para abrir conexões.
* **UDP (User Datagram Protocol):** Focado em **velocidade**. Transmissão assíncrona, não garante a ordem e nem se o dado chegou (ideal para streamings e jogos online).
* **Ferramenta Útil:** `telnet <ip> <porta>` (usado para testar conexões TCP manuais).

### 🗺️ Camada de Internet (Endereçamento)
* **IP (Internet Protocol):** O identificador único de cada dispositivo na rede, funcionando exatamente como um **CEP**.

---

## 🔍 4. Resolução de Nomes (DNS)

Como humanos não decoram números de IP, utilizamos o **DNS (Domain Name System)**, que funciona como a lista telefônica da internet, traduzindo URLs (`google.com`) nos IPs reais dos servidores.

* **Ferramenta Útil:** `ping <url>` (testa a conectividade com o servidor e verifica se o DNS está resolvendo o nome corretamente).

---

