import requests
from io import BytesIO
import ssl
import os


class Request:
    url = None
    client = False

    def __init__(self, url):
        self.url = url
        self.client = self.get_client(url, self)

    def get_content(self):
        if not self.client: return False
        return self.client.content

    def get_bytes_io(self):
        if not self.client: return False
        return BytesIO(self.get_content())

    def get_content_length(self):
        if not self.client: return False
        if self.client.headers['content-length']:
            return int(self.client.headers['content-length'])
        else:
            return len(self.get_content())

    def get_content_type(self):
        if not self.client: return False
        if self.client.headers['content-type']:
            return self.client.headers['content-type']
        else:
            return len(self.get_content())

    @staticmethod
    def get_client(url, self):
        response = None
        try:
            response = requests.get(
                url,
                headers={
                    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                    'Accept-Language': 'en-GB,en-US,en;q=0.8'
                }
            )
        except requests.exceptions.SSLError as e:
            self.error = str(e)
        except Exception as e:
            self.error = str(e)

        return response


def get(url):
    return Request(url)
