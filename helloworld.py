import random

if __name__ == '__main__':
    r_num1 = random.randint(0, 100)
    r_num2 = random.randint(0, 100)
    print("Rong Jin", r_num1, r_num2, 
          f"Sum = {r_num1+r_num2}", 
          f"Average = {(r_num1+r_num2)/2}", 
          sep='\n') 
    