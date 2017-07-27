class Network:
    def __init__(self):
        self.users = []

    def add_users(self, new_user):
        self.users.append(new_user)

class User:

    def __init__(self, name):
        self.name = name
        self.friends = []


    def add_friends(self, friend):
        self.friends.append(friend)

def main():
    net = Network()

    while True:

        #ask for what the user wants to do
        print("List of users: ")
        for person in range (0, len(net.users)):
            print(net.users[person].name)
        user_action = input("What do you want to do?\n \
        You can create a user (u), to add a friend (a), show your friends (f), show all users(s),\n \
        or you can quit (q). ")

        if user_action == 'q':
            print("Sorry to see you go!")
            exit()

        #elif = else if. So, if the user action was NOT q, now check if it's u
        elif user_action == 'u':
            user_id = input('What\'s your name? ')
            person1 = User(user_id)
            print('Hello ' + (person1.name) + "!")
            net.add_users(person1)

        #add a friend
        elif user_action == 'a':
            you = input('Who do you want to add? ')
            me = input("Who are you? ")
            for user in net.users:
                if (user.name == me):
                    for user2 in net.users:
                        if (user2.name == you):
                            print("You are now friends with " + you)
                            user2.add_friends(user)
                            user.add_friends(user2)



        #show your friends
        elif user_action == 'f':
            tree = input('Who are you? ')
            isInList = False
            for user3 in net.users:
                if (user3.name == tree):
                    isInList = True
                    print("Here are your friends!")
                    for bud in user3.friends:
                        print(bud.name)
                    break
            if isInList == False:
                print('That user doesn\'t exist. ')


        #show all users
        elif user_action == 's':
            print("List of users: ")
            for person in range (0, len(net.users)):
                print(net.users[person].name)


        #else here means, if the user action was ANYTHING else
        #besides q, u, d, r, or l.
        else:
            print("Um, I don't know what that means. Please ask again.")

        #at the end of the if/else statements, print a line of stars
        #to help the user separate the previous action from the next action
        print("**********************\n")

main()
