# ask for today's input
# append data to habits.csv 
# prevent duplicate dates
# validate simlpe input

import csv
from datetime import datetime

def get_today_input():
    today = datetime.now().strftime("%m-%d-%Y")
    print(f"Today's date: {today}")
    
    # Check if today's date already exists in the CSV
    with open('streak-engine/data/habits.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == today:
                print("Today's data already exists. No duplicate entries allowed.")
                return
    
    # Get user input for today's habits
    habit_inputs = []
    coding_hrs = input("Enter hours spent coding today: ")
    topic_studied = input("Enter the topic you studied today: ")
    workout = input("Did you workout today? (yes/no): ")
    reading_pages = input("Enter the number of pages you read today: ")
    sleep_hrs = input("Enter hours of sleep you had last night: ")
    mood = input("How was your mood today? (good/bad/neutral): ")
    habit_inputs.extend([coding_hrs, topic_studied, workout, reading_pages, sleep_hrs, mood])
    
    # Validate input (simple validation to check if it's not empty)
    for input_value in habit_inputs:
        if not input_value.strip():
            print("Input cannot be empty. Please try again.")
            return
    
    # Append today's data to the CSV
    with open('streak-engine/data/habits.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([today] + habit_inputs)
    
    print("Today's habits have been recorded successfully.")

if __name__ == "__main__":
    get_today_input()

