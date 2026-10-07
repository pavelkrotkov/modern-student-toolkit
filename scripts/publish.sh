#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-pavelkrotkov/modern-student-toolkit}"

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required: https://brew.sh" >&2
  exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  brew install gh
fi
if ! gh auth status >/dev/null 2>&1; then
  gh auth login -h github.com -p https -w
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init -b main
fi

LOGIN="$(gh api user --jq .login)"
UIDNUM="$(gh api user --jq .id)"
git config user.name >/dev/null 2>&1 || git config user.name "$LOGIN"
git config user.email >/dev/null 2>&1 || git config user.email "${UIDNUM}+${LOGIN}@users.noreply.github.com"

git add .
if ! git diff --cached --quiet; then
  git commit -m "Initial student toolkit"
fi

if ! gh repo view "$REPO" >/dev/null 2>&1; then
  gh repo create "$REPO" --public --source=. --remote=origin --push \
    --description "Russian-first practical computing curriculum for a modern university student"
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/${REPO}.git"
  git push -u origin main
fi

# Enable Pages for a custom GitHub Actions workflow. A 409 means it is already enabled.
gh api --method POST "/repos/${REPO}/pages" -f build_type=workflow >/dev/null 2>&1 || true

for _ in 1 2 3 4 5; do
  if gh workflow run pages.yml -R "$REPO" >/dev/null 2>&1; then
    break
  fi
  sleep 2
done

echo "Repository: https://github.com/${REPO}"
echo "Pages:      https://${REPO%%/*}.github.io/${REPO#*/}/"
