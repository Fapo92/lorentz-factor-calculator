#coding=utf-8

import cmath
from math import sqrt
from decimal import Decimal

v = 0.0
c = 1
resultado = 0.0
welcome = """
    **********************************************
    *       Welcome to the Lorentz factor        *
    *               calculator.                  *  
    *                                            *    
    * Use: input a velocity in c (example: 0.5c) *
    * to obtain its factor. Repeat as many times *
    * as you need to.                            *                       
    **********************************************
    """

def gamma():
    try:

        v = Decimal(input("Input the relative velocity v: "))
        if  v < 1:
            resultado = 1/(sqrt(1-(v/c)**2))
            print('y = ' + str(resultado))
        elif v > 1:
            resultado = 1/(cmath.sqrt(1-(v/c)**2))
            print('y = ' + str(resultado) + ' (Warning: v faster than c. The Lorentz factor becomes an imaginary number.)')
        elif v == 1:
            print("The Lorentz factor goes to infinity when v = c. Try something else.")
    except Exception as e:
        print('Please input a valid velocity') 

def main():
    print(welcome)
    print("After each calculation, you will be prompted to continue (press Enter) or exit (write 'exit' and press enter)") 
    print("")
    key = ''
    while key != 'exit':
        gamma()
        key = input('Continue or exit? ')

if __name__ == "__main__":
    main()