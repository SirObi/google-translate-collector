# You can run this script like so:
# BING_KEY=$BING_KEY bash -c "sh generate_mp3_files.sh"
# Note that the script won't work without prepending BING_KEY, unless you export it in your shell config file (e.g. ~/.zshrc)

docker build --build-arg BING_KEY=$BING_KEY -t mandarin .
docker run -v $PWD/mp3_outputs:/app/mp3_outputs mandarin
