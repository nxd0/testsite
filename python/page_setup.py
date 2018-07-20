import json
from component_detect import*
from best_practice_check import*


class Page:
	def __init__(self, page_name, page_type):
		self.url = "Unknown"
		self.page_name = page_name
		self.page_type = page_type
		self.states = {}
		self.best_practices = []
		self.best_practices_followed = "Unknown"
		self.score = "Unknown"


class Page_State:
	def __init__(self, page_name, file_name, page_state_name):
		self.file_name = file_name
		self.raw_components = []
		self.unsorted_components = []
		self.sorted_components = {}
		self.page_name = page_name
		self.page_state_name = page_state_name
		self.page_type = "Unknown"
		with open(file_name) as f:
			self.file = json.load(f)

def load_page(page_name,page_type):
	pages [page_name] =  Page(page_name,page_type)

def load_page_state(Page_State):
	page = pages[Page_State.page_name]
	page.states [Page_State.page_state_name] = Page_State


def page_analysis(page_state):
	gather_components(page_state.file, page_state.raw_components)

	page_state.sorted_components  = sort_components(page_state.raw_components, page_state.unsorted_components)
	best_practice_checker(page_state)


def print_page_analysis(page):
	print ("\n")
	print ("SIGN-IN ANALYSIS: " + page.page_name.upper())
	print_best_practices(page)

	print ("STATE ANALYSIS")
	print ("Number of states detected: " + str(len(page.states) ) )
	print ("--------------\n")

	for state in page.states:
		print ("State Analysis: " + page.states[state].page_state_name.upper() + '\n"' + page.states[state].file_name )
		print ("--------------\n")

		print_sorted_components(page.states[state].sorted_components)
		print_components(page.states[state].unsorted_components)


def compare_pages(*test_pages):
	print ("COMPARE PAGES: ")
	print ("--------------\n")
	for page in test_pages:		
		print (page.page_name + " score: " + page.score)
	print ("\n")

