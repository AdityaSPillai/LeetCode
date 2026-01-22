class Twitter:

    def __init__(self):
        self.time=0
        self.followers=defaultdict(set)
        self.tweets=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([tweetId,self.time])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxHeap=[]

        self.followers[userId].add(userId)
        for i in self.followers[userId]:
            if i in self.tweets:
                index=len(self.tweets[i])-1
                tweet,count=self.tweets[i][index]
                maxHeap.append([count,tweet,i,index-1])
        heapq,heapify(maxHeap)

        while maxHeap and len(res)<10:
            count,tweet,follower,index=heapq.heappop(maxHeap)
            res.append(tweet)
            if index>=0:
                tweet,count=self.tweets[follower][index]
                heapq.heappush(maxHeap,[count,tweet,follower,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)