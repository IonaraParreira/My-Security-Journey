<h1>Momento URRR</h1>
<p align="center">
  <img width="334" height="207" alt="image" src="https://github.com/user-attachments/assets/c07ccc2a-8e09-4339-a9ad-37cb6b6ee55b" />
</p>

>Toda URL é uma URI, mas nem toda URI é uma URL. E sim, ambas têm o objetivo,fazer com que sistemas e redes consigam apontar para um recurso específico.
<h1>URI</h1>

É o termo mais abrangente. Funciona como o nome de uma pessoa ou o número de um documento. Serve para identificar um recurso.
Identifica um recurso (o "que" é), enquanto a URL fornece o caminho e o protocolo para localizá-lo e acessá-lo (o "onde" está). 

<h1>URL</h1>
É uma subcategoria da URI. Funciona como o endereço completo com rua e número de uma casa. Serve para identificar e localizar exatamente onde o recurso está e como acessá-lo (por exemplo, usando protocolos como https://). 
<br>

<h1>Diferença entre URI vs URL vs URN</h1>

Para entender a diferença definitiva entre esses três conceitos, podemos olhar para a estrutura de um único endereço de API:

`https://api.meubackend.com/v1/usuarios#id-9876`

Aqui está o desmembramento

* **1. URL (Uniform Resource Locator):** `https://api.meubackend.com/v1/usuarios`
  > **O que faz:** É o localizador. Funciona como o mapa ou endereço físico. Ele define o protocolo (`https`) e o domínio/caminho do servidor onde o recurso está hospedado. Te diz *como chegar lá*.

* **2. URN (Uniform Resource Name):** `usuarios#id-9876`
  > **O que faz:** É o nome/identidade. Funciona como o "RG" ou "CPF" do recurso dentro daquele contexto. Identifica o ID específico do usuário, independentemente de onde o servidor esteja rodando.

* **3. URI (Uniform Resource Identifier):** `https://api.meubackend.com/v1/usuarios#id-9876`
  > **O que faz:** É o identificador completo. Como a URI é a categoria maior (a união de Localização + Nome), a linha inteira combinada é, por definição, a URI desse recurso.

---

📌 **Resumo de Bolso**
* **URL** = `Como eu chego lá?` (Protocolo + Domínio/Caminho)
* **URN** = `Quem ou o que está lá?` (Nome/Identificador do recurso)
* **URI** = `O endereço completo.` (A junção da URL com a URN)
