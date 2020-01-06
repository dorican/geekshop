window.onload = function () {
    console.log('ПРИВЕТ');
    $(".cart_wrapper__container").on('change',
        'input[type="number"]',
        function (event) {
            // console.log(event.target);
            // console.log(event.target.name);
            // console.log(event.target.value);
            $.ajax({
                url: "/basket/update/" + event.target.name + "/" + event.target.value + "/",
                success: function(data) {
                $('.cart_wrapper__container').html(data.result);
                }
            });
    });
};


$(document).ready(function () {
    $('.btn-add-product-minus').click(function () {
        let $input = $(this).parent().find('input');
        let count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.btn-add-product-plus').click(function () {
        let $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });
});

