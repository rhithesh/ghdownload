import os
import requests
from github import Github
from github.GithubException import GithubException

def get_repos(token):
    try:
        g = Github(token)
        user = g.get_user()
        repos = []
        for repo in user.get_repos():
            repos.append({
                "name": repo.full_name,
                "private": repo.private,
                "url": repo.html_url,
                "default_branch": repo.default_branch,
                "repo_obj": repo
            })
        return repos
    except GithubException as e:
        raise Exception(f"Failed to fetch repositories: {e.data.get('message', str(e))}")

def download_repo_zip(token, repo_full_name, default_branch, output_dir):
    """
    Downloads the zipball of the specified repository.
    """
    url = f"https://api.github.com/repos/{repo_full_name}/zipball/{default_branch}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        safe_name = repo_full_name.replace("/", "_") + ".zip"
        output_path = os.path.join(output_dir, safe_name)
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return output_path
    else:
        raise Exception(f"Failed to download {repo_full_name}. Status code: {response.status_code}")



def token_valid(token):
        url = "https://api.github.com/user"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }

        response = requests.get(url, headers=headers)
        auth = response.headers.get("X-OAuth-Scopes")
        if "repo" in auth:
            return response.status_code == 200
        else:
            return False