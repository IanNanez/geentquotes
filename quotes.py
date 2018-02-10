def send_simple_message():
    return requests.post(
        "hehehe",
        auth=("api", "hehehe"),
        data={"from": "Mailgun Sandbox <hehehe>",
              "to": "hehehe <hehehe>",
              "subject": "Hello heheh",
              "text": "Congratulations hehehe, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message
