from pronouns_celery import *
import time
from collections import Counter


start = time.time()  

result1 = task1.delay()
#result2 = task2.delay()
#finaldict = Counter(result1.wait()) + Counter(result2.wait())
#print(finaldict)
print(result1.wait())

end = time.time()
print("Time is ",end-start," s")
