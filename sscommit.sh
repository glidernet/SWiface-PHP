rm *funcs.py  ksta.py
cp /nfs/OGN/src/funcs/parserfuncs.py .
cp /nfs/OGN/src/funcs/dtfuncs.py .
cp /nfs/OGN/src/SARsrc/ksta.py .
cp /nfs/OGN/src/funcs/parserfuncs.py .
cp /nfs/OGN/src/funcs/ogntfuncs.py .
cp /nfs/OGN/src/funcs/ognddbfuncs.py .
cp /nfs/OGN/src/funcs/flarmfuncs.py .
cp /nfs/OGN/src/funcs/geofuncs.py .
cp /nfs/OGN/src/funcs/gistfuncs.py .
cp /nfs/OGN/src/funcs/dir2filfuncs.py .
cp /nfs/OGN/src/funcs/sgp2filfuncs.py .
cp /nfs/OGN/src/funcs/soa2filfuncs.py .
pipreqs   --force  . >&/dev/null
git add .
git commit
git push origin   master
git push glidernet master

