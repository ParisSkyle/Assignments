import sys
class User():
    def __init__(self,username,friends = []): 
        self.username = username
        self.friends = friends
class SocialNetwork():
    def __init__(self,userList = []): 
        self.userList = userList
        self.AddData()
    def AddData(self): 
        with open(sys.argv[1]) as data:
            with open("output.txt","w") as f: pass
            for inpts in data:
                lst = inpts.split(":")
                usr = User(username = str(lst[0]))
                self.userList.append(usr)
                lst.pop(0)
                usr.friends = lst[0][:-1].split(" ") 
                if "" in usr.friends:usr.friends.remove("")
    def AddUser(self,username):
        isUser = False
        with open("output.txt","a") as output:
            for user in self.userList:
                if username == user.username:
                    output.write("ERROR: Wrong input type! for 'ANU’! -- This user already exists!!\n")
                    isUser = True
            if not isUser: 
                self.userList.append(User(username = username))
                output.write("User {} has been added to the social network successfully\n".format(username))
    def DeleteExistingUser(self,username):
        isUser = False
        with open("output.txt","a") as output:
            for user in self.userList:
                if username == user.username:
                    isUser = True
                    self.userList.remove(user)
            if isUser:
                for friend in self.userList: 
                    if username in friend.friends:
                        friend.friends.remove(username)
                output.write("User {} and his/her all relations have been removed successfully\n".format(username))                               
            else: output.write("ERROR: Wrong input type! for 'DEU'!--There is no user named {}!!\n".format(username))
    def Add_Delete_Friend(self,username,friendName,what = "add"):
        isuser, isfriend  = False, False
        with open("output.txt","a") as output:
            for user in self.userList:
                if friendName == user.username: isfriend = True
                if username == user.username:
                    isuser = True
                    for friend in self.userList:
                        if friendName == friend.username:                           
                            if what == "add":
                                if  friendName not in user.friends:
                                    user.friends.append(friendName)
                                    output.write("Relation between {} and {} has been added successfully\n".format(username,friendName))
                                else: output.write("ERROR: A relation between {} and {} already exists!!\n".format(username,friendName))
                            else: 
                                if  friendName in user.friends:
                                    user.friends.remove(friendName)
                                    friend.friends.remove(user.username)
                                    output.write("Relation between {} and {} has been deleted successfully\n".format(username,friendName))
                                else: output.write("ERROR: No relation between {} and {} found!!\n".format(username,friendName))
            if not isuser or not isfriend:
                if not isuser and not isfriend:
                    if what == "add": output.write("ERROR: Wrong input type! for 'ANF'! -- No user named {} and {} found!!\n".format(username,friendName))
                    else: output.write("ERROR: Wrong input type! for 'DEF'! -- No user named {} and {} found!!\n".format(username,friendName))
                elif not isuser: 
                    if what == "add": output.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named {username} found!!\n")
                    else: output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named {username} found!!\n")
                else: 
                    if what == "add": output.write(f"ERROR: Wrong input type! for 'ANF'! -- No user named {friendName} found!!\n")
                    else: output.write(f"ERROR: Wrong input type! for 'DEF'! -- No user named {friendName} found!!\n") 
    def FriendCount(self,username):
        isuser = False
        with open("output.txt","a") as output:
            for user in self.userList:
                if username == user.username:
                    output.write("User {} has {} friends\n".format(username,len(user.friends)))
                    isuser = True
            if not isuser: output.write(f"ERROR: Wrong input type! for 'CF'! -- No user named {username} found!\n")
    def FindPossibleFriends(self,username,maxdistance):
        isUser = False
        possibleFriendList = []
        with open("output.txt","a") as output:
            for user in self.userList:
                if username == user.username:
                    isUser = True
                    for friend in user.friends:                       
                        possibleFriendList.append(friend)
                        if int(maxdistance) >= 2:
                            for friendUser in self.userList:
                                if friend == friendUser.username:
                                    for friendsFriends in friendUser.friends:
                                        possibleFriendList.append(friendsFriends)
                                        if int(maxdistance) == 3:
                                            for friendsFriendsUser in self.userList:
                                                if friendsFriends == friendsFriendsUser.username:
                                                    for friendsFriendsFriends in friendsFriendsUser.friends:
                                                        possibleFriendList.append(friendsFriendsFriends)
            if not isUser: output.write(f"ERROR: Wrong input type! for 'FPF'! -- No user named {username} found!\n")
            else:
                if maxdistance > 0 and maxdistance < 4:
                    possibleFriendList = set(possibleFriendList)
                    possibleFriendList = list(possibleFriendList)
                    possibleFriendList.sort()
                    try: possibleFriendList.remove(username) 
                    except: pass              
                    output.write(f"User {username} has {len(possibleFriendList)} possible friends when maximum distance is {maxdistance}\n")
                    output.write("These possible friends: {}\n".format(str(possibleFriendList).replace("[","{").replace("]","}")))
                else: output.write("ERROR: Maximum distance is out of range!!\n")
    def SuggestFriend(self, username,md):
        isUser = False
        temp = []
        suggested_list = list()
        suggested_str = ""       
        with open("output.txt","a") as output:
            for user in self.userList:
                if username == user.username: 
                    isUser = True
                    for friend in user.friends:                       
                        for friendUser in self.userList:
                            if friend == friendUser.username:
                                for friendsFriends in friendUser.friends:
                                    temp.append(friendsFriends)
                                try: temp.remove(username)
                                except: pass            
            if not isUser: output.write(f"Error: Wrong input type! for 'SF'! -- No user named {username} found!!\n")
            else:
                if md < 1 or md > 4: output.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
                else:
                    for frnd in temp:
                        if frnd not in suggested_list and temp.count(frnd) >= md: suggested_list.append(frnd)
                    output.write(f"Suggestion List for {username} (when MD is {md})\n")
                    suggested_list.sort()
                    for suggestedFriend in suggested_list:
                        if temp.count(suggestedFriend) == 2: output.write("{} has {} mutual friends with {}\n".format(username,temp.count(suggestedFriend),suggestedFriend))
                    for suggestedFriend in suggested_list:
                        if temp.count(suggestedFriend) == 3: output.write("{} has {} mutual friends with {}\n".format(username,temp.count(suggestedFriend),suggestedFriend))
                    for i in suggested_list:
                        suggested_str = suggested_str +" " + i + ","
                    output.write(f"The suggested friends for {username}: {suggested_str}\n")
def main():
    main_inpts = []
    variables = []
    with open("output.txt","a") as output:
        with open(sys.argv[2]) as commands:
            for inpt in commands.read().splitlines():
                lst = inpt.split(" ")
                main_inpts.append(lst[0])
                variables.append(lst[1:])
            for i in main_inpts:
                if i == "ANU": socialNW.AddUser(username = variables[0][0]), variables.pop(0)
                elif i == "DEU": socialNW.DeleteExistingUser(username = variables[0][0]), variables.pop(0)
                elif i == "ANF": socialNW.Add_Delete_Friend(username = variables[0][0], friendName= variables[0][1], what = "add"), variables.pop(0)
                elif i == "DEF": socialNW.Add_Delete_Friend(username = variables[0][0], friendName= variables[0][1], what = "remove"), variables.pop(0)
                elif i == "CF": socialNW.FriendCount(username = variables[0][0]), variables.pop(0)
                elif i == "FPF": socialNW.FindPossibleFriends(username = variables[0][0],maxdistance= int(variables[0][1])), variables.pop(0)
                elif i == "SF":
                    try: socialNW.SuggestFriend(username = variables[0][0], md = int(variables[0][1])), variables.pop(0)
                    except: output.write("ERROR: Wrong Command\n"), variables.pop(0)
                else: variables.pop(0)
socialNW = SocialNetwork()
main()


