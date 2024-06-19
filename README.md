# event-integration
integration of amplitude

# how to run this app?

```shell
pip install -r requirements.txt
```
```shell
user_id=<AMPLITUDE_USERNAME> api_key=<AMPLITUDE_API_KEY> python3 app/main.py 
```

# More about Amplitude Python SDK
```curl
https://amplitude.com/docs/sdks/analytics-sdks/python/ampli-for-python-sdk#:~:text=Send%20event%20objects%20using%20the%20generic%20track%20method.,%23%20str%2C%20song_favorited%20%3D%20True%2C%20%23%20bool%29%2C%20EventOptions%28device_id%3D%22device_id%22%29%29
```

# How to start python venv
source .venv/bin/activate

# More about Amplitude HTTP Documentation

```curl
https://amplitude.com/docs/apis/analytics/http-v2#keys-for-the-event-argument
```

```curl
https://amplitude.com/docs/partners/create-an-event-ingestion-integration#test-and-submit-the-integration
```

# How to use frontend app

1. Replace API_KEY_PLACEHOLDER with your actual Amplitude api key
2. open  frontend/index.html in your browser