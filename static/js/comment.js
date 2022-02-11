let CommentFrom = document.getElementById('regForm');

CommentFrom.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(CommentFrom);
    fetch(CommentFrom.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    CommentFrom.reset();
    openReviewModal();
    // el = document.getElementById('feedback');
    // el.innerHTML = "<b>Спасибо за отзыв</b>"

};
