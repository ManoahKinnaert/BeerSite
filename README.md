# BeerSite
Een eenvoudige website gemaakt om een OC (onderzoekscompetentie) over bierbrouwen te showcasen.

Ollama dient op je computer / server te staan.

# Instructies
1) Maak een virtual environment.
`python -m venv venv`
2) Activeer de virtual environment.
`source venv/bin/activate (Voor Unix / Linux)`
`Op windows heb je pech :) (Niet waar zoek het online op)`
3) Installeer benodigdheden.
`pip install -r requirements.txt`
4) Start de ollama server
`OLLAMA_HOST=127.0.0.1:jouw_poort ollama serve`
bv. `OLLAMA_HOST=127.0.0.1:5051 ollama serve`
5) Start de flask server
`DEBUG=true OLLAMA_HOST=127.0.0.1:ollama_poort python beer_site`
bv. `DEBUG=true OLLAMA_HOST=127.0.0.1:5051 python beer_site`
6) Geniet van de app
