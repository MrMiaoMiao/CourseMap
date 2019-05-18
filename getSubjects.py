import config

import re
import requests
from bs4 import BeautifulSoup
try:
	from urllib.parse import urlparse, parse_qs
except ImportError:
	from urlparse import urlparse, parse_qs

all_subjects = open('course/subjects.txt', 'w')

page = requests.get(config.UW_UNDERGRAD_COURSE_TABLE).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find(text=re.compile("^Course$")).find_parent('table')

table = soup.find(text='Course').find_parent('table')

for row in table.findAll('tr'):
	a = row.find('a', attrs={'href': re.compile("^/courses")})
	if a is not None:
		parsed_link = urlparse(a.get('href'))
		if parsed_link.query:
			course_code = parse_qs(parsed_link.query).get('Code')[0]
		else:
			course_code = parsed_link.path.split('/')[2]
		if course_code in config.DO_NOT_INCLUDE:
			continue
		all_subjects.write(config.UW_UNDERGRAD_CALENDAR_BASE + '/courses/' + course_code + '\n')

all_subjects.close()
