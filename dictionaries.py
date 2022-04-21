#given a string s, return the number of occurences of each word in s, separated by spaces. lines in output can be any order
import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()


'''
solution: 
each word can be saved as a key in the dictionary, then print keys
can dynamically define words by:
    > 1. s.split() to create a list of words
    > 2. create an empty list and iterate over list. dynamically save .count to {word: word.count}
'''

def word_counter(string):
    dict = {}
    for word in string.split(" "):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    
    for key, value in dict.items():
        print(key, value)
    
# %%
#testing function
word_counter("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")
