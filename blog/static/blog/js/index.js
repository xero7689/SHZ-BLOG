$(document).ready(function () {
  let nav = $("#nav");

  let scrollHandler = (function () {
    let previousScrollTop = $(this).scrollTop();
    let isHiding = false;

    return function () {
      let scrollTop = $(this).scrollTop();

      if (scrollTop > previousScrollTop && !isHiding) {
        nav.animate({ top: "-100px" });
        isHiding = true;
      } else if (scrollTop <= previousScrollTop - 10 && isHiding) {
        nav.animate({ top: "0px" });
        isHiding = false;
      }

      previousScrollTop = scrollTop;
    };
  })();

  $(window).scroll(scrollHandler);
});
