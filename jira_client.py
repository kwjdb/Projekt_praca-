from datetime import date

import requests

class JiraClient():
    def __init__(self, token,mail,domena = "https://hubert-python-dev.atlassian.net"):
        self.token = token
        self.mail = mail
        self.domena = domena.rstrip('/')
        self.auth = (self.mail, self.token)
        self.headers = {'Content-Type': 'application/json','Accept': 'application/json'}


    def stworz_ticket(self, project_key = "KAN", summary="", description=""):
        url = f"{self.domena}/rest/api/3/issue"
        if summary == "":
            dzien = date.today()
            summary = f"zapis kursu za dzien{dzien}"

        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": description,
                "issuetype": {"name": "Task"}
            }
        }
        odpwoedz = requests.post(url, auth=self.auth, headers=self.headers, json=payload)
        if odpwoedz.status_code != 201:
            raise ValueError(f"nie udalo sie utowrzyc ticketu w jira Status: {odpwoedz.status_code}, Tresc: {odpwoedz.text}")
        odpowiedz_po_obrobce = odpwoedz.json()
        print(odpowiedz_po_obrobce)
        return odpowiedz_po_obrobce["key"]


    def dodaj_zalacznik(self,file_path, ticket_key):
        url = f"{self.domena}/rest/api/3/issue/{ticket_key}/attachments"
        headers_plik = {"X-Atlassian-Token": "no-check"}
        plik = {"file": open(file_path, 'rb')}
        odpowiedz = requests.post(url, auth=self.auth, headers=headers_plik, files=plik)
        if odpowiedz.status_code != 200:
            raise ValueError( f"nie udalo sie dodac zalacznika: {odpowiedz.status_code}, Tresc: {odpowiedz.text}")
        else:
            print(odpowiedz.json())


    def usun_wszystkie_tickety(self, project_key="KAN"):
        url = f"{self.domena}/rest/api/3/search/jql?jql=project={project_key}"
        odpwoiedz = requests.get(url, auth=self.auth)
        if odpwoiedz.status_code != 200:
            raise ValueError(f"nie udalo sie pobrac istniejacych ticketow: {odpwoiedz.status_code}, Tresc: {odpwoiedz.text}")
        slownik_z_id = odpwoiedz.json()["issues"]
        for i in slownik_z_id:
            id = i['id']
            url = f"{self.domena}/rest/api/3/issue/{id}"
            odpowiedz = requests.delete(url, auth=self.auth)
            if odpowiedz.status_code != 204:
                raise ValueError(
                    f"nie udalo sie usunac ticektu od id:{id}, status cod: {odpowiedz.status_code} ")







if __name__ == '__main__':
    with open("token.txt", "r") as token_file:
        token_my = token_file.read().strip()
    jiraklient = JiraClient(token_my,mail="hub.jatczak@gmail.com")

    # description = {
    #     "type":"doc",
    #     "version":1,
    #     "content":[
    #         {"type": "paragraph",
    #             "content":[
    #                 {"type": "text", "text": "testowy opis zgloszenia"}
    #         ]}
    #     ]
    #
    # }
    # key = jiraklient.stworz_ticket(project_key = "KAN", summary = "probny ticket", description = description)
    # jiraklient.dodaj_zalacznik(file_path = "faktury_rozliczone.xlsx", ticket_key = key)
    # czy_usunac = input("podaj czy usunac: ")
    # if czy_usunac == "1":
    jiraklient.usun_wszystkie_tickety(project_key = "KAN")

