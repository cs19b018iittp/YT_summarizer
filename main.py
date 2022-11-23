from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from youtube_transcript_api.formatters import TextFormatter

def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

def get_summary(transcript):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    return summarizer(transcript, max_length=130, min_length=30, do_sample=False)

def main():
    video_id = 's_ht4AKnWZg'

    transcript_list = get_transcript(video_id)

    formatter = TextFormatter()

    text_transcript = formatter.format_transcript(transcript_list)
    
    if(text_transcript == None):
        print('Null Value')
    else:
        summary = get_summary(text_transcript)
        print(summary)

    print('Done!!!')

if __name__ == '__main__':
    main()