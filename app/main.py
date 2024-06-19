"""POC on amplitude events sending app"""

import os
import json
import requests


def init():
    """init func"""
    print("init..")


def exit_fn():
    """exit func"""
    print("exited")


def send_amplitude_event(event_type: str, event_properties: dict):
    """sends amplitude event"""
    api_key = os.getenv("api_key")
    user_id = os.getenv("user_id")
    headers = {"Content-Type": "application/json", "Accept": "*/*"}

    data = {
        "api_key": api_key,
        "events": [
            {
                "user_id": user_id,
                "event_type": event_type,
                "event_properties": event_properties,
            }
        ],
    }

    response = requests.post(
        "https://api2.amplitude.com/2/httpapi",
        headers=headers,
        data=json.dumps(data),
        timeout=5000,
    )

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.text)


if __name__ == "__main__":
    init()
    events = [
        {
            "name": "Smith",
            "os_version": "15",
            "variant": "ios",
            "device_type": "mobile",
        },
        {
            "name": "Jones",
            "os_version": "12",
            "variant": "android",
            "device_type": "mobile",
        },
        {
            "name": "Bob",
            "os_version": "11",
            "variant": "microsoft",
            "device_type": "Desktop",
        },
    ]
    for index, ev in enumerate(events):
        print("processing event ", index)
        send_amplitude_event(event_type="signup", event_properties=ev)
    exit_fn()
