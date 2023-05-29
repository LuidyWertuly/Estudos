$(function(){

    $("#name").focus(function(){
        $("body").css("background-color","red");
    });
    $("#name").blur(function(){
        $("body").css("background-color","blue");
    });

    $("#send").hover(function(){
        $("#send").css("background-color","yellow")
    },
    function(){
        $("#send").css("background-color","white")
    });

});