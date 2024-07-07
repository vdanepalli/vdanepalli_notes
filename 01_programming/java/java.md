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

