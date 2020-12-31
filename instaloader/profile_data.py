import instaloader

L = instaloader.Instaloader()

f = open('input.txt','r')
accounts = f.read()
p = accounts.split('\n')

PROFILE = p[:]
print(PROFILE)

for ind in range(len(PROFILE)):
    pro = PROFILE[ind]
    profile = instaloader.Profile.from_username(L.context, pro)
    main_followers = profile.followers
    posts = profile.mediacount
    id = profile.userid
    print('The profile UserID')
    print(id)
    print('The number of followers')
    print(main_followers)
    print('The total number of posts')
    print(posts)
    print('The profile is a verified profile?')
    print(profile.is_verified)
    print('\n')