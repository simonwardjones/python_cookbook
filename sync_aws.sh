echo "Syncing the build to s3"
aws --profile simon s3 sync ./build s3://cookbook.simonwardjones.co.uk
