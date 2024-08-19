<h1 style="color: greenyellow">django web-socket messager</h1>
<h3 style="color: mediumpurple">the way of how to create messager-app using web-socket</h3>

# base setup
<ul>
    <li>create message app with template and render it</li>
    <li style="color: orangered">test it</li>
</ul>
<ul>
    <li>python -m pip install -U 'channels[daphne]'</li>
    <li>add "dephne" to INSTALLED_APPS as "third party app"</li>
    <li>create " core / <span style="color: chartreuse;">routing.py</span> "</li>
    <li>in core/<span style="color: chartreuse"> settings.py</span> -> <span style="color: cyan">ASGI_APPLICATION = 'core.routing.application' </span>[ remove wsgi ]</li>
    <li>create application with ProtocolTypeRouter</li>
    <li style="color: orangered">test again</li>
</ul>

# message-app
<ul>
    <li>create consumer</li>
    <li>create routing</li>
    <li>connect <span style="color: yellow"> app/consumer</span> -> <span style="color: yellow"> app/routing</span> -> <span style="color: chartreuse"> core/routing</span></li>
    
</ul>