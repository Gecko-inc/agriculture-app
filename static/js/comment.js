let CommentFrom = document.getElementById('CommentFrom');

CommentFrom.onsubmit = async (e) => {
    e.preventDefault();
    let data = new FormData(CommentFrom);
    console.log(CommentFrom.getAttribute('action'));
    fetch(CommentFrom.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    sendForm();

};
