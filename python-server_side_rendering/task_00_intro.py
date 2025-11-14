#!/usr/bin/env python3
"""
This module contains a function to generate personalized invitation files.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendees list.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list")
        return
    
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Each attendee must be a dictionary")
        return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        for placeholder in placeholders:
            placeholder_key = f"{{{placeholder}}}"
            value = attendee.get(placeholder)
            
            if value is None or value == "":
                value = "N/A"
            
            invitation = invitation.replace(placeholder_key, str(value))
        
        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
            print(f"Generated {filename}")
        except Exception as e:
            print(f"Error writing {filename}: {e}")


if __name__ == "__main__":
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)
