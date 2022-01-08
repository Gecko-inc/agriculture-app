"use strict"
// alert("hello world!00");
const ratings = document.querySelectorAll(`.rating`);
if (ratings.length > 0) {
    initRatings();
}

//Основная функция
function initRatings(){
    let ratingActive, ratingValue;
    //бегаем по всем рейтингам по странице
    for (let index = 0; index < ratings.length; index++) {
        const rating = ratings[index];
        initRating(rating);
    }

    //инициализируем конкретный рейтинг
    function initRating(rating) {
        initRatingVars(rating);

        setRatingActiveWidth();

        if (rating.classList.contains('rating_set')) {
            setRating(rating);
        }
    }

    //инициализация перменных
    function initRatingVars(rating) {
        ratingActive = rating.querySelector('.rating_active');
        ratingValue = rating.querySelector('.rating_value');
    }

    //изменение ширины активных звезд
    function setRatingActiveWidth(index = ratingValue.innerHTML) {
        const ratingActiveWidth = index / 0.05;
        ratingActive.style.width = `${ratingActiveWidth}%`;
    }

    //возможность ставить оценку
    function setRating(rating){
        const ratingItems = rating.querySelectorAll('.rating_item');
        for (let index = 0; index < ratingItems.length; index++) {
            const ratingItem = ratingItems[index];
            ratingItem.addEventListener("mouseenter", function () {
                //обновление переменных
                initRatingVars(rating);
                //обновление активных звезд
                setRatingActiveWidth(ratingItem.value);
            });
            ratingItem.addEventListener("mouseleave", function () {

                //обновление активных звезд
                setRatingActiveWidth();
            });

            ratingItem.addEventListener("click", function () {
                //обновление переменных
                initRatingVars(rating);

                // if (rating.dataset.ajax) {
                //     //отправить на сервер
                //     setRatingValue(ratingItem.value, rating);
                // }
                // else {
                //отобразить указанную оценку
                ratingValue.innerHTML = index + 1;
                setRatingActiveWidth();
                // }
            });
        }
    }
}
