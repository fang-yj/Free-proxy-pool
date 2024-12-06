# yancy_qubiaoqian1.py

def clean_tag(tag):
    """Remove other tags and retain only text."""
    return tag.get_text(strip=True)

# def parse_table(thead, tbody):
def parse_table(tbody):
    """Parse thead and tbody elements of a table."""
    # if thead:
    #     thead_rows = [[clean_tag(th) for th in row.find_all("tr")] for row in thead.find_all("th")]
    # else:
    #     thead_rows = []

    if tbody:
        tbody_rows = [[clean_tag(td) for td in row.find_all("td")] for row in tbody.find_all("tr")]
    else:
        tbody_rows = []

    return tbody_rows

def ihuan_table(tbody):

    if tbody:
        tbody_rows = [[clean_tag(td) for td in row.find_all("td")] for row in tbody.find_all("tr")]
    else:
        tbody_rows = []

    return tbody_rows