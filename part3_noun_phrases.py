# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:46:20 2019

@author: gordon.garisch
"""

import os
os.chdir('C:\\Users\\gordon.garisch\\Documents\\Projects\\Stevens\\fe595\\FE595_Assignment3')

from textblob import TextBlob
from part1_data_cleaning import cleanTFC
import pprint

# =============================================================================
# Open file and read into variable
# =============================================================================
f = open(os.path.join(os.getcwd(),
                      "data\\output\\output.txt"),"r")
# =============================================================================
# Get clean data
# =============================================================================
shes, hes = cleanTFC(f.read())
f.close()
# =============================================================================
# Remove duplicates
# =============================================================================
shes = list(dict.fromkeys(shes))
hes = list(dict.fromkeys(hes))
# =============================================================================
# Create single string with all sentences
# =============================================================================
thems = '. '.join(hes) + '. ' + '. '.join(shes)
# =============================================================================
# Create TextBlob object
# =============================================================================
blob = TextBlob(thems)
# =============================================================================
# Extract noun-phrases
# =============================================================================
nps = blob.np_counts
# =============================================================================
# Print 10 most frequent noun-phrases with frequency
# =============================================================================
pprint.pprint(["Descriptor / Noun Phrase: \"{}\" has {} occurrences."
               .format(key, value)
               for (key, value) in 
               reversed(sorted(nps.items(), key=lambda x: x[1])[-10:])])

# =============================================================================
# Output from last run:
# ['Descriptor / Noun Phrase: "wrong side" has 21 occurrences.',
# 'Descriptor / Noun Phrase: "satanic" has 13 occurrences.',
# 'Descriptor / Noun Phrase: "wrong crowd" has 13 occurrences.',
# 'Descriptor / Noun Phrase: "god" has 13 occurrences.',
# 'Descriptor / Noun Phrase: "true killer" has 12 occurrences.',
# 'Descriptor / Noun Phrase: "wife \'s" has 12 occurrences.',
# 'Descriptor / Noun Phrase: "late maiden aunt" has 11 occurrences.',
# 'Descriptor / Noun Phrase: "incredible destiny" has 11 occurrences.',
# 'Descriptor / Noun Phrase: "mississippi" has 11 occurrences.',
# 'Descriptor / Noun Phrase: "secret government programme" has 11 occurrences.']
# =============================================================================
