document.getElementById('donation-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var amount = document.getElementById('amount').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/donate', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert('تم التبرع بنجاح!');
        }
    };
    xhr.send('name=' + name + '&email=' + email + '&amount=' + amount);
});
