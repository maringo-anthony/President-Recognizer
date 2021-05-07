import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('jim-ryan-01.jpg','Jim Ryan'),
      ('jim-ryan-02.jpg','Jim Ryan'),
      ('jim-ryan-03.jpg','Jim Ryan'),
      ('tim-sands-01.jpg','Tim Sands'),
      ('tim-sands-02.jpg','Tim Sands'),
      ('tim-sands-03.jpg','Tim Sands')
      ]


# images=[('jim-ryan-01.jpg','Jim Ryan')
#       ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('alm4cu-cs4740-pa5','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )