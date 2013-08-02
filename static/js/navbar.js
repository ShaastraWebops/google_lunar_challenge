// On load
$(window).bind('load', function() {
    $(window).resize(onResize);
    initNavigation();
    onResize();
    moon_init();
    link_moon_clicks();
    start_clock();
});

// Marquee fade function
function marquee_play(){
	var start_x = 0, end_x = $(window).width() - $("#marquee").width();
	$("#marquee").animate( {
		left: start_x + (end_x-start_x)*0.1, // fade in
		opacity: 1
	}, 10000, function() {
		$("#marquee").animate( {
			left: start_x + (end_x-start_x)*0.9 // move
		}, 10000, function() {
			$("#marquee").animate( {
				left: end_x, // fade out at end
				opacity: 0
			}, 10000, function() {
				
			});
		});
	});
}

function onResize() {
    // Need to get current element and click the menu element
    pos($('.current-menu-item'), 0);
    cur_elems = $('.in')
    cur_elem_id = $('.in').get()[0].id
    cur_elem_menu_id = "#" + cur_elem_id.substr(0, cur_elem_id.length - "_content".length) + "_menu"
    $(cur_elem_menu_id).click()
    reset_moon();
    clock_reset();
}

function pos(e, s) {
    $('.cursor-bottom, .cursor,.cursor-top').show();
    if(e.length > 0) {
        var off = e.offset().left;
        var w = e.width();
        TweenLite.to($('.cursor-bottom'), s, {
            css:{
                width:w,
                left:off
            }
        });
        TweenLite.to($('.cursor-top'), s, {
            css:{
                width:w,
                left:off
            }
        });
        TweenLite.to($('.cursor'), s, {
            css:{
                left:off+(w/2)-7
            }
        });

    } else {
        $('.cursor-bottom, .cursor').hide();
    }
}

function initNavigation() {
    $('.menu-item a').click(function(e) {
        pos($(this).parent(), 0.8);
        return true//$(this).pushLink(e);
    });

    pos($('.current-menu-item'), 0);
    

}

function setNavigationActive($e) {
    $('.menu-item').removeClass('current-menu-item').removeClass('current_page_item'),
    $e.addClass('current-menu-item current_page_item');
    pos($('.current-menu-item'), 0.8);
}

// Define label size from inside
function setLabelSizes() {
	$('.label').each(function() {
		var $t = $(this), dim = $t.find('span').getHiddenDimensions(), m = 18;
		$t.width(dim.innerWidth+m);
	});
}

function show_page(elem_menu_id) {
    // Hide everything
    current_content = $(".in").first()
    if (elem_menu_id == "moon" || elem_menu_id == "home_menu" || elem_menu_id == "home")
        elem_content = $("#container_moon")
    else {
        elem_content_id = "#" + elem_menu_id.substr(0, elem_menu_id.length - "_menu".length) + "_content"
        elem_content = $(elem_content_id)
    }
    
    if (elem_content.hasClass("slide-left") ) {
        current_content.removeClass("slide-left")
        current_content.addClass("slide-right")
    }
    else {
        current_content.removeClass("slide-right")
        current_content.addClass("slide-left")
        elem_content.addClass("slide-right")
    }
    $("#container_moon").removeClass("in")
    $("#container_moon").addClass("out")
    $(".container_page").removeClass("in")
    $(".container_page").addClass("out")
    
    // Show whats required
    if (elem_menu_id == "moon" || elem_menu_id == "home_menu" || elem_menu_id == "home") {
        //$("#container_moon").removeClass("hide");
        reset_moon();
        //if ( orbits.length > 0 )    orbits[orbits.length - 1].start();
        //if ( orbits.length > 1 )    orbits[orbits.length - 2].start();
        $("#container_moon").addClass("in");
        $("#container_moon").removeClass("out");
        //$("#container_moon").removeClass("hide")
        $("#container_moon").css('z-index', 91);
		$(".container_page").css('z-index', 90);
        
		marquee_play();
		
		$(".home_login_div").css({'display':''});
		$(".clock_wrapper").css({'display':''});
    } else {
        //elem_content_id = elem_menu_id.substr(0, elem_menu_id.length - "_menu".length) + "_content"
        //$("#" + elem_content_id).removeClass("hide")
        elem_content.top = $("#event_format_content").top
        elem_content.removeClass("out");
        elem_content.addClass("in")
        $(elem_content_id + ' .scroll-pane').jScrollPane({
            showArrows: true,
            verticalGutter: 30
        });
    
        //setTimeout("$('#container_moon').addClass('hide')", 500)
        //if ( orbits.length > 0 )    orbits[orbits.length - 1].stop();
        //if ( orbits.length > 1 )    orbits[orbits.length - 2].stop();
        
        $("#container_moon").css('z-index', 90);
        elem_content.css('z-index', 91);
        if (elem_menu_id == "intro_menu") {
			resize_intro_links();
		}
		$(".home_login_div").css({'display':'none'});
		$(".clock_wrapper").css({'display':'none'});
	}
}

function resize_intro_links() {
/*
 * 	// Reset the pics
	var temp_elem = $("#" + elem_content.get(0).id + " div.jspContainer"),
				w = 0, h = 0, t = 0, l = 0;
	h = temp_elem.height();// - $("#" + elem_content.get(0).id + " div.row-fluid").eq(0).height();
	w = temp_elem.width();
	t = 0;
	l = 0;
		
	if (h > w) {
		t = (h - w) / 2;
		l = 0;
		h = w;
	} else { // h < w
		t = 0;
		l = (w - h) / 2;
		w = h;
	}
	$("#" + elem_content.get(0).id + " #image_links").css( { 
		'width' : w + 'px', 
		'height' : h + 'px',
		//'top' : t + 'px',
		//'left' : l + 'px' 
	} );
	//console.log("did " + w + " " + h) ;
*/}
