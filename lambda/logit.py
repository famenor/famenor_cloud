import json

def lambda_handler(event, context):

    if "body" in event:
        event = event["body"]
        if event is not None:
            event = json.loads(event)

        else:
            event = {}

    if "G1" in event:
        
        new_row = {"G1": event.get("G1"), "G2": event.get("G2")}
        
        prediction = str(int(new_row["G1"]) + int(new_row["G2"]))
        return {"body": "Prediction " + prediction}
    
    return {'body': 'No parameters'}
