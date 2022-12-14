# Desafio Softfocus - Setembro/2022

## Critérios essenciais do desafio 
1. A solução deveria ser desenvolvida em Python.
2. A interface deveria ser criada em HTML.
3. A solução deveria possibilitar o CRUD de uma comunicação de perda.
4. Os dados deveriam ser salvos em um banco de dados: Postgres, MySQL, MongoDB ou Firebase.
5. A comunicação de perda deveria possuir:
    - Nome do produtor
    - email do produtor
    - CPF do produtor
    - Localização da lavoura (latitude e longitude)
    - Tipo da lavoura
    - Data da colheita
    - Evento ocorrido
6. Quando o analista estivesse cadastrando uma nova comunicação, ele deveria ser informado caso existisse no banco de dados outra comunicação em um raio de
menos de 10km com evento divergente.
7. O projeto deveria conter validações para CPF e email feitas em JavaScript.
8. Deveria ser possível realizar a busca de comunicações por CPF do produtor.
9. O projeto deveria ser disponibilizado em repositório público.
10. O projeto deveria possuir um README explicando como utilizar o app.

:white_check_mark: Todos os critérios acima foram cumpridos

## Instalação
- Para ver o guia rápido de instalação, acesse esse [link](/guia/guia_inst.md)

## Como utilizar o programa
<ul>
  <li>
    <p> O acesso ao sistema é feito pelo botão no canto superior direito. Se estiver testando a versão online, o acesso pode ser feito com as credencias
      disponibilizadas acima.
    </p>
    <p align='center'>
      <img src="/guia/images/1.png" alt="home">
    </p>
  </li>
  <li>
    <p>Após o login, o usuário é redirecionado para a página inicial do sistema. Nela, já é possível verificar as opções presentes na barra de navegação vertical.</p>
    <p align='center'>
      <img src="/guia/images/2.png" alt="dashboard">
    </p>
  </li>
  <li>
    <p>Na opção 'Meus dados', o analista pode alterar seu nome e sobrenome. Neste projeto, o cadastro de novo usuário e alteração de senha 
      foram desabilitadas.
    </p>
    <p align='center'>
      <img src="/guia/images/6.png" alt="dados_analista" width="700">
    </p>
  </li>
  <li>
    <p> O usuário também pode cadastrar uma comunicação de perda em 'Nova comunicação'. No formulário, há uma verificação de garantia de veracidade do evento informado, ou seja, caso o analista esteja inserindo uma comunicação em um raio de 10km de outra já cadastrada, com a mesma data em ambas, mas com eventos diferentes, um alerta aparecerá na tela. Além disso, no formulário, existem validações de email e CPF feitas em JavaScript.
    </p>
    <p align='center'>
      <img src="/guia/images/3.png" alt="alerta" width="900">
    </p>
  </li>
  <li>
    <p>No item 'Todas as comunicações', é possível ver as entradas feitas por qualquer analista e ainda fazer buscas de comunicações por CPF do produtor.
    </p>
    <p align='center'>
      <img src="/guia/images/4.png" alt="cpf" width="900">
    </p>
  </li>
  <li>
    <p>Cada entrada na lista possui ícones para ver detalhes, editar ou excluir a comunicação de perda.</p>
    <p align='center'>
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20">
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/edit.svg" width="20" height="20">
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/trash.svg" width="20" height="20">
    </p>
  </li>
  <li>
    <p>Por fim, a funcionalidade 'Exportar dados' permite ao analista gerar um arquivo do tipo .xlsx, .csv ou .json com todos os dados de comunicações cadastradas.</p>
    <p align='center'>
      <img src="/guia/images/7.png" alt="exportar" width="700">
    </p>
  </li>
</ul>
