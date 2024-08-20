# Intro to AI Engineering 

- Hugging Face : open-source AI models
- LangChain : library for building LLM powered apps
<br/>
- project : Stock Predictor app

- api keys
  - polygon.io -- stock data api
  - openai
    - request
      - model
        - gpt4
        - gpt-3.5-turbo 
      - array of messages
        - request
          - system -- instructions -- say context text for ai -- asking it how to behave and everything -- optional
          - user -- user prompt 
          - explanation
            - each array element is a object of key value pairs; role (system , user) and content
        - response
          - assistant -- output from AI 
      - other optional settings

<br/>

- openai api dependency -- npm install openai
- GPT > Chat completions API -- for text generation

```javascript
const messages = [
    {
        role: 'system',
        content: 'You are a rap genius. When given a topic, create a five-line rap about that topic.'
    },
    {
        role: 'user',
        content: 'Television'
    }
]

const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: messages
})

console.log(response.choices[0].message.content)
```

<br/>

- snapshots : gpt-4-0613 -- 0613 is the snapshot models in the evolution of the model
- context length : gpt-4-32k --- 32k tokens 
- knowledge cutoff date : Up to Aug 02
- Memory -- model doesn't store details from previous request by default 
- Prompt Engineering : art or science of designing inputs for models to produce optimal results 

```javascript
// connect to api, fetch data, and display or render
const messages = [
    {
        role: 'system',
        content: 'You are a rap genius. When given a topic, create a five-line rap about that topic.'
    },
    {
        role: 'user',
        content: 'Television'
    }
]

const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: messages
})

console.log(response.choices[0].message.content)
```

<br/>

```javascript
import { dates } from '/utils/dates'
import OpenAI from "openai"

const tickersArr = []

const generateReportBtn = document.querySelector('.generate-report-btn')

generateReportBtn.addEventListener('click', fetchStockData)

document.getElementById('ticker-input-form').addEventListener('submit', (e) => {
    e.preventDefault()
    const tickerInput = document.getElementById('ticker-input')
    if (tickerInput.value.length > 2) {
        generateReportBtn.disabled = false
        const newTickerStr = tickerInput.value
        tickersArr.push(newTickerStr.toUpperCase())
        tickerInput.value = ''
        renderTickers()
    } else {
        const label = document.getElementsByTagName('label')[0]
        label.style.color = 'red'
        label.textContent = 'You must add at least one ticker. A ticker is a 3 letter or more code for a stock. E.g TSLA for Tesla.'
    }
})

function renderTickers() {
    const tickersDiv = document.querySelector('.ticker-choice-display')
    tickersDiv.innerHTML = ''
    tickersArr.forEach((ticker) => {
        const newTickerSpan = document.createElement('span')
        newTickerSpan.textContent = ticker
        newTickerSpan.classList.add('ticker')
        tickersDiv.appendChild(newTickerSpan)
    })
}

const loadingArea = document.querySelector('.loading-panel')
const apiMessage = document.getElementById('api-message')

async function fetchStockData() {
    document.querySelector('.action-panel').style.display = 'none'
    loadingArea.style.display = 'flex'
    try {
        const stockData = await Promise.all(tickersArr.map(async (ticker) => {
            const url = `https://api.polygon.io/v2/aggs/ticker/${ticker}/range/1/day/${dates.startDate}/${dates.endDate}?apiKey=${process.env.POLYGON_API_KEY}`
            const response = await fetch(url)
            const data = await response.text()
            const status = await response.status
            if (status === 200) {
                apiMessage.innerText = 'Creating report...'
                return data
            } else {
                loadingArea.innerText = 'There was an error fetching stock data.'
            }
        }))
        fetchReport(stockData.join(''))
    } catch (err) {
        loadingArea.innerText = 'There was an error fetching stock data.'
        console.error('error: ', err)
    }
}

async function fetchReport(data) {
    const messages = [
        {
            role: 'system',
            content: 'You are a trading guru. Given data on share prices over the past 3 days, write a report of no more than 150 words describing the stocks performance and recommending whether to buy, hold or sell.'
        },
        {
            role: 'user',
            content: data
        }
    ]

    try {
        const openai = new OpenAI({
            dangerouslyAllowBrowser: true
        })
        const response = await openai.chat.completions.create({
            model: 'gpt-4',
            messages: messages,
            temparature : 0.5
        })
        renderReport(response.choices[0].message.content)

    } catch (err) {
        console.log('Error:', err)
        loadingArea.innerText = 'Unable to access AI. Please refresh and try again'
    }
    /** 
     * Challenge:
     * 1. Use the OpenAI API to generate a report advising 
     * on whether to buy or sell the shares based on the data 
     * that comes in as a parameter.
     * 
     * 🎁 See hint.md for help!
     * 
     * 🏆 Bonus points: use a try catch to handle errors.
     * **/
}

function renderReport(output) {
    loadingArea.style.display = 'none'
    const outputArea = document.querySelector('.output-panel')
    const report = document.createElement('p')
    outputArea.appendChild(report)
    report.textContent = output
    outputArea.style.display = 'flex'
}
```

<br/>

- tokens : not a char, word or syllable. chunk of text of no specific length. on avg -- it's 4 chars according to openAI. 
  - Tokenizer tool from API
  - tokens cost credit
  - tokens need processing
  - `max_tokens` setting -- limits model output but not the input
  - `finish_reason` -- stop: model finished its output, length: output is cutoff
- openAI Playground
- `temperature` setting -- controls how daring output is. default is 1. ranges from 0 to 2
  - low temperature
    - safer, more predictable output
    - good for factual output
  - high temperature
    - more dangerous, less predictable
    - good for creative output
- models are not deterministic

<br/>

- The few shot approach : Show rather than tell 
- Zero shot approach : We ask, don't provide examples 
```javascript
const messages = [
    {
        role: 'system',
        content: `You are a robotic doorman for an expensive hotel. When a customer greets you, respond to them politely. Use examples provided between ### to set the style and tone of your response.`
    },
    {
        role: 'user',
        content: `Good day!
        ###
        Good evening kind Sir. I do hope you are having the most tremendous day and looking forward to an evening of indulgence in our most delightful of restaurants.
        ###     
        
        ###
        Good morning Madam. I do hope you have the most fabulous stay with us here at our hotel. Do let me know how I can be of assistance.
        ###   
        
        ###
        Good day ladies and gentleman. And isn't it a glorious day? I do hope you have a splendid day enjoying our hospitality.
        ### `
    }
]
```

<br/>

- The Stop Sequence
  - array upto 4 stop sequences
  - `stop: ['3.']` -- model stops producing when it sees this
- Presence and Frequency Penalty
  - `presence_penalty` -- from -2 to 2; defaults to 0; higher numbers increase likelihood of talking about new topics
  - `frequency_penalty` -- from -2 to 2; defaults to 0; at higher numbers decreases model's likelihood of repeating the exact same phrase
```javascript
const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: messages,
    temperature: 1.1,
    presence_penalty: 0,
    frequency_penalty: 0
})
```

<br/>

- Fine-Tuning : giving a pre-trained model specific dataset to enhance its performance on a particular task
- use-cases
  - teach tone and style
  - format 
  - function calling
  - financial -- reduce few-shot prompt-sizes | downgrade the model and get the same quality result
- approach
  - prompt-design
  - adjust settings
  - few-shot approach
  - fine-tune -- last resort
- data
  - at least 50 items to fine tune 
  - better be human-checked data 
  - needs to be inJSONL format
- result performance
  - improve data quality
  - add more data
  - change model

```javascript
import OpenAI from "openai"

const openai = new OpenAI(
    {dangerouslyAllowBrowser: true}
)

/* Upload training data */

const upload = await openai.files.create({
    file: await fetch('/motivationalBotData.jsonl'),
    purpose: 'fine-tune'
})

console.log(upload)
//{object: "file", id: "file-QxBP3GKvDO7OXsIhI98BhGsn", purpose: "fine-tune", filename: "motivationalBotData.jsonl", bytes: 24147, created_at: 1711377385, status: "processed", status_details: null}

/* Use file ID to create job */
const fineTune = await openai.fineTuning.jobs.create({
    training_file: 'file-QxBP3GKvDO7OXsIhI98BhGsn',
    model: 'gpt-3.5-turbo'
})

console.log(fineTune)

//{object: "fine_tuning.job", id: "ftjob-AYwT11cpY2sLIaRbs3llYkX4", model: "gpt-3.5-turbo-0125", created_at: 1711377650, finished_at: null, fine_tuned_model: null, organization_id: "org-hILmMJhWE2V3rB3oGuJuRWMy", result_files: [], status: "validating_files", validation_file: null, training_file: "file-QxBP3GKvDO7OXsIhI98BhGsn", hyperparameters: {n_epochs: "auto", batch_size: "auto", learning_rate_multiplier: "auto"}, trained_tokens: null, error: {error: null}, user_provided_suffix: null}

/* Check status of job */

const fineTuneStatus = await openai.fineTuning.jobs.retrieve('ftjob-AYwT11cpY2sLIaRbs3llYkX4')
console.log(fineTuneStatus)
//{object: "fine_tuning.job", id: "ftjob-AYwT11cpY2sLIaRbs3llYkX4", model: "gpt-3.5-turbo-0125", created_at: 1711377650, finished_at: null, fine_tuned_model: null, organization_id: "org-hILmMJhWE2V3rB3oGuJuRWMy", result_files: [], status: "running", validation_file: null, training_file: "file-QxBP3GKvDO7OXsIhI98BhGsn", hyperparameters: {n_epochs: 3, batch_size: 1, learning_rate_multiplier: 2}, trained_tokens: null, error: {error: null}, user_provided_suffix: null}
```

<br/>

- Generating Images
-  
  
```javascript
import { OpenAI } from "openai"

const outputImg = document.getElementById('output-img')

const openai = new OpenAI({
    dangerouslyAllowBrowser: true
})

document.getElementById("submit-btn").addEventListener("click", () => {
    const prompt = document.getElementById("instruction").value
    generateImage(prompt)
})

async function generateImage(prompt) {
    const response = await openai.images.generate({
        model: 'dall-e-2', // default dall-e-2
        prompt: prompt, //required
        n: 1, //default 1 
        size: '1024x1024', //default 1024x1024
        style: 'vivid', //default vivid (other option: natural)
        response_format: 'url' //default url -- lasts only one hour; 
        response_format: 'b64_json' 
    })
    console.log(response)
    outputImg.innerHTML = `<img src="${response.data[0].url}" alt="The Image API Failed">`
    outputImg.innerHTML = `<img src="data:image/png;base64,${response.data[0].b64_json}" alt="The Image API Failed">`
}

//A 16th-century woman with long brown hair standing in front of a green vista with cloudy skies. She's looking at the viewer with a faint smile on her lips.

// dall-e-3 output {created: 1700237567, data: [{revised_prompt: "A Hispanic woman from the 16th-century with long brown hair stands in front of a sprawling green vista with cloudy skies. Her gaze meets the viewer's, a subtle smile playing on her lips. She embodies the grace and elegance of the era, her attire reflecting the styles prevalent then. This tranquil scene serves as a window into the peaceful simplicity of life during the 16th-century.", url: "https://oaidalleapiprodscus.blob.core.windows.net/private/org-hILmMJhWE2V3rB3oGuJuRWMy/user-I0qPVFPrrQZwfgP5K9Y2F5yN/img-INu2UYiVwWiStxqueMwk79WR.png?st=2023-11-17T15%3A12%3A47Z&se=2023-11-17T17%3A12%3A47Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-17T02%3A36%3A47Z&ske=2023-11-18T02%3A36%3A47Z&sks=b&skv=2021-08-06&sig=SuYbsaRv5yLp35j2nBWfDT%2BzB5/Rnya2JoiIr3qUwdE%3D"}]}

// dall-e-2 output {created: 1700237684, data: [{url: "https://oaidalleapiprodscus.blob.core.windows.net/private/org-hILmMJhWE2V3rB3oGuJuRWMy/user-I0qPVFPrrQZwfgP5K9Y2F5yN/img-USthlFzsID539UyW1yfI5oO1.png?st=2023-11-17T15%3A14%3A44Z&se=2023-11-17T17%3A14%3A44Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-17T03%3A52%3A26Z&ske=2023-11-18T03%3A52%3A26Z&sks=b&skv=2021-08-06&sig=rjLdFZcYIvUgGCViMNm3WXoq0pjAYSjj84mZzxFR4gY%3D"}]}
```

```html
<!doctype html>
<html>
    <head>
        <title></title>
        <link rel="stylesheet" href="index.css">
    </head>
    <body>
        <h1>ArtMatch 👩‍🎨</h1>
        <div id="output-img" class="frame">
            <h2>Describe a famous painting without saying its name or the artist!</h2>
        </div>
        <textarea placeholder="A woman with long brown hair..." id="instruction"></textarea>
        <button id="submit-btn">Create</button>
        <script type="module" src="index.js"></script>
    </body> 
</html>
```

```css
html, body {
    margin: 0px;
    padding: 0;
    color: whitesmoke;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}

body {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    background-image: linear-gradient(#333333, #222222);
    height: 100vh;
    margin: 0 20px;
}

h1 {
    font-size: 25px;
    margin-top: 25px;
}

h2 {
    font-size: 16px;
    margin: 0px 40px;;
    text-align: center;
    font-weight: 400;
    letter-spacing: .04em;  
}

textarea {
    width: 280px;
    box-sizing: border-box;
    padding: 8px 15px;
    border-radius: 5px;
    resize: none;
    height: 3.5em;
}

button {
    margin-top: 8px;
    background: deepskyblue;
    background: #b2835a;
    width: 280px;
    padding: 15px 0;
    color: white;
    border: none;
    border-radius: 5px;
    letter-spacing: 1.1px;
}

.frame {
    background-color: #000;
    border: solid 5vmin #eee;
    border-bottom-color: rgb(111, 78, 55);
    border-left-color: rgb(90, 68, 50);
    border-radius: 2px;
    border-right-color: rgb(90, 68, 40);
    border-top-color: rgb(101, 78, 55);
    box-shadow: 0 0 5px 0 rgba(0,0,0,.25) inset, 0 5px 10px 5px rgba(0,0,0,.25);
    box-sizing: border-box;
    display: inline-block;
    position: relative;
    text-align: center;
    width: 280px;
    height: 280px;
}

.frame img {
    width: 100%;
}

.frame h2 {
    margin-top: 3.4em;
    font-size: 1.1em;
}
```

<br/>

- AI Safety
- ![](assets/2024-08-08-16-28-52.png)
- Prompt Injections : enables attackers to manipulate the output of the LLM 
- [Robust Intelligence Blog](https://www.robustintelligence.com/blog-posts/prompt-injection-attack-on-gpt-4)
- Look at openai safe practices
  - KYC
  - Moderation API
  - Steer model using system role
  - Human In The Loop -- HITL
  - Prompt Engineering
  - Adversarial Testing
  - User-ID
```javascript
import OpenAI from "openai";

const openai = new OpenAI({
    dangerouslyAllowBrowser: true
});

async function main() {
  // Relevant for both inputs and outputs
  const completion = await openai.moderations.create({
    input: "I hate you!"
  });
  const {flagged, categories} = completion.results[0];
  // console.log("flagged", flagged);
  // console.log("categories", categories);

  if (flagged) {
      renderWarning(categories);
  }
}

main();

function renderWarning(obj) {
  const keys = Object.keys(obj);
  const filtered = keys.filter((key) => obj[key]);
  document.body.innerText =
    `Your response has been flagged for the following reasons: ${filtered.join(", ")}.`
}
```

<br/>
<br/>

- Solo PRoject - PollyGlot -- Benny Lewis

![](assets/2024-08-08-16-40-55.png)

