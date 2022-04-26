import os
import sys
from colorama import init, Fore, Back, Style

init()
def menu():
    print(Style.BRIGHT + Fore.WHITE)
    print("█───██─███──█──█──█──██")
    print("██─███─█────█──█──█─█──█")
    print("█─█─██─███──████──████─█")
    print("█───██─█────█──█──█─█──█")
    print("█───██─███──█──█──█──██")
    print("""
    1. Порахувати вартiсть комуналки!
    2. Подивитися данi по мiсяцях(В РОЗРОБЦІ)!
    3. Вихiд
    """)
menu()    
choice = input("\nВиберiть дiю: ")

def back_to_menu():
    print(Style.BRIGHT + Fore.WHITE)
    print("""1. Закрити програму\n2. Зберегти дані про оплату""")

def back_to_menu_key():   
    if choice == "1":
        print("Дякую за використання програми")
        exit
    elif choice == "2":
        f = open(Month +".txt", 'w')
        gas_write = (f"Газ: {Gas} грн.")
        gas_roz_write = (f"\n\nГазрозподіл: {Gas_roz} грн. ")
        electricity_write = (f"\n\nЕлектроенергія: {Electricity} грн. ")
        internet_write = (f"\n\nІнтернет: {Internet} грн. ")
        general_sum_write = (f"\n\n\nСума до сплати: {sum} грн. ")
        f.write(gas_write)
        f.write(gas_roz_write)
        f.write(electricity_write)
        f.write(internet_write)
        f.write(general_sum_write)
        f.close()
        print("Дані збереженно у файл:",Month +".txt")
        
        
if choice == "1": 

    Month= input("\nВведiть назву мiсяця: ")
    Gas = float(input("Оплата за Газ: " ))
    Gas= str(Gas)
    Gas_roz = float(input("Оплата за Газрозподiл: " ))
    Gas_roz = str(Gas_roz)
    Electricity = float(input("Оплата за Електроенергiю: " ))
    Electricity = str(Electricity)
    Internet = float(input("Оплата за Iнтернет: " ))
    Internet = str(Internet)
    Gas_sum = float(Gas)
    Gas_roz_sum = float(Gas_roz)
    Electricity_sum = float(Electricity)
    Internet_sum = float(Internet)
    
    sum = (Gas_sum + Gas_roz_sum + Electricity_sum + Internet_sum )
    print(Style.BRIGHT + Fore.GREEN)
    print('\nДо оплати:' , sum,  "грн." )
    back_to_menu()
    choice = input("\nВиберiть дiю: " )
    back_to_menu_key()
    
#elif choice == "2":
    #pass