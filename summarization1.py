import g4f

from g4f.Provider import You

from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi

videosSearch = VideosSearch("New Zealand's News Today", limit = 5)

videoids = []

for video in videosSearch.result().get("result"):
    print(video.get("title")) # the output includes keys such as 'title', 'id', 'duration', etc.
    videoids.append(video.get("id"))

for id in videoids:
    transcripts = YouTubeTranscriptApi.get_transcript(id)
    paragraph = ""
    for transcript in transcripts:
        sentence = transcript["text"]
        savedSentence = ""
        isSaving = True
        for character in sentence:
            if (character == '['):
                isSaving = False
            elif (character == ']'):
                isSaving = True
            elif (isSaving == True):
                savedSentence += character
        duration = transcript["duration"]
        if duration > 6.5:
            paragraph += savedSentence + ".\n"
        else:
            paragraph += savedSentence + " " 

    print(paragraph)

response=g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.Vercel,
    messages=[{"role":"user","content":"Please summarize the news:"+paragraph}],
    )

print(response + "\n\n\n\n")


























 
