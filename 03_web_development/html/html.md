- Hyper Text Markup Language - Tim Berners Lee - 1991
- two spaces for indentation
- ignores multiple spaces and line breaks within elements
- parent, child, siblings -- say tag levels 
- attributes : name=value pairs
- class and id values must always be lowercase. multiple word names are separated by dashes - 
- better to have headings in article and section tags


- Attributes:
  1. class -- used for labelling elements. element can be assigned multiple class values in the form of space-separated lists. same class can be assigned to multiple elements
        `<p class="first-value second-value third-value">Hello, World</p>`
    1. id -- used for labelling elements. should have only one value and be unique in entire page
        `<a href="#medellin">Link to Medellín</a>; <h2 class="city" id="medellin">Medellín 🇨🇴</h2>`
    2. href 
    3. src
    4. type
    5. alt
    6. text-decoration
    7. color
    8. width
    9.  height
    10. background-color
    11. margin
    12. text-align
    13. border
    14. display
    15. action
    16. method 


- Tags: Caps -- self closing tags
    0. `<!DOCTYPE html>` -- esslential for all html files. tells browser that file is written in HTML5
    1. `<body>`-- only one in html file
    2. `h1, h2, h3, h4, h5, h6` -- headings -- only one h1 in html file
    3. `p` -- paragraph
    4. `BR` -- line break
    5. `b` -- bold (just bold statistically, no importance); `i` -- italicize; `u` -- underline; `s` -- strikethrough
    6. `strong` -- convey importance while bolding text
    7. `ul` -- unordered list; `ol` -- ordered list (default numbers); `li` -- list item
        - `type="a"` -- lowercase letters
        - `type="i"` -- roman numbers
        - `type="A"` -- uppercase letters
        - `type="I"` -- uppercase roman 

    8. `a` -- anchor element -- used for adding hyperlinks -- `href` - hyperlink reference
        - `<a href="https://archive.org/web">Internet Archive</a>`
        - `<a href="mailto:frankie@gmail.com">📧</a>`
        - `<a href="tel:640-500-CODE">☎️</a>`
        - `<a href="sms:320-250-HTML">💬</a> target="_blank"` -- opens in a new tab
    9. IMG -- images 
        `<img src="https://i.redd.it/5unn16axx1v81.jpg"> alt="Alternative text for the image"`
    10. `marquee` -- scrolling text
    11. `head` -- info for browser, not visible on page
    12. `title` -- goes in `<head>` and assigns text to tab in our browser
    13. `<!-- Everything in here is a comment -->` -- not rendered on the browser
    14. `div` -- defines section. generic container with no particular meaning; groups content
    15. style -- attribute -- stylize elements 
        ```html
        <p>
            Roses are <span style="color:red; text-decoration:underline;">red</span>.<br />
            Violets are <span style="color:blue; text-decoration:underline;">blue</span>.
        </p>

        <style> -- say went inside head tag
            span {  text-decoration: u; } -- applies to all span tags
            #red-word { color: red; } -- applies to all matching ids
            .blue-word { color: blue; } -- applies to all matching classes
            .ranger-div { width: 50%; height: 100px; background-color: red; }
        </style>
        ```
    16. form , INPUT
        - `action` -- where the data should go 
        - `method` -- how the data should be processed

        ```html
        <form>
            <input type="text">
            <input type="submit" value="Hey">
            <input type="email">
            <input type="password">
            <input type="password" minlength="4" maxlength="10">
            <input type="text" required>
            <input type="number" step="2" min="1" max="39">
            <input type="checkbox">
            <input type="radio">
            <input type="radio" name="option"> -- name attribute groups together radio buttons of same name together
            <textarea id="data-entry" rows="7" cols="42"  placeholder="Enter some data here!"></textarea> -- default rows 2, cols default 20 
            <label for="title">Book Title: </label><input type="text" id="title"> -- to associate <label> elements to form inputs, its for attribute must match id of given <input> element
            <label>Book Title: <input type="text"></label> -- associations are implicit in here
        </form>
        ```
    17. `HR` -- horizontal line
    18. `<header>` 
    19. `<nav>` -- navigation links in header go here.  child of `<header>`
    20. `<main>` -- main topics or ideas on the page go here -- only one main element per page
    21. `<footer>` -- information that is important but not suitable for header
    22. `<section>` -- group pieces of related content together
    23. `<article>` -- singular pieces of content; can nest article inside article
    24. `<figure>` -- graphic, image, or diagram 
    25. `<figcaption>` -- used to describe what is in `<figure>` ; can describe multiple pieces of content within figure