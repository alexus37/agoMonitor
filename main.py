
import requests
import random
import json
import os
import time
from timeit import default_timer as timer


# constants
BASE_URL = "https://services9.arcgis.com/ZpmTCcECcEOnkrrK/ArcGIS/rest/services/Zurich_Master_Feature_Layer_V19_DEV_View/FeatureServer/6/query"
SAMPLE_TIMESTEP = 15 # in seconds
FEATURE_COUNT_DB = 40000
LOG_FILE = './logs.json'


def make_single_request():
  # get an random offset
  result_offset = random.randint(0, FEATURE_COUNT_DB)
  # create query url
  qry_url = f'{BASE_URL}?where=1%3D1&outFields=*&returnGeometry=true&resultRecordCount=50&f=pjson&resultOffset={result_offset}'

  r = requests.get(qry_url)
  return r


def main():
  logs = []

  if os.path.exists(LOG_FILE) and os.path.isfile(LOG_FILE):
    with open(LOG_FILE) as json_file:
      logs = json.load(json_file)
  i = 0

  # main loop
  while True:
    print(f"Running query ({i})")

    start = timer()
    response = make_single_request()
    end = timer()

    rtt = end - start

    response_json = response.json()

    logs.append({
      "ts": int(time.time()),
      "rtt": rtt,
      "httpStatus": response.status_code,
      "error": response_json['error'] if 'error' in response_json else ''
    })

    # write logs
    with open(LOG_FILE, 'w+') as json_file:
      json.dump(logs, json_file)

    i += 1
    print("====================================")
    time.sleep(SAMPLE_TIMESTEP)



if __name__ == '__main__':
    main()
