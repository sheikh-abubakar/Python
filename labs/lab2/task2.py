student_data = {
    'students':[
        {'name': 'AnnaBel', 'grades':[85, 90, 88]},
        {'name': 'Ben', 'grades':[78, 82, 80]},
        {'name': 'Cara', 'grades':[92, 91, 93]}
    ]
}

# average Grade

for grades in student_data['students']:
    avg = round(sum(grades['grades']) / len(grades['grades']), 2)
    print(f"{grades['name']} having average grades: {avg}")
    print("-" * 20)

# convert_to_tuples(student_data)

def convert_to_tuples(student_data):
    for std in student_data['students']:
        tuple = []
        name = std['name']
        avg_grade = round(sum(std['grades']) / len(std['grades']), 2)
        tuple.append((name, avg_grade))
        print(tuple)

print("-" * 20)

convert_to_tuples(student_data)