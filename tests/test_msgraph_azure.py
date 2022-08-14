import pytest
from azure.core.exceptions import ClientAuthenticationError
from msgraph_azure.msgraph_azure import MSGraphAzure, Users


class TestMSGraphAzure:
    @pytest.mark.usefixtures("_mock_azure_login_envvars")
    def test_get_output(self):
        with pytest.raises(ClientAuthenticationError):
            MSGraphAzure().get_output("/users")


class TestUsers:
    def test_get_user_info_list(self, sample_users_list):
        user_info_list = Users().get_user_info_list(users=sample_users_list)
        assert len(user_info_list) == 3

    def test_get_test_user_list(self, sample_users_list):
        user_info_list = Users().get_user_info_list(users=sample_users_list)
        test_user_list = Users().get_test_user_list(user_info_list=user_info_list)
        assert len(test_user_list) == 2
        test_user_list[0].name == "TestUser1"
        test_user_list[1].name == "TestUser2"
