# Image Embedding Generation with Voyage AI

This script, `escape.py`, is designed to generate multimodal embeddings for images using the Voyage AI API. It connects to a MongoDB Atlas database to retrieve documents containing image URLs, downloads the images, and generates embeddings using the Voyage AI service. The generated embeddings are then stored back in the MongoDB database.

## Prerequisites

- Python 3.x
- MongoDB Atlas account
- Voyage AI API key

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Packages**:
   Install the necessary Python packages using pip:
   ```bash
   pip install pymongo requests pillow voyageai
   ```

3. **Configure Environment Variables**:
   - Set the `VOYAGE_API_KEY` environment variable with your Voyage AI API key.

4. **MongoDB Connection**:
   - Update the MongoDB connection string in `escape.py` to point to your MongoDB Atlas instance.

## Usage

Run the script to generate embeddings:
```bash
python escape.py
```

The script will:
- Connect to the MongoDB database and fetch documents containing image URLs.
- Download each image and store it locally.
- Use the Voyage AI API to generate embeddings for each image.
- Store the generated embeddings back in the MongoDB database.

## Logging

The script uses Python's logging module to provide detailed information about the process, including any errors encountered during execution.

## Troubleshooting

- Ensure that the `VOYAGE_API_KEY` is correctly set and that the Voyage AI client is initialized without errors.
- Verify that the MongoDB connection string is correct and that the database is accessible.
- Check the logs for any errors related to image downloading or embedding generation.

## License

This project is licensed under the MIT License. See the LICENSE file for details.