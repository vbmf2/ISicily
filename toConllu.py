"""
Usage: python3 toConllu.py

This script takes a single epidoc document, feeds it to UDPipe, and
saves the resulting output in conllu format.

The default output is a file called <document id>.conllu. This is
written to the current working directory. (If running from PyCharm,
Victoria, that's /Users/vbmf2/dev/helper_scripts.

The script continues to output a vert file for SketchEngine, written
to the same location (called <document id>.vert).

If wanting to process a corpus, then the corpus should be loaded instead,
and the script should be modified to instead iterate through the
documents to be processed.
"""


from pyepidoc import EpiDoc, EpiDocCorpus
import requests
import json

# change this to whatever (single epidoc) file you want to process
# Matthew messed up /Users/vbmf2/dev/ISicily-dev-main/tokenization/tokenized_no_ids/ISic ...
doc = EpiDoc('ISicily/inscriptions/ISic000942.xml')
doc.tokenize()

tokens_aggregated = ''
for t in doc.tokens_normalized:
    tokens_aggregated = tokens_aggregated + str(t) + '\n'

# argument to UDPipe's "process" method
udpipe_process_arg = {
    'data': tokens_aggregated,
    'model': 'ancient_greek-proiel-ud-2.12-230717', # ancient_greek-proiel-ud-2.12-230717 latin-proiel-ud-2.12-230717
    'input': 'vertical',
    'tagger': '',
    'parser': '',
}

udpipe_res = requests.post(
    'http://lindat.mff.cuni.cz/services/udpipe/api/process',
    data=udpipe_process_arg
)

json_result = udpipe_res.json()

# print(json_result['result'])
with open(f"{doc.id}.conllu", "w") as text_file:
    text_file.write("%s" % json_result['result'])

###################################
# WRITE TO VERT

conllu_str_lines = str(json_result['result']).splitlines()

with open(f"{doc.id}.vert", "w") as vert_file:
    inSentence = False
    vert_file.write(f"<doc title=\"{doc.id}.xml\" author=\"None\">\n")
    vert_file.write("<p>\n")

    for line in conllu_str_lines:
        if line.startswith("#"):
            # skip comments and header
            continue

        if "." in line:
            # end of sentence
            vert_file.write("</s>\n")
            inSentence = False
            continue

        fields = line.split()

        if len(fields) < 6:
            # malformed line (e.g. empty line at end of doc)
            continue

        token = fields[1]
        lemma = fields[2]
        pos = fields[3]
        morphology = fields[5]

        if not inSentence:
            vert_file.write("<s>\n")
            inSentence = True

        vert_file.write(f"{token}\t{pos}\t{lemma}\t{morphology}\tNO_VERBAL_MORPHOLOGY\n")

    if inSentence:
        vert_file.write("</s>\n")
        inSentence = False

    vert_file.write("</p>\n")
    vert_file.write("</doc>\n")


