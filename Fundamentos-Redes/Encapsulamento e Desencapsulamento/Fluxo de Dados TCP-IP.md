<h1> Fluxo de Dados TCP/IP</h1>

Quando enviamos uma requisição pela web, os dados passam por uma espécie de "linha de produção" onde cada camada adiciona o seu próprio cabeçalho (etiqueta) com informações de controle.

<h2>Camada de Aplicação (Ex: HTTP, HTTPS, FTP)</h2> É a camada que interage diretamente com o usuário ou software. Ela gera os dados puros (como uma mensagem ou requisição de página).<br>
<br>
<h2>Camada de Transporte (Ex: TCP, UDP)</h2> Ela pega os dados da aplicação e adiciona uma etiqueta contendo as Portas de Origem e Destino (como a porta 80 para HTTP ou 443 para HTTPS), dividindo tudo em pedaços chamados Segmentos.<br>
<br>
<h2>Camada de Rede ou Internet (Ex: IP)</h2>Pega o segmento e adiciona os Endereços IP de Origem e Destino. Aqui, o pacote de dados é chamado de Pacote. É onde ocorre o roteamento pela internet.<br>
<br>
<h2>Camada de Interface de Rede ou Link (Ex: Ethernet, Wi-Fi)</h2>Transforma o pacote em um Quadro (Frame), adicionando os endereços físicos da placa de rede, conhecidos como Endereços MAC. Por fim, esses dados são convertidos em impulsos elétricos ou ondas de rádio (bits) e transmitidos pelos cabos ou pelo ar.<br>
<br>
<h2>Quando os dados chegam ao destino, o processo inverso acontece (Desencapsulamento)</h2>o servidor lê e remove a etiqueta de cada camada até que restem apenas os dados originais da aplicação.
