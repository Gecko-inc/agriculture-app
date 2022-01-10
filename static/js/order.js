let text = "Заявка успешно отправлена!";
let Form = document.getElementById('form');

Form.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(Form);
    fetch(Form.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    Form.reset();
    alert(text);
    window.location.replace("/cart");

};
