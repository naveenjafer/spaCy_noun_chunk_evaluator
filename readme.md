#Noun Phrase chunker evaluation tool for spaCy
This evaluation tool uses CoNLL 2000 dataset to evaluate the Noun Phrase chunking capabiilities of spaCy.  

#How does it work?
CoNLL datatset uses BIO format which has been converted to a list of Noun Phrase chunks.  
Similarly, the output of spaCy's "noun_chunks" has also been converted to a list of Noun Phrase chunks.  
A F1 score calculation has been carried out for the same, results are as follows.  

Precision: 92.41  
Recall: 80.84  
F-Score: 86.25  
