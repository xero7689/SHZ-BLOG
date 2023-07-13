$(document).ready(function () {
  let nav = $("#nav");

  const appBarElement = document.getElementById("appbar-wrapper");
  const appBarHeight = appBarElement.offsetHeight;

  // AppBar Display Handler
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

  /*
   * Code Snippets Collapse Button
   */
  // Collapse Button Factory
  function createCollapseButton(preBlock) {
    let button = document.createElement("div");
    let icon = document.createElement("i");

    //
    icon.classList.add("fa-solid");
    icon.classList.add("fa-chevron-down");

    // button.textContent = "Expand..";
    button.classList.add("hljs-collapse-btn");
    button.appendChild(icon);

    button.onclick = () => {
      preBlock.classList.toggle("active");
      icon.classList.toggle("fa-chevron-down");
      icon.classList.toggle("fa-chevron-up");
    };

    return button;
  }

  const preBlocks = document.getElementsByTagName("pre");
  for (let i = 0; i < preBlocks.length; i++) {
    let preBlock = preBlocks[i];

    if (preBlock.querySelectorAll(".hljs")) {
      let preRect = preBlock.getBoundingClientRect();
      if (preRect.height < 256) {
        preBlock.classList.toggle("active");
        preBlock.classList.add("pre-not-overflow");
      } else {
        let collapseButton = createCollapseButton(preBlock);
        preBlock.after(collapseButton);
      }
    }
  }
});
