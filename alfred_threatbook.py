# -*- encoding=utf8 -*-
import ipaddress
import sys
from urllib.parse import urlparse

query = sys.argv[1].strip().replace("\n", "").replace("\r\n", "")
query_type = ""
query_host = ""

if query.startswith('http'):
    # 解析 URL，并获取 host 部分
    query_host = urlparse(query).netloc

try:
    ipaddress.ip_address(query)
    query_type = "ip"
except ValueError:
    query_type = "domain"

print("https://x.threatbook.com/v5/{}/{}".format(query_type, query_host))