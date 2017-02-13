#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

    print ("The longest transcript is: ", result[0],"with length; ",k, "and the sequence is:",'\n', result[1])




