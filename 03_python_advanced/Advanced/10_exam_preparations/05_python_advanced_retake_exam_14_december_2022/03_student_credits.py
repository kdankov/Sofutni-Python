def students_credits(*args):
    courses_dict = {}
    result = []
    gathered_credits = 0

    for data in args:
        course_name, course_credits, max_test_points, diyans_points = data.split('-')

        courses_dict[course_name] = int(course_credits) * (int(diyans_points) / int(max_test_points))
        gathered_credits += courses_dict[course_name]

    sorted_courses = sorted(courses_dict.items(), key=lambda x: -x[1])

    if gathered_credits >= 240:
        result.append(f'Diyan gets a diploma with {gathered_credits:.1f} credits.')
    else:
        result.append(f'Diyan needs {(240 - gathered_credits):.1f} credits more for a diploma.')

    for key, value in sorted_courses:
        result.append(f'{key} - {value:.1f}')

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print()

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print()

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
