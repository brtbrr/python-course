import sys
import click

@click.command()
@click.argument("files", nargs=-1, type=click.Path())
def task2(files):
    def tail(file):
        with open(file, 'r') as f:
            lines = f.readlines()
            last_lines = lines[-10:]
            return last_lines

    if not files:
        lines = []
        try:
            while True:
                line = input()
                if line.strip() == "":
                    break
                lines.append(line)
        except EOFError:
            pass 

        last_lines = lines[-17:]
        sys.stdout.write(''.join(last_lines))
    else:
        for file in files:
            if len(files) > 1:
                sys.stdout.write('==> ' + file + ' <==\n')
            last_lines = tail(file)
            sys.stdout.write(''.join(last_lines))
                 
task2()