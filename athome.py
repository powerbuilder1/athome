import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')

print(IP_NETWORK)