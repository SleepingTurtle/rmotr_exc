def get_grade_letter(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade_letter(94))
print(get_grade_letter(84))
print(get_grade_letter(74))
print(get_grade_letter(64))
print(get_grade_letter(4))