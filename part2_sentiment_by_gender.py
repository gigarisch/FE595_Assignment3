# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:48:53 2019

@author: gordon.garisch
"""

import os
from textblob import TextBlob
from part1_data_cleaning import cleanTFC
import pprint

def sentiment_by_gender():
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
    

if __name__ == "__main__":
    sentiment_by_gender()
# =============================================================================
# Output from last run:
#'Worst 10 Female'
#["1. Polarity: -1.0 Sentence: She's a virginal African-American cab driver "
# 'with an evil twin sister, ',
# "2. Polarity: -1.0 Sentence: She's a tortured hip-hop barmaid with an evil "
# 'twin sister, ',
# "3. Polarity: -0.8 Sentence: She's a violent bisexual lawyer from Mars ",
# "4. Polarity: -0.6 Sentence: She's a cynical communist Valkyrie fleeing from "
# 'a Satanic cult ',
# "5. Polarity: -0.6 Sentence: She's a cynical communist magician's assistant "
# 'from beyond the grave ',
# "6. Polarity: -0.6 Sentence: She's a cynical belly-dancing opera singer "
# 'fleeing from a Satanic cult ',
# "7. Polarity: -0.6 Sentence: She's a cynical gold-digging nun prone to fits "
# 'of savage, blood-crazed rage ',
# "8. Polarity: -0.6 Sentence: She's a cynical cigar-chomping soap star with "
# "someone else's memories, ",
# "9. Polarity: -0.5 Sentence: She's a time-travelling insomniac advertising "
# 'executive from the wrong side of the tracks ',
# "10. Polarity: -0.5 Sentence: She's a chain-smoking extravagent magician's "
# 'assistant operating on the wrong side of the law ']
#'Best 10 Female'
#["1. Polarity: 0.9 Sentence: She's a manipulative belly-dancing museum curator "
# 'with an incredible destiny, ',
# "2. Polarity: 0.9 Sentence: She's a brilliant motormouth bodyguard with an "
# 'incredible destiny ',
# "3. Polarity: 0.9 Sentence: She's a cold-hearted snooty bodyguard with an "
# 'incredible destiny ',
# "4. Polarity: 0.9 Sentence: She's a manipulative psychic opera singer with an "
# 'incredible destiny ',
# "5. Polarity: 0.9 Sentence: She's a brilliant insomniac Hell's Angel from "
# 'beyond the grave ',
# "6. Polarity: 0.85 Sentence: She's a beautiful insomniac opera singer with an "
# 'MBA from Harvard ',
# "7. Polarity: 0.85 Sentence: She's a beautiful bisexual widow with a "
# 'flame-thrower ',
# "8. Polarity: 0.7 Sentence: She's a brilliant bisexual safe cracker with "
# "someone else's memories ",
# "9. Polarity: 0.6 Sentence: She's a tortured antique-collecting college "
# 'professor with her own daytime radio talk show ',
# "10. Polarity: 0.6 Sentence: She's a green-fingered tomboy angel with her own "
# 'daytime radio talk show ']
#'Worst 10 Male'
#["1. Polarity: -0.875 Sentence: He's a one-legged devious paranormal "
# "investigator plagued by the memory of his family's brutal murder ",
# "2. Polarity: -0.875 Sentence: He's a benighted drug-addicted messiah plagued "
# "by the memory of his family's brutal murder ",
# "3. Polarity: -0.875 Sentence: He's an old-fashioned playboy grifter plagued "
# "by the memory of his family's brutal murder ",
# "4. Polarity: -0.875 Sentence: He's a leather-clad one-eyed filmmaker plagued "
# "by the memory of his family's brutal murder ",
# "5. Polarity: -0.875 Sentence: He's a genetically engineered moralistic "
# "dog-catcher plagued by the memory of his family's brutal murder ",
# "6. Polarity: -0.875 Sentence: He's a hate-fuelled playboy firefighter "
# "plagued by the memory of his family's brutal murder ",
# "7. Polarity: -0.7 Sentence: He's an obese misogynist barbarian on a mission "
# 'from God ',
# "8. Polarity: -0.7 Sentence: He's a world-famous dishevelled barbarian "
# 'looking for a cure to the poison coursing through his veins ',
# "9. Polarity: -0.7 Sentence: He's a hate-fuelled pirate barbarian on a "
# 'mission from God ',
# "10. Polarity: -0.6999999999999998 Sentence: He's an unconventional "
# 'umbrella-wielding ex-con gone bad ']
#'Best 10 Male'
# ["1. Polarity: 0.4333333333333333 Sentence: He's a superhumanly strong flyboy "
# 'romance novelist from a doomed world, ',
# "2. Polarity: 0.4333333333333333 Sentence: He's a superhumanly strong flyboy "
# 'romance novelist in a wheelchair ',
# "3. Polarity: 0.4166666666666667 Sentence: He's a war-weary gay cowboy who "
# 'must take medication to keep him sane ',
# "4. Polarity: 0.4166666666666667 Sentence: He's a hate-fuelled gay "
# 'photographer from a doomed world ',
# "5. Polarity: 0.41111111111111115 Sentence: He's a superhumanly strong pirate "
# 'assassin on the hunt for the last specimen of a great and near-mythical '
# 'creature ',
# "6. Polarity: 0.41111111111111115 Sentence: He's a superhumanly strong "
# 'small-town paranormal investigator on the hunt for the last specimen of a '
# 'great and near-mythical creature ',
# "7. Polarity: 0.4055555555555556 Sentence: He's a notorious gay househusband "
# 'with a winning smile and a way with the ladies ',
# "8. Polarity: 0.4 Sentence: He's a one-legged voodoo librarian on the hunt "
# 'for the last specimen of a great and near-mythical creature ',
# "9. Polarity: 0.4 Sentence: He's a maverick drug-addicted dwarf with a "
# 'winning smile and a way with the ladies ',
# "10. Polarity: 0.4 Sentence: He's a one-legged sweet-toothed messiah on the "
# 'hunt for the last specimen of a great and near-mythical creature ']
# =============================================================================
