"""
Usage: python3 toVert.py
"""

from pathlib import Path

conllu_file_path = "conllu/ISic000637.conllu"

with open(conllu_file_path, 'r') as conllu_file:
    conllu_str_lines = conllu_file.read().splitlines()

    doc_id = Path(conllu_file_path).stem
    lines_skipped = 0
    lines_missing_morph = 0
    total_lines = 0

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

            if len(fields) < 3:
                # malformed line (e.g. empty line at end of doc)
                lines_skipped = lines_skipped + 1
                continue

            token = fields[1]
            lemma = fields[2]
            pos = fields[3]
            if len(fields) >= 6:
                morphology = fields[5]
            else:
                morphology = ""
                lines_missing_morph = lines_missing_morph + 1

            total_lines = total_lines + 1

            if not inSentence:
                vert_file.write("<s>\n")
                inSentence = True

            vert_file.write(f"{token}\t{pos}\t{lemma}\t{morphology}\tNO_VERBAL_MORPHOLOGY\n")

        if inSentence:
            vert_file.write("</s>\n")
            inSentence = False

        vert_file.write("</p>\n")
        vert_file.write("</doc>\n")

print(f"Total lines: {total_lines}")

if lines_missing_morph > 0:
    print(f"WARNING: {lines_missing_morph} are missing morphology")
        
if lines_skipped == 1:
    print("WARNING: skipped 1 line (maybe you had a blank line at the end of the input file?)")
        
if lines_skipped > 1:
    print(f"WARNING: skipped {lines_skipped} lines")
        
