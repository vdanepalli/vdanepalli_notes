
- GIGO -- garbage in garbage out
- Neural Networks
- Data Representation for Images, Text, Audio
- Spatial to Temporal data
- Convolutions
- Fully Connected Lyers
- Forward Propagation

<br/><br/>

- EVA
- ERA
- VIT : Visual Transformer      
- RNN : Reccurrent Neural Networks
- LSTM : Long Term Short Term Memory
  - Multiple gates
  - Memory of 25 to 30 words, after that it forgets
- 2017 -- transformer based architectures revoluti onized foundations of Vision AI(relied on convolutions) and NLP(relied on RNN/LSTM)
- Transformers 
  - Encoder
    - Understand the question : data 
    - Takes all the data at the same time
  - Decoder 
    - Answer
    - Works as many times as there are tokens
  - ChatGPT -- decoder only model 
    - Prompt -- Encoder -- context -- Decoder -- Response
  - Increase in accuracy vs model size was not linear until 2017. With transformers, it is actually linearish
  - With transformers, we do not need supervised data, the model predicts the missing. Learns context. Fills the blanks. Something like, I went to ____ to buy a phone. In doing so, it learns the context. GDP of India in 2022 is ____ 
  - Halucination : Say you ask gdp of a imaginative land, and the model answers some billion dollars. 
  - We do not need to annotate data.
  - Another way is to take two sentences from two different wiki pages, club them together, feed to the model and ask it if they are related? "Audi released A8. India is the most populous country."
  - For images, delete some pixels, and ask the model to predict that. It has to be pixel wise correct. Model gets the context. 
  - Multimodal models: say text and image are fed into the model. 
  - "i am at a bank" 5 inputs go in--> Encoder --> you will get outpus 
  - 100 x 100 / (10 x 10 patches ) = 100; 
    - We don't tell the model what it is predicting
    - It has to somehow replicate the results. 
    - This is where the loss function comes in 


<br/><br/>

- A brain is plastic : plasticity -- if a part gets damaged, the other part can pick up meaning same architecture can do multiple things
- Lots of inspiration from medical and neuroscience
- Rodes (light part -- black or white) and Cones (color part) --- 20:1 ration
- JPEG -- lossy; PNG -- lossless
- Newspapers, magazines -- use CMYK channels
- Colors are not important. Say cars come in all colors. Model has to learn the shape of the car
- something complex can be build in many many forms
- Graphics -- has edges. so small that sometimes looks like curves
- Combine edges to form textures and patterns 
- Textures and Patterns to Objects


<br/><br/>

- Edges and Gradients, Textures and Patterns, Parts of Objects, Objects
- Characters, Words, Sentences, Paragraphs, Book
- Air vibration, Phoneme, Sound of word, Sound of full sentence
- Each bucket can be called as "Block of layers" 
- Every layer would have 100s of thousands of channels, where each channel is responsible only for one thing. 
- when we think in terms of channels, we can split whateveritis into its individual components
- 


<br/><br/>


- Reference
  - Attention is all you need
  - YOLO 
  - Patch is all you need
  - Deepmind
    - robotics transformer for real world control at scale
  - Amazon: Context 
  - Mid Journey -- chatGPT for images 
  - 

<br/><br/>

- a picture is worth 1000 words
- How do we break down the problem into the simplest possible stuff, that can be combined in trillions of ways to represent anything that we may want
