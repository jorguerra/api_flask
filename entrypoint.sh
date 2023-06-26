#!/bin/sh

flask migrate
if [[ $DEBUG == true ]] 
then 
    flask --app /app/app run --host=0.0.0.0 --debug
else
    flask --app /app/app run --host=0.0.0.0
fi   
