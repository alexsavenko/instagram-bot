import post_uploader as pu

params = {
    'login': 'your_username',
    'pwd': 'your_password',
    'file': '/path/to/your/file.jpg',
    'caption': 'Check out this awesome photo!'
}

pu.create_post(**params)