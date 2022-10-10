"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computes all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 5)
    ['agtag', 'gtagt', 'tagtc', 'agtcg']
    """
    if k <= 0:
        raise Exception("k not positve")
    
    kmers = [x[i:i+k] for i in range(len(x)-k+1)]

    # kmers = []
    # for i in range(len(x)-k+1):
    #     kmers.append(x[i:i+k])

    return kmers


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computes all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']

    >>> unique_kmers('gttttatttg', 2)
    ['gt', 'tt', 'ta', 'at', 'tg']

    """
    unique = []
    kmers = kmer(x, k)
    for km in kmers:
        if km not in unique:
            unique.append(km)

    # unique = list(set(kmer(x, k))) # set only stores a value once, however not in order

    return unique



def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computes all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}

    >>> count_kmers('gttttatttg', 2)
    {'gt': 1, 'tt': 5, 'ta': 1, 'at': 1, 'tg': 1}
    """
    kmer_count = {}
    for km in kmer(x, k):
        if km not in kmer_count:
            kmer_count[km] = 0
        kmer_count[km] += 1
    
    return kmer_count


# print(kmer('agtagtcg', 3))
# print(unique_kmers('agtagtcg', 3))
# print(count_kmers('agtagtcg', 3))