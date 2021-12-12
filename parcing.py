import pandas as pd

def cast_not_concur_people(f1, f2, info):
    count = 0
    for (f1, f2) in zip(info[f1], info[f2]):
        if not prize_concur_people(f1, f2) and not prize_concur_people(f2, f1):
            count += 1
    return count

def prize_concur_people(f1, f2):
    arr = f1.lower().replace('-', ' ').split()
    for word in arr:
        if word in f2.lower():
            return True
    return False

def have_theme(size_t, info, f_search, f_back, str_search):
    return info[info[f_search].str.lower().str.contains(str_search[:-2])][f_back].str.lower(
        ).value_counts().head(size_t)

works = pd.read_csv("works.csv").dropna()
cast_not_concur_people = cast_not_concur_people("jobTitle", "qualification", works)
print(f"Из {works.shape[0]} людей не сходятся профессии и должность у {cast_not_concur_people}")

print("\nОбразование людей, которые работают менеджерами:")
print(have_theme(5, works, "jobTitle", "qualification", "менеджер"))

print("\nДолжности людей, которые ыладеют диплом инженера:")
print(have_theme(5, works, "qualification", "jobTitle", "инженер"))