from performance import Performance
from trie_structure.levenshtein_trie import LevenshteinTrie
from trie_structure.damerau_levenshtein_trie import DamerauLevenshteinTrie
from dict_structure.levenshtein_dict import LevenshteinDict
from dict_structure.damerau_levenshtein_dict import DamerauLevenshteinDict
import json
import time


def main():
    path_kbbi ="./kbbi.txt"
    path_saltik = "./saltik_200.json"
    saltik = json.load(open(path_saltik))
    # Object Algorithm 
    lev_dict = LevenshteinDict(path_kbbi)
    lev_trie = LevenshteinTrie(path_kbbi)
    dalev_dict = DamerauLevenshteinDict(path_kbbi)
    dalev_trie = DamerauLevenshteinTrie(path_kbbi)
    performance = Performance(saltik=saltik)
    # lev_trie
    lev_trie_acc = performance.accuracy(lev_trie)    
    # dalev_trie
    dalev_trie_acc = performance.accuracy(dalev_trie)
    # lev_dict
    lev_dict_acc = performance.accuracy(lev_dict)
    # dalev_dict
    dalev_dict_acc = performance.accuracy(dalev_dict)
    print("============================")
    print("Muhammad Haddad - 2006596195")
    print("---------- lev_trie ----------")
    print(lev_trie_acc,"\n")
    print("---------- dalev_trie ----------")
    print(dalev_trie_acc,"\n")
    print("---------- lev_dict ----------")
    print(lev_dict_acc,"\n")
    print("---------- dalev_dict ----------")
    print(dalev_dict_acc,"\n")
    print("============================")
if __name__ == '__main__':
    main()