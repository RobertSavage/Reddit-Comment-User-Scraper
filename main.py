import praw
import requests
import bs4
from prawcore.exceptions import Forbidden
from time import sleep
import subreddit_list as SL
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

client_id = '######'
client_secret = '######'
username = '######'
password = '######'
user_agent = 'pulling_models_test'
reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,username=username,password=password,user_agent=user_agent)

subred = SL.subred
listtest = []

print('START TIME: ', datetime.now())

def commentusers(subredd):

	x = reddit.subreddit(subredd)
	y = x.new(limit=1000)
	worked = 0
	failed = 0
	try:
		for post in y:
			for comment in post.comments:
				try:
					Text_file = open('comments.txt','a', encoding='utf-8')
					Text_file.write(str(comment.author)+"\n")
					worked += 1
					sleep(0.3)
				except:
					print(f'{subredd}bad g')
					failed += 1
					sleep(5)
					continue
		print('----------------------------------------')
		print(subredd,' TIME: ',  datetime.now())
		print(subredd,' Worked: ',worked,' Failed: ', failed)
		print('----------','DONE: ',subredd,'----------')
		sucess = 0
		worked = 0
		sleep(20)
	except:	
		print(f'BIG BOI MESSED UP ALL DIS BITCH {subredd}')
		sleep(20)
		pass



processes = []
with ThreadPoolExecutor(max_workers=10) as executor:
	for sub in subred:
		processes.append(executor.submit(hoe_search, sub))

for task in as_completed(processes):
	print(task.result())

print('END OF TASK: ',datetime.now())