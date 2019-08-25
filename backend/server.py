from flask import Flask
from flask import jsonify
from flask import request
from scipy.io.wavfile import read as wavread
from scipy.io.wavfile import write as wavwrite
import numpy as np
import wave
import cgi
import contextlib
import base64
import soundfile as sf
from flask_cors import CORS, cross_origin
import subprocess

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def post():
    with open("file.wav", "wb") as vid:
        vid.write(request.data)

    proc = subprocess.Popen(
        "deepspeech --model /home/magda/deepspeech-models/output_graph.pbmm --alphabet /home/magda/deepspeech-models/alphabet.txt --lm /home/magda/deepspeech-models/lm.binary --trie /home/magda/deepspeech-models/trie --audio file.wav",
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    print(output)

    return jsonify(
        username=output.decode('utf-8')
    )

@app.route('/file', methods=['POST'])
@cross_origin()
def post1():
    with open("file.wav", "wb") as vid:
        vid.write(request.data)

    proc = subprocess.Popen(
        "deepspeech --model /home/magda/deepspeech-models/output_graph.pbmm --alphabet /home/magda/deepspeech-models/alphabet.txt --lm /home/magda/deepspeech-models/lm.binary --trie /home/magda/deepspeech-models/trie --audio file.wav",
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    print(output)

    return jsonify(
	username=output.decode('utf-8')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
