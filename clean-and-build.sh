#!/bin/bash
set -e
cd /home/ole/workspace/driftsstotte-vg2

# Clean up stale build artifacts
mv dist/ dist-stale-cleanup/ 2>/dev/null || true
mv .astro/ .astro-stale/ 2>/dev/null || true

# Build
echo "=== Build ==="
./node_modules/.bin/astro build 2>&1
BUILD_EXIT=$?

echo ""
echo "=== Build exit code: $BUILD_EXIT ==="
echo "=== Pagefind ==="
npx pagefind --site dist 2>&1 || true

exit $BUILD_EXIT
