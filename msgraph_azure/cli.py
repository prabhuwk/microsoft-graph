import click
from click_plugins import with_plugins
from pkg_resources import iter_entry_points
from msgraph_azure.msgraph_azure import Users


@with_plugins(iter_entry_points("azure.plugins"))
@click.group("msgraph-azure")
def azure():
    """Entry point for azure commands."""


@azure.command("users")
@click.option("--list", "-l", help="List Users", is_flag=True)
@click.option("--list-test-users", "-t", help="List Test Users", is_flag=True)
def list_users(list: bool, list_test_users: bool):
    """List Azure users"""
    if list:
        click.secho("Getting list of azure users")
        users = Users().list
        click.secho(users)
    if list_test_users:
        click.secho("Getting list of azure test users")
        users = Users().list
        test_users = Users().get_test_user_list(users)
        click.secho(test_users)
