# -*- encoding=utf8 -*-
import ipaddress
import sys
from urllib.parse import urlparse

query = sys.argv[1].strip().replace("\n", "").replace("\r\n", "")

try:
    ipaddress.ip_address(query)
    query_host = ipaddress.ip_address(query)
    query_type = "ip"
except ValueError:
    query_host_item = urlparse(query)
    query_host = query_host_item.netloc
    if not query_host_item.netloc:
        query_host = query_host_item.path
    query_type = "domain"

print("https://x.threatbook.com/v5/{}/{}".format(query_type, query_host))
