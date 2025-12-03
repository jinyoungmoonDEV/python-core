# Database Settings
DATABASES = {
    'default': {
        # MongoDB Example
        # 'host': '<host>',
        # 'port': 27017,
        # 'db': '<db>',
        # 'username': '<user>',
        # 'password': '<password>'
    }
}

# Cache Settings
CACHES = {
    'default': {
        # Redis Example
        # 'host': '<host>',
        # 'port': 6379,
        # 'db': 0
    }
}

# Handler Configuration
HANDLERS = {
    'authentication': [
        # Default Authentication Handler
        # {
        #     'backend': 'spaceone.core.handler.authentication_handler:AuthenticationGRPCHandler',
        #     'uri': 'grpc://identity:50051/v1/Domain/get_public_key'
        # }
    ],
    'authorization': [
        # Default Authorization Handler
        # {
        #     'backend': 'spaceone.core.handler.authorization_handler:AuthorizationGRPCHandler',
        #     'uri': 'grpc://identity:50051/v1/Authorization/verify'
        # }
    ],
    'mutation': [],
    'event': []
}

# Connector Settings
CONNECTORS = {}

# gRPC Client Default Settings
GRPC_DEFAULT_TIMEOUT = 180  # seconds
GRPC_DEFAULT_MAX_RETRIES = 2

# gRPC Method Retry and Timeout Configuration
# 특정 resource.verb 조합에 대한 timeout과 retry 설정
# 예시:
# GRPC_METHOD_CONFIG = {
#     "Domain.list": {
#         "timeout": 60,
#         "max_retries": 5
#     },
#     "Job.get": {
#         "timeout": 300,
#         "max_retries": 1
#     }
# }
GRPC_METHOD_CONFIG = {}

# Log Settings
LOG = {
    # 'loggers': {
    #     '<package>': {
    #         'level': 'DEBUG',
    #         'handlers': ['console']
    #     }
    # },
    # 'filters': {
    #     'masking': {
    #         'rules': {
    #             'HelloWorld.say_hello': [
    #                 'name'
    #             ]
    #         }
    #     }
    # }
}
