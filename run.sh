#!/usr/bin/env bash
# Run this locally, from the root of your repo, whenever you want to
# preview your site with an up-to-date CV PDF.
#
# Usage:
#   ./build.sh          -> rebuilds cv.pdf, then starts a local preview server
#   ./build.sh --build  -> rebuilds cv.pdf, then does a one-time site build (no server)

set -e

echo "==> Rebuilding assets/cv.pdf from _pages/cv.md ..."
python3 scripts/build_cv.py

echo "==> CV PDF updated."

if [ "$1" == "--build" ]; then
  echo "==> Building Jekyll site (output in _site/) ..."
  bundle exec jekyll build
else
  echo "==> Starting Jekyll local server at http://localhost:4000 ..."
  bundle exec jekyll serve
fi
