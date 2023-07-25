from minio import Minio
from minio.error import S3Error
import os

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "192.168.56.6:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("mybucket")
    if not found:
        client.make_bucket("mybucket")
    else:
        print("Bucket 'mybucket' already exists")

    # Upload '/home/user/Photos/asiaphotos.zip' as object name
    # 'asiaphotos-2015.zip' to bucket 'asiatrip'.

    dir = '/Server/minio/static/'
    
    for file in os.listdir(dir):

        if file.endswith('.css'):
            client.fput_object(
                "mybucket", f"static/{file}", f"/Server/minio/static/{file}",
                content_type="text/css",
            )
        elif file.endswith('.js'):
            client.fput_object(
                "mybucket", f"static/{file}", f"/Server/minio/static/{file}",
                content_type="application/javascript",
            )
        else:
            client.fput_object(
                "mybucket", f"static/{file}", f"/Server/minio/static/{file}",
            )
        print(
                f"/Server/minio/static/{file} is successfully uploaded as object 'static/{file}' to bucket 'mybucket'."
            )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)