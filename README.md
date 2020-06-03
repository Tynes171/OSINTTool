# OSINT (Concept) Tool

## Setup

Once the repository is cloned, run 

-pip3 install -r requirements.txt

-python3 SeniorDesignDesktop.py

-THe GUI Will run but you must set everything (SEE BELOW) For the functionalities to work

## APIS

Create an auth.json file like this

{
    
    "twilioSID":"",
    "twilioToken":"",
    "dehasheduser":"",
    "dehashedkey":"",
    "emailrepiokey":"",
    "instagramusername":"",
    "instagrampassword":""


}



## Phone.py
```
-Phone.py uses twilio. You must first create an account with Twilio. 

-Then you should see your dashboard. Click the *three dots* on the left toolbar.

-Scroll down to *"SUPER NETWORK"* and click *"LOOKUP"*. Then click add-ons.

-Then click the *"Ekata reverse phone lookup"* and click install.

-After that copy the Account SID thats presented with the add-on *(DO NOT USE THE ONE ON YOUR HOME DASHBOARD)*. Go to your home dashboard.

-Copy your auth token (On your home dashboard) and paste them in the auth.json file.
```


## Instagram.py
```
-Instagram.py Uses instaloader as its main function.

-To set this up all you have to do is create an instagram account 

-Put in your credentials In the auth.json file

-You can download profile data from someones instagram. 

-If a persons profile is private, then you must be following them to download their data
```


## EmailRepIO.py
```
-EmailRepIO.py Uses EmailRepIO as its main function.

-Go to emailrepio.com and click "API KEY"

-Choose which one free or paid, then fill out the information.

-Afterwards, check your email and there is your API Key

-Paste this in the auth.json file
```