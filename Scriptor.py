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
				"pre_questions":["What's your name?"],
				"methods":["AEIOU", "POEMS"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}
	fakedata =  {"survey_name":"I3 Survey- Module 1: Research",
				"pre_questions":["What's your name?"],
				"methods":["AEIOU","POEMS","POSTA","Closed Card Sorting","Open Card Sorting","Design Ethnography","Focus Group","Community Appraisal","Conversation Cafe","Competitive Analysis","Conjoint Analysis","1:1 Interview","User Observation","Usability Testing"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}
	survey2 = 	{"survey_name":"I5 Survey- Module 2: Analysis",
				"pre_questions":["What's your name?"],
				"methods":["Why-how Laddering","Empathy Map","Spectrum Mapping","2x2 Matrix","Reframing","Powers of 10","Customer Journey Mapping","How Might We","Mind Map","Contextmapping","Affinity","Diagramming","Atomize","Concept Map","Touchpoint Matrix","Task Analysis","Kano Analysis"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}	
	survey3 = 	{"survey_name":"I6 Survey- Module 3: Ideate",
				"pre_questions":["What's your name?"],
				"methods":["6-Up Sketches","Visual Brainstorming","Brainstorming","3-12-3 Brainstorming","6-3-5 Brainwriting","Attribute Listing","Do-Redo- Undo","Biomimicry","Weighted Matrix","Forced Analogy","Design Heuristics","The Anti-Problem","Borda Count Voting","Design the Box"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}
	survey4 = 	{"survey_name":"I8 Survey- Module 4: Build",
				"pre_questions":["What's your name?"],
				"methods":["Live Prototyping","Wireframe","Rapid Prototyping","Laser Cutting","3-D Printing","Water Jet Cutting","Direct Shell Production Casting","Laminated Object Manufacturing","Fused Deposition Models","Tangible Prototype","Experience Prototype","Service Prototype","Additive Manufacturing"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}	
	survey5 = 	{"survey_name":"I9 Survey- Module 5: Communicate",
				"pre_questions":["What's your name?"],
				"methods":["Envisionment Videos","Storyboards","Service Blueprint","Business Model Canvas","7 Ps Framework","Usability Report","Personas","Composite Characters"],
				"questions":[
							{"type":"multiple_choice","question_text":"Were you familiar with this method before using theDesignExchange?","choice_items":["Yes","No"]},
							{"type":"multiple_choice","question_text":"Did you choose this method?","choice_items":["Yes","No"]},
							{"type":"text","question_text":"Why did you choose or not choose this method?"}
							]
				}
	print Scriptor(survey5).scriptRender()

		