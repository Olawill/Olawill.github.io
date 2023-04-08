document.addEventListener('DOMContentLoaded', function() {
    const res_value = document.querySelector('.a-price-whole').innerHTML;
    const selectElement = document.querySelector('#size-select');
    selectElement.addEventListener('change', (event) => {
       const result = document.querySelector('.a-price-whole');
      //  const input_size = document.querySelector('#input-size');
       if (event.target.value === 'Select a size') {
        result.textContent = res_value;
        document.querySelector('#submit').style.display = 'none';
       } else {
        result.textContent = event.target.value;
        document.querySelector('#submit').style.display = 'inline-block';
        // input_size.value = event.value;
       }
    });

  });