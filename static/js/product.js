"use strict";

var iframe_el = document.getElementsByTagName('iframe')[0];
iframe_el.setAttribute( 'class', 'video-style' );

function selectDesc() {
    document.querySelector(".info-block-title-review").classList.remove('active-title-review');
    document.querySelector(".product-info-review").classList.remove('active-review');
    document.querySelector(".info-block-title-desc").classList.remove('not-active-title-desc');
    document.querySelector(".product-info-description").classList.remove('not-active-desc');
    document.querySelector(".info-block-title-character").classList.remove('active');
    document.querySelector(".product-info-character").classList.remove('active');
    document.querySelector(".info-block-title-certif").classList.remove('active');
    document.querySelector(".product-info-certif").classList.remove('active');
    document.querySelector(".info-block-title-extraInfo").classList.remove('active');
    document.querySelector(".product-info-extraInfo").classList.remove('active');

}

function selectReview() {
    document.querySelector(".info-block-title-review").classList.add('active-title-review');
    document.querySelector(".info-block-title-desc").classList.add('not-active-title-desc');
    document.querySelector(".product-info-review").classList.add('active-review');
    document.querySelector(".product-info-description").classList.add('not-active-desc');
    document.querySelector(".info-block-title-character").classList.remove('active');
    document.querySelector(".product-info-character").classList.remove('active');
    document.querySelector(".info-block-title-certif").classList.remove('active');
    document.querySelector(".product-info-certif").classList.remove('active');
    document.querySelector(".info-block-title-extraInfo").classList.remove('active');
    document.querySelector(".product-info-extraInfo").classList.remove('active');
}

function selectCharacter() {
    document.querySelector(".info-block-title-review").classList.remove('active-title-review');
    document.querySelector(".info-block-title-desc").classList.add('not-active-title-desc');
    document.querySelector(".product-info-review").classList.remove('active-review');
    document.querySelector(".product-info-description").classList.add('not-active-desc');
    document.querySelector(".info-block-title-character").classList.add('active');
    document.querySelector(".product-info-character").classList.add('active');
    document.querySelector(".info-block-title-certif").classList.remove('active');
    document.querySelector(".product-info-certif").classList.remove('active');
    document.querySelector(".info-block-title-extraInfo").classList.remove('active');
    document.querySelector(".product-info-extraInfo").classList.remove('active');
}

function selectCertif() {
    document.querySelector(".info-block-title-review").classList.remove('active-title-review');
    document.querySelector(".info-block-title-desc").classList.add('not-active-title-desc');
    document.querySelector(".product-info-review").classList.remove('active-review');
    document.querySelector(".product-info-description").classList.add('not-active-desc');
    document.querySelector(".info-block-title-character").classList.remove('active');
    document.querySelector(".product-info-character").classList.remove('active');
    document.querySelector(".info-block-title-certif").classList.add('active');
    document.querySelector(".product-info-certif").classList.add('active');
    document.querySelector(".info-block-title-extraInfo").classList.remove('active');
    document.querySelector(".product-info-extraInfo").classList.remove('active');
}

function selectExtraInfo() {
    document.querySelector(".info-block-title-review").classList.remove('active-title-review');
    document.querySelector(".info-block-title-desc").classList.add('not-active-title-desc');
    document.querySelector(".product-info-review").classList.remove('active-review');
    document.querySelector(".product-info-description").classList.add('not-active-desc');
    document.querySelector(".info-block-title-character").classList.remove('active');
    document.querySelector(".product-info-character").classList.remove('active');
    document.querySelector(".info-block-title-certif").classList.remove('active');
    document.querySelector(".product-info-certif").classList.remove('active');
    document.querySelector(".product-info-extraInfo").classList.add('active');
    document.querySelector(".info-block-title-extraInfo").classList.add('active');
}


document.body.onclick = function (event) {
    event = event || window.event;
    if (event.target.classList.contains('small-photo')) {
        let src = event.target.src;
        document.querySelector(".main-photo").src = event.target.src;
        document.querySelector(".video").classList.remove('video-active');
        document.querySelector(".main-photo").classList.remove('none');
    }
};

window.addEventListener('DOMContentLoaded', function () {
    let video = document.querySelector('.small-video');
    let main = document.querySelector('.main-photo-block');
    let small = document.querySelectorAll('.small-photo');


    video.addEventListener('click', function () {

        document.querySelector(".main-photo").classList.toggle('none');
        document.querySelector(".video").classList.toggle('video-active');
        if (video.classList.contains('ready')) {
            return;
        }
        video.classList.add('ready');
    });
});


function descSelect() {
    document.querySelector(".mobile-desc-container").classList.toggle('active');
    document.querySelector(".mobile-desc-arrow").classList.toggle('active');
}

function characterSelect() {
    document.querySelector(".mobile-character-container").classList.toggle('active');
    document.querySelector(".mobile-character-arrow").classList.toggle('active');
}

function certifSelect() {
    document.querySelector(".mobile-certif-container").classList.toggle('active');
    document.querySelector(".mobile-certif-arrow").classList.toggle('active');
}

function extraInfoSelect() {
    document.querySelector(".mobile-extraInfo-container").classList.toggle('active');
    document.querySelector(".mobile-extraInfo-arrow").classList.toggle('active');
}

function reviewSelect() {
    document.querySelector(".mobile-review-container").classList.toggle('active');
    document.querySelector(".mobile-review-arrow").classList.toggle('active');
}


function openReview() {
    document.querySelector(".modal").classList.add('active');
}

function closeReview() {
    document.querySelector(".modal").classList.remove('active');
}

let modal = document.querySelector('.modal');
window.onclick = function (event) {
    if (event.target === modal) {
        document.querySelector(".modal").classList.remove('active');
    }
}

//модольное окно

//переключение вперед
function nextPage1() {
    document.querySelector(".page-1").classList.add('none');
    document.querySelector(".next-1").classList.add('none');
    document.querySelector(".step-1").classList.add('none');
    document.querySelector(".alert").classList.add('none');

    document.querySelector(".page-2").classList.add('active');
    document.querySelector(".next-2").classList.add('active');
    document.querySelector(".back-2").classList.add('active');
    document.querySelector(".step-2").classList.add('active');
}

function nextPage2() {
    document.querySelector(".page-2").classList.remove('active');
    document.querySelector(".next-2").classList.remove('active');
    document.querySelector(".back-2").classList.remove('active');
    document.querySelector(".step-2").classList.remove('active');

    document.querySelector(".page-3").classList.add('active');
    document.querySelector(".next-3").classList.add('active');
    document.querySelector(".back-3").classList.add('active');
    document.querySelector(".step-3").classList.add('active');

}

function nextPage3() {
    document.querySelector(".page-3").classList.remove('active');
    document.querySelector(".next-3").classList.remove('active');
    document.querySelector(".back-3").classList.remove('active');
    document.querySelector(".step-3").classList.remove('active');

    document.querySelector(".page-4").classList.add('active');
    document.querySelector(".next-4").classList.add('active');
    document.querySelector(".back-4").classList.add('active');
    document.querySelector(".step-4").classList.add('active');
}

function sendForm() {
    let CommentFrom = document.getElementById('CommentForm');
    let data = new FormData(CommentFrom);
    fetch(CommentFrom.getAttribute('action'), {
        method: 'POST',
        body: data
    });
    document.querySelector(".page-4").classList.remove('active');
    document.querySelector(".next-4").classList.remove('active');
    document.querySelector(".back-4").classList.remove('active');
    document.querySelector(".step-4").classList.remove('active');

    document.querySelector(".page-5").classList.add('active');

    // alert("Спасибо за Ваш отзыв, он будет отправлен на модерацию!")
}


//переключение назад
function backPage2() {
    document.querySelector(".page-1").classList.remove('none');
    document.querySelector(".next-1").classList.remove('none');
    document.querySelector(".step-1").classList.remove('none');
    document.querySelector(".alert").classList.remove('none');

    document.querySelector(".page-2").classList.remove('active');
    document.querySelector(".next-2").classList.remove('active');
    document.querySelector(".back-2").classList.remove('active');
    document.querySelector(".step-2").classList.remove('active');
}

function backPage3() {
    document.querySelector(".page-2").classList.add('active');
    document.querySelector(".next-2").classList.add('active');
    document.querySelector(".back-2").classList.add('active');
    document.querySelector(".step-2").classList.add('active');

    document.querySelector(".page-3").classList.remove('active');
    document.querySelector(".next-3").classList.remove('active');
    document.querySelector(".back-3").classList.remove('active');
    document.querySelector(".step-3").classList.remove('active');
}

function backPage4() {
    document.querySelector(".page-3").classList.add('active');
    document.querySelector(".next-3").classList.add('active');
    document.querySelector(".back-3").classList.add('active');
    document.querySelector(".step-3").classList.add('active');

    document.querySelector(".page-4").classList.remove('active');
    document.querySelector(".next-4").classList.remove('active');
    document.querySelector(".back-4").classList.remove('active');
    document.querySelector(".step-4").classList.remove('active');
}
