let CommentFrom = document.getElementById('AddCart');

CommentFrom.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(CommentFrom);
    fetch(CommentFrom.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    document.getElementById('AddToCart').innerHTML("<div>Товар добавлен в корзину</div>");
    // CommentFrom.reset();
    // openReviewModal();
    // el = document.getElementById('feedback');
    // el.innerHTML = "<b>Спасибо за отзыв</b>"

};
