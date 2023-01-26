#!/usr/bin/env python3

import os, json

#print("Content Type: text/html")
#print(os.environ)
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
#print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']}</p> ")