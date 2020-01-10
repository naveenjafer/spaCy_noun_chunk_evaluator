# Noun Phrase chunker evaluation tool for spaCy
This evaluation tool uses CoNLL 2000 Shared task of Chunking - https://www.aclweb.org/anthology/W00-0726.pdf and https://www.clips.uantwerpen.be/conll2000/chunking/ to evaluate the Noun Phrase chunking capabiilities of spaCy.  

# How does it work?
CoNLL datatset uses BIO format which has been converted to a list of Noun Phrase chunks.  
Similarly, the output of spaCy's "noun_chunks" has also been converted to a list of Noun Phrase chunks.  
A F1 score calculation has been carried out for the same, results are as follows.  

# Results
Precision: 92.41  
Recall: 80.84  
F-Score: 86.25  

# Extending it?
Any of the modern Noun phrase chunkers can be evaluated with simple modifications to the script.

