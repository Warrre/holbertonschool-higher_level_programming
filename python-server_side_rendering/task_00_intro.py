def generate_invitations(template, attendees):
	if not isinstance(template, str):
		print("Error: template must be a string.")
		return
	if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
		print("Error: attendees must be a list of dictionaries.")
		return
	if not template.strip():
		print("Template is empty, no output files generated.")
		return
	if not attendees:
		print("No data provided, no output files generated.")
		return
	for index, item in enumerate(attendees):
		tmp = template
		name = item.get("name") or "N/A"
		event_title = item.get("event_title") or "N/A"
		event_date = item.get("event_date") or "N/A"
		event_location = item.get("event_location") or "N/A"

		tmp = tmp.replace("{name}", name)
		tmp = tmp.replace("{event_title}", event_title)
		tmp = tmp.replace("{event_date}", event_date)
		tmp = tmp.replace("{event_location}", event_location)

		filename = f"output_{index + 1}.txt"
		with open(filename, 'w') as f:
			f.write(tmp)
