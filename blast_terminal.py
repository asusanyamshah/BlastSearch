import sys
from Bio.Blast import NCBIWWW, NCBIXML

query = sys.argv[1]
database = sys.argv[2]

result_handle = NCBIWWW.qblast('blastp', database, query)

blast_records = NCBIXML.parse(result_handle)

for record in blast_records:
    for alignment in record.alignments:
        for hsp in alignment.hsps:
            print("Sequence", hsp.title) 
            print("Length", hsp.length) 
            print("e value", hsp.expect) 
            print("Score", hsp.score)
            print("Identity", hsp.indentities) 
            print("Gaps", hsp.gaps) 
            print("query_start", hsp.query_start) 
            print("query_end", hsp.query_end) 
            print("subject_start", hsp.subject_start) 
            print("subject_end", hsp.subject_end) 
