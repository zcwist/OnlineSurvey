function myFunction() {
  var form = FormApp.create("{{survey_name}}").setDescription("In this individual survey, you will be required to submit 3 methods that you plan to select for your project. Additionally, you will be required to justify both methods that you and did not choose. Due *******"); 
  form.setCollectEmail(true);
  form.setProgressBar(true);
  {% for pre_quesiton in pre_questions %}form.addTextItem().setTitle("{{pre_quesiton}}").setRequired(true);
  {% endfor %}
  {% for method in methods %}//section for {{method}}
  form.addPageBreakItem().setTitle("{{method}}");
  {% for question in questions %}
  {% if question.type == "text" %}form.addTextItem().setTitle("{{question.question_text}}").setRequired(true);
  {% elif question.type == "multiple_choice" %}var item = form.addMultipleChoiceItem();
  item.setTitle("{{question.question_text}}");
  item.setChoices([
  item.createChoice("Yes"),
  item.createChoice("No"),
  ]);
  item.setRequired(true)
  {% endif %}{% endfor %}//end section for {{method}}
  {% endfor %}
  form.addPageBreakItem().setTitle("Additional?").setHelpText("If you used any methods that were not listed, please include them here.")
  form.addParagraphTextItem().setTitle("Please list all additional methods here, if applicable.")
  form.addParagraphTextItem().setTitle("Why did you choose?")
  }


