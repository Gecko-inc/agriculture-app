let SubscribeView = document.getElementById('SubscribeView');

SubscribeView.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(SubscribeView);
    fetch(SubscribeView.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    SubscribeView.reset();
    // el = document.getElementById('feedback');
    // el.innerHTML = "<b>Спасибо за отзыв</b>"

};
