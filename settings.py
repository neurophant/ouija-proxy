import os

from cryptography.fernet import Fernet


DEBUG = bool(int(os.getenv('OUIJA_DEBUG')))
MONITOR = bool(int(os.getenv('OUIJA_MONITOR')))

PROXY_HOST = os.getenv('OUIJA_PROXY_HOST')
PROXY_PORT = int(os.getenv('OUIJA_PROXY_PORT'))

KEY = os.getenv('OUIJA_KEY')
fernet = Fernet(KEY)
TOKEN = os.getenv('OUIJA_TOKEN')
SERVING_TIMEOUT = float(os.getenv('OUIJA_SERVING_TIMEOUT'))
TCP_BUFFER = int(os.getenv('OUIJA_TCP_BUFFER'))
TCP_TIMEOUT = float(os.getenv('OUIJA_TCP_TIMEOUT'))
UDP_PAYLOAD = int(os.getenv('OUIJA_UDP_PAYLOAD'))
UDP_TIMEOUT = float(os.getenv('OUIJA_UDP_TIMEOUT'))
UDP_RETRIES = int(os.getenv('OUIJA_UDP_RETRIES'))
UDP_CAPACITY = int(os.getenv('OUIJA_UDP_CAPACITY'))
UDP_RESEND_SLEEP = float(os.getenv('OUIJA_UDP_RESEND_SLEEP'))
