
import json
from component_detect import*
from best_practice_check import*
from page_setup import*

import sys
print sys.path

#Load pages (page name)

load_page("twitter","sign-in")
load_page("netflix","sign-in")
load_page("tmisha","sign-in")
load_page("airtable","sign-in")

#Load page states (page name, file name, page state name)
load_page_state(Page_State('twitter','twitter-out.json','start'))
load_page_state(Page_State('netflix','netflix-out.json','start'))
load_page_state(Page_State('airtable','airtable-out.json','start'))
load_page_state(Page_State('tmisha','tmisha-out.json','start'))


#Analyze all states in all pages (Only do this once)p
for page in pages:
	for state in pages[page].states:
		page_analysis(pages[page].states[state])

#Print analysis of a particular page state
print_page_analysis(pages["netflix"])

template = "<html>\n<body>\n %s \n</body>\n</html>"
#print template % output


Html_file= open("main.html","w")
Html_file.write(template % "d")
Html_file.close()

#Compare scores of multiple page states
#compare_pages(pages["twitter"],pages["netflix"],pages["airtable"],pages["tmisha"])









'''
def pick_a_page():
	print "Which page do you want to analyze?"
	pap_count = 0
	for values in pages:
		print (str(pap_count) + ". " + values)
		pap_count +=1
	choice = input("s")
	choice_count = int(choice)
	print choice
pick_a_page()

'''