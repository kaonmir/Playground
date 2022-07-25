import json

import requests
from celery_app import celery, headers, NOTION_DATABASE_ID


def formatNotionPage(restaurant, menu):
    return {
        "parent": {
            "database_id": NOTION_DATABASE_ID,
        },
        "properties": {
            "Restaurant": {"title": [{"text": {"content": restaurant}}]},
            "Menu": {"select": {"name": menu}},
        },
    }


@celery.task
def createNotionItemToDatabase(restaurant, menu):
    print("Start createNotionItemToDatabase function")
    notion_database_url = "https://api.notion.com/v1/pages"
    newPageData = formatNotionPage(restaurant, menu)
    data = json.dumps(newPageData)
    res = requests.request("POST", notion_database_url, headers=headers, data=data)
    if res.status_code != 200:
        raise Exception("Error creating new page in Notion")

    return f"You have eaten {menu} at {restaurant}"
