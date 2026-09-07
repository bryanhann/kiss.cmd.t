import subprocess

from rich import print
from rich.panel import Panel

def run(line, verbose=True):
    cmds = line.split()
    print()
    _invoke = f'[bold]$ {line}'
    print(Panel(_invoke))
    result=subprocess.run(cmds, capture_output=True, text=True)
    stdout = result.stdout.strip()[:300]
    stderr = result.stderr.strip()[:300]
    status = str( result.returncode )

    _status = "[bold]exit status:[/bold]\n" + f'{status}'
    _stdout = "[bold]stdout:     [/bold]\n" + f'[green]{stdout}[/green]'
    _stderr = "[bold]stderr:     [/bold]\n" + f'[red]{stderr}[/red]'

    acc = []
    acc.append(_invoke)
    acc.append(_status)
    line = _status
    if stdout: acc.append(_stdout)
    if stderr: acc.append(_stderr)
    block = '\n'.join(acc)
    print(Panel(block)) 
    return result

def text4run(line):
    return run(line).stdout

def lines4run(line):
    lines = text4run(line).split('\n')
    if lines and lines[-1] == '':
        del lines[-1]
    return lines

def listrepos():
    lines = lines4run('gh repo list -L 9999')
    for line in lines:
         yield line.split()[0].split('/')[1]

def status( method, msg ):
    cname = method.__self__.__class__.__name__
    fname = method.__func__.__name__
    name = f'{cname}.{fname}'
    print( f'[blue]{name}(...) : {msg}[/blue]' )

def leave( method, result ):
    cname = method.__self__.__class__.__name__
    fname = method.__func__.__name__
    name = f'{cname}.{fname}'
    print( f'\n[blue]{name}(...) -> {result}[/blue]' )
    return result

def success( method, result ):
    cname = method.__self__.__class__.__name__
    fname = method.__func__.__name__
    name = f'{cname}.{fname}'
    msg = result and 'success' or 'failure'
    print( f'[blue]{name}(...) : {msg}[/blue]' )
