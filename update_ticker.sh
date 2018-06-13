#!/bin/bash

curl -G https://api.coinmarketcap.com/v1/ticker/\?limit\=0 > ~/Downloads/ticker
grep -w "id" ticker > ticker_id.tx
vim ticker_id.txt # Block delete
sed -i '' "s/\,\ //g" ticker_id.txt

grep -w "id" -A 2 ticker > ticker_id_full.txt
vim ticker_id_full.txt #  Block delete
sed -i '' '/^\-\-/d' ticker_id_full.txt

\mv ~/Downloads/ticker_id* .
git add -A . && git commit -m "[Blockchain] Update ticker" && fuckgfw git push origin master
