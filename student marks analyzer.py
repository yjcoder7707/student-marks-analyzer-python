from functools import reduce

def analyze_marks(*marks):
    if not marks:
        return None

    average = reduce(lambda a, b: a + b, marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    good_marks = list(
        filter(lambda x: x >= 75, marks)
    )

    squared_marks = list(
        map(lambda x: x * x, marks)
    )

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "marks_above_75": good_marks,
        "squared_marks": squared_marks
    }


result = analyze_marks(65, 82, 91, 74, 88)

print(result)