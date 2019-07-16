from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen,Request
from urllib.parse import quote
import re

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
def search(url):
	#add ur url here
	print(url)
	client=Request(url,headers=headers)
	page_html=urlopen(client).read()
	page_soup=soup(page_html,"html.parser")
	return page_soup
	"""a=(page_soup.find("div",{"class":"product-box-list"}).findAll("p",{"class":"title"}))
	for i in a:
		print(type(i))"""
	#systax search:https://tiki.vn/search?q=túi+du+lịch
def find_items(page_soup,sea):#
	a=page_soup.find("div",{"class":"product-box-list"}).findAll("div",{"data-seller-product-id":re.compile("^[0-9]")})
	#print(a)
	min=10000000
	name=""
	url_item=""
	data_id=0
	dem=0
	for i in a:
		#print(i.attrs["data-title"],i.attrs["data-price"])
		if int(i.attrs["data-price"])<min and sea.lower() in (i.attrs["data-title"]).lower():
			min=int(i.attrs["data-price"])
			name=i.attrs["data-title"]
			data_id=int(i.attrs["data-id"])
	print(f"{name}:{min} with id {data_id}")
	return data_id

def getLink(data_id,page_soup):
	b=page_soup.find("div",{"class":"product-box-list"}).findAll("a",{"href":re.compile("^(https://tiki.vn/)")})
	for i in b:
		if int(i.attrs["data-id"])== data_id:
			return (i.attrs["href"])


def main():
	while True:
		sea=input("bạn muốn mua gì:")
		# search:https://tiki.vn/search?q=túi+du+lịch
		url="https://tiki.vn/search?q="+quote(sea)
		inf=search(url)
		item=find_items(inf,sea)
		a=getLink(item,inf)
		b=input("Can I open your browser (Y/N)")
		if(b.lower()=="y"):
			from selenium import webdriver
			from selenium.webdriver.common.keys import Keys
			import webbrowser
			browser = webdriver.Chrome(executable_path=r"C:\Users\ASUS\Documents\python\tacke\chromedriver_1.exe")
			browser.get(a)
		else :
			b=input("bạn có muốn tìm tiếp (Y/N)")
			if(b.lower()=="n"):
				break
			else:
				continue

if __name__ == '__main__':
	main()


