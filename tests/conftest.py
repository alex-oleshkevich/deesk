import base64
import os
import pytest

from ekko.drivers.fs import LocalFsDriver
from ekko.drivers.memory import MemoryDriver
from ekko.drivers.s3 import S3Driver

# requires local https://min.io instance
AWS_ACCESS_KEY_ID = 'admin'
AWS_SECRET_ACCESS_KEY = 'adminadmin'
AWS_REGION_NAME = None
AWS_ENDPOINT_URL = os.environ.get('AWS_ENDPOINT_URL', 'http://localhost:9000')

drivers = [
    LocalFsDriver(base_dir='/tmp'),
    MemoryDriver(),
    S3Driver(
        bucket='ekko',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME,
        endpoint_url=AWS_ENDPOINT_URL,
    ),
]


@pytest.fixture
def image() -> bytes:
    RED_DOT = """iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAIAAAACDbGyAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9
    kT1Iw0AcxV9TpUVaFOwgIpihCoIFURFHrUIRKoRaoVUHk0s/hCYNSYuLo+BacPBjserg4qyrg6sg
    CH6AuLk5KbpIif9LCi1iPDjux7t7j7t3gFAvMc3qGAM0vWKmEnExk10RA68IIowejGBQZpYxK0lJ
    eI6ve/j4ehfjWd7n/hxhNWcxwCcSzzDDrBCvE09tVgzO+8QRVpRV4nPiUZMuSPzIdcXlN84FhwWe
    GTHTqTniCLFYaGOljVnR1IgniaOqplO+kHFZ5bzFWStVWfOe/IWhnL68xHWaA0hgAYuQIEJBFRso
    oYIYrTopFlK0H/fw9zt+iVwKuTbAyDGPMjTIjh/8D353a+Unxt2kUBzofLHtjyEgsAs0arb9fWzb
    jRPA/wxc6S1/uQ5Mf5Jea2nRI6B7G7i4bmnKHnC5A/Q9GbIpO5KfppDPA+9n9E1ZoPcW6Fp1e2vu
    4/QBSFNXyRvg4BAYLlD2mse7g+29/Xum2d8PfP9yq/QP1TIAAAAJcEhZcwAALiMAAC4jAXilP3YA
    AAAHdElNRQflCA0QKgFMDexDAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAA
    ABFJREFUCNdj/M+AApgYKOMDAFCRAQngX9IjAAAAAElFTkSuQmCC"""
    return base64.b64decode(RED_DOT)
