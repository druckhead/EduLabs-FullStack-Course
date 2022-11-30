salary = int(input("Enter your yearly salary: "))

tax_to_pay = 0.0

if salary < 77_400:
    tax_to_pay = (salary * 0.1)
else:
    tax_to_pay += (77_400 * 0.1)
    if salary >= 77_401:
        if salary < 110_881:
            tax_to_pay += ((salary - 77_400) * 0.14)
        else:
            tax_to_pay += ((110_880 - 77_400) * 0.14)
        if salary >= 110_881:
            if salary < 178_081:
                tax_to_pay += ((salary - 110_880) * 0.2)
            else:
                tax_to_pay += ((178_080 - 110_881) * 0.2)
            if salary >= 178_081:
                if salary < 247_441:
                    tax_to_pay += ((salary - 178_080) * 0.31)
                else:
                    tax_to_pay += ((247_440 - 178_081) * 0.31)
                if salary >= 247_441:
                    if salary < 541_921:
                        tax_to_pay += ((salary - 247_440) * 0.35)
                    else:
                        tax_to_pay += ((514_920 - 247_441) * 0.35)
                    if salary >= 514_921:
                        if salary < 663_240:
                            tax_to_pay += ((salary - 514_920) * 0.47)
                        else:
                            tax_to_pay += ((663_240 - 514_921) * 0.47)
                        if salary > 663_240:
                            tax_to_pay += ((salary - 663_240) * 0.50)

percent = (tax_to_pay / salary) * 100

print(f"you have to pay {tax_to_pay} shekels, which is overall,", "~{:.2f}".format(percent), "% of your salary")
print(f"You have {salary - tax_to_pay} shekels left after tax")
