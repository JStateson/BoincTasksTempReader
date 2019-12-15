The two scripts here obtain temperature information from nvidia-smi an sensors
This info is reported to Boinctasks using the the Efmer "TThrottle" protocol

cpu temps:  will be the highest value of all the cores
GPU temps:  will be the current value of each GPU: ATI or NVidia

If your system contains a mix of both NVIdia and ATI then only the
manufacturer with the most cards will be reported at the present time


FetchTemps.ph - python 3  app tested on 18.04

run_cycle.sh - bash script that runs the python program every 10 seconds

