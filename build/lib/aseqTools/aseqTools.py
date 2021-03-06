import os

def readFile(file):
    """Takes an aseq file as input and returns a list of strings (each string is one record)"""
    data = open(file, encoding="utf-8").read()
    recs = data.split("LDR")
    out = [recs[i - 1][-10:] + "LDR" + recs[i][:-10].rstrip() for i in range(1, len(recs) - 1)]
    out.append(recs[-2][-10:] + "LDR" + recs[-1].rstrip())
    return out

class Record(object):

    def __init__(self, aseq_rec):
        self.record = {}
        self.id = None
        self.sysnr = aseq_rec[0:9]
        record = self.read(aseq_rec)

    def read(self, aseq_rec):
        """Takes one record in aseq-format, and populates the Record object"""
        record = {}
        counts = {}
        fields = aseq_rec.split("\n")

        for line in fields:
            field = {}
            subfields = []
            tag = line[10:13]

            field["tag"] = tag

            if field["tag"] == "LDR" or field["tag"].startswith("00") == True:
                field["ind"] = None
                field["subfields"] = [("fixed", line[18:].rstrip())]
            else:
                field["ind"] = line[13:15].replace(" ", "#")
                contents = line[20:].rstrip().split("$$")
                for subfield in contents:
                    subfields.append(("$$" + subfield[0], subfield[1:]))
                field["subfields"] = subfields

            if tag in counts.keys():
                counts[tag] += 1
                self.record[tag + str(counts[tag]).zfill(3)] = field
            else:
                counts[tag] = 0
                self.record[tag + str(counts[tag]).zfill(3)] = field

        return record

    def getField(self, tag):
        """returns one field with the tag 'tag'"""
        return self.record[tag]

    def getRecord(self):
        """returns the whole record as dictionary"""
        return self.record

    def getFields(self):
        """returns a sorted list of fields."""
        d = self.record.copy().keys()
        flist = [self.record["LDR000"]]
        for key in sorted(d):
            if key == "LDR000":
                continue
            else:
                flist.append(self.record[key])
        return flist
