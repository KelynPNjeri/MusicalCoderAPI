"""This is the configuartion module that contains all the configurarions for the api."""
class Config:
    """Configurations"""
    DEBUG = False
class DevelopmentConfig(Config):
    """Configurations for Development Phase."""  
    DEBUG = True
class TestingConfig(Config):
    """Configurations for Testing Phase."""
    DEBUG = True
    TESTING = True
class ProductionConfig(Config):
    """Configurations for Production Phase."""
    DEBUG = False
    TESTING = False
APP_CONFIG = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
