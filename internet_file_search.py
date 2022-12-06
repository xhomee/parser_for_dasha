import requests

headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

url = 'https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=b24c65985c3d63aef6eacd17a0c7b2d9c3357199'
filename = 'index.html'

response = requests.get(url,headers=headers)
if response.status_code == 200:
    with open(filename,'w', encoding="utf-8") as file:
        file.write(response.text)
else:
  print(response)