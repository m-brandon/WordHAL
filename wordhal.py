import click


version = 0.1


@click.group()
def wordhal():
    click.echo(f"WordHAL v{version}")


if __name__ == "__main__":
    wordhal()
