#!c:\users\kanik\lambda-serverless-py\tutorial-env\scripts\python.exe
# -*- coding: utf-8 -*-
import logging
import os

import click

import aws_lambda

CURRENT_DIR = os.getcwd()

logging.getLogger("pip").setLevel(logging.CRITICAL)


@click.group()
def cli():
    pass


@click.command(help="Create a new function for Lambda.")
@click.option(
    "--minimal",
    default=False,
    is_flag=True,
    help="Exclude any unnecessary template files",
)
@click.argument(
    "folder", nargs=-1, type=click.Path(file_okay=False, writable=True),
)
def init(folder, minimal):
    path = CURRENT_DIR
    if len(folder) > 0:
        path = os.path.join(CURRENT_DIR, *folder)
        if not os.path.exists(path):
            os.makedirs(path)
    aws_lambda.init(path, minimal=minimal)


@click.command(help="Bundles package for deployment.")
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option(
    "--requirements",
    default=None,
    type=click.Path(),
    help="Install packages from supplied requirements file.",
)
@click.option(
    "--local-package",
    default=None,
    type=click.Path(),
    help="Install local package as well.",
    multiple=True,
)
def build(requirements, local_package, config_file, profile):
    aws_lambda.build(
        CURRENT_DIR,
        requirements=requirements,
        local_package=local_package,
        config_file=config_file,
        profile_name=profile,
    )


@click.command(help="Run a local test of your function.")
@click.option(
    "--event-file", default="event.json", help="Alternate event file.",
)
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option("--verbose", "-v", is_flag=True)
def invoke(event_file, config_file, profile, verbose):
    aws_lambda.invoke(
        CURRENT_DIR,
        event_file=event_file,
        config_file=config_file,
        profile_name=profile,
        verbose=verbose,
    )


@click.command(help="Register and deploy your code to lambda.")
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option(
    "--requirements",
    default=None,
    type=click.Path(),
    help="Install all packages defined in supplied requirements file",
)
@click.option(
    "--local-package",
    default=None,
    type=click.Path(),
    help="Install local package as well.",
    multiple=True,
)
@click.option(
    "--preserve-vpc",
    default=False,
    is_flag=True,
    help="Preserve VPC configuration on existing functions",
)
def deploy(requirements, local_package, config_file, profile, preserve_vpc):
    aws_lambda.deploy(
        CURRENT_DIR,
        requirements=requirements,
        local_package=local_package,
        config_file=config_file,
        profile_name=profile,
        preserve_vpc=preserve_vpc,
    )


@click.command(help="Upload your lambda to S3.")
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option(
    "--requirements",
    default=None,
    type=click.Path(),
    help="Install all packages defined in supplied requirements file",
)
@click.option(
    "--local-package",
    default=None,
    type=click.Path(),
    help="Install local package as well.",
    multiple=True,
)
def upload(requirements, local_package, config_file, profile):
    aws_lambda.upload(
        CURRENT_DIR,
        requirements=requirements,
        local_package=local_package,
        config_file=config_file,
        profile_name=profile,
    )


@click.command(help="Deploy your lambda via S3.")
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option(
    "--requirements",
    default=None,
    type=click.Path(),
    help="Install all packages defined in supplied requirements file",
)
@click.option(
    "--local-package",
    default=None,
    type=click.Path(),
    multiple=True,
    help="Install local package as well.",
)
def deploy_s3(requirements, local_package, config_file, profile):
    aws_lambda.deploy_s3(
        CURRENT_DIR,
        requirements=requirements,
        local_package=local_package,
        config_file=config_file,
        profile_name=profile,
    )


@click.command(help="Delete old versions of your functions")
@click.option(
    "--config-file", default="config.yaml", help="Alternate config file.",
)
@click.option(
    "--profile", help="AWS profile to use.",
)
@click.option(
    "--keep-last",
    type=int,
    prompt="Please enter the number of recent versions to keep",
)
def cleanup(keep_last, config_file, profile):
    aws_lambda.cleanup_old_versions(
        CURRENT_DIR, keep_last, config_file=config_file, profile_name=profile,
    )


if __name__ == "__main__":
    cli.add_command(init)
    cli.add_command(invoke)
    cli.add_command(deploy)
    cli.add_command(upload)
    cli.add_command(deploy_s3)
    cli.add_command(build)
    cli.add_command(cleanup)
    cli()
