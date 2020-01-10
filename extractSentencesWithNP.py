import time
import copy
import spacy

nlp = spacy.load("en_core_web_sm")

with open("test.txt") as fp:
    line = fp.readline()
    count = 0
    sentenceList = []
    sentCount = 0
    NPstarted = False
    NPList = []
    sentence = ""
    runningNP = ""
    while line:
        lineList = line.split(" ")
        if line.strip() == "":
            tempObj = {"sentence" : sentence.strip(), "NPList" : copy.deepcopy(NPList)}
            sentenceList.append(tempObj)
            sentCount = sentCount + 1
            NPstarted = False
            NPList = []
            runningNP = ""
            sentence = ""
            line = fp.readline()
            continue

        word = lineList[0]
        POS = lineList[1]
        POS = POS.strip()
        NP = lineList[2]
        NP = NP.strip()
        if NP == "B-NP" and NPstarted == False:
            #print("came here")
            NPstarted = True
            runningNP = word
        else:
            if NPstarted == True and (NP == "I-NP" or (NP == "B-NP" and POS == "POS")):
                #print("came here ")
                if POS == "POS" or POS == "." or POS == ",":
                    runningNP = runningNP + word
                else:
                    runningNP = runningNP + " " + word

            elif NPstarted == True and NP != "I-NP":
                #print("came in elif")
                NPstarted = False
                NPList.append(runningNP.strip())
                runningNP = ""
                if NP == "B-NP":
                    NPstarted = True
                    runningNP = word

        if POS == "POS" or POS == "." or POS == ",":
            sentence = sentence + word
        else:
            sentence = sentence + " " + word

        count = count + 1
        line = fp.readline()

print("Number of total sentences being evaluated: " + str(sentCount))
onlySentenceList = [item["sentence"] for item in sentenceList]

docs = list(nlp.pipe(onlySentenceList))
time1 = time.time()

chunks = list(list(doc.noun_chunks) for doc in docs)
time2 = time.time()

same = 0
changes = []

totalChunksGroundTruth = 0
totalChunksPredicted = 0
totalCorrectChunksPredicted = 0

for i in range(len(chunks)):
    chunkList = []
    for item in chunks[i]:
        chunkList.append(str(item))
    totalChunksGroundTruth = totalChunksGroundTruth + len(sentenceList[i]["NPList"])
    totalChunksPredicted = totalChunksPredicted + len(chunkList)

    for predictedNP in chunkList:
        if predictedNP in sentenceList[i]["NPList"]:
            totalCorrectChunksPredicted = totalCorrectChunksPredicted + 1
    if chunkList == sentenceList[i]["NPList"]:
        same = same + 1
    else:
        changes.append(i)

print("Fraction of sentences whose spacy predictions matched perfectly with CoNLL 2000 dataset ground truth: " + str(same/len(chunks)) + "\n")
precision = (totalCorrectChunksPredicted/totalChunksPredicted)*100

print("-----------------------------------------------------------------")
print("Precision: \t" + str(precision))
recall = (totalCorrectChunksPredicted/totalChunksGroundTruth)*100
print("Recall: \t" + str(recall))
FScore = 2 * ((precision * recall)/(precision + recall))
print("F Score: \t" + str(FScore))
print("-----------------------------------------------------------------")


# uncomment the following lines to understand the specific cases where spaCy makes mistakes. The list "changes" contains a list of index of all the sentences that had a mismatch with the ground truth.
'''
print(changes)
sampleTest = 5

print("*********    The sentence being analyzed   *********")
print(onlySentenceList[sampleTest])

print("*********    Predicted Noun Phrases    *********")
print(chunks[sampleTest])

print("*********    Ground Truth Noun Phrases     *********")
print(sentenceList[sampleTest]["NPList"])


'''
#print(sentenceList[0:5])
