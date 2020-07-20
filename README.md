# custom-actions-app-python

<img width="1644" alt="artboard_small" src="https://user-images.githubusercontent.com/19295862/66240171-ba8dd280-e6b0-11e9-9ccf-573a4fc5961f.png">

# Use Custom Actions with Frame.io

Frame.io's [custom actions](https://docs.frame.io/docs/custom-actions) feature allows developers to integrate workflows directly into Frame.io as programmable UI components.

Custom actions are triggered by users within the app.  Once enabled on developer.frame.io, they display in the right-click dropdown menu available on any asset. In the example below, *Test* is the name of the custom action:

<p align="center"><img width="362" alt="Screen Shot 2019-10-03 at 4 54 58 PM" src="https://user-images.githubusercontent.com/19295862/66240029-3b989a00-e6b0-11e9-90fc-3d7cf91d346c.png"></p>

_If you aren't familiar with assets, read about them in the [API Guides](https://docs.frame.io/docs/uploading-assets)._

Once created, your action will be accessible from all Assets in a Project.  You can create multiple custom actions, and each action may comprise one or several interactions between Frame.io and your app.

## What can I do with the sample code?

- Present users with forms including text and selection fields.
- Add a custom action publishing a Frame.io asset to YouTube

We'll add samples to this repository over time. This is an open source resource --  your submissions are extremely welcome.

## Pre-requisites 

* [Frame.io account](https://developer.frame.io/)
* Note that you will need **Team Manager** permissions to create Custom Actions for your team.
* A valid bearer token or OAuth app token
* A Zapier account (see [example Zap](https://zapier.com/shared/e843e87f06172a4ad6ef7854e651921894c4eb44))
* Web server with a publicly accessible address - we recommend [ngrok](https://docs.frame.io/docs/how-to-setup-and-troubleshoot-ngrok-mac)
* Python 3.6+

## Configure Your Custom Action

You must configure your custom action in the [Custom Actions](https://developer.frame.io/actions/) area of developer.frame.io. Follow the instructions [here](https://docs.frame.io/docs/custom-actions#section-setup).

## Installation

```
$ pipenv shell
$ python <file_to_run.py>
```

## Troubleshooting

Make sure your ngrok or middleware port matches your app (by default the application runs on `PORT 8000`.)  If you need help getting ngrok to work, you can check out our [troubleshooting guide for ngrok](https://docs.frame.io/docs/how-to-setup-and-troubleshoot-ngrok-mac).

If the tests won't build, try running `pytest --pyargs <file_to_run>`
