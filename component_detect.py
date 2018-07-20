

#Component object class
class Component:
	def __init__(self, tag, name, iden, x, y, active, visable):
		self.x = x
		self.y = y
		self.tag = tag
		self.name = name
		self.id = iden
		self.active = active
		self.visable = visable		
		self.placeholder = None	
		self.vis_text = None	
	def print_all(self):
		print ("Tag = " + str(self.tag))
		print ("Name = " + str(self.name))
		print ("ID = " + str(self.id))
		print ("X-coor = " + str(self.x))
		print ("Y-coor = " + str(self.y))
		print ("Active = " + str(self.active))
		print ("Visable = " + str(self.visable))
		if self.placeholder != None:
			print ("Placeholder Text = " + str(self.placeholder)) 
		if self.vis_text != None:
			print ("Text = " + str(self.vis_text)) 
		print("\n")	

#method for parsing json data into unsorted Component objects
def gather_components(site,raw_components):
	count = 0
	for e in site[0]:
		#gather the basics
		raw_components.append(Component(e.get('tag',"none"), e.get('name',"none"), e.get('id',"none"), e.get('left',"none"), e.get('top',"none"), True, True))
		#gather disabled / hidden
		if "disabled" in e.get('outerHTML',"none"):
			raw_components[count].active = False
		if "hidden" in e.get('outerHTML',"none"):
			raw_components[count].visable = False
		#gather placeholder
		if (e.get('tag',"none") == 'input' and ("placeholder" in e.get('outerHTML',"none"))):
					x = e.get('outerHTML',"none")
					y = x.index("placeholder") + 13
					ph = ""
					while x[y] != '"':
						ph += x[y]
						y += 1
					raw_components[count].placeholder = str(ph)	
		
		#gather visable text (INNER HTML)
		html_str = str(e.get('outerHTML',"none"))

		text = ""

		for i in range(len(html_str)):
			if i +1 < len(html_str):
				if ((html_str[i] == ">") and (html_str[i+1] != "<")):
					counter = i+1
					while html_str[counter] != '<':
						text += html_str[counter]
						counter += 1
		
				
		if text != "":
			raw_components[count].vis_text = str(text)
	
		count += 1
				

#method for printing unsorted component objects
def print_components(c):
	print("Unsorted Components: (" + str(len(c)) + ")\n--------------\n")	
	for i in c:
		i.print_all()


#method for sorting Component objects into types 
def sort_components(component_list,unsorted_component_list):
	sorted_components = {}
	if unsorted_component_list != []:
		return

	def check_if_not(element):
		if element in sorted_components:
			return False
		else:
			return True

	for i in component_list:
		if "forgot" in str(i.vis_text).lower() and check_if_not("Forgot Password Link"):
			sorted_components["Forgot Password Link"] = i
		if ("show" in str(i.name).lower() and "pass" in str(i.name).lower()) or ("hide" in str(i.name).lower() and "pass" in str(i.name).lower()):
			sorted_components["Show/Hide Password Toggle"] = i
		elif str(i.tag).lower() == "input" and "email" in str(i.name).lower():
			sorted_components["Email Input Field"] = i
		elif str(i.tag).lower() == "label" and "email" in str(i.vis_text).lower():
			sorted_components["Email Input Label"] = i
			
		elif str(i.tag).lower() == "input" and "pass" in str(i.name).lower():
			sorted_components[("Password Input Field")] = i
			
		elif str(i.tag).lower() == "label" and "pass" in str(i.vis_text).lower():
			sorted_components["Password Input Label"] = i
		elif (str(i.tag).lower() == '[type="submit"]' or ((str(i.tag).lower() == 'button') and ("log" in str(i.vis_text).lower() or "sign" in str(i.vis_text).lower()) or "continue" in str(i.vis_text).lower() or "next" in str(i.vis_text).lower())):
			sorted_components["Submit Button"] = i
		elif "remember me" in str(i.vis_text).lower() or "keep me" in str(i.vis_text).lower():
			sorted_components["Remember Me Checkbox Label"] = i
		elif ("remember" in str(i.name).lower() or "remember" in str(i.id).lower() ) and "input" == str(i.tag).lower():
			sorted_components["Remember Me Checkbox"] = i
		elif "clear" in str(i.vis_text).lower():
			sorted_components["Clear Button"] = i
		else:
			unsorted_component_list.append(i)	

	return sorted_components

def print_sorted_components(sorted_components):
	
	print ("Sorted Components: (" + str(len(sorted_components)) + ")")
	for i in sorted_components:
			print ("\t" + i + "\n"),
	print ("--------------")
	for i in sorted_components:
		print "\n"
		print i

		print ("\t" + "Tag = " + str(sorted_components[i].tag))
		print ("\t" + "Name = " + str(sorted_components[i].name))
		print ("\t" + "ID = " + str(sorted_components[i].id))
		print ("\t" + "X-coor = " + str(sorted_components[i].x))
		print ("\t" + "Y-coor = " + str(sorted_components[i].y))
		print ("\t" +  "Active = " + str(sorted_components[i].active))
		print ("\t" + "Visable = " + str(sorted_components[i].visable))
		if sorted_components[i].placeholder != None:
			print ("\t" + "Placeholder Text = " + str(sorted_components[i].placeholder)) 
		if sorted_components[i].vis_text != None:
			print ("\t" + "Text = " + str(sorted_components[i].vis_text)) 
		
	print ("\n")



#run the actual code	

'''
raw_component_list = []
unsorted_component_list = []
sorted_component_dict = {}

gather(tmisha, raw_component_list)

sorted_component_dict = sort_components(raw_component_list,unsorted_component_list)

best_practice_checker(sorted_component_dict)

print_sorted_components(sorted_component_dict)

print_components(unsorted_component_list)
'''



