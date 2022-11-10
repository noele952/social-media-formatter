import os
import boto3
from PIL import Image

input_bucket = os.getenv('INPUT_BUCKET')
output_bucket = os.getenv('OUTPUT_BUCKET')


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    key = event['Records'][0]['s3']['object']['key']
    print(key)
    file_type = os.path.splitext(key)[-1].lower()
    try:
        local_file_name = '/tmp/file' + file_type
        s3.download_file(input_bucket, key, local_file_name)
    except Exception as e:
        print(e)
        return False
    if file_type == '.mp4':
        outfile = '/tmp/file2.mp4'
        ffmpeg_commands = ' -vf format=yuv420p -c:v libx264 -c:a aac -crf 23 -maxrate 3500k -bufsize 3500k -r 30 -ar ' \
                          '44100 -b:a 256k -sn -f mp4 '
        os.system('/opt/python/ffmpeg -i ' + str(local_file_name) + ffmpeg_commands + str(outfile))
    elif file_type in ['.jpg', '.jpeg']:
        try:
            image = Image.open(local_file_name)
        except Exception as e:
            print(e)
            return False
        outfile = '/tmp/file.jpg'
        if file_type != '.jpg':
            image = image.convert('RGB')
            image.save(outfile)
        aspect_ratio_limits = (1.01, 1.91)
        width, height = image.size[0], image.size[1]
        aspect_ratio = width / height
        if width > 1280 or (height > 1024):
            image.thumbnail((1280, 1024))
        if not aspect_ratio_limits[0] < aspect_ratio < aspect_ratio_limits[1]:
            print(f"aspect ratio out of spec: {aspect_ratio}\n"
                   f"Resized to {image.size[0]} x {image.size[1]}")
            new_height = int(width / 1.5)
            padding_size = int((new_height - height) / 2)
            result = Image.new(image.mode, (width, new_height), (0, 0, 0))
            result.paste(image, (0, padding_size))
            result.save(outfile)
    try:
        response = s3.upload_file(outfile, output_bucket, key, ExtraArgs={'ACL': 'public-read'})
    except Exception as e:
        print(e)
        return False

    s3.delete_object(
        Bucket=input_bucket,
        Key=key)
    return True