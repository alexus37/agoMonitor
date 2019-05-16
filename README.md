# ArcGIS Online basic monitoring tool

Display monitoring information from agol as chart and basic stats.

## Run connect to AWS

```
ssh -i "agolMonitorESRI.pem" ubuntu@ec2-54-188-129-23.us-west-2.compute.amazonaws.com
```

Run the sampler as well as a simple http server via screen

```
  python3 -m http.server 80 (as sudo)
  python3 main.py 30
```
