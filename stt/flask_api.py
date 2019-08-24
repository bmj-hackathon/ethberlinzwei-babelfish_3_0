from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import wave
import random
import json
from deepspeech import Model, printVersions
from timeit import default_timer as timer

# Load config file
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

app = Flask(__name__)


def setup_model(config):
    # Load and setup model with parameters specified in config file
    ds_model = Model(
        config['deepspeech']['model'],
        config['deepspeech']['features']['n_features'],
        config['deepspeech']['features']['n_context'],
        config['deepspeech']['alphabet'],
        config['deepspeech']['features']['beam_width'])

    if config['deepspeech']['lm'] and config['deepspeech']['trie']:
        ds_model.enableDecoderWithLM(
            config['deepspeech']['alphabet'],
            config['deepspeech']['lm'],
            config['deepspeech']['trie'],
            config['deepspeech']['features']['lm_alpha'],
            config['deepspeech']['features']['lm_beta'])
    return ds_model


# Initialize model
model = setup_model(config)


@app.route('/stt', methods=['POST'])
def predict():
    # Get the probability of being a 'bad' audio2text processor
    prob = request.args.get('prob', default=0, type=float)
    # Get the data from the POST request.
    data = request.stream
    fin = wave.open(data)
    fs = fin.getframerate()
    audio = np.frombuffer(fin.readframes(fin.getnframes()), np.int16)
    # audio_length = fin.getnframes() * (1 / 16000)
    fin.close()
    inference_start = timer()
    solution = model.stt(audio, fs)
    inference_end = timer() - inference_start
    resp = {'solution': solution.strip(), 'error': False, "time": inference_end, 'fraud_probability': prob}
    if random.random() < prob:
        # Create 'bad' transcript (shuffle the words in the text and remove 2 words
        # if there are at least 4 words in the transcript)
        sol = resp['solution'].split()
        random.shuffle(sol)
        if len(sol) >= 4:
            resp['solution'] = ' '.join(sol[:-2])
        else:
            resp['solution'] = ' '.join(sol)
    return jsonify(resp)


if __name__ == '__main__':
    app.run(host=config['server']['http']['host'],
            port=config['server']['http']['port'],
            debug=True)
