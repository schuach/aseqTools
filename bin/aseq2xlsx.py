import aseqTools.aseqTools as at
import xlsxwriter
import easygui as g
import os

infile = g.fileopenbox(msg="Bitte Quelldatei wählen", title="Quelldatei")
outdir = g.diropenbox(msg="Bitte Zielverzeichnis wählen", title="Zielverzeichnis")

# das Zielverzeichnis leeren
# for file in os.listdir(outdir):
#     os.remove(os.path.join(outdir, file))

for record in at.readFile(infile):
    record = at.Record(record)

    # compose the filename
    acnr = record.getField("009000")["subfields"][0][1]
    title = record.getField("245000")["subfields"][0][1].replace(" ", "_").replace("<", "").replace(">", "").replace("\"", "").replace("/", "")
    if len(title) > 30:
        fname = title[:30] + f"({acnr})"
    else:
        fname = title + f"({acnr})"

    workbook = xlsxwriter.Workbook(f"{outdir}/{fname}.xlsx")

    # create a worksheet and set the layout
    worksheet = workbook.add_worksheet()
    worksheet.set_paper(9) # set paper to A4
    worksheet.set_column(0, 2, 4)
    worksheet.set_column(3, 3, 50)

    row = 1
    tag_format = workbook.add_format({ 'valign': "top",
                                       'bold': True,
                                       'underline': True,
                                       'font_name': "Courier New",
                                       'font_color': "blue"})
    ind_format = workbook.add_format({ 'valign': "top",
                                       'bold': True,
                                       'underline': True,
                                       'font_name': "Courier New",
                                       'font_color': "blue"})

    subfield_format = workbook.add_format({ 'valign': "top",
                                    'bold': True,
                                    'font_name': "Courier New",
                                    'font_color': "red"})

    header_format = workbook.add_format({'bold': True,
                                        'font_name': "Courier New"})

    content_format = workbook.add_format({'valign': "top",
                                          'font_name': "Courier New",})

    # aseq = at.readFile("./tests/testinput_single_record.seq")
    fields = record.getFields()

    # make header
    worksheet.write(0, 0, "Tag", header_format)
    worksheet.write(0, 1, "Ind.", header_format)
    worksheet.write(0, 2, "SF", header_format)
    worksheet.write(0, 3, "Inhalt", header_format)

    for field in fields:
        if field["tag"] == "CAT":
            continue
        merge_range = len(field["subfields"]) - 1
        if field["tag"] in ["LDR", "006", "007", "008"]:
            worksheet.write(row, 3, "0....5....10...15...20...25...30...35...40", content_format)
            row += 1
        if field["subfields"][0][0]  == "fixed":
            worksheet.write(row, 0, field["tag"], tag_format)
            worksheet.write(row, 3, field["subfields"][0][1], content_format)
            row += 1
        else:
            if merge_range > 0:
                worksheet.merge_range(row, 0, row + merge_range, 0, field["tag"], tag_format)
                worksheet.merge_range(row, 1, row + merge_range, 1, field["ind"], ind_format)
            else:
                worksheet.write(row, 0, field["tag"], tag_format)
                worksheet.write(row, 1, field["ind"], ind_format)
            for subfield in field["subfields"]:
                worksheet.write(row, 2, subfield[0], subfield_format)
                worksheet.write(row, 3, subfield[1], content_format)
                row += 1
    print(f"Schreibe {fname}")
    workbook.close()

print("\nVerarbeitung abgeschlossen.")
input("Drücken Sie ENTER um dieses Fenster zu schließen.")
