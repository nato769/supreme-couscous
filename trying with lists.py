from tkinter import *
root =Tk()
root.title("Error")
root.geometry("720x360")
frame = Frame(root)
label = Label(frame, text="All of the food and drinks have sold out due to popular demand. Please come back tomorrow. \n We are sorry for any inconvenience that this may have caused.")
frame.pack()
label.pack()
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
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Only one option",
    "Coke/L&P/Sprite/Ginger Beer/Tonic Water/ Lime and soda/Lemon Lime and Bitters",
    "Ginger Beer/ Feijoa and Pear/ Mandarin/ Lime and Bitters/ Lemon and Rhubarb",
    "Regular or sugar free",
    "Orange/Apple/Cranberry/Pineapple/Tomato/Mango/Peach",
    "Blackcurrent/Passionfruit",
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
receipt = []
cost_stuff = []
hjk=0
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
for i in range(0,17):
    print((i+1), ".", item[i], "|", descript[i], "|", opt[i], "| $", cost[i], )
iorb = input("\nWould you like to buy any items? b for buying items and d for looking in detail ")
print(iorb)
if iorb == "d":
    while True:
        try:
            x = int(input("What item would you like to see in detail? "))
            y = x-1
            if x == 0:
                False
            if y <=-1:
                print("please input an integer from 1 to 17")
                continue

            print(item[x], "|", descript[x], "|", opt[x], "|", cost[x], )
        except:
            print("f please input an integer from 1 to 17")
elif iorb == "b":
    print("This is the system for buying items. "
          "\nYou can pick any integer from 1 to 4 for the amount of each item. "
          "\nSay buy or nothing in options to continue to the buying stage."
          "\nSay order to see all of the items on your current order. "
          "\nSay finish when you have added all items to your order."
          "\nSay cancel if you want to cancel the whole order.")
    while True:
        try:
            kys = 0
            o = str(input("What option would you like to use? "))
            if o == "cancel":
                c = str(input("Are you sure you want cancel your whole order?\nThis action can not be undone.\nSay yes or no "))
                if c == "yes":
                    print("cancelling order")
                    receipt = []
                    cost_stuff = []

                elif c == "no":
                    continue
                else:
                    print("please say yes or no")
            elif o == "order":
                print("printing current order")
                for i in receipt:
                    print(i)
                    continue
            elif o == "finish":
                c = str(input("Are you sure you want to finish your order? Say yes or no "))
                if c == "yes":
                    print("finishing order")
                    break
                elif c == "no":
                    continue
                else:
                    print("please say yes or no")
            elif o == "" or o == "buy":
                print("buying stage")
                x = int(input("What item would you like to buy? "))
                kys=1
            else:
                print("please choose a valid option")
                continue
            y = x - 1
            if y <= -1:
                print("please input an integer from 1 to 17")
                continue
            if y >= 17:
                print("please input an integer from 1 to 17")
                continue
            if kys == 1:
                a = int(input("How many of that item would you like? "))
            else:
                continue
            b = a - 1
            if b <= -1:
                print("please input an integer from 1 to 4")
                continue
            if b >= 10:
                print("please input an integer from 1 to 4")
                continue
            print(item[x],"x",(a),"\nadded to order")
            f = float(cost[x])*(a)
            print("cost for that amount of the item $", f)
            p = item[x],'x',(a), cost[x]
            cost_stuff.append(f)
            receipt.append(p)
            hjk=1


            #if (str(input("would you like to finish your order?"))) == "finish order":



        except:
            print("f please input an integer from 1 to 17 or a valid option")
else: print("cringe")

if hjk==1:
    print("printing receipt")
    for i in receipt:
        print(i)
    q = 0
    for i in cost_stuff:
        q = q + i
    print("The final cost of everything is $",q)
    root.mainloop()
'''for i in range(ui('int', 'what item? ')):
    list2.append(ui('int', "how many items?"))
    continue'''
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
'''try:
  print(x)
except:
  print("An exception occurred")'''
