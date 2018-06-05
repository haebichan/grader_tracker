from pymongo import MongoClient 
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost:27017')

grades = client.tracker.grades 
#tracker as name of the database, grades as the name of the collection


# d = {}
# for _ in range(3):
#     name = input('student name: ')
#     klass = input('student class: ')
#     grade = float(input('student grade: '))

#     d = {'name': name, 'klass': klass, 'grade': grade}
#     grades.insert_one(d)

total = 0
count = grades.find().count()
for g in grades.find():
    total += g['grade']
    avg = total/count
print(avg)



print(len(total))    