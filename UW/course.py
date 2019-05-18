import re

class CourseInfo:
	def __init__(self, data):
		self.course_id		= data.get('course_id')
		self.subject		= data.get('subject')
		self.catalog_number = data.get('catalog_number')
		self.title			= data.get('title')

	def __repr__(self):
		return str(self.subject) + ' ' + str(self.catalog_number)

class Course:
	def __init__(self, data):
		self.course_id				= data.get('course_id')
		self.subject				= data.get('subject')
		self.catalog_number			= data.get('catalog_number')
		self.title					= data.get('title')
		self.units					= data.get('units')
		self.description			= data.get('description')
		self.sections				= data.get('sections')
		self.prerequisites			= data.get('prereq')
		self.prerequisites_parsed	= self.parseRequisites(self.prerequisites)
		self.antirequisites			= data.get('antireq')
		self.antirequisites_parsed	= self.parseRequisites(self.antirequisites)
		self.corequisites			= data.get('coreq')
		self.corequisites_parsed	= self.parseRequisites(self.corequisites)
		self.crosslist				= data.get('crosslist')
		self.terms_offered			= self.parseTermsOffered(data.get('terms_offered'))
		self.offered_online			= data.get('offered_online')
		self.notes					= data.get('notes')

	def __repr__(self):
		val = "#####################################################################\n"
		val += 'subject: ' + str(self.subject) + '\n'
		val += 'catalog_number: ' + str(self.catalog_number) + '\n'
		val += 'title: ' + str(self.title) + '\n'
		val += 'units: ' + str(self.units) + '\n'
		val += 'description: ' + str(self.description) + '\n'
		val += 'sections: ' + str(self.sections) + '\n'
		val += 'prerequisites: ' + str(self.prerequisites) + '\n'
		val += 'prerequisites_parsed: ' + str(self.prerequisites_parsed) + '\n'
		val += 'antirequisites: ' + str(self.antirequisites) + '\n'
		val += 'antirequisites_parsed: ' + str(self.antirequisites_parsed) + '\n'
		val += 'corequisites: ' + str(self.corequisites) + '\n'
		val += 'corequisites_parsed: ' + str(self.corequisites_parsed) + '\n'
		val += 'terms_offered: ' + str(self.terms_offered) + '\n'
		val += 'offered_online: ' + str(self.offered_online) + '\n'
		val += 'notes: ' + str(self.notes) + '\n'
		val += "#####################################################################\n"
		return val

	def parseTermsOffered(self, terms):
		available_terms = ['F', 'W', 'S']
		terms_offered = []
		for term in terms:
			if term[0] in available_terms:
				terms_offered.append(term[0])

		return terms_offered

	def parseRequisites(self, requisites):
		return []

