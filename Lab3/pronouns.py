import json
import os
import re

path_to_json = "/home/ubuntu/data/"
pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]
total = [0, 0, 0, 0, 0, 0, 0]

def read_input(f):
    with open(f,"r") as f:
        for l in f:
            if not l.strip():
                continue

            tweet = json.loads(l)

            if "retweeted_status" not in tweet:
                text = tweet['text']
                yield text
def main():
    json_files = [pos_json for pos_json in os.listdir(path_to_json)]
    num = 0
    for json in json_files:
        data = read_input(path_to_json + json)
        for line in data:
            num +=1
            final = set()
            line = line.strip().lower()
            words = re.findall(r"\w+|[^\w\s]", line, re.UNICODE)
            for word in words:
                if word in pronouns:
                    final.add(word)
            for word in final:
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

    print("unique", "\t", num)
    for i in range(7):
        print(pronouns[i], "\t", total[i])

if __name__ == "__main__":
    main()


