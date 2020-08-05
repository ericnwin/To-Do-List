def heading(string, hashtag=1):
    hashes = "#"
    if hashtag < 6 and hashtag > 1:
        hashes *= hashtag
    elif hashtag > 6:
        hashes *= 6
    elif hashtag < 1:
        hashes *= 1
    
    return f"{hashes} {string}"


print(heading("A"))      # Returns "# A"
print(heading("A", 3))   # Returns "### A"
print(heading("A", 1))   # Returns "# A"
print(heading("A", 0))   # Returns "# A"
print(heading("A", 10))  # Returns "###### A"