from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt
import time
import os

# Replace 'client = mqtt.Client()' with:
# The IP of your Ubuntu Server
BROKER_IP = "192.168.40.129"
PORT = 30001 
# read the file


FILE_PATH = "/home/florian/Documents/20260120_kinoko/record_streamlit.tsv"
TOPIC = "/home/florian/Documents/record_streamlit.tsv"

client = mqtt.Client(CallbackAPIVersion.VERSION2)
client.connect(BROKER_IP, PORT)

def follow(the_file):
    """ Yield each new line added to a file. """
    the_file.seek(0, os.SEEK_END) # Go to the end of the file
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(0.1) # Wait briefly for new data
            continue
        yield line

if __name__ == "__main__":
    print(f"Watching {FILE_PATH} and pushing to {BROKER_IP}...")
    with open(FILE_PATH, "r") as f:
        for new_line in follow(f):
            clean_line = new_line.strip()
            if clean_line:
                client.publish(TOPIC, clean_line)
                print(f"Pushed: {clean_line}")
