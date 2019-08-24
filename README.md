# ethberlinzwei-babelfish_3_0
EthBerlinZwei hackathon submission for a decentralized speech to text service!

## Team 

[Marcus](https://github.com/MarcusJones) - Full stack

[Magdalena](https://github.com/mtagda) - Data Science


## Concept

Speech to text transcription is the problem tackled in this project. This is furthermore a demo and hack for generalized compute and AI services which are orchestrated, incentivized, scaled, and secured by Ethereum smart contracts! 

There exist several popular transcription services, for example, the [Google Speech-To-Text](https://cloud.google.com/speech-to-text/) API. 

But wait, are you willing to give away your sensitive audio speech files to a FANG company? What if you could be rewarded for providing your speech audio file? And what about competition and price discovery? 

Project **babelfish 3.0** envisions and enables a mobile DApp which puts the power back in your hands. 

As a user, you specify the price for your data (0 if you want to only purchase the transcription), the reward offered to the processor services, and the number of processor nodes. With these settings, your audio file is securely registered into the Ocean Protocol decentralized data registry. 

Next, the processor nodes bid on offering the requested service. The chosen processors execute the transcription task, and submit (oracalize) their results to a verifier smart contract. 

The verifier 

## Scope of the project

### Prior work, libraries, 
This project makes use of the open source [Ocean Protocol](https://oceanprotocol.com/) project to register and 'own' data assets. 

### Implemented

 * Interfacing to Ocean Protocol for *registration* of audio file via python client library. 
 * Interfacing to Ocean Protocol for *download* of audio by processors
 * Transcription of audio using the open source [DeepSpeech](https://github.com/mozilla/DeepSpeech) tensorflow library and pre-trained model.
 * Productionization of the transcription service to AWS using python Flask
 * Simulation of the verifier service
 
### Not implemented / WIP

 * Verifier smart contract not programmed in solidity or deployed
 * Full end-end integration (manual walkthrough, see below)
 
## Deep dive: Transcription service
 
## Deep dive: End to end user story

