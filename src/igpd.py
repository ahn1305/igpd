import instaloader

import os

from instaloader import Profile, Post

from print import *




def activate():

	print("Welcome to igpd", SM,GREEN)

	div.div('-')

	print("a: Download a post",YELLOW)
	print("b: Dowload story",YELLOW)
	print("c: Dowload highlights",YELLOW)
	print("d: Download entire Profile",YELLOW)
	print("e: exit",YELLOW)

	option = input("\nEnter your choice: ")

	if option == 'a':
		downloadpost()
	elif option == 'b':
		downloadstory()
	elif option == 'c':
		downloadhighlights()
	elif option == 'd':
		downloadprofile()
	elif option == 'e':
		quit()
	else:
		pass



def downloadpost():

	print('\nLOGIN')

	name = input("\nEnter username: ")
	passwo = input("Enter password: ")

	instance = instaloader.Instaloader()

	instance.login(user=name,passwd=passwo)
	print("\nLogin successful")
	print(f"\nWelcome {name}")
	ide = input("\nEnter the id of the post you want to download: ")

	post = Post.from_shortcode(instance.context, ide)
	instance.download_post(post,target=(ide))

	print("\nPost downloaded successful and saved in -- "+ ide)

	conti_1 = input("\nDo you want to continue(yes/no): ")

	if conti_1 == 'yes':
		activate()
	else:
		quit() 



def downloadstory():
	print('\nLOGIN')

	name = input("\nEnter username: ")
	passwo = input("Enter password: ")

	instance = instaloader.Instaloader()

	instance.login(user=name,passwd=passwo)
	print("\nLogin successful")
	print(f"\nWelcome {name}")
	st = input("\nEnter the username of the person: ")

	profile = Profile.from_username(instance.context, username=st)

	instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))

	print("Story downloaded successfully and saved as {}/stories".format(profile.username))

	conti_2 = input("\nDo you want to continue(yes/no): ")

	if conti_2 == 'yes':
		activate()
	else:
		quit() 




def downloadhighlights():
	print('\nLOGIN')

	name = input("\nEnter username: ")
	passwo = input("Enter password: ")

	instance = instaloader.Instaloader()

	instance.login(user=name,passwd=passwo)
	print("\nLogin successful")
	print(f"\nWelcome {name}")
	usre = input("\nEnter the username of the person: ")
	profile = Profile.from_username(instance.context, username= usre)

	for highlight in instance.get_highlights(user=profile):
	    # highlight is a Highlight object
	    for item in highlight.get_items():
	        # item is a StoryItem object
	        instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))

	print("\nHighlights downloaded successful and saved as {}/{}".format(highlight.owner_username, highlight.title))

	conti_3 = input("\nDo you want to continue(yes/no): ")

	if conti_3 == 'yes':
		activate()
	else:
		quit() 





def downloadprofile():
	print('\nLOGIN')

	name = input("\nEnter username: ")
	passwo = input("Enter password: ")

	instance = instaloader.Instaloader()

	instance.login(user=name,passwd=passwo)
	print("\nLogin successful")
	print(f"\nWelcome {name}")
	usr = input("\nEnter the username of the person: ")

	instance.download_profile(profile_name=usr)


	print("\nProfile download successful and saved as -- "+ usr)

	conti_4 = input("\nDo you want to continue(yes/no): ")

	if conti_4 == 'yes':
		activate()
	else:
		quit() 


			
activate()