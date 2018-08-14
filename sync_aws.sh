echo "Syncing the build to s3"
aws --profile simon s3 sync ./build s3://cookbook.simonwardjones.co.uk
ls -1 ./python_recipes/*.py | wc -l | tr -d [:blank:]  > live_recipe_count.txt