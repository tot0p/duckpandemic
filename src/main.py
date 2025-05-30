import requests
import os

API = "https://random-d.uk/api/v2/random"

magicTitle = "🦆 Quack"


githubRepo = os.environ['GITHUB_REPOSITORY']
coauth = os.environ['CO_AUTH'] == "true"



DEL_START  ="<!--DUCK-->"
DEL_END    ="<!--/DUCK-->"

def get_duck():
    r = requests.get(API)
    r = r.json()
    if r['url'] == None:
        return None
    return r['url']

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

    conttemp = [f"### Duck changed by [{os.environ['ISSUE_OWNER']}](https://github.com/{os.environ['ISSUE_OWNER']})\n",
    f"[![Duck]({url})](https://github.com/"+githubRepo+"/issues/new?title=%F0%9F%A6%86%20Quack)\n",
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


