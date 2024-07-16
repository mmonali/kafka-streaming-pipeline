# kafka-streaming-pipeline
# Real-Time Streaming Data Pipeline

This project sets up a real-time streaming data pipeline using Kafka and Docker.

## Setup

1. Ensure Docker is installed locally.
2. Clone this repository and navigate to the project directory.
3. Run the following command to start the Docker containers:

    ```sh
    docker-compose up -d
    ```

## Kafka Consumer

The Kafka consumer (`consumer.py`) consumes data from the `user-login` topic, processes the data, and writes it to a new Kafka topic `processed-data`.

### Running the Consumer

1. Ensure the Docker containers are running.
2. Run the consumer script:

    ```sh
    python consumer.py
    ```

## Design Choices

- **Docker**: Used to ensure a consistent environment and easy setup.
- **Kafka**: Provides robust and scalable message queuing and processing capabilities.
- **Python**: Simple and efficient for writing the consumer script.

## Data Flow

1. Data generator produces messages to the `user-login` topic.
2. Kafka consumer reads messages from `user-login`, processes them, and writes to `processed-data`.

## Scalability and Fault Tolerance

- **Scalability**: Kafka is inherently scalable, allowing easy addition of more consumers/producers.
- **Fault Tolerance**: Kafka handles failures gracefully with replication and offset management.

## Production Deployment

1. Deploy Kafka and Zookeeper on a managed service or Kubernetes cluster.
2. Use CI/CD pipelines for deploying the consumer/producer applications.
3. Implement monitoring and alerting using tools like Prometheus and Grafana.
4. Scale Kafka brokers, producers, and consumers as needed.

## Additional Components

- **Schema Registry**: To manage and enforce schema consistency.
- **Monitoring Tools**: Prometheus and Grafana for monitoring Kafka metrics.
- **Security**: Implement SSL and authentication for secure communication.

## Scaling with Growing Dataset

1. Add more Kafka brokers to distribute the load.
2. Increase the number of partitions for topics.
3. Use Kafka Streams or other stream processing frameworks for complex processing.

