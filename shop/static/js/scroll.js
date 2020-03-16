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



document.querySelector('.btn-fitler-mobile').addEventListener('click',()=>{
document.querySelector('.filter').classList.toggle('filter-active');
})