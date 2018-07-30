
import json
from component_detect import*
from best_practice_check import*
from page_setup import*

import sys

#finds the JSON files in the output folder. 
import os
output = os.listdir(str(os.curdir) + '/output')

print '\n--------------------------------------------------------'
print "Starting RUN.PY "
print '--------------------------------------------------------'

'''
#for printing files found
print "\nJSON FILES FOUND:\n--------------"
for file in output:
	if '.json' in file: 
		print file

#Load pages & page states
for file in output:
	if '.json' in file:
		file_name = str(file)
		name = file_name.replace('-out.json','')
		load_page (name, "sign-in")
		load_page_state (Page_State(name, 'output/' + file_name, 'start'))
'''


#Find the most recent json files, and Load pages & page states

mr_name = ''
mr_time = ''
mr_file_name = ''

for file in output:
	if '-start' in file:
		file_name = str(file)
		name = file_name.replace('-start','')
		name = name.replace('.json','')
		time = ''
		for sub in name:
			if sub == '@':
				time = ''
			else:
				time += sub
		name  = name.replace(str(time),'')
		name  = name.replace(str('@'),'')

		
		if mr_name == '':
			mr_name = name
			mr_time = time
			mr_file_name = file_name
		elif mr_time < time:
			mr_name = name
			mr_time = time
			mr_file_name = file_name

		#load_page (name, "sign-in")
		#load_page_state (Page_State(name, 'output/' + file_name, 'start'))

print "most recent name: " + mr_name
print "most recent time: " + mr_time
print 'most recent file: ' + mr_file_name

load_page (mr_name, "sign-in")
load_page_state (Page_State(mr_name, 'output/' + mr_file_name, 'start'))

#Analyze all states in all pages (Only do this once)p
for page in pages:
	for state in pages[page].states:
		page_analysis(pages[page].states[state])

#Print analysis of a the most recent JSON file
print_page_analysis(pages[mr_name])


'''
template = "<html>\n<body>\n %s \n</body>\n</html>"
#print template % output


Html_file= open("main.html","w")
Html_file.write(template % "d")
Html_file.close()
'''

#Compare scores of multiple page states
#compare_pages(pages["twitter"],pages["netflix"],pages["airtable"],pages["tmisha"])








#Load pages (page name) - OLD
'''
load_page("twitter","sign-in")
load_page("netflix","sign-in")
load_page("tmisha","sign-in")
load_page("airtable","sign-in")
load_page("walmart","sign-in")

#Load page states (page name, file name, page state name)
load_page_state(Page_State('twitter','output/twitter-out.json','start'))
load_page_state(Page_State('netflix','output/netflix-out.json','start'))
load_page_state(Page_State('airtable','output/airtable-out.json','start'))
load_page_state(Page_State('tmisha','output/tmisha-out.json','start'))
load_page_state(Page_State('walmart','output/walmart-out.json','start'))
'''

