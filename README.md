# Home Assignment for Luxonis

The app scrapes 500 properties from [sreality.cz](https://sreality.cz)

## Usage

### How to run
Run `clean_run.sh` for clean run. `Docker` and `docker-compose` is needed.

### Webapp
* `http://localhost:8080/scrape-and-store`
* `http://localhost:8080/flats`


## BeautifulSoap
I use `BeautifulSoup` for parsing `HTML` because I am familiar with it and I didn't read assignment carefully, so I didn't notice that I should use `scrapy` framework which I am unfamiliar with.

### What could be done better
* download 60 properties instead of 20 (probably it requires selenium click)
* parallel of multiple website pages
* use an async framework for DB (but for this assignment, it would be pointless)
* ORM (SQLAlchemy) + Alembic
* guvicorn with uvicorn workers
* proper, not hard-coded, config
* error handling
* structured logging
* tests
* HTML template for viewing properties in static the folder
* more general installation of chromedriver in Dockerfilie

## Typos
Now I would use `property` instead of `flat`
