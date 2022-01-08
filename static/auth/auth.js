"use strict"

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('authForm');
    form.addEventListener('submit', formSend);

    async function formSend(e) {
        e.preventDefault();

        let error = formValidate(form);

        if (error===0){

        }else {

            document.getElementsByClassName('auth-form_email')[0].placeholder = 'Пожалуйста, заполните это поле';
            document.getElementsByClassName('password')[0].placeholder = 'Пожалуйста, заполните это поле';

        }
    }

    function formValidate(form) {
        let error = 0;
        let formReq = document.querySelectorAll('._req');

        for (let index = 0; index < formReq.length; index++) {
            const input = formReq[index];

            if (input.classList.contains('_email')){
                if (emailTest(input)){
                    formAddErrorRed(input);
                    error++;

                }
            }
            else {
                if (input.value === '') {

                    formAddErrorRed(input);
                    error++;
                }
            }
        }
        return error;
    }

    //функция теста email
    function emailTest(input) {
        return !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(input.value);
    }

    function formAddErrorRed(input) {
        input.parentElement.classList.add('_red');
        input.classList.add('_red');
    }

});

