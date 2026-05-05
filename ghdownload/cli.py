import os
import sys
import questionary
from rich.console import Console
from .github_api import get_repos, download_repo_zip, token_valid
from pathlib import Path
from InquirerPy import inquirer

console = Console()

config_path= Path.home()/".ghdownloadertoken"

def save_token(token):
    config_path.write_text(token)
def load_token():
    if config_path.exists():
        return config_path.read_text().strip()
    return None

def main():
    console.print("[bold blue]Welcome to ghdownload - GitHub Repo Archiver[/bold blue]")
    
    # Prompt for GitHub token

    token = load_token()
    if token:
        verified = token_valid(token)
    else:
        verified = False

    if  not  verified:
        token = questionary.password("Please enter your GitHub Personal Access Token (with 'repo' scope): This tool currently requires a classic GitHub token get it here: https://github.com/settings/tokens").ask()
        verified = token_valid(token)
        if not verified:
            console.print("[bold red]Invalid token. Exiting.[/bold red]")
            sys.exit(1)

        #console.print("Token is valid")
        save_token(token)
    
    if not token:
        console.print("[bold red]Token is required. Exiting.[/bold red]")
        sys.exit(1)

    console.print("[black]Fetching your repositories...[/black]")
    try:
        all_repos = get_repos(token)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
        
    if not all_repos:
        console.print("[bold red]No repositories found or access denied.[/bold red]")
        sys.exit(0)
        
    console.print(f"[green]Successfully fetched {len(all_repos)} repositories.[/green]")
    
    # Filter public/private
    visibility_choice = questionary.select(
        "Which repositories do you want to list?",
        choices=[
            "All (Public and Private)",
            "Public only",
            "Private only"
        ]
    ).ask()
    
    filtered_repos = all_repos
    if visibility_choice == "Public only":
        filtered_repos = [r for r in all_repos if not r["private"]]
    elif visibility_choice == "Private only":
        filtered_repos = [r for r in all_repos if r["private"]]
        
    if not filtered_repos:
        console.print(f"[bold red]No repositories match the '{visibility_choice}' filter.[/bold red]")
        sys.exit(0)

    # Ask how to select
    selection_mode = questionary.select(
        "How would you like to select repositories to download?",
        choices=[
            "Select specific repositories (Searchable)",
            f"Download ALL ({len(filtered_repos)} repos)"
        ]
    ).ask()
    
    selected_repos = []
    if "Download ALL" in selection_mode:
        selected_repos = filtered_repos
    else:
        repo_map = {
            f"{r['name']} ({'Private' if r['private'] else 'Public'})": r
            for r in filtered_repos
        }

        selected_labels = inquirer.fuzzy(
            message="Search and select repositories:",
            choices=list(repo_map.keys()),
            multiselect=True,
        ).execute()

        selected_repos = [repo_map[label] for label in selected_labels]
        
    if not selected_repos:
        console.print("[bold red]No repositories selected for download. Exiting.[/bold red]")
        sys.exit(0)
        
    console.print(f"[bold green]Starting download for {len(selected_repos)} repositories...[/bold green]")
    
    output_dir = Path.cwd() / "ghdownloads"

    output_dir.mkdir(exist_ok=True)           
    success_count = 0

    console.print(f"All repos will be downloaded to {output_dir}")
    
    for r in selected_repos:
        repo_name = r["name"]
        branch = r["default_branch"]
        console.print(f"Downloading [cyan]{repo_name}[/cyan]...")
        try:
            download_repo_zip(token, repo_name, branch, output_dir)
            console.print(f"  [green]✓ Success[/green]")
            success_count += 1
        except Exception as e:
            console.print(f"  [bold red]✗ Failed:[/bold red] {e}")
            
    console.print(f"\n[bold black]Download complete! {success_count}/{len(selected_repos)} successfully downloaded to {output_dir}.[/bold black]")

if __name__ == "__main__":
    main()
