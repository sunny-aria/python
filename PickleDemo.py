from Student import  Student

import  json

s = Student('hd',90)

print(s.__dict__)

json.dumps(s , default=lambda obj : obj.__dict__)
