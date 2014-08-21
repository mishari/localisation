localisation
============

Repository for collaborative localisation of Taxonomy and UI Strings

Translating ODM's Taxonomy

ODM's Taxonomy has been structured in a file with JSON format, initially for the English language (taxonomy/taxonomy_en.json).

In order to Translate ODM's Taxonomy to the other languages, following steps has to be followed:

- Cloning this repository to the Translators machine. For doing that in an easy way (without using command line), the Github desktop client or other Git client can be downloaded and installed on Windows, OSX and Linux.

https://windows.github.com/
https://mac.github.com/

- After the repository is cloned, translators will have access to the different json files, which can be edited with any Text editor. The translation process consist on translating the values found along the file:

"name" :  "Agricultural production"  ->  "name" :  "TRANSLATION_HERE" 

- The structure and indexing of the file should not be modified in order for the JSON files to maintain the same Tree structure. Which can be validated and visualised with several free web tools, such as:

http://jsonviewer.stack.hu/
