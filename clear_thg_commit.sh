echo "clear pyc"
find . -name "*.pyc" -exec rm -f {} \;
echo ".idea/*"
find . -name "*.idea/*" -exec rm -f {} \;
echo "___pycache__"
find . -name "pycache" -exec rm -f {} \;

python3 commit.py