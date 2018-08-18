import wikipedia

# briefing
print wikipedia.summary('Pythonidae')
#
print wikipedia.search('C++')

taipei = wikipedia.page('Taipei')
print taipei.title, taipei.url, taipei.content[:50]
print taipei.links[0]

wikipedia.set_lang('zh')
print wikipedia.summary('Taipei',sentences=5)