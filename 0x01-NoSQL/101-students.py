#!/usr/bin/env python3
"""Update and sort student scores in MongoDB."""

from pymongo import MongoClient


def get_student(mongo_collection):
    """Retrieve all student documents from the collection.

    Args:
        mongo_collection: The MongoDB collection object.

    Returns:
        A cursor to the documents in the collection.
    """
    return mongo_collection.find()


def get_score(student):
    """Calculate the average score of a student.

    Args:
        student: The student document.

    Returns:
        The average score of the student.
    """
    topics = student["topics"]
    average = sum(topic["score"] for topic in topics) / len(topics)
    return average


def top_students(mongo_collection):
    """Update each student with their average score and sort by score.

    Args:
        mongo_collection: The MongoDB collection object.

    Returns:
        A cursor to the sorted student documents.
    """
    students = get_student(mongo_collection)
    for student in students:
        average_score = get_score(student)
        mongo_collection.update_one(
            {"_id": student["_id"]},
            {"$set": {"averageScore": average_score}}
        )

    sorted_students = mongo_collection.find().sort("averageScore", -1)
    return sorted_students
