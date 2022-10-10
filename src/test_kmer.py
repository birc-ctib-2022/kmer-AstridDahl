# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from itertools import count
from kmer import (
    kmer,
    unique_kmers,
    count_kmers
)



def test_me():
    assert False, "Don't forget to write tests"

def test_kmer():
    assert kmer('agtagtcg', 5) == ['agtag', 'gtagt', 'tagtc', 'agtcg']

def test_unique_kmers():
    assert unique_kmers('gttttatttg', 2) == ['gt', 'tt', 'ta', 'at', 'tg']

def test_count_kmers():
    assert count_kmers('gttttatttg', 2) == {'gt': 1, 'tt': 5, 'ta': 1, 'at': 1, 'tg': 1}