import asyncio
import base64
from ekko.drivers.fs import LocalFsDriver
from ekko.storage import Storage

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


async def main():
    fs = Storage(LocalFsDriver('/tmp'))
    await fs.write("/tmp/ekko.txt", "Hello from Ekko")

    print('exists? %s' % await fs.exists('/tmp/ekko.txt'))

    contents = await fs.read('/tmp/ekko.txt')
    print('File contents:')
    print(contents)

    print('delete %s' % await fs.delete('/tmp/ekko.txt'))
    print('exists? %s' % await fs.exists('/tmp/ekko.txt'))

    image = base64.b64decode(RED_DOT)
    await fs.write('/tmp/red.png', image)

    await fs.copy('/tmp/red.png', '/tmp/copy/red.copy.png')


if __name__ == "__main__":
    asyncio.run(main())
