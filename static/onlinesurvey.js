$(document).ready(function(){
	$(".method-selected").dblclick(function(){
		$(this).remove();
	});
	$("#add_method").click(function(){
		method_name = $("#method_name").val();
		if (method_name != ""){
			$("#methods-selected").append(newMethod(method_name));
		}
	});

	$("span.pre_question.glyphicon-plus").click(function(){
		old_id = $(".pre_questions div:last-child").attr("id");
		var newPrequestion;
		if (old_id){
			new_id = parseInt(old_id)+1;
		}
		else {
			new_id = 1;
		}
		newPrequestion = $("#template").children(".pre_question").clone();	
		console.log(newPrequestion);
		$(newPrequestion).attr("id",new_id);
		$(newPrequestion).children("span.pre_question.glyphicon-minus").click(function(){
			$(this).parent().remove();
		});
		// newPrequestion.children("label").text("Pre-question " + new_id);
		$(".pre_questions").append(newPrequestion);
	});

	$("span.question.glyphicon-plus").click(function(){
		old_id = $(".questions div:last-child").attr("id");
		var newQuestion;
		if (old_id){
			new_id = parseInt(old_id)+1;
		}
		else {
			new_id = 1;
		}
		newQuestion = $("#template").children(".question").clone();	
		console.log(newQuestion);
		$(newQuestion).attr("id",new_id);
		$(newQuestion).children("span").click(function(){
			console.log("here");
			$(this).parent().remove();
		});

		$(newQuestion).find(".dropdown-menu").on('click', 'li a', function(){
			console.log("here");
	      	$(newQuestion).find(".btn:first-child").text($(this).text());
	      	$(newQuestion).find(".btn:first-child").val($(this).text());

   		});
		$(".questions").append(newQuestion);
	});

	newMethod = function(name){
		var str = 	'<span class="method-selected">'+
					name +
					'</span>'
		return str;
	}

	$("span.glyphicon-plus").click();
	
	$("#submit").click(function(){
		var survey = {};
		// console.log($("#collection_name").val());
		survey.survey_name = $("#collection_name").val();
		survey.pre_questions = [];
		$.each($(".pre_questions > .pre_question"),function(i,v){
			// console.log(v);
			pre_question = $(v).find("input").val();
			// console.log(pre_question);
			survey.pre_questions.push(pre_question);
		})
		survey.methods = []
		$.each($("#methods-selected > span"),function(i,v){
			// console.log(v);
			method = $(v).text();
			survey.methods.push(method);
			// console.log(method);
		})
		

		survey.questions = [];
		$.each($(".questions > .question"),function(i,v){
			question = {}
			question.type = $(v).find(".btn:first-child").text();
			console.log(question.type);
			question.question_text = $(v).find("input").val();
			survey.questions.push(question);
		})
		console.log(survey);

		$.ajax({
			type:"POST",
			url:"/uploadSurveyModel",
			data:JSON.stringify({"data":survey}),
			dataType: "json",
            contentType: 'application/json;charset=UTF-8',
            success: function(result){
            	$("#script").html(result.script);
            }
		})
	})
})