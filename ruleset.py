import requests

# === Configuration ===
GITHUB_TOKEN = "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"
ORG = "qualcomm-linux"
REPO = "kernel-topics"

# Define branches and allowed merge users
branches_and_teams = {
    "maintainers.qualcomm-kernel" :["qualcomm-kernel.maint"]
}

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# === Helper to get GitHub user ID ===
def get_team_id(teamname):
    url = f"https://api.github.com/orgs/{ORG}/teams/{teamname}"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("id")
    else:
        print(f"Failed to get user ID for {teamname}")
        return None


# === Step 1: Set classic branch protection ===
def set_classic_protection(branch, bypass_users):
    url = f"https://api.github.com/repos/{ORG}/{REPO}/branches/{branch}/protection"
    payload = {
        "required_status_checks": {
            "strict": True,
            "contexts": []
        },
        "enforce_admins": True,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": True,
            "require_code_owner_reviews": True,
            "required_approving_review_count": 1,
            "bypass_pull_request_allowances": {
                "users": [],
                "teams": bypass_users,
                "apps": []
            }
        },
        "restrictions": None,
        "allow_force_pushes": False,
        "allow_deletions": False,
        "required_linear_history": True
    }

    r = requests.put(url, headers=headers, json=payload)
    if r.status_code in [200, 201]:
        print(f"Classic protection set on '{branch}'")
    else:
        print(f"Classic protection failed on '{branch}': {r.status_code} - {r.text}")


# === Step 2: Create branch ruleset with 'restrict updates' ===
def create_ruleset(branch, bypass_users):
    url = f"https://api.github.com/repos/{ORG}/{REPO}/rulesets"
    bypass_actors = []

    for user in bypass_users:
        uid = get_team_id(user)
        if uid:
            bypass_actors.append({"actor_id": uid, "actor_type": "Team", "bypass_mode": "always"})

    payload = {
        "name": f"{branch}-ruleset",
        "target": "branch",
        "enforcement": "active",
        "conditions": {
            "ref_name": {
                "include": [f"refs/heads/{branch}"],
                "exclude": []
            }
        },
        "rules": [
            {
                "type": "update",
                "parameters": {
                    "update_allows_fetch_and_merge": False,
                }
            },
            {
                "type": "deletion"
            },
            {
                "type": "non_fast_forward"
            }
        ],
        "bypass_actors": bypass_actors
    }

    r = requests.post(url, headers=headers, json=payload)
    if r.status_code in [200, 201]:
        print(f"✅ Ruleset created for '{branch}'")
    else:
        print(f"❌ Ruleset failed for '{branch}': {r.status_code} - {r.text}")


# === Step 3: Set auto-delete on PR merge ===
def set_auto_delete():
    url = f"https://api.github.com/repos/{ORG}/{REPO}"
    payload = {"delete_branch_on_merge": True}
    r = requests.patch(url, headers=headers, json=payload)
    if r.status_code == 200:
        print("Auto-delete enabled.")
    else:
        print(f"Auto-delete failed: {r.status_code} - {r.text}")


def add_team_to_repo(team_slugs):
    for team_slug in team_slugs:
        url = f"https://api.github.com/orgs/{ORG}/teams/{team_slug}/repos/{ORG}/{REPO}"
        data = {
            "permission": "maintain"
        }
        response = requests.put(url, headers=headers, json=data)
        if response.status_code == 204:
            print(f" ✅ Team '{team_slug}' added to the repository.")
        else:
            print(f"❌ Failed to add team '{team_slug}' to the repository: {response.status_code} - {response.text}")



# === Run All ===
for branch, teams in branches_and_teams.items():
    # set_classic_protection(branch, teams)
    # create_ruleset(branch, teams)
    add_team_to_repo(teams)

# set_auto_delete()