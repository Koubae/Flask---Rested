#!/bin/bash



function make_secret() {
  python3 ./Scripts/make_secret.py;
}


if [ $1 == "make_secret" ];
  then make_secret;

else echo "No action needed..";
fi;

