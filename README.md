# Qualcomm Actions and Workflows

Common actions and workflows for Qualcomm repositories.

## Workflows

### qcom-preflight-checks

This is a reusable workflow that runs a series of preflight checks on your proposed contribution. The checks include:

* **[Repolinter](https://github.com/todogroup/repolinter)**: Checks the repository for consistency and adherence to coding standards.
* **[Semgrep](https://github.com/semgrep/semgrep)**: Runs a static analysis tool to detect potential security vulnerabilities and coding errors.
* **[Copyright-License-Detector](https://github.com/qualcomm/copyright-license-checker-action)**: Checks for proper copyright and licensing information in the code.
* **[PR-Check-Emails](https://github.com/qualcomm/commit-emails-check-action)**: Verifies that the commit emails are properly formatted.

Each check can be individually disabled when not applicable to your project, however in general they should not be disabled. Create an [Issue](https://github.com/qualcomm/qcom-actions/issues) if you run into any issues.

#### How To Install

To start using `qcom-preflight-checks` use one of the below options to create the workflow file in your repository:

1. Copy the file [./github/workflows/qcom-preflight-checks.yml](./github/workflows/qcom-preflight-checks.yml) to your repository's `.github/workflows` directory.
1. Repositories created using [qualcomm/qualcomm-repository-template](https://github.com/qualcomm/qualcomm-repository-template), will include the file at `./github/workflows/qcom-preflight-checks.yml`.
1. Create the file via the **Actions** tab in the UI:
    1. Click on Actions
    1. If you have existing actions in the repo, click "New workflow", else skip to next step
    1. Scroll to `By Qualcomm Technologies, Inc.` section and click `Configure` under `Qualcomm Preflight Checker Workflow`
    1. Click "Commit changes...", select "Commit directly to the main branch" (or feel free to create a new branch and start a PR), ensure your Qualcomm email is selected under "Commit Email", and then click "Sign off and commit changes"
    1. This will create a GitHub Action config file in your repo under the path `.github/workflows/qcom-preflight-checks.yml`
    1. Adjust it as needed, e.g. the qcom-preflight-checks workflow is configured to run on Push and Pull Requests into the default branch (typically main), but you may want to further adjust when it runs.

#### How to Configure

If you need to disable individual checks, open `./github/workflows/qcom-preflight-checks.yml` in your repository and set the check to `false`. E.g. if you want to disable `semgrep`, you can set `semgrep: false` in the `with` section of the workflow. Default value is `true` for all checkers.

## Actions

| Action     | Description      | POC |
| ------------- | ------------- |------------- |
| repolinter| GitHub action for checking the repository for consistency and adherence to coding standards| @mynameistechno |
| semgrep | GitHub action for running Semgrep static analysis tool| @njjetha and @igibek |
| [qualcomm/commit-emails-check-action](https://github.com/qualcomm/commit-emails-check-action) | GitHub action for checking email addresses in PR/Push commits | @quic-nasserg |
| [qualcomm/copyright-license-checker-action](https://github.com/qualcomm/copyright-license-checker-action) | GitHub action for copyright and license issues in PR/Push commits | @targoy-qti |

## Versioning Workflows and Actions

After updating your workflow or action, ensure you tag it following [SemVer](https://semver.org/):

```
Given a version number MAJOR.MINOR.PATCH, increment the:

MAJOR version when you make incompatible API changes
MINOR version when you add functionality in a backward compatible manner
PATCH version when you make backward compatible bug fixes
```

Use GitHub's "Create a new release" in the Releases section. Click the "Generate release notes" to pre-populate a list of merged PRs in the diff, updating as needed.

## GitHub Rulesets

Rulesets can be used to require workflows to pass prior to merge. Some workflows are required for all repos and managed at an organization level. Individual repositories can also require workflows and checks to pass prior to merge. See [About Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) for more information.

## Contributing to qcom-actions

### Branches

**main**: Primary development branch. Contributors should develop submissions based on this branch, and submit pull requests to this branch.

### Getting in Contact

* [Report an Issue on GitHub](../../issues)

## License

**qcom-actions** is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
