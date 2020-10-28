#kap.org.tr sitesindeki verileri bazı verileri çekmek için yazmış olduğum beautifulsoup ile webden veri çekme

import requests

from bs4 import BeautifulSoup

r = requests.get("https://www.kap.org.tr/tr/bist-sirketler")
source = BeautifulSoup(r.content, "html.parser")
bist = source.find_all(
    "div", 
    attrs={"class": "w-clearfix w-inline-block comp-row"}
)
for i in bist:
    a = [j.text for j in i.find_all("a")]
    print(f"{a[0]}\n{a[1]}\n")
