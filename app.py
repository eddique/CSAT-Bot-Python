from crypt import methods
from statistics import pstdev
from flask import Flask, request, Response, render_template
from jira import JIRA
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
import os
import json
from pathlib import Path
from dotenv import load_dotenv

client  = WebClient(token = os.getenv("SLACK_TOKEN"))
#jira = JIRA(server=os.getenv("JIRA_URL"), basic_auth=(os.getenv("JIRA_USERNAME"), os.getenv("JIRA_TOKEN")))
#slack_event = SlackEventAdapter(os.getenv("SIGNING_SECRET"), "/slack/events", app)

app = Flask(__name__)

@app.route("/slack/button-event", methods=["POST"])
def button_event():
    data = request.form.to_dict()
    payload = json.loads(data["payload"])
    user_id = payload.get("user", {}).get("id")
    channel_id = payload.get("channel", {}).get("id")
    button_value = payload.get("actions", [])[0].get("value")

    if button_value == "csat_submit":
        pass
    elif button_value == "csat_cancel":
        pass

    return Response(), 200

@app.route("/jira/issue-updated", methods=["GET", "POST"])
def jira_update():
    payload = request.json()
    event_type = payload["issue_event_type_name"]
    
    if event_type == "issue_closed":
        #issue = jira.issue(payload["issue"].get("id"))
        #reporter = issue.get_field("reporter")
        #slack_id = client.users_lookupByEmail(email=reporter.emailAddress)

        # send slack message to user
        #client.chat_postMessage(channel=f"@{slack_id}", text="hello!")
        pass
        
    return Response(), 200

@app.route("/")
def home_view():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)