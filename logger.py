import json

def log_query(user, bot):

    data = {
        "user": user,
        "bot": bot
    }

    with open("logs.json","a") as f:
        f.write(json.dumps(data) + "\n")