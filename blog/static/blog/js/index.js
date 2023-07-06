$(document).ready(function () {
  let nav = $("#nav");

  const appBarElement = document.getElementById("appbar-wrapper");
  const appBarHeight = appBarElement.offsetHeight;

  let scrollHandler = (function () {
    let previousScrollTop = $(this).scrollTop();
    let isHiding = false;

    return function () {
      let scrollTop = $(this).scrollTop();

      if (scrollTop > previousScrollTop && !isHiding) {
        nav.animate({ top: `-${appBarHeight}px` });
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
