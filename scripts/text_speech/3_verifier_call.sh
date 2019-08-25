echo "Oracalizing 5 transcriber nodes"
echo "Recieved 0.1 ETH reward"
echo "Submitting text from all transcribers to verifier..."
curl -X POST --data-binary @results.json http://0.0.0.0:8080/verify                      
echo "Verification complete, processing payment"
echo "Text transmitted, job complete"
