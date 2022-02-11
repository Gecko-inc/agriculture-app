"use strict";

let select = function () {
    let selectHeader = document.querySelectorAll(`.select-header`);
    let selectItem = document.querySelectorAll(`.select-item`);
    let m_selectHeader = document.querySelectorAll(`.m-select-header`);
    let m_selectItem = document.querySelectorAll(`.m-select-item`);


    selectHeader.forEach(item=>{
        item.addEventListener(`click`, selectToggle);
    })

    selectItem.forEach(item=>{
        item.addEventListener(`click`, selectChoose)
    });

    m_selectHeader.forEach(item=>{
        item.addEventListener(`click`, m_selectToggle);
    })
    m_selectItem.forEach(item=>{
        item.addEventListener(`click`, m_selectChoose)
    });


    function selectToggle() {
        this.parentElement.classList.toggle(`is-active`);
        document.querySelector(".select-header").classList.toggle('active');
    }
    function selectChoose() {
        let text =this.innerText,
            select = this.closest(`.select`),
            translationLung = select.querySelector(`.translation-language`);
        translationLung.innerText = text;
        document.querySelector(".select-header").classList.toggle('active');
        select.classList.add(`is-active`);
    }


    function m_selectToggle() {
        this.parentElement.classList.toggle(`m-is-active`);
        document.querySelector(".m-select-header").classList.toggle('m-active');
    }
    function m_selectChoose() {
        let m_text =this.innerText,
            select = this.closest(`.m-select`),
            translationLung = select.querySelector(`.m-translation-language`);
        translationLung.innerText = m_text;
        document.querySelector(".m-select-header").classList.toggle('m-active');
        select.classList.add(`m-is-active`);
    }


};

select();

function Footer() {
    document.querySelector(".catalog-items-footer").classList.toggle('catalog-active-footer');
    document.querySelector(".catalog-header-footer").classList.toggle('a');
}

function catalogSelect() {
    document.querySelector(".catalog-items").classList.toggle('catalog-active');
    document.querySelector(".catalog-header").classList.toggle('catalog-header-active');
}

function burgerCatalogSelect() {
    document.querySelector(".catalog-burger-items").classList.toggle('catalog-active');
    document.querySelector(".catalog-burger-header").classList.toggle('catalog-header-active');
}


function auto_grow(element) {
    element.style.height = "auto";
    element.style.height = (element.scrollHeight)+"px";

}

// const textarea = document.querySelector(".f2");
// textarea.addEventListener("keyup", e=> {
//     let scHeight = e.target.scrollHeight;
//     textarea.style.height = "100px";
//     textarea.style.height = `${scHeight}px`;
// });

function openReviewModal() {
    document.querySelector(".modal-review").classList.add('active');
}
function closeReviewModal() {
    document.querySelector(".modal-review").classList.remove('active');
}

let rev_modal = document.querySelector('.modal-review');
window.onclick = function (event) {
    if (event.target === rev_modal) {
        document.querySelector(".modal-review").classList.remove('active');
    }
}