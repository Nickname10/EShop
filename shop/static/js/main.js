const buttonNextTen = document.querySelector('.next-ten');
const buttonPreviousTen = document.querySelector('.previous-ten');
let currentPage = 0;

buttonNextTen.addEventListener("click", () => {
    HTTP.Get(String(++currentPage));
});
buttonPreviousTen.addEventListener("click", () => {
    HTTP.Get((String(--currentPage)));
});

class HTTP {
    constructor() {
    }

    checkStatus(response) {
        if (response.status >= 200 && response.status < 300) {
            return response;
        }
        const error = new Error(response.statusText);
        error.response = response;
        throw error;
    }

    static Get(url) {

        return fetch(url).then(this.checkStatus).then((response) =>
            response.json()).then(data => ShowItems(data));
    }
}

function ShowItems(data) {
    document.querySelector('.items-box').innerHTML = "";
    console.log(data['Items'].forEach(item => {
        let cardItem = document.createElement('div');
        let title = document.createElement('div');
        let itemPrice = document.createElement('div');
        let itemDescription = document.createElement('div');
        let itemImageBox = document.createElement('div');
        let image = document.createElement('img');

        cardItem.classList.add('item');
        title.classList.add('item-title');
        itemPrice.classList.add('item-price');
        itemDescription.classList.add('item-description');
        itemImageBox.classList.add('item-img-box');
        image.classList.add('item-img');

        image.setAttribute('src','/media/'+ item.image);
        image.setAttribute('alt','');

        itemImageBox.appendChild(image);

        title.textContent = item.title;
        itemPrice.textContent = item.price;
        itemDescription.textContent = item.description;

        cardItem.appendChild(itemImageBox);
        cardItem.appendChild(title);
        cardItem.appendChild(itemDescription);
        cardItem.appendChild(itemPrice);

        document.querySelector('.items-box').appendChild(cardItem);

    }));

}

