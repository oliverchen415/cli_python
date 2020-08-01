import click

@click.command()
@click.option('-c', '--count', default=1, help='number of greetings')
@click.argument('name', default='guest')
def hello(count, name):
    for x in range(count):
        click.echo(f'Hello {name}!')

if __name__ == "__main__":
    hello()