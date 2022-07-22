import json

import requests
from celery_app import celery, smtp_gmail, headers, NOTION_DATABASE_ID
from email.message import EmailMessage


def formatNotionPage(restaurant, menu):
    return {
        "parent": {
            "database_id": {NOTION_DATABASE_ID},
        },
        "properties": {
            "Restaurant": {"title": [{"text": {"content": restaurant}}]},
            "Menu": {"select": {"name": menu}},
        },
    }


@celery.task
def createNotionItemToDatabase(restaurant, menu):
    notion_database_url = "https://api.notion.com/v1/pages"
    newPageData = formatNotionPage(restaurant, menu)
    data = json.dumps(newPageData)

    res = requests.request("POST", notion_database_url, headers=headers, data=data)

    print(res.status_code)
    print(res.text)

    return f"{restaurant}, {menu} is added to database"
