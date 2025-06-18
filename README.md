# QCOM Actions

Actions information and common workflows for Qualcomm repositories.

## Actions

### List of available actions

| Action     | Description      | POC |
| ------------- | ------------- |------------- |
| repolinter| GitHub action for checking the repository for consistency and adherence to coding standards| @mynameistechno |
| semgrep| GitHub action for running Semgrep static analysis tool| @njjetha |
| [qualcomm/commit-emails-check-action](https://github.com/qualcomm/commit-emails-check-action) | GitHub action for checking email addresses in PR/Push commits | @quic-nasserg |
| [qualcomm/copyright-license-checker-action](https://github.com/qualcomm/copyright-license-checker-action) | GitHub action for copyright and license issues in PR/Push commits | @targoy-qti |


## Workflows

**multi-checker** This workflow is a reusable workflow to run a series of preflight checks on your code. The checks include:

* **[Repolinter](https://github.com/qualcomm/qcom-actions)**: Checks the repository for consistency and adherence to coding standards.
* **[Semgrep](https://github.com/qualcomm/qcom-actions)**: Runs a static analysis tool to detect potential security vulnerabilities and coding errors.
* **[Copyright-License-Detector](https://github.com/qualcomm/copyright-license-checker-action)**: Checks for proper copyright and licensing information in the code.
* **[PR-Check-Emails](https://github.com/qualcomm/commit-emails-check-action)**: Verifies that the commit emails are properly formatted.

### Examples
In order to call multi-checker workflow please add below file to your repository's under`.github/workflows` directory.
```
name: preflight-checkers 
on:
  pull_request_target:
    branches: [ "main" ]
  push:
    branches: [ "main" ]
  workflow_dispatch:

permissions:
 contents: read
 security-events: write

jobs:
  checker:
    uses: qualcomm-linux/qli-actions/.github/workflows/multi-checker.yml@main
    with:
        repolinter: true # default: true
        semgrep: true # default: true
        copyright-license-detector: true # default: true
        pr-check-emails: true # default: true

    secrets:
      SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
```
OR 

Alternative way to enable in your repo via Action tab workflow templates. Follow below steps
1. Click on Actions
2. If you have existing actions in the repo, click "New workflow", else skip to next step
3. Scroll to `By Qualcomm Technologies, Inc.` section and click `Configure` under `Qualcomm Preflight Checker Workflow`
4. Click "Commit changes...", select "Commit directly to the main branch" (or feel free to create a new branch and start a PR), ensure your Qualcomm email is selected under "Commit Email", and then click "Sign off and commit changes"
5. This will create a GitHub Action config file in your repo under the path `.github/workflows/preflight-checker-workflow.yml`
6. Adjust it as needed, e.g. the preflight-checker action is configured to run on Push and Pull Requests into the main/master branch, but you may want to further adjust when it runs.

If you want to disable semgrep, you can set `semgrep: false` in the `with` section of the workflow. Default value is `true` for all checkers.

## Rulesets

Rulesets can be used to require workflows to pass prior to merge. Some workflows are required for all repos and managed at an organization level. Individual repositories can also require workflows and checks to pass prior to merge.

TBD more info on how to use and required org-level workflows

## Contributing to qcom-actions

### Branches

**main**: Primary development branch. Contributors should develop submissions based on this branch, and submit pull requests to this branch.

### Getting in Contact

* [Report an Issue on GitHub](../../issues)

## License

**qli-actions** is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
