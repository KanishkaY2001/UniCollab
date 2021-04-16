from bs4 import BeautifulSoup
import requests
import re
import json

courses = {
    "COMP1511": "https://webcms3.cse.unsw.edu.au/COMP1511/21T1/outline",
    "COMP1521": "https://cgi.cse.unsw.edu.au/~cs1521/20T3/outline",
    "COMP1531": "https://webcms3.cse.unsw.edu.au/COMP1531/21T1/outline",
}

importantHeaders = ["Course Summary", "Assumed Knowledge", "Learning Outcomes"]

data = {}

for course in courses.items():
    html_content = requests.get(course[1]).text

    soup = BeautifulSoup(html_content, 'html.parser')    

    # Store result in here
    result = []


    if (re.search("https://cgi.cse.unsw.edu.au", course[1])):
        # A cgi course
        course_summary = soup.find(id='course-summary')
        for elem in course_summary.next_siblings:
            if (elem.name == 'h3'):
                break
            elif elem.name in ['p', 'ul', 'ol']:
                result.append(' '.join(elem.text.split()))

        assumed_knowledge = soup.find(id='assumed-knowledge')
        for elem in assumed_knowledge.next_siblings:
            if (elem.name == 'h3'):
                break
            elif elem.name in ['p', 'ul', 'ol']:
                result.append(' '.join(elem.text.split()))

        learning_outcomes = soup.find(id='learning-outcomes')
        for elem in learning_outcomes.next_siblings:
            if (elem.name == 'h3'):
                break
            elif elem.name in ['p', 'ul', 'ol']:
                result.append(' '.join(elem.text.split()))
    else: 
        headers = soup.find_all('h3')
        # A webcms course
        for header in headers:
            headerText = header.text.strip()
            matched = 0
            for important in importantHeaders:
                if matched == 3:
                    break
                if re.search(important, headerText):
                    matched += 1         
                    for elem in header.next_siblings:
                        if (elem.name == 'h3'):
                            break
                        elif elem.name == 'p' or elem.name == 'ul':
                            result.append(' '.join(elem.text.split()))
    
    final_string = ' '.join(result)
    data[course[0]] = final_string

with open('scrape.json', 'w') as outfile:
    json.dump(data, outfile)