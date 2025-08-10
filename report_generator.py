# -*- coding: utf-8 -*-

def generate_mission_summary(missions):
    """
    Generates a summary report for a list of missions.

    Args:
        missions (list): A list of dictionaries, where each dictionary represents a mission
                         and must contain a "status" key.

    Returns:
        str: A formatted string containing the mission summary.
    """
    if not isinstance(missions, list):
        return "Error: Input must be a list of missions."

    total = len(missions)
    # Count missions with "Active" status
    active = len([m for m in missions if m.get("status") == "Active"])
    # Count missions with "Complete" status
    complete = len([m for m in missions if m.get("status") == "Complete"])
    pending = total - active - complete

    # Create the report using an f-string for easy formatting
    report = f"""
=== MISSION INTELLIGENCE SUMMARY ===
Total Missions: {total}
Active Missions: {active}
Completed Missions: {complete}
Pending Missions: {pending}
==================================
"""
    return report.strip()

def generate_personnel_report(personnel):
    """
    Generates a summary report for a list of personnel.

    Args:
        personnel (list): A list of dictionaries, where each dictionary represents a person
                          and must contain a "clearance" key.

    Returns:
        str: A formatted string containing the personnel summary.
    """
    if not isinstance(personnel, list):
        return "Error: Input must be a list of personnel."

    total = len(personnel)
    # Count personnel with "Top Secret" clearance
    top_secret = len([p for p in personnel if p.get("clearance") == "Top Secret"])
    regular = total - top_secret

    # Create the report using an f-string
    report = f"""
=== PERSONNEL SUMMARY ===
Total Personnel: {total}
Top Secret Clearance: {top_secret}
Regular Clearance: {regular}
========================
"""
    return report.strip()

def export_data_to_file(data, filename):
    """
    Exports processed data (like a report string) to a file.

    Args:
        data (str): The data to be written to the file.
        filename (str): The name of the file to save the data to.

    Returns:
        str: A confirmation message indicating the export was successful.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(data))
        return f"Data exported successfully to {filename}"
    except IOError as e:
        return f"Error exporting data to {filename}: {e}"

# This block of code will only run when the script is executed directly
if __name__ == "__main__":
    # --- Example Usage ---

    # 1. Sample data for missions and personnel
    sample_missions = [
        {"name": "Alpha", "status": "Active"},
        {"name": "Bravo", "status": "Active"},
        {"name": "Charlie", "status": "Complete"},
        {"name": "Delta", "status": "Complete"},
        {"name": "Echo", "status": "Complete"},
        {"name": "Foxtrot", "status": "Pending"},
    ]

    sample_personnel = [
        {"id": "001", "clearance": "Top Secret"},
        {"id": "002", "clearance": "Regular"},
        {"id": "003", "clearance": "Regular"},
        {"id": "004", "clearance": "Top Secret"},
        {"id": "005", "clearance": "Regular"},
    ]

    # 2. Generate the reports
    mission_report = generate_mission_summary(sample_missions)
    personnel_report = generate_personnel_report(sample_personnel)

    # 3. Print the reports to the console
    print(mission_report)
    print("\n" + "="*30 + "\n") # Separator
    print(personnel_report)

    # 4. Export the combined reports to a file
    combined_report = f"{mission_report}\n\n{personnel_report}"
    export_message = export_data_to_file(combined_report, "summary_report.txt")
    print("\n" + "="*30 + "\n") # Separator
    print(export_message)
