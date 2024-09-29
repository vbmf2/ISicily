# ISicily: Sketch Engine Corpus

The corpus comprises the early imperial funerary and honorific inscriptions from Catania, Termini, and Syracuse (time range 1 BC to AD 401) drawn from the [ISicily database](http://sicily.classics.ox.ac.uk/inscriptions/) on 09 May 2024. The corpus selection file provides information. 

Files were tokenized by means of `PyEpiDoc` and lemmatised and part-of-speech (POS) tagged by means of the `ancient_greek-proiel-ud-2.12-230717` and `latin-priel-ud-2.12-230717` models by means of `toConllu.py`. Manual correction was applied to the tokens, lemmata, and POS tags. Morphosyntactic information was not corrected and is thus not correct in the files. 

Files were subsequently turned into the Sketch Engine compatible vertical format by means of `toVert.py`. 

Files were separated into a Latin and a Greek corpus based on the information in the ISicily database. When multiple languages were listed, the first one was used to move the file into the Latin or the Greek corpora respectively. The `cat`ed `.vert` files for immediate implementation into Sketch Engine are `ROUND3GR_CORPUS.vert` and `ROUND3LA_CORPUS.vert`.

Sketch Engine: [https://app.sketchengine.eu](https://app.sketchengine.eu)

Modified corpus configuration file (use Expert mode to implement): [https://github.com/MatthewIreland/xml_lemmatiser_tagger/blob/main/files/configFile.txt](https://github.com/MatthewIreland/xml_lemmatiser_tagger/blob/main/files/configFile.txt )

In Sketch Engine: select language ‘Ancient Greek’ for the Greek and the Latin corpora as there are bilingual inscriptions and the ‘Latin’ setting cannot deal with Greek script. 

The Latin lemmata are generally those of classical Latin, the Greek lemmata those of classical Attic-Ionic. While this is anachronistic given the date of the corpus, it allows for lemma searches more easily and with cross-reference to standard dictionaries. The following additional standardisation was applied during manual correction: 

**LATIN = NOUN**
* Ianuarius
* Februarius
* Martius
* Aprilis
* Maius
* Iunius
* Iulius / Quintilis
* Augustus / Sectilis
* September
* October
* November
* December

**Other calender-related items: = NOUN**
* Idus / eidus, plural, feminine, nom/acc εἰδοί
* Kalendae, feminine, plural
* nona, ae f. 

**Attic Ionic standardisation**
* σύμβιος
* ἄμεμπτος (also for ADV)
* πᾶς
* ὑπατία
* χάριν as ADP if with genitive!
* [https://insaph.kcl.ac.uk/insaph/iaph2007/iAph110001.html](https://insaph.kcl.ac.uk/insaph/iaph2007/iAph110001.html) παροδεῖτα ‘passerby’
* οὐ ADV
* χριστιανός ideally instead of eta
* ave / have -> aveo
* a / e for the relevant prepositions 
* adjust inpensa to impensa AND aidilis to aedilis
* in frons -> complex PP but annotated as separate items
* mille

**numerals (currently signs as ADV and words as NUM)**

When the lemma and/or part-of-speech were unclear due to fragmentary preservation of the text, the labels `NOLEMMA` and `NOPOS` are set. These were assigned conservatively, i.e. when there was any doubt.


