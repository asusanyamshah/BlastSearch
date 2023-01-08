from Bio.Blast import NCBIWWW, NCBIXML
import sys

# Access a file  
query = sys.argv[1] 

# Access database in a similar way
database = sys.argv[2]

# Accesses online BLAST
result_handle = NCBIWWW.qblast('blastp', database, query) 

#Parses the result_handle in XML Format and generates individual blast result.
blast_results = NCBIXML.parse(result_handle)

# Iterates through each result and gives the required values for each
for record in blast_results:
    for alignment in record.alignments:
        for hsp in alignment.hsps:
            print("Sequence", alignment.title)
            print("Length", alignment.length)
            print("e value", hsp.expect)
            print("Score", hsp.score)
            print("Indentity", hsp.identities)
            print("Gaps", hsp.gaps)
            print("Query_start", hsp.query_start)
            print("Query_end", hsp.query_end)
            print("Subject_start", hsp.subject_start)
            print("Subject_end", hsp.subject_end)