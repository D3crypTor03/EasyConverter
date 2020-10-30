#!/usr/bin/python3

import os


print("\t\t\t[Coded by Harish]\n\n")


def bin2deci():
    bina = int(input("Enter a Binary value: "))
    deci, inc = 0, 0
    while bina != 0:
        rem = bina % 10
        deci = deci + rem * pow(2, inc)
        bina = bina // 10
        inc += 1
    print("The Decimal value :", deci)
    print("\n")


def bin2oct():
    bina = input("Enter a Binary value: ")
    val = int(bina, 2)
    val = oct(val).replace("0o", "")
    print("The Octal value :", val)
    print("\n")


def bin2hex():
    bina = input("Enter a binary: ")
    val = int(bina, 2)
    hexa = hex(val).replace("0x", "")
    print("The Hexadecimal value :", hexa)
    print("\n")


def deci2bin():
    deci = int(input("Enter a Decimal value: "))
    value = bin(deci).replace("0b", "")
    print("The Binary value :", value)
    print("\n")


def deci2oct():
    deci = int(input("Enter a Decimal value: "))
    value = oct(deci).replace("0o", "")
    print("The Octal value :", value)
    print("\n")


def deci2hex():
    deci = int(input("Enter a Decimal value : "))
    val = hex(deci).replace("0x", "")
    print("The Hexadecimal value :", val)
    print("\n")


def oct2bin():
    octa = input("Enter an Octal value: ")
    value = int(octa, 8)
    value = bin(value).replace("0b", "")
    print("The Binary value : ", value)
    print("\n")


def oct2deci():
    octa = input("Enter an Octal value: ")
    while octa != 0:
        value = str(int(octa, 8))
        print("The Decimal value :", value)
        break
    print("\n")


def oct2hex():
    octa = input("Enter an Octal value : ")
    dec = int(octa, 8)
    hexa= hex(dec).replace("0x", "")
    print("The Hexadecimal value : ", hexa)
    print("\n")


def hex2bin():
    hexa = input("Enter a Hexadecimal : ")
    val = int(hexa,16)
    val = bin(val).replace("0b","")
    print("The Binary value : ",val )
    print("\n")


def hex2deci():
    hexa  = input("Enter a Hexadecimal : ")
    val = int(hexa, 10)
    val = str(val)


def hex2oct():
    menu()


def banner():
    #os.system("clear")
    print('\t\t\t😎 EasyConverter! 😎\n\n')


def menu():
    print("|========================|")
    print("|😊 Choose your option 😊|\n|========================|\n")
    print("Press 1 to convert Binary to Decimal \n")
    print("Press 2 to convert Binary to Octal  \n")
    print("Press 3 to convert Binary to Hexadecimal \n")
    print("Press 4 to convert Decimal to  Binary \n")
    print("Press 5 to convert Decimal to  Octal \n")
    print("Press 6 to convert Decimal to  Hexadecimal \n")
    print("Press 7 to convert Octal to Binary \n")
    print("Press 8 to convert Octal to Decimal \n")
    print("Press 9 to convert Octal to Hexadecimal  \n")
    print("Press 10 to convert Hexadecimal to Binary \n")
    print("Press 11 to convert Hexadecimal to Decimal \n")
    print("Press 12 to convert Hexadecimal to Octal  \n")
    print("Press 0 to  Exit\n\n")
    print("SORRY FOR THE INCONVIENCE\nLast two option will not work for now this will be fixed soon ")
    print()
    ch = int(input("\t\tEnter your option:  "))
    os.system("clear")
    if ch == 1:
        bin2deci()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 2:
        bin2oct()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 3:
        bin2hex()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 4:
        deci2bin()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 5:
        deci2oct()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 6:
        deci2hex()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 7:
        oct2bin()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 8:
        oct2deci()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 9:
        oct2hex()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 10:
        hex2bin()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 11:
        hex2deci()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 12:
        hex2oct()
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()
    elif ch == 0:
        print("👋 BYE BYE 👋")
        exit()
    else:
        print("Invalid")
        c = input("press + to continue!: ")
        if c == "+":
            menu()
        else:
            exit()


banner()
menu()
