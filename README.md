# easy-wiki

Easy scraper that extracts data from Wikipedia articles thanks to its URL slug

Developed by Alexandre MEYER - CC BY-NC-SA 2.0

Installation

```python
$ pip install easywiki
```

## Initialization

Import
```python
import easy_wiki as ew
```

Set the language page in Wikipedia for the query
(ISO 639-1 & by default "en" for English)
```python
ew.lang("fr")
```

Basic request
Search and get content by the URL slug of the article
(Exemple : https://fr.wikipedia.org/wiki/Paris)

```python
result = ew.searchBySlug("Paris")
```
## Examples

```python
# Get article's title
result.getTitle()
```

```python
### Sidebar ###
# Get value of the sidebar information label
result.getSideInfo("Gentilé")
```

```python
### Summary ###
# Get all paragraphs of summary
print(result.getSummary())
# Get the second paragraph of summary
print(result.getSummary()[1])
# Optional : Get the x paragraphs, starting from the beginning
print(result.getSummary(2))
```

```python
### Images ###
# Get all illustration images
img = result.getImage()
# Get a specific image thanks to its position in the page
print(img[0]) # Main image
```

```python
### Sections ###
# Get paragraphs from a specific section thanks to the parents' header title
# All optional args : .getSection(h2Title, h3Title, h4Title)
# Exemple : https://fr.wikipedia.org/wiki/Paris#Politique_et_administration
print(result.getSection('Politique et administration', 'Statut et organisation administrative', 'Historique')[0])
```