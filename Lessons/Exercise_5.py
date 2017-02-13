#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from rna import RNATranslationTable

def get_transcript_id(attr_list):
    for attr in attr_list:
        if 'transcript_id' in attr:
            return attr
    raise ValueError('I did not find a transcript_id')


with open('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.dna.chromosome.7.fa', 'r', encoding='utf-8') as DNA:
    lines_after_begin = DNA.readlines()[1:]
    sequence = []

    for line in lines_after_begin:
        line = line.strip()
        sequence.append(line)

    complete_list = "".join(sequence)

with open('/Users/salendrapradh/Downloads/Homo_sapiens.GRCh38.87.gtf', 'r', encoding='utf-8') as GTF:
    transcripts = {}
    start_end =[]

    for line in GTF:
        if line.startswith('#'):
            continue
        else:
            fields = line.split('\t')
            biotype = fields[2]
            chromosome = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            gene = fields[-1]

        if ("exon" == biotype) and ("7" == chromosome) and ("ENSG00000001626" in gene):
                id = get_transcript_id(gene.split(';'))
                values = transcripts.get(id, [])
                values.append(complete_list[(start-1):(end)])
                transcripts[id] = values

        if ("start_codon" == biotype or "stop_codon" == biotype) and ("7" == chromosome) and ("ENSG00000001626" in gene):
            id = get_transcript_id(gene.split(';'))
            if ("ENST00000003084" in id):
                start_end.append((complete_list[(start-1):(end+6)]))

    print (start_end)

    for (keys,values) in transcripts.items():
        transcripts[keys]= ''.join(values)

    k = 0
    result= ("","")

    for (keys,values) in transcripts.items():

        if (len(transcripts[keys])) > k:
            k = len(transcripts[keys])
            result = (keys, values)
            # print (len(transcripts[keys]))
            # print (transcripts[keys])
            # print (keys)


sequence = result[1]
#print (sequence)
cds_position = []
num_bases = len(sequence)

for b in range (num_bases):
    #print (b)
    if sequence[b:b+9] == start_end[0]:
        mrna_start =b
        cds_position.append(mrna_start)

    if sequence[b:b+9] == start_end[1]:
        mrna_end =b+3
        cds_position.append(mrna_end)

cds = sequence[cds_position[0]:cds_position[1]]

#print(cds)
table = RNATranslationTable()

codon = []
for b in range (0,len(cds),3):
    cod = (cds[b:b+3])
    codon.append(cod)

aminoacids=[]
for codons in codon:
    t = table.translate(codons)
    if codons =="*":
        break
    aminoacids.append(t)

print ("".join(aminoacids))



