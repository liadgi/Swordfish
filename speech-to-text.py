import io
import os
import subprocess

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


gcs_uri = "gs://lecture-videos/audio.flac"
# Instantiates a client
client = speech.SpeechClient()


audio = types.RecognitionAudio(uri=gcs_uri)
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=16000,
    language_code='he-IL')

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
response = operation.result()

import pdb; pdb.set_trace()

# Each result is for a consecutive portion of the audio. Iterate through
# them to get the transcripts for the entire audio file.
for result in response.results:
    # The first alternative is the most likely one for this portion.
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))