import aseqTools.aseqTools as at
import xlsxwriter

workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet()
row = 0
tag_format = workbook.add_format({ 'valign': "top" })

aseq = at.readFile("./tests/testinput_single_record.seq")
record = at.Record(aseq[0])
fieldlst = record.getFieldList()

