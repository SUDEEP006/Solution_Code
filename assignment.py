# python assignment.py -input protein-sequences.tsv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-input', dest='infile', required=True, help='Input file of script.')
args = parser.parse_args()
infile=args.infile

inputf = open(infile,"r")
temp_list = []

for line in inputf:
    if line.startswith("Accession"):
        pass
    else:
        data = line.rstrip().split("\t")
        last_item = int(data[-1])
        temp_list.append(last_item)

# sort the eleemnts of list 
sorted_list = sorted(temp_list)

# creating string list for join elements
my_list = [str(i) for i in sorted_list]
final_out = "\n".join(my_list)

# printing sorted list of the last coloumn
print(final_out)

