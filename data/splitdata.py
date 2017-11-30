import os,sys,csv
import numpy as np
from collections import defaultdict

datafile = file('video_corpus.csv')
datareader = csv.reader(datafile)
datalist = []
datadict = defaultdict(list)
for line in datareader:
    if datareader.line_num == 1:
        datahead = line
        continue
    datalist.append(line)
    datadict[line[0]+'_'+line[1]+'_'+line[2]+'.avi'].append(line)

datanum = len(datadict.keys())
splitpoint = round(datanum * 0.8)

trainfile = file('video_corpus_train.csv', 'wr')
trainwriter = csv.writer(trainfile)
trainwriter.writerow(datahead)
traindir = 'YouTubeClips_train'
# os.system('mkdir '+traindir)

testfile = file('video_corpus_test.csv', 'wr')
testwriter = csv.writer(testfile)
testwriter.writerow(datahead)
testdir = 'YouTubeClips_test'
# os.system('mkdir '+testdir)

i = 0
for video in datadict.keys():
    if i <= splitpoint:
        # mv to train set
        if os.path.exists(os.path.join('YouTubeClips', video)):
            os.system('cp '+os.path.join('YouTubeClips', video)+' '+traindir)
            trainwriter.writerows(datadict[video])
            print 'cp '+video+' to train folder and add annotations'
        else:
            print 'train file '+video+' not exist'
        i += 1
    else:
        # mv to test set
        if os.path.exists(os.path.join('YouTubeClips', video)):
            os.system('cp '+os.path.join('YouTubeClips', video)+' '+testdir)
            testwriter.writerows(datadict[video])
            print 'cp '+video+' to test folder and add annotations'
        else:
            print 'test file '+video+' not exist'

print 'finish processing'
datafile.close()
trainfile.close()
testfile.close()
