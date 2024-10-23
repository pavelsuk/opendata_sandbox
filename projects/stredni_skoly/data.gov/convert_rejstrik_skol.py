import xml.etree.ElementTree as ET
import pandas as pd


def parse_element(el, tags:set):

    ret_lines = list()

    if len(list(el)) == 0:
        return None

    local_vals = dict()
    local_lines = list()

    for child in list(el):
        if len(list(child)) == 0:
            if child.tag in tags:
                local_vals[child.tag] = child.text
                print(f'{child.tag} {child.text}')
        else:
            new_lines = parse_element(child, tags)
            new_local_lines = list()
            if new_lines:
                for line in new_lines:
                    if local_lines:
                        for loc_line in local_lines:
                            if set(line.keys()) == set(loc_line.keys()):
                                # print(f'{child} {child.text}')
                                if  line not in new_local_lines:
                                    new_local_lines.append(line)
                                if  loc_line not in new_local_lines:
                                    new_local_lines.append(loc_line)
                            else:
                                new_local_lines.append(loc_line | line)
                    else:
                        new_local_lines.append(line)
            # local_lines = new_local_lines.copy()
                local_lines = new_local_lines

    if local_lines:
        for line in local_lines:
            ret_lines.append(local_vals | line)
    elif local_vals:
        ret_lines.append( local_vals)
    return ret_lines

def main():
    fpath = 'Q:\dev\_projects\github\opendata_sandbox\projects\stredni_skoly\data.gov\\'
    # fname = 'rejstrik_skol_test.xml'
    # fname = 'rejstrik_skol_err.xml'
    fname = 'vrejcelk.xml'
    # xml_data = open('rejstrik_skol_test.xml', 'r', encoding='UTF-8').read()  # Read file vrejcelk.xml
    xml_data = open(fpath + fname, 'r', encoding='UTF-8').read()
    root = ET.XML(xml_data)  # Parse XML

    tags_all = {"RedIzo", "ICO",
            "RedZkracenyNazev", "RedRUAINKod", "RedAdresa1", "RedAdresa2", "RedAdresa3",
                "PravniForma", "DruhZrizovatele", "Okres", "ORP",
            "ZrizICO",
            "IZO",
            "SkolaDruhTyp",
                "IDMista",
                "MistoDruhTyp",
                "MistoRUAINKod",
                "MistoAdresa1",
                "MistoAdresa2",
                "MistoAdresa3"
    }

    tags_mvp = {"RedIzo", "ICO",
                "RedZkracenyNazev", "RedRUAINKod", "RedAdresa1", "RedAdresa2", "RedAdresa3",
                    "PravniForma", "DruhZrizovatele", "Okres", "ORP"
    }

    tags_mid = {"RedIzo", "ICO",
                "RedZkracenyNazev", "RedRUAINKod", "RedAdresa1", "RedAdresa2", "RedAdresa3",
                    "PravniForma", "DruhZrizovatele", "Okres", "ORP",
                "SkolaDruhTyp",
                    "IDMista",
                    "MistoDruhTyp",
                    "MistoRUAINKod",
                    "MistoAdresa1",
                    "MistoAdresa2",
                    "MistoAdresa3"
    }

    tags = tags_all


    # loop_inside = {"SkolyZarizeni"}

    data = []

    for child in root:
        lines = parse_element(child, tags)
        if lines:
            for line in lines:
                data.append(line)


    df = pd.DataFrame(data)
    df.to_csv('rejstrik_out.csv', index_label='ROWID_TMP')

main()
