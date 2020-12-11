# mapit.py - tool to search physical addresses
# usage -- python  mapit.py 6600 Williams Road Richmond
# output: should take us to the address in google maps

import webbrowser
import sys

# TODO: read the arguments from the command line
address = " ".join(sys.argv[1:])
print(address)
# TODO: open the browser at a Gmaps page with the arguments
prefix = "https://google.com/maps/place/"
webbrowser.open(prefix + address)

# TODO: add feature to grab address from clipboard




