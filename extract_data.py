from google.cloud import storage

def upload_blob (bucket_name, source_file_name, destination_blob_name):
    storage_client= storage.Client()
    bucket= storage_client.bucket(bucket_name)
    blob= bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
         "File {} uploaded to {}.".format(
             source_file_name, destination_blob_name
         )
    )

if __name__== "__main__":
    bucket_name= "telecomm-storage"
    source_file_name= "cleaned_telecommunication_data.csv"
    destination_blob_name= "data_folder/cleaned_telecommunication_data.csv"
    upload_blob(bucket_name, source_file_name, destination_blob_name)