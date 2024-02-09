import instaloader


def ShowInformations(profile):

    username = profile.username
    followers = profile.followers
    bio = profile.biography

    print("\nUsername:", username)
    print("Followers:", followers)
    print("Bio:", bio)


def scrape_instagram_profile(username, password, target_profile):

    loader = instaloader.Instaloader()

    if username != "" and password != "":
        loader.login(username, password)

    try:
        # Load the profile of the given username
        profile = instaloader.Profile.from_username(
            loader.context, target_profile)

        all_followers = profile.get_followees()

        i = 0
        for follower in all_followers:
            ShowInformations(follower)
            i += 1
            if i == 5:
                break

    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile not found.")


print("Instagram login...")
username = input("Enter your username: ")
password = input("Enter your password: ")
target_profile = input("Enter the target profile: ")
scrape_instagram_profile(username, password, target_profile)
