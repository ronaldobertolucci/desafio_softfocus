(function() {
  const $btn = $('#btn')
  const $sidebar = $('.sidebar')
  const $mainContent = $('.main-content')
  const $headerContent = $('.header')

  $btn.on('click', function() {
    $sidebar.toggleClass('ativo')
    $mainContent.toggleClass('ativo')
    $headerContent.toggleClass('ativo')
  })
}())
