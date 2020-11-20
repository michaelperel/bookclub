# Run lights on Rpi 4
* Plug lights starting at GPIO 10
* Boot machine, SSH into it
* Install Docker
* Clone this repo
* `sudo chmod 777 /dev/gpiomem`
* `docker build -t lights .`
* `docker run -it --rm -v /dev:/dev --privileged lights`
