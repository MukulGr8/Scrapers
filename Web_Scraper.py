import requests
from bs4 import BeautifulSoup
loc=raw_input("Enter Location"+"\n")
pages=input("How Much Pages"+"\n")
page = 0 
base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
#loc = "San+Francisco,+CA"
while page < pages:
	print page
	url = base_url + loc + "&start" + str(page) 
	yelp = requests.get(url)
	yelp_soup = BeautifulSoup(yelp.text,"html.parser")
	business = yelp_soup.findAll('div',{'class':'biz-listing-large'})
	yelp_soup.encode("utf-8")
	file_path = "yelp.txt" 
	with open(file_path,"a") as textfile:
		for li in business:
			title = li.findAll('a',{'class':'biz-name'})[0].text #use .contents for html content at place of text
			titles = title.encode("utf-8")  #Fix For Encoding Error
			print(titles)
			add = li.findAll('address')[0].getText().strip(" \n\t\r")
			adds =  add.encode("utf-8")
			print(adds)
			phone = li.findAll('span',{'class':'biz-phone'})[0].getText().strip(" \n\t\r")
			ph = phone.encode("utf-8")
			print (ph+"\n")
			page_line = "{Title}\n{Address}\n{Phone}\n\n".format(
					Title = titles,
					Address = adds,
					Phone = ph
			) 
			textfile.write(page_line)
		page+=10

#For Links
#for link in yelp_soup.findAll('a'):
#	print(link)

#For Lists in class names
#for li in yelp_soup.findAll('li',{'class':'regular-search-result'}):
#	print (li)
	
#For links in class names
#for links in yelp_soup.findAll('a',{'class':'biz-name'}):
#	print (links.text.encode("utf-8"))   #Fix For Encoding Error
	
 
