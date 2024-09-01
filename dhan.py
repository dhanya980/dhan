class Hash:
  def init (self): 
     self.buckets=[[],[],[],[],[]]
  def insert(self,key): 
     bindex = key % 5
     self.buckets[bindex].append(key) 
     print(key,"inserted in Bucket No.",bindex+1)
  def search(se1f,key): 
     bindex = key % 5
    if key in self.buckets[bindex]:
          print(key,"present in bucket No.",bindex+1)
     else:
       print(key,"is not present in any of the buckets") 
  def display(self):
     for i in range(0,5):
        print("\nBucket No.",i+1,end=":") 
        for j in self.buckets[i]:
          print(j,end="->") 

