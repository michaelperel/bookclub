FROM mperel/dev-container

RUN sudo apt-get update && \
    sudo apt-get install -y python3-rpi.gpio

COPY main.py .

CMD python main.py
