# usere inputs a number indicating how many times he wants the sequense to go on.
#we use a for loop and loop as many times as the user wants.
#the sequence works like this, we plus the last 3 digits of the sequence to get the new number for the sequence
#then we repeat this printing out all the numbers in the seq
#
#
#
#
#
#


n = int(input("Enter the length of the sequence: ")) # Do not change this line
seq1 = int(0)
seq2 = int(0)
seq3 = int(1)
seq_max = int(0)
for i in range(1, n + 1):
    seq1 = seq2
    seq2 = seq3
    seq3 = seq_max
    seq_max = seq1 + seq2 + seq3
    print(seq_max)
