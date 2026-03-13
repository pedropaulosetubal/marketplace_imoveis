document.addEventListener('DOMContentLoaded', function () {
  var thumbs = document.querySelectorAll('.property-thumbs img');
  var main = document.querySelector('.property-main-image');
  if (main && thumbs.length) {
    thumbs.forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        main.src = this.src;
      });
    });
  }
});
