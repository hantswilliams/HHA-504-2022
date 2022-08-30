## What is gunicorn? 
- https://gunicorn.org/
- https://vsupalov.com/what-is-gunicorn/ 

## Notes: 
- If starting this on a new machine: 
    - `sudo apt-get update`
    - `sudo apt install python3-pip`
    - `sudo apt install gunicorn3` // if get error gunicorn3 not found, redo sudo apt-get update
    - then install packages as normal: 
        - `pip install flask` 

# to deploy: 
`sudo gunicorn3 -w 2 -b 0.0.0.0:80 app:app`  
# -w = workers, set to 2 
# -b = base URL, set to 0.0.0.0 so it will go to whatever the IP is
# - app:app, means that our pythong file is called app (first app), and the second (:app) is default 
