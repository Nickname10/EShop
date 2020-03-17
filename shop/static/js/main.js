const buttonNextTen = document.querySelector('.next-ten');
const buttonPreviousTen = document.querySelector('.previous-ten');
cartLinkAdd();
var currentPage = 0;
buttonNextTen.addEventListener("click", () => {
    currentPage++;
    renderRequest();
});
buttonPreviousTen.addEventListener("click", () => {
    currentPage--;
    renderRequest()
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

    static Get(url, fun) {

        return fetch(url).then(this.checkStatus).then((response) =>
            response.json()).then(data => fun(data));
    }
}

function ShowItems(data) {
    document.querySelector('.items-box').innerHTML = "";

    data['Items'].forEach(item => {
        let divRow = document.createElement("div");
        let divCols12m6rowItems = document.createElement("div");
        let divCard = document.createElement("div");
        let divCardImage = document.createElement("div");
        let aModalTrigger = document.createElement("a");
        let itemImageMaterialBoxed = document.createElement("img");
        let divModal = document.createElement("div");
        let divModalContent = document.createElement("div");
        let divModalContentSource = document.createElement("div");
        let divModalImg = document.createElement("div");
        let divSourceInfo = document.createElement("div");
        let divSourceTitle = document.createElement("div");
        let divSourceCost = document.createElement("div");
        let spanSourceCost = document.createElement("span");
        let divSourceBrand = document.createElement("div");
        let spanSourceBrand = document.createElement("span");
        let divModalDescTitle = document.createElement("div");
        let divModalDescription = document.createElement("div");
        let divModalComment = document.createElement("div");
        let divCommentTitle = document.createElement("div");
        let divCommentForm = document.createElement("div");
        let divRowCommentField = document.createElement("div");
        let formColS12 = document.createElement("form");
        let divRowCommentFieldUnderForm = document.createElement("div");
        let divInputFieldColS6 = document.createElement("div");
        let iMaterialIconsPrefix = document.createElement("i");
        let textAreaIconPrefix = document.createElement("textarea");
        let labelIconPrefix = document.createElement("label");

        let divModalCommentItems = document.createElement("div");

        // need render comment between for and endfor
        let divModalFooter = document.createElement("div");
        let aModalCloseWaveEffect = document.createElement("a");
        let spanCardTitle = document.createElement("span");
        let aBtnFloatingHalfway = document.createElement("a");
        let iMaterialIcons = document.createElement("i");
        let divCardContent = document.createElement("div");
        let pShortDescription = document.createElement("p");
        let spanCardTitleName = document.createElement("span");
        let spanCardTitleCost = document.createElement("span");
        document.querySelector(".items-box").appendChild(divRow);

        divRow.appendChild(divCols12m6rowItems);
        divCols12m6rowItems.appendChild(divCard);
        divCard.appendChild(divCardImage);
        divCard.appendChild(divCardContent);
        divCardImage.appendChild(aModalTrigger);
        divCardImage.appendChild(itemImageMaterialBoxed);
        divCardImage.appendChild(divModal);
        divCardImage.appendChild(spanCardTitle);
        divCardImage.appendChild(aBtnFloatingHalfway);

        aBtnFloatingHalfway.appendChild(iMaterialIcons);
        divModal.appendChild(divModalContent);
        divModal.appendChild(divModalFooter);
        divModalFooter.appendChild(aModalCloseWaveEffect)
        divModalContent.appendChild(divModalContentSource);
        divModalContent.appendChild(divModalDescTitle);
        divModalContent.appendChild(divModalDescription);
        divModalContent.appendChild(divModalComment);
        divModalContentSource.appendChild(divModalImg);
        divModalContentSource.appendChild(divSourceInfo);
        divSourceInfo.appendChild(divSourceTitle);
        divSourceInfo.appendChild(divSourceCost);
        divSourceInfo.appendChild(divSourceBrand);
        divModalComment.appendChild(divCommentTitle);
        divModalComment.appendChild(divCommentForm);
        divCommentForm.appendChild(divRowCommentField);
        divModalComment.appendChild(divModalCommentItems);
        divRowCommentField.appendChild(formColS12);
        formColS12.appendChild(divRowCommentFieldUnderForm);
        divRowCommentFieldUnderForm.appendChild(divInputFieldColS6);
        divInputFieldColS6.appendChild(iMaterialIconsPrefix);
        divInputFieldColS6.appendChild(textAreaIconPrefix);
        divInputFieldColS6.appendChild(labelIconPrefix);
        divCardContent.appendChild(pShortDescription);
        spanCardTitle.appendChild(spanCardTitleName);
        spanCardTitle.appendChild(spanCardTitleCost);

        divRow.classList.add("row");
        divCols12m6rowItems.classList.add("col", "s12", "m6", "row-items");
        divCard.classList.add("card");
        divCardImage.classList.add("card-image");
        aModalTrigger.classList.add("waves-effect", "waves-light", "btn", "modal-trigger");
        itemImageMaterialBoxed.classList.add("materialboxed");
        divModal.classList.add("modal");
        divModalContent.classList.add("modal-content");
        divModalContentSource.classList.add("modal-content-source");
        divModalImg.classList.add("modal-img");
        divSourceInfo.classList.add("source-info");
        divSourceTitle.classList.add("source-title");
        divSourceCost.classList.add("source-cost");
        divSourceBrand.classList.add("source-brand");
        divModalDescTitle.classList.add("modal-desc-title");
        divModalDescription.classList.add("modal-description");
        divModalComment.classList.add("modal-comment");
        divCommentTitle.classList.add("comment-title");
        divModalCommentItems.classList.add("modal-comment-items");
        divCommentForm.classList.add("comment-form");
        divRowCommentField.classList.add("row");
        divRowCommentField.id = "comment-field";
        formColS12.classList.add("col", "s12");
        divInputFieldColS6.classList.add("input-field", "col", "s6");
        divInputFieldColS6.id = "ww";
        divRowCommentFieldUnderForm.classList.add("row");
        divRowCommentField.id = "ww";
        iMaterialIconsPrefix.classList.add("material-icons", "prefix");
        textAreaIconPrefix.id = "icon_prefix2";
        textAreaIconPrefix.classList.add("materialize-textarea");
        divModalFooter.classList.add("modal-footer");
        aModalCloseWaveEffect.classList.add("modal-close", "waves-effect", "waves-green", "btn-flat");
        spanCardTitle.classList.add("card-title");
        aBtnFloatingHalfway.classList.add("btn-floating", "halfway-fab", "waves-effect", "waves-light", "red", "js-add-cart");
        iMaterialIcons.classList.add("material-icons");
        divCardContent.classList.add("card-content");
        spanCardTitleName.classList.add("card-title-name");
        spanCardTitleCost.classList.add("card-cost");
        textAreaIconPrefix.style.height = "43px";

        aModalTrigger.href = "#i" + item.id; // айтем айди будет получин возже item.id
        itemImageMaterialBoxed.src = "/media/" + item.image;//item.image.url
        divModal.id = "i" + item.id;
        divModalImg.style.background = 'url("/media/' + item.image + '"';
        divModalImg.style.background += "no-repeat";
        divModalImg.style.backgroundSize = "contain";
        divModalImg.style.width = "600px";
        aBtnFloatingHalfway.setAttribute("value", item.id)
        labelIconPrefix.setAttribute('for', 'icon_prefix2');
        labelIconPrefix.textContent = 'Your comment';
        aModalTrigger.textContent = "More";
        divSourceTitle.textContent = item.title;
        divSourceCost.textContent = "Cost : ";
        divSourceCost.appendChild(spanSourceCost);
        spanSourceCost.textContent = item.price + " $";
        divSourceBrand.textContent = "Brand: ";
        divSourceBrand.appendChild(spanSourceBrand);
        spanSourceBrand.textContent = item.Brand;
        pShortDescription.textContent = item.short_description;
        divModalDescTitle.textContent = "Description";
        divModalDescription.textContent = item.long_description;
        divCommentTitle.textContent = "Comments :";
        iMaterialIcons.textContent = "add";
        iMaterialIconsPrefix.textContent = "mode_edit";
        spanCardTitleName.textContent = item.title;
        spanCardTitleCost.textContent = item.price + "$";
        let allComments = data["Comments"].filter(c => c.item_id === item.id);
        allComments.forEach(c =>
        {
           let divCommentItem = document.createElement("div");
           let divCommentItemInfo = document.createElement("div");
           let divCommentInfo = document.createElement("div");
           let divCommentDate = document.createElement("div");
           let imgCommentItemLogo = document.createElement("img");
           let pCommentNickname = document.createElement("p");
           divCommentItem.appendChild(divCommentItemInfo);
           divCommentItem.appendChild(divCommentInfo);
           divCommentItem.appendChild(divCommentDate);
           divCommentItemInfo.appendChild(imgCommentItemLogo);
           divCommentItemInfo.appendChild(pCommentNickname);
           divCommentItem.classList.add("comment-item");
           divCommentItemInfo.classList.add("comment-item-info");
           divCommentInfo.classList.add("coment-info");
           divCommentDate.classList.add("commnet-date");
           console.log(c);
           imgCommentItemLogo.src= '/media/' +c.profile__photo;
           imgCommentItemLogo.width = "40px";
           imgCommentItemLogo.id = "comment-item-logo";
           pCommentNickname.textContent = c.profile__user__username;
           divModalCommentItems.appendChild(divCommentItem);
           divCommentInfo.textContent = c.text ;
           divCommentDate.textContent = c.date;

        });
        cartLinkAdd();
    });

}


let slider = document.getElementById('test-slider');
noUiSlider.create(slider, {
    start: [10, 90],
    connect: true,
    step: 1,
    orientation: 'horizontal', // 'horizontal' or 'vertical'
    range: {
        'min': 0,
        'max': 100
    },
});


function cartLinkAdd() {
    let linksAdd = document.getElementsByClassName("js-add-cart");
    for (let i = 0; i < linksAdd.length; i++) {
        linksAdd[i].addEventListener("click", () => {
            HTTP.Get("cart/add/" + linksAdd[i].getAttribute("value"), addToCart);
        })
    }

}

function addToCart(data) {
    //Добавить функцию которая выведет, что элемент успешно добавлен в корзину
    showCart(data);
}

document.querySelector('.btn-fitler-mobile').addEventListener('click', () => {
    document.querySelector('.filter').classList.toggle('filter-active');
});
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.materialboxed');
    var instances = M.Materialbox.init(elems);
});
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
});

document.querySelector('.cart-open').addEventListener('click', () => {
    HTTP.Get('cart/view/', showCart);
    document.querySelector('.user-cabinet').classList.toggle('disable');
});
document.querySelector('.cart-close').addEventListener('click', () => {
    document.querySelector('.user-cabinet').classList.toggle('disable');
    console.log("ЗАКРЫТО");
});

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
            HTTP.Get("cart/remove/" + item.id, removeCart)
        });
        document.querySelector('.user-cart-items').appendChild(divCartItems);
    });

    document.querySelector('.cart-total-cost-p').textContent ="Total price: " + data.Price + "$";


}

function removeCart(data) {
    showCart(data);

}