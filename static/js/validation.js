(function() {
  $('form').on('submit', function (e) {
    var valid = {};                      // cria um objeto de validação
    var isValid;
    var isFormValid;

    if (!validateEmail()) {              // verifica se o email é válido
      showErrorMessage($('#id_email_produtor'))
    } else {
      removeErrorMessage($('#id_email_produtor'));
    }

    if (!validateCPF()) {                // verifica se o CPF é válido
      showErrorMessage($('#id_cpf_produtor'))
    } else {
      removeErrorMessage($('#id_cpf_produtor'));
    }

    for (var field in valid) {           // verifica cada campo em valid
      if (!valid[field]) {
        isFormValid = false;
        break;
      }
      isFormValid = true;                // se todos forem verdadeiros, submeta
    }

    if (!isFormValid) {
      e.preventDefault();
    }

    /* função de validação de CPF baseada no código de Arthur Ronconi,
       que, por sua vez, se inspirou no script/regras da Receita Federal
       http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/funcoes.js */
    function validateCPF() {
      const $cpfField = $('#id_cpf_produtor');
      setErrorMessage($cpfField, 'CPF inválido');
      var Soma = 0;
      var Resto;
      var strCPF = $cpfField.val().replace(/[^\d]/g, '');
      valid.cpf = false;

      if (strCPF.length !== 11)
        return valid.cpf

      if ([
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999',
      ].indexOf(strCPF) !== -1)
        return valid.cpf

      for (i=1; i<=9; i++)
        Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (11 - i);

      Resto = (Soma * 10) % 11

      if ((Resto == 10) || (Resto == 11))
        Resto = 0

      if (Resto != parseInt(strCPF.substring(9, 10)) )
        return valid.cpf

      Soma = 0

      for (i = 1; i <= 10; i++)
        Soma = Soma + parseInt(strCPF.substring(i-1, i)) * (12 - i)

      Resto = (Soma * 10) % 11

      if ((Resto == 10) || (Resto == 11))
        Resto = 0

      if (Resto != parseInt(strCPF.substring(10, 11) ) )
        return valid.cpf

      valid.cpf = true;
      return valid.cpf
    }



    // validação de email
    function validateEmail() {
      const $emailField = $('#id_email_produtor')
      // expressão regular para um email
      const emailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      valid.email = false;
      if ($emailField.val().match(emailFormat)) {
        valid.email = true;
      } else {
        setErrorMessage($emailField, 'Endereço de email inválido')
      }
      return valid.email;
    }


    // guarde a mensagem de erro no elemento
    function setErrorMessage(el, message) {
      $(el).data('errorMessage', message);
    }

    function getErrorMessage(el) {
      return $(el).data('errorMessage') || el.title;
    }

    function showErrorMessage(el) {
      var $el = $(el);
      var errorContainer = $el.siblings('.error.message'); // caso existam erros

      if (!errorContainer.length) {                         // caso não existam erros
         // crie um span, após o el, para segurar a mensagem de erro
         errorContainer = $('<span class="error message"></span>').insertAfter($el);
      }
      errorContainer.text(getErrorMessage(el));             // Adicione a msg
    }

    function removeErrorMessage(el) {
      var errorContainer = $(el).siblings('.error.message');
      errorContainer.remove();                               // remova o erro
    }
  })
}());
