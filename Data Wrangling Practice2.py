#already sorted by timestamp, with exact duplicates removed. Can be many feeds
feed_a = [(1, "AAPL", 187.5), (4, "MSFT", 412.1), (7, "AAPL", 187.8)]
feed_b = [(2, "AAPL", 187.6), (4, "MSFT", 412.1), (9, "MSFT", 412.0)]
feed_c = [(3, "TSLA", 250.0), (7, "AAPL", 187.8)]
# Write a function that takes a list of feeds and returns one combined list, 
# sorted by timestamp, with exact duplicates removed.

#expected output: 
# [(1, "AAPL", 187.5), 
# (2, "AAPL", 187.6), 
# (3, "TSLA", 250.0), 
# (4, "MSFT", 412.1), 
# (7, "AAPL", 187.8), 
# (9, "MSFT", 412.0)]

import heapq
from itertools import groupby

# with merge and groupby
def combine_feeds(feeds):
    feeds = heapq.merge(*feeds)
    return (transaction for transaction, grp in groupby(feeds))


#without merge and groupby
def combine_feeds(feeds):
    iters = [iter(feed) for feed in feeds] #an iterator for each feed
    heap = []
    for i, val in enumerate(iters): #feed # and its iterator
        first = next(val, None)
        if first is not None:
            heapq.heappush(heap, (first, i)) #store the first element of each feed in the heap along with its index

    last = None #last trade returned from smallest, to avoid duplicates
    while heap:
        trade, i = heapq.heappop(heap)
        if last != trade:
            yield trade #return the trade if it's not a duplicate of the last one returned, also clears memory of the last trade returned
            last = trade

        #for the feed that the trade came from, get the next trade and push it onto the heap
        next_val = next(iters[i], None)
        if next_val is not None:
            heapq.heappush(heap, (next_val, i))