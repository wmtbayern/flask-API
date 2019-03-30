$(function () {
    $.getJSON('/api/v1/banners/',
       function (a) {
        console.log(a)
        $.each(a,function (a) {
            console.log(data.data.img)
            $('<img/>').attr('src',item.img).appendTo('#banner #list li a');

        })
            //
            // console.log(data.img)
            // // $('#banner #list li a img').val(data.img)




        // $.get('/axf/addcart/', request_data, function (response) {
        //     console.log(response)

        }
    )
})

