import config
from course import Course, CourseInfo

import re
import json
import requests
from bs4 import Tag, NavigableString, BeautifulSoup

def getTagText(tag):
	if tag is None:
		return None
	if isinstance(tag, NavigableString):
		return tag.strip().replace('\n', ' ')
	else:
		return tag.get_text().strip().replace('\n', ' ')

all_courses = []
courses = {}

for subject in config.ALL_SUBJECTS:
	page = requests.get(subject).text
	soup = BeautifulSoup(page, 'html.parser')
	course_list = soup.findAll('center')
	subject_code = subject.rsplit('/', 1)[-1]
	courses[subject_code] = {}

	for course in course_list:
		all_info = course.findAll('tr')
		course_header = all_info[0].findAll('td')
		course_info = getTagText(course_header[0]).split(' ')
		catalog_number = course_info[1]
		sections = course_info[2].split(',')
		units = course_info[3]
		course_id = getTagText(course_header[1]).split(' ')[2]
		title = getTagText(all_info[1])
		description = getTagText(all_info[2])
		notes = getTagText(course.find(text=re.compile("^\[Note: ")))
		if notes:
			notes = notes.split('[Note: ')[1][:-1]
		online = getTagText(course.find(text=re.compile(".*(Online)$")))
		prereq = getTagText(course.find(text=re.compile("^Prereq: ")))
		if prereq:
			prereq = prereq.split('Prereq: ')[1]
		antireq = getTagText(course.find(text=re.compile("^Antireq: ")))
		if antireq:
			antireq = antireq.split('Antireq: ')[1]
		coreq = getTagText(course.find(text=re.compile("^Coreq: ")))
		if coreq:
			coreq = coreq.split('Coreq: ')[1]
		crosslist = getTagText(course.find(text=re.compile("^\(Cross-listed with ")))
		if crosslist:
			crosslist = [x.strip() for x in crosslist.split('with ')[1][:-1].split(',')]
		terms_offered = []

		data = {
			'course_id': course_id,
			'subject': subject_code,
			'catalog_number': catalog_number,
			'title': title,
			'units': units,
			'description': description,
			'sections': sections,
			'prereq': prereq,
			'antireq': antireq,
			'coreq': coreq,
			'crosslist':  crosslist,
			'terms_offered': [],
			'offered_online': online,
			'notes': notes
		}

		all_courses.append(vars(CourseInfo(data)))
		courses[subject_code][catalog_number] = vars(Course(data))

with open('course/courses.json', 'w') as course_data:
	course_data.write(json.dumps(all_courses, indent=4))

with open('course/course_data.json', 'w') as course_data:
	course_data.write(json.dumps(courses, indent=4))
