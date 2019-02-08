# Capstone Project: Improving Upon NLTK's Lemmatization Process


## Executive Summary
The Natural Language Toolkit (NLTK) is an open source solution for computer processing and analysis of human language.  When I used the toolkit's stemming and lemmatizing programs for a Natural Language Processing (NLP) classification project, I grew very curious about first, the data that was being created, and second, the logic going on under the hood.  My questions led me to wonder about how I could improve the quality of my input data, especially given that the sheer number of features in an NLP project makes it quite challenging to understand what the data looks like.

### Goal
The goal of this project is to improve upon NLTK lemmatization process in these areas:
- Usability
- Functionality
- Performance, particularly as it relates to processing very large datasets

Guiding Principles
- Make software changes only (i.e no changes to the WordNet lexical database files).
- Avoid changing current processing as much as possible.
- Provide downward compatibility.

Enhancement Overview
- (Usability)    Added optional capability to provide a local dictionary of domain-specific vocabulary and designated lemmas.  The local dictionary can be used, for whatever reason, to preempt lemmatizer processing for user-specified words.
- (Functionality) Added optional capability to override the default processing when the input does not have part of speech tags to narrow the discrepancy between output from default and tagged processing.  Note that this enhancement has a negative impact on performance.
- (Functionality) Modified existing code to correct a couple of bugs.
- (Performance)  Added optional capability to provide high-frequency words that need no lemmatization.
- (Performance)  Added optional capability to cache previously lemmatized words and bypass redundant lemmatization.

## Data
The primary data for my work has been the source code.  For testing purposes, I am currently planning to use the IMDB classification dataset.

## Metrics (still haven't quite nailed this down)
For performance:   Time
For functionality: Accuracy between output with and without tagging
For usability:     Researching usability metrics now.

## Findings
Working on that.

The
What risks/limitations/assumptions affect these findings?

## Project Milestones
- Research.  The project began with research into NLP.  Will cite sources.
- Development environment build.  It took a weekend for me to push through this challenge and figure out how to set up an environment where I could isolate my changes.
- Final selection of enhancements.  After conversations with my local intructor I dropped the spelling enhancement I had been pondering.  Spelling assistance is probably better handled during tokenization rather than lemmatization.  There is still one important usability enhancement waiting in the wings.  If I get time this weekend, I will see how far I can get.
- Learning how to use the python debugger, timeit, and memit (which I will not be using because it does not track memory usage during function calls.)


## Repository Structure
**Folders**


## NLTK
NLTK is an open source solution for computer processing and analysis of human language.  Development on NLTK began at the University of Pennsylvania in 2001, and over time, the product has grown to include software that can be used across an impressive variety of Natural Language Processing (NLP) tasks like parsing, tagging, tokenizing, stemming, lemmatizing, classifying, and semantic reasoning. The toolkit provides interfaces to several dozen important corpora and lexical data bases and also boasts a large and active user community.  The toolkit is updated multiple times per year; contributors are located all over the world.

## WordNet
Put info about wordnet here.

## Resources:

- Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

- https://www.nltk.org/

George A. Miller (1995). WordNet: A Lexical Database for English.
Communications of the ACM Vol. 38, No. 11: 39-41.

Christiane Fellbaum (1998, ed.) WordNet: An Electronic Lexical Database. Cambridge, MA: MIT Press.

A few more to add to this list.
Plus thank yous to Dave Yerrington, Matt Brems, and Sam Stack for guidance.
