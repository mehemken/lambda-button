import requests

def ping_lambda():
    url = 'https://ye1851xhde.execute-api.us-west-2.amazonaws.com/test/lbutton'
    response = requests.get(url)
    return response.text
