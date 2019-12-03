# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:59:23 2019

@author: gordon.garisch
"""

def top_output(they_dict, top=10, best=False, key='pol'):
    '''
    Function sorts dict based on provided key and outputs to top
    specified numbers of entries and the associated senstence.
    
    Dict is assumed to have a 'sentence' key.
    
    By default the top 10 worst outcomes by polarity is returned.
    '''
    # =============================================================================
    # Identify IDs sorted by polarity
    # =============================================================================
    assert key in they_dict.keys(), 'Provided key not in dictionary'
    assert top <= len(they_dict[key]), 'Provided key not in dictionary'
    they_sort=sorted(range(len(they_dict[key])),
                     key=lambda k: they_dict[key][k],reverse=best)
    
    return["{}. Polarity: {} Sentence: {} "
                   .format(t+1,they_dict[key][i] ,they_dict['sentence'][i])
                   for (t,i) in enumerate(they_sort[:top])]