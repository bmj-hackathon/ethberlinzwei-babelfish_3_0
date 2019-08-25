from flask import Flask
from flask import jsonify
from flask import request
from scipy.io.wavfile import read as wavread
from scipy.io.wavfile import write as wavwrite
from fraud_detection import fraud_score
import numpy as np
import wave
import cgi
import contextlib
import base64
import soundfile as sf
from flask_cors import CORS, cross_origin
import subprocess
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['POST'])
@cross_origin()
def post():
    # Get the probability of being a 'bad' audio2text processor
    prob = request.args.get('prob', default=0.0, type=float)
    # Get the data from the POST request.
    with open("file.wav", "wb") as vid:
        vid.write(request.data)

    proc = subprocess.Popen(
        "deepspeech --model /home/magda/deepspeech-models/output_graph.pbmm --alphabet /home/magda/deepspeech-models/alphabet.txt --lm /home/magda/deepspeech-models/lm.binary --trie /home/magda/deepspeech-models/trie --audio file.wav",
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0].decode('utf-8')
    print(output)
    if random.random() < prob:
        # Create 'bad' transcript (shuffle the words in the text and remove 2 words
        # if there are at least 4 words in the transcript)
        sol = str(output).strip().split()
        random.shuffle(sol)
        if len(sol) >= 4:
            output = ' '.join(sol[:-2])
        else:
            output = ' '.join(sol)
    return jsonify(username=output)


@app.route('/file', methods=['POST'])
@cross_origin()
def post1():
    # Get the probability of being a 'bad' audio2text processor
    prob = request.args.get('prob', default=0.0, type=float)
    # Get the data from the POST request.  
    with open("file.wav", "wb") as vid:
        vid.write(request.data)

    proc = subprocess.Popen(
        "deepspeech --model /home/magda/deepspeech-models/output_graph.pbmm --alphabet /home/magda/deepspeech-models/alphabet.txt --lm /home/magda/deepspeech-models/lm.binary --trie /home/magda/deepspeech-models/trie --audio file.wav",
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0].decode('utf-8')
    print(output)
    if random.random() < prob:
        # Create 'bad' transcript (shuffle the words in the text and remove 2 words
        # if there are at least 4 words in the transcript)
        sol = str(output).strip().split()
        random.shuffle(sol)
        if len(sol) >= 4:
            output = ' '.join(sol[:-2])
        else:
            output = ' '.join(sol)
    return jsonify(username=output)



@app.route('/verify', methods=['POST'])
def verification():
#Sample json file: 
#	{
#	  "0": "there's no coffee because you forgot to buy it",
#	  "1": "there is no coffee because you forgot to buy it",
#	  "2": "there is coffee because you forgot to buy it",
#	  "3": "there's no coffee because you forget to buy it",
#	  "4": "because there's forgot but to it you no"
#	}	
#	Output:
#	'1.0,1.0,1.0,1.0,0.0'
    results = request.get_json(force=True)
    transcripts = list(results.values())
    print(transcripts)
    verification = fraud_score(transcripts)
    output = ','.join(verification)
    return jsonify(
        output
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
