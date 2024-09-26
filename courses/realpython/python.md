




<details open>
    <summary> Sending Emails: Intro and Account Configuration </summary>

<br/>
<br/>

- Create a developer gmail account
- Go to settings > privacy > turn on Less Secure App Access
- SSL Secure Socket Layer; TSL Transport Security Layer -- encrypt connection between machines
- gmail upgrades SSL to TLS
- smtplib -- connect to mail server

- Encrypted connection from beginning
    ```python
    import smtplib, ssl

    smtp_server = 'smtp.gmail.com'
    port = 465

    sender = 'heycoolassgorgeous@gmail.com'
    password = input('would you be kind enough to let me know your password?')  

    receiver = 'youbeautifullittlesoul@gmail.com'
    message = """\
    Subject: Hi there!

    Would you like to have a cup of coffee with me?
    """  # -- if you pass this as messsage, the receiver will be bcc'd. Not a direct maail 


    message2 = """\
    From: {}
    To: {}
    Subject : Hello Gorgeous!

    How would you like me to take you to dinner tonight?
    """.format(sender, receiver) # -- this will be sent as a direct email

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        print("You do remember your password bitch!")

        server.sendmail(sender, receiver, message)
    ```
- Opportunistic encryption with starttls()
  ```python
  import smptplib, ssl

  smtp_server = 'smtp.gmail.com'
  port = 587

  sender = 'iaintgoinganywhereanysoon@gmail.com'
  psasword = input('C\'mon! why do you need mine?')

  context = ssl.create_default_context()

  try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo() # extended helo -- gets more information from server as opposed to regular one
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)

    print('It fucking worked!')

  except Exception as e:
    print(e)
  
  finally:
    server.quit()
  ```


<br/>
<br/>

- Html Formatting in Emails
- MIME -- Multipurpose Internet Mail Extensions

    ```python
    import smtplib, ssl
    from email.mime.text import MIMEText # contains the body
    from email.mime.multipart import MIMEMultipart # envelope containing header information, different MimeText or attachments information

    smtp_server = 'smtp.gmail.com'
    port = 465

    sender = 'heycoolassgorgeous@gmail.com'
    password = input('would you be kind enough to let me know your password?')  
    receiver = 'youbeautifullittlesoul@gmail.com'
    
    message = MIMEMultipart('alternative') # some mail clients do not display html content, this lets them know that their is alternate plain text version
    message['Subject'] = 'Hey ah!'
    message['From'] = 'someone@gmail.com'
    message['To'] = 'mydearhomie@gmail.com'

    text = """\
    Hey darling!

    How you doin?

    www.letsgetlostinspace.com
    """

    html = """
    <html>
        <body>
            <p> Hi bro! </p>
        </body>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    message.attach(part1)
    message.attach(part2) # we are attaching html later because, clients read from last to early. so it will try to read html first, and plain later


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        print("You do remember your password bitch!")

        server.sendmail(sender, receiver, message.as_string())
    ```

<br/>
<br/>

- emails are designed to work with text and attachments are binary
- encode attachments as base64 before sending them over the air

    ```python
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase # this is where attachments go
    from email.mime.text import MIMEText # contains the body
    from email.mime.multipart import MIMEMultipart # envelope containing header information, different MimeText or attachments information

    smtp_server = 'smtp.gmail.com'
    port = 465

    sender = 'heycoolassgorgeous@gmail.com'
    password = input('would you be kind enough to let me know your password?')  
    receiver = 'youbeautifullittlesoul@gmail.com'
    
    message = MIMEMultipart('alternative') # some mail clients do not display html content, this lets them know that their is alternate plain text version
    message['Subject'] = 'Hey ah!'
    message['From'] = 'someone@gmail.com'
    message['To'] = 'mydearhomie@gmail.com'

    text = """\
    Hey darling!

    How you doin?

    www.letsgetlostinspace.com
    """

    html = """
    <html>
        <body>
            <p> Hi bro! </p>
        </body>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    filename = 'mygirl.jpg'

    with open(filename, 'rb') as attachment:
        part_a = MIMEBase('application', 'octet-stream')
        part_a.set_payload(attachment.read())

    encoders.encode_base64(part_a)

    part_a.add_header(
        'Content-Disposition', 
        f'attachment; filename = {filename}',
    )

    message.attach(part1)
    message.attach(part2) # we are attaching html later because, clients read from last to early. so it will try to read html first, and plain later
    message.attach(part_a)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, password)
        print("You do remember your password bitch!")

        server.sendmail(sender, receiver, message.as_string())
    ```

<br/>
<br/>

- Multiple emails from
  
  ```python
  import csv, smtplib, ssl

  message = """\
  From: {sender}
  To: {email}
  Subject: Hey dear!

  Hi {name}, you look fine af. Here is my {number}.
  """

  sender = 'iamyours@gmail.com'
  password = input("Please don't let my intrusive thoughts win")

  context = ssl.create_default_context()

  with smptplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    with open('contacts.csv') as file:
        reader = csv.reader(file)
        next(reader) # skips first line, say header
        for name, email, number in reader:
            server.sendmail(
                sender, 
                email, 
                message.format(
                    sender = sender, 
                    name = name, 
                    email = email, 
                    number = number
                )
            )

  # 'assumeyouremail+somerandombs@gmail.com' -- gmail ignores anything after + during routing. So I assume it's safe to say that it sends to 'assumeyouremail@gmail.com'
  ```


<br/>
<br/>


- yagmail
- pip install yagmail

  ```python
  import yagmail

  receiver = 'someone@gmail.com'
  body = 'Oops, do I still got it'
  filename = 'youwish.jpg'

  yag = yagmail.SMTP('myemail@gmail.com')
  yag.send(
    to=receiver, 
    subject="Don't you brag now!",
    contents=body,
    attachment=filename,
  )
  ```
- find a library that suits your email client.
- yagmail for gmail and others for others

</details>

-----

<br/>
<br/>


<details open>
    <summary> Python Coding Interviews: Tips & Best Practices </summary>

<br/>

- python for loops are collection based iterations; python assigns next item from iterable to the loop variable on every iteration; helps prevent off-by-one-errors 
- range() vs enumerate()
- enumerate() takes an iterable and iterates through that to generate tuples (index, value)
- enumerate(iterable, start=optional_value_indexing_begins_from_here) 
  
  ```python
  for i in range(len(numbers)):
    num = numbers[i]

    if num%3 == 0:
        print("fizz")
    if num%5 == 0:
        print("buzz")
    if num%3 == 0 and num%5 == 0:
        print("fizzbuzz")
  ```

<br/>
<br/>

- list comprehension, map, filter, max, min, any, bool, all
  
  ```python
  def square(x):
    return x*x

  list(map(square, my_list)) # map returns a map object. basically applies square function to each element in my_list

  [square(num) for num in my_list] # list comprehension

  def is_odd(x):
    return x%2 == 1

  list(filter(is_odd, my_list)) # only keeps values that return true when passed as parameter to is_odd

  [num for num in my_list if is_odd(num)]



  grid = []
  for _ in range(nrows):
    curr_row = []
    for _ in range(ncols):
        curr_row.append(0)
    grid.append(curr_row)


  grid = [[0 for _ in range(ncols)] for _ in range(nrows)]


  max(1, 2, 3)
  max(my_list)
  max(my_list, key = lambda x : x*x) # returns value with max square value

  any(my_list) # returns true if any of the values is true else false


  bool(2) # True

  [(lambda x : x*x)(num) for num in my_list] # [True, False, ...]

  any([(lambda x : x*x)(num) for num in my_list]) # checks if any of the list elements is odd

  all([(lambda x : x*x)(num) for num in my_list]) # checks if all of the list elements are odd
  ```

<br/>
<br/>

- print(), breakpoint() -- built-in pdb debugging
- import pdb; pdb.set_trace() for older versions <= 3.7
- `float("inf"), - float("inf")`
  
  ```python
  float("inf")
  -float("inf")

  print("I am %s and I am gonna kick your %s" %(name, somepart))
  print("I am {0} and I am gonna kick your {1}".format(name, somepart))
  print("I am {name} and I am gonna kick your {somepart}".format(name =name, somepart=somepart))
  print(f"I am {name} and I am gonna kick your {ass}")
c
  class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return (
            f"My name is {self.name}"
            f"I am gonna kick your {self.age}"
        )
    
  print(A(name, age)) -- prints output of __repr__
  ```


</details>

-----

<br/>
<br/>


<details open>
  <summary> Explore your dataset with pandas </summary>

<br>


</details>

-----

<br/>
<br/>


<details open>
<summary> Python and REST APIs </summary>

- REST : Architecture style = Representational State Transfer -- defines a pattern of client and server communications over network
- API : Application Programming Interface
</details>

--------

<br/><br/>





