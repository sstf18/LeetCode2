"""
tickets[i] = [from_i, to_i]
must start from : JFK

if multiple itineraries, return the smallest lexical order
"""

from typing import List


class Solution: 
    def findItinerary(self, tickets: List[List[str]]) -> List[str]: 
        tickets.sort()
        used = [0] * len(tickets)
        path = ['JFK']
        results = []
        self.backTracking(tickets, used, path, 'JFK', results)
        return results[0]
    def backTracking(self, tickets, used, path, cur, results): 
        if len(path) == len(tickets) + 1: 
            results.append(path[:])
            return True 
        for i, ticket in enumerate(tickets): 
            if ticket[0] == cur and used[i] == 0: 
                used[i] = 1 
                path.append(ticket[1])
                state = self.backTracking(tickets, used, path, ticket[1], results)
                path.pop()
                used[i] = 0 
                if state: 
                    return True 