# Guia de instalação e utilização deste projeto 

## Requerimentos
- Docker
- Git

## Deployment
Este projeto também está online na plataforma Heroku em [www]()
- login:
- senha:

## Instalação 
- Para ver o guia rápido de instalação, acesse esse [link](/guia/guia_inst.md)

## Como utilizar o programa
<ul>
  <li>
    <p> O acesso ao sistema é feito pelo botão no canto superior direito. Se estiver testando a versão online, o acesso pode ser feito com as credencias
      disponibilizadas acima. 
    </p>
    <p align='center'>
      <img src="/guia/images/1.png" alt="home" style="max-width: 100%;">
    </p>
  </li>
  <li>
    <p>Após o login, o usuário é redirecionado para a página inicial do sistema. Nela, já é possível verificar as opções presentes na barra de navegação vertical.</p>
    <p align='center'>
      <img src="/guia/images/2.png" alt="home" style="max-width: 100%;">
    </p>
  </li>
  <li>
    <p>Na opção 'Meus dados', o analista pode alterar seu nome, sobrenome e email. Neste projeto, o cadastro de novo usuário e alteração de senha 
      foram desabilitadas.
    </p>
  </li>
  <li>
    <p> Em 'Nova comunicação', o usuário pode cadastrar uma comunicação de perda. No formulário, existem validações de email e CPF feitas em JavaScript, assim como uma 
verificação de garantia de veracidade do evento informado, ou seja, caso o analista esteja inserindo uma comunicação de uma lavoura em um raio de 10km de outra já
cadastrada, com a mesma data em ambas, mas com eventos diferentes, um alerta aparecerá na tela.
    </p>
    <p align='center'>
      <img src="/guia/images/3.png" alt="home" style="max-width: 100%;">
    </p>
  </li>
  <li>
    <p>No item 'Todas as comunicações', é possível ver as entradas feitas por qualquer analista e ainda fazer buscas de comunicações por CPF do produtor. 
    </p>
    <p align='center'>
      <img src="/guia/images/4.png" alt="home" style="max-width: 100%;">
    </p>
  </li>
  <li>
    <p>Cada entrada na lista, possui ícones para ver detalhes, editar ou excluir a comunicação de perda.</p>
    <p align='center'>
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/circle-info.svg" width="20" height="20">
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/edit.svg" width="20" height="20">
      <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/5.x/svgs/solid/trash.svg" width="20" height="20">
    </p>
  </li>
  <li>
    <p>Na opção 'Exportar dados', o analista ainda pode gerar (com um clique) um arquivo .xlsx com todos os dados de comunicações no banco de dados.</p>
  </li>
</ul>
