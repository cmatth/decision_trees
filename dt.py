import readData as rd
import labels as l
import entropy as ent
import nodes
import random
import copy

dataset = 'voting'


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

print len(list)

raw_input('begin evaluation')



#print correct
#print len(test)



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

def optimize(list, set, classes):
    cur = evaluate(list[0], set)
    print cur

    for i in range(0,2000):
        ind = random.randint(1,len(list)-1)
        if list[ind].leaf == True:
            pass
        else:
            for x in classes:
                listy = copy.deepcopy(list)
                c = random.choice(listy[ind].children.keys())
                listy[ind].children[c] = nodes.leaf(x,listy[ind])
                new = evaluate(listy[0], set)
                print "%f\r" %(new),
                if new > cur:
                    cur = new
                    list = copy.deepcopy(listy)
                else:
                    pass
    return list



def evaluate(tree, set):
    correct = 0
    total = len(set)

    for x in test:
        # print "actual", x[labels['class']]
        # print "result", tree.eval(labels, attributes, x, mostcommon)
        if x[labels['class']] == tree.eval(labels, attributes, x, mostcommon):

            correct += 1
        else:
            pass
    return (float(correct) / total)


# print correct
# print len(test)

# Evaluate Test Set Performance
print "Test Results: %f %%" %(evaluate(tree,test))
print "Number of nodes: %d" %(len(list))
#print "Results: %f %%" %(evaluate(tree,train))
list = optimize(list, train, attributes['class'])
print "**************************************"
print "Results: %f %%" %(evaluate(list[0],test))
print "Number of nodes: %d" %(len(list))
#print "Results: %f %%" %(evaluate(list[0],train))