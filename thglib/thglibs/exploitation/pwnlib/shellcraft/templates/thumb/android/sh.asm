<% from pwnlib.shellcraft import thumb %>
<%docstring>
Execute a different process.
</%docstring>
${thumb.linux.execve('/system/bin//sh', ['sh'], 0)}
