  var loc = window.location.pathname;
   $('#navbarNav').find('a').each(function() {
     $(this).toggleClass('active', $(this).attr('href') == loc);
  });