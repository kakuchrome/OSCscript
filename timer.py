import argparse
import time , datetime 
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)
  
dt_now =  datetime.datetime.now()
base = datetime.time(7, 0, 0)
now = dt_now.time()

if __name__ == '__main__':
    while True:
        # when realtime is beyond 7am then set timer osc parameter to true
        if base > now :
            client.send_message("/avatar/parameters/timer", 0)
            print("timer off ")
        else:
            client.send_message("/avatar/parameters/timer", 1)
            print("timer on ")
        time.sleep(60)
