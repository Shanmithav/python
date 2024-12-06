str1= "ShanmithaVangeti"
result={ }
for ele in str1:
    if ele in result:
        result[ele] += 1
    else:
        result[ele] = 1
print("count of elements in str: \n", str(result))
