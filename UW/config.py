import json

UW_UNDERGRAD_CALENDAR_BASE = 'http://ugradcalendar.uwaterloo.ca'
UW_UNDERGRAD_COURSE_TABLE = 'http://ugradcalendar.uwaterloo.ca/page/Course-Descriptions-Index'
UW_UNDERGRAD_COURSE_VERSION = '1920' # 2019 - 2020
DO_NOT_INCLUDE = ['BUS'] # excluded courses

try:
	ALL_SUBJECTS = open('course/subjects.txt', 'r').read().splitlines()
except IOError:
	ALL_SUBJECTS = []

try:
	ALL_COURSES = json.load('course/courses.txt')
except AttributeError:
	ALL_COURSES = []
