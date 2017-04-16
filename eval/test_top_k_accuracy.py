"""Unit tests for top_k_accuracy.py
Written by Grant Van Horn.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import random
import unittest

import numpy as np

import top_k_accuracy

def make_accuracy_data(num_classes, num_test_samples, num_correct_predictions, k):
    """Convenience method to create the labels and predictions array.
    Args:
        num_classes (int): The number of classes in the dataset.
        num_test_samples (int): The number of labels and predictions to generate.
        num_correct_predictions (int): The number of predictions that are correct.
        k (int): The number of class labels in a prediction.
    Returns:
        list : The labels.
        list : The predictions.
    """

    assert k <= num_classes, "k too big"
    assert num_correct_predictions <= num_test_samples, ""\
        "`num_correct_predictions` is larger than `num_test_samples`"

    if k == num_classes:
        assert num_test_samples == num_correct_predictions, ""\
            "`num_correct_predictions` should be equal to `num_test_samples` "\
            "when `k` equals `num_classes`"

    labels = []
    predictions = []

    class_labels = range(num_classes)

    # Determine which idexes will be correct
    if num_correct_predictions > 0:
        correct_prediction_idxs = set(random.sample(range(num_test_samples),
                                                    num_correct_predictions))
    else:
        correct_prediction_idxs = set()

    # Fill in the labels and prediction lists
    for i in range(num_test_samples):
        gt_label = random.choice(class_labels)
        labels.append(gt_label)

        preds = random.sample(class_labels, k)
        if i in correct_prediction_idxs:
            if gt_label not in preds:
                preds[0] = gt_label
        else:
            if gt_label in preds:
                preds = [p for p in preds if p != gt_label]
                preds.append(gt_label + 1 % num_classes)
        predictions.append(preds)

    return labels, predictions


class TestAccuracy(unittest.TestCase):

    def test_top_1_perfect(self):

        labels, predictions = make_accuracy_data(
            num_classes=10,
            num_test_samples=100,
            num_correct_predictions=100,
            k=1)

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with strings
        labels = map(str, labels)
        predictions = [map(str, preds) for preds in predictions]
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

    def test_top_3_perfect(self):
        labels, predictions = make_accuracy_data(
            num_classes=10,
            num_test_samples=100,
            num_correct_predictions=100,
            k=3)

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with strings
        labels = map(str, labels)
        predictions = [map(str, preds) for preds in predictions]
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

    def test_top_5_half_right(self):
        labels, predictions = make_accuracy_data(
            num_classes=10,
            num_test_samples=10,
            num_correct_predictions=5,
            k=5)

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.5)

        # Try with strings
        labels = map(str, labels)
        predictions = [map(str, preds) for preds in predictions]
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.5)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.5)

    def test_top_5_none_correct(self):

        labels, predictions = make_accuracy_data(
            num_classes=10,
            num_test_samples=100,
            num_correct_predictions=0,
            k=5)

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.)

        # Try with strings
        labels = map(str, labels)
        predictions = [map(str, preds) for preds in predictions]
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0.)

    def test_top_5_with_5_classes(self):

        labels, predictions = make_accuracy_data(
            num_classes=5,
            num_test_samples=100,
            num_correct_predictions=100,
            k=5)

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with strings
        labels = map(str, labels)
        predictions = [map(str, preds) for preds in predictions]
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 1.)

    def test_empty_labels(self):
        labels = []
        predictions = []

        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0)

        # Try with numpy
        labels = np.array(labels)
        predictions = np.array(predictions)
        accuracy = top_k_accuracy.compute_top_k_accuracy(labels, predictions)

        self.assertEqual(accuracy, 0)

    @unittest.expectedFailure
    def test_unmatched_lengths(self):

        labels, predictions = make_accuracy_data(
            num_classes=10,
            num_test_samples=100,
            num_correct_predictions=0,
            k=3)
        # add one extra prediction to the prediction matrix
        predictions.append([0, 1, 2])

        # Should throw an Exception
        top_k_accuracy.compute_top_k_accuracy(labels, predictions)

def make_csv_file(output_path, field_names, row_data):
    """Write the data to a csv file.
    Args:
        output_path (str) : File path to write the csv file.
        field_names [str] : The column field names.
        prediction_data ([{}] : A list of dict containing the field names.
    """
    with open(output_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for data in row_data:
            writer.writerow(data)

def make_submission_file(output_path, submission_data):
    """Create a submission csv file.
    Args:
        output_path (str) : File path to write the csv file.
        submission_data [{}] : A list of dicts containing values for the keys
            "image_id" and "preditions".
    """
    make_csv_file(output_path, field_names=["image_id", "predictions"],
                  row_data=submission_data)

def make_solution_file(output_path, solution_data):
    """Create a solution csv file.
    Args:
        output_path (str) : File path to write the csv file.
        solution_data [{}] : A list of dicts containing values for the keys
            "image_id", "truth" and "usage".
    """
    make_csv_file(output_path, field_names=["image_id", "truth", "usage"],
                  row_data=solution_data)

def make_submission_entry(image_id, predictions):
    """Convenience function to create a prediction dictionary that can be
        written to a csv file.
    Args:
        image_id : The image id.
        predictions [] : A list of predictions.
    Returns:
        {} : A dict that can be used by a csv.DictWriter to write the data.
    """

    predictions_str = " ".join(map(str, predictions))
    return {
        "image_id" : image_id,
        "predictions" : predictions_str
    }

def make_submission_files(num_classes, k, num_public_samples,
                          num_correct_public_predictions, num_private_samples,
                          num_correct_private_samples):
    """Convenience method to create the submission and solution csv files.
    Args:
        num_classes (int): The number of classes in the dataset.
        k (int): The number of predictions to consider.
        num_public_samples (int): The number of "Public" samples.
        num_correct_public_predictions (int): The number of "Public" samples
            the user gets correct.
        num_private_samples (int): The number of "Private" samples.
        num_correct_private_samples (int): The number of "Private" samples the
            user gets correct.
    Returns:
        str: A file path to a submission file.
        str: A file path to a solution file.
    """
    public_labels, public_predictions = make_accuracy_data(
        num_classes=num_classes,
        num_test_samples=num_public_samples,
        num_correct_predictions=num_correct_public_predictions,
        k=k)

    private_labels, private_predictions = make_accuracy_data(
        num_classes=num_classes,
        num_test_samples=num_private_samples,
        num_correct_predictions=num_correct_private_samples,
        k=k)

    solution_data = []
    for i, label in enumerate(public_labels):
        solution_data.append({
            "image_id" : i,
            "truth" : label,
            "usage" : "Public"
        })
    for i, label in enumerate(private_labels):
        solution_data.append({
            "image_id" : i + num_public_samples,
            "truth" : label,
            "usage" : "Private"
        })

    submission_data = []
    for i, preds in enumerate(public_predictions + private_predictions):
        image_id = i
        submission_data.append(make_submission_entry(image_id, preds))

    submission_fp = '/tmp/submission_file.txt'
    make_submission_file(submission_fp, submission_data)

    solution_fp = '/tmp/solution_file.txt'
    make_solution_file(solution_fp, solution_data)

    return submission_fp, solution_fp

class TestSubmissions(unittest.TestCase):

    def test_top_1_perfect(self):
        k = 1
        submission_fp, solution_fp = make_submission_files(
            num_classes=10,
            k=k,
            num_public_samples=100,
            num_correct_public_predictions=100,
            num_private_samples=100,
            num_correct_private_samples=100)

        public_acc, private_acc = top_k_accuracy.evaluate(submission_fp,
                                                          solution_fp, k=k)

        self.assertEqual(public_acc, 1.)
        self.assertEqual(private_acc, 1.)

    def test_top_3_perfect(self):

        k = 3
        submission_fp, solution_fp = make_submission_files(
            num_classes=10,
            k=k,
            num_public_samples=100,
            num_correct_public_predictions=100,
            num_private_samples=100,
            num_correct_private_samples=100)

        public_acc, private_acc = top_k_accuracy.evaluate(submission_fp,
                                                          solution_fp, k=k)

        self.assertEqual(public_acc, 1.)
        self.assertEqual(private_acc, 1.)

    def test_top_5_half_right(self):

        k = 5
        submission_fp, solution_fp = make_submission_files(
            num_classes=10,
            k=k,
            num_public_samples=100,
            num_correct_public_predictions=50,
            num_private_samples=100,
            num_correct_private_samples=50)

        public_acc, private_acc = top_k_accuracy.evaluate(submission_fp,
                                                          solution_fp, k=k)

        self.assertEqual(public_acc, 0.5)
        self.assertEqual(private_acc, 0.5)

    def test_top_5_none_right(self):

        k = 5
        submission_fp, solution_fp = make_submission_files(
            num_classes=10,
            k=k,
            num_public_samples=100,
            num_correct_public_predictions=0,
            num_private_samples=100,
            num_correct_private_samples=0)

        public_acc, private_acc = top_k_accuracy.evaluate(submission_fp,
                                                          solution_fp, k=k)

        self.assertEqual(public_acc, 0.)
        self.assertEqual(private_acc, 0.)

if __name__ == '__main__':
    unittest.main()
