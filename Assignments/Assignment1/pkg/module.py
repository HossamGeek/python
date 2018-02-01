def replacefunc(strr):
    str1 = '';
    vowels = ('a','e','i','o','u');
    for charr in strr:
        if(not(charr in vowels)):
           str1 += charr
        
    return str1


def replacefunclist(strr):
    strr = ','.join(strr);
    str1 = "";
   
    vowels = ('a','e','i','o','u');
    for charr in strr:
        if(not(charr in vowels)):
           str1 += charr
    str2 = str1.split(",");    
    return str2

def calcword(strr,key):
    str1=[];
    lenstrr = len(strr);
    for i in range(lenstrr):
        if(strr[i] == key):
            str1.append(i);
    return str1        
    

    
def multifunc(num):
    valone = [];
    result = [];
    b = 1;
    for i in range(num):
        c = (i+1);
        b = 1;
        #result = [[]]*i;
        while (b <= c):
            valone.append((b*c))
            b += 1;
        #result[i].append(valone);         
        result.append(valone);    
        valone=[];    
    return result

        
        
def calcarea(shape,num,height=3):
    if shape == 't':
        return (0.5*num*height);
    elif shape == 'r':
        return (num*height);
    elif shape == 'c':
        return (3.14*(num**2));
    
"""    
def dicname(listname):
    names={};
    for i in  range(len(listname)):
        names[listname[i][0]]=[listname[i]];
    print(names)    
    
    #%logstart -o
"""

    
def dicnames(listname):
    
    names={};
    for i in range(len(listname)): 
            if(listname[i][0] in names):
                names[listname[i][0]].append(listname[i]) 
                names[listname[i][0]].sort()
            else:
                names[listname[i][0]]=[listname[i]];
                names[listname[i][0]].sort()
    
    return sorted(names.items()) 


def star(num):
    result = [];
    count = 1;
    space=" ";
    spaces="";
    star='*';
    stars = '*';
    for i in range(num):  
        
        spaces="";
        
        count = num-2;
        while(count>=i):
            spaces += space
            count-=1;

        print(spaces+stars)
        stars += star
    
    """
    number = input("num")
    
    rang = rang(int(number))
    
    for i in rang:
        print(""*(int(number)-1*i)+"*"*(i+1))
        
def keylis():        
    for key in name.keys():
        print(key,":",name[key])
        
"""
        
        