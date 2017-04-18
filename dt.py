import readData as rd
import labels as l
import entropy as ent
import nodes
import random
import copy
from subprocess import call
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

dataset = 'car'
test_num = 10
eval_num = 2000


# set up dataset then split into training and test
#path = "/home/casey/PycharmProjects/decision_trees/" + dataset + "_data.txt"
path = "/home/kmoney/Documents/decision_trees/decision_trees/" + dataset + "_data.txt"
set = rd.readFromFile(path)
set = rd.parseToArrays(set)
sets = rd.splitIntoSets(set, 3)
train = sets[0] + sets[1]
test = sets[2]

labels = l.getLabels(dataset)
attributes = l.getAttributes(dataset)
mostcommon = ent.mostCommon(train, labels, attributes)
list = []
tree = nodes.root(train, labels, attributes, mostcommon, list)


print('Tree Built!')

def optimize(list, set, classes):
    cur = evaluate(list[0], set, False)

    for i in range(0,eval_num):
        ind = random.randint(1,len(list)-1)
        if list[ind].leaf == True:
            pass
        else:
            for x in classes:
                listy = copy.deepcopy(list)
                c = random.choice(listy[ind].children.keys())
                listy[ind].children[c] = nodes.leaf(x,listy[ind])
                new = evaluate(listy[0], set, False)
                #print "%f\r" %(new),
                if new > cur:
                    cur = new
                    list = copy.deepcopy(listy)
                else:
                    pass
    return list

def evaluate(tree, set, pO):
    correct = 0
    total = len(set)

    truePositive = 0
    trueNegative = 0
    falsePositive = 0
    falseNegative = 0

    # R == positive
    # D == negative

    lab = []
    for x in attributes['class']:
        lab.append(x)

    y_true = []
    y_pred = []

    for x in test:
        # print "actual", x[labels['class']]
        # print "result", tree.eval(labels, attributes, x, mostcommon)
        pred = tree.eval(labels, attributes, x, mostcommon)
        y_true.append(x[labels['class']])
        y_pred.append(pred)
        if x[labels['class']] == pred:

            correct += 1
        else:
            pass
    if pO == True:
        fscore = f1_score(y_true, y_pred, lab, average='macro')
        recall = recall_score(y_true, y_pred, lab, average='macro')
        precis = precision_score(y_true, y_pred, lab, average='macro')
        #print "Precision: %f" %precis
        #print "Recall: %f" %recall
        #print "F Score: %f" %fscore
        return (float(correct)/total), precis, recall, fscore
    else:
        return (float(correct) / total)
    #return f1_score(y_true, y_pred, lab, average='macro'



avg_fscore = 0
avg_prec = 0
avg_rec = 0
avg_perc = 0

avg_fscore1 = 0
avg_prec1 = 0
avg_rec1 = 0
avg_perc1 = 0


y_true = []
y_pred = []


for x in range(0,test_num):
    # Evaluate Test Set Performance
    #print "****************************"
    perc, precis, recall, fscore = evaluate(tree,test, True)
   # print "Test Results: %f %%" %(perc)
    avg_fscore += fscore
    avg_prec += precis
    avg_rec += recall
    avg_perc += perc

    #print "Number of nodes: %d" %(len(list))
    call(['clear'])
    print "Optimizing..."
    #print "Results: %f %%" %(evaluate(tree,train))
    #raw_input("Begin Optimization")
    list = optimize(list, train, attributes['class'])
    perc, precis, recall, fscore = evaluate(list[0],test, True)
    #print "Optimized Results: %f %%" %(perc)
    avg_fscore1 += fscore
    avg_prec1 += precis
    avg_rec1 += recall
    avg_perc1 += perc

print "AVERAGED RESULTS ***********"
print "Precision: %f" %(avg_prec / test_num)
print "Recall: %f" %(avg_rec / test_num)
print "F Score: %f" %(avg_fscore / test_num)
print "Percent: %f%%" %(avg_perc / test_num)
print "****************************"
print "PrecisionO: %f" %(avg_prec1 / test_num)
print "RecallO: %f" %(avg_rec1 / test_num)
print "F ScoreO: %f" %(avg_fscore1 / test_num)
print "PercentO: %f%%" %(avg_perc1 / test_num)
print "****************************"
raw_input("PRESS ENTER TO END")
call(['clear'])


#print "Number of nodes: %d" %(len(list))
#print "Results: %f %%" %(evaluate(list[0],train))

### TESTING ###
'''
attr = 'doors'
train = ent.divideByAttributes(labels[attr], train, attributes[attr])
for key in train:
    print '***************' + key + '*****************'
    for x in train[key]:
        print x[labels['class']]
'''
'''''
print 'Entropy(S) = %f' %(ent.entropy(train, attributes['class'], labels['class']))

results = []
for attr in attributes:
    pass
    #print 'InfoGain('+ dataset +','+attr+') = %f' \
#%(ent.infoGain(labels[attr], attributes[attr],train,attributes['class'],labels['class']))
print ent.maxInfoGain(train, labels, attributes)
'''