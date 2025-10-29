from services.general.base_helper import BaseHelper


class GroupsHelper(BaseHelper):
    ENDPOINT_PREFIX = '/groups'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GROUP_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{group_id}}/'

    def post_create_group(self, json=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            json=json
        )
        return res

    def get_groups(self):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT
        )
        return res

    def delete_groups(self, index_group: str):
        res = self.api_utils.delete(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=index_group)
        )
        return res

    def get_group(self, index_group: str):
        res = self.api_utils.get(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=index_group)
        )
        return res

    def put_group(self, index_group: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=index_group),
            json=json
        )
        return res



