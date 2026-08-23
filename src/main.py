import requests
import os
import re

API = "https://random-d.uk/api/v2/random"

magicTitle = "🦆 Quack"


githubRepo = os.environ['GITHUB_REPOSITORY']
coauth = os.environ['CO_AUTH'] == "true"
counter = os.environ.get('QUACK_COUNTER', 'true') == "true"



DEL_START  ="<!--DUCK-->"
DEL_END    ="<!--/DUCK-->"

COUNT_RE = re.compile(r"<!--QUACKS:(\d+)-->")

def get_duck():
    r = requests.get(API)
    r = r.json()
    if r['url'] == None:
        return None
    return r['url']

def get_quack_count(lines):
    for line in lines:
        m = COUNT_RE.search(line)
        if m:
            return int(m.group(1))
    return 0

if __name__ == "__main__":
    if os.environ['ISSUE_TITLE'] != None and os.environ['ISSUE_OWNER'] != None and os.environ['ISSUE_NUMBER'] != None:
        if os.environ['ISSUE_TITLE'] != magicTitle:
            print(f"I don't understand the issue title{os.environ['ISSUE_TITLE']}")
            exit(0)
    else:
        print("Error: Issue not found")
        exit(1)
       
    url = get_duck()
    n = 0
    readmefile=open('README.md','r',encoding='utf-8')
    lines = readmefile.readlines()
    readmefile.close()
    start =-1
    end = -1
    for line in lines:
        if DEL_START in line:
            start = n
        if DEL_END in line:
            end = n
        n+=1
    if start == -1 or end == -1:
        print("Error: Delimiter not found")
        exit(1)

    partONe = lines[:start+1]
    conttemp = lines[start+1:end]
    partTwo = lines[end:]

    if url == None:
        print("Error: Duck not found")
        exit(1)

    quacks = get_quack_count(conttemp) + 1

    conttemp = [f"### Duck changed by [{os.environ['ISSUE_OWNER']}](https://github.com/{os.environ['ISSUE_OWNER']})\n",
    f"[![Duck]({url})](https://github.com/"+githubRepo+"/issues/new?title=%F0%9F%A6%86%20Quack)\n",
    ]

    if counter:
        conttemp += [f"<!--QUACKS:{quacks}-->\n",
        "\n",
        f"![Quack counter](https://img.shields.io/badge/🦆_Quacks-{quacks}-yellow?style=for-the-badge)\n",
        ]

    result = partONe + conttemp + partTwo

    readmefile=open('README.md','w',encoding='utf-8')
    readmefile.writelines(result)
    readmefile.close()

    os.system('git config --local user.email "github-actions[bot]@users.noreply.github.com"')
    os.system('git config --local user.name "github-actions[bot]"')
    os.system('git add .')
    os.system(f'git commit -m "🦆 Quack by @{os.environ["ISSUE_OWNER"]} #{os.environ["ISSUE_NUMBER"]}"')
    if coauth:
        os.system(f'git commit --amend --no-edit --author="{os.environ["ISSUE_OWNER"]} <{os.environ["ISSUE_OWNER"]}@users.noreply.github.com>"')
    os.system('git push')


