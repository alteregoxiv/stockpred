window.onload = function(){

    today = new Date().toLocaleDateString().split('/');
    document.getElementById('day').value = today[2] + "-" + today[1] + "-" + today[0];

}
