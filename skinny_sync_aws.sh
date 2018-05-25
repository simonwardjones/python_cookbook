echo "Syncing the local data.json to s3"
aws --profile simon s3 cp ./build/data.json s3://cookbook.simonwardjones.co.uk/data.json
