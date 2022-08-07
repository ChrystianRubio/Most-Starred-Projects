import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# api call

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
doing = requests.get(url)

results = doing.json()

repo_dicts = results['items']


names, stars = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


#visualization

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

