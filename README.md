# Run lights on Rpi 4
* Plug in lights starting at GPIO 10
* Boot machine, SSH into it
* Install Docker
* Clone this repo
* `sudo chmod 777 /dev/gpiomem`
* `docker build -t lights .`
* `docker run -it --rm -v /dev:/dev --privileged lights`

## Simple Teams Light that does not use AAD or Graph API. 

Teams writes out a log file by default and one of the bits of information it logs is the change of status for the user. We can scrape these logs by running a small python app on the same PC as the Teams client and react to status changes. In this case we simply call an API on the Pi with the updated status (Busy, Available etc.) which sets the light color accordingly. 

### To run the app
Run *teamslight.py* on the Raspberry Pi with the Traffic light plugged in. 
- Note the IP address of the Raspberry Pi and set it to the *host* variable. 

Run *teamslogwatch.py* on your laptop where the Teams client is running. 
- Look in the Teams settings for the location of the log file and update the variable *teams_logfile* in this file before running it. 
- This will watch the log file for changes and parse it looking for status updates. After parsing the status, it will call the API on the Pi to PUT the status. 
- Note that this was tested using Teams version 1.3.00.33674.
- Also update the variable *pi_url* with the IP address of the Raspberry Pi from above. 
