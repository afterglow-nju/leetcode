class Twitter:
    
    def __init__(self):
        self.h=[]
        heapq.heapify(self.h)
        self.time=0
        self.d=defaultdict(set)
        import copy
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.h,[self.time,tweetId,userId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tem=copy.copy(self.h) #这里最费时间
        #也可以用list记录每一个人发的帖，然后根据你关注了谁，在这里建堆，这样会省时间
        record=0
        ret=[]
        while len(tem)>0 and record<10:
            t=heapq.heappop(tem)
            if t[2] in self.d[userId] or t[2]==userId:
                record+=1
                ret.append(t[1])
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.d[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.d[followerId].remove(followeeId)
        except:
            pass
#亏好没有删帖子这一说，不然还得从heap中删

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)