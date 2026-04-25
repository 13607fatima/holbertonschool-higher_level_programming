def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string. Provided: {}"
              .format(type(template).__name__))
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict)
                                                  for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, 1):
        processed_template = template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            placeholder = "{" + key + "}"
            processed_template = processed_template.replace(placeholder, value)

        filename = "output_{}.txt".format(i)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(processed_template)
