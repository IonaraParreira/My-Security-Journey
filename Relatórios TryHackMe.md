<h1>Estudo voltado nas atividades de laboratório do TryHackme <img src="https://github.com/user-attachments/assets/63414096-eaa7-40e7-b733-80347267a6ac" width="80" align="middle" alt="image" /></h1>

<h1>Aprendendo o porquê e não o comando📌</h1>
Percebi que, à medida que anotava a minha evolução nos laboratórios do site TryHackMe, conseguia reter melhor o aprendizado. A seguir, algumas das anotações: evidências de escolhas e...

1) Perguntas Mestres🏷️:

🔍O que esse comando faz?<br>
🔍O que as flags significam?<br>
🔍Quando eu devo usá-lo?<br>
🔍Quais alternativas eu tenho se ele falhar?<br>
🔍Como descobrir algo?<br>
🔍Como evitar de acontecer?


2) O que foi que aprendi mais, como explicar para uma empresa. gerar check-list, mini relatóruio, o que eu vi. o impacto e qual recomendação que dou.
3) É importante equilibrar o ofensivo do defensivo.

<h1>Fica a dica</h1>
<img width="1121" height="537" alt="Captura de tela 2026-06-10 180958" src="https://github.com/user-attachments/assets/11346b64-cfe4-434a-936f-42df2051557e" />

<h3>Analista de Segurança</h3>
São chamados de defensores digitais porque monitoram,investigam e respondem a ameaças,protegendo os ativos da organização.

<h1> Endereço Mac</h1>
É um número hexadecimal de doze caracteres(um sistema de numeração de base dezesseis usado em computação para representar números) dividido em dois e separado por dois pontos. Esses dois pontos são considerados separadosres. Por exemplo:Os seis primeiros caracteres representam a empresa que fabricou a interface de rede e os seis últimos são um número único.<br>
<br>
<p align="center">
<img width="521" height="291" alt="image" src="https://github.com/user-attachments/assets/a22a3100-9dd0-4909-941a-fcc6de4044f2" />
</p>

<h1> DNS</h1>

>Sistema de Nomes de Domínio

É uma maneira simples de nos comunicarmos com dispositivos na internet sem precisarmos memorizar números complexos.Em vez de memorizar 104.26.10.229, se pode memorizar tryhackme.com

<h1>Fica a dica</h1>
<img width="1276" height="800" alt="Captura de tela 2026-06-12 034552" src="https://github.com/user-attachments/assets/92498575-3c4b-49ed-bf63-af6f7245c851" />

<h1>Relembrar é Viver</h1>

```
+------------------------------------+
| APLICAÇÃO   -->   HTTP  /  FTP     |  (Seu código/APIs)
+------------------------------------+
| TRANSPORTE  -->   TCP   /  UDP     |  (Garantia ou velocidade)
+------------------------------------+
| REDE        -->       ICMP         |  (Diagnóstico/Ping)
+------------------------------------+
```
<h1>ICMP (Internet Control Message Protocol)</h1>
<h2>Camada de Rede / Internet (Infraestrutura e Rotas)</h2>

>O que faz: Envia mensagens de status, relatório de erros e diagnósticos de rede.<br>
>Na prática: É o protocolo nativo utilizado pelo comando ping para testar se um servidor está online.<br>
<br>
<h1>TCP (Transmission Control Protocol)</h1>
<h2>Camada de Transporte (Como os dados viajam)</h2>

>O que faz: Protocolo orientado à conexão. Ele garante que todos os pacotes cheguem na ordem correta e sem perdas (se um pacote falhar, ele reenvia).<br>
>Na prática: Usado onde a segurança dos dados é crucial (APIs REST, bancos de dados, carregamento de páginas web).<br>
<br>
<h1>UDP (User Datagram Protocol)</h1>

>O que faz: Protocolo não orientado à conexão. Ele apenas envia os dados o mais rápido possível, sem checar se chegaram ou se estão na ordem.<br>
>Na prática: Usado onde velocidade importa mais que perdas eventuais (Streaming de vídeo, jogos online, chamadas de voz, DNS).<br>
<br>
<h1>HTTP (Hypertext Transfer Protocol)</h1>
<h2>Camada de Aplicação (Onde o Back-end codifica)</h2>

>O que faz: Protocolo de transferência de hipertexto. Base da comunicação da Web, funciona no modelo Cliente-Servidor (Request/Response).<br>
>Na prática: É o que você usa para construir suas APIs (GET, POST, PUT, DELETE). Roda sob o protocolo TCP.<br>
<br>
<h1>FTP (File Transfer Protocol)</h1>

>O que faz: Protocolo específico para a transferência de arquivos de forma direta entre um cliente e um servidor.<br>
>Na prática: Usado para fazer upload de arquivos de configuração, imagens ou backups para um servidor. Também roda sob o TCP.<br>
<br>

<h1>Importante!</h1>
<img width="1442" height="427" alt="Captura de tela 2026-06-16 143717" src="https://github.com/user-attachments/assets/63b9954c-22e4-4005-96fe-4705bb2949ef" /><br>

<img width="1077" height="775" alt="Captura de tela 2026-07-11 084021" src="https://github.com/user-attachments/assets/b28e86ed-724e-4343-9e1b-19233ff5c770" />


<h1>Olha o oculto!</h1>

>Pasta compartilhada oculta

Para achar: Abrir o Gerenciamento do Computador> executar `mkdir` compmgmt.msc> Pastas Compartilhadas> Compartilhamentos

<h1>Resumo da Semana</h1>
<img width="1103" height="775" alt="Captura de tela 2026-07-06 094759" src="https://github.com/user-attachments/assets/dd681fcd-4471-47a9-b40d-77f0fa5f7d67" />

<img width="1227" height="762" alt="Captura de tela 2026-07-06 094825" src="https://github.com/user-attachments/assets/556d8a09-8342-4e29-9c93-0af872750322" />

<img width="1187" height="575" alt="Captura de tela 2026-07-06 095040" src="https://github.com/user-attachments/assets/2e72d912-3ced-4244-bf96-3b17008dd325" />

<h1>Equipe</h1>
<p align="center">
  <img width="1407" height="199" alt="Captura de tela 2026-07-13 111151" src="https://github.com/user-attachments/assets/a9aff94e-725c-406a-92a7-2dff17895dc7" />
<img width="967" height="83" alt="Captura de tela 2026-07-13 112303" src="https://github.com/user-attachments/assets/3b60f908-0c60-473e-a2bb-51be89161c43" />

</p>

<h1>Cenário</h1>
<p align="center">
  <img width="1045" height="661" alt="Captura de tela 2026-07-13 112743" src="https://github.com/user-attachments/assets/f1a044a5-a5d1-4005-9e79-aa277bca90cd" />
</p>

1. SIEM created an alert about FW-NY-01 firewall brute-force.Who should triage the alert?
>R: Lucas | SOC L1 Analyst

2. The HR manager Anna launched a phishing malware.Who should make a deep analysis? 
>R: Susan |SOC L2 Analyst

3. The office in France was somehow hit with ransomware.Immediate response is required!
>R: Robert |CERT Lead

4. Our servers storing the credit cards require PCI DSS audit. Who can help us here?
>R: Nick| GRC Auditor

5. Who can check the new version of tryhackme.thm for vulnerabilities?
>R:Ben | Penetration Tester

6. The SIEM is unavailable due to a storage limit.Who can investigate the issue?
>R: Eugen | SOC Engineer

7. FIN7 threat group actively targets our company.Who can analyze their tactics?
>R: Alice | Threat Researcher

<h1>Minha evolução da semana 😎</h1>
<p align="center">
<img width="391" height="192" alt="image" src="https://github.com/user-attachments/assets/8f9c7d34-1bb2-4e9a-96bd-e6ee3e568924" />
</p>
