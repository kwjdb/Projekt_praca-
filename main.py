import jira_clinet_ang
import NBP_client_ang
import excel_02_ang


def process_daily_rate(target_date=None):
    with open("token.txt", "r") as token_file:
        token_my = token_file.read().strip()
    #handling nbp
    curent_object  = NBP_client_ang.NbpClient()
    usd_object = curent_object.get_currency(code = "usd",rate_date = target_date )
    eur_object = curent_object.get_currency(code = "eur", rate_date = target_date )
    #handling excel
    date_to= usd_object.date

    #["Date", "Currency", "NBP Rate"]
    excel_02_ang.make_workbook(f"{date_to}_file.xlsx")
    excel_02_ang.append_data_load(f"{date_to}_file.xlsx",data = [date_to, usd_object.currency, usd_object.cost])
    excel_02_ang.append_data_load(f"{date_to}_file.xlsx", data=[date_to, eur_object.currency, eur_object.cost])

    #handling jira

    jira_client = jira_clinet_ang.JiraClient(token = token_my, mail="hub.jatczak@gmail.com" )
    description = {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph",
             "content": [
                 {"type": "text", "text": "daily_currency"}
             ]}
        ]

    }
    key = jira_client.create_ticket( project_key='KAN',description=description, summary=f"Exchange rates {date_to}")
    jira_client.add_attachment(ticket_key=key,file_path=f"{date_to}_file.xlsx")

if __name__ == '__main__':
    process_daily_rate()

