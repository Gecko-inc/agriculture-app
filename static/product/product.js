"use strict";

function selectReview() {
    document.querySelector(".info-block-title-review").classList.add('active-title-review');
    document.querySelector(".info-block-title-desc").classList.add('not-active-title-desc');
    document.querySelector(".product-info-review").classList.add('active-review');
    document.querySelector(".product-info-description").classList.add('not-active-desc');
}


function selectDesc() {
    document.querySelector(".info-block-title-review").classList.remove('active-title-review');
    document.querySelector(".info-block-title-desc").classList.remove('not-active-title-desc');
    document.querySelector(".product-info-review").classList.remove('active-review');
    document.querySelector(".product-info-description").classList.remove('not-active-desc');

}


document.body.onclick = function (event) {
    event = event || window.event;
    if (event.target.classList.contains('small-photo')) {
        let src = event.target.src;
        document.querySelector(".main-photo").src = event.target.src
    }

}
