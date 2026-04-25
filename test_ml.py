import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, inference, compute_model_metrics


@pytest.fixture
def sample_data():
    """Create small sample training data for testing."""
    np.random.seed(42)
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    return X, y


def test_train_model(sample_data):
    """Test that train_model returns a RandomForestClassifier."""
    X, y = sample_data
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


def test_inference(sample_data):
    """Test that inference returns predictions of the correct shape."""
    X, y = sample_data
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape == y.shape


def test_compute_model_metrics(sample_data):
    """Test that compute_model_metrics returns three float values."""
    X, y = sample_data
    model = train_model(X, y)
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(fbeta, float)