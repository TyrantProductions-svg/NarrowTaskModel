# NTM Architecture

## Status and scope

This document describes the verified project skeleton and its intended direction. A file or directory being present does not mean its behavior is implemented or finalized. The biological terms below are functional analogies for software organization, not claims that the hardware or software reproduces biological structures.

The project is developed in three phases: **The Brain** (Python architecture developed and tested independently), **The Nervous System** (Arduino sketch and peripheral integration), and **The Body** (construction and integration of a mobile robot).

## Verified project skeleton

The following is the current project structure. It is the canonical skeleton; keep it intact unless a structural change is discussed and approved.

```text
NarrowTaskModel/
├── app.yaml
├── README.md
├── python/
│   ├── main.py
│   ├── requirements.txt
│   └── ntm/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── runtime.py
│       │   ├── scheduler.py
│       │   └── config.py
│       ├── brain/
│       │   ├── __init__.py
│       │   ├── corpus_callosum.py
│       │   ├── left_hemisphere/
│       │   │   ├── __init__.py
│       │   │   ├── frontal_lobe.py
│       │   │   └── temporal_lobe.py
│       │   └── right_hemisphere/
│       │       ├── __init__.py
│       │       ├── frontal_lobe.py
│       │       └── temporal_lobe.py
│       ├── memory/
│       │   ├── __init__.py
│       │   ├── memory_manager.py
│       │   └── consolidation.py
│       ├── perception/
│       │   ├── __init__.py
│       │   ├── audio.py
│       │   └── vision.py
│       ├── affective_system/
│       │   ├── __init__.py
│       │   ├── motivation.py
│       │   └── emotional_state.py
│       ├── learning/
│       │   ├── __init__.py
│       │   ├── plasticity.py
│       │   ├── experience.py
│       │   └── evaluation.py
│       ├── neural/                     # Approved addition; scaffolding only
│       │   ├── __init__.py
│       │   ├── neuron.py
│       │   ├── synapse.py
│       │   ├── network.py
│       │   ├── activation.py
│       │   └── learning_rules.py
│       ├── communication/
│       │   ├── __init__.py
│       │   ├── language.py
│       │   └── speech.py
│       └── hardware/
│           ├── __init__.py
│           ├── mcu_bridge.py
│           ├── microphone.py
│           └── speaker.py
├── sketch/
│   └── sketch.ino
├── data/
│   ├── memories/
│   ├── experiences/
│   └── learned_knowledge/
├── tests/
│   └── __init__.py
└── docs/
    └── architecture.md
```

## Hardware architecture

The Arduino UNO Q contains two main computing components with different roles:

- **Qualcomm QRB2210 Linux MPU — conceptual cerebrum:** the Linux environment for the Python-side cognitive system and higher-level processing.
- **STM32U585 microcontroller — conceptual cerebellum and brainstem:** the microcontroller for Arduino-sketch-based, lower-level hardware operations, real-time tasks, and peripheral interfaces.

These are functional analogies only. They do not imply biological equivalence. The Python-to-microcontroller connection and its communication mechanism are not yet specified.

## Python subsystem responsibilities

The package names express intended areas of responsibility, not finalized internal behavior or APIs.

| Area | Location/status | Intended purpose |
|---|---|---|
| Entry point and dependencies | `python/main.py`, `python/requirements.txt` | Python application entry and declared Python dependencies. |
| Core | `python/ntm/core/` | Runtime, scheduling, configuration, and overall system coordination. |
| Brain | `python/ntm/brain/` | Two computational hemispheres and their communication hub. Each hemisphere has corresponding frontal- and temporal-lobe modules. Their exact responsibilities remain open. |
| Memory | `python/ntm/memory/` | Store, retrieve, organize, and consolidate memories and experiences. |
| Perception | `python/ntm/perception/` | Process sensory information, including audio and potentially vision in the future. |
| Affective system | `python/ntm/affective_system/` | Represent computational internal states, motivation, and priorities. These states are not genuine subjective feelings. |
| Learning | `python/ntm/learning/` | Evaluate experience and explore plasticity and adaptation. |
| Neural | `python/ntm/neural/` **(approved addition)** | Foundational neural components implemented in ordinary Python: neurons, synapses, network propagation, activation functions, and learning-rule foundations. The package files are scaffolding, not implemented functionality. |
| Communication | `python/ntm/communication/` | Language processing and speech-related capabilities. |
| Hardware interfaces | `python/ntm/hardware/` | Connect Python-side functions to the microcontroller and peripherals. Exact interfaces are undecided. |
| Arduino sketch | `sketch/sketch.ino` | Firmware-side starting point for the STM32U585 and connected hardware. |
| Persistent data | `data/memories/`, `data/experiences/`, `data/learned_knowledge/` | Intended locations for persistent memories, recorded experiences, and learned knowledge. Storage formats and retention policies are undecided. |
| Tests | `tests/` | Automated checks for individual components and integrated behavior. |
| App configuration | `app.yaml` | Project/application configuration for the UNO Q environment. |
| Documentation | `README.md`, `docs/` | Project overview, development roadmap, and architecture notes. |

These descriptions do not assert that every listed capability is implemented today.

## Brain and hemisphere organization

The left and right hemispheres are separate computational areas with corresponding frontal- and temporal-lobe modules. The **Corpus Callosum** is intended to coordinate communication between corresponding modules and serve as a major communication hub between the hemispheres.

The boundaries, responsibilities, and information flow of these modules have not been decided. In particular, “left” and “right” do not establish specific cognitive specializations. Avoid assigning fixed functions to a hemisphere, lobe, or the Corpus Callosum until those choices are deliberately designed and documented.

## Approved neural package addition

The `python/ntm/neural/` package is an approved addition to the verified project skeleton. Its files are initial scaffolding; implementation is intentionally left to the project author:

```text
ntm/
└── neural/
    ├── __init__.py
    ├── neuron.py
    ├── synapse.py
    ├── network.py
    ├── activation.py
    └── learning_rules.py
```

This package will provide foundational artificial-neural components: neuron computations, weighted synaptic connections, network organization and propagation, activation functions, and initial weight-update rules. The network core is to be implemented in ordinary Python rather than supplied by a neural-network framework. The specific APIs and how this package relates to `learning/` and `brain/` remain design decisions.

## Cross-cutting decisions to make

Design and test these points incrementally before treating module boundaries as fixed:

1. **Hemisphere responsibilities:** What problem does the two-hemisphere split solve? Which work belongs in each hemisphere, what do corresponding frontal and temporal modules mean, and what should remain shared?
2. **Corpus Callosum scope:** Is it limited to hemisphere-to-hemisphere coordination, or does it route wider system messages? What must not depend on it?
3. **Neural integration:** How should the foundational neural components relate to `learning/plasticity.py` and the cognitive modules in `brain/`? Keep general weight-update mechanisms distinct from experience evaluation and higher-level adaptation unless a deliberate design says otherwise.
4. **Module communication:** Which interactions are direct calls versus queued/events? What are the message/data shapes, ownership rules, error behavior, and lifecycle expectations? Keep interfaces small enough to test independently.
5. **Persistence and learning:** What is stored as an experience, what qualifies as learned knowledge, and how are versions, retrieval, consolidation, and model updates kept safe and measurable?
6. **Hardware boundary:** Which operations require the microcontroller, how are commands and sensor readings represented, and what behavior is required for timeouts, disconnection, and safe hardware operation?
7. **Resource limits and verification:** What memory, CPU, latency, and power budgets apply on the UNO Q, and what tests demonstrate useful improvement without unacceptable regressions?

## Development phases

1. **The Brain:** Design and test the Python cognitive and any neural architecture independently of hardware. Develop core coordination, memory, perception, internal computational states, learning, and communication incrementally.
2. **The Nervous System:** Develop the Arduino sketch and integrate the STM32U585, sensors, microphones, speakers, and other peripherals. Define and test the Linux-MCU interface before depending on it.
3. **The Body:** Construct and integrate the physical mobile robot platform, connecting its movement and environmental sensing to the previously tested system.

The phases are a development plan, not claims of completed capabilities. Brain-inspired design is a source of organizational ideas; NTM is a computational system, not a biological brain. Likewise, affective-system variables represent modeled internal state and must not be presented as evidence of subjective emotion or consciousness.
