import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# FastAPI settings
API_PORT = int(os.getenv("API_PORT", 8000))
API_HOST = os.getenv("API_HOST", "0.0.0.0")

# Kafka settings
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "logs")

# Elasticsearch settings
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")
ELASTICSEARCH_PORT = int(os.getenv("ELASTICSEARCH_PORT", 9200))
ELASTICSEARCH_INDEX = os.getenv("ELASTICSEARCH_INDEX", "logs")

# Prometheus settings
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", 9090))
