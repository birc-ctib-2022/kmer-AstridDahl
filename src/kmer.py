"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 5)
    ['agtag', 'gtagt', 'tagtc', 'agtcg']
    """
    kmers = []
    for i in range(len(x)-k+1):
        kmers.append(x[i:i+k])

    return kmers


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

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

    return unique



def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}

    >>> count_kmers('gttttatttg', 2)
    {'gt': 1, 'tt': 5, 'ta': 1, 'at': 1, 'tg': 1}
    """
    # kmer_count = {}
    # kmers = kmer(x, k)
    # unique = unique_kmers(x, k)
    # for i in unique:
    #     count = 0
    #     for j in kmers:
    #         if i == j:
    #             count +=1
    #     kmer_count[i] = count

    kmer_count = []
    kmers = kmer(x, k)
    unique = unique_kmers(x, k)
    for i in unique:
        count = 0
        for j in kmers:
            if i == j:
                count += 1
        kmer_count.append((i, count))

    sorted_kcount = sorted(kmer_count, key=lambda t:t[1])
    
    return sorted_kcount



print(count_kmers('agtagtcg', 3))
print(count_kmers('gttttatttg', 2))