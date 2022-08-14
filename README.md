![pytest](https://github.com/prabhuwk/msgraph-azure-users/actions/workflows/test.yml/badge.svg)
![docker build](https://github.com/prabhuwk/msgraph-azure-users/actions/workflows/build.yml/badge.svg)


# msgraph-azure-users

In this we are going to

Find list of users from Azure AD using Microsoft Graph API and use dataclass to represent UserInfo object.
```shell
$ msgraph-azure users --list
Getting list of azure users
[UserInfo(name='Regular User', test_user=False), UserInfo(name='TestUser1', test_user=True), UserInfo(name='TestUser2', test_user=True)]
```

Find list of test users obtained from previous command. TestUser are seggregated based on flag set in  UserInfo dataclass.
```shell
$ msgraph-azure users --list-test-users
Getting list of azure test users
[UserInfo(name='TestUser1', test_user=True), UserInfo(name='TestUser2', test_user=True)]
```

Create `msgraph-azure-users` Docker Image using [Github Actions](https://docs.github.com/en/actions).


Run tests using [pytest](https://docs.pytest.org/en/7.1.x/contents.html).
```shell
$ pytest tests
======================== test session starts ========================
platform darwin -- Python 3.10.6, pytest-7.1.2, pluggy-1.0.0
rootdir: /msgraph-azure-users
collected 3 items

tests/test_msgraph_azure.py ...                                [100%]

======================== 3 passed in 0.50s ==========================
```
