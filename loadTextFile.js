window.onload = function() {
    var filePath = 'example.txt';

    var xhr = new XMLHttpRequest();
    xhr.open('GET', filePath, true);

    xhr.onload = function() {
        if (xhr.status === 200) {
            var textContent = xhr.responseText;
          
            document.getElementById('text-content').innerText = textContent;
        }
    };

    xhr.send();
};
