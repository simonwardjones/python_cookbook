echo "Syncing the local data.json to s3"
aws --profile simon s3 cp ./build/data.json s3://cookbook.simonwardjones.co.uk/data.json
ls -1 ./python_recipes/*.py | wc -l | tr -d [:blank:]  > live_recipe_count.txt