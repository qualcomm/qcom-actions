# List of workflows and actions
This folder contains workflows that are helpful for maintaining a smooth and secure development process. The workflows should be enabled for open-source projects.

Workflows:
1. `pr-dependency-check.yml` - This workflow will run on every pull request to check if the proposed code changes contain third-party dependencies (third-party library and/or third-party actions) with vulnerabilities. If the proposed changes introduce third-party dependencies that contain vulnerabilities with HIGH or above severity, the workflow execution will fail.
2. `qualcomm-organization-repolinter.yml` - This workflow will on every push and pull request event check if the repository follows the organization's open-source repository standards. For example, the workflow will check if the repository contains CONTRIBUTING file.
3. `stale-issues.yaml` - This workflow will periodically run every 30 days to check for stalled issues and PRs. If the workflow detects any stalled issues and/or PRs, it will automatically leave just a comment to draw attention.
4. `semgrep-checker.yml` - This workflow will run on every push and pull request event to check if the proposed code changes contain any security vulnerabilities. If the workflow detects any security vulnerabilities, it will marked the action failed and leaves comment on PR
5. `multi-checker.yml` - This is a reusbale workflow which is responsible for running multiple checkers based on the event. The workflow will run the following checkers:
    - `Repolinter`
    - `Semgrep`
    - `Copyright-License-Detector`
    - `PR-Check-Email`
6. `preflight-checker-workflow` - This workflow that triggers the `multi-checker.yml` workflow template to run a set of preflight checks on a repository.