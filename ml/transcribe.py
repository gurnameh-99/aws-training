import boto3

# create client object
transcribe = boto3.client('transcribe')

# specify the audio file to transcribe
job_name = "example-job"
job_uri = "s3://example-bucket/example-audio-file.mp3"

# call the start_transcription_job method to start the transcription job
response = transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp3',
    LanguageCode='en-US'
)

# wait for the transcription job to complete
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break

# get the transcription results
if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    response = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    transcription = response['TranscriptionJob']['Transcript']['TranscriptText']
    print(transcription)
else:
    print("Transcription job failed.")

