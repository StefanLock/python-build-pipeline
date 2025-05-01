# python-build-pipeline

# making a reference for when I come back to it
docker build -t flask-demo:latest .
docker run flask-demo:latest -p 5000:5000

## Bugs

"@semantic-release/github" fails due to GH token in releaserd.json

Warning: The `set-output` command is deprecated and will be disabled soon. Please upgrade to using Environment Files. For more information see: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/