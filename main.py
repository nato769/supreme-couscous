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
    "drink g": "Red Peach",
    "drink h": "Citrus Burst",
    "drink i": "Mango Madness",
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
    "descript a": "See Options",
    "descript b": "See Options",
    "descript c": "See Options",
    "descript d": "See Options",
    "descript e": "See Options",
    "descript f": "Orange cranberry and pineapple juice with a delicious layer of passionfruit puree",
    "descript g": "Peach nectar lemonade grenadine and fresh lemon juice",
    "descript h": "Mango nectar orange juice and apple juice",
    "descript i": "Mango nectar cranberry juice and fresh lime",
}
opts = {
    "opt a": "Coke/L&P/Sprite/Ginger Beer/Tonic Water/ Lime and soda/Lemon Lime and Bitters",
    "opt b": "Ginger Beer/ Feijoa and Pear/ Mandarin/ Lime and Bitters/ Lemon and Rhubarb",
    "opt c": "Regular or sugar free",
    "opt d": "Orange/Apple/Cranberry/Pineapple/Tomato/Mango/Peach",
    "opt e": "Blackcurrent/Passionfruit",
}
cost = {
    "cost 0": "M $26.50 / L $33.00",
    "cost 1": "$29.50",
    "cost 2": "$26.50",
    "cost 3": "$25.50",
    "cost 4": "$22.50",
    "cost 5": "$22.50",
    "cost 6": "S $22.50 / D $32.50",
    "cost 7": "$29.00",
    "cost 8": "$30.00",
    "cost a": "$6",
    "cost b": "$7",
    "cost c": "$7.50",
    "cost d": "$6.50",
    "cost e": "$8.00",
    "cost f": "$8.50",
    "cost g": "$8.50",
    "cost h": "$8.50",
    "cost i": "$8.50",
}

root.mainloop()