# Java : Tutorials Point 

- June 1991 -->GreenTalk(.gt) --> Oak language --> Green --> Java ( Island in Indonesia, java coffee - unique, dynamic, revolutionary, fun)
- Java - high-level, object-oriented programming language. Developed by Sun Microsystems - James Gosling, released in 1995. Now, owned by Oracle.
- general purpose programming language; WORA - Write Once, Run Anywhere -- Once compiled, can run on any platform.
- 13 Nov 2006 -- GNU General Public License (GPL)
- 08 May 2007 -- all was opensourced except a part to which sun didn't have copyright  

    ```java
    public class MyFirstJavaProgram {

    /* This is my first java program.
        * This will print 'Hello, World!' as the output
        */

    public static void main(String []args) {
        System.out.println("Hello, World!"); // prints Hello, World!
    }
    }
    ```
- Java is 
  1. object oriented
     1. polymorphism
     2. inheritance
     3. encapsulation
     4. abstraction
     5. classes
     6. objects
     7. instance
     8. method
     9. message passing
  2. platform independent -- java code is compiled into platform neutral byte code executed by JVM Java Virtual Machine. JVMs are platform specific. 
  3. easy to learn -- inherits features from C and C++
     1. No pointers, operator overloading, multiple inheritance, explicit memory allocation, etc...
  4. Secure - java is secure by architecture. Automatic garbage collection. No need to interact with underlying memory or operating system. Authentication is based on public-key encryption.
  5. Architecture neutral - JRE handles code execution on different processors with architecture neutral object file format
  6. Portable - Compiler in Java is written in ANSI C with a clean portability boundary, which is a POSIX subset; POSIX - Portable Operating System Interface
  7. Robust - stron compile time error-checking, strict type-checking, runtime exception handling; no pointers, no direct access to memory
  8. Multithreading - multiprocessing and multithreading - two or more parts that run concurrently; multitasking is when multiple processes share common resourcesl multithreading - multiple activities running in parallel in the same program
     1. thread handling 
     2. monitors
     3. deadlock handling 
     4. racing conditions
  9.  High Performance - Just in time Compiler
  10. Distributed - Designed for Distributed Systems
  11. Open Source
  12. Interpreted - byte code is translated on the fly and is not stored anywhere; jvm compiles bytecode in binary using JIT compilation 
      1.  Method inlining
      2.  Dead code elimination
      3.  Heuristics for optimizing call sites
      4.  Constant folding
  13. Dynamic - java programs can carry extensive runtime information
   
- Java SE, Java EE, Java ME
- Java 8 --- 18 March 2014 ( functional programming, javascript engine, new APIs for date time manipulation, streaming apis, lambda expressions, method references, default methods, optional class)
- Lambda expressions
  - facilitates functional programming, works on the principle of functional interface, interface with only one method to implement
  ```java
  public class Tester {

   public static void main(String[] args) {
      // Interface implementation using anonymous class
      Calculator sum = new Calculator() {
         @Override
         public int operate(int a, int b) {
            return a + b;
         }
      };
      int result = sum.operate(2,3);
      System.out.println(result);	   

      // Interface implementation using lambda expression
      Calculator sum1 = (a,b) -> a + b;
      result = sum1.operate(2,3);
      System.out.println(result);
   }  

   interface Calculator {
      int operate(int a, int b);
   }
    }
  ```
- Method references
  - classname::method
  - instancename::method
  - classname::new -- invokes constructor
    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Tester {
    public static void main(String args[]) {
        List<Integer> numbers = Arrays.asList(1,2,4,9,8,7,3);
        System.out.println("Sorted using static method reference");
        // Use static method compare
        numbers = numbers.stream().sorted(Integer::compare).toList();
        System.out.println(numbers);

        numbers = Arrays.asList(1,2,4,9,8,7,3);
        System.out.println("Sorted using instance method reference" );
        // Use instance method compareTo
        numbers = numbers.stream().sorted(Integer::compareTo).toList();

        System.out.println(numbers);		
    }
    }
    ```

- Default Methods 
  - before java 8, interfaces can only have abstract methods; with java 8 lambda expressions were introduced
    ```java
        interface vehicle {
        // default method must have an implementation
        default void message() {
            System.out.println("I am a vehicle!");
        }
        }

        // implementing class need not to implement the default method
        // of an interface.
        public class Tester implements vehicle {
        public static void main(String args[]) {
            Tester tester = new Tester();
            // implementing class can access the default method as its own method
            tester.message(); 
        }
        }
    ```

- Stream API 
  - new abstract layer; process data in a declarative way
  - `<<collection-instance>>.stream().<<non-terminal-operation()>>.<<non-terminal-operation()>>.<<terminal-operation()>>` - generic syntax
  
    ```java
    import java.util.Arrays;
    import java.util.List;

    public class Tester {
    public static void main(String args[]) {
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");

        // get stream from list using stream() method
        // then apply filter
        // lastly count the result of filter
        long count = strings.stream().filter(string->string.isEmpty()).count();
        System.out.println("Empty Strings: " + count);
    }
    }
    ```

- Optional Class
  - introduced to handle null pointer exceptions (occurs whenever a null object reference is used to get value from it or to invoke its method)
    ```JAVA
    import java.util.Optional;

    public class Tester {
    public static void main(String args[]) {
        // case 1: Optional is having null as underlying value
        Optional<Integer> valueOptional = Optional.ofNullable(null);

        // case 2:  Optional is having not null as underlying value
        Optional<Integer> valueOptional1 = Optional.ofNullable(Integer.valueOf(10));

        // orElse will return -1 being default value
        Integer value = valueOptional.orElse(Integer.valueOf(-1));

        System.out.println(value);

        //  orElse will return the underlying value
        Integer value1 = valueOptional1.orElse(Integer.valueOf(-1));

        System.out.println(value1);
    }
    }    
    ```

- Date Time API
  - thread safe; zone ready; uses immutable constructs and no setter methods
  - `java.time.LocalDate; java.time.LocalDateTime; java.time.Month; java.time.ZonedDateTime`
    ```java
    import java.time.LocalDate;
    import java.time.LocalDateTime;
    import java.time.Month;
    import java.time.ZonedDateTime;

    public class Tester {
    public static void main(String args[]) {
        // Get the current date and time
        LocalDateTime currentTime = LocalDateTime.now();
        System.out.println("Current DateTime: " + currentTime);

        LocalDate date1 = currentTime.toLocalDate();
        System.out.println("date1: " + date1);

        Month month = currentTime.getMonth();
        int day = currentTime.getDayOfMonth();
        int seconds = currentTime.getSecond();

        System.out.println("Month: " + month +", day: " + day +", seconds: " + seconds);

        ZonedDateTime date2 = ZonedDateTime.parse("2007-12-03T10:15:30+05:30[Asia/Karachi]");
        System.out.println("date2: " + date2);
    }
    }
    ```



# Java Brains


<details open>
  <summary> Java - Essentials </summary>

<br>

- Java language
  - sun micro systems -- 1990-95
  - James Gosling -- father of java
  - Patrick Naughton, Chris Warth, Ed Frank, Mike Sheridan 
  - goal 
    - platform independence : write once run anywhere
    - c / c++ : source code -> compiler -> executable (diff machines have diff machine level code and hence diff executables)
    - .class (java) -> compiler -> .class (byte code) -> runtime (executes)
    - JVM is the runtime (doesn't care how .class files are generated, just runs it. You can write code in other languages, compile it to .class and then run on JVM)
- JDK JRE JVM
  - JDK
    - Java SDK 
    - contains compiler and other tools to build java applications
    - not necessary to run java applications
    - comes with runtime
  - JRE
    - required to run java applications
    - runs byte code 
    - language agnostic (all it cares about the .class files)
    - contains standalone JVM
  - JVM
    - runs on a computer any program that is compiled to byte code
    - it acts like an abstract virtual computer
    - has byte code loader, verifier and interpreter
    - can convert byte code to machine specific code
- Java Byte Code : Instruction set meant for execution by JVM (Optimized for JVM)
- advantages
  - write once run anywhere
  - JVM acts as a sandbox protecting the machine (you doing unintentional things)
- JIT : Just in time compiler 
  - selective optimization that the JVM does to convert byte code into direct machine level code that is run on barebones machine
  - say, there's a loop that is run for 39 times. 
- running Java Bytecode
  - Interpret the intermediate bytecode directly
  - Just before executing, compile to native code : JIT
  - Convert intermediate code fully to native code before executing : Ahead of time compilation AOT (Only available from Java 9)
- five goals
  - it must be simple, object-oriented, and familiar
  - it must be robust and secure
  - it must be architecture neutral and portable
  - it must execute with high performance
  - it must be interpreted, threaded and dynamic

<br/>
<br/>

- adoptopenjdk.net
- java --version
- intellij idea
- `javac filename.java`
- `java filename` -- this is the filename of the .class file 
- `java filename.java` -- compiles to .class and runs .class 
- JShell -- REPL Read Evaluate Print Loop

<br/>
<br/>

## variables and types 

- ```java
  public class HelloWorld {
    public static void main( String[] args) {
      System.out.println("Hello Ash!");
    }
  }
  ```
- public -- accessible to everyone
- static -- not associated with an instance
- void -- does not return anything
- main -- method name (starts execution)

<br/>
<br/>

- `int age; int double price = 12; int count, sum;`
- `var age = 39 ; var price = 12.39;
- primitive types -- java doesn't create objects for these, it uses the value as is 
  - Integer
    - byte
    - short 
    - int -- 32 bit signed twos compliment
    - long -- 64 bit signed twos compliment
  - Floating Point
    - float -- 32 bit floating point
    - double -- 64 bit floating point 
  - char -- 'a', 's', 'h'
  - boolean -- true, false
- literals -- way to specify value inline
- `int price = 39_000; ` -- same as saying `int price = 39000`
- `double coeff = 23_456.75_01`
- `double val = 5.012E15` --> 10^15
- `double price = 25D`
- `String name = "ash"` -- Strings are not primitive but "ash" here is a string literal
  
<br/>
<br/>

- java is a strongly typed language
- every variable has a type (static typing) -- compile time
- `<type> varName = <value>` -- ideally, type and value should match exactly, but they can be compatible
- primitive type conversions -- `int a = 39; double b = a;`
  - compatible types
  - destination is larger than the source
- casting : when you know conversion is okay; force conversion from one type to another
  - `double a = 39; int b = (int) a;` // casting with lossy conversion
  - casting object references
  - precision loss
    - `int a = 4 / 2` -- 2
    - `int a = 3 / 2` -- 1 
    - `double a = 3 / 2` -- 1.0 (java evaluates the right hand side first, int / int should result in int)
    - `double a = 3.0 / 2` -- 1.5
- automatic type promotion
  - `double a = 39; int b = 12; var c = a * b;`  -- b is promoted to double and multipled by a; so c is double

<br/>
<br/>

- arrays
- declarations
  - `int slNos[]` -- just declares, doesn't allocate space yet
  - `int slno` -- declares and allocates space
  - `slNos = new int[5]` -- allocates space for 5 ints
  - `int slNos[] = new int[10]; double slNos1[];`
  - `double slNos[] = new int[39]` -- compiler doesn't let this happen : error
- assignment
  - zero based indexing
  - array out of the bounds 
  - `int slNos[] = {1, 2, 3, 9}` -- array initializer
  - `int matrix[][] = new int [3][9]` -- multidimentional array
  - `int matrix[][] = new int[3][]; int matrix[0] = new int[12]; int matrix[1] = new int[39]; ...` -- zagged array; second dimension is not consistent. first dimension cannot be skipped
  - `int matrix [][] = {{1,2 ,3 }, {1, 2, 3}}`

<br/>
<br/>

- Operators 
- arithmetic + - * / %
- assignment =, +=, -=, *=, /=, %=, &=, ^=, |=, <<=, >>=, >>>=
- prefix ++prefix --prefix
- postfix post++ post--
- equality ==, !=
- relational <, >, <=, >=
- logical &&, ||
- ternary operator ? : `boolean bagContents = isRaining ? Umbrella : Hat`
- ![](assets/2024-09-30-22-41-36.png)
- {} -- creates blocks, and variable scoping -- each variable has a life : start -- declaration; end -- scope end
- local variables -- local to scope

<br/>
<br/>

## control flow syntax structures

- if () ... else if () .... else ... 
- switch (a) { case 0: ... break; case 12: ... break; default: ...}
  - a can be byte, short, char, int, String, Enum; case will be literal values
  - whole switch is one block
    - say you declare a variable i in case 1
    - you cannot declare variable i in case 2
- ![](assets/2024-09-30-22-47-17.png)
- ![](assets/2024-09-30-22-50-00.png) 
  - java 14 and above only feature
  - no fall through -- no breaks required
  - switch expression returns value
  - possible to declare same variable in multiple blocks
    - each case is it's own block

<br/>
<br/>

- `for(int i = 0; i<= 12; i++) { ... }` (initialization, condition, action per iteration)
- `for(i=12, j=39; i < 10; i++, j--) { ... }`
- `for(type iterationVariable : collection) { ... }` for-each loop; these loops are capable of type inference. so we can use var instead of type
- `for(int[] subArray : matrix) { for(int element : subArray) { print(elemen) } }`
- classic for -- when index is needed
- for each -- when you just need element; handy with collection APIs
- while (condition) { ... }
- do { ... } while (condition)
- break -- ends the loop
- continue --  ends the iteration of the loop; continues the loop


## classes and objects
  
- Class : models things in real or business world
  - define state and behavior
  - state -- data
  - behavior -- things it does
  - new data type
  - acts as a blueprint; can use this to create instances of classes
  - is a template for objects
- Object : instance of a class; value of that type
  - is a instance of a class
  - instances or class instances

```java
class ClassName{
  // member variables -- state
  // aka instance variables

  type memberVariable; 

  // methods -- behavior

  type methodName(parameters){
    // method body
  }
}


class Car{ // Pascal case for class names

  int seats; // camel case for variables

  double topSpeed;

} // this essentially creates a type called Car

Car myNewCar = new Car();
```

![](assets/2024-09-30-23-25-05.png)

![](assets/2024-09-30-23-27-36.png)

- new keyword allocates memory for the object instance
- memory allocation happens at runtime (when it's needed)
- object variables are reference variables;
- references can be changed by pointing them to other instances

<br/>
<br/>

- this -- reference to the instance the method will be run on
- ![](assets/2024-09-30-23-31-33.png)
- instance variable shadowing by method arguments : giving parameter names same as instance variable names

<br/>
<br/>

- constructors
  - same name as class
  - no return type
  - can use access modifiers
  - can have multiple constructors (constructor overloading)
- ![](assets/2024-09-30-23-35-59.png)
- copy constructor pattern 
  - ![](assets/2024-09-30-23-38-11.png)
  - takes in instance of same class as argument and copies over the instance variables
  - cloning of objects
- Java is always call by value; java doesn't implement call by reference. only implements call by value
- ![](assets/2024-09-30-23-43-26.png)
- ![](assets/2024-09-30-23-43-47.png)
- any value passed as parameter, is copied to method arguments
- if the argument is a reference, the reference is copied. 
- the reference still points to the same instance as the source object reference
</details>

-----
