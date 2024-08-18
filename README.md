
# Fitness Meme Generator

A fitness meme generator that collects data from various sources, processes it, and generates memes related to fitness.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Fitness Meme Generator is a tool designed to create fitness-related memes by gathering data from sources like Twitter, Reddit, and Imgflip. It uses various APIs to collect trending content, processes the data, and generates custom memes.

## Features
- Collect data from social media platforms (Twitter, Reddit).
- Generate memes using the Imgflip API.
- Containerized using Docker for easy deployment.
- Modular code structure for easy maintenance and extension.

## Technologies Used
- **Python**: The primary language used for scripting and backend logic.
- **Django**: A Python web framework used for the backend of the application.
- **Docker**: Used to containerize the application, ensuring consistent environments across development and production.
- **OpenAI API**: Utilized for generating text or content based on AI models.
- **Imgflip API**: Used for meme generation by leveraging existing meme templates.
- **Reddit API & Twitter API**: For collecting data from social media platforms to gather content and trends.
- **Git**: Version control system for tracking changes and collaborating on the project.
- **SQLite** (or **MySQL** depending on the setup): Database used to store data related to memes and user interactions.

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fitness_meme_generator.git
    cd fitness_meme_generator
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
   - Create a `.env` file in the project root.
   - Add necessary API keys and database configurations.

4. **Run the application**:
    ```bash
    python manage.py runserver
    ```

## Usage
- **Data Collection**: The scripts under `data_collectors/` collect data from specified sources.
- **Meme Generation**: Use the provided API endpoints to generate memes based on the collected data.

## Deployment
- **Docker**:
    - Build and run the Docker container:
        ```bash
        docker-compose up --build
        ```
- **AWS Deployment**:
    - Deploy the application to AWS Elastic Beanstalk with the provided configuration in the `docker-compose.yml` file.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
