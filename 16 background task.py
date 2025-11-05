
from fastapi import FastAPI , BackgroundTasks

import requests

import time


app = FastAPI()

image_urls = [
    "https://unsplash.com/photos/a-bunch-of-pink-donuts-are-stacked-on-top-of-each-other-obyYZVKwCNI",
    "https://images.unsplash.com/photo-1508138221679-760a23a2285b?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1074",
    "https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=764",
    "https://images.unsplash.com/photo-1500462918059-b1a0cb512f1d?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=687",
    "https://wpengine.com/wp-content/uploads/2021/05/optimize-images-1024x681.jpg",
    "https://media.istockphoto.com/id/1399246824/photo/digital-eye-wave-lines-stock-background.jpg?s=612x612&w=0&k=20&c=1cW5xuLcb6HPDj6CLQQFBvGK5_fJvx9eA2egik-3hAc="
]

async def download_image(image_urls):
    start_time = time.time()
    for image in image_urls:
        # print("#"*10,image_urls,"#"*10)
        print("#"*10,image,"#"*10)
        # break
        image_name = image.split('/')[3]
        image_name = f'{image_name}.jpg'

        byte_image = requests.get(image).content 

        with open(image_name,'wb') as img_file:
            img_file.write(byte_image)
            print(f'{image_name} Download')
    
    end_time = time.time() - start_time
    print(end_time)

@app.post('/download')
async def download(image_url:list[str],background_task : BackgroundTasks):
    background_task.add_task(download_image,image_urls)
    return {"message" : "Image Download"}    



# async def download_image(image_urls):
#     start = time.time()
#     for image in image_urls:
#         image_name = image.split('/')[3]
#         image_name = f'{image_name}.jpg'  
#         byte_image = requests.get(image).content
        

#         with open(image_name ,'wb') as img_file:
#             img_file.write(byte_image)
#             print(f'{image_name} download')
#     end = time.time() - start
#     print(end)



# @app.post('/download')
# async def download(image_urls:list[str],background_task : BackgroundTasks):
#     background_task.add_task(download_image,image_urls)
#     return{"message":"Image has beeen Download"}

