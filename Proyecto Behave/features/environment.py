from behave import *


def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()


def after_all(context):
    print("se terminó")
