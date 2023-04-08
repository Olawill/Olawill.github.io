document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#size-select').onchange = () => {
      var select = document.querySelector('#size-select');

      for (var i = 0; i < select.options.length; i++) {
        select.options[i].removeAttribute('selected');
      }
      // Now add selected attribute to the selected option
      if (select.options[select.options.selectedIndex].innerHTML === 'Select a size') {
        select.options[select.options.selectedIndex].removeAttribute('selected');
      } else {
        select.options[select.options.selectedIndex].setAttribute('selected', 'selected');
      }
    }
  });