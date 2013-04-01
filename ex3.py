#!/usr/bin/python3

# lstrip(), rstrip(), and strip() are methods that remove
# leading trailing, and both leading and trailing whitespace,
st = "\n\t Some Non-Spaciou Text\n \t\r"
s1 = st.lstrip()
print (s1)
s2 = st.rstrip()
print (s2)
s3 = st.strip()
print (s3)


xml_tag = "<some_tag>"
x1 = xml_tag.lstrip("<")
print (x1)
x2 = xml_tag.strip(">").strip("<")
print (x2)

some_list = ['one','two', 'three','four']
st1= ', '.join(some_list)
print (st1)


some_list = [1,2,3,4,5,6,7]
st1 = ",".join([str(i) for i in some_list])
print (st1)

