# To do a Google search for recipes.

import webbrowser



def search_web(term):
    url = "https://www.google.ca/search?q={}".format("recipe with "+ term)

    webbrowser.open_new_tab(url)
