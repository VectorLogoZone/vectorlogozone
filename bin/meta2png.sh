#!/bin/bash
find .. -name *.png -exec mogrify -comment "This image is from [HackerLogos](http://www.hackerlogos.org/).  Enjoy!" {} \;
