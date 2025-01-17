import boto3
import json

# Using boto3 to call the Comprehend API
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

text_PII = "Customer: Tom Brady Credit Card Number: 54322234099876678 Bank Account Number: 1238766897 Routing Number: 1342121 Address 75667 Park Ln, Waltham MA"
text_sentiment = "I don't think there is anything I really like about the product"

print(json.dumps(comprehend.detect_pii_entities(Text=text_PII, LanguageCode='en'), sort_keys=True, indent=4))
print(json.dumps(comprehend.detect_sentiment(Text=text_sentiment, LanguageCode='en'), sort_keys=True, indent=4))
