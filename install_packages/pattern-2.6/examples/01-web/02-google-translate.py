import os, sys; sys.path.insert(0, os.path.join("..", ".."))

from pattern.web import Google, plaintext

# Search engines in pattern.web sometimes have custom methods that others don't.
# For example, Google has Google.translate() and Google.identify().

# This example demonstrates the Google Translate API.
# It will only work with a license key, since it is a paid service.
# In the Google API console (https://code.google.com/apis/console/), 
# activate Translate API.

g = Google(license=None) # Enter your license key.
q = "Your mother was a hamster and your father smelled of elderberries!"    # en
#   "Ihre Mutter war ein Hamster und euer Vater roch nach Holunderbeeren!"  # de
print q
print plaintext(g.translate(q, input="en", output="de")) # fr, de, nl, es, cs, ja, ...
print

q = "C'est un lapin, lapin de bois, un cadeau."
print q
print g.identify(q)