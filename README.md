# End to End Text-Summarization-NLP

# workflow
1. Update config.yaml
2. Updateparams.yaml
3. Update entity
4. Update Configuration manager in src config
5. Update the Components
6. Update Pipeline
7. Update Main.py
8. Update App.py



**Project Title:** Conversational Dialogue Summarization using Google Pegasus-CNN/DailyMail Model

**Project Overview:**
The goal of this project is to develop a Natural Language Processing (NLP) system that takes two-person dialogs as input and generates concise summaries of the conversations. The project utilizes the Google Pegasus-CNN/DailyMail model, a state-of-the-art pre-trained language model designed for text summarization. The system is containerized using Docker and set up for easy deployment on the cloud through GitHub Actions, ensuring a smooth Continuous Integration and Continuous Deployment (CICD) pipeline.

**Project Steps:**

1. **Data Collection and Preprocessing:**
   - Collect conversational dialog datasets containing two-person conversations.
   - Preprocess the raw text data by removing noise, special characters, and irrelevant information.

2. **Model Selection and Integration:**
   - Choose the Google Pegasus-CNN/DailyMail model from the Hugging Face Transformers library for text summarization.
   - Integrate the model into the project codebase and set up the required dependencies.

3. **Tokenization and Summarization:**
   - Tokenize the input conversations to prepare them for input into the model.
   - Utilize the model to generate abstractive summaries of the dialog content.
   - Post-process the generated summaries to ensure readability and coherence.

4. **Docker Containerization:**
   - Create a Dockerfile specifying the necessary environment, dependencies, and configurations.
   - Build a Docker image containing the project code and the required model.
   - Verify that the Docker container runs seamlessly with the summarization functionality.

5. **Cloud Deployment with GitHub Actions:**
   - Set up a GitHub repository to host the project code.
   - Create GitHub Actions workflows for automated deployment to a cloud platform (e.g., AWS, Google Cloud) whenever changes are pushed to the repository.
   - Configure the GitHub Actions workflow to build the Docker image and deploy the application on the cloud.

6. **CICD Pipeline:**
   - Whenever changes are made to the repository, GitHub Actions automatically trigger the defined workflow.
   - The workflow builds the Docker image, runs tests, and deploys the application to the cloud environment.
   - Notifications are sent to the team regarding the success or failure of each step in the pipeline.

**Benefits:**
- Efficient Summarization: The system provides concise summaries of two-person conversations, making it easier for users to quickly grasp the main points without reading the entire dialogue.
- Containerization: Docker containerization ensures consistent performance across different environments and simplifies deployment.
- Cloud Deployment: GitHub Actions automate the deployment process, making it convenient to deploy the application to the cloud.
- CICD Pipeline: The CICD pipeline facilitates development, testing, and deployment, ensuring a robust and reliable system.

**Future Enhancements:**
- Multi-Modal Summarization: Extend the system to handle conversations with mixed text and images or other modalities.
- User Interface: Develop a user-friendly interface to input conversations and visualize generated summaries.
- Fine-Tuning: Fine-tune the model on specific conversational datasets to improve summarization quality.
- Performance Metrics: Implement metrics to quantify the quality of generated summaries and continuously enhance the model's performance.

By implementing this project, the team aims to provide a powerful tool for automatically summarizing conversations, enhancing efficiency, and improving user experiences in various domains such as customer support, content analysis, and more.

