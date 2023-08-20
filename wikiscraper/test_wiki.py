#┌----------------------------------------------┐#
#| Wikiscraper								    |#
#| Developed by Alexandre MEYER                 |#
#| License CC BY 4.0                            |#
#| https://github.com/Alexandre333/wikiscraper  |#
#| 2021 - 2023                                  |#
#| Unit test file : python -m pytest			|#
#└----------------------------------------------┘#

import wikiscraper as ws

# Wiki language page
ws.lang("fr")

# https://fr.wikipedia.org/wiki/Paris
result = ws.searchBySlug("Paris")

error_message = "Unable to find the requested query: please check the spelling of the slug"

### Sidebar ###
def test_getSideInfo():
	assert result.getSideInfo("Gentilé") != [error_message]

### Abstract ###
def test_getAbstract():
	errors = []

	# Get all paragraphs of abstract
	if not result.getAbstract() != [error_message]:
		errors.append("Error to get all paragraphs of abstract")
	
	# Get the second paragraph of abstract
	if not result.getAbstract()[1] != [error_message]:
		errors.append("Error to get the second paragraph of abstract")
	
	# Get the x paragraphs, starting from the beginning
	if not result.getAbstract(2) != [error_message]:
		errors.append("Error to get the x paragraphs")

	# Results
	assert not errors, "errors occured:\n{}".format("\n".join(errors))

### Images ###
def test_getImage():
	assert result.getImage() != []

### Sections ###
def test_getContentsTable():
	errors = []

	# Only first headlines
	if not result.getContentsTable() != []:
		errors.append("Error to get first level headlines")
	
	# All headelines (first and second levels)
	if not result.getContentsTable(subcontents=True) != []:
		errors.append("Error to get all headelines (first and second levels)")
	
	# Get paragraphs from a specific section thanks to the parents' header title
	if not result.getSection('Politique et administration', 'Statut et organisation administrative', 'Historique')[0]:
		errors.append("Error to get paragraphs from a specific section thanks to the parents' header title")

	# Results
	assert not errors, "errors occured:\n{}".format("\n".join(errors))