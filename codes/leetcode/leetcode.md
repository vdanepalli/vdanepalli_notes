
# Leetcode 


<details open>
    <summary> Other </summary>

<br>

### 151. [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string) | Solved | Medium

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

#### Approach 1

```cpp
class Solution {
public:
    string reverseWords(string s) {
        // remove leading and trailing spaces
        s.erase(0, s.find_first_not_of(' '));  // prefixing spaces
        s.erase(s.find_last_not_of(' ') + 1);  // suffixing spaces

        // split by spaces
        istringstream iss(s);
        vector<string> words;
        copy(istream_iterator<string>(iss), istream_iterator<string>(),
             back_inserter(words));

        // reverse and join
        reverse(words.begin(), words.end());
        ostringstream oss;
        copy(words.begin(), words.end() - 1,
             ostream_iterator<string>(oss, " "));
        oss << words[words.size() - 1];
        return oss.str();
    }
};

```


```java
class Solution {
    public String reverseWords(String s) {
        // remove leading spaces
        s = s.trim();
        // split by multiple spaces
        List<String> wordList = Arrays.asList(s.split("\\s+"));
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
}

```


```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

```


```go
func reverseWords(s string) string {
    // split by spaces
    words := strings.Fields(s)
    // reverse
    for i := 0; i < len(words)/2; i++ {
        words[i], words[len(words)-i-1] = words[len(words)-i-1], words[i]
    }
    // join the words with a space
    return strings.Join(words, " ")
}

```


```js
var reverseWords = function (s) {
    // remove leading and trailing spaces
    s = s.trim();
    // split by spaces and reverse
    let words = s.split(/\s+/).reverse();
    // join the words with a space
    return words.join(" ");
};

```


#### Approach 2

```cpp
class Solution {
  public:
  string reverseWords(string s) {
    // reverse the whole string
    reverse(s.begin(), s.end());

    int n = s.size();
    int idx = 0;
    for (int start = 0; start < n; ++start) {
      if (s[start] != ' ') {
        // go to the beginning of the word
        if (idx != 0) s[idx++] = ' ';

        // go to the end of the word
        int end = start;
        while (end < n && s[end] != ' ') s[idx++] = s[end++];

        // reverse the word
        reverse(s.begin() + idx - (end - start), s.begin() + idx);

        // move to the next word
        start = end;
      }
    }
    s.erase(s.begin() + idx, s.end());
    return s;
  }
};
```

```java
class Solution {
    public StringBuilder trimSpaces(String s) {
        int left = 0, right = s.length() - 1;
        // remove leading spaces
        while (left <= right && s.charAt(left) == ' ') ++left;

        // remove trailing spaces
        while (left <= right && s.charAt(right) == ' ') --right;

        // reduce multiple spaces to single one
        StringBuilder sb = new StringBuilder();
        while (left <= right) {
            char c = s.charAt(left);

            if (c != ' ') sb.append(c);
            else if (sb.charAt(sb.length() - 1) != ' ') sb.append(c);

            ++left;
        }
        return sb;
    }

    public void reverse(StringBuilder sb, int left, int right) {
        while (left < right) {
            char tmp = sb.charAt(left);
            sb.setCharAt(left++, sb.charAt(right));
            sb.setCharAt(right--, tmp);
        }
    }

    public void reverseEachWord(StringBuilder sb) {
        int n = sb.length();
        int start = 0, end = 0;

        while (start < n) {
            // go to the end of the word
            while (end < n && sb.charAt(end) != ' ') ++end;
            // reverse the word
            reverse(sb, start, end - 1);
            // move to the next word
            start = end + 1;
            ++end;
        }
    }

    public String reverseWords(String s) {
        // converst string to string builder
        // and trim spaces at the same time
        StringBuilder sb = trimSpaces(s);

        // reverse the whole string
        reverse(sb, 0, sb.length() - 1);

        // reverse each word
        reverseEachWord(sb);

        return sb.toString();
    }
}
```

```python
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != " ":
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return "".join(l)
```


```go
// Translated Go solution
func reverseWords(s string) string {
    // convert string to char slice
    // and trim spaces at the same time
    arr := trimSpaces(s)

    // reverse the whole string
    reverse(arr, 0, len(arr)-1)

    // reverse each word
    reverseEachWord(arr)

    return strings.Join(arr, "")
}

func trimSpaces(s string) []string {
    left, right := 0, len(s)-1
    // remove leading spaces
    for left <= right && s[left] == ' ' {
        left++
    }

    // remove trailing spaces
    for left <= right && s[right] == ' ' {
        right--
    }

    // reduce multiple spaces to single one
    output := make([]string, 0)
    for left <= right {
        if s[left] != ' ' {
            output = append(output, string(s[left]))
        } else if output[len(output)-1] != " " {
            output = append(output, string(s[left]))
        }
        left++
    }
    return output
}

func reverseEachWord(c []string) {
    n := len(c)
    start, end := 0, 0

    for start < n {
        // go to the end of the word
        for end < n && c[end] != " " {
            end++
        }
        // reverse the word
        reverse(c, start, end-1)
        // move to the next word
        start = end + 1
        end++
    }
}

func reverse(c []string, start int, end int) {
    for start < end {
        c[start], c[end] = c[end], c[start]
        start++
        end--
    }
}
```

```js
// Translated JavaScript solution
var reverseWords = function (s) {
    // convert string to char array
    // and trim spaces at the same time
    let arr = trimSpaces(s);

    // reverse the whole string
    reverse(arr, 0, arr.length - 1);

    // reverse each word
    reverseEachWord(arr);

    return arr.join("");
};

var trimSpaces = function (s) {
    let left = 0,
        right = s.length - 1;
    // remove leading spaces
    while (left <= right && s[left] === " ") ++left;
    // remove trailing spaces
    while (left <= right && s[right] === " ") --right;
    // reduce multiple spaces to single one
    let output = [];
    while (left <= right) {
        if (s[left] !== " ") output.push(s[left]);
        else if (output[output.length - 1] !== " ") output.push(s[left]);
        ++left;
    }
    return output;
};

var reverseEachWord = function (arr) {
    let n = arr.length;
    let start = 0,
        end = 0;
    while (start < n) {
        // go to the end of the word
        while (end < n && arr[end] !== " ") ++end;
        // reverse the word
        reverse(arr, start, end - 1);
        // move to the next word
        start = end + 1;
        ++end;
    }
};

var reverse = function (arr, start, end) {
    while (start < end) {
        const tmp = arr[start];
        arr[start++] = arr[end];
        arr[end--] = tmp;
    }
};

```


#### Approach 3


```cpp
class Solution {
public:
    string reverseWords(string s) {
        int left = 0, right = s.size() - 1;
        while (left <= right && s[left] == ' ') ++left;
        while (left <= right && s[right] == ' ') --right;

        deque<string> d;
        string word;

        while (left <= right) {
            if (s[left] == ' ' && !word.empty()) {
                d.push_front(word);
                word.clear();
            } else if (s[left] != ' ') {
                word += s[left];
            }
            ++left;
        }
        d.push_front(word);

        string result = "";
        while (!d.empty()) {
            result += d.front();
            d.pop_front();
            if (!d.empty()) {
                result += " ";
            }
        }
        return result;
    }
};
```

```java
class Solution {
    public String reverseWords(String s) {
        int left = 0, right = s.length() - 1;
        // remove leading spaces
        while (left <= right && s.charAt(left) == ' ') ++left;

        // remove trailing spaces
        while (left <= right && s.charAt(right) == ' ') --right;

        Deque<String> d = new ArrayDeque();
        StringBuilder word = new StringBuilder();
        // push word by word in front of deque
        while (left <= right) {
            char c = s.charAt(left);

            if ((word.length() != 0) && (c == ' ')) {
                d.offerFirst(word.toString());
                word.setLength(0);
            } else if (c != ' ') {
                word.append(c);
            }
            ++left;
        }
        d.offerFirst(word.toString());

        return String.join(" ", d);
    }
}
```

```python
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []
        # push word by word in front of deque
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))

        return " ".join(d)
```


```go
func reverseWords(s string) string {
    s = strings.TrimSpace(
        s,
    ) // Trim is done in the beginning to simplify the code
    words := strings.Fields(s)
    left := 0
    right := len(words) - 1
    for left < right {
        words[left], words[right] = words[right], words[left]
        left++
        right--
    }
    return strings.Join(words, " ")
}
```

```js
var reverseWords = function (s) {
    let left = 0,
        right = s.length - 1;
    while (left <= right && s.charAt(left) == " ") left++;
    while (left <= right && s.charAt(right) == " ") right--;

    let d = [];
    let word = "";

    while (left <= right) {
        if (word.length != 0 && s.charAt(left) == " ") {
            d.push(word);
            word = "";
        } else if (s.charAt(left) != " ") {
            word += s.charAt(left);
        }
        left++;
    }
    d.push(word);
    return d.reverse().join(" ");
};
```

------

### [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) | Solved | Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)



```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // The length of the input array
        int length = nums.size();

        // The left and right arrays as described in the algorithm
        vector<int> L(length), R(length), answer(length);

        // L[i] contains the product of all the elements to the left
        // Note: for the element at index '0', there are no elements to the
        // left, so the L[0] would be 1
        L[0] = 1;
        for (int i = 1; i < length; i++) {
            // L[i - 1] already contains the product of elements to the left of
            // 'i - 1' Simply multiplying it with nums[i - 1] would give the
            // product of all elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1];
        }

        // R[i] contains the product of all the elements to the right
        // Note: for the element at index 'length - 1', there are no elements to
        // the right, so the R[length - 1] would be 1
        R[length - 1] = 1;
        for (int i = length - 2; i >= 0; i--) {
            // R[i + 1] already contains the product of elements to the right of
            // 'i + 1' Simply multiplying it with nums[i + 1] would give the
            // product of all elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1];
        }

        // Constructing the answer array
        for (int i = 0; i < length; i++) {
            // For the first element, R[i] would be product except self
            // For the last element of the array, product except self would be
            // L[i] Else, multiple product of all elements to the left and to
            // the right
            answer[i] = L[i] * R[i];
        }

        return answer;
    }
};


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // The length of the input array
        int length = nums.size();

        // The answer vector to be returned
        vector<int> answer(length);

        // answer[i] contains the product of all the elements to the left
        // Note: for the element at index '0', there are no elements to the
        // left, so answer[0] would be 1
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            // answer[i - 1] already contains the product of elements to the
            // left of 'i - 1' Simply multiplying it with nums[i - 1] would give
            // the product of all elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1];
        }

        // R contains the product of all the elements to the right
        // Note: for the element at index 'length - 1', there are no elements to
        // the right, so R would be 1
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            // For the index 'i', R would contain the
            // product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R;
            R *= nums[i];
        }

        return answer;
    }
};
```

```java
class Solution {

    public int[] productExceptSelf(int[] nums) {
        // The length of the input array
        int length = nums.length;

        // The left and right arrays as described in the algorithm
        int[] L = new int[length];
        int[] R = new int[length];

        // Final answer array to be returned
        int[] answer = new int[length];

        // L[i] contains the product of all the elements to the left
        // Note: for the element at index '0', there are no elements to the left,
        // so L[0] would be 1
        L[0] = 1;
        for (int i = 1; i < length; i++) {
            // L[i - 1] already contains the product of elements to the left of 'i - 1'
            // Simply multiplying it with nums[i - 1] would give the product of all
            // elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1];
        }

        // R[i] contains the product of all the elements to the right
        // Note: for the element at index 'length - 1', there are no elements to the right,
        // so the R[length - 1] would be 1
        R[length - 1] = 1;
        for (int i = length - 2; i >= 0; i--) {
            // R[i + 1] already contains the product of elements to the right of 'i + 1'
            // Simply multiplying it with nums[i + 1] would give the product of all
            // elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1];
        }

        // Constructing the answer array
        for (int i = 0; i < length; i++) {
            // For the first element, R[i] would be product except self
            // For the last element of the array, product except self would be L[i]
            // Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i];
        }

        return answer;
    }
}


class Solution {

    public int[] productExceptSelf(int[] nums) {
        // The length of the input array
        int length = nums.length;

        // Final answer array to be returned
        int[] answer = new int[length];

        // answer[i] contains the product of all the elements to the left
        // Note: for the element at index '0', there are no elements to the left,
        // so the answer[0] would be 1
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            // answer[i - 1] already contains the product of elements to the left of 'i - 1'
            // Simply multiplying it with nums[i - 1] would give the product of all
            // elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1];
        }

        // R contains the product of all the elements to the right
        // Note: for the element at index 'length - 1', there are no elements to the right,
        // so the R would be 1
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            // For the index 'i', R would contain the
            // product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R;
            R *= nums[i];
        }

        return answer;
    }
}

```

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):

            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):

            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer
				
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array
        length = len(nums)

        # The answer array to be returned
        answer = [0] * length

        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):

            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]

        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):

            # For the index 'i', R would contain the
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
```

------


### [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Medium

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false. 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?


```
first_num = second_num = some very big number
for n in nums:
    if n is smallest number:
        first_num = n
    else if n is second smallest number:
        second_num = n
    else n is bigger than both first_num and second_num:
        # We have found our triplet, return True

# After loop has terminated
# If we have reached this point, there is no increasing triplet, return False
```

```python
# my solution
class Solution:
def increasingTriplet(self, nums: List[int]) -> bool:
    if len(nums)<3:
        return False
    elif len(nums) == 3:
        return nums[0] < nums[1] < nums[2]

    r1 = r2 = float('inf')

    for i in range(0, len(nums)):
        if nums[i] <=r1:
            r1 = nums[i]
        elif nums[i] <= r2:
            r2 = nums[i]
        elif nums[i] > r1 and nums[i] > r2:
            return True
        
    return False

        

        
```

```cpp

```

```java
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int first_num = Integer.MAX_VALUE;
        int second_num = Integer.MAX_VALUE;
        for (int n: nums) {
            if (n <= first_num) {
                first_num = n;
            } else if (n <= second_num) {
                second_num = n;
            } else {
                return true;
            }
        }
        return false;
    }
}

  public boolean increasingTriplet(int[] nums) {
        if(nums==null || nums.length==0)
            return false;
        int[] dp = new int[nums.length];
        dp[0] = 1;
        for(int i = 1;i<nums.length;i++){
            int j = i-1;
            while(j>=0){
                if(nums[i]>nums[j]){
                    if(dp[j]==2)
                        return true;
                    else
                        dp[i] = 2;
                }
                j--;
            }
        }
        return false;
    }
```

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False
```


```go
// go

```

```js
// js

```


----


### [443. String Compression](https://leetcode.com/problems/string-compression/) |  Medium

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.


```python
# my solution
class Solution:
    def compress(self, chars: List[str]) -> int:
        r = chars[0]
        count = 0
        i = 0
        for c in chars:
            if r == c:
                count += 1
                continue
            else:
                if count == 1:
                    chars[i] = r
                    i += 1
                else:
                    chars[i] = r
                    i += 1
                    t = list(str(count))
                    chars[i:i + len(t)] = t
                    i+= len(t)

                count = 1
                r = c
        
        chars[i] = r
        i += 1
        if count > 1:
            t = list(str(count))
            chars[i:i + len(t)] = t
            i+= len(t)
        return i
```


```cpp
// cpp
class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0, res = 0;
        while (i < chars.size()) {
            int groupLength = 1;
            while (i + groupLength < chars.size() && chars[i + groupLength] == chars[i]) {
                groupLength++;
            }
            chars[res++] = chars[i];
            if (groupLength > 1) {
                for (char c : to_string(groupLength)) {
                    chars[res++] = c;
                }
            }
            i += groupLength;
        }
        return res;
    }
};
```

```java
// java
class Solution {
    public int compress(char[] chars) {
        int i = 0, res = 0;
        while (i < chars.length) {
            int groupLength = 1;
            while (i + groupLength < chars.length && chars[i + groupLength] == chars[i]) {
                groupLength++;
            }
            chars[res++] = chars[i];
            if (groupLength > 1) {
                for (char c : Integer.toString(groupLength).toCharArray()) {
                    chars[res++] = c;
                }
            }
            i += groupLength;
        }
        return res;
    }
}
```

```python
# python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res
```


```go
// go

```

```js
// javascript

```

----

### [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

```python
# my solution

```


```cpp
// cpp
// space sub-optimal 
void moveZeroes(vector<int>& nums) {
    int n = nums.size();

    // Count the zeroes
    int numZeroes = 0;
    for (int i = 0; i < n; i++) {
        numZeroes += (nums[i] == 0);
    }

    // Make all the non-zero elements retain their original order.
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            ans.push_back(nums[i]);
        }
    }

    // Move all zeroes to the end
    while (numZeroes--) {
        ans.push_back(0);
    }

    // Combine the result
    for (int i = 0; i < n; i++) {
        nums[i] = ans[i];
    }
}

// Space optimal, operation sub-optimal
void moveZeroes(vector<int>& nums) {
    int lastNonZeroFoundAt = 0;
    // If the current element is not 0, then we need to
    // append it just in front of last non 0 element we found.
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] != 0) {
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
    // After we have finished processing new elements,
    // all the non-zero elements are already at beginning of array.
    // We just need to fill remaining array with 0's.
    for (int i = lastNonZeroFoundAt; i < nums.size(); i++) {
        nums[i] = 0;
    }
}


void moveZeroes(vector<int>& nums) {
    for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        if (nums[cur] != 0) {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }
}
```

```java
// java

```

```python
# python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1

```


```go
// go

```

```js
// javascript

```


----


### [412 Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104


```python
# my solution

```


```cpp
// cpp

```

```java
// java
class Solution {

    // Naive 
    public List<String> fizzBuzz(int n) {

        // ans list
        List<String> ans = new ArrayList<String>();

        for (int num = 1; num <= n; num++) {

            boolean divisibleBy3 = (num % 3 == 0);
            boolean divisibleBy5 = (num % 5 == 0);

            if (divisibleBy3 && divisibleBy5) {
                // Divides by both 3 and 5, add FizzBuzz
                ans.add("FizzBuzz");
            } else if (divisibleBy3) {
                // Divides by 3, add Fizz
                ans.add("Fizz");
            } else if (divisibleBy5) {
                // Divides by 5, add Buzz
                ans.add("Buzz");
            } else {
                // Not divisible by 3 or 5, add the number
                ans.add(Integer.toString(num));
            }
        }

        return ans;
    }


    // String Concatenation
    public List<String> fizzBuzz(int n) {
        // ans list
        List<String> ans = new ArrayList<String>();

        for (int num = 1; num <= n; num++) {

            boolean divisibleBy3 = (num % 3 == 0);
            boolean divisibleBy5 = (num % 5 == 0);

            String numAnsStr = "";

            if (divisibleBy3) {
                // Divides by 3, add Fizz
                numAnsStr += "Fizz";
            }

            if (divisibleBy5) {
                // Divides by 5, add Buzz
                numAnsStr += "Buzz";
            }

            if (numAnsStr.equals("")) {
                // Not divisible by 3 or 5, add the number
                numAnsStr += Integer.toString(num);
            }

            // Append the current answer str to the ans list
            ans.add(numAnsStr);
        }

        return ans;
    }


    // Hash
    public List<String> fizzBuzz(int n) {

        // ans list
        List<String> ans = new ArrayList<String>();

        // Hash map to store all fizzbuzz mappings.
        HashMap<Integer, String> fizzBuzzDict =
                new HashMap<Integer, String>() {
                    {
                        put(3, "Fizz");
                        put(5, "Buzz");
                    }
                };
            
        // List of divisors which we will iterate over.
        List<Integer> divisors = new ArrayList<>(Arrays.asList(3, 5));

        for (int num = 1; num <= n; num++) {

            String numAnsStr = "";

            for (Integer key : divisors) {

                // If the num is divisible by key,
                // then add the corresponding string mapping to current numAnsStr
                if (num % key == 0) {
                    numAnsStr += fizzBuzzDict.get(key);
                }
            }

            if (numAnsStr.equals("")) {
                // Not divisible by 3 or 5, add the number
                numAnsStr += Integer.toString(num);
            }

            // Append the current answer str to the ans list
            ans.add(numAnsStr);
        }

        return ans;
    }
}
```

```python
# python
class Solution:
def fizzBuzz(self, n: int) -> List[str]:
    answer = []
    for n in range(1, n+1):
        if n%3==0 and n%5==0:
            answer.append("FizzBuzz")
        elif n%3==0:
            answer.append("Fizz")
        elif n%5==0:
            answer.append("Buzz")
        else:
            answer.append(str(n))
    return answer

def fizBuzz(self, n: int) -> List[str]:
    ans = []
    for n in range(1, n+1):
        div3 = (num%3==0)
        div5 = (num%5==0)

        i = ''

        if div3:
            i += 'Fizz'
        if div5:
            i+= 'Buzz'
        if not i:
            i = str(n)
        ans.append(i)
    return ans

def fizBuzz(self, n: int) -> List[str]:
    ans = []

    fizz_buzz_dict = {3: 'fizz', 5:'bzuz'}
    divisors = [3, 5]
    for n in range(1, n+1):
        i = []
        for key in divisors:
            if n % key == 0:
                i.append(fizz_buzz_dict[key])
        if not i:
            i.append(str(n))
        ans.append(''.join(i))
```


```go
// go

```

```js
// javascript

```

### [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12
 

Constraints:

0 <= num <= 106

```python
# my solution

```


```cpp
// cpp

```

```java
// java
public int numberOfSteps(int num) {
    
    // Get the binary for num, as a String.
    String binaryString = Integer.toBinaryString(num);
    
    int steps = 0;
    // Iterate over all the bits in the binary string.
    for (char bit : binaryString.toCharArray()) {
        if (bit == '1') { // If the bit is a 1 
            steps = steps + 2; // Then it'll take 2 to remove.
        } else { // bit == '0'
            steps = steps + 1; // Then it'll take 1 to remove.
        }
    }

    // We need to subtract 1, because the last bit was over-counted.
    return steps - 1;
}


public int numberOfSteps(int num) {

    // We need to handle this as a special case, otherwise it'll return -1.
    if (num == 0) return 0;

    int steps = 0;

    for (int powerOfTwo = 1; powerOfTwo <= num; powerOfTwo = powerOfTwo * 2) {
        // Apply the bit mask to check if the bit at "powerOfTwo" is a 1.
        if ((powerOfTwo & num) != 0) {
            steps = steps + 2;
        } else {
            steps = steps + 1;
        }
    }

    // We need to subtract 1, because the last bit was over-counted.
    return steps - 1;
} 
```

```python
# python
class Solution:
def numberOfSteps(self, num: int) -> int:
    n = num
    c = 0
    while(n):
        if n%2==0:
            n = n / 2
        else:
            n = n - 1
        c += 1
    return c

def numberOfSteps(self, num: int) -> int:
    s = 0
    binary = bin(num)[2:] # remove 0b
    for bit in binary:
        if bit == '1':
            s += 2
        else:
            s += 1
    return s - 1 # to account off-by-one error Last digit -- even if its one only takes one step. 

def numberOfSteps(self, num: int) -> int:
    binary = bin(num)[2:]
    ones = binary.count("1")
    total = len(binary)
    return ones + total - 1

def numberOfSteps(self, num: int) -> int:
    if n == 0:
        return 0
    s = 0
    power_of_two = 1

    while power_of_two <= n:
        if (power_of_two & n) != 0:
            s += 2
        else:
            s += 1
        power_of_two = power_of_two * 2
    return s - 1
```


```go
// go

```

```js
// javascript

```
-----

### [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/) | Easy

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node. 

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

```python
# my solution

```


```cpp
// cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        vector<ListNode*> A = {head};
        while (A.back()->next != NULL)
            A.push_back(A.back()->next);
        return A[A.size() / 2];
    }
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

```java
// java
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode[] A = new ListNode[100];
        int t = 0;
        while (head != null) {
            A[t++] = head;
            head = head.next;
        }
        return A[t / 2];
    }
}

class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}
```

```python
# python
class Solution:
def middleNode(self, head: ListNode) -> ListNode:
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr) // 2]

class Solution:
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```


```go
// go

```

```js
// javascript
var middleNode = function(head) {
    let A = [head];
    while (A[A.length - 1].next != null)
        A.push(A[A.length - 1].next);
    return A[Math.trunc(A.length / 2)];
};

var middleNode = function(head) {
    slow = fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};
```

------- 
 
### [383. Ransom Note](https://leetcode.com/problems/ransom-note/description/) | Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote. 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

    - approach 1
      - for each char in ransomNote: look if there is a match in magazine; if yes, remove and update magazine; if no -- return false
      - O(m.n) Time and O(m) space
    - approach 2: two hashmaps
    - approach 3: one hashmap
    - approach 4: sorting and stacks

```python
# my solution

```


```cpp
// cpp

```

```java
// java
public boolean canConstruct(String ransomNote, String magazine) {
    // For each character, c,  in the ransom note.
    for (char c : ransomNote.toCharArray()) {
        // Find the index of the first occurrence of c in the magazine.
        int index = magazine.indexOf(c);
        // If there are none of c left in the String, return False.
        if (index == -1) {
            return false;
        }
        // Use substring to make a new string with the characters 
        // before "index" (but not including), and the characters 
        // after "index". 
        magazine = magazine.substring(0, index) + magazine.substring(index + 1);
    }
    // If we got this far, we can successfully build the note.
    return true;
}

class Solution {
    
    // Takes a String, and returns a HashMap with counts of
    // each character.
    private Map<Character, Integer> makeCountsMap(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            int currentCount = counts.getOrDefault(c, 0);
            counts.put(c, currentCount + 1);
        }
        return counts;
    }
    
    
    public boolean canConstruct(String ransomNote, String magazine) {
        
        // Check for obvious fail case.
        if (ransomNote.length() > magazine.length()) {
            return false;
        }

        // Make the count maps.
        Map<Character, Integer> ransomNoteCounts = makeCountsMap(ransomNote);
        Map<Character, Integer> magazineCounts = makeCountsMap(magazine);
        
        // For each unique character, c, in the ransom note:
        for (char c : ransomNoteCounts.keySet()) {
            // Check that the count of char in the magazine is equal
            // or higher than the count in the ransom note.
            int countInMagazine = magazineCounts.getOrDefault(c, 0);
            int countInRansomNote = ransomNoteCounts.get(c);
            if (countInMagazine < countInRansomNote) {
                return false;
            }
        }
        
        // If we got this far, we can successfully build the note.
        return true;
    }
}


class Solution {
    
    // Takes a String, and returns a HashMap with counts of
    // each character.
    private Map<Character, Integer> makeCountsMap(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (char c : s.toCharArray()) {
            int currentCount = counts.getOrDefault(c, 0);
            counts.put(c, currentCount + 1);
        }
        return counts;
    }
    
    
    public boolean canConstruct(String ransomNote, String magazine) {
        
        // Check for obvious fail case.
        if (ransomNote.length() > magazine.length()) {
            return false;
        }

        // Make a counts map for the magazine.
        Map<Character, Integer> magazineCounts = makeCountsMap(magazine);
        
        // For each character in the ransom note:
        for (char c : ransomNote.toCharArray()) {
            // Get the current count for c in the magazine.
            int countInMagazine = magazineCounts.getOrDefault(c, 0);
            // If there are none of c left, return false.
            if (countInMagazine == 0) {
                return false;
            }
            // Put the updated count for c back into magazineCounts.
            magazineCounts.put(c, countInMagazine - 1);
        }
        
        // If we got this far, we can successfully build the note.
        return true;
    }
}


class Solution {
    
    // Please, if there's a nicer way of doing this, without getting tangled in
    // primitives vs Java's generics let me know in the article comments :-)
    private Stack<Character> sortedCharacterStack(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        Stack<Character> stack = new Stack<>();
        for (int i = s.length() - 1; i >= 0; i--) {
            stack.push(charArray[i]);
        }
        return stack;
    }
    
    
    public boolean canConstruct(String ransomNote, String magazine) {
        
        // Check for obvious fail case.
        if (ransomNote.length() > magazine.length()) {
            return false;
        }
        
        // Reverse sort the characters of the note and magazine, and then
        // put them into stacks.
        Stack<Character> magazineStack = sortedCharacterStack(magazine);
        Stack<Character> ransomNoteStack = sortedCharacterStack(ransomNote);
        
        // And now process the stacks, while both have letters remaining.
        while (!magazineStack.isEmpty() && !ransomNoteStack.isEmpty()) {
            // If the tops are the same, pop both because we have found a match.
            if (magazineStack.peek().equals(ransomNoteStack.peek())) {
                ransomNoteStack.pop();
                magazineStack.pop();
            } 
            // If magazine's top is earlier in the alphabet, we should remove that 
            // character of magazine as we definitely won't need that letter.
            else if (magazineStack.peek() < ransomNoteStack.peek()) {
                magazineStack.pop();
            }
            // Otherwise, it's impossible for top of ransomNote to be in magazine.
            else {
                return false;
            }
        }
                
        // Return true iff the entire ransomNote was built.
        return ransomNoteStack.isEmpty();
        
    }
}
```

```python
# python
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # For each character, c,  in the ransom note.
    for c in ransomNote:
        # If there are none of c left in the String, return False.
        if c not in magazine:
            return False
        # Find the index of the first occurrence of c in the magazine.
        location = magazine.index(c)
        # Use splicing to make a new string with the characters 
        # before "location" (but not including), and the characters 
        #after "location". 
        magazine = magazine[:location] + magazine[location + 1:]
    # If we got this far, we can successfully build the note.
    return True

def canConstruct(self, ransomNote: str, magazine: str) -> bool:

    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    magazine_counts = collections.Counter(magazine)
    ransom_note_counts = collections.Counter(ransomNote)
        
    # For each *unique* character in the ransom note:
    for char, count in ransom_note_counts.items():
        # Check that the count of char in the magazine is equal
        # or higher than the count in the ransom note.
        magazine_count = magazine_counts[char]
        if magazine_count < count:
            return False
                
    # If we got this far, we can successfully build the note.
    return True

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False

    # In Python, we can use the Counter class. It does all the work that the
    # makeCountsMap(...) function in our pseudocode did!
    letters = collections.Counter(magazine)
        
    # For each character, c, in the ransom note:
    for c in ransomNote:
        # If there are none of c left, return False.
        if letters[c] <= 0:
            return False
        # Remove one of c from the Counter.
        letters[c] -= 1
    # If we got this far, we can successfully build the note.
    return True


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
    # Check for obvious fail case.
    if len(ransomNote) > len(magazine): return False
        
    # Reverse sort the note and magazine. In Python, we simply 
    # treat a list as a stack.
    ransomNote = sorted(ransomNote, reverse=True) 
    magazine = sorted(magazine, reverse=True)
        
    # While there are letters left on both stacks:
    while ransomNote and magazine:
        # If the tops are the same, pop both because we have found a match.
        if ransomNote[-1] == magazine[-1]:
            ransomNote.pop()
            magazine.pop()
        # If magazine's top is earlier in the alphabet, we should remove that 
        # character of magazine as we definitely won't need that letter.
        elif magazine[-1] < ransomNote[-1]:
            magazine.pop()
        # Otherwise, it's impossible for top of ransomNote to be in magazine.
        else:
            return False   
    # Return true iff the entire ransomNote was built.
    return not ransomNote
```


```go
// go

```

```js
// javascript

```

------- 

###  [198. House Robber](https://leetcode.com/problems/house-robber/description/) Medium
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12. 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400


```python
# my solution

```


```cpp
// cpp

// recursion with memoization
class Solution {
public:
    vector<int> memo;

    int rob(vector<int>& nums) {
        memo.resize(100, -1);

        return robFrom(0, nums);
    }

private:
    int robFrom(int i, vector<int>& nums) {
        // No more houses left to examine.
        if (i >= nums.size()) {
            return 0;
        }

        // Return cached value.
        if (memo[i] > -1) {
            return memo[i];
        }

        // Recursive relation evaluation to get the optimal answer.
        int ans = max(robFrom(i + 1, nums), robFrom(i + 2, nums) + nums[i]);

        // Cache for future use.
        memo[i] = ans;
        return ans;
    }
};


// DP with tablulation -- bottom-up approach
class Solution {
public:
    int rob(vector<int>& nums) {
        int N = nums.size();

        // Special handling for empty case.
        if (N == 0) {
            return 0;
        }

        vector<int> maxRobbedAmount(N + 1);

        // Base case initializations.
        maxRobbedAmount[N] = 0;
        maxRobbedAmount[N - 1] = nums[N - 1];

        // DP table calculations.
        for (int i = N - 2; i >= 0; --i) {
            // Same as the recursive solution.
            maxRobbedAmount[i] =
                max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]);
        }

        return maxRobbedAmount[0];
    }
};
```

```java
// java
// recursion with memoization 

class Solution {
    private int[] memo;

    public int rob(int[] nums) {
        this.memo = new int[100];

        // Fill with sentinel value representing not-calculated recursions.
        Arrays.fill(this.memo, -1);

        return this.robFrom(0, nums);
    }

    private int robFrom(int i, int[] nums) {
        // No more houses left to examine.
        if (i >= nums.length) {
            return 0;
        }

        // Return cached value.
        if (this.memo[i] > -1) {
            return this.memo[i];
        }

        // Recursive relation evaluation to get the optimal answer.
        int ans = Math.max(
            this.robFrom(i + 1, nums),
            this.robFrom(i + 2, nums) + nums[i]
        );

        // Cache for future use.
        this.memo[i] = ans;
        return ans;
    }
}

// DP with tabulation -- bottom-up approach
class Solution {
    public int rob(int[] nums) {
        int N = nums.length;

        // Special handling for empty array case.
        if (N == 0) {
            return 0;
        }

        int[] maxRobbedAmount = new int[nums.length + 1];

        // Base case initializations.
        maxRobbedAmount[N] = 0;
        maxRobbedAmount[N - 1] = nums[N - 1];

        // DP table calculations.
        for (int i = N - 2; i >= 0; --i) {
            // Same as the recursive solution.
            maxRobbedAmount[i] = Math.max(
                maxRobbedAmount[i + 1],
                maxRobbedAmount[i + 2] + nums[i]
            );
        }

        return maxRobbedAmount[0];
    }
}
```

```python
# python
# recursion with memoization

class Solution:

def __init__(self):
    self.memo = {}

def rob(self, nums: List[int]) -> int:

    self.memo = {}

    return self.robFrom(0, nums)

def robFrom(self, i, nums):

    # No more houses left to examine.
    if i >= len(nums):
        return 0

    # Return cached value.
    if i in self.memo:
        return self.memo[i]

    # Recursive relation evaluation to get the optimal answer.
    ans = max(
        self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i]
    )

    # Cache for future use.
    self.memo[i] = ans
    return ans

# DP with tabulation --- bottom-up approach
class Solution:

def rob(self, nums: List[int]) -> int:

    # Special handling for empty case.
    if not nums:
        return 0

    maxRobbedAmount = [None for _ in range(len(nums) + 1)]
    N = len(nums)

    # Base case initialization.
    maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]

    # DP table calculations.
    for i in range(N - 2, -1, -1):

        # Same as recursive solution.
        maxRobbedAmount[i] = max(
            maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i]
        )

    return maxRobbedAmount[0]
```


```go
// go

```

```js
// javascript

```

------- 

</details>

-----

## Leetcode 75


<details open>
    <summary> Leetcode 75 </summary>

<br>

### 0 : TOC

- Array / String 
- Two Pointers
- Sliding Window
- Prefix Sum
- Heat Map / Set
- Stack
- Queue
- Linked List
- Binary Tree - BFS
- Binary Tree - DFS
- Binary Search Tree
- Graphs - BFS
- Graphs - DFS
- Heap / Priority Queue
- Binary Search
- Backtracking
- DP - 1D
- DP - Multidimensional
- Bit Manipulation
- Trie
- Intervals
- Monotonic Stack

### 1 : 1768. Merge Strings Alternately : easy

    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.

 

    Example 1:

    Input: word1 = "abc", word2 = "pqr"
    Output: "apbqcr"
    Explanation: The merged string will be merged as so:
    word1:  a   b   c
    word2:    p   q   r
    merged: a p b q c r
    Example 2:

    Input: word1 = "ab", word2 = "pqrs"
    Output: "apbqrs"
    Explanation: Notice that as word2 is longer, "rs" is appended to the end.
    word1:  a   b 
    word2:    p   q   r   s
    merged: a p b q   r   s
    Example 3:

    Input: word1 = "abcd", word2 = "pq"
    Output: "apbqcd"
    Explanation: Notice that as word1 is longer, "cd" is appended to the end.
    word1:  a   b   c   d
    word2:    p   q 
    merged: a p b q c   d
 

    Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.

#### Approach 1: Two Pointers O(m + n)

```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        string result = "";
        int i = 0, j = 0;

        while (i < m || j < n) {
            if (i < m) {
                result.push_back(word1[i++]);
            }
            if (j < n) {
                result.push_back(word2[j++]);
            }
        }

        return result;
    }
};
```

```java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        StringBuilder result = new StringBuilder();
        int i = 0, j = 0;

        while (i < m || j < n) {
            if (i < m) {
                result.append(word1.charAt(i++));
            }
            if (j < n) {
                result.append(word2.charAt(j++));
            }
        }

        return result.toString();
    }
}
```

```python
class Solution(object):
def mergeAlternately(self, word1, word2):
    m = len(word1)
    n = len(word2)
    i = 0
    j = 0
    result = []

    while i < m or j < n:
        if i < m:
            result += word1[i]
            i += 1
        if j < n:
            result += word2[j]
            j += 1

    return "".join(result)
```

#### Approach 2: One Pointer O(m + n)

```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        string result = "";

        for (int i = 0; i < max(m, n); i++) {
            if (i < m) {
                result.push_back(word1[i]);
            }
            if (i < n) {
                result.push_back(word2[i]);
            }
        }

        return result;
    }
};
```

```java
class Solution {
    public String mergeAlternately(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.max(m, n); i++) {
            if (i < m) {
                result.append(word1.charAt(i));
            }
            if (i < n) {
                result.append(word2.charAt(i));
            }
        }

        return result.toString();
    }
}
```

```python
class Solution(object):
def mergeAlternately(self, word1, word2):
    result = []
    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

    return "".join(result)
```

### 2 : 1071. Greatest Common Divisor of Strings : easy

    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

    Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"
    Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"
    Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
 

    Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.

#### Approach 1: Brute force O(min(m,n)⋅(m+n)) T O(min(m, n)) S

```cpp
class Solution {
public:
    bool valid(string str1, string str2, int k) {
        int len1 = str1.size(), len2 = str2.size();
        if (len1 % k > 0 || len2 % k > 0) {
            return false;
        } else {
            string base = str1.substr(0, k);
            int n1 = len1 / k, n2 = len2 / k;
            return str1 == joinWords(base, n1) && str2 == joinWords(base, n2);
        }
    }
    string joinWords(string str, int k) {
        string ans = "";
        for (int i = 0; i < k; ++i) {
            ans += str;
        }
        return ans;
    }
    
    
    string gcdOfStrings(string str1, string str2) {
        int len1 = str1.length(), len2 = str2.length();
        for (int i = min(len1, len2); i >= 1; --i) {
            if (valid(str1, str2, i)) {
                return str1.substr(0, i);
            }
        }
        return "";
    }
};
```

```java
class Solution {
    public boolean valid(String str1, String str2, int k) {
        int len1 = str1.length(), len2 = str2.length();
        if (len1 % k > 0 || len2 % k > 0) {
            return false;
        } else {
            String base = str1.substring(0, k);
            return str1.replace(base, "").isEmpty() && str2.replace(base, "").isEmpty();
        }
    }
    
    
    public String gcdOfStrings(String str1, String str2) {
        int len1 = str1.length(), len2 = str2.length();
        for (int i = Math.min(len1, len2); i >= 1; --i) {
            if (valid(str1, str2, i)) {
                return str1.substring(0, i);
            }
        }
        return "";
    }
}
```

```python

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
```

#### Approach 2: Greatest Common Divisor O(m+n) Time and

```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // Check if they have non-zero GCD string.
        if (str1 + str2 != str2 + str1) {
            return "";
        }

        // Get the GCD of the two lengths.
        int gcdLength = gcd(str1.size(), str2.size());
        return str1.substr(0, gcdLength);
    }
};
```

```java
class Solution {
    public int gcd(int x, int y) {
        if (y == 0) {
            return x;
        } else {
            return gcd(y, x % y);
        }    
    }
    
    public String gcdOfStrings(String str1, String str2) {
        // Check if they have non-zero GCD string.
        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }
        
        // Get the GCD of the two lengths.
        int gcdLength = gcd(str1.length(), str2.length());
        return str1.substring(0, gcdLength);
    }
}
```

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
```



### : 11. Container With Most Water : medium

    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

 

    Example 1:


    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    Example 2:

    Input: height = [1,1]
    Output: 1
 

    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

#### Approach 1: Brute Force O(n^2) Time and O(1) Space

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxarea = 0;
        for (int left = 0; left < height.size(); left++) {
            for (int right = left + 1; right < height.size(); right++) {
                int width = right - left;
                maxarea = max(maxarea, min(height[left], height[right]) * width);
            }
        }
        return maxarea;
    }
};
```

```java
public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0;
        for (int left = 0; left < height.length; left++) {
            for (int right = left + 1; right < height.length; right++) {
                int width = right - left;
                maxarea = Math.max(
                    maxarea,
                    Math.min(height[left], height[right]) * width
                );
            }
        }
        return maxarea;
    }
}
```

```python
class Solution:
def maxArea(self, height: List[int]) -> int:
    maxarea = 0
    for left in range(len(height)):
        for right in range(left + 1, len(height)):
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)

    return maxarea
```

#### Approach 2: Two Pointer Approach O(n) Time and O(1) Space

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxArea = 0;
        int left = 0;
        int right = height.size() - 1;

        while (left < right) {
            int width = right - left;
            maxArea = max(maxArea, min(height[left], height[right]) * width);
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
};
```

```java
public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            int width = right - left;
            maxarea = Math.max(
                maxarea,
                Math.min(height[left], height[right]) * width
            );
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxarea;
    }
}
```

```python
class Solution:
def maxArea(self, height: List[int]) -> int:
    maxarea = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        maxarea = max(maxarea, min(height[left], height[right]) * width)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return maxarea
```












</details>

-----
