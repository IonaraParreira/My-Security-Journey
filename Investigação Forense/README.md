<h1>Capturar Dados antes que o computador seja desligado.</h1>(o 🖥️ é a sua testemunha mais importante.)

<br>Seus olhos não focam no corpo, 
nem nas marcas de sangue na parede, mas sim no brilho da tela de um desktop no canto da sala.

Pegando as luvas para manter a máxima  integridade da cena e evidências.

Mas antes de se aproximar do computador,antes de tocar no teclado ou no mouse imediatamente. 
<h2>O que olhar?? Tudo o que importa😅</h2>
<br>

1)Verificação de Energia: Observa se a torre está ligada, se o cooler está girando ou se há luzes de LED acesas, indicando que o sistema está operando.<br>

2)A "Captura Viva": Se o monitor estiver com a imagem ativa, ele fotografa a tela rapidamente, ciente de que qualquer ação pode alterar evidências voláteis na memória RAM.<br>

3)Inspeção Física: Olha por trás da máquina para verificar conexões de rede, pen drives ou dispositivos de armazenamento externo.Com o auxílio de um bloqueador de escrita portátil, e se prepara para isolar o dispositivo da rede e garantir que nenhum dado seja alterado.<br>

4)Anota mentalmente a necessidade de extrair imagens apagadas e logs de internet que podem ter sido gerados naquele exato momento.

A regra é: colete primeiro o que desaparece mais rápido. A RAM é o topo da lista. Se você desliga o servidor, as evidências de um ataque em tempo real (como um malware rodando apenas em memória) somem para sempre.

<h3>Você sabia? Na RAM enquanto seu código roda,armazena</h3>
Credenciais em texto claro: Senhas ou tokens de API que foram descriptografados para uso imediato.
<br>
Conexões de Rede: Endereços IP de onde os usuários estão vindo (mesmo que eles tentem apagar os logs depois).

Processos Ocultos: Scripts maliciosos que não foram salvos no disco para evitar detecção por antivírus comuns.

<h1>Ferramentas de Investigação</h1>

DumpIt ou FTK Imager: Usados para tirar uma "foto" (dump) de tudo o que está na RAM naquele instante.<br>
<br>
Volatility Framework: É o padrão ouro. Ele permite que você pegue esse arquivo de "dump" e pergunte: "Quais processos estavam rodando?" ou "Me mostre o histórico do terminal que o usuário usou".<br>


1. O Primeiro Passo: Captura com o DumpIt
O DumpIt é uma ferramenta de "um clique". Ele é essencial porque, na forense, quanto menos você mexe no sistema alvo, melhor (para não sobrescrever dados na RAM).

Como usar: Você executa o .exe como administrador diretamente de um pendrive (para não instalar nada no HD da vítima).

O que ele faz: Ele lê toda a memória RAM física e gera um arquivo bruto, geralmente com a extensão .raw ou .dmp (ex: MEMORIA.raw).

O resultado: Se o computador tem 16GB de RAM, o arquivo terá exatamente 16GB. É um "espelho" bit a bit de tudo o que estava acontecendo.

2. O Segundo Passo: Análise com o Volatility
Agora que você tem o arquivo .raw no seu computador de trabalho, você usa o Volatility para "interrogar" esse arquivo.

Comandos Essenciais (Volatility 3):
A. Identificar as informações do sistema:
Antes de tudo, você precisa saber qual era o SO para o Volatility entender como a memória estava organizada.

Bash
python3 vol.py -f MEMORIA.raw windows.info
B. Listar Processos (O "Task Manager" do passado):
Isso mostra todos os processos que estavam rodando no momento do dump. É aqui que você procura por nomes estranhos ou processos sem pai.

Bash
python3 vol.py -f MEMORIA.raw windows.pslist
C. Ver Conexões de Rede:
Como programadora backend, isso vai te brilhar os olhos. Você consegue ver sockets abertos, IPs remotos e portas, mesmo que a conexão já tenha sido fechada!

Bash
python3 vol.py -f MEMORIA.raw windows.netscan
D. Extrair Senhas e Hashes:
O comando hashdump tenta extrair os hashes das senhas dos usuários que estavam carregados na memória.

Bash
python3 vol.py -f MEMORIA.raw windows.hashdump
Por que isso é importante para o seu backend?
Imagine que seu servidor sofreu um ataque de Fileless Malware (malware que não salva arquivos no disco, só roda na RAM). Se você apenas reiniciar o servidor, você apaga a única prova do crime. Usar o DumpIt garante que você tenha a "cena do crime" congelada para estudar depois com o Volatility.

Elas são de graça?
Sim! Ambas são ferramentas de código aberto (Open Source) e gratuitas, amplamente utilizadas por profissionais de segurança e perícia digital no mundo todo.

Como "instalar"?
DumpIt (Windows)
Ele não precisa de instalação (é o que chamamos de portable).

Você baixa o executável.

Clica com o botão direito e seleciona "Executar como Administrador".

Ele vai perguntar se você quer confirmar a captura. Digite y (yes).

Ele salva o arquivo na mesma pasta onde o executável está.

Volatility 3 (Multiplataforma)
Como você é dev, vai tirar de letra. Ele é um projeto em Python.

Você faz um git clone do repositório oficial no GitHub.

Instala as dependências (geralmente via pip install -r requirements.txt).

Roda ele direto pelo terminal usando o comando python vol.py.

1. Na Máquina da Vítima (Coleta)
Você não usa o Volatility lá. Você usa apenas a ferramenta de coleta (o DumpIt), que é "standalone" (não precisa de instalação).

Você chega com um Pendrive Pericial (com trava de escrita, se possível).

Roda o DumpIt.exe direto do pendrive.

Salva o arquivo .raw de volta no seu pendrive ou em um HD externo.

Pronto. Você retira o pendrive e deixa o computador da vítima exatamente como estava (ou o desliga, dependendo do protocolo).

2. Na SUA Máquina (Análise)
A análise nunca é feita no computador invadido. Você leva o arquivo .raw para o seu computador de trabalho (o seu laboratório).

É no seu computador que o Python e o Volatility estarão instalados.

Lá, você processa o arquivo com calma, sem pressa e sem medo de alterar a cena do crime original.


<h1>Para não alterar nenhum dado😌☝🏻</h1><br>

>É importante usar os bloqueadore físicos ou montagem via software.<br>

Abaixo estão as práticas essenciais para preparar e conduzir o processo de forma segura😉:
1. Bloqueador de Escrita (Write Blocker)
A forma mais segura e recomendada é o bloqueador de escrita por hardware.
O que faz: Intercepta os comandos do computador, permitindo que você leia o disco de destino sem a possibilidade de enviar dados ou alterar o sistema de arquivos.
Como usar: Conecte o disco suspeito a um Write Blocker (dispositivo de hardware) e conecte-o à sua estação forense via USB/SATA. 

2. Bloqueio por Software (Caso não use hardware)
Se não possuir o bloqueador físico, você deve bloquear a escrita via sistema operacional. 

No Linux:
Identifique o disco (ex: /dev/sdb) e force o modo leitura:
sudo hdparm -r1 /dev/sdb 

No Windows:
Abra o prompt de comando (CMD) como Administrador e digite diskpart: 

Digite list disk e identifique o número do disco alvo.
Selecione o disco: select disk X (substitua pelo número correto).
Ative o atributo de leitura: attributes disk set readonly.<br>

3. Utilização de Sistemas Operacionais Forenses
A melhor prática consiste em iniciar o computador de análise com uma distribuição Linux focada em forense.
O CAINE ou o DEFT são sistemas operacionais inicializáveis (Live USB) que possuem bloqueio automático de escrita nativo em todas as mídias conectadas.
Eles garantem que o sistema operacional de análise não toque ou modifique o disco alvo durante o processo. 
<br>

4. Criação da Imagem Forense
Após montar o disco em modo leitura, nunca analise o disco original diretamente. Você deve criar uma imagem (cópia bit-a-bit). 
Utilize ferramentas de duplicação forense para criar um arquivo de imagem (como .E01 ou .raw).
O FTK Imager (Windows) ou ferramentas de linha de comando como dc3dd são referências no mercado.
<br>

5. Cálculo e Verificação de Hash
Para garantir que a cópia é idêntica ao original:
Calcule o valor de hash (como MD5 ou SHA-256) do disco original antes da cópia e do arquivo de imagem gerado ao final.
Os valores de hash devem ser exatamente iguais, o que prova a integridade da evidência para fins legais. 
A partir desse ponto, você realiza a análise forense utilizando a cópia exata do disco, preservando a mídia original intacta. 

<h1>Logs:Melhores práticas - armazenamento,retenção e exclusão </h1>
*Defina a política de armazenamento,retenção e exclusão com base nas necessidades da empresa e nos requisitos legais.
*Revisar e atualizar regularmente as diretrizes de acordo com as mudanças nas condições e regulamentações.
*Automatize os processos de armazenamento,retenção e exclusão para garantir consistência e evitar erros humanos.
