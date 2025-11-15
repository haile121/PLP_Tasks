# Sample data
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 85},
    {"name": "David", "grade": 95},
]

# AI-suggested code
def sort_dicts_by_key_ai(data, key):
    return sorted(data, key=lambda x: x[key])

sorted_students_ai = sort_dicts_by_key_ai(students, "grade")
print("AI-suggested sort result:", sorted_students_ai)

# Manual implementation
def sort_dicts_by_key_manual(data, key):
    sorted_data = data.copy()
    n = len(sorted_data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if sorted_data[j][key] < sorted_data[min_index][key]:
                min_index = j
        sorted_data[i], sorted_data[min_index] = sorted_data[min_index], sorted_data[i]
    return sorted_data

sorted_students_manual = sort_dicts_by_key_manual(students, "grade")
print("Manual sort result:", sorted_students_manual)
