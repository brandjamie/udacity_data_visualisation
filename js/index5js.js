// Array of chart divs - initially only one. 
var divs_arr = ["#chartone","#charttwo"]


// Attitudes to select from along with question code and question number
var attitudes_arr = [
    ["ST86Q01","Students get along well with most teachers","Q39"],
    ["ST86Q02","Most teachers are interested in students well-being","Q39"],
    ["ST86Q03","Most of my teachers really listed to what I have to say.","Q39"],
    ["ST86Q04","If I need extra help, I will receive it from my teachers.","Q39"],
    ["ST86Q05","Most of my teachers treat me fairly.","Q39"],
    ["ST87Q01","I feel like an outsider (or left out of things) at school.","Q40"],
    ["ST87Q02","I make friends easily at school","Q40"],
    ["ST87Q03","I feel like I belong at school.","Q40"],
    ["ST87Q04","I feel awkward and out of place in my school.","Q40"],
    ["ST87Q05","Other students seem to like me","Q40"],
    ["ST87Q06","I feel lonely at school.","Q40"],
    ["ST87Q07","I feel happy at school.","Q40"],
    ["ST87Q08","Things are ideal in my school.","Q40"],
    ["ST87Q09","I am satisfied with my school.","Q40"],
    ["ST88Q01","School has done little to prepare me for adult life when I leave school.","Q41"],
    ["ST88Q02","School has been a waste of time.","Q41"],
    ["ST88Q03","School has helped give me confidence to make decisions.","Q41"],
    ["ST88Q04","School has taught me things which could be useful in a job.","Q41"],
    ["ST89Q02","Trying had at school will help me get a good job.","Q42"],
    ["ST89Q03","Trying hard at school will help me get into a good college.","Q42"],
    ["ST89Q04","I enjoy receiving good grades.","Q42"],
    ["ST89Q05","Trying hard at school is important.","Q42"],
    ["ST91Q01","If I put in enough effort I can succeed in school.","Q43"],
    ["ST91Q02","It is completely my choice whether or not I do well at school.","Q43"],
    ["ST91Q03","Family demands or other problems prevent me from putting a lot of time into my school work.","Q43"],
    ["ST91Q04","If I had different teachers I would try harder at school.","Q43"],
    ["ST91Q05","If I wanted to I could do well in school.","Q43"],
    ["ST91Q06","I do badly in school whether or not I study for my exams.","Q43"]
    ]

// Options for attitudes
var attitudes_domain = ["Strongly Agree","Agree","Disagree","Strongly Disagree"]

// Possible questions from the school survey
var school_arr = [
    ["SC14Q01","A lack of qualified science teachers"],
    ["SC14Q02","A lack of qualified mathematics teachers"],
    ["SC14Q03","A lack of qualified English teachers"],
    ["SC14Q04","A lack of qualified teachers of other subjects"],
    ["SC14Q05","Shortage or inadequacy of science laboratory equipment"],
    ["SC14Q06","Shortage or inadequacy of instructional materials (e.g., textbooks)"],
    ["SC14Q07","Shortage or inadequacy of computers for instruction"],
    ["SC14Q08","Lack or inadequacy of Internet connectivity"],
    ["SC14Q09","Shortage or inadequacy of computer software for instruction"],
    ]
// Options for the school survey questions. 
var school_domain = ["Not at all","Very Little","To some extent","A lot"]
// Array of boolean values dictating whether to include schools with each response. 
var school_domain_bools = [[],[]];

// color used in charts
var color = d3.scale.category10();

// string for adding toggles dynamically
var toggle_html_string = '<label class="switch"><input id="'

var toggle_html_string_two = '" type="checkbox" class="switch\-input" checked><span class="switch-label" data-on="On" data-off="Off"><\/span><span class="switch-handle"><\/span><\/label>'


// set inintial parameters - all as arrays to accomodate for more than one chart
var subject_var = ["ave","ave"]

var attitude_var = ["ST88Q02","ST88Q02"]
var school_score_toggle = [false,false];
var school_question_toggle = [false,false];
var school_var = [school_arr[0][0],school_arr[0][0]];
var school_score_min = [0,0];
var school_score_max = [720,720];
var num_of_students = [];
var num_of_schools = [];
// global variables to be set later.
var ukschools;
var chartdata = [];

//arrays containing the charts
var svgs = [];
var xAxiss = [];
var yAxiss = [];
var legends = [];

//chart dimensions
var   margin = {top: 60, right: 20, bottom: 35, left: 60};
var    width = 500 - margin.left - margin.right;
var    height = 450 - margin.top - margin.bottom;

// returns the string for the attitude question
function getAttitudeString (num) {
    for (i = 0; i<attitudes_arr.length; i++) {
	if (attitudes_arr[i][0]==attitude_var[num]) {
	    return attitudes_arr[i][1]
	} 

    }

}

function getSchoolString (num) {
    for (i = 0; i<school_arr.length; i++) {
	if (school_arr[i][0]==school_var[num]) {
	    return school_arr[i][1]
	} 

    }
}

// load data
d3.csv("uk_studentsThree.csv",function(error, data) {
    if (error) throw error;
     ukschools = data;
     drawChart();
 });



// add options to attitude dropdown
var attitude_el = document.getElementById("attitude");
var attitude_elb = document.getElementById("attitudeb");

for (i = 0; i < attitudes_arr.length;i++) {
	var option = document.createElement("option");
	option.setAttribute("value", attitudes_arr[i][0]);
	option.text = attitudes_arr[i][1];
    attitude_el.appendChild(option.cloneNode(true));
    	attitude_elb.appendChild(option);

    }


// add options to school questions dropdown 
var school_el = document.getElementById("school");
var school_elb = document.getElementById("schoolb");

    for (i = 0; i < school_arr.length;i++) {
	var option = document.createElement("option");
	option.setAttribute("value", school_arr[i][0]);
	option.text = school_arr[i][1];
	school_el.appendChild(option.cloneNode(true));
	school_elb.appendChild(option);
    }

// update chart on change in attitude dropdown
d3.select('#attitude')
    .property( "value", attitude_var[0] )   
    .on('change', function() {
	attitude_var[0] = d3.select(this).property('value');
	updateChart(0);
    });
d3.select('#attitudeb')
    .property( "value", attitude_var[1] )   
    .on('change', function() {
	attitude_var[1] = d3.select(this).property('value');
	updateChart(1);
    });


// update chart on change in school question dropdown
d3.select('#school')
    .property( "value", school_var[0] )   
    .on('change', function() {
	school_var[0] = d3.select(this).property('value');
	updateChart(0);
    });

d3.select('#schoolb')
    .property( "value", school_var[1] )   
    .on('change', function() {
	school_var[1] = d3.select(this).property('value');
	updateChart(1);
    });


// update chart on change in score toggle
d3.select('#score_toggle')
    .on('change', function() {
	school_score_toggle[0] = d3.select(this).property('checked');
	updateChart(0);
    });

d3.select('#score_toggleb')
    .on('change', function() {
	school_score_toggle[1] = d3.select(this).property('checked');
	updateChart(1);
    });


// update chart on change in question toggle
d3.select('#question_toggle')
    .on('change', function() {
	school_question_toggle[0] = d3.select(this).property('checked');
	updateChart(0);
    });

d3.select('#question_toggleb')
    .on('change', function() {
	school_question_toggle[1] = d3.select(this).property('checked');
	updateChart(1);
    });


// update chart on change in subject dropdown. 
d3.select('#subject')
    .property( "value", subject_var[0] ) 
    .on('change', function() {
	subject_var[0] = d3.select(this).property('value');
	updateChart(0);
    });

d3.select('#subjectb')
    .property( "value", subject_var[1] ) 
    .on('change', function() {
	subject_var[1] = d3.select(this).property('value');
	updateChart(1);
    });



function slider_one_mouse_up (value) {
    value = value.split(";")
    school_score_min[0] = parseInt(value[0]);
    school_score_max[0] = parseInt(value[1]);
    	updateChart(0);
}

function slider_two_mouse_up (value) {
    value = value.split(";")
    school_score_min[1] = parseInt(value[0]);
    school_score_max[1] = parseInt(value[1]);
    	updateChart(1);
}


function drawChart() {
   
    ukschools.forEach(function(d) {
    	d.maths = Math.floor(+d.maths);
    	d.scie = Math.floor(+d.scie);
    	d.read = Math.floor(+d.read);
    	d.ave = Math.floor(+d.read);
    	d.schoolmaths = Math.floor(+d.maths);
    	d.schoolscie = Math.floor(+d.scie);
    	d.schoolread = Math.floor(+d.read);
   	d.schoolave = Math.floor(+d.read);
    	d.SCHOOLID = +d.SCHOOLID;
    	for (i = 0; i < attitudes_arr.length; i++){
    	    thisstring = "d."+attitudes_arr[i][0]+";"
    	    thisdatum = eval(thisstring);
    	    thisdatum = Math.floor(+thisdatum);
    	}
    	for (i = 0; i < school_arr.length; i++){
    	    thisstring = "d."+school_arr[i][0]+";"
    	    thisdatum = eval(thisstring);
    	    thisdatum = Math.floor(+thisdatum);
    	}

    });
    chartdata[0] = makeChartData(0)
    chartdata[1] = makeChartData(1)
  
    makeChart(0)
    makeChart(1)
    $( "#second_chart" ).hide();
}

function makeChartData(num) {
 
    
    thisdata = {"sagreetotal":0,"sagreenum":0,
		"agreetotal":0,"agreenum":0,
		"dagreetotal":0,"dagreenum":0,
		"sdagreetotal":0,"sdagreenum":0}

 
    // cache of results for checkSchool 
    schools_filter = []
    
    
    function checkSchool (this_school_var,this_school_id,this_school_score) {
	// check cache
	if (schools_filter[this_school_id] == true || schools_filter[this_school_id] == false) {
	    school_bool = schools_filter[this_school_id];

	} else {	
	    school_bool = checkScore(this_school_score)
	    if (school_question_toggle[num] == true && school_bool == true) {
		school_bool = school_domain_bools[num][this_school_var]
	    }
	    schools_filter[this_school_id] = school_bool
	}
	return school_bool;
    }

    function checkScore (this_score_value) {
	score_bool = true;
	if (school_score_toggle[num] == true) {
	    if (this_score_value < school_score_min[num] || this_score_value > school_score_max[num]) {
		score_bool = false;
	    }
	}
	return score_bool;
    }
    num_of_students[num] = 0;

    for (i = 0; i<ukschools.length;i++) {
	this_attitude = ukschools[i][attitude_var[num]]
	this_score_value = ukschools[i][subject_var[num]]
	this_school_score = ukschools[i]["school"+subject_var[num]]
	this_school_var = ukschools[i][school_var[num]]-1
	this_school_id = ukschools[i]["SCHOOLID"]
	this_school = checkSchool(this_school_var,this_school_id,this_school_score)
	
	if (this_attitude == "Strongly agree" && this_school) {
	    thisdata["sagreetotal"] = thisdata["sagreetotal"] + this_score_value;
	    thisdata["sagreenum"] = thisdata["sagreenum"] + 1;
	    num_of_students[num] = num_of_students[num]+1
	}
	else if (this_attitude == "Agree" && this_school) {
	    thisdata["agreetotal"] = thisdata["agreetotal"] + this_score_value;
	    thisdata["agreenum"] = thisdata["agreenum"] + 1;
	    num_of_students[num] = num_of_students[num]+1
	}
	else if (this_attitude == "Disagree" && this_school) {
	    thisdata["dagreetotal"] = thisdata["dagreetotal"] + this_score_value;
	    thisdata["dagreenum"] = thisdata["dagreenum"] + 1;
	    num_of_students[num] = num_of_students[num]+1
	}
	else if (this_attitude == "Strongly disagree" && this_school) {
	    thisdata["sdagreetotal"] = thisdata["sdagreetotal"] + this_score_value;
	    thisdata["sdagreenum"] = thisdata["sdagreenum"] + 1;
	    num_of_students[num] = num_of_students[num]+1
	}   


    }
    thischartdata = getPercentAndScores(thisdata)
    num_of_schools[num] = 0;

    for (i=0; i<schools_filter.length; i++) {
	if (schools_filter[i] == true) {
	    num_of_schools[num] = num_of_schools[num]+1;

	}
    }
  
 

  
    
    return thischartdata
}

// get perecentages and scores from results dictionary 
function getPercentAndScores(data) {
    
    totalnum = data["sagreenum"]+data["agreenum"]+data["dagreenum"]+data["sdagreenum"]
    if (totalnum > 0) {
	sapercent = (data["sagreenum"]/totalnum)*100;
	apercent = (data["agreenum"]/totalnum)*100;
	dpercent = (data["dagreenum"]/totalnum)*100;
	sdpercent = (data["sdagreenum"]/totalnum)*100;
    } else {
	sapercent = 0;
	apercent = 0;
	dpercent = 0;
	sdpercent = 0;
    }	

    
    saave = 0;
    aave = 0;
    dave = 0;
    sdave = 0;
    if (data["sagreenum"]>0) {
	
	saave = (data["sagreetotal"]/data["sagreenum"])
    } 
    if (data["agreenum"]>0) {
	aave = (data["agreetotal"]/data["agreenum"])
    }
    if (data["dagreenum"]>0) {
	dave = (data["dagreetotal"]/data["dagreenum"])
    }
    if (data["sdagreenum"]>0) {
        sdave = (data["sdagreetotal"]/data["sdagreenum"])
    }
   
    
    thisPercentAndScores = [{startpercent:0,percent:sapercent,score:saave},
			    {startpercent:sapercent,percent:apercent+sapercent,score:aave},
			    {startpercent:apercent+sapercent,percent:apercent+sapercent+dpercent,score:dave},
			    {startpercent:dpercent+apercent+sapercent,percent:100,score:sdave}]
    
    return thisPercentAndScores;

    

    

}
function sizeText (id,maxwidth) {
    thistext = d3.select(id).node()
    if (thistext.getComputedTextLength() > maxwidth) {
	curr_fontsize = thistext.style.fontSize;
	curr_fontsize = curr_fontsize.split("p");
	curr_fontsize = parseInt(curr_fontsize[0]);
	new_fontsize =  curr_fontsize - 1;
	if (new_fontsize > 17) {
 	thistext.style.fontWeight = "bold";
	}

	
	new_fontsize = new_fontsize + "px";
 	thistext.style.fontSize = new_fontsize;
	sizeText (id,maxwidth)
    }
}

function toggleSecondChart() {
  if ( $( "#second_chart" ).is( ":hidden" ) ) {
      $( "#second_chart" ).slideDown( "slow" );
      $("#toggleSecondChart").html("Hide Second Chart");
  } else {
         $( "#second_chart" ).slideUp( "slow" );
      $("#toggleSecondChart").html("Add a chart for comparison");

//    $( "#second_chart" ).hide();
  }

}


 function getTicks (datanum) {
	return 10;
    }

function getXText (datanum) {
    return "Percentage of answers";
}

function getYText () {
    if (subject_var == "maths") {
	return "Average score in Maths";
    }
    else if (subject_var == "read") {
	return "Average score in Reading";
        }
    else if (subject_var == "scie") {
	return "Average score in Science";
    }
    else {
	return "Average score in Maths, Reading and Science";
        }
}


  function getTitleText(chartnum) {

      title_string = num_of_students[chartnum] + " Students from " + num_of_schools[chartnum] + " schools."
      return title_string
    }





function getSubtitleTooltipText(datanum) {
    text = ""
    if (school_score_toggle[datanum] == false && school_question_toggle[datanum] == false) {
	text = "All schools are included";
    }
    else if (school_score_toggle[datanum] == false) {
	text = "Including schools which answered the question: <br><br>";
	text = text + "<div class='question'>"
	text = text +  "Is your school's capacity to provide instuction hindered by any of the following issues?"
	text = text + "<br>"   + getSchoolString(datanum) + "</div>";
	text = text + "With the answers:" 
	text = text + "<div  class='answers'>"
	for (i = 0; i<school_domain.length; i++) {
	    if (school_domain_bools[datanum][i] == true) {
		text = text+school_domain[i] + "<br>"
	    }
	}
	text = text + "</div>";
    }
    else if (school_question_toggle[datanum] == false) {
	text = "Including Schools with an average score of more than ";
	text = text + school_score_min[datanum];
	text = text + " and less than " + school_score_max[datanum] + ".";
    } else {
	text = "Including Schools with an average score of more than ";
	text = text + school_score_min[datanum];
	text = text + " and less than " + school_score_max[datanum];
	text = text + " and which answered the question: <br><br>";
	text = text + "<div class='question'>"
	text = text +  "Is your school's capacity to provide instuction hindered by any of the following issues?"
	text = text + "<br>"   + getSchoolString(datanum) + "</div>";
	text = text + "With the answers:" 
	text = text + "<div  class='answers'>"
	for (i = 0; i<school_domain.length; i++) {
	    if (school_domain_bools[datanum][i] == true) {
		text = text+school_domain[i] + "<br>"
	    }
	}
	text = text + "</div>";
    }
   return text;
}






function makeChart(datanum) { 

   
    
    x = d3.scale.linear()
    .range([0, width]);

    y = d3.scale.linear()
    .range([height,0]);

   
    x.domain([0,100]);
    y.domain([200,700]);

 
    var svg = d3.select(divs_arr[datanum]).append("svg")
    	.attr("width", width + margin.left + margin.right)
    	.attr("height", height + margin.top + margin.bottom)
    	.append("g")
    	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

 
    var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
	.ticks(getTicks(datanum));
     
    svg.append("g")
    	.attr("class", "x axis")
    	.attr("transform", "translate(0," + height + ")")
    	.call(xAxis)
    	.append("text")
    	.attr("class", "x_label")
    	.attr("x", width)
    	.attr("y", 30)
    	.style("text-anchor", "end")
    	.text(getXText(datanum));


    
    var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");
		
    svg.append("g")
	.attr("class", "y axis")
	.call(yAxis)
	.append("text")
	.attr("class", "y_label")
	.attr("transform", "rotate(-90)")
	.attr("y", -50)
	.attr("dy", ".71em")
	.style("text-anchor", "end")
	.text(getYText());

   

    svg.selectAll(".bar")
    	.data(chartdata[datanum])
    	.enter()
    	.append("rect")
    	.attr("class","bar")
    	.attr("x",function(d,i) {return x(d.startpercent);})
    	.attr("y",function(d) {return height-(height-y(d.score))})
    	.attr("width",function(d) {return x(d.percent-d.startpercent);})
    	.attr("height",function(d,i){
    	    return height - y(d.score);})
    	.style("fill", function(d,i) {
		return color(i)
	})
	.on('mouseover', function(d, i) {
	    tooltip.select('.label').html(attitudes_domain[i] + "<br><br>");
	    tooltip.select('.score').html("Average score: " + Math.round(d.score));
	    this_percent = Math.round(d.percent-d.startpercent)
	    this_num_of_students = Math.round((num_of_students[datanum]/100)*this_percent);
	    
	    tooltip.select('.percent').html( this_percent + " percent (" + this_num_of_students + " students)");
	    
	    tooltip.style('display','block');
	})
	.on('mouseout', function(d) {
	    tooltip.style('display','none');
	});
    

    svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top/2))
	.attr("id","main_title")
    	.attr("text-anchor", "middle")  
        .style("font-size","20px")
     	.style("fontWeight", "")
        .text(getAttitudeString(datanum));

    sizeText("#main_title",width)
    
    svg.append("text")
        .attr("x", (width / 2))             
        .attr("y", 0 - (margin.top/5))
	.attr("class","title")
    	.attr("text-anchor", "middle")  
        .style("text-decoration", "underline")
	.on('mouseover', function(d, i) {
	    titletooltip.select('.label').html(getSubtitleTooltipText(datanum));
	    titletooltip.style('display','block');
	})
	.on('mouseout', function(d) {
	    titletooltip.style('display','none');
	})
        .text(getTitleText(datanum));




    
    // if (datanum != 0 && datanum != 1) {
    
    // svg.append("rect")
    // 	.attr("x",(width - 20))
    // 	.attr("y", 0 - (margin.top - 10))
    // 	.attr("class","school_legend")
    //     .attr("width", 20)
    // 	.attr("height", 20)
    // 	.style("fill", function () {
    // 		    return schoolcolor(datanum - 2)
    // 	});

    // }

    
  
    
	
	var legend = svg.selectAll(".legend")
    	    .data(color.domain())
    	    .enter().append("g")
    	    .attr("class", "legend")
    	    .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; })
	
	legend.append("rect")
    	    .attr("x", width - 18)
    	    .attr("width", 18)
    	    .attr("height", 18)
	    .on('mouseover', function(d, i) {
		data = chartdata[datanum][i];
		tooltip.select('.label').html(attitudes_domain[i] + "<br><br>");
		tooltip.select('.score').html("Average score: " + Math.round(data.score));
		this_percent = Math.round(data.percent-data.startpercent)
		this_num_of_students = Math.round((num_of_students[datanum]/100)*this_percent);
		tooltip.select('.percent').html( this_percent + " percent (" + this_num_of_students + " students)");
		tooltip.style('display','inline-block');
		})
	    .on('mouseout', function(d) {
		tooltip.style('display','none');
	    })
	    .style("fill", function (d) {
		    return color(d)
	    });
	
	

	legend.append("text")
	    .attr("class","text")
    	    .attr("x", width - 24)
    	    .attr("y", 9)
    	    .attr("dy", ".35em")
    	    .style("text-anchor", "end")
    	    .text(function(d) {
		    return attitudes_domain[d];
		    
	    });

    
   
    
    svgs[datanum] = svg
    xAxiss[datanum] = xAxis
    yAxiss[datanum] = yAxis
    if (datanum == 0 || datanum == 1) {
    legends[datanum] = legend
    }
    

    
    check_boxes_string = ""
    for (i = 0; i<school_domain.length; i++) {
	thistoggle = "domain"+i+datanum;
	check_boxes_string += school_domain[i];
	check_boxes_string += toggle_html_string;
	check_boxes_string += thistoggle
	check_boxes_string += toggle_html_string_two;
	if (i == 1) {
	    check_boxes_string += "<br>";}
	school_domain_bools[datanum].push(true);
	
	
    }

    function handleToggle(thistoggle,i,num) {
	d3.select(thistoggle)
	    .on('change', function() {
		var newData = d3.select(this).property('checked');
		school_domain_bools[num][i] = newData;
		togglesChanged(num);
	    });
    }
    if (datanum == 0) {
	checkbox_id = "#school_domain_check_boxes"}
    else
    {
    	checkbox_id = "#school_domain_check_boxesb"}
    

    $(checkbox_id).html(check_boxes_string);
    for (i = 0; i<school_domain.length; i++) {
	thistoggle = "#domain"+i+datanum;
	thisnum = Number(datanum);
	handleToggle(thistoggle,i,thisnum);
    }
    this_chart_div = "#first_chart";
    if (datanum == 1) {
    this_chart_div = "#second_chart";
    }
    
    var tooltip = d3.select(this_chart_div)            
	.append('div')                             
	.attr('class', 'tooltip');                 

    tooltip.append('div')                        
	.attr('class', 'label');                   

    tooltip.append('div')                        
	.attr('class', 'score');                   

    tooltip.append('div')                        
	.attr('class', 'percent');                 

    var titletooltip = d3.select(this_chart_div)            
	.append('div')
	.attr('class', 'titletooltip');                 

    titletooltip.append('div')                        
	.attr('class', 'label');                   

    
    
    $("#score_toggle").prop("checked", false);
    $("#question_toggle").prop("checked", false);

    $("#score_toggleb").prop("checked", false);
    $("#question_toggleb").prop("checked", false);

    
    curr_values = $("#Slider1").slider("value");
    curr_values = curr_values.split(";");
    school_score_min[0] = parseInt(curr_values[0]);
    school_score_max[0] = parseInt(curr_values[1]);


    curr_values = $("#Slider2").slider("value");
    curr_values = curr_values.split(";");
    school_score_min[1] = parseInt(curr_values[0]);
    school_score_max[1] = parseInt(curr_values[1]);


    //fix for slider not working properly before a resize
    $(window).resize()
    
};


function togglesChanged(num) {
    updateChart(num);
}




function updateChart(chartnum) {
    chartdata[chartnum] = makeChartData(chartnum)
  
    x = d3.scale.linear()
    .range([0, width]);



    y = d3.scale.linear()
    .range([height,0]);

    
    x.domain([0,100]);

    y.domain([200,700]);
    
    svg = svgs[chartnum]
    xAxis = xAxiss[chartnum]
    yAxis = yAxiss[chartnum]
    svg.selectAll(".bar")
    	.data(chartdata[chartnum])
	.transition()
       	.duration(100)
    	.attr("x",function(d,i) {return x(d.startpercent);})
    	.attr("y",function(d) {return height-(height-y(d.score))})
    	.attr("width",function(d) {return x(d.percent-d.startpercent);})
    	.attr("height",function(d,i){
    	    return height - y(d.score);});
 
   // if (chartnum == 1) {
//	legend = legends[chartnum]
//	legend.selectAll(".text")
//	    .transition()
//	    .text(function(d) {
//		return get_school_domain(d);
//	    })
		    
  //  }

    svg.selectAll("#main_title")
        .style("font-size","20px")
        .style("fontWeight","")
        .text(getAttitudeString(chartnum));

    sizeText("#main_title",width)

    svg.selectAll(".y_label")
     	.text(getYText())

    svg.selectAll(".x_label")
     	.text(getXText(chartnum))

    svg.selectAll(".title")
     	.text(getTitleText(chartnum))



    
    

   
}

function get_school_domain(d) {
    if (isPercentileQ()) {
	return percentile_domain[d];
    } else  {
	return school_domain[d];
    }
		      }

