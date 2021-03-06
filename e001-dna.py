#!/usr/bin/env python

# Counting Nucleotides
# ====================
# 
# A string is simply an ordered collection of symbols selected from some
# alphabet and formed into a word; the length of a string is the number of
# symbols that it contains.
# 
# An example of a DNA string (whose alphabet contains the symbols A, C, G, 
# and T) is "ATGCTTCAGAAAGGTCTTACG".
# 
# Given: A DNA string s of length at most 1000 nt.
# 
# Return: Four integers separated by space corresponding to the number of 
# times that the symbols A, C, G, and T occur in s.
#
# Sample Dataset
# --------------
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
#
# Sample Output
# -------------
# 20 12 17 21


def count_basie(s):
    counted = {}
    ordered = []

    for c in s:
        if not counted.has_key(c):
            counted[c] = 0
        counted[c] += 1

    for c in sorted(counted.iterkeys()):
        ordered.append(counted[c])

    return ordered


if __name__ == "__main__":

    small_dataset = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    large_dataset = "TAGCGTAGGATGGAGCTTAGTTCGCAAGCCTAATTATCCTCGCCCGCTGACGTGATGAAGATAACTGCAACGCACAGCAGGATATAAACTAGCAACGCAAAATGGTGGGGCCATGCACTGTCTATCCCAGCTATATCTAATATGTTGGCCGTTTGTGGAAATGCATGATCTGGGTAATTTCTAGGAGAACTCTTAGTCCTCAAGACTATAAGGCGGCGAAATAATAGTAACAGTCTTCGTACCAATTGAGAATCAAGCTCCTCGACGTCGAAGATGGGGGTTTACACCCCTTGACCAGCGTCCCCGGCCGTTAATCTATCTATAGGTTCACGTGGGGCGAACAGCGCCGAGTGAGCTCTACCCAATGATCGGGTGCGGCTTTGCGACTCGTATTGGGCGATGCGCCGCACCTGGCCCTGGGGACATACGCATTGTTTCGAATAAGAGCATACGCTAGTACCCCATACGAATGTGTCCGTAAAGACTAGTCCTTCCTGCGCTAAGGACGGGATTTGTTGAAACCTACGCTGATTGGCGACCGAGTAATCTGGAGATTATGTTATGATTGTAAAGGGAACACATAAGCCCTTCGTTCTTTTGAGTACCTTAGCGAAAAGGTATCAGTCTACGCCCAACGCTATCTCATGGGGTATCCCGAATCCAATGCGCAGCCACCTATCGTACAAGGAGCACCCAAGCCGATATTCGTGGATGGATCCTCCTTGGTGTGTAACTCTGAATCATGGAATCCGTCTAAAGCCTGTACTGGGTTAATCACCCCCGGTAACTTGAGTTTCCTGTCCCTTGAACGTATCTAGAGTTAA"

    counts = count_basie(large_dataset)

    print ' '.join(map(str, counts))

