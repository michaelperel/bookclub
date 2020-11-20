# Run lights on Rpi 4
(1) Plug lights starting at GPIO 10
(2) Boot machine, SSH into it
(3) Install Docker
(4) On the host, `sudo chmod 777 /dev/gpiomem`
(5) `docker build -t lights .`
(6) `docker run -it --rm -v /dev:/dev --privileged lights`
