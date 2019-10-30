#! /usr/bin/env python
import argparse
import numpy as np
import os

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class SocialNetwork:
    def __init__(self):
        self.names = []
        self.network = []
        self.posts = []

    def findNode(self, u):
        flag = 0
        for i in range(len(self.names)):
            if self.names[i] == u:
                flag = 1
                break
        if flag == 1:
            return i
        else:
            return -1    

    def createNode(self, u):
        self.names.append(u)
        self.network.append([]) 
        self.posts.append([])

    def deleteNode(self, u):
        indexOfPerson = self.findNode(u)
        if (indexOfPerson >= 0):
            self.network.pop(indexOfPerson)
            self.posts.pop(indexOfPerson)
            self.names.pop(indexOfPerson)

    def addEdge(self, u, v):
        self.network[u].append(v)

    def createPost(self, u, post):
        self.posts[u].append(post)

    def showGraph(self):
        print(self.graph)

    def getNetwork(self, u):
        return self.network[u]

    def getPosts(self, u):
        return self.posts[u]

    def breadthFirstSearch(self, start):
        if start < len(self.network):
            visited = []
            q1 = Queue()
            result = []
            V = len(self.network)
            for i in range(V):
                visited.append('white')
            visited[start] = 'grey'
            result.append(start)
            q1.enqueue(start)
            while not q1.isEmpty():
                curr = q1.dequeue()
                for i in self.network[curr]:
                    if visited[i] == 'white':
                        visited[i] = 'grey'
                        result.append(i)
                        q1.enqueue(i)
                visited[curr] = 'black'
            return result
        return None

    def DFSUtil(self, start, visited, result): 
        visited[start] = True
        result.append(start)
        for i in self.network[start]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited, result) 
  
    def depthFirstSearch(self, start): 
        if start < len(self.network):
            visited = [False] * (len(self.network)) 
            result = []
            self.DFSUtil(start, visited, result)
            return result
        return None

class Post:
    def __init__(self):
        self.title = ""
        self.content = ""
        self.likes = []

def run(args):

    # initialize a SocialNetwork
    g1 = SocialNetwork()



    
    if args.ite:
        # if the arguments provided in command line interface will have a '-i' flag, then the program will proceed in interactive testing environment 
        choice = 1
        print("### Entering interactive testing environment ###")
        print("\n-:-:-:-:-:-: Choose from the below choices to continue :-:-:-:-:-:-")
        print("(1) Load network")
        print("(2) Set probabilities")
        print("(3) Node operations (find,insert,delete)")
        print("(4) Edge operations (like/follow-add,remove)")
        print("(5) Newpost")
        print("(6) Display network (visualise)")
        print("(7) Display statistics")
        print("(8) Update (runatimestep)")
        print("(9) Save network") 
        while choice != -1:

            # one of the above choices will lead to some functionality as stated above
            choice = int(input("Enter a choice (Press 0 to see the choices again or Press -1 to exit): "))
            while choice < -1 or choice > 9:
                choice = int(input("Enter a valid choice (Press 0 to see the choices again or Press -1 to exit): "))


            # For reprinting all the choices that the user have    
            if choice == 0:
                print("\n-:-:-:-:-:-: Choose from the below choices to continue :-:-:-:-:-:-")
                print("(1) Load network")
                print("(2) Set probabilities")
                print("(3) Node operations (find,insert,delete)")
                print("(4) Edge operations (like/follow-add,remove)")
                print("(5) Newpost")
                print("(6) Display network (visualise)")
                print("(7) Display statistics")
                print("(8) Update (runatimestep)")
                print("(9) Save network") 



            # Loads the g1 object of type SocialNetwork from the .npy files names1, network1, posts    
            elif choice == 1:
                print("-:-:-:-:-:-: Loading Networks :-:-:-:-:-:-")
                if os.path.exists('names1.npy') and os.path.exists('network1.npy') and os.path.exists('posts1.npy'):
                    loadedNames = np.load('names1.npy', allow_pickle = True)
                    loadedNetwork = np.load('network1.npy', allow_pickle = True)
                    loadedPosts = np.load('posts1.npy', allow_pickle = True)
                    g1.names = [None] * len(loadedNames)
                    g1.network = [None] * len(loadedNames)
                    g1.posts = [None] * len(loadedNames)
                    for i in range(len(loadedNames)):
                        g1.names[i] = loadedNames[i]
                    for i in range(len(loadedNetwork)):
                        if loadedNetwork[i] == "NA":
                            g1.network[i] = []
                        else:
                            g1.network[i] = loadedNetwork[i]
                    for i in range(len(loadedPosts)):
                        if loadedPosts[i] == "NA":
                            g1.posts[i] = []
                        else:
                            g1.posts[i] = loadedPosts[i]
                    # for i in range(len(g1.posts)):
                    #     if g1.posts[i] == "NA":
                    #         g1.posts[i] = []
                else:
                    print("No file to load!")
                
            elif choice == 2:
                print("...Entering set probabilities...")

                
            # For finding, inserting and deleting a node/person from the SocialNetwork
            elif choice == 3:
                print("\n-:-:-:-:-:-: Enter the operation number you want to perform :-:-:-:-:-:-")
                print("(1) Find a person")
                print("(2) Insert a person")
                print("(3) Delete a person")
                operation = int(input("Enter an operation: "))
                while operation < 1 or operation > 3:
                    operation = int(input("Enter a valid operation: "))
                if operation == 1:
                    name = input("Enter the name of the person you want to find: ")
                    foundIndex = g1.findNode(name)
                    if foundIndex == -1:
                        print("No person found with the entered name!")
                    else:
                        print("\n-:-:-:-:-:-: Enter the seriel of the information you want to know about", name, ":-:-:-:-:-:-")
                        print("(1) Number of following")
                        print("(2) Number of posts")
                        info = int(input("Enter the info number: "))
                        while info < 1 or info > 2:
                            info = int(input("Enter a valid info number: "))
                        if info == 1:
                            print("Number of persons following", name, ":", len(g1.getNetwork(foundIndex)))
                        elif info == 2:
                            print("Number of posts by", name, "are", len(g1.getPosts(foundIndex)))        
                elif operation == 2:
                    name = input("Enter the name of the person you want to insert: ")
                    g1.createNode(name)

                elif operation == 3:   
                    name = input("Enter the name of the person you want to delete: ") 
                    g1.deleteNode(name)


            # For liking / unliking / follow / unfollow
            elif choice == 4:
                name = input("Please, enter your name to continue: ")
                foundIndex = g1.findNode(name)
                if foundIndex < 0:
                    print("No person found with this name")
                else:
                    print("Hi,", name)
                    print("\n-:-:-:-:-:-: Enter the operation number you want to perform :-:-:-:-:-:-")
                    print("(1) Like / Unlike a post")
                    print("(2) Follow / Unfollow somebody")
                    operation = int(input("Enter an operation: "))
                    while operation < 1 or operation > 2:
                        operation = int(input("Enter a valid operation: "))
                    if operation == 1:
                        personName = input("Enter the name of the person whose post you want to see: ")
                        foundPersonIndex = g1.findNode(personName)
                        if foundPersonIndex < 0:
                            print("No person found with this name")
                        else:
                            personPosts = g1.posts[foundPersonIndex]
                            if len(personPosts) == 0:
                                print(personName + " has posted nothing on SocialSim!")
                            else:
                                print("Posts by", personName, "are: ")
                                for i in range(len(personPosts)):
                                    print("(" + str(i + 1) + ") " + personPosts[i].title)
                                postNumber = int(input("Select the post number: "))
                                while postNumber < 1 or postNumber > len(personPosts):
                                    postNumber = int(input("Select a valid post number: "))
                                print("Title: " + personPosts[postNumber - 1].title)
                                print("Content: " + personPosts[postNumber - 1].content)
                                liked = False
                                # print("foundIndex: " + str(foundIndex))
                                # print("likes:", personPosts[postNumber - 1].likes)
                                for personWhoLiked in range(len(personPosts[postNumber - 1].likes)):
                                    # print("Person who liked: " + str(personWhoLiked))
                                    if personWhoLiked == foundIndex:
                                        liked = True
                                        break
                                if liked:
                                    print("->->->->->-> Liked by you!")
                                    wantToUnlike = input("Do you want to unlike the post(y/n): ")
                                    # while(wantToUnlike != "n" or wantToUnlike != "y"):
                                    #     wantToUnlike = input("Do you want to unlike the post(y/n): ")
                                    if wantToUnlike == "y":
                                        for j in range(len(personPosts[postNumber - 1].likes)):
                                            if personPosts[postNumber - 1].likes[i] == foundIndex:
                                                personPosts[postNumber - 1].likes.pop(j)
                                                break
                                        print("Post unliked by you!")
                                else:
                                    wantToLike = input("Do you want to like the post(y/n): ")
                                    # while(wantToLike != "n" or wantToLike != "y"):
                                    #     wantToLike = input("Do you want to like the post(y/n): ")
                                    if wantToLike == "y":
                                        personPosts[postNumber - 1].likes.append(foundIndex)
                                        print("Post liked by you!")
                    elif operation == 2:
                        personName = input("Enter the name of the person whom you want to follow/unfollow: ")
                        foundPersonIndex = g1.findNode(personName)
                        if foundPersonIndex < 0:
                            print("No person found with this name")
                        else:
                            if foundIndex == foundPersonIndex:
                                print("You cannot follow/unfollow yourselves!")
                            else:
                                myNetwork = g1.network[foundIndex]
                                following = False
                                for i in range(len(myNetwork)):
                                    if myNetwork[i] == foundPersonIndex:
                                        following = True
                                        break
                                if following:
                                    print("You are following " + g1.names[foundPersonIndex])
                                    wantToUnfollow = input("Do you want to unfollow " + g1.names[foundPersonIndex] + "(y/n): ")
                                    if wantToUnfollow == "y":
                                        myNetwork.pop(i)
                                        print("You have now unfollowed " + g1.names[foundPersonIndex] + "!")
                                else:
                                    wantToFollow = input("Do you want to follow " + g1.names[foundPersonIndex] + "(y/n): ")
                                    if wantToFollow == "y":
                                        myNetwork.append(foundPersonIndex)
                                        print("You are now following " + g1.names[foundPersonIndex] + "!")
                            

            # Creates a new post    
            elif choice == 5:
                name = input("Enter the name of the person who want to post: ")
                foundIndex = g1.findNode(name)
                if foundIndex < 0:
                    print("No person found with this name")
                else:
                    print("Hi,", name)
                    post = Post()
                    post.title = input("Enter the title of the new post: ")
                    post.content = input("Enter the content of the new post:\n")
                    g1.createPost(foundIndex, post)



            # display and visualize the network
            elif choice == 6:
                print("-:-:-:-:-:-: Displaying Network :-:-:-:-:-:-")
                for i in range(len(g1.names)):
                    if len(g1.network[i]) == 0:
                        print(g1.names[i] + " is not following anybody!")
                    else:
                        print(g1.names[i] + " is following ", end = '')
                        for j in range(len(g1.network[i])):
                            if j == len(g1.network[i]) - 1:
                                print(g1.names[g1.network[i][j]], end = '.\n')
                            else:
                                print(g1.names[g1.network[i][j]], end = ', ')
                            

                print('Names:', g1.names)
                print('Network:', g1.network)
                print('Posts:', g1.posts)
                print('BFS: ', g1.breadthFirstSearch(0))
                print('DFS: ', g1.depthFirstSearch(0))



            elif choice == 7:
                print("...Entering Display statistics...")
            elif choice == 8:
                print("...Entering run a timestep...")


            # saves the g1 object in .npy files
            elif choice == 9:
                print("...Entering save...")
                temp_network = g1.network.copy()
                temp_posts = g1.posts.copy()
                for i in range(len(temp_network)):
                    if temp_network[i] == []:
                        temp_network[i] = "NA"
                for i in range(len(temp_posts)):
                    if temp_posts[i] == []:
                        temp_posts[i] = "NA"
                # print('Names:', g1.names)
                # print('Network:', temp_network)
                # print('Posts:', temp_posts)
                np.save('names1.npy', g1.names, allow_pickle = True)
                np.save('network1.npy', temp_network, allow_pickle = True)
                np.save('posts1.npy', temp_posts, allow_pickle = True)
        
    elif args.sm:
        # if the arguments provided in command line interface will have a '-s' flag, then the program will proceed in simulation mode
        print("### Entering simulation mode ###")

    else:
        # no argument is passed
        print("### Showing usage information ###")
        print("--> Use the flag '-i' to enter the interactive testing mode")
        print("--> Use the flag '-s' to enter simulation mode eg:(SocialSim –s netfile eventfile prob_like prob_foll)")    

    print("Thank you for using SocialSim")
    

def main():
    parser = argparse.ArgumentParser(description = "Hello World from argparse... YEAH!!")
    parser.add_argument("-i", help = "Interactive Testing Environment", dest = "ite", action = "store_true")
    parser.add_argument("-s", help = "Simulation mode", dest = "sm", type = str, required = False)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()