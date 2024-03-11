from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from sreality_scraper import scrape_flats
from repository import insert_flats, get_all_flats


app = FastAPI()


@app.get("/scrape-and-store")
def scrape_and_store():
    flats = scrape_flats()
    insert_flats(flats)
    return f"{len(flats)} flats were scrapped from sreality.cz and store to database."


@app.get("/flats")
def get_flats():
    flats = get_all_flats()
    html = """<HTML>
    <HEAD>
        <META charset="UTF-8">
    </HEAD>
    <BODY>
        <TABLE>
            <tr>
              <th>Title</th>
              <th>Image</th>
            </tr>
            {{HTML_FLATS}}
        </TABLE>
    </BODY>
    </HTML>"""

    flats_html = ""
    for flat in flats:
        flats_html += f"""
        <tr>
          <td>{flat.title}</td>
          <td><img src="{flat.img_url}"></td>
        </tr>"""

    html_response = html.replace("{{HTML_FLATS}}", flats_html)
    return HTMLResponse(content=html_response, status_code=200)
