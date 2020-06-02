# SeniorDesign

## Setup

Once the repository is cloned, run 

-pip3 install -r requirements.txt



-python3 SeniorDesignDesktop.py



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

-Phone.py uses twilio. You must first create an account with Twilio. 
-Then you should see your dashboard. Click the *three dots* on the left toolbar.
-Scroll down to *"SUPER NETWORK"* and click *"LOOKUP"*. Then click add-ons.
-Then click the *"Ekata reverse phone lookup"* and click install.
-After that copy the Account SID thats presented with the add-on *(DO NOT USE THE ONE ON YOUR HOME DASHBOARD)*. Go to your home dashboard.
-Copy your auth token (On your home dashboard) and paste them in the auth.json file.
