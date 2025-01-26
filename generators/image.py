from google.cloud import aiplatform
import vertexai.preview

def endpoint_predict_sample(
    project: str, location: str, instances: list, endpoint: str
):
    aiplatform.init(project=project, location=location)

    endpoint = aiplatform.Endpoint(endpoint)

    prediction = endpoint.predict(instances=instances)
    print(prediction)
    return prediction



project = 'dish-data-lab-prod-2512'

    # the Vertex AI region you will use
    # defaults to us-central1
location = 'us-central1'

instances = ["A cat holding a sign that says hello world"]

response = endpoint_predict_sample(project=project, location=location, instances=instances, endpoint="3220365104151265280")

print(response)