#!/usr/bin/env python3

###################################
# Sample Custom Action: Upload Frame.io video to Youtube
###################################


from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from typing import Dict
import uvicorn
import requests
import json
import os


router = APIRouter()

# TODO swap out asset Dict for modeled asset data using Pydantic:
# @router.post('/upload_to_youtube'), response_model=Asset
# ... then use BaseModel to model out the asset and capture relevant data

@router.post('/upload_to_youtube')
def upload_to_youtube(data: Dict):
    """ 
    This function creates a form and asks the Frame.io user to specify info
    about the file they want uploaded to YouTube.  The data is pushed into a payload
    and fired off to YouTube via a Zapier hook.
    To troubleshoot uploads, check Zapier's [https://zapier.com/app/history](zap history) and your YouTube account.
    """

    # Build a GET request to /v2/asset/:id
    asset_id = data.get('resource').get('id')
    asset_url = base_url+'assets/'+asset_id
    r = requests.request("GET", asset_url, headers=headers)

    # Store Frame.io's response to our GET /v2/asset request as a dict.
    asset = r.json()

    # Use attributes from asset dict to build a payload. 
    # Our FastAPI router sends the payload back to Frame.io in a callback response.
    asset_name = asset['name']
    description = asset['description']
    upload_url = asset['original']

    # Build a form to drive the user interaction in Frame.io.
    # We're pre-filling some fields for the user to facilitate a quicker upload.
    youtube_upload_form = {
        'title': 'Publish to Youtube',
        'description': 'Publishes to Channel: Frame io Platform',
        'fields': [
            {
            'type': 'text',
            'name': 'title',
            'label': 'Video Title',
            'value': asset_name
            },
            {
            'type': 'textarea',
            'name': 'description',
            'label': 'Description',
            'value': description
            },
            {
            "type": "select",
            "label": "Privacy",
            "name": "privacy",
            "value": "private",
            "options": [
                {
                    "name": "Public",
                    "value": "public"
                },
                {
                    "name": "Private",
                    "value": "private"
                },
                {
                    "name": "Unlisted",
                    "value": "unlisted"
                }
                ]
            },
            {
            "type": "text",
            "name": "tags",
            "label": "Tags"
            }
        ]
    }

    # See example_action.py for a detailed explanation of this conditional.
    if "data" in data:
        # Confirm we're working with the right asset:
        if data.get('resource').get('id') == asset.get('id'):

            payload = {
                'title': data['data']['title'],
                'description': data['data']['description'],
                'privacy': data['data']['privacy'],
                'tags': data['data']['tags'],
                'video_url': upload_url
            }

            #TODO is there a more appropriate FastAPI pattern for this request?
            requests.post(ZAPIER_HOOK_URL, data=json.dumps(payload))

	        # The special case tells the user their form submitted successfully.
            return JSONResponse({
            'title': 'Your video "'+ data['data']['title'] + '" has been submitted for upload to YouTube!'
        })

        else:
            raise HTTPException(
                status_code=400,
                detail="Bad request: Asset data not found or does not match expectations"
            )

	# The default behavior or 'base case' surfaces the form to the user.
    return JSONResponse(youtube_upload_form)


if __name__ == '__main__':

    # Safely store environment variables
    TOKEN = os.getenv('FRAME_IO_TOKEN')
    ZAPIER_HOOK_URL = os.getenv('ZAPIER_HOOK_URL')

    # Configure the custom action and webhook
    base_url = 'https://api.frame.io/v2/'
    headers = {
    "Authorization": "Bearer "+TOKEN
    }

    uvicorn.run(router, host="localhost", port=8000)