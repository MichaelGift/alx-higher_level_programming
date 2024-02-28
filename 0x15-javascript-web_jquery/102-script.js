'use strict';
$(() => {
    $('INPUT#btn_translate').click(() => {
        const BASE_URL = 'https://fourtonfish.com/hellosalut/?';
        const code = $('INPUT#language_code').val();

        $.get(`${BASE_URL}lang=${code}`,(data, status) => {
         $('DIV#hello').html(data.hello);
        });
    });
});