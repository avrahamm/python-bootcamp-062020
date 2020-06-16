age_in_years = 0
while True:
    try:
        age_in_years = int(input("Insert your age in years: "))
        break
    except Exception:
        print("Illegal value! Only numbers are permitted. Insert again")

age_in_months = age_in_years * 12
print(f"Your age in months is {age_in_months}")


