import json
from datetime import datetime


inventory = {
    "R10k":     {"name": "Res10K", "quantity": 50, "min_stock":20}, 
    "C100N":    {"name": "C100nf", "quantity": 80, "min_stock":30},
    "REDLED":   {"name": "RedLED5mm", "quantity": 12, "min_stock":30},
    "REG7805":  {"name": "Reg7805", "quantity": 18, "min_stock":10},
    "DIOD":     {"name": "1N4007", "quantity": 120, "min_stock":50},
        }

def save_to_file():
    with open("electronics_inventory.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=4)
        print("the new list has sucessfully saved")
        
def load_from_file():
    global inventory
    try:
        with
    open("electronics_inventory.json", encoding="utf-8") as f:
            inventory = json.load(f)
        print("download from file")
    except FileNotFoundError:
        print("there is not saved file, use from recent file")
        
def show_inventory():
    print("\n"+ "="*60)
    print("number of electronic components")
    print("="*60)
    for code, item in inventory.items():
        status = "Lack of component" 
if item["quantity"]<item["min_stock"]
else:
    print(f"{code:8}| {item['name']:25} | {item['quantity']:4}| {status}")
    print("="*60)

def add_part():
    code = input("\n R1K").upper()
    name = input("name: ")
    qty = int(input("number: "))
    min_stock= int(input(" min: "))
    inventory[code] = {"name": name,"quantity": qty, "min_stock": min_stock}
    print(f"component {} has successfully aded")
def use_part():
    code = input("\n code: ").upper()
    if code in inventory:
        num = int(input (f"number : {inventory[code]['quantity']}): "))
            if num<= inventory[code] ["quantity"]:
                inventory[code]["quantity"] -= num
                print(f"{num} has used from{code}")
            else:
                print("not enough")
                
                
print("welcome")
load_from_file()

while True:
    print("\n" + "-"*50)
    print("1. display inventory")
    print("2. add new inventory")
    print("3. useing component")
    print("4.save and exit")
    choice = input("choose one")
    
    if choice == "1":
        show_inventory()
    elif choice == "2":
        add_part()
    elif choice == "3":
        use_part()
    elif choice == "4":
        save_to_file()
        print("End of program")
        break
    elase:
        print("invelid choice")
    
