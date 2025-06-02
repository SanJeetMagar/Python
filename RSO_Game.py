Like = []
Dislike = []
def create(*fav):
    # print(fav)
    for item in fav:
        Like.append(item)
        print(f"Add: {item}")
def create1(*Not):
    for item in Not:
        Dislike.append(item)
        print(f"Add: {item}")
def view(index = None, Like_list = True, Dislike_list = True):

    if Like_list:
        for i in range(0, len(Like)):
            print(f"{i+1} - {Like[i]}")
    if Dislike_list:        
        for i in range(0, len(Dislike)):
            print(f"{i+1} - {Dislike[i]}")  
                
def delete(index = None):
    if index:
        Like.remove(Like[index])
        Dislike.remove(Dislike[index])
    Like.pop()
    Dislike.pop()

task = ["Travel","Watch anime"]
create(*task)
dontlike = ["Sleeping", "lossing"]
create1(*dontlike)
view(Like_list = True)
delete()
# print(Like)


