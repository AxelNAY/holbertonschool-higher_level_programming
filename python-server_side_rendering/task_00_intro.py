#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("template needs to be a string.")
        return
    if not isinstance(attendees, list):
        print("attendess needs to be a list.")
        return
    if not template:
        print("template is empty. no output files generated.")
        return
    if not attendees:
        print("attendees is empty. no output files generated.")
        return
    
    for i, attende in enumerate(attendees, start=1):
        content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attende.get(placeholder, "N/A")
            content = content.replace(f"{{{placeholder}}}", value if value else "N/A")
        output_filename = f"output_{i}.txt"
        with open(output_filename, "w") as output_filename:
            output_filename.write(content)
        print(f"Generated {output_filename}")
    