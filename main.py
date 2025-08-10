from mission_processor import load_mission_data, filter_by_status
from personnel_analyzer import load_personnel_data, filter_by_clearance
from report_generator import generate_mission_summary, generate_personnel_report


def main():
    print("=== ARMY INTELLIGENCE DATA PROCESSOR ===\n")

    # Load data
    missions = load_mission_data()
    personnel = load_personnel_data()

    while True:
        print("1. Mission Summary")
        print("2. Personnel Report")
        print("3. Filter Active Missions")
        print("4. Show Top Secret Personnel")
        print("5. Exit")

        choice = input("\nSelect option: ")

        if choice == '1':
            print(generate_mission_summary(missions))

        elif choice == '2':
            print(generate_personnel_report(personnel))

        elif choice == '3':
            active = filter_by_status(missions, "Active")
            for mission in active:
                print(f"Mission {mission['id']}: {mission['location']}")

        elif choice == '4':
            cleared = filter_by_clearance(personnel, "Top Secret")
            for person in cleared:
                print(f"{person['rank']} {person['name']} - Unit {person['unit']}")

        elif choice == '5':
            print("Session terminated.")
            break

        else:
            print("Invalid selection")
        print()


if __name__ == "__main__":
    main()
