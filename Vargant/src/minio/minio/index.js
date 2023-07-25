let role = document.querySelector('.role');
let tree = document.querySelector('.tree');
let game = document.querySelector('#game');
document.body.addEventListener('keydown', jump);
let otime = new Date();
let last_score = 0
let start_game=false;
function jump(event) {
    if (event.keyCode == 32) {
        if (role.classList != "animate") {
            role.classList.add("animate");
        }
        setTimeout(function () {
            role.classList.remove("animate");
        }, 500);
    }
}

document.addEventListener("DOMContentLoaded", function(){
    tree.style.animation = "none";
    start_game = false;
    document.querySelector("h3").innerText = "分數：" + last_score;
    update_score();

  });

$(document).ready(function ()
{
    $('#start_game').on('click', function ()
    {
        otime = new Date();
        start_game = true;
        document.querySelector("#start_game").style.display = "none";
    });

    $('#input_name').on('click', function ()
    {
        send_score();
        update_score();
    });

    $('#clear_board').on('click', function ()
    {
        clear_board();
        update_score();
    });

});


function clear_board(){
    let data = JSON.stringify({mode: 'clear'});
    
    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        url: 'http://192.168.56.3:5000/',
        data: data,
        dataType: 'json',
        error: function (data)
        {
            alert(data.responseJSON['msg']);
        }
    }).done();
}

function send_score(){
    let name = $('#user_name');
    let data = JSON.stringify({mode: 'insert', name: name.val(), score: last_score});

    $.ajax({
        type: 'POST',
        contentType: 'application/json; charset=utf-8',
        url: 'http://192.168.56.3:5000/',
        data: data,
        dataType: 'json',
        
        error: function (data)
        {
            alert(data.responseJSON['msg']);
        }
    }).done();
}

function update_score(){
    
    $.ajax({
        type: 'GET',
        url: 'http://192.168.56.3:5000/',
        dataType: 'json',
        success: function (data)
        {   
            let name = "";
            let len = 0;
            
            if(Object.keys(data.data).length <= 10){
                len = Object.keys(data.data).length;
            }else{
                len = 10;
            }
            for (var i=0; i < len; i++) {
                name += (i+1).toString().concat('. ', data.data[i][0], ' : ', data.data[i][1]);
                name += '<br>'
            }
            
            document.querySelector("#scoreBoard").innerHTML = name;
        },
        error: function () { alert('Failed to get comment list!'); }
    });
    
}

var check = setInterval(function () {
    if (start_game){
        
        game_main();
    }
}, 10)

function game_main(){
    let ntime = new Date();
    let score = Math.ceil((ntime - otime)/10);
    tree.style.animation = "stop 1s infinite";
    
    if (score >= 5000) {
        tree.style.animation = "none";
        role.style.animation = "none";
        document.querySelector("h2").style.display = "block";
        document.querySelector("#resume").style.display = "block";
        last_score = score
        document.body.removeEventListener('keydown', jump);
        clearInterval(check);
    }
    document.querySelector("h3").innerText = "分數：" + score;
    
    let blockButtom = parseInt(window.getComputedStyle(role)
        .getPropertyValue("bottom"));
    let stopRight = parseInt(window.getComputedStyle(tree)
        .getPropertyValue("right"));
    if (stopRight > 570 && stopRight < 590 && blockButtom < 25) {
        tree.style.animation = "none";
        role.style.animation = "none";
        document.querySelector("p").style.display = "block";
        document.querySelector("#resume").style.display = "block";
        last_score = score
        document.body.removeEventListener('keydown', jump);
        clearInterval(check);
    }
}