#!/bin/bash
# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    message += " that requires immediate attention today!"

# Provide a customized reminder
print(f"Reminder: {message}")

# Modify the Note for non-time-bound task
if time_bound == 'no':
    print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
