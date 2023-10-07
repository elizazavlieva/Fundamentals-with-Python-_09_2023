grade_info = float(input())


def evaluation(grade):
    grade_with_words = ''
    if 2.00 <= grade <= 2.99:
        grade_with_words = 'Fail'
    elif 3.00 <= grade <= 3.49:
        grade_with_words = 'Poor'
    elif 3.50 <= grade <= 4.49:
        grade_with_words = 'Good'
    elif 4.50 <= grade <= 5.49:
        grade_with_words = 'Very Good'
    elif 5.50 <= grade <= 6.00:
        grade_with_words = 'Excellent'
    return grade_with_words


print(evaluation(grade_info))
