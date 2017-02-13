#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_transcript_id(attr_list):
    for attr in attr_list:
        if 'transcript_id' in attr:
            return attr
    raise ValueError('I did not find a transcript_id')

def get_longest_transcript(filename = "Homo_sapiens.GRCh38.87.gtf", chromosome = '7', gene='ENSG00000001626'):
    
    
    # ===================================================================
    with open(filename, mode="rt",encoding="utf-8") as gtf_file:

        gene_id = 'gene_id "%s"' % gene
        transcripts = {}

        for line in gtf_file:


            blocks = line.split("\t")


            # Only that chromosome and 
            if (
                len(line) < 9 or             # no comments, please
                blocks[0] != chromosome or     # only that chromosome. Careful: not comparing integers!
                blocks[2] != 'exon' or         # the line should be an exon
                not gene_id in blocks[8]       # Is that the right gene?
            ): 
                continue # skip to the next line
            
            # Otherwise, it is a transcript for the given gene and chromosome
            attributes = blocks[-1]
            transcript_id = get_transcript_id(attributes.split(';'))

            start  = int(blocks[3])
            end    = int(blocks[4])
            
            # Adding it to the table
            transcript_length = transcripts.get(transcript_id, 0)
            transcripts[transcript_id]= transcript_length + abs(end-start+1)

    ## works up to this point
    # ===================================================================
    # File closed.

    maximum = (max(transcripts, key=transcripts.get))
    print (maximum, transcripts[maximum])


    # biggest_so_far = (0,'')
    # # Going through the records
    # for  k,v in transcripts.values():
    #     if v > biggest_so_far[0]:
    #         biggest_so_far = (v,k)
    #
    # print (biggest_so_far)

    #outside the loop
#    print('The longest transcript is',transcripts[biggest_so_far],'with',biggest_so_far,'pairs.')


get_longest_transcript(filename="Homo_sapiens.GRCh38.87.gtf", chromosome='7', gene='ENSG00000001626')
