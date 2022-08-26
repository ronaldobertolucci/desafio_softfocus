$(function() {
  let $btn = $('#btn')
  let $sidebar = $('.sidebar')
  let $mainContent = $('.main-content')

  $btn.on('click', function() {
    $sidebar.toggleClass('ativo')
    $mainContent.toggleClass('ativo')
  })
})
