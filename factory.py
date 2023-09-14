import logging 
import yaml
from os import environ as env 
from jinja2 import Template
from github import Github
from github import Auth 
from github.GithubException import *

# token = open('../access_token.secret').read()
token = env.get('GH_TOKEN')
auth = Auth.Token(token)
gh = Github(auth=auth)
org = gh.get_organization('SHR-jPLF')
module_repos = [r for r in org.get_repos() if r.name.endswith('-module')]

stages = []
for m in module_repos:
    name = m.name 
    
    try:
        meta_str = m.get_contents('.module-info.yml').decoded_content
        meta = yaml.safe_load(meta_str)
    except GithubException:
        meta = {}
        logging.warning(f"{name} has no metadata file")
    
    stages_file = meta.get('stages','stages.groovy')
    name = meta.get('name', name)
    stages_str = m.get_contents(stages_file).decoded_content.decode()
    stages_str = stages_str.replace('Exec',f'{name} Exec')
    stages += [stages_str]
template = """
{%- raw -%}
pipeline {
    agent none
    stages {
{%- endraw -%}
    {%- for s in stages %}
        {{ s | indent(8, first=False) }}
    {% endfor -%}
{%- raw -%}
    }
}
{% endraw %}
"""
rendered = Template(template).render(stages=stages)
print(rendered)
with open('resolved.groovy', 'w') as f:
    f.write(rendered)