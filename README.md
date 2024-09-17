
# EthiopicBibleAPI

The **EthiopicBibleAPI** is a FastAPI-based RESTful API designed to provide access to the Ethiopian Bible in multiple languages, including Amharic. This API allows developers to easily integrate Ethiopian Bible texts (verses, chapters, and books) into their applications, websites, or digital platforms.

## Table of Contents
- [Project Name](#project-name)
- [Introduction](#introduction)
- [Live Demo and Blog](#live-demo-and-blog)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [Licensing](#licensing)
- [Resources](#resources)
- [Screenshot](#screenshot)

## Project Name
EthiopicBibleAPI

## Introduction
The **EthiopicBibleAPI** provides developers with a simple, performant, and highly scalable API for accessing the Ethiopian Bible. Whether you are developing a mobile app, web application, or digital platform, you can use this API to retrieve Bible texts in multiple languages, including Amharic, and integrate them into your projects.

### Key Features:
- Retrieve specific Bible verses, chapters, or books.
- Supports multiple languages, including Amharic.
- High performance using FastAPI.
- Easy-to-use API endpoints for quick integration.

## Live Demo and Blog

- **Live API Deployment**: [EthiopicBibleAPI Live](https://ethiopicbibleapi-2.onrender.com/docs)  
  *(Replace this with the actual deployment link)*
- **Final Project Blog Article**: [How I Built EthiopicBibleAPI](https://medium.com/@danielendale/building-ethiopicbibleapi-a-fastapi-powered-restful-api-for-the-ethiopian-bible-abfab6abfe0d)  
  *(Replace this with the blog link)*

## Author
- **Daniel Demerw **  
  [LinkedIn](https://www.linkedin.com/in/danieldemerw)

## Installation

Follow these steps to install and set up the **EthiopicBibleAPI** project on your local machine:

### 1. Clone the Repository
\```bash
git clone https://github.com/sheshbazzarr/EthiopicBibleAPI.git
cd EthiopicBibleAPI
\```

### 2. Set Up a Virtual Environment
\```bash
python -m venv env
source env/bin/activate  # On Linux/macOS
\```

OR

\```bash
env\Scripts\activate  # On Windows
\```

### 3. Install Dependencies
\```bash
pip install -r requirements.txt
\```

### 4. Run the Application
\```bash
uvicorn main:app --reload
\```

Visit `http://127.0.0.1:8000/docs` to access the automatically generated API documentation.

## Usage

Here are some example API requests:

- **Get a specific Bible verse**:  
  `GET /bible/verse?book=John&chapter=3&verse=16`
  
- **Get a chapter**:  
  `GET /bible/chapter?book=John&chapter=3`
  
- **Get an entire book**:  
  `GET /bible/book?book=John`

For more detailed documentation, visit the `/docs` or `/redoc` endpoints once the app is running.

## Contributing

If you would like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

All contributions are welcome, including bug fixes, new features, and documentation improvements.

## Related Projects
Here are a few similar or related projects that you might find interesting:

- [Bible API](https://ethiopicbibleapi-2.onrender.com/docs)
- [YouVersion Bible API](https://www.youversion.com/develo/)

## Licensing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Screenshot

Here’s a preview of the EthiopicBibleAPI in action:

![Ethiopic Bible API Screenshot](./img001.png)  
*(Replace `screenshot.png` with the actual image path)*

## Watch the Demo

[![Watch the Demo on YouTube](https://img.youtube.com/vi/oo6tStCSIeE/0.jpg)](https://www.youtube.com/watch?v=oo6tStCSIeE)
