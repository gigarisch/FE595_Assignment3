# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:48:53 2019

@author: gordon.garisch
"""

import os
os.chdir('C:\\Users\\gordon.garisch\\Documents\\Projects\\Stevens\\fe595\\FE595_Assignment3')

from textblob import TextBlob
from data_cleaning import cleanTFC
import pprint

# =============================================================================
# Open file and read into variable
# =============================================================================
f = open(os.path.join(os.getcwd(),
                      "data\\output\\output.txt"),"r")
# ===================================a==========================================
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
# Create dictionaries for the following:
# 1. Item Number
# 2. Sentence
# 3. Polarity of Sentence
# 4. Subjectivity of Sentence
# =============================================================================
shes_dict = dict(zip(['number','sentence','pol','sub'],
                     [list(range(len(shes))),
                      shes,
                      [TextBlob(j).sentiment[0] for j in shes],
                      [TextBlob(j).sentiment[1] for j in shes]]))

hes_dict = dict(zip(['number','sentence','pol','sub'],
                     [list(range(len(hes))),
                      hes,
                      [TextBlob(j).sentiment[0] for j in hes],
                      [TextBlob(j).sentiment[1] for j in hes]]))
# =============================================================================
# Identify IDs sorted by polarity
# =============================================================================
shes_sort=sorted(range(len(shes_dict['pol'])),
                 key=lambda k: shes_dict['pol'][k])
hes_sort=sorted(range(len(hes_dict['pol'])),
                 key=lambda k: hes_dict['pol'][k])
# =============================================================================
# Print Results
# =============================================================================
pprint.pprint("Worst 10 Female")
pprint.pprint(["{}. Polarity: {} Sentence: {} "
               .format(t+1,shes_dict['pol'][i] ,shes_dict['sentence'][i])
               for (t,i) in enumerate(shes_sort[:10])])
pprint.pprint("Best 10 Female")
pprint.pprint(["{}. Polarity: {} Sentence: {} "
               .format(t+1,shes_dict['pol'][i] ,shes_dict['sentence'][i])
               for (t,i) in enumerate(reversed(shes_sort[-10:]))])
pprint.pprint("Worst 10 Male")
pprint.pprint(["{}. Polarity: {} Sentence: {} "
               .format(t+1,hes_dict['pol'][i] ,hes_dict['sentence'][i])
               for (t,i) in enumerate(hes_sort[:10])])
pprint.pprint("Best 10 Male")
pprint.pprint(["{}. Polarity: {} Sentence: {} "
               .format(t+1,hes_dict['pol'][i] ,hes_dict['sentence'][i])
               for (t,i) in enumerate(reversed(hes_sort[-10:]))])

