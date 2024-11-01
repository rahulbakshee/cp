import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.count = 0
        self.maxHeap = []

        # tweet maps userId - list of [time, tweet1,] [time, tweet2]...
        self.tweet_map = defaultdict(list)

        # {ID follows ID}
        self.follow_map = defaultdict(set)

    def postTweet(self, userId:int, tweetId:int)->None:
        """Composes a new tweet with ID tweetId by the user userId. 
        Each call to this function will be made with a unique tweetId.
        """
        # add userId tweet to the list of tweets
        self.tweet_map[userId].append([self.count, tweetId])
        self.count -= 1

        # userId 10: [time=2, tweetId=7], [time=5, tweetId=10], [time=3, tweetId=20], 
        # userId 3: [time=12, tweetId=17], [time=51, tweetId=1023]


    def getNewsFeed(self, userId:int)->List[int]:
        """Retrieves the 10 most recent tweet IDs in the user's news feed. 
        Each item in the news feed must be posted by users who the user 
        followed or by the user themself. Tweets must be ordered from most 
        recent to least recent.
        """
        result = []
        minHeap = []

        # add the user itself to the follower so that its newsfeed also counted in result
        self.follow_map[userId].add(userId)

        # take all the tweets from followeeId
        for fid in self.follow_map[userId]:
            if fid in self.tweet_map:
                index = len(self.tweet_map[fid])-1
                count, tweetId = self.tweet_map[fid][index]
                minHeap.append([count, tweetId, fid, index-1])

        heapq.heapify(minHeap)
        while minHeap and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])

        return result


    def follow(self, followerId:int, followeeId:int)->None:
        """The user with ID followerId started following the user with ID followeeId.
        """
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId:int, followeeId:int)->None:
        """The user with ID followerId started unfollowing the user with ID followeeId.
        """
        self.follow_map[followerId].discard(followeeId)
