import requests
from json import dumps
from sys import stderr

NLP = "192.168.43.84"


def summarize(text):
    """Talk to NLP microservice to get text summary."""
    response = requests.post(NLP, data=text)

    if response.status_code == 200:
        return response.data
    else:
        stderr.write("NLP Api sux, can't even respond properly, \
                      status_code: {}".format(str(response.status_code)))

    return None


summarize("HELLO")
