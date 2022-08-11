import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# api call

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
doing = requests.get(url)

results = doing.json()

repo_dicts = results['items']

#visualization

my_style = LS('#333366', base_style=LCS)


chart = pygal.Bar(style=my_style, x_label_rotation=45,show_legend=False,show_y_guides = False)

chart.title = "Python Projects"
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
                {'value': 121906, 'label': 'httpie'},
                {'value': 141109, 'label': 'django'},
                {'value': 136657, 'label': 'flask'},
]



chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
