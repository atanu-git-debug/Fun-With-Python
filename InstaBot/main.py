# create a virtual environment and install instabot
# python -m venv instabot_env (to create a virtual environment)
# source instabot_env/bin/activate (to activate the virtual environment)
# pip install instabot (to install instabot library)

#importing the Bot class from instabot library
from instabot import Bot

# Create an instance of the Bot class
bot = Bot()

# Login to Instagram
bot.login(
    username="USER_NAMR",
    password="PASSWORD"
)

# to follow a user
bot.follow("username_to_follow")

# to unfollow a user
bot.unfollow("username_to_unfollow")

# to like a post by its URL
bot.like("https://www.instagram.com/p/POST_ID/")

# to comment on a post by its URL
bot.comment("https://www.instagram.com/p/POST_ID/", "Nice post!")

# to send a direct message to a user
bot.send_message("Hello! This is a test message.", ["recipient_username"])

# to upload a photo with a caption
bot.upload_photo("path/to/photo.jpg", caption="This is a caption for the photo.")

# to unfollow all users who do not follow back
bot.unfollow_non_followers()

# to unfollow all users
bot.unfollow_all()

# to logout from Instagram
bot.logout()