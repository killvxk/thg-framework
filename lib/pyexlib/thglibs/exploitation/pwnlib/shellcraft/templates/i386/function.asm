<%
    from pwnlib.shellcraft import i386
%>
<%docstring>
Converts a shellcraft template into a callable function.

Arguments:
    name(str):
        Name of the function.
    template_sz(str, callable):
        Rendered shellcode template.  Any variable Arguments
        should be supplied as registers.
    registers(list):
        List of registers which should be filled from the stack.

::

    >>> shellcode = ''
    >>> shellcode += shellcraft.function('write', shellcraft.i386.linux.write, 'eax', 'ebx', 'ecx')

    >>> hello = shellcraft.i386.linux.echo("Hello!", 'eax')
    >>> hello_fn = shellcraft.i386.function('hello', hello, 'eax').strip()
    >>> exit = shellcraft.i386.linux.exit('edi')
    >>> exit_fn = shellcraft.i386.function('exit', exit, 'edi').strip()
    >>> shellcode = '''
    ...     push STDOUT_FILENO
    ...     call hello
    ...     push 33
    ...     call exit
    ... %(hello_fn)s
    ... %(exit_fn)s
    ... ''' % (locals())
    >>> p = run_assembly(shellcode)
    >>> p.recvall()
    b'Hello!'
    >>> p.wait_for_close()
    >>> p.poll()
    33

Notes:

    Can only be used on a shellcraft template which takes
    all of its arguments as registers.  For example, the
    pushstr
</%docstring>
<%page args="name, template_function, *registers"/>
<%
    ifdef = '_%s_' % name
%>
/* ${name}(${', '.join(registers)}) */
#ifndef ${ifdef}
#define ${ifdef}
${name}:
    /* Save stack */
    ${i386.prolog()}
    /* Load arguments */
% for i, reg in enumerate(registers):
    ${i386.stackarg(i, reg)}
% endfor

% if isinstance(template_function, str):
    ${template_function}
% else:
    ${template_function(*registers)}
% endif

    /* Restore stack */
    ${i386.epilog(len(registers))}
#endif /* ${ifdef} */
