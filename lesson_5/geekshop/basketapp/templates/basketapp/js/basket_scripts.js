window.onload = function () {
    $('.basket_record').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        console.log('adasdasdsa')
        console.log( t_href.name)
        console.log( t_href.value)

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.basket_record').html(data.result);
            },
        });

        event.preventDefault();
    });
}
//document.querySelector('.basket_record').addEventListener('click', function (event) {
// var t_href = event.target;
// console.log('adasdasdsa')
// console.log( t_href.name)
// console.log( t_href.value)
// $.ajax({
//            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
//
//            success: function (data) {
//                $('.basket_record').html(data.result);
//            },
//        });
// event.preventDefault();
//})