import instaloader
import os, cv2, shutil, imutils, json

from itertools import islice
from math import ceil

session = instaloader.Instaloader()
with open('auth.json') as json_file:
	data = json.load(json_file)

try:

	session.login(data['instagramusername'], data['instagrampassword'])

except instaloader.exceptions.BadCredentialsException:
	print("Go to Instagram.py File and put in your username and password")

def display_photos(image):
	'''
	captionFile = image.replace('.jpg', '.txt')
	caption = ''
	try:
		with open(captionFile, 'r') as f:
			caption = f.read()
	except:
		pass
	'''
	img = cv2.imread(image)
	img = imutils.resize(img, width = 400, height = 400)
	#if len(caption) > 0:
	#	cv2.putText(img, caption, (0, 200), cv2.FONT_HERSHEY_SIMPLEX, .25, (0, 0, 255), 5)
	
	cv2.imshow('Photo ', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()



def display_stories(story):
	vid = cv2.VideoCapture(story)
	ret = True
	while ret:

		ret, frame = vid.read()
		if ret == True:

			frame = imutils.resize(frame, width = 400, height = 400)

			cv2.imshow('frame', frame)


			if cv2.waitKey(30) & 0xFF == ord('q'):
				break

		else:
			break

	
	vid.release()
	cv2.destroyAllWindows()
	return

def get_profile(user):

	try:
		profile = instaloader.Profile.from_username(session.context, user)


		return profile.biography
		
	except Exception as e:

		return "Failed Because of {}".format(e)


def get_stories(user):

	

	os.system('instaloader --login {} --stories-only {}'.format('nauticalnonsense_1', user))
	files = os.listdir(user)
	display = []
	for f in files:
	
		display.append(f)

	for d in display:
		if d.endswith('.mp4'):
			display_stories('{}/{}'.format(user, d))
		if d.endswith('.jpg'):
			display_photos('{}/{}'.format(user, d))

	shutil.rmtree(user)


def get_photos(user):
	
	limit = 6
	profile = instaloader.Profile.from_username(session.context, user)
	posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.date_local,
                               reverse=True)

	for post in islice(posts_sorted_by_likes, limit):
		session.download_post(post, user)
	

	files = os.listdir(user)
	display = []
	for f in files:
		if f.endswith('.jpg'):
			display.append(f)

	for i in range(5):
		display_photos('{}/{}'.format(user, display[i]))

	shutil.rmtree(user)
	


def get_highlights(user):
	profile = instaloader.Profile.from_username(session.context, user)

	for highlight in session.get_highlights(profile):

		for item in highlight.get_items():

			session.download_storyitem(item, '{}'.format(highlight.owner_username))
	
	files = os.listdir(user)
	display = []
	for f in files:
	
		display.append(f)

	for d in display:
		if d.endswith('.mp4'):
			display_stories('{}/{}'.format(user, d))
		if d.endswith('.jpg'):
			display_photos('{}/{}'.format(user, d))
	shutil.rmtree(user)


if __name__ == '__main__':
	
	USER = input("Enter a username\n")
	#get_stories(USER)
	get_photos(USER)
	#get_highlights(USER)





