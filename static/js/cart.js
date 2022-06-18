var element_1 = document.getElementById('ItemList');
var element_2 = document.getElementById('CartTotal');

document.addEventListener("click", function (e) {
    if (e.target.className == "ButtonPlus") {
        let response = fetch("/ru/cart/edit/", {
            method: 'POST',
            body: JSON.stringify({"id": e.target.id, "action": "+"})
        })
        .then(response => {
            if (response.status !== 200) {

                return Promise.reject();
            }
            return response.text()
        })
        .then(data => {
                element_1.innerHTML = JSON.parse(data).html;
                element_2.innerHTML = JSON.parse(data).total
            }
        );
    }
});
document.addEventListener("click", function (e) {
    if (e.target.className == "basket-title del ButtonDelete") {
        let response = fetch("/ru/cart/delete/", {
            method: 'POST',
            body: JSON.stringify({"id": e.target.id})
        })
        .then(response => {
            if (response.status !== 200) {

                return Promise.reject();
            }
            return response.text()
        })
        .then(data =>
            {
                element_1.innerHTML = JSON.parse(data).html;
                element_2.innerHTML = JSON.parse(data).total
            }
        );
    }
});
document.addEventListener("click", function (e) {
    if (e.target.className == "ButtonMinus") {
        let response = fetch("/ru/cart/edit/", {
            method: 'POST',
            body: JSON.stringify({"id": e.target.id, "action": "-"})
        })
        .then(response => {
            if (response.status !== 200) {

                return Promise.reject();
            }
            return response.text()
        })
        .then(data =>
            {
                element_1.innerHTML = JSON.parse(data).html;
                element_2.innerHTML = JSON.parse(data).total
            }
        );
    }
});