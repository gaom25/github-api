class GitHubConnectorException(Exception):
    pass


class GitHubPaymentConnectionException(GitHubConnectorException):
    pass


class GitHubPaymentException(GitHubConnectorException):
    pass


class GitHubPaymentInsufficientFundsException(GitHubConnectorException):
    pass


class GitHubLoanConnectionException(GitHubConnectorException):
    pass


class GitHubLoanException(GitHubConnectorException):
    pass


class GitHubOfferListConnectionException(GitHubConnectorException):
    pass


class GitHubOfferListException(GitHubConnectorException):
    pass


class GitHubLoanStatusConnectionException(GitHubConnectorException):
    pass


class GitHubLoanStatusException(GitHubConnectorException):
    pass
