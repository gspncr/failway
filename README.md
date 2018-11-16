# failway
Frontend for tracking the schedule of a train route from National Rail. 

N.b. I am hosting this here as part of a docker pipeline into k8s, it is no official project by National Rail. 

# modifying the start / end stations
This is possible by modifying the values in `my_url` - check the format on National Rail Online Journey Planner.

# modifying the logging utility
This is possible in the logging.basicConfig. Change the file name and include a path (optional), you can change the logging level in the utility along with the format. The API details are at https://docs.python.org/3/library/logging.html

# deploying in kubernetes
I recommend deploying this in k8s or using an IaaS container service. If the number of requests becomes high then the IP is banned for a period of time by NatRail, k8s or an IaaS can take care of redeploying and new IPs when this happens.

# running the docker image
Find it at https://hub.docker.com/r/gspncr/failway/ this can also be used in the k8s deployment just provide gspncr/failway

# running the python script manually
`python3 nr.py &` will run the script silently and listens on port 80 - configure that at the bottom of the script in the Flask app setup. 
I changed the logging utility which would previously stream the logs. I am going to introduce stdout logging which makes the program even more portable, and benefits log streaming in kubernetes too.

# system requirements
I never seen it use more than 30mb of memory and CPU use is very low. I wouldn't worry but I mention it because if you are thinking to reserve resources in kubernetes I would not bother - it uses hardly any and k8s does a good job of looking after it :)
