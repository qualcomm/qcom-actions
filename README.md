# Qualcomm Actions and Workflows

Common actions and workflows for Qualcomm repositories.

## Workflows

### Qualcomm Preflight Checks

`qcom-preflight-checks` calls a [reusable-workflow](https://github.com/qualcomm/qcom-reusable-workflows/blob/main/.github/workflows/qcom-preflight-checks-reusable-workflow.yml) that runs a series of preflight checks on your proposed contribution. The checks include:

| Action/Workflow  | Description  | POC |
| ------------- | ------------- |------------- |
| [todogroup/repolinter](https://github.com/todogroup/repolinter)| GitHub action for checking the repository for consistency and adherence to coding standards| @mynameistechno |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | GitHub action for running Semgrep static analysis tool| @njjetha and @igibek |
| [qualcomm/commit-emails-check-action](https://github.com/qualcomm/commit-emails-check-action) | GitHub action for checking email addresses in PR/Push commits | @quic-nasserg |
| [qualcomm/copyright-license-checker-action](https://github.com/qualcomm/copyright-license-checker-action) | GitHub action for copyright and license issues in PR/Push commits | @targoy-qti |
| [actions/dependency-review-action](https://github.com/actions/dependency-review-action) | Detects vulnerable dependencies and invalid licenses in PRs | @igibek |
| [qualcomm/commit-msg-check-action](https://github.com/qualcomm/commit-msg-check-action) | GitHub action for validating commit message format and content (optional, requires user to opt-in) | @ynancher |

Each check can be individually disabled when not applicable to your project, however in general they should not be disabled. Create an [Issue](https://github.com/qualcomm/qcom-actions/issues) if you run into any issues.

#### How To Install

To start using `qcom-preflight-checks` use one of the below options to create the workflow file in your repository:

1. Copy the file [./github/workflows/qcom-preflight-checks.yml](https://github.com/qualcomm/qcom-actions/blob/main/.github/workflows/qcom-preflight-checks.yml) to your repository's `.github/workflows` directory.
1. Repositories created using [qualcomm/qualcomm-repository-template](https://github.com/qualcomm/qualcomm-repository-template), will include the file at `./github/workflows/qcom-preflight-checks.yml`.
1. Create the file via the **Actions** tab in the UI:
    1. Click on Actions
    1. If you have existing actions in the repo, click "New workflow", else skip to next step
    1. Scroll to `By Qualcomm Technologies, Inc.` section and click `Configure` under `Qualcomm Preflight Checker Workflow`
    1. Click "Commit changes...", select "Commit directly to the main branch" (or feel free to create a new branch and start a PR), ensure your Qualcomm email is selected under "Commit Email", and then click "Sign off and commit changes"
    1. This will create a GitHub Action config file in your repo under the path `.github/workflows/qcom-preflight-checks.yml`
    1. Adjust it as needed, e.g. the qcom-preflight-checks workflow is configured to run on Push and Pull Requests into the default branch (typically main), but you may want to further adjust when it runs.

#### How to Configure

If you need to disable individual checks, open `./github/workflows/qcom-preflight-checks.yml` in your repository and set the check to `false`. E.g. if you want to disable `semgrep`, you can set `enable-semgrep-scan: false` in the `with` section of the workflow. To disable the commit message check, set `enable-commit-msg-check: false`. Default value is `true` for all checkers except for commit message check which defaults to `false`.

## Versioning Workflows and Actions

After updating your workflow or action, ensure you tag it following [SemVer](https://semver.org/):

```
Given a version number MAJOR.MINOR.PATCH, increment the:

MAJOR version when you make incompatible API changes
MINOR version when you add functionality in a backward compatible manner
PATCH version when you make backward compatible bug fixes
```

Use GitHub's "Create a new release" in the Releases section. Click the "Generate release notes" to pre-populate a list of merged PRs in the diff, updating as needed.

### Why you should not use main or a moving branch

Using main (or any branch) to reference an action or a reusable workflow seems convenient, but it introduces three classes of risk:

#### Supply‑chain risk

The upstream maintainer can force‑push unreviewed code or accidentally merge code that adds a malicious step. Your workflow will pick it up automatically the next run.

#### Breaking changes & reproducibility loss

A minor upstream change (inputs/outputs, environment assumptions) can silently change behavior and break builds.

#### Incident blast radius

When many repositories reference main, a single upstream change can fail all pipelines at once.

### Alternatives to using a branch

To ensure callers of workflow files and actions have the latest, below are some alternatives.

#### Dependabot

* Dependabot can automatically open PRs when a new version of a referenced workflow or action is published
* [qualcomm-repository-template](https://github.com/qualcomm/qualcomm-repository-template) already includes the [dependabot config](https://github.com/qualcomm/qualcomm-repository-template/blob/main/.github/dependabots.yaml) required for this to work for GitHub Actions/Workflow files. If you didn't use the template repo when creating your project, you can manually create it.
* Maintainers that want to strictly control dependency upgrades may prefer this approach

#### Floating tags e.g. @v1

* Some projects create a major version tag (e.g., v1) and then move that tag forward as they release new minor or patch versions (v1.1.0, v1.2.3, etc.).
* This allows consumers to get updates without changing their workflow file every time.
* This approach has similar risks to using a branch. However, some maintainers prefer this approach and are OK with the potential reproducibility loss and other issues related to tag mutation
* Some projects leverage workflows to automate moving major version tags forward whenever a minor or patch release is made. E.g. [actions/update-major-version-tag](https://github.com/marketplace/actions/update-major-version-tag) or a [simple gist example](https://gist.github.com/cicirello/ade1d559a89104140557389365154bc1).

## GitHub Rulesets

Rulesets can be used to require workflows to pass prior to merge. Some workflows are required for all repos and managed at an organization level. Individual repositories can also require workflows and checks to pass prior to merge. See [About Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) for more information.

## Contributing to qcom-actions

### Branches

**main**: Primary development branch. Contributors should develop submissions based on this branch, and submit pull requests to this branch.

### Getting in Contact

* [Report an Issue on GitHub](../../issues)

## License

**qcom-actions** is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
