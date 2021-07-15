window.onload = function(){

    today = new Date().toLocaleDateString().split('/');
    document.getElementById('day').value = today[2] + "-" + today[1] + "-" + today[0];

}

function predict(pdate){
    
    document.getElementById("loader").classList.add('loader');
    document.getElementsByClassName('main')[0].classList.add('slide');
    document.getElementsByClassName('result')[0].classList.add('slide');

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
        document.getElementById("loader").classList.remove('loader');
        document.getElementsByClassName("output")[0].classList.remove('hide');

    }).catch(console.log);

}

function back(){

    document.getElementsByClassName("main")[0].classList.remove('slide');
    document.getElementsByClassName("result")[0].classList.remove('slide');
    document.getElementsByClassName("output")[0].classList.add('hide');

}
