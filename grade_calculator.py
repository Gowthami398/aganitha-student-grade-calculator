def get_marks():
    marks = []
    for i in range(5):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return marks

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("=== Student Grade Calculator ===")
    marks = get_marks()
    total = sum(marks)
    avg = total / len(marks)
    grade = calculate_grade(avg)

    print("\n--- Results ---")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
