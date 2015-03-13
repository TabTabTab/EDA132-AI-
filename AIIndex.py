import collections

A={};
A['em algorithm']=829;
A['forward-backward filtering']=586;
A['viterbi algorithm']=588;
A['decision tree']=709;
A['alpha-beta pruning']=170;
A['min-max algo']=168;
A['bayes\' rule']=503;
A['naive bayes\' model']=821;
A['entropy']=715;
A['information gain']=715;
A['horn clause']=228;
A['definite clause']=228;
A['heuristic functions']=104;
A['8-puzzle']=105;
A['admissible heuristics']=106;
A['simulated annealing']=128;
A['conjunctive normal form']=225;
A['propositional logic']=221;
A['resolution proof']=224;
A['entailment']=212;



print("Index for Artificial Intelligence: A Modern Approach, Third Edition (international)");
print("")
for key in sorted(A):
    print ("%s: %s" % (key, A[key]));