"""Top-k accuracy metric.

This module implements the top-k accuracy metric. Given a ground truth
label and a list of predictions (sorted by confidence) for each sample,
the pseudo code is:

score = 0
for each sample
    gt = ground truth label of sample
    preds = predictions for sample
    if gt in preds[:k]
        score +=1
accuracy = score / number of samples

This module can compute the top-k accuracy metric given two csv files: a
submission file and a solution file. The submission file should have the
format:

    image_id, predictions
    12345.jpg, label1 label2 label3 label4 label5

And the solution file format should be:

    image_id, truth, usage
    12345.jpg, label2, Public

You can then do:
    public_acc, private_acc = evaluate(submission_file, solution_file, k)

Written by Grant Van Horn.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv

import numpy as np

def read_submission_file(submission_file, k):
    """
    Args:
        submission_file (str): Path to a csv submission file, whose format is:
            image_id, predictions
            12345.jpg, label1 label2 label3 label4 label5
        k (int) : Consider the top k predictions.
    Returns:
        [] : A list of image ids.
        np.array([-1, k], dtype=np.object) : Each row contains the k
            predictions for the corresponding entry in the image id array
    Raises:
        ValueError : if a row in the `submission_file` has less than k
            predictions.
    """
    image_ids = []
    predictions = []
    with open(submission_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            image_id = row['image_id']
            preds = row['predictions']

            preds = preds.strip().split(' ')
            if len(preds) < k:
                raise ValueError("Image %s in submission file %s contains "\
                                 "%d predictions when k=%d." % (
                                     image_id, submission_file, len(preds), k))
            preds = preds[:k]

            image_ids.append(image_id)
            predictions.append(preds)

    predictions = np.array(predictions, dtype=np.object)
    return image_ids, predictions

def read_solution_file(solution_file):
    """
    Args:
        solution_file (str): Path to a csv solution file, whose format is:
            image_id, truth, usage
            12345.jpg, label2, Public
    Returns:
        {image_id : truth} : A dict mapping image ids to their true label for
            the public set.
        {image_id : truth} : A dict mapping image ids to their true label for
            the private set.
    Raises:
        ValueError : if usage is not "Public" or "Private"
    """

    public_data = {}
    private_data = {}

    with open(solution_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_id = row['image_id']
            true_label = row['truth']
            usage = row['usage']

            if usage == 'Public':
                public_data[image_id] = true_label
            elif usage == 'Private':
                private_data[image_id] = true_label
            else:
                raise ValueError("Image %s in solution file %s contains "\
                                 "an unknown usage %s" % (
                                     image_id, solution_file, usage))

    return public_data, private_data

def compute_top_k_accuracy(labels, predictions):
    """Compute the accuracy of the `predictions` using `labels` as ground
        truth.
    Args:
        labels: An iterable of ground truth labels.
        predictions: A matrix where each row contains k label predictions. The
            true label is in the corresponding entry of `labels`.
    Returns:
        float: The accuracy.
    Raises:
        ValueError: If number of `labels` does not equal the number of rows in
            `predictions`.
    """

    num_samples = len(labels)

    if num_samples == 0:
        return 0.

    if num_samples != len(predictions):
        raise ValueError("`labels` and `predictions` must have the same "\
                         "number of entries")

    num_correct = 0
    for i in range(num_samples):
        if labels[i] in predictions[i]:
            num_correct += 1
    return num_correct / (1. * num_samples)

def evaluate(submission_file, solution_file, k):
    """Evaluate the top `k` accuracy of the `submission_file` using the
        `solution_file` as ground truth.
    Args:
        submission_file (str): Path to a csv submission file, whose format
            should be:
                image_id, predictions
                12345.jpg, label1 label2 label3 label4 label5
        solution_file (str): Path to a csv solution file, whose format should
            be:
                image_id, truth, usage
                12345.jpg, label2, Public
        k (int): Compute accuracy for the top k predictions.
    Returns:
        float: Accuracy at k for the public split.
        float: Accuracy at k for the private split.
    Raise:
        ValueError : If `k` is less than 1.
        ValueError : If image ids from the `solution_file` are not found in
            the `submission_file`.
    """

    if k < 1:
        raise ValueError("Bad value for k %d" % (k,))

    # Load in the submission data
    submission_image_ids, submission_predictions = read_submission_file(
        submission_file, k)

    # Load in teh solution data
    public_image_data, private_image_data = read_solution_file(solution_file)
    public_image_ids = set(public_image_data.keys())
    private_image_ids = set(private_image_data.keys())

    # Check to see if the submission file contains all solution image ids
    all_solution_image_ids = public_image_ids.union(private_image_ids)
    missing_submission_ids = all_solution_image_ids.difference(
        submission_image_ids)
    num_missing_submission_ids = len(missing_submission_ids)
    if num_missing_submission_ids > 0:
        raise ValueError("Submission file %s is missing %d image ids that "\
                         "were found in the solution file %s" % (
                             submission_file, num_missing_submission_ids,
                             solution_file)
                        )

    # Split the submission data into public and private sets
    public_submission_predictions_idxs = []
    public_submission_labels = []
    private_submission_predictions_idxs = []
    private_submission_labels = []

    for idx, image_id in enumerate(submission_image_ids):
        if image_id in public_image_ids:
            public_submission_predictions_idxs.append(idx)
            label = public_image_data[image_id]
            public_submission_labels.append(label)
        elif image_id in private_image_ids:
            private_submission_predictions_idxs.append(idx)
            label = private_image_data[image_id]
            private_submission_labels.append(label)
        else:
            # ignore image ids that are not in the solution file
            pass

    # Separate the public predictions from the private predictions
    public_submission_predictions = submission_predictions[
        public_submission_predictions_idxs]
    private_submission_predictions = submission_predictions[
        private_submission_predictions_idxs]

    # Compute the accuracies
    public_accuracy = compute_top_k_accuracy(public_submission_labels,
                                             public_submission_predictions)
    private_accuracy = compute_top_k_accuracy(private_submission_labels,
                                              private_submission_predictions)

    return public_accuracy, private_accuracy
