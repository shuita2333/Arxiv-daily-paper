# 📦 其他研究 | 2026年06月26日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 1. [Graph-Based Phonetic Error Correction of Noisy ASR](https://arxiv.org/abs/2606.24889)

**<font color=#1a73e8>作者：</font>** Pratik Rakesh Singh, Mohammadi Zaki, Aneesh Mukkamala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems, despite low overall word error rates, produce residual lexical errors that disproportionately affect semantically critical tokens such as named entities, negations, and sentiment-bearing words. These errors are often structured, arising from phonetic similarity rather than random noise, making naive token-level correction insufficient. We propose a structured ASR correction framework, that we call G-SPIN, that combines phonetic graph modeling with contextual language understanding. A graph neural network (GNN) first constructs acoustically plausible candidate neighborhoods for flagged tokens, explicitly restricting the correction search space to phonetic alternatives. A masked language model (MLM) then provides local contextual scoring, and an instruction-tuned large language model (LLM) performs final context-aware re-ranking over this compact candidate set. By decoupling structured phonetic reasoning from contextual semantic selection, our method avoids unconstrained generation while improving correction accuracy. The framework is lightweight, modular, and operates entirely at inference time.

---


### 2. [AgentOdyssey: Open-Ended Long-Horizon Text Game Generation for Test-Time Continual Learning Agents](https://arxiv.org/abs/2606.24893)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Zehao Wen, Alvin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For agents to learn continuously from interaction with the world at test time, they must be able to explore effectively, acquire new world knowledge and skills, retain relevant episodic experiences, and plan over long horizons. To evaluate these key abilities of test-time continual learning agents, we introduce AgentOdyssey, a novel evaluation framework that procedurally generates open-ended text games with rich entities, world dynamics, and long-horizon tasks. Critically, AgentOdyssey goes beyond the conventional machine learning assumption that learning does not occur at test time by placing agents in a continuous, long-horizon setting that interleaves learning and inference throughout deployment. We further propose a multifaceted evaluation methodology that measures not only game progress but also offers diagnostic tests on world knowledge acquisition, episodic memory, object and action exploration, action diversity, and model cost. We evaluate diverse agent paradigms in the generated games. Our experimental results reveal critical limits in agents' key abilities, as well as factors that influence their meaningful horizon. Although performance scales with stronger base models, even the top agent remains far below human performance, leaving substantial headroom for improvement. Among agent mechanisms, we find that short-term memory benefits multiple agent paradigms and is an important component of agent test-time training.

---


### 3. [From Meta Idea to Advanced Mathematical Discovery -- Human-AI Co-Discovery of Sign-Embedding Quantum Algorithms](https://arxiv.org/abs/2606.24899)

**<font color=#1a73e8>作者：</font>** Yanqiao Wang, Jin-Peng Liu, Peng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-assisted mathematics is often evaluated on solving predefined problems. In practice, however, many important advances begin earlier, when a vague research intuition is transformed into a concrete problem, a promising route, and a theorem family worth proving. This report studies that stage through a case study that led to sign-embedding quantum algorithms for matrix equations and matrix functions, foundational primitives in quantum linear algebra and operator-output quantum algorithms. The project began with a human-originated intuition that rational approximation is especially effective for jump-type functions such as the sign function, and might therefore serve as a design principle for quantum algorithms. Rather than merely assisting after the problem was fixed, AI-assisted exploration, including workflows later integrated into the agentic AI-mathematician system AIM, played a key role in expanding this intuition into a route map, comparing candidate formulations, and converging toward sign embedding as the central framework. AIM then helped connect a known matrix-sign identity to wider classes of matrix equations and matrix functions, and drafted proof and complexity calculations. The decisive scientific judgments remained human: selecting which human-AI-expanded routes were worth pursuing, rejecting a Cayley-trapezoidal approximation when its validity required a hidden condition, and refining the Sylvester implementation from a coarse quadratic-gap query route to the final factorized and scaled analysis. The report argues that human-AI co-discovery workflows, with systems such as AIM as important components, are most valuable not as standalone theorem provers, but as research partners for problem formation, connection discovery, derivation, and skeptical review inside a human-gated research loop.

---


### 4. [On-Device Neural Architecture Search](https://arxiv.org/abs/2606.24900)

**<font color=#1a73e8>作者：</font>** Andrea Mattia Garavagno, Edoardo Ragusa, Paolo Gastaldo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a new approach to near-sensor computing, in which a lightweight Neural Architecture Search (NAS) is performed directly on the deployment device to find the best tiny neural architecture for analyzing the real-time data acquired through sensors. This new adaptation capability can be particularly useful in the case of human-machine interfaces for which the neural network analyzing the biometrical data can be re-designed each time the user changes, after a guided data collection procedure, fighting the typical data variations between individuals on a new level. To implement the proposed approach a new NAS has been designed and then validated on the Italian Sign Language dataset (ISL), a collection of surface electromyography (sEMG) signals of the signs of the Italian alphabet, using several embedded systems. Moreover, further validation on the Case Western Reserve University dataset (CWRU), a benchmark for intelligent fault diagnosis, is presented to suggest another possible application of the proposed approach. When run on a Raspberry Pi 4, the proposed NAS performs beyond the state of the art proposing a tiny neural architecture having 0.63 times less RAM occupancy and 5.96 percentage points of more accuracy in the case of the ISL dataset; and 0.44 times less RAM occupancy and 0.2 percentage points of more accuracy in the case of the CWRU dataset.

---


### 5. [A Spectral Phase Diagram for Binary Few-Shot Classification: Intrinsic Dimensionality, Geometric Saturation, and Representational Diagnosis](https://arxiv.org/abs/2606.24903)

**<font color=#1a73e8>作者：</font>** Arnav Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deciding when to stop collecting labeled examples is a fundamental but undertheorized problem in applied machine learning. The saturation index $S(K) = \operatorname{erank}(\widehat{\Sigma}_W^{(K)}) / K$ measures the ratio of the effective rank of the pooled within-class sample covariance to the shot count; we prove it falls below a threshold precisely when the covariance estimator is well-concentrated around the population covariance and the linear discriminant has stabilized. The index is computable in $O(d^3)$ time from support features alone, requiring no test labels or trained classifier.
Evaluated across $N = 246$ doubling-pair observations from seventeen binary tasks and six datasets, sixteen of seventeen tasks have a positive within-task Spearman correlation between $S(K)$ and marginal accuracy gain (median $\rho = 0.811$). The pooled Spearman correlation is $\rho = 0.548$ ($p = 1.1 \times 10^{-20}$, $N = 246$). A three-phase diagram (exploration, transition, saturation) with mean marginal gains of $3.48\%$, $2.40\%$, and $0.82\%$ is supported by all pairwise significance tests ($p \leq 0.008$). As a binary stopping rule, the index achieves AUC $= 0.752$, providing meaningful probabilistic guidance for annotation decisions. Asymptotic effective rank and peak accuracy show no significant monotone relationship across tasks (Spearman $r_s = 0.380$, $p = 0.133$, $N = 17$). A small saturation index paired with low accuracy diagnoses representational inadequacy. All results are for binary classification with a fixed linear classifier; extensions to $N$-way settings and pretrained backbone representations are discussed as future work.

---


### 6. [Unprivileged Topology Certificates for Cloud GPU Attestation](https://arxiv.org/abs/2606.24934)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud GPU tenants receive a model name and a region, but cannot directly inspect the physical accelerator that runs their job. We present a software-only attestation primitive for this setting. A CUDA probe measures an SM-by-memory-region latency matrix using physical SM labels and dependent global loads. A streaming reducer commits sufficient statistics, configuration, code hashes, network evidence, and a compressed raw data archive into a certificate that a verifier can check without a GPU. The certificate supports three claims. First, the per-SM latency map is a stable physical fingerprint. Over a six-hour full-load RTX 5090 run, its median temporal jitter is 0.09 cycles, while shape-only leave-one-out classification separates distinct Blackwell dies with 100.0% accuracy. Second, cache-bypassing HBM sweeps recover hardware-class topology across generations, including a unified Volta V100 memory domain, a two-way Hopper H200 L2 split, and a Blackwell B200 two-die NV-HBI package whose 74/74 SM partition carries a 30-cycle, 15.5 ns cross-die penalty. Third, public network landmarks bind the same certificate to a coarse location. In the B200 run, 169 RIPE Atlas probes place the server within 44 km of its claimed datacentre and reject all 11 decoy sites. Together, these measurements check cloud-GPU identity, class, and coarse location without privileged access or a vendor key.

---


### 7. [SEMIR: Topology-Preserving Graph Minors for Thin-Structure Segmentation](https://arxiv.org/abs/2606.24935)

**<font color=#1a73e8>作者：</font>** Luke James Miller, Yugyung Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thin-structure segmentation--power lines, cracks, lane markings at 1-3 pixel width--requires preserving connectivity that standard representations preclude: patching severs continuous structures and conventional superpixels merge thin targets into background before classification. Topology-aware losses penalize connectivity breaks at the objective level but cannot recover what the representation has already destroyed. We propose SEMIR, a framework that replaces the pixel lattice with a parameterized graph minor whose contraction map preserves thin-structure connectivity under the contraction criterion. The minor collapses millions of pixels into tens or hundreds of boundary-aligned supernodes, enabling full-resolution inference without patching at scales demonstrated up to 21 MP in this paper; a lightweight GNN classifies the reduced graph and an exact map lifts predictions to pixel resolution. One pipeline--identical architecture, features, loss, and GNN hyperparameters across all dataset--matches or exceeds domain-specific baselines on TTPLA (power lines), CrackSeg9k (pavement cracks), and SkyScapes Lane (aerial markings) on Dice, IoU, and Boundary F1 while reducing mask fragmentation by at least 4.6x relative to SLIC at matched inference.

---


### 8. [Quantum-Resilient Decentralized AI Economies: Proof-of-Useful-Work and Post-Quantum Security](https://arxiv.org/abs/2606.24942)

**<font color=#1a73e8>作者：</font>** Connor Barbaccia, Sudip Vhaduri, Sayanton Dibbo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proof-of-Work blockchains secure consensus through hash puzzles, producing no external value. In this research, we propose a decentralized AI economy where nodes are rewarded for useful machine-learning work, i.e., inference and training, instead of ineffective hashing method. Our proposed three-layer architecture separates compute, validation, and economic coordination. We formalize it via a $(\theta_c, \theta_w, W)$-closed-loop token economy and derive a sufficient-stake condition for honest participation. While existing Grover's algorithm provides only a quadratic speedup against hash puzzles, it does not accelerate ML-native linear algebra. On the other hand, Shor's algorithm threatens classical blockchain signatures. Post-quantum migration to lattice-based and hash-based standards can address the signature layer. Therefore, useful-work consensus thus offers both economic and quantum-security advantages over classical proof-of-work.

---


### 9. [Supervised Reinforcement Learning for the Coordination of Distributed Energy Resources](https://arxiv.org/abs/2606.24947)

**<font color=#1a73e8>作者：</font>** Haoyuan Deng, Yihong Zhou, Thomas Morstyn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The increasing integration of distributed energy resources (DERs) is crucial for power system decarbonization, yet unlocking DERs' flexibility is challenged by their inherent uncertainties and modelling complexity. As traditional optimization methods struggle with such uncertainty and complexity of DERs, reinforcement learning (RL) has emerged as a promising alternative for DER management. However, standard RL methods suffer from sample inefficiency and sub-optimality when trained from scratch. Inspired by the training paradigms in large language models, this paper proposes a Supervised Reinforcement Learning (SRL) framework for learning DER coordination policies. This framework first pre-trains a policy on demonstration data in a supervised-learning fashion, which is then further fine-tuned using RL. Furthermore, we propose a two-step fine-tuning process: offline fine-tuning for enhancing policy performance and online fine-tuning for adapting it to the real-world dynamics. Experiments demonstrate that RL implementations based on the proposed framework significantly outperform all benchmarks, achieving high cost efficiency even under low-quality demonstration data.

---


### 10. [Holographic Memory for Zero-Shot Compositional Reasoning in Knowledge Graphs: A Mechanistic Study of Where and Why It Fails](https://arxiv.org/abs/2606.24948)

**<font color=#1a73e8>作者：</font>** Randhir Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE) models predict single-hop links well but have no mechanism for zero-shot compositional queries: multi-hop questions whose relation chains never appeared during training. Holographic Reduced Representations (HRR), which bind and unbind symbols via circular convolution, are a theoretically attractive candidate, since binding is approximately invertible and associative. We test whether this promise holds.
We study two holographic memory variants, real-valued HRR and phase-only Fourier HRR (FHRR), each with a modern Hopfield cleanup, on FB15k-237 over five seeds. Four findings follow. First, both are competitive single-hop retrievers (filtered MRR 0.358 +/- 0.002 for HRR, 0.350 +/- 0.021 for FHRR). Second, neither composes zero-shot: accuracy stays at chance across all cleanup temperatures. Third, the main contribution, we localise the failure mechanistically. A hop-1 probe shows the memory recovers the correct intermediate entity with high fidelity (MRR 0.896 +/- 0.002 for HRR), yet composition still fails even with a verified-correct intermediate. A second probe shows why: posing the ground-truth second-hop fact as a standalone atomic query, bypassing composition entirely, already recovers it at only 0.26 to 0.48x average atomic accuracy, uniformly across relation fan-out. The bottleneck is not the bind-unbind algebra or the cleanup; it is that facts compositional chains pass through are intrinsically harder for the superposed memory to retrieve, a capacity and interference effect present already at a single hop. Fourth, we prove (Lemma 4.1) that FHRR's softmax cleanup is not phase-equivariant, compounding the primary failure on the minority of chains where hop-1 itself errs. Fixing zero-shot composition requires improving retrieval capacity under superposition, not just redesigning the cleanup.

---


### 11. [How Complexity Contributes to Learning Opacity in Machine Learning](https://arxiv.org/abs/2606.24953)

**<font color=#1a73e8>作者：</font>** Joachim Stein, Eric Raidl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) algorithms are known to be opaque. We do not know the reasons for their predictions. The learning process leading to the prediction function is also opaque. We do not fully understand the time evolution of the weight values of neural nets (NN) and related dynamical phenomena. While prediction opacity is widely studied, learning opacity remains largely underexplored. This article studies learning opacity trough the lens of complex dynamical systems. We argue that NN learning is essentially a complex system and that learning opacity is due to dynamical complexity and the epistemological challenges that arise from it. We identify three key properties of training complexity -- sensitivity to weight initialization, feedback in gradient based optimization, and sensitivity to the training data -- and show how each contributes to learning opacity. As these properties are fundamental to the learning process damping or eliminating them would fundamentally alter how ML systems learn. Some sources of opacity in ML may hence be irreducible.

---


### 12. [Towards Continuous Power Forecasting: Practical Continual Learning for Real-World Energy Systems in Nonstationary Time Series](https://arxiv.org/abs/2606.24955)

**<font color=#1a73e8>作者：</font>** Yujiang He, Frederic Uhrweiller, Bernhard Sick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Power forecasting models deployed in real-world energy markets must operate under nonstationary conditions, where data distributions continually evolve due to weather variability, infrastructure upgrades, and changing consumption behaviors. In practice, these models face strict operational constraints: historical data may be limited or unavailable for repeated retraining, and uninterrupted long-term service is often required. This paper addresses these challenges by proposing the paradigm of Continuous Power Forecasting, which views power forecasting as a continual learning problem rather than a static offline task. Based on an adaptive continual learning framework for regression, we systematically investigate the practical effectiveness of six representative continual learning approaches from three methodological categories. These approaches are evaluated under different realistic assumptions regarding data accessibility and update policies. Experimental validation on real-world power datasets demonstrates that continual learning enables forecasting models to self-adapt to distributional drift, accumulate knowledge over time, and mitigate catastrophic forgetting without relying on large-scale historical data storage. Beyond performance gains, our study provides practical insights into the stability and adaptation behaviors of different continual learning approaches under realistic operational constraints. Overall, this work illustrates how continual learning can be pragmatically integrated into industrial power forecasting pipelines, offering a scalable and sustainable solution for long-term deployment in dynamic environments.

---


### 13. [Convex--Concave Quadratic Spectral Filtering for Graph Neural Networks](https://arxiv.org/abs/2606.24956)

**<font color=#1a73e8>作者：</font>** Ranhui Yan, Jia Cai, Mengzhu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectral graph neural networks (GNNs) interpret message passing as frequency-selective filtering. While low-order spectral filters are efficient, their limited selectivity often leads to weak attenuation outside the passband, whereas high-order alternatives introduce optimization challenges. We propose DCQ-GNN, a spectral GNN based on a compact bank of adaptive convex--concave quadratic filters. By restricting the filter order to two while explicitly exploiting complementary curvature, DCQ-GNN improves spectral selectivity as quantified by Dirichlet energy and entropy measures without resorting to high-order polynomial expansions. The model fuses filter outputs through a node-adaptive gating mechanism to enable node-wise structure-aware spectral selection. We provide a formal spectral analysis grounded in Dirichlet energy attenuation, von Neumann entropy, and curvature polarity, and derive explicit characterizations of filter behavior across varying levels of homophily and structural perturbations. Extensive benchmarks on 10 datasets show that DCQ-GNN ties for the top average rank (3.0) on heterophilic graphs and obtains the second-best rank (4.2) on homophilic graphs, remaining competitive with representative high-order polynomial spectral filters. Furthermore, under strong structural perturbations, DCQ-GNN exhibits substantially smaller performance degradation compared to both first-order and high-order baselines. These results demonstrate that curvature-aware quadratic banks provide a robust and efficient alternative to high-order spectral models while preserving optimization stability and computational efficiency.

---


### 14. [Swarm-Inspired Generation of Collective Behaviors in Graph Dynamical Systems](https://arxiv.org/abs/2606.24958)

**<font color=#1a73e8>作者：</font>** Ji Chen, Song Chen, Chengzhang Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collective behavior arises when locally interacting units produce coordinated global organization, from synchronization in dynamical systems to task-relevant information flow on graphs. The central challenge is not only to explain how collective behavior emerges, but to design local interaction rules that can produce desired global organization and generalize across graphs, dynamics and this http URL address this challenge, we introduce the Swarm-Inspired Emergent Synchronizer (SIES), a graph-dynamical framework that learns generalizable local-interaction laws for controllable collective organization. Each node is an agent-like dynamical unit with a state and task cue, and signed source-target-conditioned attention acts as an adaptive coupling term inside an explicit evolution model. Therefore, SIES combines an explicit dynamical engine with local agent intelligence, similar to biological swarms. For synchronization control, SIES learns a generalizable coupling operator that produces prescribed synchronization patterns for CDSs across untrained network scales, target phase relations, and intrinsic node dynamics without retraining. The learned operator also reaches gait-related modes faster than three oscillator baselines and generalizes synchronization-driven locomotion to simulated multi-legged robots of different scales and a physical hexapod after leg disablement. For graph representation learning, SIES applies the same signed interaction principle to message passing and achieves the highest performance among the compared methods on heterophilous node-classification benchmarks. Together, these results position SIES as a generalizable and learnable graph-dynamical interaction framework with promise for synchronization control, adaptive robot coordination, and heterophilous graph representation learning.

---


### 15. [Reliable Conformal Prediction for Ordinal Classification Using the Ranked Probability Score](https://arxiv.org/abs/2606.24959)

**<font color=#1a73e8>作者：</font>** Stefan Haas, Luca Killmaier, Alireza Javanmardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordinal classification (OC) arises in high-stakes domains such as medicine and finance, where uncertainty quantification must account for the severity of ordinal errors. Conformal prediction (CP) provides distribution-free prediction sets with marginal coverage guarantees; however, its practical effectiveness depends critically on the choice of nonconformity function. We introduce a CP method for ordinal classification based on the ranked probability score (RPS), a proper scoring rule defined over cumulative predictive distributions. Although it reflects ordinal risk quite naturally, it has largely been neglected in conformal ordinal prediction (COP). When used as a measure of nonconformity, RPS yields median-centered contiguous prediction sets by construction. The method is model-agnostic, supports both assessed and grouped ordered categorical outcomes, and permits efficient implementation compared to greedy interval selection procedures. Across multiple ordinal image and tabular datasets, RPS-based CP produces contiguous prediction sets and strikes a favorable balance between prediction set width and the magnitude of ordinal miscoverage relative to existing CP methods.

---


### 16. [Enhancing Clinician Decision-Making via Uncertainty-Aware Multi-Expert Fusion for Stroke Rehabilitation](https://arxiv.org/abs/2606.24960)

**<font color=#1a73e8>作者：</font>** Tamim Ahmed, Thanassis Rikakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tailoring stroke rehabilitation requires assessing how movements are organized, not merely if they succeed. Currently, this assessment is a rate-limiting bottleneck. Instruments like the Action Research Arm Test (ARAT) compress rich behavioral observations into single ordinal endpoints, discarding the movement-quality details that distinguish recovery from compensation. Automated alternatives typically chase accuracy on noisy, single-observer labels to output opaque scores - a technology-centric approach that rarely reaches clinical practice. To address this, we present xAARA: an engine designed to augment rather than replace clinical judgment. From multi-view video, xAARA returns ARAT assessments with calibrated uncertainty and explanations across task, movement-phase, and movement-quality levels. Treating clinical scoring as an ill-posed inference problem, xAARA composes 692 calibrated multimodal models via a Dynamic Bayesian Network with entropy-based gating. It qualifies results against clinical validity rules and defers low-confidence cases. In 105 stroke survivors (788 exercises), xAARA achieved 94.2% task accuracy (Cohen's kappa=0.934) and 81.3% movement-phase accuracy (kappa=0.727), reducing predictive uncertainty by 96.1% compared to single-clinician scoring. For subjective cases, it matched at least one rater 100% of the time and never returned out-of-range scores. Four independent clinicians validated the assessments and indicated willingness to adopt the system. We argue that principled uncertainty quantification and clinician-aligned explainability are the critical bridges moving automated assessment from technical demonstration to a deployable clinical tool.

---


### 17. [Towards Scalable Multi-Task Reinforcement Learning with Large Decision Models](https://arxiv.org/abs/2606.24962)

**<font color=#1a73e8>作者：</font>** Thibaut Kulak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in large-scale sequence modeling has shown that a single model can learn useful representations across highly diverse data distributions. Inspired by these advances, we investigate whether a unified transformer policy can be trained across large collections of heterogeneous reinforcement learning environments.
We introduce LDM-v0, a Large Decision Model trained offline on trajectories collected from thousands of environments spanning multiple domains and modalities. LDM-v0 is a multi-task, multi-modal transformer policy conditioned on histories of observations, actions, rewards, and termination signals, and trained through supervised next-action prediction over offline trajectories. We describe the environment infrastructure, automated data generation pipeline, model architecture, and training methodology used to build LDM-v0, and evaluate its performance across diverse environments. We show that a single pretrained model matches the performance of independently trained task-specific reference policies on approximately 1,000 environments including robotics, autonomous driving, inventory management, cybersecurity, trading, and video games. These results demonstrate the feasibility of large-scale offline pretraining across heterogeneous reinforcement learning environments using a single transformer policy.

---


### 18. [Learning Dynamical Systems from Multiple Sparse Datasets: A Hierarchical Bayesian Modeling Approach](https://arxiv.org/abs/2606.24966)

**<font color=#1a73e8>作者：</font>** Cristian Brugnara, Lea Multerer, Marco Forgione 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating parameters of dynamical systems from sparse, noisy, and irregularly sampled data is often severely ill-conditioned. When multiple related datasets are available, they provide additional information if the shared structure and variability are properly modeled. We propose a hierarchical Bayesian framework for probabilistic meta-learning in dynamical systems, modeling dataset-specific parameters as draws from a shared population distribution. A numerical ODE solver is embedded within gradient-based MCMC to enable efficient posterior inference of the shared population and dataset-specific parameter distribution. Experiments show improved predictive performance over unpooled methods, highlighting the potential for data-efficient system identification in settings with sparse data.

---


### 19. [What Do Language Priors Contribute to Darcy-Flow Inversion? A Mechanistic Audit](https://arxiv.org/abs/2606.24967)

**<font color=#1a73e8>作者：</font>** Taiga Saito, Yu Otake, Daijiro Mizutani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In ill-posed inverse problems, the recovered solution depends as much on the prior as on the data, yet much of the engineering knowledge that could serve as that prior is recorded qualitatively rather than in formal mathematical form. Here we test whether sentence embeddings can act as an inference-time interface for injecting geological descriptions into a learned Darcy-flow inverse solver. Across six synthetic geological classes and an exploratory transfer to a benchmark reservoir model (SPE10), we vary only the conditioning representation and find that text conditioning reduces reconstruction error by 81 % relative to a no-text counterfactual. Most of this gain comes from a categorical, class-level constraint whose value concentrates where the hydraulic head leaves the conductivity field underdetermined, while within-class geometric detail is secondary and pattern-dependent. Compared with a discrete class label, sentence embeddings add little dense-observation accuracy but improve training stability and enable paraphrase-based sensitivity analysis and open-vocabulary inputs. These results show that language priors can serve as an engineering-informatics interface for injecting geological knowledge into learned inverse solvers, while clarifying when they help and what signal they actually carry.

---


### 20. [Training Dynamics of Neural Software Defect Predictors under Coupled Data-Quality Issues](https://arxiv.org/abs/2606.24968)

**<font color=#1a73e8>作者：</font>** Emmanuel Charleson Dapaah, Philip Makedonski, Jens Grabowski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context: Software defect prediction supports maintenance decisions such as testing prioritization, release-risk assessment, and quality monitoring. However, metric-based SDP datasets often contain coupled data-quality issues, especially class imbalance and class overlap. Prior work has mainly measured their impact through endpoint performance, while recent evidence suggests that such issues may also appear in neural training dynamics (gradients, weights, biases, error trajectories). However, these studies examine issues in isolation, leaving open how internal neural network training patterns manifest when data quality issues are coupled.
Objective: We investigate how training-dynamics patterns from class imbalance, overlap, and their coupling can be characterized under interaction-aware conditions in deep learning-based SDP.
Method: We conduct a controlled intervention study on class-level UBD datasets, training a fixed MLP under imbalance-only, overlap-only, and joint conditions across five seeds. Training dynamics are logged per epoch; fidelity is monitored via coupling ratios. Patterns are characterized using effect sizes, trajectories, sensitivity analyses, and rule-based classification.
Expected contribution: The study will produce an interaction-aware empirical protocol and a candidate taxonomy of training-dynamics patterns for coupled data-quality issues in metric-based SDP.

---


### 21. [Frequency Domain Reservoir Computing](https://arxiv.org/abs/2606.24969)

**<font color=#1a73e8>作者：</font>** Klaus Schertler, Xiomara Runge, Andrea Ceni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While the quadratic sequence-length bottleneck of transformers has fueled a resurgence in recurrent models, effectively capturing complex dynamics requires architectures that balance efficient training with highly expressive latent states. Echo State Networks (ESNs) offer a compelling approach by utilizing fixed recurrent weights to circumvent backpropagation through time, enabling a closed-form training solution. However, achieving the expressivity needed for complex tasks demands large reservoirs, exposing an $\mathcal{O}(N^2)$ state-update bottleneck that prevents ESNs from matching the scale of contemporary recurrent models. To address this limitation, we introduce Frequency Domain Reservoir Computing (FRESCO), an ESN architecture operating entirely in the frequency domain while avoiding domain-shift overheads to achieve $\mathcal{O}(N)$ complexity for dense, non-linear recurrent updates. By employing a novel dimensional zero-padding input embedding, a packed \FDh readout, and a natively applied frequency-domain non-linearity, FRESCO drastically reduces computational costs and energy consumption of training and inference. Furthermore, FRESCO matches the state-of-the-art predictive performance on memory benchmarks, sequential classification, and multivariate long-horizon forecasting, offering a scalable path forward for dense recurrent architectures.

---


### 22. [Quantifying Explainable AI-introduced signal noise on ECG data with Spectral Entropy](https://arxiv.org/abs/2606.24974)

**<font color=#1a73e8>作者：</font>** David A. Kelly, Nathan Blake  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainability techniques are used to assess the output of various deep learning models. This is especially true in healthcare, where models need to be trusted and decisions justified. Explainability (XAI) tools use heuristics which often add signal noise to the explanation "core". It is not always obvious what is signal from the model and what is noise from the XAI. We propose the use of spectral entropy as a measure of noise in XAI output. We demonstrate its usefulness in the context of classifying arrhythmias in an ECG dataset with different post hoc explainability techniques.

---


### 23. [Why Do Accumulated Transformations Extrapolate?](https://arxiv.org/abs/2606.24975)

**<font color=#1a73e8>作者：</font>** Mahesh Godavarti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PaTH Attention showed that replacing RoPE's position-indexed rotations with accumulated data-dependent Householder reflections yields strong length extrapolation, though performance degrades at extreme context lengths. We ask whether this depends on Householder-specific structure or reflects a general property of accumulated transformations along source-to-query paths. We study a simpler variant keeping RoPE's block-diagonal SO(2) rotations but replacing position-indexed angles with accumulated token-dependent ones. It shows the same pattern: improved extrapolation then degradation at long contexts. We prove the result extends to accumulated orthogonal transformations satisfying certain regularity conditions: their products become incoherent after finitely many steps, suppressing attention to distant tokens. Accumulated rotations of queries and keys create a finite mixing window independent of context length; per-token suppression learned in training transfers unchanged to any evaluation length, and high-dimensional concentration produces a score gap suppressing far tokens while near-route transport preserves the target signal. Conversely, a lower bound shows accumulated rotations must eventually degrade: as the far set grows, no rotations preserve the near signal without explicit far-mass control. For SO(2) rotations, rotating values too makes residual far contributions combine incoherently, extending the range. Controlled experiments support these predictions: random accumulated rotations substantially improve extrapolation over RoPE, learned token-dependent rotations maintain near-training-length perplexity far beyond the training context, and rotating values helps over queries and keys alone. Rotation-only models still degrade at extreme lengths, while ALiBi stays length-stable, consistent with the need for far-mass control.

---


### 24. [Auto-Configured Explainable Graph Neural Networks for Multi-Site Pollution Prediction](https://arxiv.org/abs/2606.24978)

**<font color=#1a73e8>作者：</font>** Abdelkader Dairi, Fouzi Harrou, Ying Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate particulate matter (PM) prediction is crucial for mitigating air pollution. Graph Neural Networks (GNNs) effectively model spatiotemporal dependencies, but predefined graphs limit adaptability, and some datasets complicate learning. This study introduces a graph construction method based on a confusion matrix from a supervised learning process to dynamically capture inter-class relationships. Additionally, a hybrid loss function that combines energy distance and Huber loss is applied to address the vanishing gradient problem and improve learning stability. The approach is evaluated using air pollution data from the University of Utah AirU Pollution Monitoring Network in Salt Lake City, UT, with five GNN models: Graph Convolutional Networks (GCNs), Simple Graph Convolutional Networks (SGConv), Graph Isomorphism Networks (GINs), Graph Attention Networks (GATs), and GraphSage. The experimental results of single- and multistep predictions confirm that GraphSage achieves the highest accuracy in predicting the concentrations of PM${1}$, PM${10}$, and PM$_{2.5}$ over different time horizons. Furthermore, {\color{black} GNNExplainer (Graph Neural Network Explainer) and PGExplainer (Probabilistic Graph Explainer)} are applied to interpret feature importance and graph structure, ensuring model transparency. Results show improved prediction accuracy, with GNN models outperforming traditional machine learning \textcolor{black}{and deep learning models (i.e., Prophet, Long short-term memory, Gated recurrent units} in air pollution forecasting.

---


### 25. [CKM-Driven Communication-Aware UAV Intelligent Trajectory Optimization for Urban Inspection](https://arxiv.org/abs/2606.24979)

**<font color=#1a73e8>作者：</font>** Yang Xiaomeng, Jia Ziye, Zhu Qiuming 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) are increasingly employed in urban inspection tasks, where reliable communication is critical but challenging due to the severe spatial channel heterogeneity. To address the issue, in this paper, we focus on the communication-aware path planning for multi-UAV tasks, and propose a channel knowledge map (CKM)-driven trajectory planning framework which integrates the channel modeling and trajectory decision-making. Specifically, we apply the diffusion model to construct a time-accumulated CKM and achieve the accurate perception with low flight overhead, which leverages the sparse observation data to reconstruct the high-fidelity global channel quality distribution. Based on the CKM, we propose a global-to-local graph attention network soft actor-critic algorithm. The graph attention network optimizes the complex combinatorial node ordering problem, generating an optimal and communication-aware sequence for the inspection targets. Subsequently, the soft actor-critic algorithm performs continuous action control to ensure the smoothness of the flight path and dynamically avoid communication attenuation areas. Simulation results demonstrate that the proposed method effectively guides UAVs through high-quality channel regions without dependence on real-time channel feedback, significantly improving both the trajectory efficiency and communication reliability.

---


### 26. [Latent Block-Diffusion Temporal Point Processes: A Semi-Autoregressive Framework for Asynchronous Event Sequence Generation](https://arxiv.org/abs/2606.24982)

**<font color=#1a73e8>作者：</font>** Shuai Zhang, Yancheng Chen, Chuan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling and sampling from the underlying distribution of asynchronous event sequences are crucial in various real-world applications, including social networks, medical diagnosis, and financial transactions. Existing autoregressive methods suffer from error accumulation during multi-step generation, while non-autoregressive diffusion methods are typically limited to fixed-length output sequences. In this paper, we propose Latent Block-Diffusion Temporal Point Processes (LBDTPP), a novel semi-autoregressive TPP framework that introduces a latent block diffusion mechanism for high-quality and variable-length event sequence generation. The core idea is to define an autoregressive probability distribution over event blocks in latent space and perform Gaussian diffusion within each block. By sequentially generating blocks while simultaneously sampling events in each block, LBDTPP preserves the length flexibility of autoregressive TPPs and inherits the parallel high-quality generation capability of diffusion models. Theoretically, we derive Wasserstein error bounds showing that, under suitable local approximation and prefix-stability assumptions, block-wise generation can reduce error accumulation compared with event-wise autoregressive generation. Extensive experiments on six real-world benchmark datasets demonstrate that LBDTPP outperforms state-of-the-art TPP baselines in both unconditional and conditional generation tasks. Further empirical analyses verify the benefits of latent-space diffusion and block-wise generation, and reveal the trade-off between generation quality and block size. Our code is available at this https URL.

---


### 27. [Learning Diachronic Representations of Ancient Greek Letterforms](https://arxiv.org/abs/2606.24984)

**<font color=#1a73e8>作者：</font>** John Pavlopoulos, Spyros Barbakos, Lavinia Ferretti 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning representations that remain robust across centuries of variation in handwriting is a key challenge in diachronic representation learning. Taking one of the longest continuously used writing systems, ancient Greek, as a case study, we introduce three datasets for diachronic representation learning: Hell-Char, a curated training set spanning the 3rd-1st centuries BCE, and two evaluation sets, PaLit-Char (2nd-5th c. CE) and Med-Char (9th-14th c. CE). To address the challenges of symbolic variation, scarce data, and systematic degradation, we propose: a similarity-weighted supervised contrastive loss that biases embeddings using dynamically estimated inter-class similarities, and a lacuna-driven augmentation scheme that simulates realistic manuscript corruptions. Trained with these strategies, both a lightweight CNN and a pretrained ResNet achieve strong recognition performance and produce embeddings that more coherently separate character classes than PCA or generic pretrained models. These embeddings enable clustering, identification of stylistic subgroups, and construction of prototype images that visualize diachronic evolution and transitional letterforms. Our results demonstrate that respecting intrinsic inter-letter relationships and augmenting with domain-informed corruptions yield robust, interpretable representations, offering a transferable paradigm for representation learning under scarce, temporally evolving, and noisy conditions. Code and data available at: this https URL.

---


### 28. [When Multi-Sensor Fusion Fails to Generalize: Cattle Posture Classification Under Animal-Level and Temporal Distribution Shift](https://arxiv.org/abs/2606.24986)

**<font color=#1a73e8>作者：</font>** Leutrim Uka, Severino Pinto, Gundula Hoffmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated cattle posture-classification systems frequently report near-perfect accuracy, yet their robustness under realistic deployment conditions remains largely unknown. In particular, it is unclear whether multimodal sensor fusion improves generalisation or leads models to rely on context-specific signals that fail under distribution shift. Here, we evaluate the robustness of automated posture classification (lying versus standing) using collar accelerometers, rumen-bolus sensors, and environmental measurements collected from a pasture-based beef cattle herd across two consecutive years (2024-2025). XGBoost served as the primary model, with Logistic Regression, Random Forest, and Long Short-Term Memory networks evaluated as comparative baselines. Model robustness was assessed under progressively more stringent evaluation protocols, ranging from conventional random train-test splits to leave-one-animal-out validation and cross-year evaluation on an independent cohort of previously unseen animals recorded one year later. While multimodal models achieved strong within-year performance (macro-F1 0.94), the performance declined substantially under cross-year evaluation (macro-F1 0.49). Explainability analysis revealed persistent reliance on rumen-bolus activity and environmental variables even when predictive performance deteriorated. Distribution-shift diagnostics further confirmed substantial differences in feature distributions between recording years. Our findings demonstrate that commonly used evaluation protocols can substantially overestimate real-world performance and that multimodal sensor fusion may reduce, rather than improve, robustness under temporal distribution shift. More broadly, the results highlight that benchmark accuracy alone is insufficient to assess deployment readiness and underscore the need for robustness-centred evaluation in livestock-monitoring research.

---


### 29. [Low-Cost High-Order Singular Value Decomposition for Tensor-Based Reconstruction from Sparse Sensor Measurements: Urban Flow and Air-Quality Applications](https://arxiv.org/abs/2606.24989)

**<font color=#1a73e8>作者：</font>** Arindam Sengupta, Paul Jeanney, Ricardo Vinuesa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban flow and air-quality simulations generate high-dimensional datasets describing velocity and pollutant transport across multiple spatial, temporal, and physical-variable dimensions. Reconstructing these fields from sparse sensor measurements is a fundamental challenge in environmental monitoring, digital twins, forecasting, and data assimilation. Existing low-cost reconstruction approaches are commonly based on matrix decompositions, which require multidimensional datasets to be flattened into two-dimensional snapshot matrices, thereby discarding important structural information. This work introduces the low-cost High-Order Singular Value Decomposition (lcHOSVD), a novel tensor-based sparse-sensing reconstruction framework for high-dimensional environmental fields. To the authors' knowledge, this is the first methodology that combines sparse sensing and HOSVD for field reconstruction. Unlike matrix-based approaches, lcHOSVD preserves the natural tensor structure of the data, enabling the exploitation of correlations across spatial, temporal, and physical-variable dimensions while substantially reducing the computational requirements of conventional HOSVD. The methodology is applied to urban flow and air-quality datasets, where three-dimensional velocity and pollutant concentration fields are reconstructed using only 1-4% of the available spatial locations. While lcSVD provides larger computational speed-ups, lcHOSVD consistently achieves lower reconstruction errors in configurations characterized by strong multidimensional coupling and heterogeneous dynamics across dimensions. Additional sensor-anisotropy analyses demonstrate that the tensor formulation is significantly more robust to uneven sensor distributions, a common situation in practical environmental monitoring networks.

---


### 30. [The Geometry of Sequential Learning: Lie-Bracket Prediction of Transfer Order](https://arxiv.org/abs/2606.24993)

**<font color=#1a73e8>作者：</font>** John Sweeney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential learning is order-dependent: from Pile-style next-token domain adaptation to instruction-SFT and DPO, N candidate sources induce N! possible curricula. We show that the local order effect is governed by a computable geometric quantity, the Lie-bracket commutator of gradient update fields, yielding a pairwise score for whether A->B or B->A is better for a target domain. The pairwise bracket primitive also defines a Lie-Bracket Tournament: with a shared theta_0 target-gradient reference, Hessian symmetry gives Borda/row-sum scores from one Hessian-vector product per source, O(N) dot products, and an O(N log N) sort, without materializing the O(N^2) edge matrix. Empirically, the planner reaches 98.1%/98.9% pairwise accuracy at k=1 for instruction-SFT/DPO, remains at 73.1%/72.2% at k=20, and preserves the original pretraining-domain evidence with 82.4-92.0% accuracy across four LLMs and 91.1% on diffusion. At curriculum scale, it recovers the best of all 3! schedules in 87.5% of trials, ranks 85 Stack programming-language source domains for a Python target in the 99th sampled percentile, and reaches the 99.0-99.6th sampled percentile on 56 MMLU subjects, sharply above the reported descending gradient-norm baseline. These results reframe sequential learning as a geometric tournament problem: commutators provide both local pairwise order information and a scalable primitive for many-domain schedules.

---


### 31. [From Forecasting Leaderboards to Deployment Decisions: A Fail-Closed Certification Protocol](https://arxiv.org/abs/2606.24996)

**<font color=#1a73e8>作者：</font>** Geumyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting leaderboards rank models by predictive quality, but their winners are often read as deployment-ready top-1 advice. That reading can fail when forecasts are passed through a fixed decision interface, such as an alert threshold, a top-k budget, or a switching-cost policy. We study when a forecast-side winner can be certified as deployment-actionable for a specified interface and deployed utility. We introduce a fail-closed certification protocol whose gates are sufficient evidential conditions for a strong claim: a friction-caused, non-tie, statistically supported, and recurrent deployment-side reversal. Traffic-Hourly provides a certified anchor: winners agree at zero friction, but positive switching friction makes the forecast winner deployed-suboptimal. A locked native audit tests overclaiming: across 22 verified candidates and 362 full-grid cells, 155 apparent forecast/deployment winner inversions are blocked before certification. The contribution is not a new forecaster, metric, or universal utility, but a conservative protocol for deciding when forecasting leaderboard winners should be read as deployment-actionable top-1 advice.

---


### 32. [What's in an Earth Embedding? An Explainability Analysis of Location Encoders](https://arxiv.org/abs/2606.24997)

**<font color=#1a73e8>作者：</font>** Livia Betti, Sebastian Ricke, Ivica Obadic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geographic implicit neural representations (INRs) learn to map any coordinate on Earth to a location embedding, implicitly encoding geospatial data into the weights of a neural network. Location embeddings are widely used off the shelf as general-purpose geospatial representations, yet users lack principled tools to audit what geographic or semantic information these embeddings capture. In this work, we analyze the information content of geographic INRs through their location embeddings. We decompose these embeddings into human-interpretable features$\unicode{x2014}$namely, (i) sparse latent concepts, (ii) natural language concepts, and (iii) visual features. The latent concept embeddings are learned using sparse autoencoders. To recover natural language concepts, we apply sparse linear concept embeddings (SpLiCE) over a predefined geospatial dictionary. Finally, visual features are extracted using saliency maps derived from CLIP Surgery. We show that location embeddings can be decomposed into human-interpretable representations while retaining high reconstruction capability, revealing interpretable geographic structures such as forests, deserts, and urban features. Across methods, sparse decompositions expose systematic differences in encoded information, ranging from urban structures to broader biome and climate signals, and pretraining-space saliency maps further highlight complementary features such as roads and landmarks. We hope this work provides a first step toward interpretable geospatial representations.

---


### 33. [A Zeroth-Order Deep Learning Method for Fully Nonlinear Parabolic Partial Differential Equations with Unknown Coefficients](https://arxiv.org/abs/2606.24999)

**<font color=#1a73e8>作者：</font>** Yanwei Jia, Du Ouyang, Huyên Pham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional partial differential equations (PDEs) with unknown coefficients arise widely in scientific machine learning, including continuous-time reinforcement learning, yet solving them efficiently in a data-driven way remains challenging. Existing deep learning solvers often rely on repeated automatic differentiation to evaluate differential operators, which can cause instability and amplify derivative errors in high dimensions, while probabilistic methods based on stochastic representations require explicit knowledge of the data-generating dynamics and therefore do not apply to black-box environments. We introduce two types of simulators as data-generating mechanisms, and take a ``representing-then-learning" approach that learns the solutions and their derivatives under settings where the underlying PDE operators are accessible only through simulations and pointwise evaluations. Our representation of derivatives relies on the zeroth-order derivative (ZOD) estimators derived from perturbed Monte Carlo trajectories. This fully model-free approach generates targets for the gradient and Hessian networks using only function evaluations. We provide a statistical learning analysis of the proposed approach, including a bias--variance tradeoff for ZODs. Assuming a standard contraction property of the underlying operator, we establish a non-asymptotic error bound that decomposes the total error into discretization error, approximation error, statistical error, and ZOD bias. Crucially, we derive the sample complexity of the learned representations in (weighted) Sobolev space, characterizing the error up to second-order derivatives. Numerical experiments illustrate the competitive performance of the method in moderate and high dimensions.

---


### 34. [Geo-Strat-RL: Learning Geological Event Reasoning from Verifiable Tasks](https://arxiv.org/abs/2606.25000)

**<font color=#1a73e8>作者：</font>** Lukas Mosser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To evaluate whether vision-language models can reason about geological histories, it is necessary to construct observations for which the underlying process history is known. Furthermore, reasoning over geological histories is not just a question of recognizing visual patterns, but also of understanding temporal and structural relationships that may be only indirectly visible or highly ambiguous. When ground-truth event histories are not uniquely identifiable or are unavailable, it remains an open challenge to teach models capable of visual reasoning to produce valid geological reconstructions that are consistent with both observed evidence and geological principles. We therefore investigate whether defining a verifiable geological reasoning task can improve geological event reconstruction across observation domains through reinforcement learning with verifiable rewards (RLVR). To this end, we present Geo-Strat-RL, a synthetic environment that generates stratigraphic observations and compact visible-evidence event histories. The environment combines a geological generator with an executable verifier that scores chronology, event identity, deposition, and structural relationships. We show that RLVR improves geological reconstruction in vision-language models (VLMs), increasing geological content scores on held out stratigraphic diagrams. We further evaluate the same held-out geological histories in a synthetic seismic observation domain by converting the generated scenes into acoustic-impedance-derived amplitude sections. In this controlled paired-renderer setting, we present evidence that geological reasoning learned from stratigraphic diagram-domain RLVR training transfers to synthetic seismic representations without seismic-specific training examples, supporting the hypothesis that RLVR can teach reusable geological reasoning concepts across related observation formats.

---


### 35. [Erased, but Not Gone: Output Forgetting Is Not True Forgetting](https://arxiv.org/abs/2606.25001)

**<font color=#1a73e8>作者：</font>** Teresa Pui Yee Yong, Win Kent Ong, Chee Seng Chan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning (MU) is commonly judged by output forgetting, such as low forget-set accuracy or reduced logit-level membership inference. But if output-level success can coexist with retraining-inconsistent residuals in representation space, what kind of forgetting are current evaluations actually certifying? We study this question through retraining-consistent representation forgetting, using the retrained model (i.e., trained from scratch without the forget data) as an operational reference for correct forgetting. Across multiple unlearning methods, datasets, and models, our theoretical analysis and empirical results show that standard output-level evaluation can systematically overestimate the success of unlearning. Under this stronger lens, current methods often appear forgotten at the output layer while exhibiting a structured mismatch relative to retraining. They partially align with retraining on forget samples, remain more inconsistent on retain samples, and leave residual discrepancy concentrated along retraining-related directions rather than diffuse in representation space. This structured mismatch is characterized by forget/retain asymmetry, directional mismatch, and concentrated residuals along retraining-related directions. These results suggest that current MU is often evaluated for apparent forgetting rather than retraining-consistent forgetting. More broadly, retraining reveals what output forgetting hides.

---


### 36. [TRACER: Training-Free Closed-Loop Structured Inference for Traffic Accident Reconstruction](https://arxiv.org/abs/2606.25002)

**<font color=#1a73e8>作者：</font>** Yanchen Guan, Chengyue Wang, Bin Rao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic accident reconstruction is a forensic inverse problem that requires recovering physically consistent motion from sparse and heterogeneous evidence. Existing learning-based approaches predominantly optimize for semantic plausibility or visual realism, rather than quantitative agreement with measurable geometry and dynamics. Here, we present TRACER, a training-free framework that formulates reconstruction as a closed-loop structured inference process. Instead of directly generating dense trajectories, our framework constructs and iteratively refines event-anchored motion hypotheses under geometric, kinematic, and interaction constraints, guided by structured case memory and consistency-driven diagnosis. This design enables incremental, interpretable corrections when evidence is insufficient, making the accident reconstruction process more aligned with the workflow of human experts. Experiments on real-world accident data show that TRACER achieves improved geometric fidelity, velocity consistency, and collision accuracy over both data-driven and physics-based baselines.

---


### 37. [Adaptive Joint Compression and Synchronisation in Federated Split Learning for IoT Rainfall Prediction](https://arxiv.org/abs/2606.25003)

**<font color=#1a73e8>作者：</font>** Wenjie Ding, Yi Sin Lin, Jiale Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated split learning (FSL) enables collaborative training across bandwidth-constrained IoT devices, but repeated activation and gradient exchange creates a communication bot-tleneck. Prior work optimises either activation compression or synchronisation frequency in isolation. This paper presents an FSL framework for IoT rainfall prediction that jointly regulates activation compression and the synchronisation interval \r{ho} via a latency driven scheduler on a server with per client EMA smoothing. The system is evaluated on hourly ERA5 data from 11 weather stations through a 17 scenario simulation matrix and a four scenario Raspberry Pi deployment over a real wide-area link. The simulation matrix validates scheduler switching across low, high, and mixed latency profiles, while the Pi deployment validates the high latency endpoint selected by the same policy. AUPRC varies only slightly across configurations (0.6381-0.6484 in simulation; within 0.011 on Pi), indicating that aggressive quantisation and sparser aggregation do not materially degrade predictive quality in this setting. On Pi, the selected endpoint (int8 with rho=3) achieves an 87% reduction in activation upload payload and a 54% reduction in synchronisation traffic relative to the float32 baseline, while reducing runtime jitter from +/-688 s to +/-10 s.

---


### 38. [Certification of Machine Learning Models via Directional Sharpness](https://arxiv.org/abs/2606.25004)

**<font color=#1a73e8>作者：</font>** Gefei Tan, Adria Gascon, Sarah Meiklejohn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In machine learning, model certification has been identified as an important method for gaining assurance about a model's trustworthiness and quality. A model's quality is largely determined by its ability to generalize, i.e., to perform well on data beyond what it was trained on. It is not possible to certify generalization directly, however, as it depends on unknown data and is not directly measurable. Proxies such as test accuracy can be misleading when the training process is perturbed (intentionally or accidentally), and metrics such as sharpness -- which has an empirically supported link to generalization -- are computationally expensive and can also serve as unreliable signals when training deviates from a prescribed procedure. In this work, we propose directional sharpness, a metric designed to efficiently and reliably indicate generalization despite potential training deviations. We provide empirical and analytical evidence that directional sharpness (1) correlates more strongly with generalization than existing metrics and (2) identifies models with poor generalization more reliably than existing metrics. Furthermore, directional sharpness is efficiently computable in model auditing settings, where the verifier has access to training data, and via zero-knowledge proofs that certify quality without revealing training data.

---


### 39. [Scalable Peptide Design via Memory-Efficient Equivariant Transformer](https://arxiv.org/abs/2606.25006)

**<font color=#1a73e8>作者：</font>** Rui Jiao, Xiangzhe Kong, Yinjun Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Target-specific peptide design requires sequence and structure co-design under full atom geometric constraints. Latent generative frameworks offer an effective route for this problem by compressing fine grained atomic structures into block level latent representations and performing conditional generation in a compact latent space. However, the scalability of such systems depends heavily on the geometric backbone used throughout their encoding, decoding, and denoising components. We introduce MEET (Memory Efficient Equivariant Transformer), an E(3) equivariant backbone for scalable atomistic peptide modeling. MEET maintains coupled invariant scalar and equivariant vector feature streams, while reformulating geometric computation around memory efficient attention. It initializes vector features through global coordinate aggregation, incorporates pairwise distances through augmented query and key dot products, and injects covalent bond information through sparse bond adaptation. Integrated into a VAE and latent diffusion pipeline for full atom peptide generation, \model{} achieves linear memory scaling with atom count and improves generation quality over existing peptide design methods. Experiments on large scale AFDB derived datasets further show that the proposed backbone supports systematic model and data scaling, leading to better binding affinity, physical validity, and sample diversity.

---


### 40. [Multi-Stream Temporal Fusion for Financial Fraud Detection](https://arxiv.org/abs/2606.25007)

**<font color=#1a73e8>作者：</font>** Mohammadamin Dashti Moghaddam, Nick Sciarrilli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial fraud detection in digital banking requires reasoning over multiple heterogeneous event streams -- transactions, login sessions, risk signals -- that individually appear benign but collectively reveal fraudulent patterns. We propose the Multi-Stream Fraud Transformer (MSFT), a unified architecture that encodes each event stream with independent Transformer encoders and fuses their representations through configurable mechanisms. We conduct a systematic ablation study comparing five fusion strategies: concatenation, gated fusion, time-aware positional encoding, cross-stream attention, and a full combination. On a large-scale dataset (10M users, 1.5% fraud rate) with 85M parameter models, we demonstrate that (1) sequence models significantly outperform gradient-boosted trees operating on aggregated features (0.74 vs. 0.99 AUROC), (2) per-stream encoding is essential -- a single-stream Transformer baseline with matched parameter budget reaches only 0.82 AUROC, an 18-point gap that confirms the multi-stream inductive bias is necessary, (3) time-aware positional encoding achieves the highest discrimination (0.9961 AUROC), (4) gated fusion yields the best precision (0.989) suitable for production deployment, and (5) the risk event stream provides the strongest individual signal contribution. We further validate on proprietary production data from a digital banking platform, showing over 22% relative AUROC improvement over the XGBoost baseline.

---


### 41. [Noise-Aware Boundary-Enhanced Generative Learning for Ultrasound Speckle Reduction](https://arxiv.org/abs/2606.25009)

**<font color=#1a73e8>作者：</font>** Yuexi Gu, Mengqi Wu, Yongheng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound is a non-invasive, real-time, and cost-effective imaging technique widely used in clinical diagnosis. However, its diagnostic efficacy is often compromised by inherent speckle noise that degrades image quality and obscures underlying anatomical structures. Existing speckle reduction methods tend to over-smooth tissue boundaries and generalize poorly to heterogeneous noise levels. To address these limitations, we propose a Noise-Aware Boundary-Enhanced Generative Learning (NBGL) framework for ultrasound speckle reduction, which simultaneously preserves annotated anatomical boundaries and adapts to varying noise levels. The NBGL framework consists of a speckle reduction branch and a boundary enhancement branch. The former leverages generative learning to suppress speckle noise, while the latter learns boundary-sensitive representations to preserve target anatomical structures. Furthermore, a noise-aware interaction weight generation (NIWG) module estimates the speckle noise level via 3D Laplacian filtering and a median absolute deviation estimator, and translates it into an adaptive interaction weight. This weight is incorporated into a weighted feature-wise linear modulation (wFiLM) module to adaptively modulate cross-branch feature coupling, thereby improving robustness to varying noise levels. Extensive evaluations on 141 3D transvaginal ultrasound volumes demonstrate that NBGL consistently outperforms state-of-the-art methods in speckle reduction and structural preservation across six noise levels, while maintaining consistency with annotated anatomical boundaries.

---


### 42. [Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns](https://arxiv.org/abs/2606.25010)

**<font color=#1a73e8>作者：</font>** Vatsal Baherwani, Zixi Chen, Shikai Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural scaling laws for transformer language models predict smooth improvements in pretraining loss with increasing parameters, but downstream capabilities such as in-context learning are known to emerge abruptly past a certain model scale. In this paper, we show that emergent capabilities arise stochastically throughout training, with larger models acquiring them earlier on average. We demonstrate that the emergence of capabilities such as pattern completion and indirect object identification corresponds to the abrupt learning of task-relevant attention patterns. To isolate this phenomenon, we train transformer models on synthetic linear map and cellular automata datasets, and we show that the difficulty of learning attention patterns depends on context length and pattern sparsity. Moreover, scaling the number of attention heads improves learning efficiency on our synthetic tasks, while increasing the head dimension yields diminishing returns past a minimum capacity. We additionally investigate architectures with alternative attention mechanisms, showing that MLP-Mixer outperforms a transformer on linear map tasks with complex attention patterns. Our findings provide a mechanistic insight into emergence, showing that downstream capabilities arise abruptly due to the intrinsic difficulty of learning sparse attention patterns in transformer models.

---


### 43. [Chorus II: Cross-Request Sparsity Reuse for Efficient Image-to-Video Generation](https://arxiv.org/abs/2606.25040)

**<font color=#1a73e8>作者：</font>** Hao Liu, Chenghuan Huang, Hao Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Serving diffusion models for image-to-video generation is computationally expensive, posing significant challenges for large-scale deployment. Real I2V workloads often contain similar requests, such as repeated effect templates, related subjects, and recurring shot layouts. Existing cross-request acceleration methods mainly exploit this redundancy through feature reuse. We observe that similar I2V requests also share highly consistent sparse attention patterns, enabling historical sparse masks to serve as request-conditioned priors with almost no online mask-prediction overhead. We propose a cross-request reuse framework centered on \textbf{sparsity reuse}, with \textbf{feature reuse} as an optional extension safeguarded by a lightweight \textbf{guidance enhancement}. Our sparsity reuse is implemented as shared sparse mask reuse, which reuses high-quality sparse masks from similar historical requests to avoid per-request online mask prediction. Optional feature reuse applies downsampled computation to highly redundant spatiotemporal regions, mitigating boundary artifacts while preserving efficiency gains. Guidance enhancement reinforces image/text conditioning after reuse, mitigating semantic drift and condition-adherence issues. Experiments show that default sparsity reuse configuration preserves generation quality with a \textbf{2.16$\times$} speedup.

---


### 44. [What Does It Mean to Break a Distillation Defense?](https://arxiv.org/abs/2606.25059)

**<font color=#1a73e8>作者：</font>** Lena Libon, Pura Peetathawatchai, Michael Aerni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Black-box LLMs (accessible only via API) are vulnerable to distillation attacks, in which an attacker queries the model and trains a student on its outputs. A recent line of work proposes output perturbation defenses that modify the teacher's output to reduce student performance while preserving utility for legitimate users. As a relatively new family of approaches, output perturbation defenses lack a shared threat model, making it difficult to compare them, reason about composing them with other attacks, or evaluate their robustness against realistic adversaries. This underspecification matters beyond technical evaluation: when defenses are deployed to protect intellectual property or justify regulatory compliance, an imprecise threat model can create a false sense of security. We propose a threat model framework that describes attackers along three dimensions: a query budget, a data budget, and an interface profile that captures how attackers interact with the API. Using antidistillation sampling as a case study, we show that whether the defense is considered effective depends on the assumed threat model. We argue that future work on distillation defenses, along with any governance or policy frameworks built around them, should explicitly specify and stress-test attacker capabilities along our three dimensions.

---


### 45. [Adapt Only When It Pays: Budgeted Decision-Loss Priority for Delayed Online Time-Series Adaptation](https://arxiv.org/abs/2606.25068)

**<font color=#1a73e8>作者：</font>** Xibai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online time-series forecasters receive labels only after horizon-dependent delays, while every adaptation step spends limited compute. We study when an online learner should update, not how to adapt at every opportunity, and introduce ADOWIP: a residual-adapter framework with sealed delay queues, exact budget accounting, and auditable update telemetry. Its main scheduler is an observed decision-loss priority gate that updates only after feedback is revealed, when downstream loss, optionally penalized by prediction MSE, exceeds a calibrated empirical quantile and budget remains. We prove hard-budget feasibility, projected-OGD regret for a convex linear accepted-update subproblem, and stability plus conditional finite-sample gate-selection statements. On public ETT capacity-planning tasks, a frozen calibration/evaluation split selects a gate that lowers held-out decision loss against always, fixed-period, and drift-triggered exact-update baselines under matched compute. Secondary threshold/load-index ETT suites are mixed: 33 of 41 selected contrasts clear the stricter cross-artifact Holm family, and the 8 nonpassing rows are explicitly excluded from primary claims. The same protocol improves an external UCI Bike capacity proxy with 20/0 held-out wins, and a fixed gate passes three full-year Capital Bikeshare station-rebalancing contrasts. Probe-based and finance experiments remain negative, delimiting the current scope of decision-prioritized adaptation.

---


### 46. [GCT-MARL: Graph-Based Contrastive Transfer for Sample-Efficient Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.25073)

**<font color=#1a73e8>作者：</font>** Animesh Animesh, Satheesh K Perepu, Kaushik Dey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In cooperative multi-agent reinforcement learning (MARL), from a deployment perspective, it is challenging and expensive to train agents from scratch for each new environment or task. In this work, we propose GCT-MARL, a transfer learning framework that builds on the multi-view graph contrastive backbone of MAIL and augments it with a per-view, adaptively weighted alignment loss and a two-phase training protocol specifically designed for transfer across populations of varying sizes and compositions. We empirically demonstrate that the proposed framework markedly accelerates convergence on the target task relative to from-scratch training, in both homogeneous (within-faction, varying N) and heterogeneous (cross-faction and mixed unit-type) transfer scenarios. Furthermore, we show that the framework naturally supports continual learning by sequentially chaining the two-phase transfer protocol across a series of related tasks. Overall, this work provides a unified approach to mitigating key limitations in current MARL transfer methods with new insights at both methodological and empirical levels.

---


### 47. [FreeStory: Training-Free Character Consistency for Free-Form Visual Storytelling](https://arxiv.org/abs/2606.25079)

**<font color=#1a73e8>作者：</font>** Sibo Dong, Ismail Shaheen, Sarah Adel Bargal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual storytelling aims to generate image sequences that are both aligned with narrative prompts and consistent in character appearance across images. Recent training-free methods improve character consistency by reusing attention features, but rely on structured prompts where full character descriptions are repeated in every prompt. This assumption simplifies the task but deviates from natural storytelling, where characters are typically introduced once and later referred to using pronouns or type-based expressions. We propose \textbf{FreeStory}, a training-free framework that reformulates character consistency under free-form prompts as entity-grounded feature reuse. Our method associates reference mentions with their corresponding character descriptions and combines dynamic character masks, correspondence-aware feature matching, key-value injection, and query blending to preserve identity while retaining generation diversity. We also introduce \textbf{FreeStoryBench}, a benchmark for this setting that includes both single- and multi-character stories. Experiments show that FreeStory achieves state-of-the-art performance among training-free methods on structured benchmarks and stronger overall consistency over baselines under free-form prompts.

---


### 48. [Neural Network Quantization by Learning Low-Loss Subspaces](https://arxiv.org/abs/2606.25087)

**<font color=#1a73e8>作者：</font>** Vladimir Protsenko, Mikhalina Kharkevich, Alexander Vashchilko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural network quantization aims to find a discrete representation of parameters that preserves the performance of a full-precision (FP) model as faithfully as possible. Enforcing discrete constraints perturbs parameters away from a well-optimized minimum, generally resulting in performance degradation. Recent studies indicate that low-loss FP solutions are not isolated, but instead belong to connected low-loss subspaces of the loss landscape, where the loss maintains nearly the same minimum value. Models sampled from these subspaces are diverse and retain high accuracy. This raises the question: can a quantized model be constructed to lie within a low-loss subspace of the FP model, thereby automatically preserving performance? We address this question by learning quantization-aware linear paths in weight space optimized to minimize loss. We demonstrate that the midpoint of the resulting subspace is, by design, quantization-friendly and that its direct quantization yields performance comparable to that of quantization-aware training. The proposed procedure offers a novel perspective on weight quantization and, in contrast to conventional methods, neither relies on the straight-through estimator nor involves explicit discretization during training.

---


### 49. [How Modular Is a Frontier Mixture-of-Experts? A Pre-registered Causal Test in Which Apparent Expert Modularity Mostly Dissolves](https://arxiv.org/abs/2606.25092)

**<font color=#1a73e8>作者：</font>** Tony Salomone, Deep Gandhi, Ali Asaria  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models route each token to a few of many experts, inviting the hypothesis that experts form functional modules tied to capabilities or languages. We test this causally on Command A+, a frontier open-weights MoE (218B total / 25B active; 128 experts, 8 active, +1 shared). We build a routing-mass atlas, pre-register six family-to-axis hypotheses before any intervention, and ablate each family at inference time against a size-matched random-expert null, measuring whether it selectively breaks its own axis (worst off-target effect at most one third of on-target). Crucially, we test the same families under four metrics and a held-out, independent-corpus run with bootstrap confidence intervals. Our finding is cautionary: robust functional modularity is rare and measurement-dependent. Of six pre-registered families, only one, the Arabic-language family, is a clean selective module that survives an independent corpus and a conservative statistical bar (1/6; a more permissive pre-registered point rule admits 3/6, but that count is threshold-sensitive). Every other family has a real causal effect yet fails selectivity, and its apparent modularity flips with the measurement: with the corpus, the metric, and the statistical bar. A positive control on Qwen3-30B-A3B recovers its published disjoint structure, confirming the method detects modularity when present. The verdict reproduces on the un-quantized BF16 model, ruling out a 4-bit quantization artifact. We conclude that ablation-based modularity verdicts are not safe unless the corpus, metric, and statistical bar are controlled. We release the atlas and ablation data.

---


### 50. [Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion](https://arxiv.org/abs/2606.25097)

**<font color=#1a73e8>作者：</font>** Sahil Kadadekar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates inference by letting a draft model propose tokens for a target model to verify, raising a concrete safety question: at temperature zero, can draft-side behavior leak into safety-scored outputs? We answer with Typical-Acceptance Invariance Screen (TAIS), a behavioral-equivalence screen that pairs target-only and speculative outputs on the same safety battery and requires byte-identity evidence, TOST equivalence at +/-3pp, and per-task Cohen's h below a calibrated null cutoff of |h| < 0.1. Applied to a 16,783-sample confirmatory core plus 44,066 matched expansion samples (fp16/bf16 execution, canonical and DPO-adversarial drafts, GPTQ-4bit drafts, two seeds, and four safety benchmarks), the tested temperature-zero vLLM stacks show no detectable safety divergence under TAIS. The largest absolute Cohen's h on matched target-only versus speculative refusal is 0.024, roughly an order of magnitude below the conventional trivial-effect floor; 25 of 27 per-task TOST contrasts pass at the +/-3pp margin (the two non-pass contrasts are capability-domain Wald-CI edge cases at identical ceiling rates, not genuine non-equivalence); the DPO-adversarial draft produces byte-identical output to the canonical draft across 4,006 samples; and bf16 changes 36%-53% of output bytes without moving any per-task safety rate outside equivalence. A separate 4,006-sample 70B production-scale probe, which lacks a matched 70B target-only arm and is therefore not counted as a TAIS pass, produces AdvBench refusal 0.839 over 700 AdvBench completions with 95% Wilson CI [0.809, 0.864]. We make no claim about sampling temperatures, untested frameworks, untested model families, or tree-speculation variants such as EAGLE and Medusa.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
