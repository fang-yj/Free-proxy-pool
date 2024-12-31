
def clean_tag(tag):

    return tag.get_text(strip=True)
# def parse_table(thead, tbody):
def zhan_daye_table(tbody):

    if tbody:
        tbody_rows = [[clean_tag(td) for td in row.find_all("td")] for row in tbody.find_all("tr")]
    else:
        tbody_rows = []

    return tbody_rows
