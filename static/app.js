$(document).ready(function(){
    $("nav").on("click", "#nav_button", function(){
        console.log('yas')
        $("nav ul").slideToggle("slow")
    });
    
});

$(document).ready(function(){
    $("#techincal").addClass("active_panel")
    $("#technicalpanel").show()
    $(".accordion").click(function(){
        var section = $(this).attr('id')
        var icons = $(this).find(".accordion_icon")
        $(this).toggleClass("active_panel")
        icons.children().toggle()
        $("#" + section + "panel").slideToggle();
    });   
});

$(document).ready(function(){
    $("#_container").css("color", "#181b1e");
    $("#_container").find(".hidebutton").show()
    $("section.side_tab").on("click", "li", function() {
        $(this).siblings().css("color", "white").find(".hidebutton").hide()
        $(this).css("color", "#181b1e").find(".hidebutton").show()
        $("section.projects_container").hide()
        var filter = $(this).attr('id')
        $(".projects" + filter).show()      
    });
    
});

$(document).ready(function(){
    var path = $(location).attr('href');
    var page = path.split('/').reverse()[0];
    console.log(page)
    if(page === "") {
        $("#home").addClass("active")
    } else {
        $("#" + page).addClass("active")   
    }
});

$(document).ready(function(){
    $(".tab_links").on("click", "button", function() {
        var get_id = $(this).attr('id')
        var get_content = "." + get_id + "_content"
        $(this).removeClass("inactive_tab").addClass("active_tab")
        $(this).siblings().removeClass("active_tab").addClass("inactive_tab")
        $(get_content).show()
        $(get_content).siblings().hide()
    });
});