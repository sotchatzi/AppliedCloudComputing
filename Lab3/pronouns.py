from flask import Flask,jsonify
import json
import os
import re

path_to_json = "/home/ubuntu/data/"
#filename = "/home/ubuntu/workplace/data.json"
pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]
total = [0, 0, 0, 0, 0, 0, 0]
app = Flask(__name__)

def read_input(f):
    with open(f,"r") as f:
        for l in f:
            if not l.strip():
                continue

            tweet = json.loads(l)

            if "retweeted_status" not in tweet:
                text = tweet['text']
                yield text

@app.route("/home/ubuntu")
def json_results():
    json_files = [pos_json for pos_json in os.listdir(path_to_json)]
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


#def summary():
    #with open(filename,'r') as json_file:
    #    json_data = json.load(json_file)
#    return jsonify(json_data)
#    return jsonify(main)

if __name__ == "__main__":
#    main()
    app.run(host='0.0.0.0',debug=True)



