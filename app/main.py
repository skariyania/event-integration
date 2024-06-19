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


def send_amplitude_event(event_type: str):
    """sends amplitude event"""
    api_key = os.getenv("api_key")
    user_id = os.getenv("user_id")
    headers = {"Content-Type": "application/json", "Accept": "*/*"}

    data = {
        "api_key": api_key,
        "events": [{"device_id": user_id, "event_type": event_type}],
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
    send_amplitude_event(event_type="signup")
    send_amplitude_event(event_type="onboarding")
    exit_fn()
