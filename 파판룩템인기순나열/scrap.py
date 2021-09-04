import requests
from bs4 import BeautifulSoup

def scraping():
	url = "https://ffxiv.eorzeacollection.com/glamours?filter%5BorderBy%5D=date&filter%5Brace%5D=any&filter%5Bgender%5D=male&search=&author=&filter%5Bjob%5D%5B%5D=blm&filter%5Bjob%5D%5B%5D=smn&filter%5Bjob%5D%5B%5D=rdm&filter%5Bjob%5D%5B%5D=blu&filter%5BminimumLvl%5D=1&filter%5BmaximumLvl%5D=80&filter%5BheadPiece%5D=&filter%5BbodyPiece%5D=&filter%5BhandsPiece%5D=&filter%5BlegsPiece%5D=&filter%5BfeetPiece%5D=&filter%5BweaponPiece%5D=&filter%5BoffhandPiece%5D=&filter%5BearringsPiece%5D=&filter%5BnecklacePiece%5D=&filter%5BbraceletsPiece%5D=&filter%5BleftRingPiece%5D=&filter%5BrightRingPiece%5D=&page=3"
	r = requests.get(url)
	soup = BeautifulSoup(r.text,"html.parser")
	last_page = soup.find("div",{"class":"l-section-pagination"}).find("h3",{"class":"l-section-label l-section-pagination-title"}).string.strip()
	last_page = int(last_page.split("of")[1].strip())
	list_list = []
	new_list_list = []
	for i in range(1,last_page+1):
		new_url = f"https://ffxiv.eorzeacollection.com/glamours?filter%5BorderBy%5D=date&filter%5Brace%5D=any&filter%5Bgender%5D=male&search=&author=&filter%5Bjob%5D%5B%5D=blm&filter%5Bjob%5D%5B%5D=smn&filter%5Bjob%5D%5B%5D=rdm&filter%5Bjob%5D%5B%5D=blu&filter%5BminimumLvl%5D=1&filter%5BmaximumLvl%5D=80&filter%5BheadPiece%5D=&filter%5BbodyPiece%5D=&filter%5BhandsPiece%5D=&filter%5BlegsPiece%5D=&filter%5BfeetPiece%5D=&filter%5BweaponPiece%5D=&filter%5BoffhandPiece%5D=&filter%5BearringsPiece%5D=&filter%5BnecklacePiece%5D=&filter%5BbraceletsPiece%5D=&filter%5BleftRingPiece%5D=&filter%5BrightRingPiece%5D=&page={i}"
		r = requests.get(new_url)
		soup = BeautifulSoup(r.text,"html.parser")
		parent_tag = soup.find_all("article",{"class":"c-glamour-grid-item"})
		print(f"scraping....{i}page")
		for i in parent_tag:
			standard = int(i.find("span",{"class":"c-label"}).string)
			a = i.find_all("a")
			link = "https://ffxiv.eorzeacollection.com"+a[2]["href"]
			dict_list = {
				"point":standard,
				"link":link
			}
			list_list.append(dict_list)

	list_list.sort(key=lambda post: post['point'], reverse=True)
	for i in list_list:
		point = i["point"]
		if point >= 100:
			new_list_list.append(i)
	return new_list_list		

if __name__ == "__main__":
	print(scraping())

