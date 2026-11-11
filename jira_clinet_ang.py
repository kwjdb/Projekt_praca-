from datetime import date

import requests

class JiraClient():
    def __init__(self, token, mail, domain = "https://hubert-python-dev.atlassian.net"):
        self.token = token
        self.mail = mail
        self.domain = domain.rstrip('/')
        self.auth = (self.mail, self.token)
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


    def create_ticket(self, project_key = "KAN", summary="", description=""):
        url = f"{self.domain}/rest/api/3/issue"
        if summary == "":
            today = date.today()
            summary = f"rate entry for day {today}"

        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": description,
                "issuetype": {"name": "Task"}
            }
        }
        response = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
        if response.status_code != 201:
            raise ValueError(f"failed to create ticket in jira Status: {response.status_code}, Content: {response.text}")
        processed_response = response.json()
        print(processed_response)
        return processed_response["key"]


    def add_attachment(self, file_path, ticket_key):
        url = f"{self.domain}/rest/api/3/issue/{ticket_key}/attachments"
        file_headers = {"X-Atlassian-Token": "no-check"}
        files = {"file": open(file_path, 'rb')}
        response = requests.post(url, auth=self.auth, headers=file_headers, files=files)
        if response.status_code != 200:
            raise ValueError(f"failed to add attachment: {response.status_code}, Content: {response.text}")
        else:
            print(response.json())


    def delete_all_tickets(self, project_key="KAN"):
        url = f"{self.domain}/rest/api/3/search/jql?jql=project={project_key}"
        response = requests.get(url, auth=self.auth)
        if response.status_code != 200:
            raise ValueError(f"failed to fetch existing tickets: {response.status_code}, Content: {response.text}")
        issues_list = response.json()["issues"]
        for item in issues_list:
            ticket_id = item['id']
            url = f"{self.domain}/rest/api/3/issue/{ticket_id}"
            response = requests.delete(url, auth=self.auth)
            if response.status_code != 204:
                raise ValueError(
                    f"failed to delete ticket with id:{ticket_id}, status code: {response.status_code}")






