#given multiple fasta files of dna sequences, return the fasta with largest gc content 

'''
To solve this need to read in file and find a way to separate each fasta file. Can use .read() to save as string
Fasta sequences start with >, so could do fasta.split(">") to store each fasta in an element of a list
Will have to use nested for loops, and will have to selectively iterate over dna sequence

'''
#importing fastas
lst = [] 
with open("rosalind_gc.txt", "r") as opentxt:
    fastas = opentxt.read().split(">") 
    for element in fastas:
        if len(element) > 0:
            lst.append(element.replace(">", ""))
            
#I believe that the characters from rosalind fasta label interfere with accuracy of GC estimate
#there are also \n characters still left in the dna strings which will confound GC estimate
#need to remove \n and then will create a dictionary
#the dictionary should 
empty = []
for index, value in enumerate(lst):
     empty.append(value.split("\n", 1))

#now have list of lists where first element in list is fasta name and second element is dna string
#creating a dictionary where it is dnastring:fasta header
dict = {}
fasta_list = []
for lst in empty:
    for index, value in enumerate(lst):
        if index % 2 == 1:
            value = value.replace("\n", "")
            dict[value] = lst[index-1]
            fasta_list.append(value)

#counting amount of 
gc_value = 0
top_gc = ""
for fasta in fasta_list:
    counts = {}
    for nucleotide in fasta:
        if nucleotide in counts:
            counts[nucleotide] += 1
        else:
            counts[nucleotide] = 1
    gc_content = (counts["G"] + counts["C"])/len(fasta)
    if gc_content > gc_value:
        gc_value = gc_content
        top_gc = dict[fasta]
        
print(top_gc, "\n", gc_value*100)
