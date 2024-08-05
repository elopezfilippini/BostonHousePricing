import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=None, cert_reqs=None, options=None)
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

session = requests.Session()
session.mount('https://', TLSAdapter())