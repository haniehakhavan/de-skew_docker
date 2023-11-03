# Deskew Image Processing Service

## Overview

The Deskew Image Processing Service is a web application built using Flask that allows users to automatically deskew and orient images. It can be used to correct the orientation and skew of scanned documents, which is particularly useful in applications like OCR (Optical Character Recognition) where correctly aligned text is crucial. This service provides a simple API for processing images.

## Features

- Automatic orientation estimation
- Skew correction
- Simple API for processing images
- Containerized using Docker for easy deployment

## Getting Started

Follow these steps to set up and run the Deskew Image Processing Service:

### Prerequisites

- Docker
- Python 3.x

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/deskew-image-processing.git
   cd deskew-image-processing

### Building and Running

Follow these steps to build and run the Deskew Image Processing Service using Docker:

#### Build the Docker Image

```bash
docker build -t deskew-image-processing .
```
#### Run the Docker Container with Volume Mount

To run the Deskew Image Processing Service Docker container with a volume mount, use the following command:

```bash
docker run -p 6060:6060 -v /path/to/your/project/data:/data deskew-image-processing
```

## Restful API

You can interact with the Skew Detection and Correction service through a Restful API. Below are the details of the API endpoints:

### Deskew Image

* **Method**: POST
* **Route**: /deskew
* **Request Body**: Form Data

| Parameter | Type   | Description                  |
| --------- | ------ | ---------------------------- |
| image     | file   | The image to be processed    |



