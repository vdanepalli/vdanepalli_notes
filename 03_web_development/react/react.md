## Theory


### Intro 
- 2013 - JS Library - React was introduced to build websites with reusable components
- Javascript flavour -- JSX (JavaScript Syntax Extension); .js or .jsx
- JSX gets transpiled or translated into plain javascript and then read by browser when run
    ```javascript
    // Before being transpiled
    let heading = <h1 id="welcome-heading">Welcome!</h1>;

    // After being transpiled
    let heading = React.createElement("h1", { id: "welcome-heading" }, "Welcome!");
    ```
- Fast and Scalable; Efficient in updating parts of website
- Developed by a small team at facebook
- Hot Reloading -- a feature in React; Allows us to see changes made to code in real-time
- Components -- definde like functions that return JSX content
    ```javascript
    import React from "react";

    export default function Greetings() {
    return (
        <div>
        <h1>Hello, World!</h1>
        <p>Nice to meet you. 😊</p>
        </div>
    ) 
    }
    ```
    - export default -- lets us use it in other files too
    - returned JSX must be wrapped in a single element



<br/>
<br/>



- File Structure
  - public
    - index.html -- HTML with root of React app `<div id = "root">` 
  - App.js - React code written in JSX
  - index.js - where our React app is started from 
    - `const container = document.getElementById("root")` -- this connects our html to react app
  - package.json - node packages (including react)
  - style.css
- npm - node package manager 
- 