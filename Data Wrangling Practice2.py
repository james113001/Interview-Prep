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

from decimal import Decimal
import heapq
from itertools import groupby

from collections import defaultdict, deque

class RollingAverage:
    def __init__(self, window_size=60):
        self.window_size = window_size
        self.windows = defaultdict(deque)  # store (timestamp, price) tuples, create window for each symbol
        self.sums = defaultdict(float)  # store the sum of prices for each symbol
        self.notional = defaultdict(float)  # store the sum of prices for each symbol
        self.vol = defaultdict(int)  # store the total quantity for each symbol

    def add(self, timestamp, symbol, price):
        window = self.windows[symbol]
        window.append((timestamp, price))
        self.sums[symbol] += price
        while window and timestamp - window[0][0] > self.window_size:
            old_ts, old_price = window.popleft()
            self.sums[symbol] -= old_price

        return Decimal(str(self.sums[symbol] / len(window))) #use Decimal to avoid floating point precision issues

    def vwapadd(self, timestamp, symbol, price, qty):
        window = self.windows[symbol]
        window.append((timestamp, price, qty))
        self.notional[symbol] += price * qty
        self.vol[symbol] += qty

        while window and timestamp - window[0][0] > self.window_size:
            old_ts, old_price, old_volume = window.popleft()
            self.notional[symbol] -= old_price * old_volume
            self.vol[symbol] -= old_volume

        return Decimal(str(self.notional[symbol] / self.vol[symbol])) if self.vol[symbol] > 0 else Decimal('0')

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

