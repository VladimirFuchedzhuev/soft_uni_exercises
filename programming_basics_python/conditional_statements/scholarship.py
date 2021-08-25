from math import floor
income = float(input())
grade = float(input())
min_wage = float(input())

benefits_scholarship = min_wage * 0.35
results_scholarship = grade * 25

if grade >= 5.50 and income >= min_wage:
    print(f"You get a scholarship for excellent results {floor(results_scholarship)} BGN")
elif grade >= 5.50 and income < min_wage and benefits_scholarship > results_scholarship:
    print(f"You get a Social scholarship {floor(benefits_scholarship)} BGN")
elif grade >= 5.50 and income < min_wage and benefits_scholarship <= results_scholarship:
    print(f"You get a scholarship for excellent results {floor(results_scholarship)} BGN")
elif 4.50 < grade and income < min_wage:
    print(f"You get a Social scholarship {floor(benefits_scholarship)} BGN")
elif 4.50 < grade and income >= min_wage:
    print("You cannot get a scholarship!")
elif grade <= 4.50:
    print("You cannot get a scholarship!")




