document.querySelector('#js-submit-form').addEventListener('click', () => {
        currentPage = 0;
        renderRequest();
    }
);

function renderRequest() {
    document.querySelector('.items-box').innerHTML = '<div class="progress" style="position: absolute; width: 60%;"><div class="indeterminate"></div></div>';
    let filters = document.getElementsByClassName('js-input-filter');
    const formRequest = {
        "Page": String(currentPage),
        "Discount": filters[0].checked,
        "New": filters[1].checked,
        "Brand": [],
        "Sizes": []
    };
    for (let i = 2; i < 6; i++)
        if (filters[i].checked) formRequest["Brand"].push(filters[i].value);

    for (let i = 6; i < filters.length; i++)
        if (filters[i].checked) formRequest["Sizes"].push(filters[i].value);
    console.log(formRequest);
    HTTP.Get('show/?' + toQueryString(formRequest), ShowItems).then(() => {
        let elements = document.querySelectorAll('.materialboxed');
        let instancesOne = M.Materialbox.init(elements);
        let elems = document.querySelectorAll('.modal');
        let instancesTwo = M.Modal.init(elems);
    });
    console.log(toQueryString(formRequest));


}

function toQueryString(obj) {
    const Brand = `Brand=${obj["Brand"].join('&Brand=')}`;
    const Size = `Sizes=${obj["Sizes"].join('&Sizes=')}`;
    return `&Page=${obj["Page"]}&Discount=${obj["Discount"]}&New=${obj["New"]}&${Brand}&${Size}`
}