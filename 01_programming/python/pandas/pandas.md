# CBT Nuggets : Data Structures with Pandas

- Numpy
- n-dimensional arrays
- linear algebra, fourier transforms, random numbers
- integration with c, c++, fortran
- 2 axis -- rows, cols
- type -- default -- long integers
- size -- count of elements in the array
- shape -- say 4 x 3

```python

# pip install numpy 
import numpy as np

arr = [1, 2, 3, 4, 5]
npArr = np.array([ 
    (1, 2, 3), 
    (2, 3, 4), 
    (3, 4, 5), 
    (4, 5, 6) 
    ]) # 4 x 3 array

arr.shape 
arr.ndim
arr.size 
arr.dtype

np.arrange(start, upto, step)

np.zeroes(howManyZeroesDoYouNeed).reshape(x, y) # default float64; also x*y = howManyZeroesDoYouNeed

np.ones(n, dtype=int)
```



# 