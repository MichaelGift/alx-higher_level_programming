'use strict';
$(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red') && !$('header').hasClass('green')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else if ($('header').hasClass('green') && !$('header').hasClass('red')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').addClass('red');
    }
  });
});
