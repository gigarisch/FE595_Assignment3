# FE595_Assignment3
FE595 Assignment3

How to use these scripts:
1. Create folder of zip files containing .txt files
2. Update filepaths in the extract_zips.py file to reflect correct location of the zip files, and then run the extract_zips.py script
3. The part1_data_cleaning.py script cleans sentences in the output.txt file created in step 2. It is not necessary to run this script directly. It contains a function that is called by the other scripts
4. Run the part2_sentiment_by_gender.py script. The script cleans the data using the function referenced in item 3 above, and outputs the 10 best and worst male and female characters by sentiment (polarity using the TextBlob package); a total of 4 top 10 lists.
5. Run the part3_noun_phrases.py script. This script also cleans the data using the script referenced in item 3 above, then consolidats the lists of sentences into a body of text containing both male and female characters. It then finds all the noun-phrases, and outputs the 10 most frequently occuring noun-phrases with their respective frequencies.
