#random tkinter stuff that doesnt really do anything except an error screen and text saying it doesnt work.
#it takes no input from the user and i cant really remember how it works but it does and thats the main thing.
from tkinter import *
root =Tk()
root.title("Error")
root.geometry("720x360")
frame = Frame(root)
label = Label(frame, text="All of the food and drinks have sold out due to popular demand. Please come back tomorrow. \n We are sorry for any inconvenience that this may have caused.")
frame.pack()
label.pack()
#now comes the fun bit with a of the info on everything stored in lists or 2d arrays
#this includes the item names (item), their descriptions (descript), options for the items (opt), cost of the items (cost)
item = [
    "Blue Cod Fillets",
    "Chicken Breast",
    "Mixed Grill",
    "New Zealand Ham Steak",
    "Homemade Pie",
    "Crumbed Schnitzel",
    "Lamb Shank(s)",
    "Rib Eye Steak",
    "Pork Belly",
    "Soft Drinks",
    "Mac's Range",
    "Red Bull",
    "Fruit Juices",
    "Sparkling Juice",
    "Tropicana",
    "Red Peach",
    "Citrus Burst",
    "Mango Madness",
]
descript = [
    "Homemade Beer Batter OR Pan-fried W lemon butter. Served W French fries A salad & Tartare sauce.",
    "Oven baked Chicken W melted brie, cranberries & wrapped in streaky bacon. Served with pea puree & plum sauce. With Vegetables OR French fries & Salad",
    "Bacon,Sausages, Eggs, Onions, Peppered Tomato, Schnitzel, Mushrooms & French fries",
    "Prime Cut Ham served W pineapple salsa, grilled tomato, fried egg . Served w French fries & salad.",
    "Our delicious homemade Pie. Served W creamy mash, mushy peas & Kumara chips. Check Blackboard for today's special",
    "Served with Red Wine Gravy & Vegetables.",
    "Slow cooked with onion, tomato, bay leaves, red wine & rosemary, placed on creamy mash.",
    "Served W French Fries & Salad. Grilled to your liking",
    "Five Spice Pork belly slow cooked with malt vinegar' & bourbon glaze Served on pumpkin mash W crispy crackling & kumara chips and Vegetables",
    "See Options",
    "See Options",
    "See Options",
    "See Options",
    "See Options",
    "Orange cranberry and pineapple juice with a delicious layer of passionfruit puree",
    "Peach nectar lemonade grenadine and fresh lemon juice",
    "Mango nectar orange juice and apple juice",
    "Mango nectar cranberry juice and fresh lime",
]
opt = [
    ["Medium", "Large"],
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    ["Single", "Double"],
    "Only one option",
    "Only one option",
    ["Coke" ,"L&P", "Sprite","Ginger Beer", "Tonic Water", "Lime and soda", "Lemon Lime and Bitters"],
    ["Ginger Beer", "Feijoa and Pear", "Mandarin", "Lime and Bitters", "Lemon and Rhubarb"],
    ["Regular", "sugar free"],
    ["Orange", "Apple", "Cranberry", "Pineapple", "Tomato", "Mango", "Peach"],
    ["Blackcurrent", "Passionfruit"],
    "Only one option",
    "Only one option",
    "Only one option"
]
cost = [
    ["26.50", "33.00"],
    "29.50",
    "26.50",
    "25.50",
    "22.50",
    "22.50",
    ["22.50", "32.50"],
    "29.00",
    "30.00",
    "6",
    "7",
    "7.50",
    "6.50",
    "8.00",
    "8.50",
    "8.50",
    "8.50",
    "8.50",
]
#this list is so the system can check if there is more than one option which needs another input from the user
optyn = [
    "Y",
    "N",
    "N",
    "N",
    "N",
    "N",
    "Y",
    "N",
    "N",
    "Y",
    "Y",
    "Y",
    "Y",
    "Y",
    "N",
    "N",
    "N",
]
#these are the empty lists to be filled later for the receipt/order and the cost at the end
receipt = []
cost_stuff = []
#this is another silly thing i have bc it was the first solution that came to mind and it worked so i didnt change it
hjk=0
#this is a function that i never used but its there and thats what matters
def ui(data_type,data):
    while True:
        try:
            if data_type=='int':
                i = int(input(data))
            elif data_type=='str':
                i = input(data)
            break
        except:
            print("please input an iteger from 1 to 17")
    return i
#a handy guide to help with working out which one is which i guess
print("number . item | description | options | cost")
#this is the main menu that you see at the start
#i took every item in each list and printed them together
#theres also some number and symbol shenanigans to make it look nicer
for i in range(0,17):
    print((i+1), ".", item[i], "|", descript[i], "|", opt[i], "| $", cost[i], )
#asking for input b or d, for buy and looking in detail respectively. anything else and it will just print cringe and stop
iorb = input("\nWould you like to buy any items? b for buying items and d for looking in detail ")
#spits your input back at you
print(iorb)
#if it is d
if iorb == "d":
    #just a loop that goes forever
    while True:
        #the thing that makes it restart
        try:
            #input from user about what item they want to see in detail expecting integer from 1 to 17
            x = int(input("What item would you like to see in detail? "))
            #list shenanigans that could probably be done better
            y = x-1
            if x == 0:
                False
            #checking if the input is correct
            if y <=-1:
                print("please input an integer from 1 to 17")
                continue

            #printing out item that is called for
            print(item[y], "|", descript[y], "|", opt[y], "|", cost[y], )
        #if error then try again
        except:
            print("f please input an integer from 1 to 17")
#else if you want to buy
elif iorb == "b":
    #lots of text that people need to read
    print("This is the system for buying items. "
          "\nYou can pick any integer from 1 to 4 for the amount of each item. "
          "\nSay buy or nothing in options to continue to the buying stage."
          "\nSay order to see all of the items on your current order. "
          "\nSay finish when you have added all items to your order."
          "\nSay cancel if you want to cancel the whole order.")
    #forever loop
    while True:
        try:
            #another silly little variable to stop things going into the wrong part later
            kys = 0
            #asking for options aka funny string inputs
            o = str(input("What option would you like to use? "))
            #cancel option
            if o == "cancel":
                #are you sure? expected answer yes or no
                c = str(input("Are you sure you want cancel your whole order?\nThis action can not be undone.\nSay yes or no "))
                if c == "yes":
                    print("cancelling order")
                    #setting everything to 0 again
                    receipt = []
                    cost_stuff = []
                #just goes back to options again if no
                elif c == "no":
                    continue
                else:
                    #expected answers not given
                    print("please say yes or no")
            #option to look at the current order
            elif o == "order":
                print("printing current order")
                #just printing the whole order
                for i in receipt:
                    print(i)
                    continue
            #finish option
            elif o == "finish":
                #are you sure about that? string input yes or no
                c = str(input("Are you sure you want to finish your order? Say yes or no "))
                if c == "yes":
                    print("finishing order")
                    #breaks out to the finishing stuff outside of the loop
                    break
                #back to options again
                elif c == "no":
                    continue
                else:
                #not expected answer
                    print("please say yes or no")
            #buying option
            elif o == "" or o == "buy":
                print("buying stage")
                #input from user about what item they would like to buy. expected answers integer from 1 to 17
                x = int(input("What item would you like to buy? "))
                #this variable makes it so it goes to the correct next stage
                kys=1
            else:
                #not expected value for the options asks for input again
                print("please choose a valid option")
                continue
            #making sure it is a valid integer for the system
            y = x - 1
            if y <= -1:
                print("please input an integer from 1 to 17")
                continue
            if y >= 17:
                print("please input an integer from 1 to 17")
                continue
            #no stumbling in here without choosing an item to buy first
            if kys == 1:
                #checking for food/drink options
                if optyn[y] == "Y":
                    #prints the options if they exist
                    print("options -", opt[y])
                    #asks for which option the user would like. expecting integer in the range of 1 to the amount of options
                    copt = int(input("what option would you like? (choose an integer) "))
                    #sneaky options in cost make the code need to be different for 1 and 7
                    if x == 1 or x == 7:
                        print(copt, "\n", opt[y][(copt-1)], "\nprice - $", cost[y][copt-1])
                    else:
                        #if not 1 and 7 then just run this
                        print(copt, "\n", opt[y][(copt-1)], "\nprice - $", cost[y])
                else:
                    #i cant remember why i put this here
                    kys = 1

            #again no coming here if you havent already chosen what you want to buy
            if kys == 1:
                #asking for how many of that item expecting integer between 1 and 4
                a = int(input("How many of that item would you like? "))
                #list shenanigans
                b = a - 1
                #is it valid
                if b <= -1:
                    print("please input an integer from 1 to 4")
                    continue
                if b >= 4:
                    print("please input an integer from 1 to 4")
                    continue
            else:
                continue
            #even more list shenanigans
            b = a - 1
            if b <= -1:
                #is it valid
                print("please input an integer from 1 to 4")
                continue
            if b >= 4:
                print("please input an integer from 1 to 4")
                continue
            #prints what you have chosen to order and the amount of it
            print(item[x],"x",(a),"\nadded to order")
            # works out the cost of that amount of that item
            #more 1 and 7 being annoying and breaking it so fixing that
            if x == 1 or x == 7:
                f = float(cost[y][copt-1])*a
            else:
                #if not 1 or 7 do this
                f = (float(cost[y]))*a
            #print the cost for that amount for that item
            print("cost for that amount of the item $", f)
            #even more 1 and 7 being annoying
            if y == 1 or y == 7:
                p = item[y],'x',(a),opt[y][copt],  cost[y]
            else:
                p = item[y],'x',(a), cost[y]
            #adds it to the cost list
            cost_stuff.append(f)
            #adds it to the receipt/order
            receipt.append(p)
            #variable that makes it so you cant finish without ordering
            hjk=1
        #the annoying thing that i cant take out but still useful because it returns you to the start if an error occurs
        except:
            #has the f so i know its an error as compared to the out of range checks
            print("f please input an integer from 1 to 17 or a valid option")
#having a try loop would be tedious here so it just says cringe and pouts
else: print("cringe")

#checking if the user has actually ordered anything
if hjk==1:
    print("printing receipt")
    #prints receipt
    for i in receipt:
        print(i)
    #relic of testing that doesnt stop anything so i left it in i think
    q = 0
    #finding the total cost
    for i in cost_stuff:
        q = q + i
    #printing the total cost
    print("The final cost of everything is $",q)
    #gives the gui from tkinter. i had to do it at the end because otherwise the code doesnt run until you close the window
    root.mainloop()
#ui stuff that i didnt use
'''for i in range(ui('int', 'what item? ')):
    list2.append(ui('int', "how many items?"))
    continue'''
#old system that i should probably get rid of
while True:
        '''try:
            a = int(input("What item would you like to buy more of? "))
            b = a-1
            if x <=-1:
                print("please input an integer from 1 to 17 for the item")
                continue

            print("deez")
            print("buying", (iorb), "of item", (y))
        except:
            print("please input an integer from 1 to 17")'''
#working out the try except stuff from the tic tac toe project
'''
        try:
            x = int(input("enter your row"))
            y = int(input("enter your column"))
            if x <= 3 and y <= 3:
                break
                a = False
                print("computer is not happy with you, try picking a integer from 1 to 3")
            row = int(x - 1)
            column = int(y - 1)
            while board[row][column] != " ":
                break
                print("that space is already taken")
        except:
            print("computer is not happy with you, try picking a integer from 1 to 3")

'''
#try except example from w3schools
'''try:
  print(x)
except:
  print("An exception occurred")'''
