#!/bin/bash

echo "{ \"commitHash\": \"$VERCEL_GIT_COMMIT_SHA\" }" | tee ./src/projectVersion.json
npm run build