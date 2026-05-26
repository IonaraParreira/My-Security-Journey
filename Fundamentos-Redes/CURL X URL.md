<h1>🛠️ O que é o CURL? (O Cliente)</h1
O CURL (frequentemente escrito como curl) é uma ferramenta de linha de comando (um programa que roda no seu terminal) usada para transferir dados de ou para um servidor.

Quando você digita curl https://api.github.com no seu terminal, o curl age exatamente como um navegador de internet sem interface gráfica. Ele monta uma requisição HTTP, envia para o servidor e joga a resposta na sua tela. Por isso, ele é classificado como um Cliente HTTP (assim como o Google Chrome, o Firefox ou o Postman).

Digitando curl https://api.github.com você encontrará algo do tipo:
<img width="1647" height="791" alt="Captura de tela 2026-05-26 141417" src="https://github.com/user-attachments/assets/3021a0fb-3677-440e-9799-e25e17e630a3" />

👆🏻Acima é um exemplo do contato direto com o retorno de uma API Web real.


Quando se clica no link https://api.github.com de dentro do arquivo no GitHub, o navegador abri uma nova aba e faz uma requisição HTTP do tipo GET para esse endereço.

O servidor do GitHub recebeu o pedido e respondeu com o conteúdo configurado para aquela URL. Como essa é a URL da API deles (feita para sistemas e programas conversarem entre si, e não para usuários humanos verem um site bonito), ela não devolve uma página com cores, botões ou imagens. Ela devolve dados puros ou como está vendo,esse texto esquisito

<h2>Prazer,sou o JSON</h2>
Esse formato de texto cheio de chaves { }, aspas e dois-pontos que você está vendo na imagem acima,chama-se JSON (JavaScript Object Notation).

O JSON é o padrão mais utilizado no mundo por programadores Back-end para transmitir dados entre o servidor e o cliente. Se você olhar com atenção, o GitHub está devolvendo uma "lista" de outros endereços importantes da API deles. Por exemplo:

Na linha de emojis_url, ele mostra onde o código pode buscar a lista de emojis do GitHub.

Na linha de user_url, ele mostra a estrutura para buscar informações de um usuário.

<h1>📍 O que é a URL? (O Endereço)</h1>
A URL (Uniform Resource Locator) não é um programa, ela é simplesmente o endereço de onde o recurso está na internet. É o texto que você digita.

https://www.google.com ➡️ Isso é uma URL.
<br>Visualizará <br>
<img width="837" height="1025" alt="Captura de tela 2026-05-26 142523" src="https://github.com/user-attachments/assets/cf25e8b1-6e38-4126-bc40-5e76b187c3ab" />


💡 Resumo da Ópera
Para fazer uma requisição web acontecer, o Cliente precisa de uma URL:

🗣️ "O Cliente (Chrome ou CURL) utiliza uma URL (https://...) para saber onde bater e pedir os dados."

Portanto,o navegador e CURL são exemplos de Clientes (as ferramentas que fazem o pedido), enquanto a URL é apenas o "mapa/endereço" que esses clientes usam para achar o servidor.
