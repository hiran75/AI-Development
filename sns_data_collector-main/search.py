import os
import sys
import urllib.request
client_id = "nUriXF2_0OE3PVwIucQP"
client_secret = "MdiZXS30FF"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2023-01-01\",\"endDate\":\"2023-06-11\",\"timeUnit\":\"date\",\"keywordGroups\":[{\"groupName\":\"삼성\",\"keywords\":[\"삼성\",\"samsung\"]},{\"groupName\":\"LG\",\"keywords\":[\"LG\",\"엘지\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    