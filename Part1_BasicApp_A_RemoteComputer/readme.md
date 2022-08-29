# Run instructions 

- Since this version has the __main__, you can run this flask app using the pythong command: 
    - `sudo python app.py` 
- Or you can use python3 if that is what is found on your machine: 
    - `sudo python3 app.py` 
- The reason why we need `sudo` permissions here, is that if we are deploying our app on a remote server, to port :80, which is a special port (e.g., website traffic), we need to have elevated permissions