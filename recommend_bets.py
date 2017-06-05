"""
This file gives a simple overview of how the scheme of treatment assignment and recommendation will always look like: 
    -there will always be a dictionary called treatment, where an id is linked to an assignment function, which takes data, in form of various queries, related to a user, and returns a list of bets, with recommended contracts.  Here the bets are overly simplistic in that they are just strings: "bet1", "bet2" etc. and they don't even have contracts.   
"""

IDs = range(111, 500)

bets = ["bet1", "bet2", "bet3", "bet4"]

treatment={}

#treatment assignment, to extreemly over-simplified recommendation functions
for i in range(int(float(len(IDs))/3)):
    def func(x):
        return bets[:2]
    treatment[i] = func

    #note that these functions don't even depend on information, x, at all
    #this is just in order to simplify further.
    
for i in range(int(float(len(IDs))/3), int(2*float(len(IDs))/3)):
    def func(x):
        return bets[2:]
    treatment[i] = func
    
for i in range(int(2*float(len(IDs))/3), len(IDs)):
    def func(x):
        return bets
    treatment[i] = func
    
#this is the function that will be called to retrieve the recommendations related to a specific user. This function will remain as it is, more or less. 

def recommend_bets(IRL):
    return treatment[IRL](data)


def main():
    x={"some stuff":0}

    for i in treatment.keys():
        print treatment[i](x)

        
if __name__=="__main__": main()
