const validation = new window.JustValidate('.form', {
  errorFieldCssClass: 'is-invalid',
  errorFieldStyle: {
    border: '1px solid #FF5C00',
  },
  errorLabelCssClass: 'is-label-invalid',
  errorLabelStyle: {
    color: '#FF5C00',
  },
  focusInvalidField: true,
  lockForm: true,
});

validation
.addField('.input-name', [
  {
    rule: 'required',
    errorMessage: 'Вы не ввели данные'
  },
  {
    rule: 'minLength',
    value: 3,
    errorMessage: 'Имя должно содержать хотя бы 3 буквы'
  },
  {
    rule: 'maxLength',
    value: 30,
    errorMessage: 'Имя не может содержать более 30 символов'
  }
])
.addField('.input-lastname', [
  {
    rule: 'required',
    errorMessage: 'Вы не ввели данные'
  },
  {
    rule: 'minLength',
    value: 3,
    errorMessage: 'Фамилия должно содержать хотя бы 3 буквы'
  },
  {
    rule: 'maxLength',
    value: 30,
    errorMessage: 'Фамилия не может содержать более 30 символов'
  }
])
.addField('.input-middlename', [
  {
    rule: 'required',
    errorMessage: 'Вы не ввели данные'
  },
  {
    rule: 'minLength',
    value: 3,
    errorMessage: 'Отчество должно содержать хотя бы 3 буквы'
  },
  {
    rule: 'maxLength',
    value: 30,
    errorMessage: 'Отчество не может содержать более 30 символов'
  }
])
.addField('.input-mail', [
  {
    rule: 'required',
    errorMessage: 'Вы не ввели e-mail',
  },
  {
    rule: 'email',
    errorMessage: 'E-mail должен содержать @',
  },
]);

