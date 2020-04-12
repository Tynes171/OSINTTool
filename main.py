from flask import Flask, render_template

import Twitter, Instagram
import HIBP
import Dehashed
import EmailRepIO
import Phone
import ThatsThem
import threading





app = Flask(__name__)

@app.route("/")
def index():
   return "<h1> Hey Buddy </h1>"





#BELOW ARE FUNCTIONS FOR FUNCTIONALITY 

@app.route("/twitterprofile/<username>")
def get_profile(username):
		
		text = Twitter.profile_extraction(username)
		
		return "<h1> {} </h1>".format(text)




@app.route("/instagramprofile")
def get_instagram_profile():

	
	text = Instagram.get_profile(username)
	
	

@app.route("/instagramphotos")
def get_instagram_photos():

	
	photoThread = threading.Thread(target = Instagram.get_photos, args=(username,))
	photoThread.start()



@app.route("/instagramhighlights")
def get_instagram_highlights():

	
	highlightThread = threading.Thread(target = Instagram.get_highlights, args=(username,))
	highlightThread.start()



@app.route("/instagramstories")
def get_instagram_stories():

	
	storyThread = threading.Thread(target = Instagram.get_stories, args=(username,))
	storyThread.start()


@app.route("/birthdayhits")
def get_birthday_hits():
	
	
	text = Twitter.birthday_extraction(username)
	
	


@app.route("/generalsearchtwitter")
def general_search_twitter():
	
	text = Twitter.general_extraction(username, search)
	

@app.route("/phonenumberdetails")
def get_phone_number_details(self):
	number = self.phoneNumberTextField.text()
	
	text = Phone.get_addresses(number)
	
@app.route("/breachedemailaccounts/<email>")
def get_breached_email_accounts(email):
	
	
	sites = HIBP.breached_accounts(email)
	emailProfiles = EmailRepIO.get_profiles(email)
	text = ''
	text += "<p> {} </p>".format(emailProfiles)
	text += "<h1> ----- BREACHES IT WAS FOUND IN-------- </h2>"
	for item in sites:
		text += '<h2> {} </h2>'.format(item['Name'])

	return "<h1> {} </h1>".format(text)
	

@app.route("/breachedusernamedata/<username>")
def get_breached_username_data(username):
	username = self.usernameUsernameTextField.text()

	text = Dehashed.retrieve_hits(username)
	return "<p> {} </p>".format(text)
	

@app.route("/realnamehits/")
def get_real_name_hits():
	firstName = self.firstNameTextField.text()
	lastName = self.lastNameTextField.text()
	city = self.cityTextField.text()
	state = self.stateTextField.text()


	text = ThatsThem.get_results(firstName, lastName, city, state)

	




if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()