"""
Usage: python3 toVert.py
"""

from pathlib import Path

conllu_file_path = "conllu/ISic000637.conllu"

with open(conllu_file_path, 'r') as conllu_file:
    conllu_str_lines = conllu_file.read().splitlines()

    doc_id = Path(conllu_file_path).stem

    with open(f"{doc_id}.vert", "w") as vert_file:
        inSentence = False
        vert_file.write(f"<doc title=\"{doc_id}.xml\" author=\"None\">\n")
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


