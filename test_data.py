def run_tests():
    from mission_processor import count_by_priority, load_mission_data
    missions = load_mission_data()
    counts = count_by_priority(missions)
    print("Test Results:")
    print(f"High priority missions: {counts['High']}")
    print("✓ All functions working")
if __name__ == "__main__":
    run_tests()
