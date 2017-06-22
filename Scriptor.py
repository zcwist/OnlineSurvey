from jinja2 import Environment, FileSystemLoader, select_autoescape
class Scriptor(object):
	"""Generate Google form script for set of methods and questions"""
	def __init__(self, arg):
		super(Scriptor, self).__init__()
		self.arg = arg
		# self.survey_name = arg["survey_name"]
		# self.pre_questions = arg["pre_questions"]
		# self.methods = arg["methods"]
		# self.questions = arg["questions"]
		# self.scriptRender()

	def scriptRender(self):
		env = Environment(
			loader=FileSystemLoader("./templates")
		)
		template = env.get_template("designmethod.gs")
		rendered = template.render(self.arg)
		return rendered

if __name__ == '__main__':
	fakedata =  {"survey_name":"Module 1",
				"pre_questions":["What's your name?","What class are you in?"],
				"methods":["AEIOU", "POEMS"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}
	print Scriptor(fakedata).scriptRender()

		