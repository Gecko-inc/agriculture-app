"use strict";

let select = function () {
    let selectHeader = document.querySelectorAll(`.select-header`);
    let selectItem = document.querySelectorAll(`.select-item`);


    selectHeader.forEach(item=>{
        item.addEventListener(`click`, selectToggle);
    })

    selectItem.forEach(item=>{
        item.addEventListener(`click`, selectChoose)
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


};

select();

function catalogSelect() {
    document.querySelector(".catalog-items").classList.toggle('catalog-active');
    document.querySelector(".catalog-header").classList.toggle('catalog-header-active');
}

