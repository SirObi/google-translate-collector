docker build --build-arg BING_KEY=$BING_KEY -t mandarin .
docker run -v $PWD/mp3_outputs:/app/mp3_outputs mandarin