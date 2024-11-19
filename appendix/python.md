## Sorting

```python
list.sort() # inplace, returns None
sorted(list) # returns new list
sorted(student_tuples, key = lambda student: student[2]) # sort by age
sorted(student_objects, key = lambda student: student.age) 
```

```python
from operator import itemgetter, attrgetter

sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('age'))
```

- [Sorting Python Docs Article](https://docs.python.org/3/howto/sorting.html)
- 