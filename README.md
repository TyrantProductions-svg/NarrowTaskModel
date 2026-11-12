# N.T.M.

# Narrow Task Model (NTM)
## Project Overview and Design Philosophy

### 1. Introduction

**Narrow Task Model (NTM)** is an experimental, locally operated, brain-inspired artificial intelligence system designed to run primarily on the Arduino UNO Q.

Unlike conventional conversational AI systems that primarily respond to user prompts, NTM is intended to operate as a continuously running, autonomous system. It will perceive its environment, process information, make decisions, communicate, maintain memories, and gradually adapt through its experiences.

The verified project structure, subsystem purposes, open architectural decisions, and distinction between existing and proposed components are documented in [docs/architecture.md](docs/architecture.md).

The project takes inspiration from the organization and functions of the biological human brain. Its software architecture will use brain-region-inspired modules, each responsible for a particular aspect of information processing and cognition.

NTM is not intended to compete with large language models in general intelligence or raw computational ability. Instead, its goal is to develop a specialized, efficient, adaptive AI capable of performing a narrower range of tasks.

### 2. Primary Objectives

NTM is being developed around several major objectives:

- **Autonomy:** Operate continuously without requiring a user prompt for every action.
- **Perception:** Receive and interpret information from its surroundings through sensors, initially focusing on audio.
- **Reasoning:** Process information, evaluate situations, and make decisions.
- **Memory:** Store experiences and information, retrieve relevant memories, and consolidate knowledge.
- **Communication:** Interact with users through text and eventually speech.
- **Adaptability:** Change its behavior based on accumulated experience.
- **Lifelong Learning:** Continue learning throughout its operational lifetime rather than remaining entirely dependent on its initial training.
- **Embodiment:** Connect its cognitive processes to physical hardware and its surrounding environment.

### 3. Hardware Architecture

NTM uses the Arduino UNO Q as its primary hardware platform. Its two main processing components serve different purposes.

**Qualcomm QRB2210 Linux MPU — Cerebrum**

The Linux-capable processor serves as the primary cognitive computing environment. It will host the Python-based software architecture, including reasoning, memory, perception, learning, and communication systems.

**STM32U585 Microcontroller — Cerebellum and Brainstem**

The microcontroller serves as the lower-level control system. Its intended responsibilities include hardware interaction, real-time operations, sensor handling, and other lower-level functions.

The division is inspired by the relationship between higher-level cognitive processing and lower-level biological control systems. This is a functional analogy, not an attempt to reproduce the actual biological brain.

### 4. Brain-Inspired Software Architecture

NTM's Linux-side software is organized into Python modules named after biological brain structures. The verified directory structure and the intended scope of each subsystem are described in [docs/architecture.md](docs/architecture.md).

These names represent the intended responsibilities of each module rather than literal biological equivalents.

The existing structure includes two computational hemispheres, each with corresponding frontal- and temporal-lobe modules:

- **Left Hemisphere:** Its specific responsibilities have not yet been assigned.
- **Right Hemisphere:** Its specific responsibilities have not yet been assigned.

The corresponding module files establish a place for future design; they do not imply that functions or specializations have been finalized.

The **Corpus Callosum** is intended to coordinate communication between corresponding modules and act as a major communication hub between the hemispheres. Its boundaries and protocols, like the wider module communication design, remain to be decided.

The `python/ntm/neural/` package is an approved addition for foundational neural components implemented in ordinary Python, not imported from a neural-network framework. Its APIs and integration with the brain and learning packages remain design decisions; see [docs/architecture.md](docs/architecture.md).

### 5. Memory and Learning

Memory and learning are among the most important components of NTM.

The system is intended to retain information from its experiences, retrieve relevant information when needed, and gradually improve its behavior.

Its learning architecture will explore the concept of **continual learning**, also known as lifelong learning.

Rather than relying exclusively on a fixed, pretrained model, NTM should be capable of adapting over time through continued operation.

This involves several distinct processes:

- Recording experiences.
- Identifying useful patterns and information.
- Retaining and retrieving relevant knowledge.
- Evaluating the results of previous decisions.
- Adjusting behavior based on accumulated experience.
- Consolidating memories during designated maintenance or sleep-like periods.

A major research challenge will be ensuring that new learning does not destroy previously acquired capabilities. The system must also distinguish between remembering an experience and actually learning a generalizable behavior from it.

### 6. Internal State and Motivation

NTM is intended to have an internal state system inspired by biological emotional and motivational processes.

This may include computational representations of:

- Motivation.
- Curiosity.
- Reward and reinforcement.
- Stress or computational load.
- Satisfaction of operational objectives.
- Internal resource requirements.

These variables will influence the system's priorities and decisions.

They are computational mechanisms inspired by biology, not evidence of genuine subjective emotions or consciousness.

### 7. Continuous Operation and Autonomy

NTM is intended to remain operational over extended periods.

Its operation should not be limited to responding to direct user commands. It should also be capable of initiating appropriate internal processes, checking its environment, maintaining its memory, and performing scheduled tasks.

Not every subsystem needs to operate continuously. Different modules can be activated according to events, priorities, or scheduled intervals.

The architecture may eventually incorporate sleep-like maintenance cycles, during which the system reviews and consolidates accumulated experiences.

### 8. Design Philosophy

The development of NTM follows several principles:

1. **Modularity:** Each subsystem should have a clearly defined responsibility.
2. **Coordination:** Modules should communicate through established interfaces rather than relying on uncontrolled interactions.
3. **Efficiency:** The system should make effective use of its limited hardware resources.
4. **Adaptability:** Learning should be an ongoing part of its operation.
5. **Reliability:** Individual components should be testable and failures should not unnecessarily destabilize the entire system.
6. **Transparency:** Its internal processes should be understandable, observable, and documented.
7. **Incremental Development:** Each subsystem should be designed, implemented, and tested progressively.

### 9. Intended Advantages and Limitations

**Potential advantages:**

- Local operation without mandatory cloud services or recurring AI subscriptions.
- Lower computational requirements than large general-purpose AI systems.
- Specialization in a defined range of tasks.
- Greater control over its software, data, and operating environment.
- Continual adaptation through accumulated experiences.
- Integration with physical hardware and sensors.

**Expected limitations:**

- More limited general knowledge and reasoning capabilities.
- Potentially slower processing than cloud-based systems.
- Hardware and memory constraints.
- Possibility of incorrect decisions and unreliable learning.
- Difficulty maintaining previously acquired capabilities while learning new ones.
- Considerable development and maintenance requirements.

These advantages are project goals, not yet demonstrated results.

### 10. Long-Term Vision

The long-term objective is to develop NTM into a persistent, embodied, adaptive AI system.

It should be able to perceive, reason, remember, communicate, and learn as parts of one coordinated architecture.

Its defining characteristic is not simply its ability to perform a particular task, but its intended capacity to develop and adapt through continued experience.

**NTM is an exploration of how far a small, modular, brain-inspired, locally operated AI system can develop through autonomy and lifelong learning.**

# Development Roadmap

## Overall Development Strategy

NTM will be developed in three major phases:

1. **Phase I — The Brain:** Develop and test the Python cognitive architecture independently of hardware. Decide whether and how to add neural components.
2. **Phase II — The Nervous System:** Develop the Arduino sketch and integrate the STM32U585, sensors, microphones, speakers, and other peripherals.
3. **Phase III — The Body:** Construct and integrate the physical mobile robot platform.

Development will be incremental. Each subsystem must be tested before being integrated into the larger system.

---

# PHASE I — THE BRAIN
## Python Cognitive Architecture

**Objective:** Develop a Python system capable of processing information, responding to inputs, and testing memory and learning approaches, including foundational neural components implemented from the ground up.

### Stage 1. Project Preparation and Python Refresher

1. Review the existing project directory and documentation.
2. Establish the Python development environment.
3. Refresh Python fundamentals:
   - Variables and data types.
   - Functions and parameters.
   - Classes and objects.
   - Lists, dictionaries, and other data structures.
   - Modules, packages, and imports.
   - File handling.
   - Exception handling.
4. Understand how Python modules communicate.
5. Establish basic coding conventions and documentation practices.

**Milestone:** A clean, understandable Python environment ready for development.

### Stage 2. Core Architecture

1. Establish the main program entry point.
2. Design the central runtime.
3. Define how individual modules communicate.
4. Investigate what responsibilities, if any, should be assigned to each hemisphere and its corresponding modules.
5. Define the intended scope of the Corpus Callosum and how it relates to other module communication.
6. Design module interfaces and information exchange, including data shapes and error behavior.
7. Define how the system starts, operates, and shuts down.
8. Implement basic logging and error reporting.

**Milestone:** A testable software framework with deliberately designed, documented module interfaces.

### Stage 3. Artificial Neurons and Neural Components

Develop basic computational components for neural processing in the approved `python/ntm/neural/` package. Implement the core mechanisms in ordinary Python rather than relying on PyTorch, TensorFlow, Keras, or another neural-network framework to provide them.

1. Study biological neurons and simplified artificial neuron models.
2. Design a Python neuron class.
3. Implement inputs, weights, bias, and activation functions.
4. Study artificial synapses and weighted connections.
5. Design how neurons transmit information to one another.
6. Organize neurons into groups and layers.
7. Develop a basic neural network structure.
8. Implement forward propagation.
9. Study loss functions and how network performance is evaluated.
10. Investigate learning algorithms and implement an appropriate initial learning method.
11. Test the network using small datasets.
12. Investigate how network parameters can be updated through experience.

**Milestone:** A small neural-network implementation whose behavior is understood and tested.

### Stage 4. Neural Learning and Plasticity

1. Study supervised, unsupervised, and reinforcement learning.
2. Decide which learning methods are appropriate for NTM.
3. Implement an initial learning mechanism.
4. Establish how experiences become training examples or feedback, and how this connects to the memory and experience modules.
5. Develop a mechanism for adjusting neural network parameters.
6. Investigate continual learning.
7. Study catastrophic forgetting and methods of reducing it.
8. Implement a basic experience evaluation system.
9. Test whether learning produces measurable improvements.
10. Investigate how previously learned capabilities can be retained.

**Milestone:** NTM can learn from information and demonstrate measurable changes in performance.

### Stage 5. Memory Architecture

1. Design the memory system.
2. Establish how information is encoded and stored.
3. Implement basic memory creation.
4. Implement memory retrieval.
5. Establish how memories are categorized and organized.
6. Investigate short-term and long-term memory models.
7. Connect memory retrieval to the cognitive architecture.
8. Develop experience recording.
9. Investigate memory consolidation.
10. Test whether NTM can remember information across sessions.

**Milestone:** NTM can store, retrieve, and retain experiences.

### Stage 6. Cognitive Architecture

Develop the brain-inspired Python modules.

1. Decide what the two-hemisphere organization is intended to accomplish.
2. Define candidate responsibilities for the corresponding frontal- and temporal-lobe modules without assuming that the two sides must have fixed biological specializations.
3. Define the Corpus Callosum's scope and its relationship to the rest of the system.
4. Specify and test information exchange between modules.
5. Decide whether neural processing belongs in a dedicated proposed package, in task-specific modules, or elsewhere.
6. Integrate neural processing only after its interfaces and relationship to learning are clear.
7. Establish how the system evaluates information.
8. Develop basic reasoning and decision-making processes.
9. Test coordination between the hemispheres.

Additional brain-inspired modules can be introduced when their responsibilities are sufficiently defined.

**Milestone:** NTM has a coordinated, modular cognitive architecture.

### Stage 7. Perception and Communication

Initially, perception and communication can operate through text-based inputs and outputs.

1. Develop a basic input-processing interface.
2. Establish how external information enters the cognitive architecture.
3. Develop a language-processing component.
4. Establish how information is interpreted.
5. Develop a response-generation mechanism.
6. Connect responses to reasoning and memory.
7. Investigate local language models or other language-processing methods if necessary.
8. Test conversations and information exchange.
9. Investigate audio processing for future hardware integration.

**Milestone:** NTM can receive information, process it, and communicate meaningful responses.

### Stage 8. Internal States and Motivation

1. Research biological motivation and emotional regulation.
2. Identify useful computational equivalents.
3. Develop an internal state representation.
4. Investigate reward and reinforcement signals.
5. Develop motivation and priority mechanisms.
6. Establish how internal states influence decisions.
7. Test how changes in internal variables affect behavior.

These are computational models inspired by biological processes, not evidence of subjective emotions or consciousness.

**Milestone:** NTM has a measurable internal state system that influences its decisions.

### Stage 9. Autonomous Operation and Maintenance

1. Develop a basic task scheduler.
2. Establish event-driven module activation.
3. Implement periodic background tasks.
4. Develop autonomous information processing.
5. Establish operational priorities.
6. Investigate sleep-like maintenance cycles.
7. Develop memory consolidation during maintenance.
8. Establish recovery from errors and interrupted operation.
9. Test extended periods of operation.

**Milestone:** NTM can operate continuously and manage its own internal processes.

### Stage 10. Phase I Integration and Testing

Integrate the completed software components.

1. Integrate the foundational neural components after their interfaces and relationship to learning are clear.
2. Connect cognitive modules to memory.
3. Connect memory to the learning system.
4. Connect perception and communication to the cognitive architecture.
5. Integrate internal states and motivation.
6. Integrate the scheduler and autonomous runtime.
7. Test information processing.
8. Test response generation.
9. Test memory retention.
10. Test learning and adaptation.
11. Evaluate performance and resource consumption.
12. Document limitations and outstanding problems.

**PHASE I FINAL MILESTONE:**

A functioning Python-based NTM prototype capable of receiving information, processing it, responding, retaining experiences, and demonstrating measurable learning.

---

# PHASE II — THE NERVOUS SYSTEM
## Arduino UNO Q Hardware Integration

**Objective:** Connect the Python-based cognitive system to the physical hardware through the STM32U585 microcontroller.

The STM32U585 represents the cerebellum and brainstem in the project's biological analogy.

### Stage 11. Microcontroller Architecture

1. Study the STM32U585 environment and Arduino programming workflow.
2. Establish the Arduino sketch structure.
3. Define the microcontroller's responsibilities.
4. Design communication between the Linux MPU and STM32U585.
5. Investigate Arduino Bridge and other appropriate communication mechanisms.
6. Establish a basic communication protocol.
7. Test information exchange between the two processors.

**Milestone:** The Linux MPU and STM32U585 can communicate reliably.

### Stage 12. Audio Hardware Integration

1. Review the microphone hardware and electrical requirements.
2. Establish a working microphone connection.
3. Test audio input.
4. Develop audio acquisition and processing.
5. Connect audio input to the Python perception system.
6. Establish the speaker and amplifier connection.
7. Test audio output.
8. Connect speech output to the communication system.
9. Test a complete audio input-to-response-to-audio output cycle.

**Milestone:** NTM can hear audio input and communicate through its speaker system.

### Stage 13. Additional Sensors and Peripherals

1. Identify future sensor requirements.
2. Establish appropriate hardware interfaces.
3. Integrate additional sensors individually.
4. Develop sensor data processing.
5. Connect sensor information to the perception architecture.
6. Test communication reliability.
7. Document hardware interfaces and limitations.

**Milestone:** NTM can receive information from multiple physical sources.

### Stage 14. Hardware Control and Integration

1. Establish a unified hardware communication interface.
2. Connect the cognitive system to the microcontroller.
3. Develop basic hardware command handling.
4. Establish safety limits for hardware operations.
5. Test communication failures and recovery.
6. Integrate audio, sensors, and other peripherals.
7. Conduct extended operational tests.

**PHASE II FINAL MILESTONE:**

NTM can operate through the UNO Q, receive information from physical sensors, communicate through audio, and control connected peripherals.

---

# PHASE III — THE BODY
## Physical Construction and Mobility

**Objective:** Transform NTM into an embodied, mobile desk buddy.

### Stage 15. Physical Platform Design

1. Establish the physical dimensions and general design.
2. Plan the internal component layout.
3. Design the enclosure.
4. Plan power distribution.
5. Plan mounting for the UNO Q and peripherals.
6. Establish the mechanical requirements for mobility.

**Milestone:** A finalized physical design ready for construction.

### Stage 16. Mobility System

1. Select appropriate motors and wheels.
2. Establish the motor-control hardware.
3. Design the motor-control interface.
4. Implement basic movement commands.
5. Test forward, backward, and turning movements.
6. Establish movement limits and emergency stopping.
7. Integrate movement control with the microcontroller.

**Milestone:** The physical platform can move under controlled commands.

### Stage 17. Environmental Awareness

1. Select appropriate environmental sensors.
2. Integrate obstacle-detection hardware.
3. Develop sensor interpretation.
4. Establish basic obstacle avoidance.
5. Investigate localization and navigation.
6. Connect environmental awareness to the cognitive architecture.
7. Test movement in a controlled environment.

**Milestone:** The desk buddy can perceive nearby obstacles and respond appropriately.

### Stage 18. Complete System Integration

1. Install the completed hardware into the physical enclosure.
2. Integrate the Python cognitive system.
3. Integrate the microcontroller.
4. Connect audio and environmental sensors.
5. Connect the mobility system.
6. Test communication between all subsystems.
7. Test autonomous operation.
8. Evaluate reliability and power consumption.
9. Document the completed system and its limitations.

**PHASE III FINAL MILESTONE:**

A functioning mobile NTM desk buddy capable of communicating, perceiving its surroundings, learning from experience, and moving through its environment.

---

# Final Project Goal

The ultimate goal of Narrow Task Model is to create a persistent, embodied, locally operated AI system with a modular, brain-inspired cognitive architecture.

Its defining feature is its intended ability to adapt and develop through continued experience.

The project will be developed through personal experimentation, research, programming, and incremental testing. Each subsystem should be understood before being expanded or integrated into the larger system.# NarrowTaskModel
