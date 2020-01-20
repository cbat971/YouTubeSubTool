import bs4 
import requests
from selenium import webdriver
import time
try:
	html = open("test.html", "r")
	# response = requests.get(vid_page)
	soup =  bs4.BeautifulSoup(html, 'lxml')

	vid_ids = []
	test = (str(soup)).split('v=')
	video_ids = []
	for each in test:
		if each[11] == '\"':
			if (str(each[0:11])) not in vid_ids:
				if "=" not in (str(each[0:11])):
					vid_ids.append(str(each[0:11]))
	import pickle
	print(vid_ids)
	with open("JRE_id's.txt", "wb") as fp:
		pickle.dump(vid_ids, fp)
	print(len(vid_ids))
except:
	print("It didn't work")