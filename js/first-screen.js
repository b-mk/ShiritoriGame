$(function () {
    $('.bxslider').bxSlider({
        slideWidth: window.innerWidth,
        infiniteLoop: false,
        startSlide: '0',
        hideControlOnEnd: false,
        nextSelector: '#feed_next_btn',
        prevSelector: '#feed_prev_btn',
    });
});

function getSelectedRadio(name) {
    var radios = document.getElementsByName(name);
    var result;
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            result = radios[i].value;
            break;
        }
    }
    return (result);
}

function transMainScreen() {
    var userName = document.forms.form_name.user_name.value;
    var modeNum = getSelectedRadio("mode_num");
    var myIconNum = getSelectedRadio("my_icon");

    query = '?name=' + encodeURIComponent(userName) + '&mode_num=' + encodeURIComponent(modeNum) + '&my_icon_num=' + encodeURIComponent(myIconNum)
    window.location.href = '../html/main-screen.html' + query
}