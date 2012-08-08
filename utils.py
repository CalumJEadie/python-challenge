TEXT_PATH = 'data/%s/text' 

def get_text(challenge_id):
    return open(TEXT_PATH % challenge_id).read()
