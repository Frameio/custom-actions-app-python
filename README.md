# custom-actions-app-python

<img width="1644" alt="artboard_small" src="https://user-images.githubusercontent.com/19295862/66240171-ba8dd280-e6b0-11e9-9ccf-573a4fc5961f.png">

# Frame.io 
Frame.io is a cloud-based collaboration hub that allows video professionals to share files, comment on clips real-time, and compare different versions and edits of a clip. With the addition of our custom actions feature, developers can extend Frame.io's capabilities by adding their own features (referred to as custom actions).

# Use Custom Actions with Frame.io

This is an example application which shows how to create a custom action for Frame.io. Frame.io custom actions allow you to build integrations directly into Frame.io as programmable UI components. This enables a whole class of workflows that can be triggered by users within the app, leveraging the same underlying events routing as Frame.io [webhooks](https://docs.frame.io/docs/webhooks). You can read more about custom actions in the [Custom Actions Overview](https://docs.frame.io/docs/uploading-assets) documentation.

Currently, custom actions are available for assets, and are displayed in the contextual / right-click dropdown menu available on any asset. An Asset is a robust representation of a file in S3, and its context in Frame.io, including transcodes, user/team/project context, and metadata. You can read about Assets in the [Uploading Assets](https://docs.frame.io/docs/uploading-assets) guide. In the Frame.io app, a custom action appears as shown in the image where *Test* is the name of the custom action: 

<p align="center"><img width="362" alt="Screen Shot 2019-10-03 at 4 54 58 PM" src="https://user-images.githubusercontent.com/19295862/66240029-3b989a00-e6b0-11e9-90fc-3d7cf91d346c.png"></p>

You can create multiple custom actions, and they will all appear in the same area as the Test custom action. 

In this example, we'll present the user with a form asking them to provide their name and favorite color. On submission, we'll present the user with a confirmation message.

For more information about how custom actions work, check out our [documentation](https://docs.frame.io/docs/custom-actions).

## Pre-requisites 

* Developer account with Frame.io - [https://developer.frame.io](https://developer.frame.io/)
* Web server with a publicly accessible address - we recommend trying [ngrok](https://https://ngrok.com/) and we have a doc on set up - [Set up and Troubleshoot ngrok (Mac)](https://docs.frame.io/docs/how-to-setup-and-troubleshoot-ngrok-mac).

## Configure Your Custom Action

You must configure your custom action in the [Custom Actions](https://developer.frame.io/actions/) area of developer.frame.io. Follow the instructions provided here: [Setup](https://docs.frame.io/docs/custom-actions#section-setup).

## Setup

```
$ export FLASK_APP=custom_action
```

## Usage

```
$ flask run
```

By default the application runs on port 5000, however this can be overridden by setting the `PORT` environment variable. You can do that by adding the port you want to the `flask run` command, as shown:

```
$ flask run -h localhost -p 8000
```

## Troubleshooting

If you need help getting ngrok to work, you can check out our [troubleshooting guide for ngrok](https://docs.frame.io/docs/how-to-setup-and-troubleshoot-ngrok-mac).
