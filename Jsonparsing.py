import json

# JSON string
json_string = '''
{
  "students": [
    {
      "name": "John Doe",
      "subjects": [
        {
          "name": "Mathematics",
          "percentage": 85
        },
        {
          "name": "English",
          "percentage": 78
        },
        {
          "name": "Science",
          "percentage": 92
        }
      ]
    },
    {
      "name": "Jane Smith",
      "subjects": [
        {
          "name": "Mathematics",
          "percentage": 85
        },
        {
          "name": "English",
          "percentage": 78
        },
        {
          "name": "Science",
          "percentage": 92
        }
      ]
    },
    {
      "name": "Emily Johnson",
      "subjects": [
        {
          "name": "Mathematics",
          "percentage": 91
        },
        {
          "name": "English",
          "percentage": 84
        },
        {
          "name": "Science",
          "percentage": 89
        }
      ]
    }
  ]
}
'''

# Parse JSON string
data = json.loads(json_string)

# maths=[]
# english=[]
# science=[]
# for student in data['students']:
#     name=student['name']
#     for subject in student['subjects']:
#         if subject['name']=='Mathematics':
#             marks=subject['percentage']
#             maths.append({"name":name,"marks":marks})
# print(maths)


maths = {}
english = {}
science={}

for student in data['students']:
    name = student['name']
    for subject in student['subjects']:
        if subject['name'] == 'Mathematics':
            marks = subject['percentage']
            if marks not in maths:
                maths[marks] = []
            maths[marks].append({"name": name,"marks":marks})
        elif subject['name'] == 'English':
            marks = subject['percentage']
            if marks not in english:
                english[marks] = []
            english[marks].append({"name": name,"marks":marks})
        else:
            marks=subject['percentage']
            if marks not in science:
                science[marks]=[]
            science[marks].append({"name":name,"marks":marks})
# print(maths.items())
# print(english)
# print(science)


result = {"mathematics": [], "english": [],"science":[]}
for marks, students in maths.items():
    if len(students) > 1:
        result["mathematics"].extend(students)

for marks, students in english.items():
    if len(students) > 1:
        result["english"].extend(students)
for marks, students in science.items():
    if len(students)>1:
        result["science"].extend(students)


result_json = json.dumps(result, indent=2)
print(result_json)
