<h1>DJANGO + HTMX + WEBSOCKET</h1>
<h5>this is the messager app with online chat in groups [ first project ]</h5>

# DJANGO

<p>django-project without any asynchronous task. here some detail about apps</p>
<ul>
    <li>app - account
        <ul>
            <li>CostumeUser:
                <p>- registration with name and password</p>
                <p>- name is defined as username ( evaluated to be unique )</p>
                <p>- signup and login is in one page ( view ) so there is no confirm-password</p>
                <p>- each user have random color in chat (saved in db)</p>
            </li>
        </ul>
    </li>
    <br>
    <li>app - message
        <ul>
            <li>Group:
                <p>- each group contain their users with ManyToManyField</p>
                <p>- after registration user will send to group page</p>
                <p>- in group page user will see the groups that admin make permission for user</p>
            </li>
            <li>Message
                <p>- after user select it group, user will send to message-page</p>
                <p>- in message-page there is all previous messages that each user have their own color</p>
                <p>- message-page will restrict user that have no permission for group or unauthenticated</p>
                <p>- each message is unique by group and user</p>
            </li>
        </ul>
    </li>
</ul>
<img src="diagram.png" alt="diagram image">

# HTMX (example)
<h5>road:</h5>
<ul>
    <li>message.html -----request----> hx-post ---> MessageView / post -----context----> chat-message.html ---> DONE_1</li>
    <li>- - - > hx-target ---> [ find tag ] ---> DONE_2</li>
    <li>- - - > hx-swap ---> [ add {DONE_1} to {DONE_2} ] ---> FINISHED</li>
</ul>
<h5>files-directory:</h5>

``` files-directory
    message
       |------ views.py
       |------ templates
                   |------ message.html
                   |------ snippet
                             |------ chat-message.html
```
<br>
<p>at the first get script-cdn from their website</p>
<h5>message.html</h5>

```html
{% for chat in chats %}
    <p id="htmx-chat"
       class="text-{{ chat.user.color }}-500 my-1">{{ chat.user.username }}] {{ chat.message }}</p>
{% endfor %}

<form method="post" hx-post="{% url 'message:chat' group_name %}" hx-target="#htmx-chat"
      hx-swap="beforebegin">{% csrf_token %}
    <input name="message">
    <button type="submit">submit</button>
</form>
```
<h5>chat-message.html</h5>

```html
<p id="htmx-chat">{{ chat.user.username }}] {{ chat.message }}</p>
```
<h5>views.py</h5>

```python
from django.shortcuts import render
from django.views import View
from .models import MessageModel, GroupModel
from .forms import MessageForm
from django.shortcuts import get_object_or_404


class MessageView(View):
    form_class = MessageForm

    # def dispatch ...

    # def get...

    def post(self, request, group_name):
        form = self.form_class(request.POST)
        if form.is_valid():
            chat = MessageModel.objects.create(user=request.user, group=get_object_or_404(GroupModel, name=group_name),
                                               message=form.cleaned_data['message'])
            return render(request, 'message/htmx/chat-message.html', {'chat': chat})
```

# HYPERSCRIPT (example)
<h5>to reset form after htmx-request</h5>
<ul>
    <li>at the first get script-cdn from their website</li>
    <li>add this to previous form tag</li>
</ul>

```html
    <form ... _="on htmx:afterRequest reset() me">...</form>
```

# WEBSOCKET
<h5>what is websocket</h5>
<p>A WebSocket is a communication protocol that provides full-duplex communication channels over a single, long-lived connection between a client (like a web browser) and a server. Unlike the traditional HTTP request/response model, WebSocket allows for interactive communication between the client and the server with minimal overhead, making it ideal for applications that require real-time updates.</p>

<img style="margin: 0 20%" src="https://www-uploads.scaleway.com/blog-websockets-bigger-4.webp" width="400">

<h5>first setup</h5>
<ul>
    <li>install channels["daphne"]</li>
    <li>add DNS of htmx-ws to html</li>
    <li>added to INSTALLED_APPS</li>
    <li>change from wsgi to asgi</li>
    <li>link core/asgi.py to app/routing.py</li>
    <li>link app/routing.py to app/consumer.py
        <ul>
            <li>consumer is similar with views.py with more features like connect, disconnect, receive</li>
        </ul>
    </li>
</ul>

<h5>how it work</h5>
<ul>
    <li>when user open the page we use [ connect-function ] to add user to the specific channel-layer</li>
    <li>and also if user close the page we use [ disconnect-function ] to remove user from our specific channel-layer</li>
    <li>if user send request to page, we will send it to [ receive-function ] using HTMX</li>
    <li>after that we can get request-data to processing level and after that send response to the new html file to add or edit our previous page with HTMX using [ hx-swap-oob ]</li>
</ul>

