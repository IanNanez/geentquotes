def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox861647c9ee8d474e950bb188c549808b.mailgun.org/messages",
        auth=("api", "key-4df658831a75f41a44941ed2d7aa39f9"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox861647c9ee8d474e950bb188c549808b.mailgun.org>",
              "to": "Ian Nanez <inaneze@gmail.com>",
              "subject": "Hello Ian Nanez",
              "text": "Congratulations Ian Nanez, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message
