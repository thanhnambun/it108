import json
import matplotlib.pyplot as plt
import sys
import os

students = []
DATA_FILE = "data.json"

def score_validation(score, name):
    """_score_validation_

    Args:
        score (_float_): _score_to_validate_
        name (_str_): _name_the_subject_

    Raises:
        ValueError: _print_the_error_
    """
    if score < 0 or score > 10:
        raise ValueError(f"{name} score must be between 0 and 10")

def classify(avg):
    """_classify_

    Args:
        avg (_float_): _the_avg_score_

    Returns:
        _str_: _classification based on avg score_
    """
    if avg >= 8:
        return 'Excellent'
    elif avg >= 6.5:
        return 'Good'
    elif avg >= 5:
        return 'Average'
    else:
        return 'Poor'

def load_from_file():
    """_load_from_file_
    """
    global students
    if not os.path.exists(DATA_FILE):
        students = []
        return
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            students = data.get('students', [])
        except json.JSONDecodeError:
            students = []

def display_students():
    """_display_students_
    """
    load_from_file()
    if not students:
        print("Empty list.")
        return
    headers = ["ID", "Name", "Math", "Physics", "Chemistry", "Average", "Rank"]
    col_widths = [10, 25, 8, 8, 10, 10, 10]
    line = " | ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    sep = "-" * len(line)
    print(sep)
    print(line)
    print(sep)
    for s in students:
        row = [
            str(s.get('id', '')).ljust(col_widths[0]),
            str(s.get('name', '')).ljust(col_widths[1]),
            f"{s.get('math', 0):.2f}".ljust(col_widths[2]),
            f"{s.get('physics', 0):.2f}".ljust(col_widths[3]),
            f"{s.get('chemistry', 0):.2f}".ljust(col_widths[4]),
            f"{s.get('average', 0):.2f}".ljust(col_widths[5]),
            str(s.get('rank', '')).ljust(col_widths[6])
        ]
        print(" | ".join(row))
    print(sep)

def find_student_index_by_id(sid):
    """_find_student_index_by_id_

    Args:
        sid (_str_): _just_string_id_

    Returns:
        _i/None_: _return_the_element_of_list_or_none_
    """
    for i, s in enumerate(students):
        if s.get('id') == sid:
            return i
    return None

def add_student():
    """_add_student_
    """
    sid = input("Enter Student ID: ").strip()
    if any(s.get('id') == sid for s in students):
        print("ID already exists.")
        return
    name = input("Enter Name: ").strip()
    try:
        math = float(input("Math Score: ").strip())
        physics = float(input("Physics Score: ").strip())
        chemistry = float(input("Chemistry Score: ").strip())
        score_validation(math, 'Math')
        score_validation(physics, 'Physics')
        score_validation(chemistry, 'Chemistry')
    except ValueError as e:
        print(f"Error: {e}")
        return
    average = (math + physics + chemistry) / 3
    rank = classify(average)
    student = {
        'id': sid,
        'name': name,
        'math': math,
        'physics': physics,
        'chemistry': chemistry,
        'average': round(average, 2),
        'rank': rank
    }
    students.append(student)
    print("Student added. (Not saved yet)")

def update_student():
    """_update_student_
    """
    sid = input("Enter Student ID to update: ").strip()
    idx = find_student_index_by_id(sid)
    if idx is None:
        print("Student ID not found.")
        return
    try:
        math = float(input("New Math Score: ").strip())
        physics = float(input("New Physics Score: ").strip())
        chemistry = float(input("New Chemistry Score: ").strip())
        score_validation(math, 'Math')
        score_validation(physics, 'Physics')
        score_validation(chemistry, 'Chemistry')
    except ValueError as e:
        print(f"Error: {e}")
        return
    average = (math + physics + chemistry) / 3
    students[idx]['math'] = math
    students[idx]['physics'] = physics
    students[idx]['chemistry'] = chemistry
    students[idx]['average'] = round(average, 2)
    students[idx]['rank'] = classify(average)
    print("Update successful. (Not saved yet)")

def delete_student():
    """_delete_student_
    """
    sid = input("Enter Student ID to delete: ").strip()
    idx = find_student_index_by_id(sid)
    if idx is None:
        print("Student ID not found.")
        return
    confirm = input(f"Are you sure to delete {sid}? (y/n): ").strip().lower()
    if confirm == 'y':
        del students[idx]
        print("Deleted. (Not saved yet)")
    else:
        print("Cancelled.")

def search_student():
    """_search_student_
    """
    key = input("Enter name (partial) or Student ID: ").strip().lower()
    results = []
    for s in students:
        if key == s.get('id', '').lower() or key in s.get('name', '').lower():
            results.append(s)
    if not results:
        print("Not found.")
        return
    print("Results:")
    for r in results:
        print(f"{r.get('id')} | {r.get('name')} | {r.get('average'):.2f} | {r.get('rank')}")

def sort_students():
    """_sort_students_
    """
    print("1. Sort by average score - descending")
    print("2. Sort by name A-Z")
    c = input("Choose: ").strip()
    if c == '1':
        students.sort(key=lambda x: x.get('average', 0), reverse=True)
    elif c == '2':
        students.sort(key=lambda x: x.get('name', '').lower())
    else:
        print("Invalid choice.")
        return
    print("Sorted. (Not saved yet)")

def statistics():
    """_statistics_

    Returns:
        _dict_: _return_the_statistic_of_rank_
    """
    if not students:
        print("Empty list.")
        return
    excellent = sum(1 for s in students if s.get('rank') == 'Excellent')
    good = sum(1 for s in students if s.get('rank') == 'Good')
    average = sum(1 for s in students if s.get('rank') == 'Average')
    poor = sum(1 for s in students if s.get('rank') == 'Poor')
    total = len(students)
    print(f"Total: {total}")
    print(f"Excellent: {excellent}")
    print(f"Good: {good}")
    print(f"Average: {average}")
    print(f"Poor: {poor}")
    return {'Excellent': excellent, 'Good': good, 'Average': average, 'Poor': poor}

def draw_chart():
    """_draw_chart_
    """
    stats = statistics()
    if not stats:
        return
    labels = list(stats.keys())
    sizes = list(stats.values())
    print("1. Pie chart")
    print("2. Bar chart")
    c = input("Choose chart type: ").strip()
    if c == '1':
        plt.figure()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Rank Distribution')
        plt.show()
    elif c == '2':
        plt.figure()
        plt.bar(labels, sizes)
        plt.title('Rank Count')
        plt.ylabel('Number of Students')
        plt.show()
    else:
        print("Invalid choice.")

def save_to_file():
    """_save_to_file_
    """
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({'students': students}, f, indent=4, ensure_ascii=False)
    print("Data saved successfully.")

while True:
    print("\n----------- MENU -----------")
    print("1. Display students")
    print("2. Add student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search student")
    print("6. Sort students")
    print("7. Statistics")
    print("8. Draw chart")
    print("9. Save to file")
    print("10. Exit")
    choice = input("Enter choice (1-10): ").strip()

    if choice == '1': display_students()
    elif choice == '2': add_student()
    elif choice == '3': update_student()
    elif choice == '4': delete_student()
    elif choice == '5': search_student()
    elif choice == '6': sort_students()
    elif choice == '7': statistics()
    elif choice == '8': draw_chart()
    elif choice == '9': save_to_file()
    elif choice == '10':
        save_to_file()
        print("Goodbye!")
        sys.exit()
    else:
        print("Invalid choice.")