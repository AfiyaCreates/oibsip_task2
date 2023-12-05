def get_user_input():
    # Function to get user input for height and weight
     height=float(input("enter height in inches: "))
     weight=float(input("enter weight in lbs: "))
     return height, weight

def BMI(height,weight):
    # Function to calculate BMI and provide a health status   
    bmi=weight/(height**2)*703
    if (bmi<16):
        return "severely underweight",bmi
    elif(bmi>=16 and bmi<18.5):
        return "underweight",bmi
    elif(bmi>=18.5 and bmi<25):
        return "healthy",bmi
    elif(bmi>=25 and bmi<30):
        return "overweight",bmi
    elif(bmi>=30):
        return "obese",bmi  

def display_bmi_result(quote, bmi):
     # Function to display the BMI result             
    print("your bmi is:{} and you are: {}".format(bmi,quote))

def main():
    # Main function to organize the BMI calculation process
    print("WELCOME TO BMI CALCULATOR!")
    height, weight = get_user_input()
    quote, bmi = BMI(height, weight)
    display_bmi_result(quote, bmi)

    # Additional feature: Provide weight recommendation for a healthy BMI
    if quote != "healthy":
        target_bmi = 22.5  # BMI for a healthy weight
        target_weight = target_bmi * (height ** 2) / 703
        weight_difference = target_weight - weight

        if weight_difference > 0:
            print("To achieve a healthy BMI, you should aim to gain {:.2f} lbs.".format(abs(weight_difference)))
        elif weight_difference < 0:
            print("To achieve a healthy BMI, you should aim to lose {:.2f} lbs.".format(abs(weight_difference)))
        else:
            print("Your weight is already in the healthy range.")


if __name__ == "__main__":
    main()    
