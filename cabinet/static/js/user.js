cartLinkAdd();
addEventFavorite();
addEventRemoveWishListItem();
addEventBuy();

class HTTP2 {
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

    static Get(url, fun) {
        return fetch(url).then(this.checkStatus).then((response) =>
            response.json()).then(data => fun(data));
    }
}


function cartLinkAdd() {
    let linksAdd = document.getElementsByClassName("js-add-cart");
    for (let i = 0; i < linksAdd.length; i++) {
        linksAdd[i].addEventListener("click", () => {

            HTTP2.Get("cart/add/" + linksAdd[i].getAttribute("value"), addToCart);
        })
    }


}

function addToCart(data) {
    M.toast({html: 'Успешно добвлено', classes: "notification-add"});
    showCart(data);
}


document.querySelector('.cart-open').addEventListener('click', () => {
    HTTP2.Get('cart/view/', showCart);
    let start = Date.now(); // запомнить время начала

    let timer = setInterval(function () {
        // сколько времени прошло с начала анимации?
        let timePassed = Date.now() - start;

        if (timePassed >= 1000) {
            clearInterval(timer); // закончить анимацию через 2 секунды
            return;
        }

        // отрисовать анимацию на момент timePassed, прошедший с начала анимации
        draw(timePassed);

    }, 10);

    // в то время как timePassed идёт от 0 до 2000
    // left изменяет значение от 0px до 400px
    function draw(timePassed) {

        document.querySelector('.user-cabinet').style.top = -900 + timePassed / 1.1 + 'px';
    }
})
document.querySelector('.cart-close').addEventListener('click', () => {
    let start = Date.now(); // запомнить время начала

    let timer = setInterval(function () {
        // сколько времени прошло с начала анимации?
        let timePassed = Date.now() - start;

        if (timePassed >= 1000) {
            clearInterval(timer); // закончить анимацию через 2 секунды
            return;
        }

        // отрисовать анимацию на момент timePassed, прошедший с начала анимации
        draw(timePassed);

    }, 10);

    // в то время как timePassed идёт от 0 до 2000
    // left изменяет значение от 0px до 400px
    function draw(timePassed) {

        document.querySelector('.user-cabinet').style.top = -timePassed / 1.1 + 'px';
    }

})


function showCart(data) {
    console.log(data);
    document.querySelector('.user-cart-items').innerHTML = "";
    data["Items"].forEach(item => {
        console.log(item.id);
        let divCartItems = document.createElement("div");
        let pCartItemsImg = document.createElement("p");
        let imgItem = document.createElement("img");
        let pCartItemsName = document.createElement("p");
        let pCartItemsCost = document.createElement("p");
        let pCartItemsClose = document.createElement("p");
        let iCartItemsClose = document.createElement("i");
        divCartItems.appendChild(pCartItemsImg);
        divCartItems.appendChild(pCartItemsName);
        divCartItems.appendChild(pCartItemsCost);
        divCartItems.appendChild(pCartItemsClose);
        pCartItemsImg.appendChild(imgItem);
        pCartItemsClose.appendChild(iCartItemsClose);
        iCartItemsClose.textContent = 'close';
        divCartItems.classList.add("cart-items");
        pCartItemsImg.classList.add('cart-items-img');
        pCartItemsName.classList.add('cart-items-name');
        pCartItemsCost.classList.add('cart-items-cost');
        iCartItemsClose.classList.add('material-icons');
        pCartItemsClose.classList.add('cart-items-close');
        imgItem.src = '/media/' + item.image;
        pCartItemsName.textContent = item.title;
        pCartItemsCost.textContent = item.price + "$";
        pCartItemsClose.addEventListener("click", () => {
            HTTP2.Get("cart/remove/" + item.id, removeCart)
        });
        document.querySelector('.user-cart-items').appendChild(divCartItems);
    });

    document.querySelector('.cart-total-cost-p').textContent = "Total price: " + data.Price + "$";


}


function removeCart(data) {
    M.toast({html: 'Успешно удалено', classes: "notification-add"});
    showCart(data);
}

function addEventFavorite() {
    let btnAddToWishList = document.getElementsByClassName('js-add-to-wish-list');
    for (let i = 0; i < btnAddToWishList.length; i++) {
        btnAddToWishList[i].addEventListener('click', () => {
            HTTP.Get('addToList/' + btnAddToWishList[i].getAttribute('value'), checkResponseAddToWishList)
        })
    }
}

function checkResponseAddToWishList(data) {
    if (data.Status === "REDIRECT") {
        window.location.replace('/shop/login/');
    }
    M.toast({html: 'Добавлено в список желаемого', classes: "notification-add"});

}
function addEventRemoveWishListItem() {
  let btnsRemove = document.querySelectorAll('.js-remove-list-item').forEach((btn)=>
      btn.addEventListener('click', ()=>{
        HTTP2.Get("removeWishListItem/"+btn.getAttribute('value')+"/",(data)=>{});
        window.location.reload();
      })
  )

}
function addEventBuy()
{
    document.querySelector('.js-btn-buy').addEventListener('click',()=>{
        HTTP2.Get('/shop/cart/buy/',(data)=>{
           if  (data["response"] === "OK"){
             M.toast({html: 'Заказ добавлен в очередь', classes: "notification-add"});
           }
           else
           {
               window.location.replace('/shop/login/');
           }
        });
    })
}