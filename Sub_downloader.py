from youtube_transcript_api import YouTubeTranscriptApi


def start_calc(time):
    seconds = int(time%60)
    if int(time/60) > 60:
        hours = int(time/3600)
        minutes = int(time%3600/60)
    else:
        minutes = int(time/60)
        hours = 0
    return ("{}:{}:{}".format(hours, minutes, seconds))


'''Prints transcription of a youtube video at a given url. Runs if the user selects anything but yes on the phrase lookup question.'''
def yt_trans(url, is_id=False): 
    trans_text = ''
    if is_id:
        transcript =(YouTubeTranscriptApi.get_transcript(url))
        for x in transcript:
            trans_text = str(trans_text) + " " + str(x['text'])
        return ((trans_text))
    else:
        if 'v=' in str(url):
            id = str(url).split('v=')[-1]
            url = 'https://youtu.be/' + id
            transcript =(YouTubeTranscriptApi.get_transcript(id))

        else:
            id = str(url).split('/')[-1]
            url = 'https://youtu.be/' + id
            transcript =(YouTubeTranscriptApi.get_transcript(id))

        
        for x in transcript:
            trans_text = str(trans_text) + " " + str(x['text'])
        return ((trans_text))

'''looks through the transcript of a youtube video at the given url and checks if the phrase asked for is in that transcript. if it is it returns the phrase used and the timestamp of where it is in the video,as well as a link to that spot.'''
def yt_search(url, phrase, is_id=False):
    if is_id:
        id= url
        url = 'https://youtu.be/' + id 
    elif 'v=' in str(url):
        id = str(url).split('v=')[-1]
        url = 'https://youtu.be/' + id
    else:
        id = str(url).split('/')[-1]
        url = 'https://youtu.be/' + id
    try:
        subs = (YouTubeTranscriptApi.get_transcript(id))
        a=b=c=d=e= ""
        for x in subs:
            e = d
            d = c
            c = b
            b = a
            a = x['text'] + " "
            saying = e + d + c + b + a
            if str(phrase) in x['text']:
                print(" '{}' was said at {}".format(saying, str(start_calc(x['start']))))
                print("The link to this use is at {}?t={}".format(url, int(x['start']-5)))
                print(" ")
                print(" ")
    except:
        print("Video {} does not have a subtitles.".format(id))

# print(yt_trans("https://www.youtube.com/watch?v=ZA106wrMUe4&t=276s"))



'''
input_url = str(input("What is your youtube videos URL? "))

if len(input_url) == 11:
    check = str(input("Would you like to search for something specific? [Y/N]")).upper()
    yes_check = ['YES', 'Y']
    if check in yes_check:
        search_will_run = True
        phrase = str(input('What word or phrase would you like to search for?'))
    else:
        search_will_run = False
    if search_will_run:
        yt_search(input_url, phrase, True)
    else:
        yt_trans(input_url, True)
if "youtu" in input_url:
    check = str(input("Would you like to search for something specific? [Y/N]"))
    yes_check = ['Yes', 'Y', 'y', 'yes']
    if check in yes_check:
        search_will_run = True
        phrase = str(input('What word or phrase would you like to search for?'))
    else:
        search_will_run = False
    if search_will_run:
        yt_search(input_url, phrase)
    else:
        yt_trans(input_url)
'''
