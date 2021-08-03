![CDL 2021 Cohort Project](../figures/CDL_logo.jpg)
# Quantum Cohort Project Business Application

## Introduction

<table align="center">
    <tr>
        <td><img src="./1.jpg" width="400"></td>
        <td><img src="./2.jpg" width="400"></td>
     </tr>
 </table>
 
Quantum Natural Language Processing (QNLP) enables canonical implementation of natural language on quantum hardware. Canonical refers to compositional language structure, including grammar, that matches the way quantum systems compose. The Categorical Distributional Compositional (DisCoCat) model for natural language makes canonical embedding possible. For instance a perfect match represents the grammatical structure of pregroups and the compositional quantum structure of bipartite entanglement. Teleportation-alike behaviours are the basis for DisCoCat. DisCoCat employees quantum-theoretic features such as vector spaces, inner-products, projector spectra for representing meanings of adjectives, verbs and relative pronouns, density matrices for representing linguistic ambiguity and lexical entailment, and entanglement for representing correlated concepts. DisCoCat-QNLP is referred to as ‘quantum-native’. Quantum implementation of DisCoCat leads to exponential reduction of space resources as compared to implementations on classical hardware, reflects the nativeness of density matrices, and gives quantum advantage of quantum algorithms typical NLP tasks such as classification [1]. 

A direct correspondence between the meanings of words and quantum states and grammatical structures and quantum measurements have been established as seen in the figure below:

<p align="center"><img src="./3.png"width=500/></p>

The network described above can’t be interpreted directly by IBM’s machine. It needs quantum circuit like this:

<p align="center"><img src="./4.png"width=500/></p>

NLP handled by quantum computers was first proposed in 2016. At the time there weren’t any sufficiently capable quantum computers able to implement the NLP tasks proposed. Encoding word meanings on a quantum computer using quantum random access memory (QRAM) is a distant possibility, despite theoretical progress and experimental proposals.
In this project we demonstrate that QNLP can be implemented on NISQ devices, and will work extremely well as these devices scale in terms of size and performance. We used the ZX-language for drawing quantum circuits developed by BC and CQC’s Ross Duncan⁷ - part of the same network language of quantum theory that works very well together with QNLP.

Our solution provides a way forward in the absence of QRAM. Quantum machine learning algorithms do not directly encode the meanings of words. We use quantum circuits instead of classical neural networks in which quantum states and processes learn their meanings/patterns in data directly from text. Neural network architectures are the state-of-the-art in classical NLP. Majority of methods do not take advantage of grammatical structures. We show that our approach to QNLP naturally accommodates both grammar and meaning. We can do several tasks:

* We could vary the hardware - ion traps or optics instead of superconducting qubits. By implementing our program via CQC’s hardware-agnostic t|ket>, this development can take place fairly easily. In our project we did not use actual QC hardware but a ??? simulator.
* We could vary the computational model, for example, MBQC (one-way or measurement-based quantum computer) instead of circuits, by exploiting the relationship between the ZX-language and MBQC.
* In addition to a single sentences we could process larger text.
* We could work on other tasks besides question-answering, such as language generation, summarization, etc. 
* When hardware becomes more powerful we can simply scale up the size of the meaning spaces and complexity of the tasks - which is our overall objective [2]. 

## Real World Applications for QNLP
**1. Text Classification:** Texts are a form of unstructured data with rich information. Since texts are unstructured, analyzing, sorting and classifying them can be very hard and time-consuming and sometimes even tedious work for humans, prone with errors. Text Classifiers categorize and organize in a scalable and more accurate way pretty much any form of text [3]. 

**2. Machine Translation:** helps us achieve multilingualism. In the early ’50s, IBM presented a machine translation system that had only 250 words and translated 49 carefully selected Russian sentences in the field of chemistry into English. Over the recent years with the resources to implement Neural networks, machine translation has significantly improved in its quality such that translating between languages is as simple as pressing a button on the available smartphones or tablets. Google Translate supports more than 100 languages and can even translate language images from up to 37 languages [3].
The Machine Translation Market was valued at USD 153.8 million in 2020, and it is expected to reach USD 230.67 million by 2026, registering a CAGR of 7.1%, during the period of 2021-2026 [4].

**3. Sentiment Analysis:** analyzing people’s sentiment towards a product is very important. Be it a brand-new movie or a cutting-edge tech that’s recently launched, the response of the intended audience is what makes or breaks them [3]. 

**4. Chatbots:** almost every other website nowadays is being supported by a bot that is designed to make our experience better and simpler. Chatbots are the bots designed for a specific use of interaction with humans or other fellow machines using the techniques of AI. Chatbots are designed keeping in mind human interaction. The use of Chatbots goes way back to 1966 when the first chatterbot named “ELIZA” was designed at MIT. Eliza could keep the conversation flowing with the human it interacted with. This led to the development of chatbots that could have a positive influence on people suffering from psychological issues [3].
The global chatbot market is USD 3.6billion in 2020 expected to reach 10.4 by 2025 [5].

**5. Virtual Assistants:** They accept user’s voice commands and perform the task entrusted with them  (alam setting, grocery list making). They are designed to interact with humans in a very human way; most of their responses would feel like the responses you would receive from a friend or colleague. In addition to NLP, virtual assistants also focus on Natural Language Understanding so as to keep up with the ever-growing slang, sentiments, and intent behind the user’s input [3].
The global intelligent virtual assistant market size was valued at USD 5.82 billion in 2020. It is expected to expand at a compound annual growth rate (CAGR) of 28.5% from 2021 to 2028). In terms of market size, North America dominated the market for intelligent virtual assistants with a revenue share of 43.94% in 2020 [6].

**6. Autocomplete in Search Engines:** search engines tend to guess what you are typing and automatically complete your sentences. For example, On typing “quantum” in Google, we get quantum computing, quantum physics, and quantum mechanics.  All these suggestions are provided using autocomplete that uses Natural Language Processing to guess what we want to ask. Search engines use their enormous data sets to analyze what their customers are probably typing when they enter particular words and suggest the most common possibilities [7].
 
**7. Grammar Checkers:** correct grammar, check spellings, suggest better synonyms and improve the overall readability of content. They utilize NLP to provide the best possible piece of writing. The NLP algorithm is trained on millions of sentences to understand the correct format. That is why it can suggest the correct verb tense, a better synonym, or a clearer sentence structure than what you have written. Some of the most popular grammar checkers that use NLP include Grammarly, WhiteSmoke, ProWritingAid, etc. [7].

**8. Email Classification and Filtering:** emails are automatically divided into 3 sections namely, Primary, Social, and Promotions. Email services use NLP to identify the contents of each Email with text classification so that it can be put in the correct section. In more advanced cases, some companies also use specialty anti-virus software with NLP to scan the Emails and see if there are any patterns and phrases that may indicate a phishing attempt on the employees [7].

## Siri, I’m lonely’

<table align="center">
    <tr>
        <td><img src="https://github.com/alice4space/CohortProject_2021/blob/4c8472cf2a35620f5c5ee0bc93d09206b01de9bd/Week4_NLP/imgs/alexa.jpg" width="400"></td>
        <td><img src="./alexa.jpg" width="400"></td>
     </tr>
 </table>
 
**The problem:** Siri, I’m lonely’: an increasing number of people are directing such affective statements, good and bad, to their digital helpmeets. According to Amazon, half of the conversations with the company’s smart-home device Alexa are of non-utilitarian nature – groans about life, jokes, existential questions. “People talk to Siri about all kinds of things, including when they’re having a stressful day or have something serious on their mind. They turn to Siri in emergencies or when they want guidance on living a healthier life.”[8]

“Emotion is what gives humans motivation and drives us to act,” explains Dr. Hoey, whose research on ACT@Home is supported by the American Alzheimer’s Association. The disease brings problems with memory and reasoning for people, as well as personality swings and even shifts in power dynamics. He says it’s important to interpret how a virtual assistant’s prompts would “fit the person’s world model” and adapt accordingly [9]. 

It seems, there is a need to make virtual assistants human-like by bringing emotional abilities to them. 

**The solution:** we make virtual assistants truly emotional with our QNLP hybrid algorithms as more accurate text, text to speech and voice to text sentiment analysis capabilities can be provided than with classical machine learning.  

**The current state:** The AI models used by the Azure Text Analytics API for instance are provided and trained by Microsoft and ready to use. Sentiment Analysis is staged on the entire offered text, instead of words in it, and it produces a more refined result when evaluating smaller pieces of text. Ideally, text size must be under 5,120 characters and returned document labels are positive, negative, neutral and mixed [10].

Generative Pre-trained Transformer 3 (GPT-3) is an autoregressive language model that uses deep learning to produce human-like text. It is the third-generation language prediction model in the GPT-n series created by OpenAI. GPT-3's full version has a capacity of 175 billion machine learning parameters. GPT-3 is part of a trend in natural language processing (NLP) systems of pre-trained language representations. Before the release of GPT-3, the largest language model was Microsoft's Turing NLG with a capacity of 17 billion parameters.

The quality of the text generated by GPT-3 is so high that it is difficult to distinguish from that written by a human, which has both benefits and risks. Microsoft announced on September 22, 2020 that it had licensed "exclusive" use of GPT-3; others can still use the public API to receive output, but only Microsoft has access to GPT-3’s underlying code. It has the ability to do tasks such as Question-Answering, Summarization, Semantic Search, Chatbot, Writing poetry, or an essay. So far GPT-3 has been applied in:

* certain Microsoft products to translate conventional language into formal computer code.
* AI Writer, which allows people to correspond with historical figures via email.
* a retro-themed chatbot project named "Project December", which is accessible online and allows users to converse with several AIs using GPT-3 technology.
by The Guardian to write an article about AI being harmless to human beings. It was fed some ideas and produced eight different essays, which were ultimately merged into one article.
* in AI Dungeon, which generates text-based adventure games [11].
Sentiment classification is available via OpenAI’s GPT-3 API and in true GPT-3 fashion, the implementation code and training data are combined in a very simplistic fashion [12]. 

**Business model:** SaaS.

**Veticals:** consumer electronics, automotive, banking, call centers

**Market:** The global intelligent virtual assistant market size was valued at USD 5.82 billion in 2020. It is expected to expand at a compound annual growth rate (CAGR) of 28.5% from 2021 to 2028). In terms of market size, North America dominated the market for intelligent virtual assistants with a revenue share of 43.94% in 2020 [6].

In terms of market size, the consumer electronics segment dominated the market with a revenue share of 18.5% in 2020. Automotive is emerging as one of the fastest-growing segments in the IVA market. Integration of virtual assistants with the infotainment system contributes towards delivering personalized content as well as improves comfort and convenience. Several companies such as Daimler, BMW, and Hyundai have integrated voice-enabled infotainment systems. In January 2020, Amazon launched Echo Auto, a voice assistant device that contributes toward enhancing the driving experience. Several companies are investing in developing the advanced virtual assistant for the automotive platform to tap into the full potential of the segment.

The text to speech segment dominated the intelligent virtual assistant market with a revenue share of 59.7% in 2020. Automatic speech recognition technology is expected to expand at the fastest CAGR of 30.0% over the forecast period owing to the wide adoption of smart speakers in various sectors. Smart speakers recognize the speech and respond to the speech generated by the consumers in a predefined manner. The rising adoption of mobile computing technology across the world is expected to boost the demand for the automatic speech recognition segment. It makes it easier for customers to interact with smartphones and their applications. Major smart speaker manufacturers are Amazon-Alexa, Google Home, and Bose [6].

**Products/roadmap:** we build expertise first in QNLP hybrid-text sentiment algorithm and then extend our products to QNLP - speech to text and - text to speech hybrid algorithms.

**Competitor and competitors advantage:**
Key players:

<table align="center">
    <tr >
        <td> <b>Company name</b> </td>
        <td> <b>Headquarter</b> </td>
        <td> <b>Profit in USD</b></td>
    </tr>
    <tr>
        <td>Amazon.com, Inc.</td>
        <td>USA</td>
        <td>$386 billion 2020</td>
    </tr>
    <tr>
        <td>Apple Inc.</td>
        <td>USA</td>        
        <td>$260 billion 2019</td>
    </tr>
    <tr>
        <td>Google Inc.</td>
        <td>USA</td>        
        <td>$146.9 billion 2020</td>
     </tr>    
    </tr>
    <tr>
        <td>Microsoft Corporation</td>
        <td>USA</td>        
        <td> $143 billion 2020</td>
     </tr>          
</table>

 **The market:** dominated by large tech companies with vast R&D capacity and highly skilled workforce. Apple has started building emotional abilities in Siri [8].

**Value proposition:** comes from quantum enhanced NLP. As we have shown, quantum implementation of DisCoCat leads to exponential reduction of space resources as compared to implementations on classical hardware, reflects the nativeness of density matrices, and gives quantum advantage of quantum algorithms typical NLP tasks such as classification. 
Advantage: Our strength lies in our quantum enhanced NLP algorithms and highly skilled team with machine learning expertise  with more than 10 years of combined experience.

**Customers:**
Auto: Tesla (2019 $25 billion)
Consumer electronics: Apple (revenue $260 billion 2019), Samsung ($222 billion 2018), Microsoft ($143 billion (2020))

## Conclusion: 

## References
[1] [Coecke, B. et al. Quantum Natural Language Processing](http://www.cs.ox.ac.uk/people/bob.coecke/QNLP-ACT.pdf)

[2] [Quantum Natural Language Processing Medium](https://medium.com/cambridge-quantum-computing/quantum-natural-language-processing-748d6f27b31d). Accessed July 30, 2021.

[3] [Applications of NLP | 5 Vital Applications of Natural Processing Language](https://www.educba.com/applications-of-nlp/). Accessed July 30, 2021.

[4 [Machine Translation Market](https://www.mordorintelligence.com/industry-reports/machine-translation-market). Accessed July 30, 2021.

[5] [Global Chatbot Market](https://www.marketdataforecast.com/market-reports/chatbot-market). Accessed July 30, 2021.

[6] [Intelligent Virtual Assistant Market](https://www.grandviewresearch.com/industry-analysis/intelligent-virtual-assistant-industry#:~:text=The%20global%20intelligent%20virtual%20assistant%20market%20size%20was,a%20CAGR%20of%2034.0%25%20over%20the%20forecast%20period.). Accessed July 30, 2021.

[7] [Top 7 Applications of NLP](https://www.geeksforgeeks.org/top-7-applications-of-natural-language-processing/). Accessed July 30, 2021.

[8] [Can emotion-regulating tech translate across cultures? | Aeon Essays](https://aeon.co/essays/can-emotion-regulating-tech-translate-across-cultures). Accessed July 30, 2021.

[9] [AGE-WELL | An emotionally supportive virtual assistant](https://agewell-nce.ca/archives/7546). Accessed July 30, 2021.

[10] [Perform sentiment analysis and opinion mining with Text Analytics REST API - Azure Cognitive Services](https://docs.microsoft.com/en-us/azure/cognitive-services/Text-Analytics/how-tos/text-analytics-how-to-sentiment-analysis?tabs=version-3-1). Accessed July 30, 2021.

[11] [GPT-3 - Wikipedia](https://en.wikipedia.org/wiki/GPT-3). Accessed August 3, 2021. 

[12] [Using GPT-3 To Measure Sentiment. And How To Add User Sentiment](https://cobusgreyling.medium.com/using-gpt-3-to-measure-sentiment-9b234db37731). Accessed August 3, 2021. 
 
