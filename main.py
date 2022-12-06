import requests
from bs4 import BeautifulSoup as BS



link = "https://ukrcomexpo.com/pharmacy_summit_Ukraine-2022/?token=b24c65985c3d63aef6eacd17a0c7b2d9c3357199"
headers = {'user-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0',
      'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')

r = requests.get(link, headers=headers)

r.encoding = 'utf8'
#print(r)

html= BS(r.content, 'html.parser')
#print(html.prettify())

temp = html.find('video', id_="video")
find_error = html.find('div', class_="alert alert-danger mt-3")
test = html.find('div', class_="about-summit-desc-container")


#print(requests.utils.default_headers())

print(temp)
print(find_error)
print(test)
print()
#print(html)

# div class alert alert-danger mt-3

#class="timer-heading"
#id="video"
#for el in html.select(".stream-box border mb-3 w-100 position-relative")