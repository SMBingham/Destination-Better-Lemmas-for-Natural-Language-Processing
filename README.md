# Capstone Project: Improving NLTK's Lemmatization Process


## Executive Summary
The Natural Language Toolkit (NLTK) is a widely used open source solution for computer processing and analysis of human language.  The toolkit includes many useful utilities including an interface to the WordNet lexical reference database.  When I used the toolkit's stemming and lemmatizing programs for a Natural Language Processing (NLP) classification project at General Assembly, I grew very curious about first, the data that was being created, and second, the logic going on under the hood.  My questions led me to wonder about how I could improve the quality of my input data, especially given that the sheer number of features in an NLP project makes it quite challenging to understand what the data looks like.

I decided to improve the NLTK interface to WordNet.  My work on this project led to many interesting insights about electronic dictionaries as well as about language processing in general.  Over the course of  project, I became more deeply interested in NLP, an area in data science that is growing rapidly.  The changes that I made to the toolkit built a foundation that provides greater control over the lemmatization process and, thus, more opportunity to improve data.  The changes will be available for implementation anywhere.

### Goal
The goal of this project was to improve NLTK lemmatization.  Lemmatization is the process by which words are standardized to specific word forms.  For example, the goal of lemmatization of nouns is for them to be singular, not plural.  The goal for verbs is to make them present tense.  Processing of comparatives and superlatives happens for adjectives.  As you might imagine, the complexity of our language leads to some complexity in the software.  WordNet, a very popular reference corpus, is organized more like a theasaus than like a dictionary.  The project will focus there.

There were two main areas for goals:
- Functionality
- Performance, particularly as it relates to processing very large datasets

### Driving questions
- If x% of words in written English make up a large y% of corpora, can we leverage that understanding prior to feature selection and modeling? 
- How can I improve my NLP input data?  
- New words are added to English fairly often these days.  How can we keep our NLP models current?

### Guiding Principles
- Make software changes only (i.e no changes to the WordNet database files).
- Avoid changing current processing as much as possible.
- Provide downward compatibility.

### Overview 
For this project, I made six improvements to the NLTK lemmatization process.  More detail about the work can be found in the Development-Notes file in this repo. 

- Added optional capability to provide high-frequency words that need no lemmatization.
- Added optional capability to provide a local dictionary of domain-specific vocabulary and designated lemmas.  The local dictionary can be used, for whatever reason, to preempt lemmatizer processing for user-specified words.
- Added optional capability to cache previously lemmatized words and bypass redundant lemmatization.
- Added optional capability to override the default processing when the input does not have part of speech tags.  This change narrows the discrepancy between output from default and tagged processing.  Note that this enhancement has a negative impact on performance.
- Added optional ability for users get metrics from the lemmatizer regarding the used of cached memory.
- Forced the program to return documented exceptions for known irregular word forms.  This corrects an issue I discovered during testing and is a maintenance item.


## Data
I used samples from the [Large Movie Review Dataset] (http://ai.stanford.edu/~amaas/data/sentiment/) in my testing.  I established three sample sizes (100, 1000, and 10000) and randomly sampled the movie reviews.  In order to reproduce and/or extend my work, please download the train folder and run the notebooks in this repo with the same random seeds that are documented.


## Metrics
- Elapsed time for the lemmatization process.  This variable was tested using the system time function.
- Model accuracy.  I compared the model scores between the data produced by the production and my development module.


## Findings
The updates to the model were successful.  The performance of the changed WordNet interface was slightly better than that of the production version across all three sample sizes.  The accuracy of the development model tracked closely with the results using the production version of the model.  All the modeling was performed with defaults.  The next steps are to delve into tuning parameters.


## Project Milestones
- Research.  The project began with research into NLP.  Will cite sources.
- Development environment build.  It took a weekend for me to push through this challenge and figure out how to set up an environment where I could isolate my changes.
- Final selection of enhancements.  After conversations with my local intructor I dropped the spelling enhancement I had been pondering.  Spelling assistance is probably better handled during tokenization rather than lemmatization.
- Learning how to use the python debugger, timeit, and memit (which I will not be using because it does not track memory usage during function calls).


## Repository Structure

**Folders**
|__ 01_Data-Collection-and-Preprocessing.ipynb 
|__ 02a_Lemmatization-Prod.ipynb
|__ 02b_Lemmatization-Dev
|__ 03_Modeling.ipynb
|__ 04_Project-Evaluation
|__ data
|__ images
|__ mynltk (my changed versions of nltk programs)
|   |__ corpus reader
|   |   |__ wordnet.py
|   |__ stem
|   |   |__ wordnet.py
|__ presentation.pdf
|__ READ-Development-Notes.md  
|__ README.md
|__ Utility_Compare_Lemmas.ipynb



## NLTK
https://www.nltk.org/
NLTK is an open source solution for computer processing and analysis of human language.  Development on NLTK began at the University of Pennsylvania in 2001, and over time, the product has grown to include software that can be used across an impressive variety of Natural Language Processing (NLP) tasks like parsing, tagging, tokenizing, stemming, lemmatizing, classifying, and semantic reasoning. The toolkit provides interfaces to several dozen important corpora and lexical data bases and also boasts a large and active user community.  The toolkit is updated multiple times per year; contributors are located all over the world.


## WordNet
https://wordnet.princeton.edu/
From the link:
"WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. Synsets are interlinked by means of conceptual-semantic and lexical relations. The resulting network of meaningfully related words and concepts can be navigated with the browser. WordNet is also freely and publicly available for download. WordNet's structure makes it a useful tool for computational linguistics and natural language processing."


## Resources:

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

C. E. Shannon, "A Mathematical Theory of Communication," Bell System Technical Journal, v. 27, pp. 379-423, 623-656, July, October,  1948.

C. E. Shannon, "Prediction and Entropy of Printed English," Bell System Technical Journal, v. 30, pp. 47-51, 1951.

Christiane Fellbaum (1998, ed.) WordNet: An Electronic Lexical Database. Cambridge, MA: MIT Press.

George A. Miller (1995). WordNet: A Lexical Database for English.
Communications of the ACM Vol. 38, No. 11: 39-41.

Jurafsky, Daniel, and James H. Martin. 2009. Speech and Language Processing: An Introduction to Natural Language Processing, Speech Recognition, and Computational Linguistics. 2nd edition. Prentice-Hall.


## Helpful people:
Thank you to Matt Brems, Riley Dallas, Sam Stack, and Dave Yerrington for guidance and encouragement.
