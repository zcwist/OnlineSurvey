function myFunction() {
  var form = FormApp.create("{{survey_name}}"); 
  {% for pre_quesiton in pre_questions %}form.addTextItem().setTitle("{{pre_quesiton}}");
  {% endfor %}
  {% for method in methods %}//section for {{method}}
  form.addPageBreakItem().setTitle("{{method}}");
  {% for question in questions %}
  {% if question.type == "Text" %}form.addTextItem().setTitle("{{question.question_text}}");
  {% elif question.type == "Multiple Choice" %}var item = form.addMultipleChoiceItem();
  item.setTitle("{{question.question_text}}");
  item.setChoices([
  item.createChoice("Yes"),
  item.createChoice("No"),
  ]);
  {% endif %}{% endfor %}//end section for {{method}}
  
  {% endfor %}}


