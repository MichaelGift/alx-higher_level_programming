'use strict';

$(() => {
    const BASE_URL = 'https://swapi-api.alx-tools.com/api'

    $.get(`${BASE_URL}/people/5/?format=json`, (data, status) => {
        data.results.forEach(film => {
            $('UL#list_movies').append(`<li>${film.title}</li>`);
        });
    });
})