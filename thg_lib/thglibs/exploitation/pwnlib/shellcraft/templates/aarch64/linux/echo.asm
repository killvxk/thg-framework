<% from pwnlib.shellcraft import aarch64 %>
<% from pwnlib.util import misc %>
<%page args="string, sock='1'"/>
<%docstring>
Writes a string to a file descriptor

Example:

    >>> run_assembly(shellcraft.echo('hello\n', 1)).recvline()
    b'hello\n'

</%docstring>
<%
string = misc.force_bytes(string)
%>
${aarch64.pushstr(string, append_null=False)}
${aarch64.linux.write(sock, 'sp', len(string))}
