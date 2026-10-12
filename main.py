from ddgs import DDGS
print ("Welcome to my AI Search Engine!")
question = input("\nWhat would you like to search for? ")
print("\nSearching for:",question)
print("="*50)
results=DDGS().text(question,max_results=3)
for number, result in enumerate(results,start=1):
    print(f"\nRESULT {number}")
    print("-"*50)
    print("Title:", result["title"])
    print("Website:",result["href"])
    print ("Description:", result["body"][:150]+"...")
    print()
results=DDGS().text(question,max_results=5)
