import Twitter, Instagram
import HIBP
import Dehashed
import EmailRepIO
import Phone
import ThatsThem


import threading
import sys



from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

class OSINTApp(App):

    def build(self):
        return TabbedPanel()

    def get_profile(self, username = "john1234"):
		
        
        text = Twitter.profile_extraction(username)
        
        print(text)

    def get_birthday_hits(self, username = "john1234"):


        text = Twitter.birthday_extraction(username)
        print(text)

    def general_search_twitter(self, username = "john1234", search = "Yes"):


        text = Twitter.general_extraction(username, search)
        print(text)


    def get_instagram_profile(self, username = "nauticalnonsense_1"):



        text = Instagram.get_profile(username)

        print(text)


    def get_instagram_photos(self, username = "nauticalnonsense_1" ):



        photoThread = threading.Thread(target = Instagram.get_photos, args=(username,))
        photoThread.start()





    def get_instagram_highlights(self,  username = "nauticalnonsense_1"):



        highlightThread = threading.Thread(target = Instagram.get_highlights, args=(username,))
        highlightThread.start()

    def get_instagram_stories(self, username = "nauticalnonsense_1"):



        storyThread = threading.Thread(target = Instagram.get_stories, args=(username,))
        storyThread.start()

    
    def get_breached_username_data(self, username):


        text = Dehashed.retrieve_hits(username)

        print(text)

    def get_phone_number_details(self, number):

        text = Phone.get_addresses(number)

        print(text)








    def get_breached_email_accounts(self, email = "justinwilliams171@yahoo.com"):
        email = self.emailAddressTextField.text()

        sites = HIBP.breached_accounts(email)
        emailProfiles = EmailRepIO.get_profiles(email)
        text = ''
        text += "\n{}".format(emailProfiles)
        text += "\n----- BREACHES IT WAS FOUND IN--------\n"
        for item in sites:
            text += item['Name'] +'\n'

        print(text)








    def get_real_name_hits(self, firstName = "Justin", lastName = "Williams", city = "Upper Marlboro", state = "MD"):

        text = ThatsThem.get_results(firstName, lastName, city, state)
        print(text)





if __name__ == '__main__':
    app = OSINTApp()
    app.run()


