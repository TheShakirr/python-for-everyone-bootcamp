from models.donors import BloodBank, Donor
from utils.storage import DATA_PATH, load_bank, save_bank

def menu_add(bank: BloodBank) -> None:
    did = input("Donor ID: ").strip()
    name = input("Full Name: ").strip()
    bg = input("Blood Group (e.g., O+, A-): ").strip().upper()
    age_txt = input("Age: ").strip()
    
    if not did or not name or not bg or not age_txt:
        print("❌ All fields are required.")
        return
    try:
        age = int(age_txt)
    except ValueError:
        print(" Age must be a number.")
        return
        
    donor = Donor(donor_id=did, name=name, blood_group=bg, age=age)
    if bank.add(donor):
        print(" Donor Added Successfully.")
    else:
        print(" That Donor ID already exists.")

def print_donors(rows: list[Donor]) -> None:
    if not rows:
        print(" No donors registered yet.")
        return
    for d in rows:
        print(f"  {d}")

def menu_list(bank: BloodBank) -> None:
    print_donors(bank.all())

def menu_remove(bank: BloodBank) -> None:
    did = input("Donor ID to remove: ").strip()
    if bank.remove(did):
        print("Donor Removed.")
    else:
        print(" No donor found with that ID.")

def menu_search(bank: BloodBank) -> None:
    
    q = input("Search (by ID, Name, Blood Group, or Age): ").strip()
    found = bank.search(q)
    if not found:
        print(" No matches found.")
        return
    print_donors(found)

def menu_update(bank: BloodBank) -> None:
    did = input("Donor ID to update: ").strip()
    donor = bank.find_by_id(did)
    if donor is None:
        print(" No donor found with that ID.")
        return
    
    # Habkan caalamiga ah ee hoose wuxuu ilaalinaya  ID-ga rasmiga ah, 
    # wuxuuna u oggolaanayaa isticmaalaha inuu beddelo Name, Blood Group, iyo Age oo kaliya.
    new_name = input(f"New Name [{donor.name}] (Enter to keep): ").strip()
    new_bg = input(f"New Blood Group [{donor.blood_group}] (Enter to keep): ").strip().upper()
    new_age = input(f"New Age [{donor.age}] (Enter to keep): ").strip()
    
    name_arg = new_name if new_name else donor.name
    bg_arg = new_bg if new_bg else donor.blood_group
    
    if new_age:
        try:
            age_arg = int(new_age)
        except ValueError:
            print(" Invalid age; update cancelled.")
            return
    else:
        age_arg = donor.age
        
    if bank.update(did, name=name_arg, blood_group=bg_arg, age=age_arg):
        print("✅ Donor Updated.")
    else:
        print("Update failed.")

def print_menu() -> None:
    print()
    print("🩸 --- Blood Bank Management System--- 🩸")
    print("1) Add Donor")
    print("2) List All Donors")
    print("3) Remove Donor")
    print("4) Search Donors")
    print("5) Update Donor Info")
    print("6) Save to Database")
    print("0) Quit")

def main() -> None:
    bank = BloodBank()
    load_bank(DATA_PATH, bank)

    try:
        while True:
            print_menu()
            choice = input("Choice: ").strip()
            if choice == "1":
                menu_add(bank)
            elif choice == "2":
                menu_list(bank)
            elif choice == "3":
                menu_remove(bank)
            elif choice == "4":
                menu_search(bank)
            elif choice == "5":
                menu_update(bank)
            elif choice == "6":
                save_bank(DATA_PATH, bank)
                print(f" Saved to {DATA_PATH}")
            elif choice == "0":
                print(" System closed. Stay safe!")
                break
            else:
                print(" Select 0–6.")
    finally:
        try:
            save_bank(DATA_PATH, bank)
            print(f" Autopreserving data to {DATA_PATH}")
        except OSError as e:
            print("Could not save:", e)

if __name__ == "__main__":
    main()