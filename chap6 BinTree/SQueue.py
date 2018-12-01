# 队列类的实现
class SQueue():
    def __init__(self, init_len = 8):
        self._len = init_len # 存储区长度
        self._elems = [0] * init_len # 元素存储
        self._head = 0 # 表头元素下标
        self._num = 0 # 元素个数
    
    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise QueueUnderflow
        return self._elems[self._head]
    
    def dequeue(self):
        if self._num == 0:
            raise QueueUnderflow
        e = self._elems[self._head]
        self._head = (self._head + 1)%self._len
        self._num -= 1
        return e
    
    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1
        
    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
            self._elems, self._head = new_elems, 0
            
class SStack():
    def __init__(self): # 用list对象_elem存储栈中元素
        self._elems = [] # 所有栈操作都映射到list中
    
    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1] # 后进先出，得到最后一个元素
    
    def push(self, elem):
        self._elems.append(elem)
    
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop() # 以列表形式弹出
    
    def printall(self):
        print(self._elems)