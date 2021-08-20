def before_all(context):
    env = context.config.userdata.get('TEST_ENV')  # behave user data example
    # print("*** Before all")
    # print(env)


def before_feature(context, feature):
    pass
    # print("*** Before feature: %s" % feature)


def before_scenario(context, scenario):
    """
        Burada senaryodaki tagler taranarak daha test başlamadan senaryoyu skip edebiliriz.
        Örneğin skip tag'i atanmış bir senaryo varsa aşağıdaki koda göre otomatik skip edilecektir.
        Farklı tagler ile örnekler çoğaltılabilir. (bug vs)
    """
    if "skip" in scenario.effective_tags:
        scenario.skip("OOPS: This scenario is not suitable for running.")
        return


def before_step(context, step):
    # print("*** Before step: %s" % step)
    pass


def after_all(context):
    pass
    # print("*** After all")


def after_feature(context, feature):
    pass
    # print("*** After feature")


def after_scenario(context, scenario):
    pass


def after_step(context, step):
    # print("*** After step")
    pass
