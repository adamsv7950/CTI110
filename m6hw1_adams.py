# Test Grade Avg
#11/2/17
# CTI-110 M6HW1 - Test Average and Grade
# Venezia Adams
#




def main():
    scores = input("Enter five test scores separated by commas: ")
    return [int(num) for num in scores.split(",")]


def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade


def calc_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("The average is: {:.1f} which is {}".format(average, grade))


def show_letters(num, letter_grade):
    print("{:.1f} is {}\n".format(num, letter_grade))


lst = main()
for n in lst:
    show_letters(n, determine_grade(n))
calc_average(lst)
