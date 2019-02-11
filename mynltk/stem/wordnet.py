# Natural Language Toolkit: WordNet stemmer interface
#
# Copyright (C) 2001-2019 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
from __future__ import unicode_literals

from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet
from nltk.compat import python_2_unicode_compatible


@python_2_unicode_compatible
class WordNetLemmatizer(object):
    """
    WordNet Lemmatizer

    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.

        >>> from nltk.stem import WordNetLemmatizer
        >>> wnl = WordNetLemmatizer()
        >>> print(wnl.lemmatize('dogs'))
        dog
        >>> print(wnl.lemmatize('churches'))
        church
        >>> print(wnl.lemmatize('aardwolves'))
        aardwolf
        >>> print(wnl.lemmatize('abaci'))
        abacus
        >>> print(wnl.lemmatize('hardrock'))
        hardrock
    """

    def __init__(self,
                 snap_words=[],
                 local_dictionary={},
                 remember_words=False):

        # Bingham updates:
        #   Added snapwords.
        #   Added local dictionary.
        #   Added word cache.

        self._call_count            = 0
        self._snap_count            = 0
        self._dictionary_count      = 0
        self._memory_count          = 0
        self._full_search           = 0
        self._snap_words            = set(snap_words)
        self._dictionary            = local_dictionary
        self._remember_words        = remember_words
        self._word_memory           = {}

    def lemmatize(self, word, pos=None, multiple_pos_calls=[NOUN],
                  print_results=False):

        # Bingham updates:
        #   Added alternative default (pos=None) processing.
        #   Added print results option.

        if print_results:
            dash           = '-' * 50
            hdr_template   = '{:<20s}{:>10s}{:>10s}{:>8s}'
            data_template  = '{:<20s}{:>10d}{:>10d}{:>8.2f}'
            total_template = '{:<20s}{:>20d}'
            print(dash)
            print(hdr_template.format('Type','Number','Hits','%'))
            print(dash)
            print(data_template.format('snapwords',
                len(self._snap_words),
                self._snap_count,
                100 * round(self._snap_count / self._call_count, 3)))
            print(data_template.format('local dictionary',
                len(self._dictionary),
                self._dictionary_count,
                100 * round(self._dictionary_count / self._call_count, 3)))
            print(data_template.format('remembered words',
                len(self._word_memory),
                self._memory_count,
                100 * round(self._memory_count / self._call_count, 3)))
            print()
            print(total_template.format('Total', self._call_count))

            return

        self._call_count += 1

        # Always before calling WordNet to look-up a word,
        # try to find it in a cached area (snapwords, the local dictionary,
        # and the word memory).  All these areas are optional.

        # Look in snapwords.  Snapwords are snapped back (i.e. they are high frequency words for which the word and the lemma are the same.)
        if word in self._snap_words:
            self._snap_count += 1
            return word

        # Build a global key (has no pos attahed).  There might be a global override in the local dictionary.
        key = word + '__'
        if key in self._dictionary:
            self._dictionary_count += 1
            return self._dictionary[key]

        # Initialize call order.  If multiple pos calls have been set, call WordNet in the order provided as an argument until a match is found.  Otherwise set up to call WordNet with the pos of noun.

        wordnet_call_order = []

        if pos == None:
            wordnet_call_order = multiple_pos_calls
        else:
            wordnet_call_order.append(pos)

        for call_pos in wordnet_call_order:

            # Build a key for the dictionary and word_memory.
            key = word + '_' + call_pos

            # Look in dictionary for the specific pos.
            if key in self._dictionary:
                self._dictionary_count += 1
                return self._dictionary[key]

            # Look in the word memory for the specific pos.
            if key in self._word_memory:
                self._memory_count += 1
                return self._word_memory[key]

            # No match has been found in cache.  Call WordNet.
            lemmas = wordnet._morphy(word, call_pos)

            # If WordNet returned a lemma, do not try any other pos.
            if lemmas:
                break

        # Remember this word/pos/lemma if option set.  If WordNet did not find the word, return the word as its own lemma.  If found, return the shortest lemma in the return list.

        if self._remember_words:
            if lemmas:
                self._word_memory[key] = min(lemmas, key=len)
            else:
                self._word_memory[key] = word

        if lemmas:
            return min(lemmas, key=len)
        else:
            return word

    def __repr__(self):
        return '<WordNetLemmatizer>'


# unload wordnet
def teardown_module(module=None):
    from nltk.corpus import wordnet
    wordnet._unload()
