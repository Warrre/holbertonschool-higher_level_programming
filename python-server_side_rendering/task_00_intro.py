#!/usr/bin/env python3
"""Simple templating: generate invitation files from a template and data list.

Function: generate_invitations(template, attendees)

Behavior:
 - Validate input types
 - Handle empty template or empty attendees list with specific messages
 - Replace placeholders {name}, {event_title}, {event_date}, {event_location}
   using "N/A" for missing or None values
 - Write files output_1.txt, output_2.txt, ... and attempt to set reasonable
   file permissions (best-effort; may be no-op on some platforms)
"""
from typing import List, Dict
import os


def generate_invitations(template: str, attendees: List[Dict]):
    """Generate invitation files from a template and a list of attendee dicts.

    Args:
        template (str): The template string containing placeholders
                          {name}, {event_title}, {event_date}, {event_location}.
        attendees (list): List of dictionaries containing the fields above.

    Behavior:
        - If template is not a string, prints an error with the actual type and returns.
        - If attendees is not a list of dicts, prints an error with the actual type and returns.
        - If template is empty (after stripping), prints
          "Template is empty, no output files generated." and returns.
        - If attendees is empty list, prints
          "No data provided, no output files generated." and returns.
        - For each attendee, missing or None values are replaced with "N/A".
        - Writes files named output_1.txt, output_2.txt, ... in the current dir.
    """
    # Type checks
    if not isinstance(template, str):
        print(f"Invalid template type: {type(template).__name__}, expected str.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Invalid attendees type: {type(attendees).__name__}, expected list of dicts.")
        return

    # Empty checks
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")

    for idx, attendee in enumerate(attendees, start=1):
        # Build substitution dictionary; missing or None -> "N/A"
        subs = {}
        for key in placeholders:
            val = attendee.get(key) if isinstance(attendee, dict) else None
            subs[key] = val if val is not None else "N/A"

        # Perform replacements. Use simple replace to avoid unexpected format errors
        # if the template contains characters that would break str.format.
        content = template
        try:
            for key, val in subs.items():
                content = content.replace("{" + key + "}", str(val))
        except Exception as e:
            print(f"Error processing attendee #{idx}: {e}")
            continue

        filename = f"output_{idx}.txt"

        try:
            # If file exists, we overwrite it but warn the user
            if os.path.exists(filename):
                # Overwrite but inform
                print(f"Warning: {filename} exists and will be overwritten.")

            with open(filename, "w", encoding="utf-8") as fh:
                fh.write(content)

            # Best-effort set permission to rw-r--r-- (0o644). On Windows this may
            # not have the same effect; ignore errors silently.
            try:
                os.chmod(filename, 0o644)
            except Exception:
                pass

        except Exception as e:
            print(f"Error writing file {filename}: {e}")


if __name__ == "__main__":
    # quick local test when running this module directly
    try:
        with open(os.path.join(os.path.dirname(__file__), "template.txt"), "r", encoding="utf-8") as f:
            tpl = f.read()
    except Exception:
        tpl = "Hello {name},\n\nYou are invited to the {event_title} on {event_date} at {event_location}.\n\nBest regards,\nEvent Team\n"

    attendees_example = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
    ]

    generate_invitations(tpl, attendees_example)
