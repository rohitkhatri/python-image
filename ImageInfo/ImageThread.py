import threading
import time
from ImageInfo import Request
from PIL import Image


class ImageThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.request = None
        self.image = False
        self._error = False
        self.allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/tiff', 'image/bmp']

    def run(self):
        self.request = Request.get(self.url)

        if self.request.client and self.status_code() == 200:
            try:
                if self.request.get_content_type() in self.allowed_types:
                    self.image = Image.open(self.request.get_bytes_io())
                else:
                    self._error = 'Image format "'+self.request.get_content_type()+'" not supported'
            except OSError as e:
                self._error = str(e)

    def status_code(self):
        return self.request.client.status_code

    def succeeded(self):
        if not self.request.client or self.status_code() != 200:
            self._error = self.request.error
            return False
        elif self._error:
            return False

        return True

    def error(self):
        return {
            'url': self.url,
            'error': self._error
        }

    def get(self):
        return {
            'url': self.url,
            'width': self.image.size[0],
            'height': self.image.size[1],
            'ratio': self.ratio(self.image.size[0], self.image.size[1]),
            'mime': self.request.get_content_type(),
            'size': self.request.get_content_length()
        }

    @staticmethod
    def ratio(width, height):
        return float('{0:.2f}'.format((height / width) * 100))


def get_image_meta(urls):
    start_time = time.time()
    threads = []
    response = {'succeeded': [], 'failed': []}

    for url in urls:
        current = ImageThread(url)
        threads.append(current)
        current.start()

    for key, t in enumerate(threads):
        t.join()
        if t.succeeded():
            response['succeeded'].append(t.get())
        else:
            response['failed'].append(t.error())

    response['time'] = time.time() - start_time

    return response
