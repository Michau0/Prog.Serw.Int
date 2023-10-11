import requests

def check_url(url: str) -> bool:
    request = requests.get(url)
    kod = request.status_code
    if kod in range(200,300):
        return True
    return False

print(check_url("http://wmii.uwm.edu.pl"))