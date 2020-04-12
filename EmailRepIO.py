from emailrep import EmailRep

# setup your api key (optional)
emailrep = EmailRep('ccrg639u7k41n7wqg3xppt4kq2dvymo3eakwhlsta151p420')



def get_profiles(email = 'justinwilliams171@yahoo.com'):
    # query an email address
    answer = ''
    results = emailrep.query(email)
    answer += '\nEmail: {}'.format(results['email'])
    answer += '\nReferences: {}'.format(results['references'])
    answer += '\n Profiles: {}'.format(results['details']['profiles'][:])
    answer += '\nSummary: {}'.format(results['summary'])

    return answer
