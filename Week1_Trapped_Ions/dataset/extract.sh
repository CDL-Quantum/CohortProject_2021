#!/bin/sh
for tar in *.tar.gz
do
  tar -xf ./"$tar"
  rm -f ./"$tar"
done
