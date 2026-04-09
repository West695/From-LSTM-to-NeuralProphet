# From LSTM to NeuralProphet

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
This project aims to demonstrate the transition from LSTM (Long Short-Term Memory) models to NeuralProphet for time series forecasting. NeuralProphet leverages the benefits of Facebook's Prophet and integrates deep learning techniques to provide enhanced predictions.

## Features
- Easy-to-use API
- High performance and scalable for large datasets
- Supports custom seasonalities and holidays
- Built-in plotting for visualizing predictions and training results

## Installation
To install the project, clone the repository and install the dependencies:

```bash
git clone https://github.com/West695/From-LSTM-to-NeuralProphet.git
cd From-LSTM-to-NeuralProphet
pip install -r requirements.txt
```

## Usage
Here's how to use the software:

1. **Prepare your dataset**: Make sure your data is in the correct format (date and value columns).
2. **Train the model**:
    ```python
    from your_module import train_neural_prophet
    train_neural_prophet(data)
    ```
3. **Make predictions**:
    ```python
    from your_module import make_predictions
    predictions = make_predictions(future_data)
    ```
4. **Visualize results**:
    ```python
    from your_module import plot_results
    plot_results(predictions)
    ```

## Examples
Refer to the `examples/` directory for Jupyter notebooks demonstrating various use cases of this project.

## Contributing
Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) for more details on how to get started.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements
- [PyTorch](https://pytorch.org/)
- [NeuralProphet](https://github.com/ourownstory/neuralprophet)
- [Facebook Prophet](https://facebook.github.io/prophet/)