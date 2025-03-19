import os
import pymongo
import requests
from PIL import Image
from io import BytesIO
import voyageai
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Voyage AI client
try:
    vo = voyageai.Client()
    logging.info("Voyage AI client initialized successfully.")
except Exception as e:
    logging.error(f"Failed to initialize Voyage AI client: {e}")
    raise

# Connect to MongoDB
client = pymongo.MongoClient("your mongodb connection string")
db = client.dataset
collection = db.plants

# Directory to store images
image_dir = "downloaded_images"
os.makedirs(image_dir, exist_ok=True)

# Fetch documents
documents = collection.find()

# Prepare inputs and process each document
for doc in documents:
    try:
        text = f"This is a {doc['plant_name']}."
        image_url = doc['image_url']
        image_path = os.path.join(image_dir, f"{doc['plant_name'].replace(' ', '_')}.jpg")
        
        # Download and save image locally
        #logging.info(f"Downloading image for {doc['plant_name']} from {image_url}")
        response = requests.get(image_url)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        
        # Open the image from local storage
        image = Image.open(image_path)
        
        # Generate embeddings
        logging.info(f"Generating embeddings for {doc['plant_name']}")
        inputs = [[text, image]]
        try:
            result = vo.multimodal_embed(inputs, model="voyage-multimodal-3")
            logging.info(f"Embeddings generated for {doc['plant_name']}: {result.embeddings}")
        except Exception as e:
            logging.error(f"Error generating embeddings for {doc['plant_name']}: {e}")
            continue
        
        # Store embeddings back in MongoDB
        logging.info(f"Storing embeddings for {doc['plant_name']}")
        collection.update_one(
            {'_id': doc['_id']},
            {'$set': {'imageembeddings': result.embeddings}}
        )
    except Exception as e:
        logging.error(f"Error processing {doc['plant_name']}: {e}")

logging.info("Embedding generation completed.")
