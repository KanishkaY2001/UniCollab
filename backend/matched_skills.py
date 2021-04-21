import json, re 

groupSkills = ["Programming", "C", "Data modelling", "Django", "Python", "SQLite"]
courses = ["COMP1511", "COMP1531"]

def lookingfor(words, courses):
    skills = []
    f = open("scrape.json", "rb")
    data = json.load(f)

    for course in data:  
        if (course in courses):
            for word in words:
                match = re.search(r'[\s|\"]'+word+r'[\s|,|:|\"|\;]', data[course], re.IGNORECASE)
                if (match and word not in skills):
                    skills.append(word)
    f.close()
    return skills

usersSkills = lookingfor(groupSkills, courses)
print("users skills are")
print(usersSkills)