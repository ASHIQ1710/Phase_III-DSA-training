data=[]
request=[]
followers=[]
post=[]
def login(data):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for index in range(len(data)):
        if username == data[index][0] and password == data[index][1]:
            print("Login successfull!")
            return
    print("Login failed! Please try again.")

def signup(data):
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    # Perform signup operation using the provided username and password
    data=[username,password]
    data.append(data)
    print("Signup successfull!")

def accept_follow_request(followers, request):
    follower = input("Enter the username of the follower: ")
    for index in range(len(data)):
        if data[index] == follower:
            print("Follower found!")
            print("follower: ",follower)
            print("data: ",data[index])
            followers.append(data[index])
            request.remove(data[index])
            print("Follow request accepted!")
            break
        else:
            print("Follower not found!")
def put_some_post(post):
    msg = input("Enter your post: ")
    post.append(msg)
    print("Post added successfully!")

def logout(username):
    print("User",username ,"logged out!")
    print("Logout successfull!")

while True:
    print("Instagram Menu:")
    print("1. Login")
    print("2. Signup")
    print("3. Accept follow request")
    print("4. Put some post")
    print("5. Logout")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login(data= data)
    elif choice == "2":
        signup(data)
    elif choice == "3":
        accept_follow_request(followers= followers, request= request)
    elif choice == "4":
        put_some_post(post= post)
    elif choice == "5":
        logout(username= data[0])
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using Instagram!")