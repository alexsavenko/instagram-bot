# instagram-bot project

The instagram-bot project is tool for automating various tasks on Instagram.

---
## Description
instagram-bot aims to automate tasks such as posting, liking, following, and more on the Instagram platform. While currently only the post_uploader.py module is available, additional modules will be added in the future to extend the functionality of the bot.

---
## Installation
To install and use the project, follow these steps:

Clone the repository to your computer and go to project directory:
```shell
git clone https://github.com/alexsavenko/instagram-bot.git
cd InstagramBot
```

Install dependencies using pip:
```shell
pip install -r requirements.txt
```

Install playwright browsers:
```shell
playwright install
```

---
## Usage

### post_uploader.py module

#### Note
This module use headless webdriver (playwright) for interaction with Instagram trough login. 
For avoiding frequent login - application saving and reuse browser storage data in file `insta_state.json` (creates after first success login).
For change this file storage path - edit variable `INSTA_STATE_FILE` in `post_uploader.py` (by default file is next to `post_uploader.py`)

#### For demo run 

1. edit params in `demo_post_uploader.py`
``` python
params = {
    'login': 'your_username',
    'pwd': 'your_password',
    'file': '/path/to/your/file.jpg',
    'caption': 'caption for post that will be uploaded'
}
```
2. run `demo_post_uploader.py`
```shell
python3 demo_post_uploader.py
```

#### Import in to your script
You can copy the file `post_uploader.py` in your project folder and use it like in example:

```python
import post_uploader as pu

login = 'your_username'
pwd = 'your_password'
file = '/path/to/your/file.jpg'
caption = 'Check out this awesome photo!'

# create post
pu.create_post(login, pwd, file, caption)
```
- login (str): The username for authentication to Instagram.
- pwd (str): The password for authentication to Instagram.
- file (str): The path to the image or video file to be posted (look at Instagram requirements for posts).
- caption (str): The caption or description for the post.

---
## Feedback and Suggestions
***This is my first project in Python, and I am still getting acquainted with this cool tool.
I welcome any feedback, comments, and advice from the community...It's very important to me.
If you have any suggestions on how to improve this project, please feel free to let me know!***

---
## Disclaimer
1. This application is an open-source project intended for learning and research purposes.
2. The author assumes no responsibility for any direct or indirect losses incurred through the use of this application.
3. When using this application, it is essential to comply with the laws and regulations of your country or region and refrain from any illegal activities.

By using this application, you agree to and accept all the terms and conditions of this disclaimer. If you do not agree with these terms, please refrain from using this application.