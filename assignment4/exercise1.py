import re

def is_course_code(s):
    return(re.fullmatch(r'[A-Z]{3}\d{3}', s))

print(is_course_code("TEC001"))   
print(is_course_code("ABC123"))   
print(is_course_code("tec001"))   
print(is_course_code("TE001"))