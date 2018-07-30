from component_detect import*

pages = {}


class BestPractice:
	"""docstring for Rule"""
	def __init__(self, rule, user_impact):
		self.rule = rule
		self.user_impact = user_impact
		self.outcome = "UNKNOWN"

		

def best_practice_checker(page_state):
	

	sorted_components = page_state.sorted_components

	'''
	if page_state.best_practices != []:
		return
	'''

	#RULES FOR START STATE
	if page_state.page_state_name == "start":

		#RULE 1
		rule1 = BestPractice("Resist using placeholder text as labels.",2)

		if "Email Input Field" in sorted_components and "Email Input Label" in sorted_components: 
			if sorted_components["Email Input Field"].placeholder == "Email" and sorted_components["Email Input Label"].vis_text != "Email":
				rule1.outcome = "FAIL"
			else:
				rule1.outcome = "PASS"
		elif "Email Input Field" in sorted_components and "Email Input Label" not in sorted_components: 
			rule1.outcome = "FAIL"
		else:
			rule1.outcome = "FAIL (Components not detected)."
			
		pages[page_state.page_name].best_practices.append(rule1)

		#RULE 2
		rule2 = BestPractice("Top align form labels.",1)
		if "Email Input Field" in sorted_components and "Email Input Label" in sorted_components: 
			if ( (sorted_components["Email Input Field"].y > sorted_components["Email Input Label"].y) and 
				(sorted_components["Email Input Field"].x -10  <= sorted_components["Email Input Label"].x  <= sorted_components["Email Input Field"].x +10) ):
				rule2.outcome = "PASS"
			else:
				rule2.outcome = "FAIL"	
		else:
			rule2.outcome = "FAIL (No form labels)."		
		pages[page_state.page_name].best_practices.append(rule2)

		#RULE 3
		rule3 = BestPractice("Arrange forms in one column",1)
		if "Email Input Field" in sorted_components and "Email Input Label" in sorted_components and "Password Input Field" in sorted_components and "Password Input Label" in sorted_components: 
			#Only works for one column right now....
			if ((sorted_components["Email Input Label"].y < sorted_components["Password Input Label"].y) and
				(sorted_components["Email Input Field"].y < sorted_components["Password Input Field"].y) and
				(sorted_components["Email Input Label"].x-5 < sorted_components["Password Input Label"].x) < sorted_components["Email Input Label"].x+5):
				rule3.outcome = "PASS"
			else:
				rule3.outcome = "FAIL"
		elif "Email Input Field" in sorted_components and "Email Input Label" not in sorted_components and "Password Input Field" in sorted_components and "Password Input Label" not in sorted_components:
			if ((sorted_components["Email Input Field"].y < sorted_components["Password Input Field"].y) and
				(sorted_components["Email Input Field"].x == sorted_components["Password Input Field"].x)):
				rule3.outcome = "PASS"
			else:
				rule3.outcome = "FAIL"
		else: 
			rule3.outcome = "FAIL - not detected"
		pages[page_state.page_name].best_practices.append(rule3)


		#RULE 4
		rule4 = BestPractice("Have a 'Remember Me' option.", 3)
		if "Remember Me Checkbox Label" in sorted_components:
			rule4.outcome = "PASS"
		else:
			rule4.outcome = "FAIL"	
		pages[page_state.page_name].best_practices.append(rule4)


		#RULE 5
		rule5 = BestPractice("Have a 'Show/Hide Password' toggle.", 3)
		if "Show/Hide Password Toggle" in sorted_components:
			rule5.outcome = "PASS"
		else:
			rule5.outcome = "FAIL"	
		pages[page_state.page_name].best_practices.append(rule5)

		#RULE 6
		rule6 = BestPractice("Have a password recovery option.", 4)
		if "Forgot Password Link" in sorted_components:
			rule6.outcome = "PASS"
		else:
			rule6.outcome = "FAIL"
		pages[page_state.page_name].best_practices.append(rule6)

		
		#RULE 7
		rule7 = BestPractice('Avoid "clear" buttons.',3)

		if "Clear Button" in sorted_components:
			rule7.outcome = "FAIL"
		else:
			rule7.outcome = "PASS"
		pages[page_state.page_name].best_practices.append(rule7)

		
		#RULE 8
		rule8 = BestPractice('Make CTAs descriptive.',2)

		if "Submit Button" in sorted_components:
			if sorted_components["Submit Button"].vis_text == "Submit":
				rule8.outcome = "FAIL"
			else:
				rule8.outcome = "PASS"		
		else:
			rule8.outcome = "FAIL, no submit button found."	
		pages[page_state.page_name].best_practices.append(rule8)
		
		#RULE 9
		rule9 = BestPractice('Auto-focus on the first field.',2)

		if "Email Input Field" in sorted_components:
			if sorted_components["Email Input Field"].focus == "true":
				rule9.outcome = "Pass"
			else:
				rule9.outcome = "Fail"		
		else:
			rule8.outcome = "FAIL, no email input field  found."	
		pages[page_state.page_name].best_practices.append(rule9)

	#Rules Followed Calculation
	success_count = 0
	total_count = 0
	for i in pages[page_state.page_name].best_practices:
		if i.outcome == "PASS":
			success_count += 1
		total_count += 1

	pages[page_state.page_name].best_practices_followed = str(success_count) + "/" + str(total_count)

	#Weighted Score Calculation
	success_count = 0
	total_count = 0
	for i in pages[page_state.page_name].best_practices:
		if i.outcome == "PASS":
			success_count += i.user_impact
		total_count += i.user_impact
	
	pages[page_state.page_name].score = str(int((float(success_count)/float(total_count))*100))

def print_best_practices(test_page):
	
	print ("Best Practice Check: (" + str(len(test_page.best_practices)) +")\n--------------\n\n" + "Rules followed: "+ test_page.best_practices_followed + "\n" + "Weighted Score: "+  test_page.score + "\n")
	
	ui1 = "Minor"
	ui2 = "Moderate"
	ui3 = "Serious"
	ui4 = "Severe"

	bpnum = 1
	for i in test_page.best_practices:
		print ("Rule #" + str(bpnum) + ": " + i.rule)
		print ("\t" + "Outcome: " + i.outcome)
		if i.user_impact == 1:
			print ("\t" +"User Impact: " + str(ui1))
		if i.user_impact == 2:
			print ("\t" +"User Impact: " + str(ui2))
		if i.user_impact == 3:
			print ("\t" +"User Impact: " + str(ui3))
		if i.user_impact == 4:
			print ("\t" +"User Impact: " + str(ui4))
		print ("\n")
		bpnum +=1










