from emailrep import EmailRep
import json

# setup your api key (optional)
with open('auth.json') as json_file:
	data = json.load(json_file)


emailrep = EmailRep(data['emailrepiokey'])



def get_profiles(email = 'justinwilliams171@yahoo.com'):
    # query an email address
    answer = ''
    
    try:
        results = emailrep.query(email)
    
    except Exception as e:
        return "Failed Becuase of a {}".format(e)
    
    
    answer += '\nEmail: {}'.format(results['email'])
    answer += '\nReferences: {}'.format(results['references'])
    answer += '\n Profiles: {}'.format(results['details']['profiles'][:])
    answer += '\nSummary: {}'.format(results['summary'])

    return answer
