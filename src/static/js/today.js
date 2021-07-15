window.onload = function(){

    today = new Date().toLocaleDateString().split('/');
    document.getElementById('day').value = today[2] + "-" + today[1] + "-" + today[0];

}

function predict(pdate){

    const val = document.getElementById('day').value;
    
    if(val < "2019-02-01"){

        alert("Please choose a date >= 2019-02-01");

    }

    fetch("/date?q=" + val)
    .then(function(res){

        return res.json();

    })
    .then(function(res){

        console.log(res);

    }).catch(console.log);

}
