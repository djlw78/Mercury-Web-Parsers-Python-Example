#!/usr/bin/python
import json
import requests

timeoutconnection = 60
headermercury = {"x-api-key": "YUOR APi KEY"}
mercury = "https://mercury.postlight.com/parser?url="

url = "http://www.example.com/article"

page = requests.get(mercury + url, headers=headermercury, timeout=timeoutconnection)

data = json.loads(page.text)

print "Output by Mercury Web Parser"
print data["title"]
print data["content"]
print data["date_published"]
print data["lead_image_url"]
print data["url"]
print data["domain"]
print data["excerpt"]
print data["word_count"]
print data["direction"]
print data["total_pages"]
print data["rendered_pages"]
print data["next_page_url"]