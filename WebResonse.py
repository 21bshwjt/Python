import requests

class TextColors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

url = "https://www.google.com/"
response = requests.get(url, headers = {'user-agent': 'hello0987654'})

if response.status_code == 200:
    print(TextColors.GREEN + url + ":URL is Responding with Code:200." + TextColors.RESET)
else:
    print(TextColors.RED + url + ":Error" + TextColors.RESET)
