from wtforms.validators import ValidationError, DataRequired, URL
from youtube_transcript_api import YouTubeTranscriptApi
import json
import openai
import re
import os
regex = "(?<=\=).*"
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_video_text(yturl):
        id = re.findall("(?<=\=).*",yturl)
        print(id)
        data = YouTubeTranscriptApi.get_transcript(id[0])

        sentence = ""
        for i in range(0,int(len(data))):
            sentence += " "
            sentence += data[i]["text"]
        sentence +="\n"
        sentence += "tl;dr:"
        return sentence

def create_summary(sentence):
    response = openai.Completion.create(
        engine="davinci",
        prompt=sentence,
        temperature=0.3,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response["choices"][0]["text"]
