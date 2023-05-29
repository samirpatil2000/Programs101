import requests

SQL_ERROR = "SQLite error"
base_url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/start?q="

# List of possible table names or words
table_names = ['users', 'orders', 'products', 'customers', 'flags', 'words', 'readme', 'ramps', 'dictonary', 'puzzles']
table_names = ['puzzle']

def call_query():    
    for table_name in table_names:
        query = f"select * from {table_name}"
        url = base_url + query
        
        response = requests.get(url)
            
        if SQL_ERROR in response.text:
            continue
        

        print(f"Table: {table_name}, Status Code: {response.status_code}")



import hashlib

hashes = [
    "md5(flag+salt):fb013abde8aa1ecc2345755410612f83:a6f817427ed2",
    "md5(flag+salt):1fbeeefcca483eba81d50343f4ca0078:16474bf95715",
    "md5(flag+salt):cd70ce7d0757440a44aeb965fb425c1b:61883aecd850",
    "md5(flag+salt):6bdcb023bf64863140519f01db2a1ea2:ed73014287d5",
    "md5(flag+salt):dc7c465a05506ff911bc08e8b532df39:26f84df81b66"
]

# Dictionary of seven-letter words
wordlist = [
    "example",
    "browser"
]

def crack_hash(hash_value, salt):
    
    for word in wordlist:
        candidate = word + salt
        hashed = hashlib.md5(candidate.encode()).hexdigest()        
        if hashed == hash_value:
            return candidate
    
    return None

for hash_entry in hashes:
    hash_value, salt = hash_entry.split(":")[1:]
    flag = crack_hash(hash_entry, salt)
    
    if flag:
        print("Cracked Hash: " + hash_entry)
        print("Flag: " + flag)
    else:
        print("Failed to crack Hash: " + hash_entry)
