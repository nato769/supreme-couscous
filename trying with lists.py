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
    "M $26.50 / L $33.00",
    "$29.50",
    "$26.50",
    "$25.50",
    "$22.50",
    "$22.50",
    "S $22.50 / D $32.50",
    "$29.00",
    "$30.00",
    "$6",
    "$7",
    "$7.50",
    "$6.50",
    "$8.00",
    "$8.50",
    "$8.50",
    "$8.50",
    "$8.50",
]
for i in range(0,17):
    print((i+1), ".", item[i], "|", descript[i], "|", opt[i], "|", cost[i], )
'''iorb = ("Would you like to ")
print(iorb)'''
if iorb == "y":
    while True:
        try:
            y = int(input("What item would you like to see in detail? "))
            x = y-1
            if x <=-1:
                print("please input an integer from 1 to 17")
                continue

            print(item[x], "|", descript[x], "|", opt[x], "|", cost[x], )
        except:
            print("please input an integer from 1 to 17")
root.mainloop()
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
