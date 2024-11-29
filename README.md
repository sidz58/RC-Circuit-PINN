# RC-Circuit-PINN

# Basic Implementation of PINN: RC Circuit

**Author**: Siddh Singhal  
**Roll Number**: 23115142  
**Email**: siddh_s@ee.iitr.ac.in  

---

## Introduction

In this implementation, we explore the use of **Physics-Informed Neural Networks (PINNs)** to model and predict the voltage across a capacitor in a simple electrical circuit. Unlike traditional neural networks that rely purely on data, PINNs incorporate known physical laws, such as differential equations, to enhance learning. 

This integration of both data and physics enables more accurate predictions, even with limited data. The main goal was to understand the working of a PINN by applying it to an RC circuit, where the voltage across the capacitor is governed by a first-order differential equation. Along the way, I learned to use various supporting libraries, such as **GEKKO** and **HyperOpt**, and how to design a flexible pipeline according to different requirements.

---

## Workflow

1. **Formation of Differential Equation**: Pen-and-paper derivation.
2. **Solve ODE Using Python**: GEKKO framework.
   - Define initial conditions and values for R, C.
   - Create a flexible pulse-wave function in Python.
3. **Ground Truth Generation**:
   - Use GEKKO to generate solutions.
4. **Model Design**:
   - Fully connected network with flexible inputs, depth, and number of nodes.
5. **Hyperparameter Optimization**:
   - Use Bayesian optimization with **HyperOpt**.
   - Optimize weights of individual losses, model architecture, learning rate, and number of training steps.
6. **Training the Model**:
   - Define PINN loss function: Boundary loss and physics loss.
7. **Model Saving**:
   - Save the trained model and the best parameters.

---

## Demonstration

### Visualizations
1. **Input and Ground Truth**:
   - **Green Plot**: Custom pulse wave voltage input with variable rise/fall rate, delay, amplitude, and periodicity.
   - **Blue Plot**: Voltage across the capacitor (ground truth) for charging/discharging cycles (solved using GEKKO).
   ![image](https://github.com/user-attachments/assets/8df104df-9392-4d83-871a-ae6f59748d82)


2. **Flexible Model Design**:
   - Models with variable nodes per layer and hidden layers were tested.
   - **HyperOpt** was used to sample and test various combinations of model architectures and hyperparameters to achieve the best performance.

3. **Optimization**:
   - Define parameter space for hyperparameters.
   - Objective function: Minimize the PINN loss function, which includes:
     - Squared error
     - Boundary conditions
     - Physics-based loss (from the differential equation)

---

### Training Overview
- Visual depiction of the training process.
- ![image](https://github.com/user-attachments/assets/cb505bad-29d1-4857-9d02-5a7dcb9adbd5)

- Hyperparameter configuration yielding the lowest loss.
- ![image](https://github.com/user-attachments/assets/adcbdda2-850b-48f8-beba-18db70630c2e)


---

## Further Improvements

1. **Optimizing Parameter Space**:
   - To reduce computation cost, the range of the number of hidden layers was reduced from `{4,10}` to `{2,4}`.

2. **Expanding Inputs**:
   - Initially, only time was used as an input to the PINN.
   - Now, amplitude is also included, representing different pulse waves.
   - Training data consists of solutions from the ODE for all these waves.

---

Thank you!  
**Siddh Singhal**  
Email: singhal.siddh@gmail.com 
