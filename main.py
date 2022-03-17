from tkinter import *
root =Tk()
root.title("Error")
root.geometry("720x360")
frame = Frame(root)
label = Label(frame, text="All of the food and drinks have sold out due to popular demand. Please come back tomorrow. \n We are sorry for any inconvenience that this may have caused.")
frame.pack()
label.pack()
items = {
    "food 0": "Blue Cod Fillets",
    "food 1": "Chicken Breast",
    "food 2": "Mixed Grill",
    "food 3": "New Zealand Ham Steak",
    "food 4": "Home -made Pie",
    "food 5": "Crumbed Schnitzel",
    "food 6": "Lamb Shank(s)",
    "food 7": "Rib Eye Steak",
    "food 8": "Pork Belly",
    "drink a": "Soft Drinks",
    "drink b": "Mac's Range",
    "drink c": "Red Bull",
    "drink d": "Fruit Juices",
    "drink e": "Sparkling Juice",
    "drink f": "Tropicana",
    "drink 6": "Red Peach",
    "drink 7": "Citrus Burst",
    "drink 8": "Mango Madness",
}
descript = {
    "descript 0": "Homemade Beer Batter OR Pan-fried W lemon butter. Served W French fries A salad & Tartare sauce.",
    "descript 1": "Oven baked Chicken W melted brie, cranberries & wrapped in streaky bacon. Served with pea puree & plum sauce. With Vegetables OR French fries & Salad",
    "descript 2": "Bacon,Sausages, Eggs, Onions, Peppered Tomato,Schnitzel, Mushrooms & French fries",
    "descript 3": "Prime Cut Ham served W pineapple salsa, grilled tomato, fried egg . Served w French fries & salad.",
    "descript 4": "Our delicious homemade Pie. Served W creamy mash, mushy peas & Kumara chips. Check Blackboard for today's special",
    "descript 5": "Served with Red Wine Gravy & Vegetables.",
    "descript 6": "Slow cooked with onion, tomato, bay leaves, red wine & rosemary, placed on creamy mash.",
    "descript 7": "Served W French Fries & Salad. Grilled to your liking",
    "descript 8": "Five Spice Pork belly slow cooked with malt vinegar' & bourbon glaze Served on pumpkin mash W crispy crackling & kumara chips and Vegetables",
}
#print(name["food 5"], descript["descript 5"])
root.mainloop()