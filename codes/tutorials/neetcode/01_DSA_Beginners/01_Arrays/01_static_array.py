import array


# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# Remove from the last position in the array if the array
# is not empty (i.e. length is non-zero).
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also the length to decreased by 1.
        arr[length - 1] = 0


# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n


# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr, i, length):
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted


def printArr(arr, capacity):
    for i in range(capacity):
        print(arr[i])


def main():
    # 1. Creating an array
    arr = array.array(
        "i", [1, 2, 3, 4, 5, 15]
    )  # 'i' is the typecode for signed integers
    print("Original array:", arr)

    # 2. Accessing elements
    print("\nAccessing elements:")
    for i in range(len(arr)):
        print(f"Element at index {i}: {arr[i]}")

    # 3. Modifying elements
    arr[1] = 10
    print("\nArray after modifying the second element (index 1):", arr)

    # 4. Inserting an element
    arr.insert(2, 15)  # Insert 15 at index 2
    print("\nArray after inserting 15 at index 2:", arr)

    # 5. Removing an element
    arr.remove(15)  # Removes the first occurrence of 15
    print("\nArray after removing 15:", arr)

    # 6. Traversing an array using a loop
    print("\nTraversing the array using a loop:")
    for element in arr:
        print(element, end=" ")
    print()

    # 7. Sum of all elements
    array_sum = sum(arr)
    print(f"\nSum of elements in the array: {array_sum}")

    # 8. Finding the maximum element
    max_element = max(arr)
    print(f"Maximum element in the array: {max_element}")

    # 9. Finding the minimum element
    min_element = min(arr)
    print(f"Minimum element in the array: {min_element}")

    # 10. Sorting the array
    sorted_arr = sorted(
        arr
    )  # This creates a sorted list, doesn't change the array itself
    print(f"\nSorted array (as a list): {sorted_arr}")

    # 11. Reversing the array
    arr.reverse()  # In-place reverse
    print(f"Array after reversing: {arr}")

    # 12. Array slicing
    print("\nSlicing the array (elements from index 1 to 3):", arr[1:4])

    # 13. Converting array to list
    arr_list = arr.tolist()
    print(f"\nArray converted to a Python list: {arr_list}")

    # 14. Appending an element
    arr.append(100)  # Appends 100 at the end
    print("\nArray after appending 100:", arr)

    # 15. Array typecode and size
    print(f"\nArray typecode: {arr.typecode}")
    print(f"Size of one array element (in bytes): {arr.itemsize}")

    # 16. Multi-dimensional array (using a list of arrays)
    matrix = [
        array.array("i", [1, 2, 3]),
        array.array("i", [4, 5, 6]),
        array.array("i", [7, 8, 9]),
    ]
    print("\n2D Array (List of arrays):")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def array_operations_with_examples():
    """
    This function demonstrates common array operations along with their time complexities.
    """

    # 1. Accessing an element by index - O(1)
    arr = [10, 20, 30, 40, 50]
    print("\n\n\n\n1. Access by Index:")
    print(f"   - arr[2] = {arr[2]}")  # Access element at index 2
    print("   - Time Complexity: O(1)\n")

    # 2. Modifying an element by index - O(1)
    arr[2] = 100
    print("2. Modifying by Index:")
    print(f"   - Modified arr[2] = {arr[2]}")
    print("   - Time Complexity: O(1)\n")

    # 3. Appending an element - O(1) Amortized
    arr.append(60)
    print("3. Appending (Adding at the End):")
    print(f"   - Appended 60: {arr}")
    print("   - Time Complexity: O(1) Amortized\n")

    # 4. Inserting an element at the beginning/middle - O(n)
    arr.insert(1, 15)
    print("4. Inserting at the Beginning or Middle:")
    print(f"   - Inserted 15 at index 1: {arr}")
    print("   - Time Complexity: O(n)\n")

    # 5. Removing an element by value - O(n)
    arr.remove(100)
    print("5. Removing an Element by Value:")
    print(f"   - Removed 100: {arr}")
    print("   - Time Complexity: O(n)\n")

    # 6. Removing an element by index - O(n)
    arr.pop(1)
    print("6. Removing by Index:")
    print(f"   - Removed element at index 1: {arr}")
    print("   - Time Complexity: O(n)\n")

    # 7. Searching for an element - O(n)
    found = 50 in arr
    print("7. Searching for an Element:")
    print(f"   - Is 50 in the array? {found}")
    print("   - Time Complexity: O(n)\n")

    # 8. Getting the length of an array - O(1)
    length = len(arr)
    print("8. Getting the Length of the Array:")
    print(f"   - Length of array: {length}")
    print("   - Time Complexity: O(1)\n")

    # 9. Slicing an array - O(k)
    sliced_arr = arr[1:4]
    print("9. Slicing an Array:")
    print(f"   - Sliced array [1:4]: {sliced_arr}")
    print("   - Time Complexity: O(k), where k is the length of the slice\n")

    # 10. Reversing an array - O(n)
    arr.reverse()
    print("10. Reversing the Array:")
    print(f"   - Reversed array: {arr}")
    print("   - Time Complexity: O(n)\n")

    # 11. Sorting an array - O(n log n)
    arr.sort()
    print("11. Sorting the Array:")
    print(f"   - Sorted array: {arr}")
    print("   - Time Complexity: O(n log n)\n")

    # 12. Sum of all elements - O(n)
    total = sum(arr)
    print("12. Sum of Elements:")
    print(f"   - Sum of all elements: {total}")
    print("   - Time Complexity: O(n)\n")

    # 13. Finding the maximum element - O(n)
    max_element = max(arr)
    print("13. Finding Max Element:")
    print(f"   - Maximum element: {max_element}")
    print("   - Time Complexity: O(n)\n")


def array_data_types_examples_with_powers():
    """
    This function explains different data types supported by the 'array' module
    in Python along with their ranges, expressed in powers of 10, and examples.
    """
    print(
        "\n\n\n\n\n### Array Data Types with Ranges (in Powers of 10) and Examples ###\n"
    )

    # 1. 'b' - Signed char (integer, 1 byte)
    signed_char_arr = array.array("b", [-128, 127])
    print("1. 'b' (Signed Char, 1 byte):")
    print(f"   - Example: {signed_char_arr}")
    print("   - Range: -128 to 127 (~ -1.28 x 10^2 to 1.27 x 10^2)\n")

    # 2. 'B' - Unsigned char (integer, 1 byte)
    unsigned_char_arr = array.array("B", [0, 255])
    print("2. 'B' (Unsigned Char, 1 byte):")
    print(f"   - Example: {unsigned_char_arr}")
    print("   - Range: 0 to 255 (~ 0 to 2.55 x 10^2)\n")

    # 3. 'h' - Signed short (integer, 2 bytes)
    signed_short_arr = array.array("h", [-32768, 32767])
    print("3. 'h' (Signed Short, 2 bytes):")
    print(f"   - Example: {signed_short_arr}")
    print("   - Range: -32,768 to 32,767 (~ -3.28 x 10^4 to 3.27 x 10^4)\n")

    # 4. 'H' - Unsigned short (integer, 2 bytes)
    unsigned_short_arr = array.array("H", [0, 65535])
    print("4. 'H' (Unsigned Short, 2 bytes):")
    print(f"   - Example: {unsigned_short_arr}")
    print("   - Range: 0 to 65,535 (~ 0 to 6.55 x 10^4)\n")

    # 5. 'i' - Signed int (integer, 4 bytes)
    signed_int_arr = array.array("i", [-2147483648, 2147483647])
    print("5. 'i' (Signed Int, 4 bytes):")
    print(f"   - Example: {signed_int_arr}")
    print(
        "   - Range: -2,147,483,648 to 2,147,483,647 (~ -2.15 x 10^9 to 2.15 x 10^9)\n"
    )

    # 6. 'I' - Unsigned int (integer, 4 bytes)
    unsigned_int_arr = array.array("I", [0, 4294967295])
    print("6. 'I' (Unsigned Int, 4 bytes):")
    print(f"   - Example: {unsigned_int_arr}")
    print("   - Range: 0 to 4,294,967,295 (~ 0 to 4.29 x 10^9)\n")

    # 7. 'l' - Signed long (integer, 4 bytes)
    signed_long_arr = array.array("l", [-2147483648, 2147483647])
    print("7. 'l' (Signed Long, 4 bytes):")
    print(f"   - Example: {signed_long_arr}")
    print(
        "   - Range: -2,147,483,648 to 2,147,483,647 (~ -2.15 x 10^9 to 2.15 x 10^9)\n"
    )

    # 8. 'L' - Unsigned long (integer, 4 bytes)
    unsigned_long_arr = array.array("L", [0, 4294967295])
    print("8. 'L' (Unsigned Long, 4 bytes):")
    print(f"   - Example: {unsigned_long_arr}")
    print("   - Range: 0 to 4,294,967,295 (~ 0 to 4.29 x 10^9)\n")

    # 9. 'q' - Signed long long (integer, 8 bytes)
    signed_long_long_arr = array.array("q", [-9223372036854775808, 9223372036854775807])
    print("9. 'q' (Signed Long Long, 8 bytes):")
    print(f"   - Example: {signed_long_long_arr}")
    print(
        "   - Range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 (~ -9.22 x 10^18 to 9.22 x 10^18)\n"
    )

    # 10. 'Q' - Unsigned long long (integer, 8 bytes)
    unsigned_long_long_arr = array.array("Q", [0, 18446744073709551615])
    print("10. 'Q' (Unsigned Long Long, 8 bytes):")
    print(f"   - Example: {unsigned_long_long_arr}")
    print("   - Range: 0 to 18,446,744,073,709,551,615 (~ 0 to 1.84 x 10^19)\n")

    # 11. 'f' - Float (4 bytes, single-precision floating point)
    float_arr = array.array("f", [-3.4028235e38, 3.4028235e38])
    print("11. 'f' (Float, 4 bytes):")
    print(f"   - Example: {float_arr}")
    print("   - Range: -3.4028235 x 10^38 to 3.4028235 x 10^38\n")

    # 12. 'd' - Double (8 bytes, double-precision floating point)
    double_arr = array.array("d", [-1.7976931348623157e308, 1.7976931348623157e308])
    print("12. 'd' (Double, 8 bytes):")
    print(f"   - Example: {double_arr}")
    print("   - Range: -1.7976931348623157 x 10^308 to 1.7976931348623157 x 10^308\n")


def list_tutorial():
    """
    A comprehensive tutorial on Python lists covering:
    - List creation
    - List operations
    - Time complexities
    - Supported data types and their ranges
    """
    
    print("\n### Python List Tutorial ###\n")
    
    # 1. List Creation
    print("1. List Creation:")
    empty_list = []
    list_of_integers = [1, 2, 3, 4, 5]
    list_of_strings = ["apple", "banana", "cherry"]
    list_of_mixed = [1, "apple", 3.14, True]

    print(f"   - Empty list: {empty_list}")
    print(f"   - List of integers: {list_of_integers}")
    print(f"   - List of strings: {list_of_strings}")
    print(f"   - List of mixed types: {list_of_mixed}\n")

    # 2. Basic List Operations
    print("2. Basic List Operations:")

    # Append an element
    list_of_integers.append(6)
    print(f"   - After append(6): {list_of_integers}")

    # Insert an element
    list_of_integers.insert(0, 0)
    print(f"   - After insert(0, 0): {list_of_integers}")

    # Remove an element by value
    list_of_integers.remove(3)
    print(f"   - After remove(3): {list_of_integers}")

    # Pop an element by index
    popped_value = list_of_integers.pop(2)
    print(f"   - After pop(2): {list_of_integers}, Popped value: {popped_value}")

    # List slicing
    sliced_list = list_of_integers[1:4]
    print(f"   - Sliced list (1:4): {sliced_list}\n")

    # 3. List Traversal
    print("3. List Traversal (Looping through a list):")
    for element in list_of_strings:
        print(f"   - Element: {element}")
    
    # 4. List Comprehension
    print("\n4. List Comprehension:")
    squared_list = [x ** 2 for x in list_of_integers]
    print(f"   - Squared values: {squared_list}\n")
    
    # 5. Supported Data Types and Ranges (Including Time Complexities)
    print("5. Supported Data Types and Ranges:")
    
    # Integer range in lists
    large_int_list = [10**9, 10**10]
    print(f"   - List of large integers: {large_int_list}")
    
    # Float range in lists
    large_float_list = [3.14e38, 1.79e308]
    print(f"   - List of large floats: {large_float_list} (single precision, double precision)\n")
    
    # Strings in lists
    string_list = ["small string", "a" * 1000]
    print(f"   - List of strings: {string_list[:2]} (string length: up to memory limits)\n")
    
    # Lists can store objects (e.g., custom class instances)
    class ExampleClass:
        def __init__(self, value):
            self.value = value
            
    object_list = [ExampleClass(1), ExampleClass(2)]
    print(f"   - List of objects (custom class instances): {[obj.value for obj in object_list]}\n")

    # 6. Time Complexities of List Operations
    print("6. Time Complexities of List Operations:")
    print("   - Append: O(1) - Adding an element at the end")
    print("   - Insert: O(n) - Adding an element at a specific index (shifts elements)")
    print("   - Remove: O(n) - Removing an element by value (needs to find the element)")
    print("   - Pop: O(1) - Removing an element from the end, O(n) for removing from a specific index")
    print("   - Access by Index: O(1) - Accessing an element directly by its index")
    print("   - List Slicing: O(k) - Slicing a list where 'k' is the size of the slice")
    print("   - List Traversal (loop): O(n) - Iterating over all elements\n")

    # 7. Nested Lists (List of Lists)
    print("7. Nested Lists (List of Lists):")
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"   - Example of nested list: {nested_list}")
    print(f"   - Access element [1][1]: {nested_list[1][1]} (row 1, column 1)\n")
    
    # 8. Common List Methods
    print("8. Common List Methods:")
    
    # Count occurrences
    count_value = list_of_integers.count(2)
    print(f"   - Count occurrences of 2: {count_value}")
    
    # Reverse the list
    list_of_integers.reverse()
    print(f"   - Reversed list: {list_of_integers}")
    
    # Sort the list
    list_of_integers.sort()
    print(f"   - Sorted list: {list_of_integers}\n")

if __name__ == "__main__":
    main()
    array_operations_with_examples()
    array_data_types_examples_with_powers()
    list_tutorial()