from Bio.Blast import NCBIWWW, NCBIXML

query = str(input("Enter Sequence: "))
database = ''

result_handle = NCBIWWW.qblast('blastp', database, query)

blast_results = NCBIXML.parse(result_handle)

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