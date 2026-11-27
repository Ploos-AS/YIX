# Alpha provenance review

Candidate baseline: b28965c675e2b9d24ca2cc5a544d8ee24b347a0d.

Discovery: changed filenames from PRs 1–34, not a complete Git tree or history audit. The following classifications are proposed, not verified rights grants.

| Paths | Intended license / review |
|---|---|
| lab/bird/*.conf, lab/compose.yaml, lab/Dockerfile, lab/rtr.py, lab/test.sh | MIT for original material; inspect copied examples and base image terms |
| lab/monitoring/*.py, *.yml, *.yaml, Dockerfile | MIT for original material; review external images and dependencies |
| toolkit/*.py, toolkit/examples/*.json | MIT for original code/configuration |
| .github/workflows/*.yml | MIT for original workflow code; external actions retain own terms |
| website/*.html, website/no/*.html, website/style.css | MIT for original markup/style; CC BY 4.0 for original prose; review assets |
| README.md, ROADMAP.md, SECURITY.md, LICENSING.md, CHANGELOG.md, GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, BRAND.md | CC BY 4.0 for original prose; brand rights excluded |
| docs/, architecture/, specification/, profiles/, implementations/, mips/ | CC BY 4.0 for original prose and diagrams; inspect embedded code separately |
| lab/*.md, lab/monitoring/README.md, toolkit/README.md, website/README.md, conformance/README.md, conformance/assessment-template.json | CC BY 4.0 for original documentation and templates |
| LICENSE, LICENSE-DOCS | License texts; retain original notices and terms |

## External materials

Review BIRD, container base images, monitoring components, GitHub Actions, referenced RFCs and any copied examples. A reference or runtime dependency is not automatically redistributed under the project license. Record exact versions, upstream sources, license identifiers and required notices before distributing third-party artifacts.

## Required maintainer review

Run from a clean checkout of the candidate:

```sh
git ls-files
git log --all --format='%h %an %s'
git submodule status
git grep -n -i -E 'copyright|spdx-license-identifier|license|adapted from|copied from'
```

Compare every tracked path with the inventory, inspect contribution history and confirm rights to license original contributions. Record per-file exceptions and notices; investigate binaries, fonts, images and generated assets. Do not publish private contributor details unnecessarily.

Status: **pending**. No complete tree, history, dependency or rights-holder verification has been performed. Unknown rights must be resolved before release. See [release gate](license-inventory.md).
