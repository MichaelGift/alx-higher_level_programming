'use strict';

$(() => {
    const BASE_URL = 'https://hellosalut.stefanbohacek.dev/?'

    $.get(`${BASE_URL}/lang=fr`, (data, status) => {
        $('DIV#hello').html(data.hello);
    });
});