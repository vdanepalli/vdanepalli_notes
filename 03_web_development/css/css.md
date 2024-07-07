## Theory

- Every rule begins with a selector - determine which html element gets styled, followed by { } and inside are declarations - property:value pairs;
  - Type Selector; something like, div, p, h1, h2 ... etc
  - Class and ID Selector; something like .class_name or #id_name
  - Targetting; something like div.class_name or div#id_name
    ```css
    ul, ol {}
    div {}
    .class_name {} 
    #id_name {}
    ul > li {} -- select only child elements of ul 
    ```

- each line ends with a semicolon;
- in head tag inside html `<link href="styles.css" rel="stylesheet">`
- coloring : 
  - you can use color: rgb(255, 255, 255) or #ff0000 or red;
- `color`: rgb(255, 255, 255), #ff0000 or red;
- `height`: 512px; -- can also use points(pt) or centimetres(cm)
- `width`: 539px;
- Absolute units may cause problems like content overflowing
- Relative units - often expressed in percentage; width : 50%
  - `em` -- measurements associated with the font of either the parent element when applying font-size or the element itself when setting the width
  - `rem` -- measurements associated with the font size of the root html element -- 16pt by default
- `font-family`: Serif, Sans-serif, Monospace, Cursive, Fantasy -- browser can fall back into other fonts if need be if multiple fonts are provided
- `font-weight`: lighter, bolder or 400 to 700. anything > 700 is bolder and anything < 400 is lighter


## Properties




Current: Codedex: 09-spellcheck