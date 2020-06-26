#!/usr/bin/env python3

###################################
# Sample Custom Action: Form submission and success event.

# Frame.io sends a payload to the URL you specify: https://developer.frame.io/actions/
# The receiving application responds with an HTTP status code to acknowledge receipt,
# or responds with a custom callback that renders UI in Frame.io.  Custom action 
# are typically used as workflow triggers: you can kick off processes in
# third-party apps or fire additional API requests to Frame.io.
###################################


from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from typing import Dict
import uvicorn


# FastAPI's router pattern is useful to namespace API routes
# from other parts of your app: https://fastapi.tiangolo.com/tutorial/bigger-applications/
router = APIRouter()


@router.post('/example_action')
def callback(data: Dict):
    """ 
    Most functions will start by building a Dict from the initial Frame.io payload.
    Our FastAPI app's callback response pushes JSON data to the Frame.io API,
    which is preserved as a "data" object in the resulting request back to FastAPI.
    This data object exists in the second Frame.io payload ONLY,
    we'll evaluate it trigger the input form or send a success response.
    FastAPI supports type hints, a Python 3.6+ feature.  Learn more here: https://fastapi.tiangolo.com/python-types/#dict
    """

    form = {
	"title": "Example Custom Action",
	"description": "Custom actions use forms to exchange data between your app and Frame.io.",
    "custom_field" : "It's possible to add fields that won't be surfaced in the action UI",
	"fields": [{
			"type": "text",
			"name": "title",
			"label": "Title"
		},
		{
			"type": "select",
			"name": "captions",
			"label": "Captions:",
			"options": [{
					"name": "Off",
					"value": "off"
				},
				{
					"name": "On",
					"value": "on"
				}]
		}
	    ]}

	# The special case tells the user their form submitted successfully.
    if "data" in data:
        return JSONResponse({
        'title': 'Your form titled "' + data['data']['title'] + '" posted successfully.',
        })

	# The default behavior or 'base case' surfaces the form to the user.
    return JSONResponse(form)

if __name__ == "__main__":
    uvicorn.run(router, host="localhost", port=8000)