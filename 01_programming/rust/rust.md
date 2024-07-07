# ZTM Rust

- low level system language
- safety in place -- similar to high level languages
- [course resources](https://github.com/jayson-lennon/ztm-rust)


<br/><br/>

## Fundamentals

- why
  - ![](assets/2024-06-10-12-23-20.png)
  - ![](assets/2024-06-10-12-24-18.png)

<br/><br/>


- data types
  - ![](assets/2024-06-10-12-26-24.png)
  - ![](assets/2024-06-10-12-26-45.png)
  - ![](assets/2024-06-10-12-27-25.png)
  - isize and usize change with respect to where the program runs, 32 bit/64 bit system, drones,. ..

<br/><br/>


- variable
  - ![](assets/2024-06-10-12-29-35.png)
  - ![](assets/2024-06-10-12-29-56.png) 

<br/><br/>


- functions
  - ![](assets/2024-06-10-12-34-27.png)
  - ![](assets/2024-06-10-12-35-48.png)
  - ![](assets/2024-06-10-12-39-11.png)
  - ! indicates that we want to use macro instead of a function which expands into code; macros use ! to call or invoke
  - :? indicates that you want to see a debug print. Not to be seen by end user but developer
  - ![](assets/2024-06-10-12-41-51.png)

<br/><br/>


- execution flow
   - ![](assets/2024-06-10-12-43-33.png)
   - ![](assets/2024-06-10-12-44-36.png)
   - ![](assets/2024-06-10-12-49-23.png)

<br/><br/>


- repetitions or loops
   - ![](assets/2024-06-10-12-51-14.png)
   - ![](assets/2024-06-10-12-52-05.png)
   - ![](assets/2024-06-10-12-53-24.png)
   - ![](assets/2024-06-10-13-45-08.png)
   - ![](assets/2024-06-10-13-46-50.png)
   - 

<br/><br/>


- setup
   - rustup -- manage rust installation
      - rust-lang.org 
         - rustup-init.exe
   - vs code
   - msvc c++ build tools
      - msvc and windows 10 sdk
   - ![](assets/2024-06-10-12-56-00.png)
   - test installation
      - `cargo init hello`
      - `cargo run`

<br/><br/>


- comments
   - `// comment` 

<br/><br/>


- numeric types and basic math
   - ![](assets/2024-06-10-13-10-40.png)

<br/><br/>

- match 
  - must be exhaustive -- all options must be accounted for
  - compiler throws error if any of the possibility is missed; pattern 'variant' not covered
  - ![](assets/2024-06-10-13-38-59.png)
  - `=>` say fat arrow
  - ![](assets/2024-06-10-13-39-49.png)
  - ![](assets/2024-06-10-13-40-30.png) 


<br/><br/>

- enums
  - can only be one variant at a time
  - used to create your own types
  - ![](assets/2024-06-10-13-48-05.png)
  - ![](assets/2024-06-10-13-48-39.png)
  - ![](assets/2024-06-10-13-51-30.png)


<br/><br/>

- Struct
  - ![](assets/2024-06-10-13-57-46.png)
  - ![](assets/2024-06-10-14-00-29.png)
  - ![](assets/2024-06-10-14-02-40.png)
  - ```rust
    enum Flavor{
        Coke,
        Pepsi,
        MountainDew,
    }

    struct Drink {
        flavor: Flavor, 
        fluid_oz : f64,
    }

    fn print_drink(drink: Drink){
        match drink.flavor{
            Flavor::Coke => println!("flavor: coke"),
            Flavor::Pepsi => println!("flavor: pepsi"),
            Flavor::MountainDew => println!("flavor: mountaindew"),
        }

        println!("oz: {:?}", drink.fluid_oz);
    }

    main(){
        let coke = Drink{
            flavor: Flavor::Coke, 
            fluid_oz: 6.0,
        };

        print_drink(coke);
    }
    ```

<br/><br/>


- Tuples
  - a way to access each piece of data within the record
  - ![](assets/2024-06-10-14-10-58.png)
  - ![](assets/2024-06-10-14-14-01.png)
  - can contain different data types
  - ![](assets/2024-06-10-14-16-55.png)
  - better use structure if tuple length is more than 2 or 3


<br/><br/>

- expressions
  - ![](assets/2024-06-10-14-20-15.png)
  - ![](assets/2024-06-10-14-21-07.png)
  - ![](assets/2024-06-10-14-21-42.png)
  - ![](assets/2024-06-10-14-22-39.png)
  - ![](assets/2024-06-10-14-23-47.png)
  - ![](assets/2024-06-10-14-26-01.png)

<br/><br/>

- activities
   - ![](assets/2024-06-10-13-06-09.png)
   - if you don't want to see the steps, compiling, finished, running just pass -q flag `cargo run -q --bin a1`
   - ![](assets/2024-06-10-13-12-38.png)
   - ![](assets/2024-06-10-13-36-26.png)
   - ![](assets/2024-06-10-13-56-16.png)


## Rust's Memory Model

- basics
  - Bits: 0 or 1
  - 1 Byte == 8 bits
  - Addresses -- used to locate data. Address is same. Data changes. Normally you will deal with variables 
  - Offsets -- represent the number of bytes away from the original address. Begin at 0. Normally you will deal with indexes
  - ![](assets/2024-06-10-14-31-45.png)
- ownership
  - owner in rust is simply a function
  - ![](assets/2024-06-10-14-33-28.png)
  - ```rust
    enum Light{
        Bright, 
        Dull
    }

    fn display_light(light: Light){
        match light {
            Light::Bright => println!("bright")
            Light::Dull => println!("dull")
        }
    }

    fn display_light(light: &Light){ // storing a borrowed data; accepting a reference
        match light {
            Light::Bright => println!("bright")
            Light::Dull => println!("dull")
        }
    }

    main(){
        let dull = Light::Dull; // owned by main 
        display_light(dull); // ownership moved to display_light function. so gets deleted after function
        display_light(dull); // dull is already deleted by above function and hence error.


        let dull = Light:Dull;
        display_light(&dull); // we are borrowing data. Referencing. So still owned by main
        display_light(&dull);
    }  
    ```
  - ![](assets/2024-06-10-14-46-27.png)



## Data Collection

- impl 
  - implement functionality 
  - ![](assets/2024-06-10-14-51-39.png)
  - ![](assets/2024-06-10-14-52-41.png)
  - ![](assets/2024-06-10-14-53-30.png)
  - Self = StructureName; self = refers to the defined structure. Kind of like instance.
    - ![](assets/2024-06-10-14-56-05.png)
  - ```rust

    enum Color {
        Red, 
        Blue, 
        Green
    }

    impl Color {
        fn print(&self) {
            match self {
                Color::Red => println!("red"),
                Color::Blue => println!("blue"),
                Color::Green => println!("green"),
            }
        }
    }

    struct Dimensions {
        width: f64, 
        height: f64, 
        depth: f64,
    }

    impl Dimensions {
        fn print(&self) {
            println!("width: {:?}", self.width);
            println!("height: {:?}", self.height);
            println!("depth: {:?}", self.depth);
        }
    }

    struct ShippingBox{
        color Color,
        weight: f64, 
        dimensions: Dimensions
    }

    impl ShippingBox {
        fn new(weight: f64, color: Color, dimensions: Dimensions) -> Self {
            Self {
                weight, 
                color, 
                dimensions // since names are same, we don't need to do dimensions: dimensions
            }
        }

        fn print(&self){
            self.color.print();
            self.dimensions.print();
            println!("weight: {:?}", self.weight);
        }
    }


    fn main() {
        let small_dimensions = Dimensions {
            width: 1.0,
            height: 2.0,
            depth: 3.0
        };

        let small_box = ShippingBox::new(5.0, Color::Red, small_dimensions);

        small_box.print();
    }
    ```

<br/><br/>

- vectors
  - stores multiple pieces of same data; used for lists of information
  - add, remove, traverse entities
  - ![](assets/2024-06-10-15-21-48.png)
  - ![](assets/2024-06-10-15-26-12.png)
  - ![](assets/2024-06-10-15-27-36.png)
  - ![](assets/2024-06-10-15-29-58.png)
    - ownership is transferred to the for loop and hence results in error
    - to fix use `for num in &my_numbers { .... }` 


<br/><br/>

- strings 
  - Are automatically borrowed. `.to_owned() | String::from()` to create an owned copy of a string slice.
  - use owned string when storing in struct
  - ![](assets/2024-06-10-15-32-05.png)
  - ![](assets/2024-06-10-15-33-20.png)
  - ![](assets/2024-06-10-15-34-06.png)
  - `let emp_name = "Win"; // this is automatically of type borrowed. `
  - ![](assets/2024-06-10-15-35-14.png)
  - ![](assets/2024-06-10-15-38-14.png)
  - ![](assets/2024-06-10-15-39-16.png)
  - ![](assets/2024-06-10-15-42-07.png)


## Expanding Knowledge

- deriving functionality

<br/><br/>

- type annotations

<br/><br/>

- enums

<br/><br/>

- options

<br/><br/>

- documentation

<br/><br/>

- STL API
  
## Fallible Functions

- result

## HashMap

- HashMap


## Data Management

- closures


<br/><br/>

- map combinator


<br/><br/>

- option combinator


<br/><br/>

- iterators



<br/><br/>

- ranges


<br/><br/>

- if let else

- while let


<br/><br/>

- inline modules


<br/><br/>

- testing


<br/><br/>

- external crates


<br/><br/>

- external modules



## Project : Billing Application



## Shared Functionality


## Lifetimes


## Improving Program Reliability


## Type Conversions


## Parallel Execution


## Shared Ownership


## Standard Libary Tour


## Other Language Features


## Development Experience


## Crate Roundup


## Project : Clip Stash

## Declarative Macros

# 