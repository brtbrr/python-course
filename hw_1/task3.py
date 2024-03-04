import click
import sys

@click.command()
@click.argument('filenames', nargs=-1, type=click.Path(exists=True))
def task3(filenames):
    if not filenames:
        text = sys.stdin.read()
        lines = text.count('\n') + 1
        words = len(text.split())
        bytes_count = len(text.encode('utf-8'))
        click.echo(f"{lines}\t{words}\t{bytes_count}")
    else:
        total_lines = 0
        total_words = 0
        total_bytes = 0
        
        for filename in filenames:
            lines = 0
            words = 0
            bytes_count = 0
            
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    lines += 1
                    words += len(line.split())
                    bytes_count += len(line.encode('utf-8'))
                    
            total_lines += lines
            total_words += words
            total_bytes += bytes_count
            
            click.echo(f"{lines}\t{words}\t{bytes_count}\t{filename}")
        
        if len(filenames) > 1:
            click.echo(f"{total_lines}\t{total_words}\t{total_bytes}\ttotal")

task3()
