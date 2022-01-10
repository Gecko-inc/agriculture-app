let CommentFrom = document.getElementById('CommentFrom');
let AddCart = document.getElementById('AddCart');

CommentFrom.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(CommentFrom);
    fetch(CommentFrom.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    CommentFrom.reset();
    alert("Отзыв ушел на модерацию")

};

AddCart.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(AddCart);
    fetch(AddCart.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    alert("Товар добавлен в корзину")

};