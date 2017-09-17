import pytest
from aseqTools.aseqTools import readFile
from aseqTools.aseqTools import Record

@pytest.fixture
def single_line():
    """Returns a single line (i.e. field) of aseq"""
    return "003257598 24500 L $$aSigmund Freud und die Geheimnisse der Seele$$b[tiefe Einsichten in das Unbewusste]$$cProjektmanagement: Lisa Löschner"

@pytest.fixture
def single_record():
    return open("tests/testinput_single_record.seq").read().rstrip()

def test_Record_single_line(single_line):
    result = Record(single_line)
    assert result.getField("245")["ind"] == "00"
    assert result.getField("245")["subfields"][0] == ("$$a", "Sigmund Freud und die Geheimnisse der Seele")
    assert result.getField("245")["subfields"][1] == ("$$b", "[tiefe Einsichten in das Unbewusste]")
    assert result.getField("245")["subfields"][2] == ("$$c", "Projektmanagement: Lisa Löschner")

def test_Record_full_record(single_record):
    record = Record(single_record)
    assert record.getField("245") == {'tag': '245', 'ind': '00', 'subfields': [('$$a', 'Sigmund Freud und die Geheimnisse der Seele'), ('$$h', 'Elektronische Ressource'), ('$$b', '[tiefe Einsichten in das Unbewusste]'), ('$$c', '[Projektmanagement: Lisa Löschner. Text: Kathie Tietz ... Sigmund-Freud-Gesellschaft: Texte, themat. Selektion, inhaltiches Konzept, wissenschaftl. Recherche: Wilhelm Burian ...]')]}

def test_readFile():
    record = readFile("tests/testinput.seq")
    assert len(record) == 4
    assert record[0][:10] == "003257598 "
    assert record[1][:10] == "004558441 "
    assert record[3][:10] == "009585231 "
    assert record[3][-5:] == "h1259"

# 003257598 24500 L $$aSigmund Freud und die Geheimnisse der Seele$$b[tiefe Einsichten in das Unbewusste]$$cProjektmanagement: Lisa Löschner"
