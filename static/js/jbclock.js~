
var clock_center = 90, clock_width = 17, clock_radius = 70;
function JBCountDown(settings) {
    var glob = settings;
   
    function deg(deg) {
        return (Math.PI/180)*deg - (Math.PI/180)*90
    }
    
    glob.total   = Math.floor((glob.endDate - glob.startDate)/86400);
    glob.days    = Math.floor((glob.endDate - glob.now ) / 86400);
    glob.hours   = 24 - Math.floor(((glob.endDate - glob.now) % 86400) / 3600);
    glob.minutes = 60 - Math.floor((((glob.endDate - glob.now) % 86400) % 3600) / 60);
    glob.seconds = 60 - Math.floor((glob.endDate - glob.now) % 86400 % 3600 % 60);
    
    if (glob.now >= glob.endDate) {
        return;
    }
    
    var clock = {
        set: {
            days: function(){
                var cdays = $("#canvas_days").get(0);
                var ctx = cdays.getContext("2d");
                ctx.clearRect(0, 0, cdays.width, cdays.height);
                ctx.beginPath();
                ctx.strokeStyle = glob.daysColor;
                
                ctx.shadowBlur    = 10;
                ctx.shadowOffsetX = 0;
                ctx.shadowOffsetY = 0;
                ctx.shadowColor = glob.daysGlow;
                
                ctx.arc(clock_center,clock_center,clock_radius, deg(2*Math.PI-0), deg(2*Math.PI- ((360/glob.total)*(glob.total - glob.days))));
                ctx.lineWidth = clock_width;
                ctx.stroke();
                $(".clock_days .val").text(glob.days);
            },
            
            hours: function(){
                var cHr = $("#canvas_hours").get(0);
                var ctx = cHr.getContext("2d");
                ctx.clearRect(0, 0, cHr.width, cHr.height);
                ctx.beginPath();
                ctx.strokeStyle = glob.hoursColor;
                
                ctx.shadowBlur    = 10;
                ctx.shadowOffsetX = 0;
                ctx.shadowOffsetY = 0;
                ctx.shadowColor = glob.hoursGlow;
                
                ctx.arc(clock_center,clock_center,clock_radius, deg(2*Math.PI-0), deg(2*Math.PI-15*glob.hours));
                ctx.lineWidth = clock_width;
                ctx.stroke();
                $(".clock_hours .val").text(24 - glob.hours);
            },
            
            minutes : function(){
                var cMin = $("#canvas_minutes").get(0);
                var ctx = cMin.getContext("2d");
                ctx.clearRect(0, 0, cMin.width, cMin.height);
                ctx.beginPath();
                ctx.strokeStyle = glob.minutesColor;
                
                ctx.shadowBlur    = 10;
                ctx.shadowOffsetX = 0;
                ctx.shadowOffsetY = 0;
                ctx.shadowColor = glob.minutesGlow;
                
                ctx.arc(clock_center,clock_center,clock_radius, deg(2*Math.PI-0), deg(2*Math.PI-6*glob.minutes));
                ctx.lineWidth = clock_width;
                ctx.stroke();
                $(".clock_minutes .val").text(60 - glob.minutes);
            },
            seconds: function(){
            /*
                var cSec = $("#canvas_seconds").get(0);
                var ctx = cSec.getContext("2d");
                ctx.clearRect(0, 0, cSec.width, cSec.height);
                ctx.beginPath();
                ctx.strokeStyle = glob.secondsColor;
                
                ctx.shadowBlur    = 10;
                ctx.shadowOffsetX = 0;
                ctx.shadowOffsetY = 0;
                ctx.shadowColor = glob.secondsGlow;
                
                ctx.arc(clock_center,clock_center,clock_radius, deg(2*Math.PI-0), deg(2*Math.PI-6*glob.seconds));
                ctx.lineWidth = clock_width;
                ctx.stroke();
                $(".clock_seconds .val").text(60 - glob.seconds);
            */
            }
        },
       
        start: function(){
            /* Seconds */
            var cdown = setInterval(function(){
                if ( glob.seconds > 59 ) {
                    if (60 - glob.minutes == 0 && 24 - glob.hours == 0 && glob.days == 0) {
                        clearInterval(cdown);
                        
                        /* Countdown is complete */
                        
                        return;
                    }
                    glob.seconds = 1;
                    if (glob.minutes > 59) {
                        glob.minutes = 1;
                        clock.set.minutes();
                        if (glob.hours > 23) {
                            glob.hours = 1;
                            if (glob.days > 0) {
                                glob.days--;
                                clock.set.days();
                            }
                        } else {
                            glob.hours++;
                        }
                        clock.set.hours();
                    } else {
                        glob.minutes++;
                    }
                    clock.set.minutes();
                } else {
                    glob.seconds++;
                }
                clock.set.seconds();
            },1000);
        }
    }
    clock.set.seconds();
    clock.set.minutes();
    clock.set.hours();
    clock.set.days();
    clock.start();
}

function clock_reset(len_def) {
    var len_sq = 50;
    if (len_def) {
        len_sq = len_def;
    } else {
        len_sq = ($('body').height() / 2 / 4)
    }
    
    $(".clock_wrapper").height(4*len_sq).width(len_sq)
    
    $(".bgLayer canvas").height(len_sq).width(len_sq)
    
    $(".bgLayer .text .val").css( {
        'font-size' : (len_sq / 50) + 'em',
    });
    
    $(".bgLayer .text .type").css( {
        'font-size' : (len_sq / 100) + 'em',
    });
    
    $(".type_hours").css({
        'font-size' : (len_sq / 120) + 'em',
    });
    
    $(".type_minutes").css({
        'font-size' : (len_sq / 120) + 'em',
    });
        
    $(".clock_days .bgLayer .text").css( {
        'top' : ((len_sq - $(".bgLayer .text").height()) / 2) + 'px',
    });
    var temp_midx = 0;//( $(".clock").width() + $(".clock .text").width() ) / 2
    $(".clock_hours").css( {
        'left' : ( temp_midx - $(".clock_hours").width() + len_sq/2 ) + 'px',
    });
    
    //alert($(".clock_days").height())
    $(".clock_minutes").css( {
        'left' : ( temp_midx + $(".clock_minutes").width() - len_sq/4 ) + 'px',//( $(".clock_hours").offset().right ) + 'px',
        'top' : ( temp_midx - len_sq/1.8 ) + 'px',
    });
    
    $("#canvas_hours").css({
        'height' : ( ($(".clock_days").height()) / 2 ) + 'px',
        'width' : ( ($(".clock_days").width()) / 2 ) + 'px',
    });
    
    $("#canvas_minutes").css({
            'height' : ( ($(".clock_days").height()) / 2 ) + 'px',
        'width' : ( ($(".clock_days").width()) / 2 ) + 'px',
    });
    
    $(".clock_hours").find('div').css({
        'width' : '40px',
    });
    
    $(".clock_minutes").find('div').css({
        'width' : '40px',
    });
    
}

function start_clock() {
    startDate = $('#startDate_value').val();
    endDate = $('#endDate_value').val();
    now = $('#now_value').val();

    JBCountDown({
        secondsColor : "#ffdc50",
        secondsGlow  : "none",
        
        minutesColor : "#000000",//"#9cdb7d",
        minutesGlow  : "none",
        
        hoursColor   : "#000000",//"#378cff",
        hoursGlow    : "none",
        
        daysColor    : "#000000",//"#ff6565",
        daysGlow     : "none",
        
        startDate   : startDate,
        endDate     : endDate,
        now         : now
    });
    clock_reset();
}
