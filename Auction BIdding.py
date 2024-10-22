Bids = {}
name = input("Enter your name : ")
bid = input("Enter your Bidding Amount = $")
Bids[name]= bid
Another_Bid = input("Do you want to add other bid Y/N")
print("\n"*100)
while Another_Bid=="y" or Another_Bid=="Y":
    name = input("Enter your name : ")
    bid = input("Enter your Bidding Amount = $")
    Bids[name] = bid
    Another_Bid = input("Do you want to add other bid Y/N")
    print("\n"*100)
    # Bids[name]= bid

print(Bids)

Bid_list = list(Bids.values())
print(Bid_list)
highest_Bid = max(Bid_list)
for name, bid in Bids.items():
    if bid == highest_Bid:
        print(f"Highest Bidder is {name} with a bid of ${highest_Bid}")
        break