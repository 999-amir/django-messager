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

# HTMX
