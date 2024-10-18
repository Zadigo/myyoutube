import secrets

def videos_directory_path(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(5)}.{extension}'
    return f'uploads/{instance.reference}/{new_file_name}'


def banners_directory_path(instance, filename):
    _, extension = filename.split('.')
    new_file_name = f'{secrets.token_hex(5)}.{extension}'
    return f'uploads/banners/{instance.user.userchannel_set.get().reference}/{new_file_name}'
