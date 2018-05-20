(function ($) {

  "use strict";

    // PRE LOADER
    $(window).load(function(){
      $('.preloader').fadeOut(1000); // set duration in brackets
    });


    //Navigation Section
    $('.navbar-collapse a').on('click',function(){
      $(".navbar-collapse").collapse('hide');
    });


    // Owl Carousel
    $('.owl-one').owlCarousel({
      animateOut: 'fadeOut',
      items:1,
      loop:true,
      autoplay:true,
    });
    $('.owl-two').owlCarousel({
      items: 4,
      loop: true,
      responsive: {
        0:{
          items: 1
        },
        600:{
          items: 2
        },
        960:{
          items: 4
        },
        1200:{
          items: 4
        }
      }
    })


    // PARALLAX EFFECT
    $.stellar();


    // SMOOTHSCROLL
    $(function() {
      $('.navbar-default a, #home a, footer a').on('click', function(event) {
        var $anchor = $(this);
          $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top - 49
          }, 1000);
            event.preventDefault();
      });
    });


    // WOW ANIMATION
    new WOW({ mobile: false }).init();

})(jQuery);
