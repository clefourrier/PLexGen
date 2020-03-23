# PLexGen
Phonetic lexicon generator and sound change applier - used in `Comparing Statistical and Neural Models for Learning Sound Correspondences`, a LT4HALA 2020 workshop paper (LREC 2020)

# How to 
## Test this repo
Run the main.py file, which will generate a protolanguage and 3 children, stored in the output folder.

## Use this repo for your languages
### sound_changes
Add your sound changes to a new file.

A sound change has the following shape: `origin_phones/new_phones/context`
- Phones: 
  - A phone in lowercase represents itself. V means vowel. C means consonnant. A comma separates two groups of phones. 
  - For example, eC,Vj means "all 'e' followed by a consonnant, all 'j' preceded by a vowel". 
  - The comma means "and" in the origin_phones (`this phone group and this one will be transformed to...`) and "or" in the new_phones (`the transformation can go to this phone group or this one` - the choice between the groups is done by the rule_change_applier).
  
### sound_inventories
To generate your own sound inventory, copy the \_default.json file and add your phones in the correct categories. 

- Phones
  - The mandatory phones will be present in your inventory
  - A random subset of your phones will be drawn from the possible phones catagory 
- Phonotactics 
  - The syllable_number must be the distribution of the possible syllable numbers for your language
    - [1, 1, 2] means that 2/3 of the words have one syllable and 1/3 have 2 syllables
  - Clusters
    - These must contain the possible letter clusters for initial, final, and middle (other) clusters in words.
    -  A phone in lowercase represents itself. V means vowel. C means consonnant. P means plosives. O means obstruent. S sonorant
    - You must provide a list of lists of combinations
    - Here, "initial": [["Vs"], ["ast", "est", "ist"]], the algorithm will randomly pick one list to begin a word, and one item from that list. It means that a word has 1/2 chance of beginning by a vowel followed by "s", 1/6 by "ast", 1/6 by "est" and 1/6 by "ist". 

### run main
If you need more inspiration, go see the provided files called italic.txt in sound_changes and italic.json in sound_inventories. When you are satisfied, edit the main file, so it picks your new configuration files, and run it.


# To use, cite
```
@inproceedings{fourrier20,
  TITLE = {{Comparing Statistical and Neural Models for Learning Sound Correspondences}},
  AUTHOR = {Fourrier, Cl{\'e}mentine and Sagot, Beno{\^i}t},
  BOOKTITLE = {{Twelfth International Conference on Language Resources and Evaluation (LREC 2020), LT4HALA Workshop}},
  ADDRESS = {Marseilles, France},
  YEAR = {2020},
  NOTE = {(to appear)}
}
```
