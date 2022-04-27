ReadMe File for ADFA-LD Feature Extraction
Frank Rossi
4-26-2022


The first step in running this code is the Removing Attacks.py, which located the traces
in the master data which contained attacks. These traces were removed and the clean data
was moved to a folder named Training_Data_Clean

The second step in running this code is Dictionary Creation, which iterates over the clean
training data to produce the word dictionary and the phrase dictionaries of lengths 1-3 in
pickle files.

Finally, in Feature Extraction, all traces in the clean training data and all traces in the
attack data are iterated over using these dictionaries to produce the feature vector for each
trace. This is very time intensive but can be sped up by running multiple versions of this
code in parallel on different portions of the data (This took 1 week running 5 instances in
parallel on a Lenovo Thinkpad with a 6-core i7-9850H @ 2.6 GHz and 32GB RAM).

The attack data and clean data from all these instances were then combined together and input
into the Jupyter Notebook.