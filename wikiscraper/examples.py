import wikiscraper as ws

# Set the language page in Wikipedia for the query
# ISO 639-1 & by default "en" for English
ws.lang("fr")

# Search and get content by the URL slug of the article
# Exemple : https://fr.wikipedia.org/wiki/Paris
result = ws.searchBySlug("Paris")

# Get article's title
print(result.getTitle())

# Get article's URL
print(result.getURL())

### Sidebar ###
# Get value of the sidebar information label
print(result.getSideInfo("Gentilé"))

### Abstract ###
# Get all paragraphs of abstract
print(result.getAbstract())
# Get the second paragraph of abstract
print(result.getAbstract()[1])
# Optional : Get the x paragraphs, starting from the beginning
print(result.getAbstract(2))

### Images ###
# Get all illustration images
img = result.getImage()
# Get a specific image thanks to its position in the page
print(img[0]) # Main image

### Sections ###
# Get paragraphs from a specific section thanks to the parents' header title
# All optional args in order : .getSection(h2Title, h3Title, h4Title)
# Exemple : https://fr.wikipedia.org/wiki/Paris#Politique_et_administration
print(result.getSection('Politique et administration', 'Statut et organisation administrative', 'Historique')[0])