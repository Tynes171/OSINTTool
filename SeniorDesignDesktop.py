
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



import Twitter, Instagram
import HIBP
import Dehashed
import EmailRepIO
import Phone
import ThatsThem


import threading
import sys





class Window(QMainWindow):

	def __init__(self, title = "OSINT Software"):
		super().__init__()
		self.title = title
		self.left = 50
		self.top = 50
		self.width = 800
		self.height = 300
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.table_widget = App(self)
		self.setCentralWidget(self.table_widget)
		
		self.show()

class App(QWidget):

	def __init__(self, parent):
		super(QWidget, self).__init__(parent)
	
		self.layout = QVBoxLayout(self)


		self.tabs = QTabWidget()
		self.twitterTab = QWidget()
		self.instagramTab = QWidget()
		self.phoneNumberTab = QWidget()
		self.usernameTab = QWidget()
		self.emailAddressTab = QWidget()
	
		self.nameTab = QWidget()

		
		self.tabs.resize(300, 200)
		self.setUpTabs()

	def setUpTabs(self):


		'''============== CREATE WIDGETS FOR TWITTER WINDOW ==================='''
		self.tabs.addTab(self.twitterTab, "Twitter")
		self.twitterTab.layout = QVBoxLayout(self)
		self.twitterSearchButton = QPushButton("Search")
		self.twitterSearchButton.clicked.connect(self.general_search_twitter)


		self.twitterBirthdayButton = QPushButton("Birthday")
		self.twitterBirthdayButton.clicked.connect(self.get_birthday_hits)


		self.twitterProfileButton = QPushButton("Profile")
		self.twitterProfileButton.clicked.connect(self.get_profile)

		self.twitterUsernameLabel = QLabel("Username")
		self.twitterSearchLabel = QLabel("Search")
		self.twitterUsernameTextField = QLineEdit()
		self.twitterSearchTextField = QLineEdit()

		'''============== ADD WIDGETS TO TWITTER WINDOW ==================='''
		self.twitterTab.layout.addWidget(self.twitterUsernameLabel)
		self.twitterTab.layout.addWidget(self.twitterUsernameTextField)
		self.twitterTab.layout.addWidget(self.twitterSearchLabel)
		self.twitterTab.layout.addWidget(self.twitterSearchTextField)
		self.twitterTab.layout.addWidget(self.twitterProfileButton)
		self.twitterTab.layout.addWidget(self.twitterBirthdayButton)
		self.twitterTab.layout.addWidget(self.twitterSearchButton)
		self.twitterTab.setLayout(self.twitterTab.layout)



		'''============== CREATE WIDGETS FOR INSTAGRAM WINDOW ==================='''
		self.tabs.addTab(self.instagramTab, "Instagram")
		self.instagramTab.layout = QVBoxLayout(self)
		self.instagramPhotosButton = QPushButton("Photos")
		self.instagramPhotosButton.clicked.connect(self.get_instagram_photos)

		self.instagramHighlightsButton = QPushButton("Highlights")
		self.instagramHighlightsButton.clicked.connect(self.get_instagram_highlights)


		
		self.instagramStoriesButton = QPushButton("Stories")
		self.instagramStoriesButton.clicked.connect(self.get_instagram_stories)



		self.instagramProfileButton = QPushButton("Profile")
		self.instagramProfileButton.clicked.connect(self.get_instagram_profile)
		
		self.instagramUsernameLabel = QLabel("Username")
		self.instagramUsernameTextField = QLineEdit()

		'''============== ADD WIDGETS TO iNSTAGRAM WINDOW ==================='''
		self.instagramTab.layout.addWidget(self.instagramUsernameLabel)
		self.instagramTab.layout.addWidget(self.instagramUsernameTextField)
		self.instagramTab.layout.addWidget(self.instagramProfileButton)
		self.instagramTab.layout.addWidget(self.instagramHighlightsButton)
		self.instagramTab.layout.addWidget(self.instagramPhotosButton)
		self.instagramTab.layout.addWidget(self.instagramStoriesButton)
		self.instagramTab.setLayout(self.instagramTab.layout)



		'''============== CREATE WIDGETS FOR USERNAME WINDOW ==================='''
		self.tabs.addTab(self.usernameTab, "Username")
		self.usernameTab.layout = QHBoxLayout(self)
		self.usernameUsernameLabel = QLabel("Username")
		self.usernameUsernameTextField = QLineEdit()
		self.usernameResultsButton = QPushButton("results")
		self.usernameResultsButton.clicked.connect(self.get_breached_username_data)
		#self.usernameBreachesButton = QPushButton("Breaches")

		self.usernameUsernameTextField = QLineEdit()

		'''============== ADD WIDGETS TO USERNAME WINDOW ==================='''
		self.usernameTab.layout.addWidget(self.usernameUsernameLabel)
		self.usernameTab.layout.addWidget(self.usernameUsernameTextField)
		self.usernameTab.layout.addWidget(self.usernameResultsButton)
		self.usernameTab.setLayout(self.usernameTab.layout)



		'''============== CREATE WIDGETS FOR PHONE NUMBER WINDOW ==================='''
		self.tabs.addTab(self.phoneNumberTab, "Phone Number")
		self.phoneNumberTab.layout = QHBoxLayout(self)
		self.phoneNumberSearchButton = QPushButton("Search")
		self.phoneNumberSearchButton.clicked.connect(self.get_phone_number_details)
		self.phoneNumberLabel = QLabel("Phone Number (Format Must be xxxyyyzzzz not (XXX)YYY-ZZZZ")
		self.phoneNumberTextField = QLineEdit()

		'''============== ADD WIDGETS TO PHONE NUMBER WINDOW ==================='''
		self.phoneNumberTab.layout.addWidget(self.phoneNumberLabel)
		self.phoneNumberTab.layout.addWidget(self.phoneNumberTextField)
		self.phoneNumberTab.layout.addWidget(self.phoneNumberSearchButton)
		self.phoneNumberTab.setLayout(self.phoneNumberTab.layout)




		'''============== CREATE WIDGETS FOR EMAIL WINDOW ==================='''
		self.tabs.addTab(self.emailAddressTab, "Email Address")
		self.emailAddressTab.layout = QHBoxLayout(self)
		self.emailAddressSearchButton = QPushButton("Search")
		self.emailAddressSearchButton.clicked.connect(self.get_breached_email_accounts)
		self.emailAddressLabel = QLabel("Email Address")
		self.emailAddressTextField = QLineEdit()

		'''============== ADD WIDGETS TO EMAIL WINDOW ==================='''
		self.emailAddressTab.layout.addWidget(self.emailAddressLabel)
		self.emailAddressTab.layout.addWidget(self.emailAddressTextField)
		self.emailAddressTab.layout.addWidget(self.emailAddressSearchButton)
		self.emailAddressTab.setLayout(self.emailAddressTab.layout)




		'''============== CREATE WIDGETS FOR NAME WINDOW ==================='''
		self.tabs.addTab(self.nameTab, "Name")
		self.nameTab.layout = QVBoxLayout(self)
		self.addressSearchButton = QPushButton("Address")
		self.addressSearchButton.clicked.connect(self.get_real_name_hits)
		self.firstNameLabel = QLabel("First Name")
		self.firstNameTextField = QLineEdit()
		self.lastNameLabel = QLabel("Last Name")
		self.lastNameTextField = QLineEdit()
		self.stateLabel = QLabel("State (Two Letter Code: GA not Georgia)")
		self.stateTextField = QLineEdit()
		self.cityLabel = QLabel("City (If Multiple Names, Sparate with Dash. Marietta-Heights not Marietta Heights")
		self.cityTextField = QLineEdit()

		'''============== ADD WIDGETS TO NAME WINDOW ==================='''
		self.nameTab.layout.addWidget(self.firstNameLabel)
		self.nameTab.layout.addWidget(self.firstNameTextField)
		self.nameTab.layout.addWidget(self.lastNameLabel)
		self.nameTab.layout.addWidget(self.lastNameTextField)
		self.nameTab.layout.addWidget(self.stateLabel)
		self.nameTab.layout.addWidget(self.stateTextField)
		self.nameTab.layout.addWidget(self.cityLabel)
		self.nameTab.layout.addWidget(self.cityTextField)
		self.nameTab.layout.addWidget(self.addressSearchButton)
		self.nameTab.setLayout(self.nameTab.layout)





	

		
		

		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)



	def get_profile(self):
		username = self.twitterUsernameTextField.text()
		
		self.text = Twitter.profile_extraction(username)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits From Twitter")
		msg.setText(self.text)


		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()


	def get_instagram_profile(self):

		username = self.instagramUsernameTextField.text()
		
		self.text = Instagram.get_profile(username)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")

		msg.setInformativeText("Hits From Instagram")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()
		

		val = msg.exec_()

	def get_instagram_photos(self):

		username = self.instagramUsernameTextField.text()
		
		photoThread = threading.Thread(target = Instagram.get_photos, args=(username,))
		photoThread.start()


		msg = QMessageBox()
		msg.setWindowTitle("Results")

		msg.setInformativeText("Photos Downloading in background")
		

		val = msg.exec_()


	def get_instagram_highlights(self):

		username = self.instagramUsernameTextField.text()
		
		highlightThread = threading.Thread(target = Instagram.get_highlights, args=(username,))
		highlightThread.start()


		msg = QMessageBox()
		msg.setWindowTitle("Results")

		msg.setInformativeText("Highlights Downloading in background")
		

		val = msg.exec_()

	def get_instagram_stories(self):

		username = self.instagramUsernameTextField.text()
		
		storyThread = threading.Thread(target = Instagram.get_stories, args=(username,))
		storyThread.start()


		msg = QMessageBox()
		msg.setWindowTitle("Results")

		msg.setInformativeText("Stories Downloading in background")
		

		val = msg.exec_()



	def get_birthday_hits(self):
		username = self.twitterUsernameTextField.text()
		
		self.text = Twitter.birthday_extraction(username)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits From Twitter")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()

	def general_search_twitter(self):
		username = self.twitterUsernameTextField.text()
		search = self.twitterSearchTextField.text()
		
		self.text = Twitter.general_extraction(username, search)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits From Twitter")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()

	def get_phone_number_details(self):
		number = self.phoneNumberTextField.text()
		
		self.text = Phone.get_addresses(number)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits From Twilio")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()


	def get_phone_number_details(self):
		number = self.phoneNumberTextField.text()
		
		self.text = Phone.get_addresses(number)
		
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits From Twilio")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()



	def get_breached_email_accounts(self):
		email = self.emailAddressTextField.text()
		
		sites = HIBP.breached_accounts(email)
		emailProfiles = EmailRepIO.get_profiles(email)
		self.text = ''
		self.text += "\n{}".format(emailProfiles)
		self.text += "\n----- BREACHES IT WAS FOUND IN--------\n"
		for item in sites:
			self.text += item['Name'] +'\n'
		msg = QMessageBox()
		msg.setWindowTitle("Results")
		
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()

	
	def get_breached_username_data(self):
		username = self.usernameUsernameTextField.text()

		self.text = Dehashed.retrieve_hits(username)

		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits For Username ")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()


	def get_real_name_hits(self):
		firstName = self.firstNameTextField.text()
		lastName = self.lastNameTextField.text()
		city = self.cityTextField.text()
		state = self.stateTextField.text()


		self.text = ThatsThem.get_results(firstName, lastName, city, state)

		msg = QMessageBox()
		msg.setWindowTitle("Results")
		msg.setInformativeText("Hits For Real Name ")
		msg.setText(self.text)

		msg.layout = QVBoxLayout()
		saveFiles = QPushButton("Save As", msg)
		
		saveFiles.clicked.connect(self.save_files)
		msg.layout.addWidget(saveFiles)

		val = msg.exec_()

	def save_files(self):
		name = QFileDialog.getSaveFileName(self, 'Save File')
		file = open(name[0],'wb')
		text = self.text
		self.text = ''
		file.write(bytes(text, 'utf-8'))
		file.close()





if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())
