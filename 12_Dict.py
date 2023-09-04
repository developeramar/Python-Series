
"""

Dictionary is the key value Storage which can store the value in key value pair.
* this is unchangebale , unorderd , they cant store the duplicate valuea

for example :
"""

dict = {
    "Name" : "Ram",
    "age" : 25,
    "College" : "AIHT Chennai",
    "Branch" : "CSE",
    "Subjects" : ["CSE" , "ECE" ,"MECH" , "EEE" , "BIO"]
}

# for "Update the any key value "

dict.update({"age":24 , "Name":"Amar"}) # for update the value in dict
dict["Color" ] = "Black"  # for add the value in dict
dict.pop("College")       # for remove the any Item from dict.

print(dict)

# x = dict.get("College") # get the particular value from key
# print(x)
# print(dict["Subjects"]) # get the particular value from key
# print(type(dict)) # find the type of dictionary
