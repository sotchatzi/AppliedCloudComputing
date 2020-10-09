from celery import Celery
from celery import shared_task
import json
import os
import re

#app = Celery('pronouns_celery', backend='rpc://', broker='amqp://')

app1 = Celery('task1', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app2 = Celery('task2', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app3 = Celery('task3', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app4 = Celery('task4', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app5 = Celery('task5', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app6 = Celery('task6', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app7 = Celery('task7', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
app8 = Celery('task8', backend='rpc://', broker='amqp://sotiris:sotiris@sotiris-c3//')
#app.conf.task_routes = {'pronouns_celery.json_results.*': {'queue': 'pron'}}
#app.conf.task_routes = {'pronouns_celery.tasks.*': {'queue': 'pron'}}

#app.conf.update(
#        task_routes = [('pronouns_celery.tasks.*', {'queue': 'pron'})]
#        )


#app.send_task('pronouns_celery.json_results')



path_to_json = "/home/ubuntu/data/"
#filename = "/home/ubuntu/workplace/data.json"
pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]
total = [0, 0, 0, 0, 0, 0, 0]
#app = Flask(__name__)

def read_input(f):
    with open(f,"r") as f:
        for l in f:
            if not l.strip():
                continue

            tweet = json.loads(l)

            if "retweeted_status" not in tweet:
                text = tweet['text']
                yield text

def json_results(json_files):
#    json_files = [pos_json for pos_json in os.listdir(path_to_json)]
    num = 0
    for json_file in json_files:
        data = read_input(path_to_json + json_file)
        for line in data:
            final = set()
            line = line.strip().lower()
            words = re.findall(r"\w+|[^\w\s]", line, re.UNICODE)
            for word in words:
                if word in pronouns:
                    final.add(word)
            for word in final:
                num +=1
                #"han"
                if (word == pronouns[0]):
                    total[0] += 1
                #"hon"
                elif(word == pronouns[1]):
                    total[1] += 1
                #"den"
                elif(word == pronouns[2]):
                    total[2] += 1
                #"det"
                elif(word == pronouns[3]):
                    total[3] += 1
                #"denna"
                elif(word == pronouns[4]):
                    total[4] += 1
                #"denne"
                elif(word == pronouns[5]):
                    total[5] += 1
                #"hen"
                elif(word == pronouns[6]):
                    total[6] += 1

#    print("unique", "\t", num)
#    for i in range(7):
#        print(pronouns[i], "\t", total[i])
    final = {pronouns[0]:total[0], pronouns[1]:total[1],
             pronouns[2]:total[2], pronouns[3]:total[3],
             pronouns[4]:total[4], pronouns[5]:total[5],
             pronouns[6]:total[6], "total":num}

    #with open(filename, "w", encoding="utf-8") as f:
    #    json.dump(final, f, ensure_ascii=False, indent=4)
    return final

@app1.task()
def task1():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final1 = json_results(json_files)
    return final1

@app2.task()
def task2():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final2 = json_results(json_files)
    return final2

@app3.task()
def task3():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final3 = json_results(json_files)
    return final3

@app4.task()
def task4():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final4 = json_results(json_files)
    return final4

@app5.task()
def task5():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final5 = json_results(json_files)
    return final5

@app6.task()
def task6():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final6 = json_results(json_files)
    return final6

@app7.task()
def task7():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final7 = json_results(json_files)
    return final7

@app8.task()
def task8():
    json_files = ['fcba121d-352f-494b-86aa-a45ff1f283a3','f7d25ca8-68d6-454e-9421-67ee5cc6f760','f683a560-fdee-4059-91de-6423da7a5300','f1c47aa7-5b69-4467-897c-24151649bcf4','f09905c6-161d-4ca1-9ef2-7af7441f9a1a','d257c9c6-aeb8-46a4-b722-62b20c9cf1b9','d1b39917-03cd-4480-84fb-8a10de1d8f19', 'cc12933c-a8d5-4fc4-8bef-56c214986d8a','cad86632-c0fe-4ff8-9d11-c17654e57b9f','c7f4aa96-1b2f-4ced-a265-cef17de64f8b','c17107b2-a732-4e6e-9e43-1b1f1f08ae40']
    final8 = json_results(json_files)
    return final8
#def main():
#    final = json_results.apply_async()
#    return final    

#@app.route("/home/ubuntu/workplace")
#def home():
#    result = json_results.delay()
##    result.wait()
#    return result.wait()


#def summary():
    #with open(filename,'r') as json_file:
    #    json_data = json.load(json_file)
#    return jsonify(json_data)
#    return jsonify(main)

#if __name__ == "__main__":
#    main()
#    app.run(host='0.0.0.0',debug=True)



