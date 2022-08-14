from dataclasses import dataclass, field
import os
from azure.core.exceptions import ClientAuthenticationError
from azure.identity._credentials import ClientSecretCredential
from msgraph.core import GraphClient
from typing import List


class MSGraphAzure:
    def __init__(self) -> None:
        self._client = self._graph_client()
        self._output = []

    def _credential(self) -> ClientSecretCredential:
        return ClientSecretCredential(
            tenant_id=os.environ.get("TENANT_ID"),
            client_id=os.environ.get("CLIENT_ID"),
            client_secret=os.environ.get("CLIENT_SECRET"),
        )

    def _graph_client(self) -> GraphClient:
        credential = self._credential()
        return GraphClient(credential=credential)

    def get_output(self, request_url) -> list:
        try:
            result = self._client.get(request_url)
            value = result.json().get("value")
            self._output.extend(value)
        except ClientAuthenticationError:
            raise ClientAuthenticationError(
                "Unable to Authenticate with provided client credentials."
            )
        return self._output


@dataclass(slots=True)
class UserInfo:
    name: str
    test_user: bool = field(init=False)

    def _set_test_user_flag(self) -> None:
        self.test_user = True if "TestUser" in self.name else False

    def __post_init__(self) -> None:
        self._set_test_user_flag()


class Users:
    def __init__(self) -> None:
        self._list = None

    @property
    def list(self) -> List[UserInfo]:
        users = MSGraphAzure().get_output("/users")
        return self.get_user_info_list(users)

    def get_user_info_list(self, users) -> List[UserInfo]:
        user_info_list = []
        for user in users:
            user_info_list.append(UserInfo(name=user.get("displayName")))
        return user_info_list

    def get_test_user_list(self, user_info_list: list) -> List[UserInfo]:
        return [user for user in user_info_list if user.test_user]
