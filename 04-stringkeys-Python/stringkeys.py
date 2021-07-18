"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        result=self.calculate_hash_value(string)
        # if(result!=-1):
        #     if(self.table[result]!=None):
        #         self.table[result].append(string)
        #     else:
        #         self.table[result]=[string]
        self.table[result]=string
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        result=self.calculate_hash_value(string)
        
        if(string in self.table):
                return result
        else:
                return -1
        # Your code goes here
        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        res=(ord(string[0])*100)+ord(string[1])
        # print(res)
        return res


ht=HashTable()
ht.calculate_hash_value('UDACITy')



