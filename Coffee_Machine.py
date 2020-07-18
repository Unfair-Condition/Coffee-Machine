# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:47:13 2020

@author: HP
"""

water=400
milk=540
coffee=120
disposable=9
money=550     
def buy(i):
    i=int(i)
    
    
    
    global water
    global milk
    global coffee
    global disposable
    global money
    if i==1:
        if water-250<0:
            
            print("Sorry, not enough water!")
        elif coffee-16<0:
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            water=water-250
            milk=milk-0
            coffee=coffee-16
            money=money+4
            disposable=disposable-1
    elif i==2:
         if water-350<0:
              print("Sorry, not enough water!")
         elif milk-75<0:
             
              print("Sorry, not enough milk!")
         elif coffee-20<0:
              print("Sorry, not enough coffee beans!")
         else:
              print("I have enough resources, making you a coffee!")
              water=water-350
              milk=milk-75
              coffee=coffee-20
              money=money+7
              disposable=disposable-1
    elif i==3:
         if water-200<0:
              print("Sorry, not enough water!")
         elif milk-100<0:
              print("Sorry, not enough milk!")
         elif coffee-12<0:
              print("Sorry, not enough coffee beans!")
         else:
              print("I have enough resources, making you a coffee!")
              water=water-200
              milk=milk-100
              coffee=coffee-12
              money=money+6
              disposable=disposable-1
    return action()         
              
              
              
def rem():
    
    print("The coffee machine has:")
    print(str(water)+" of water")
    print(str(milk)+" of milk")
    print(str(coffee)+" of coffee beans")
    print(str(disposable)+" of disposable cups")
    print("$"+str(money)+" of money") 
    return action()
    
def fill():
    global water
    global milk
    global coffee
    global disposable
    global money
    p=int(input("Write how many ml of water do you want to add:\n"))
    q=int(input("Write how many ml of milk do you want to add:\n"))
    t=int(input("Write how many grams of coffee do you want to add:\n"))
    s=int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water=p+water
    milk=q+milk
    coffee=coffee+t
    disposable=disposable+s
    
    return action()
    
def take():
    return print("I gave you "+"$"+str(money))
    
        

def action():
    print("Write action (buy, fill, take, remaining, exit):")
    x=input()
    
    while x!='exit':
        
        if x=='buy':
            
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            i=input()
            if i=='back':
                
                return action()
            else:
                
                return buy(i)
        if x=='remaining':
             return rem()
        if x=='fill':
            return fill()
        if x=='take':
            return take()
        if x=='exit':
            break
        
action()        
         
       
             
             