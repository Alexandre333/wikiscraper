# wikiscraper

Easy scraper that extracts data from Wikipedia articles thanks to its URL slug : title, images, summary, sections paragraphs, sidebar info

Developed by Alexandre MEYER - CC BY 4.0

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg


Installation

```python
$ pip install wikiscraper
```

## Initialization

Import
```python
import wikiscraper as ws
```

Main request
```python
# Set the language page in Wikipedia for the query
# (ISO 639-1 & by default "en" for English)
ws.lang("fr")
```

```python
# Search and get content by the URL slug of the article
# (Exemple : https://fr.wikipedia.org/wiki/Paris)
result = ws.searchBySlug("Paris")
```
## Examples

```python
# Get article's title
result.getTitle()
```

Sidebar
```python
# Get value of the sidebar information label
result.getSideInfo("Gentilé")
```

Summary
```python
# Get all paragraphs of summary
print(result.getSummary())
# Get the second paragraph of summary
print(result.getSummary()[1])
# Optional : Get the x paragraphs, starting from the beginning
print(result.getSummary(2))
```

Images
```python
# Get all illustration images
img = result.getImage()
# Get a specific image thanks to its position in the page
print(img[0]) # Main image
```

Sections
```python
# Get paragraphs from a specific section thanks to the parents' header title
# All optional args : .getSection(h2Title, h3Title, h4Title)
# Exemple : https://fr.wikipedia.org/wiki/Paris#Politique_et_administration
print(result.getSection('Politique et administration', 'Statut et organisation administrative', 'Historique')[0])
```