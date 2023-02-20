from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p class="special">more special text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="no">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(type(soup))
# print(soup.body)
# print(soup.body.div)
# print(soup.find('div'))
# for div in soup.find_all('div'):
#     print(div)
# print(soup.find_all(class_="special"))
# print(soup.find_all(attrs={'data-example': 'yes'}))
# ---------------------------------------------------
# print(soup.select_one('#first'))
# print(soup.select('.special'))
# print(soup.select('div'))
# print(soup.select('[data-example]')) # visiems nurodytiems atributams
# print(soup.select('[data-example="no"]')) # atributams su specifine reiksme
# ---------------------------------------------------
# for element in soup.select('.special'):
    # print(element.name)
    # print(element.get_text())
# for element in soup.select('[data-example]'):
    # print(element.attrs)
    # print(element.get_attribute_list('data-example'))
# ---------------------------------------------------
# attribute = soup.select('#first')[0]['id']
# print(attribute)
# ------------- navigacija tarp HTML elementu -------
# print(soup.body.contents)
# print(soup.select('.special')[0].parent.parent)
# print(soup.select_one('li').next_sibling.next_sibling)
# print(soup.select_one('li').find_next_sibling(class_='special'))
# print(soup.select_one('li').find_next_sibling(name='li'))
# print(soup.find('li').parent.previous_sibling.previous_sibling.h3.get_text())
