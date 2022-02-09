#inputs, output list of lists for each input ie "g", "ge", "gee", "geei".......
contacts = ['sanabaaaaababa' ,'sanababaaaaaaaa' ,'sanaababba' ,'sanbbbbbaa' ,'sanabbbbaab' ,'sanaab' ,'sanaba' ,
'sanaab' ,'sanaaabbabb' ,'sanabb' ,'sanaababbabaa', 'sanbabb' ,'sanbabbbaabbbb' ,'sanaaaaabbb'] 
n = len(contacts)
s = "sanbbb"

#looks like a backtracking problem, similar to keypad problem in leetcode
#on second thought its not a backtrack but more of a simple array looping problem
def displayContacts(n, contacts, s):
    res = []
    #removing duplicates
    temp = sorted(list(set(contacts)))
    for i,val in enumerate(s):
        running = []
        for contact in temp:
            #when the word in contacts in shorter than the query 
            if len(contact) > i and contact[i] == val:
                running.append(contact)
        if running:
            temp = running
            res.append(temp)
        else:
            temp = []
            res.append(0)
    return res

print(displayContacts(n, contacts, s))
