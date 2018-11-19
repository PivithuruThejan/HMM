from hmmlearn import hmm
import numpy as np
import math

model = hmm.MultinomialHMM(n_components=9)
model.startprob_ = np.array([ 0, 0.0725193, 0.163763, 0.1788242, 0.0754545, 0.1322050, 0.1267006, 0.1226380, 0.1278950])
# initail probabilities

model.transmat_ = np.array([
    [0, 0.0725193, 0.163763, 0.1788242, 0.0754545, 0.1322050, 0.1267006, 0.1226380, 0.1278950],
    [0.001, 0.1762237, 0.2682517, 0.4170629, 0.1174825, 0.0035964, 0.0054745, 0.0085104, 0.0023976],
    [0.001, 0.1672435, 0.3599201, 0.267984, 0.1838722, 0.0034131, 0.0073453, 0.005469, 0.0037524],
    [0.001, 0.1576223, 0.3318881, 0.3671328, 0.1223776, 0.0032167, 0.0067732, 0.0074915, 0.0024975],
    [0.001, 0.0773426, 0.3475514, 0.375944, 0.1781818, 0.0015784, 0.0070929, 0.0076723, 0.0036363],
    [0.001, 0.0002997, 0.0002047, 0.0002837, 0.0002097, 0.2994005, 0.2045904, 0.2844305, 0.2095804],
    [0.001, 0.0003216, 0.0002977, 0.0000769, 0.0003016, 0.3213566, 0.2974045, 0.0778441, 0.3013966],
    [0.001, 0.0001768, 0.000238, 0.0002917, 0.0002917, 0.1766463, 0.2385224, 0.2914165, 0.2914155],
    [0.001, 0.0002477, 0.0002457, 0.0002977, 0.0002077, 0.2475044, 0.2455084, 0.2974035, 0.2075844]
]) # transition probabilities

model.n_features = 4
model.emissionprob_ = np.array([
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]) # emission probabilities

file = open("input","r")
data = file.read()
size = len(data)
input = []
for x in range(size):
    index = 0
    if (data[x].lower() == 'a'):
        index = 0
        
    elif (data[x].lower() == 'c'):
        index = 1
    elif (data[x].lower() == 'g'):
        index = 2
    elif (data[x].lower() == 't'):
        index = 3
    input.append(index)
    
input = np.array([input]).transpose()
logprob, seq = model.decode(input)
output = ""
for x in range(len(seq)):
    if (0 < seq[x] and seq[x] < 5):
        output = output + "+" # belongs to a CPG island
    else:
        output = output + "-" # does not belong to CPG island
file= open("output.txt","w+")
file.write(output)
file.close()
