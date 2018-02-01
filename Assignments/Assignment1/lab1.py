from pkg.module import * 

#one

word1 = "mobile";

word2=["mobile","mobile","mobile"];

vowels = ('a','e','i','o','u');

for i in word1:
    if i in vowels:
        word1 = word1.replace(i,"");

        
print(word1)

print(replacefunc(word1))
print(replacefunclist(word2))

#two

print(calcword("this is javascript","i"))

#three

#num = int(input("Enter your number for multiplication : \n"))           
print(multifunc(3))

#four
print(calcarea('r',10,7))

#five
   
    
listname =["Alaa","Ahmed","Ehmed","Fatma", "Hossam","Heba"];
print(dicnames(listname))

#six

star(7)

