from pronouns_celery import *
import time
from collections import Counter


start = time.time()  

result1 = task1.delay()
result2 = task2.delay()
result3 = task3.delay()
result4 = task4.delay()
result5 = task5.delay()
result6 = task6.delay()
result7 = task7.delay()
result8 = task8.delay()
finaldict = Counter(result1.wait()) + Counter(result2.wait())  +Counter(result3.wait()) + Counter(result4.wait()) +Counter(result5.wait()) + Counter(result6.wait()) +Counter(result7.wait()) + Counter(result8.wait()) 
print(finaldict)

end = time.time()
print("Time is ",end-start," s")
