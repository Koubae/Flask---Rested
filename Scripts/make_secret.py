import os
from base64 import b64encode

if __name__ == '__main__':
    print(f'Random App Secret = {b64encode(os.urandom(20)).decode("UTF-8")}')

