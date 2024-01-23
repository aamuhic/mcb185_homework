# Amina Muhic
# aminamuhic

# Amina Muhic, Francesca Gasperini

# spelling bee 1
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -E "^[muocfta]{4,}$"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -E "^[muocfta]{4,}$" | wc -l

# spelling bee 2
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -E "^[tairnlb]{4,}$" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -E "^[tairnlb]{4,}$" | wc -l

# spelling bee 3
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -E "^[maodinc]{4,}$" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -E "^[maodinc]{4,}$" | wc -l

# spelling bee 4
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -E "^[anoigrz]{4,}$" 
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -E "^[anoigrz]{4,}$" | wc -l
