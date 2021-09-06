import easy_wiki as ew

# Set language page in Wikipedia for the query 
ew.lang("fr")

# Search content by the slug of the article
result = ew.searchBySlug("Lyon")

# article's title
#print(result.getTitle())

# first paragraph of summary
#print(result.getSummary()[0])
# optinal : number of paragraphe since the first
#print(result.getSummary(2))

# Get all illustration images
#img = result.getImage()
# position of the image in the page
#print(img[0])

print(result.getSection('Histoire', 'Préhistoire et Antiquité')[0])


"""
ew.lang("en")
result = ew.searchBySlug("Paris")
result.getSummary
result.getSideInfo
"""