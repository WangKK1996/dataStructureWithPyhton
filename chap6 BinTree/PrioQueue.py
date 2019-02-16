class PrioQueue:
    """
    利用堆来实现优先队列
    """
    def __init__(self, elist = []):
        self._elems = list(elist) # 这一步是使内部的表脱离原来的表，防止元素的共享
        if elist:
            self.buildheap()
    
    def is_empty(self):
        return not self._elems
    
    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]
    
    # 入队操作
    def enqueue(self, e):
        self._elems.append(None) # add a dummy elemnt
        self.siftup(e, len(self._elems)-1)
        
    def siftup(self, e, last):
        # 初始化，(元素-1//2)对应的是其根节点
        elems, i, j = self._elems, last, (last-1)//2 
        # 判断，当e小于其根节点的时候，把根节点一段一段往下移动
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e
    
    # 弹出操作
    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in queue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0
    
    def siftdown(self, e, begin, end):
        # 初始化，begin*2+1找的是其左根结点
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            # 判断右结点（兄弟结点）的情况
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1 # 保证elems[j]里的数据不大于其兄弟结点的数据
            # 这样就保证了根节点一定会小于兄弟结点中较小的那个
            if e < elems[j]: 
                break # 因为e已经在三者中最小，找到了位置
            elems[i] = elems[j] # 因为元素j在三者中最小，所以将其上移。
            i, j = j, j * 2 + 1 # 更新i，j指针
        elems[i] = e
    
    # 堆的初始构建
    def buildheap(self):
        end = len(self._elems)
        # 从end//2开始做是因为，后面的元素已经是叶结点（顺序表转化为二叉树的特有性质）
        # 所以，它们中的每一个都已经是一个堆了；
        # 从完全二叉树的最下最右分支结点开始，往左建堆
        # 然后再到上一层建堆；
        # 最后，整个表成为一个堆
        # 这个工作实际上就是在两个已有的堆上加上一个根元素，使其成为堆
        for i in range(end//2, -1, -1):
            self.siftdown(self._elems[i], i, end)