from project.topic import Topic
from project.category import Category
from project.document import Document
from typing import List


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    @staticmethod
    def find_object_by_id(object_id, array):
        for obj in array:
            if obj.id == object_id:
                return obj

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name: str) -> None:
        category = self.find_object_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.find_object_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.find_object_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id: int) -> None:
        category = self.find_object_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = self.find_object_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = self.find_object_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id) -> None:
        document = self.find_object_by_id(document_id, self.documents)
        return document.__repr__()

    def __repr__(self):
        result = [document.__repr__() for document in self.documents]

        return '\n'.join(result)