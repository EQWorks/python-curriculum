import json


class ItemPipeline:

    data = []

    def close_spider(self, spider):
        with open('./universities.json', 'w') as f:
            json.dump(self.data, f)

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item
