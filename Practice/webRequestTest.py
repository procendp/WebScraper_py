from requests import get

websiteList = ( # Tuple
    "google.com",
    "airbnb.com",
    "https://naver.com",
    "daum.com",
    "https://facebook.com"
)

result = {} # dicitonary

for website in websiteList:
        if not website.startswith("https://"):
            website = f"https://{website}"

        response = get(website)     # <Response [200]> ==> 성공적으로 응답 받는중
        # print(response.status_code) # only code

        if response.status_code == 200:
            result[website] = "OK"
        else:
            result[website] = "FAILED"

print(result)
             
              
        
"""
[Request Code]

Response 100번대 -> informational
Response 200번대 -> success
Response 300번대 -> redirection
Response 400번대 -> client error (ex) 404 not found
Response 500번대 -> server error
"""
        

