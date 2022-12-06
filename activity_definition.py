from temporalio import activity
import requests


@activity.defn
async def RestActivity():
    print("RestActivity starting")
    response = requests.get("https://www.google.com")
    print("RestActivity completed")
    return response
