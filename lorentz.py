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
    *                                            *
    * To exit just stop the terminal process or  *
    * write 'exit' + enter.                      *                       
    **********************************************
    """

def gamma():
    v = Decimal(input("Input the relative velocity v: "))
    if  v < 1:
        resultado = 1/(sqrt(1-(v/c)**2))
        print(resultado)
    elif v > 1:
        resultado = 1/(cmath.sqrt(1-(v/c)**2))
        print(resultado)
    elif v == 1:
        print("The Lorentz factor goes to infinity when v = c. Try something else.")

def main():
    print(welcome)
    key = input("Press enter to continue...") 
    while key != 'exit':
        gamma()
        key = input("Press enter to continue...")

if __name__ == "__main__":
    main()