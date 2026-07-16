# 📦 其他研究 | 2026年07月17日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 1. [FixItFlow: Automated Troubleshooting Guide Generation from Cloud Incidents](https://arxiv.org/abs/2607.13035)

**<font color=#1a73e8>作者：</font>** Srihari Unnikrishnan, Jaskaran Singh Walia, Drishti Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cloud services experience frequent incidents that require rapid diagnosis and resolution. Troubleshooting guides help engineers respond consistently, but creating them manually is labor-intensive, resulting in incomplete coverage and outdated documentation. We present FixItFlow, an automated system that generates troubleshooting guides from historical incident data using large language models. The system extracts diagnostic patterns from engineer actions, synthesizes structured guides with verified commands, and enforces strict validation to prevent fabricated content. In our evaluation with 26 engineers, generated guides achieved 61.5\% positive ratings for clarity and demonstrated a 2.3x reduction in mitigation time for incidents with associated guides. These results indicate that automated guide generation can improve incident response while reducing documentation burden on engineering teams.

---


### 2. [OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets](https://arxiv.org/abs/2607.13037)

**<font color=#1a73e8>作者：</font>** Haolin Xue  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a data contributor requests removal, model trainers face a practical gap: unlearning algorithms require a forget set, yet no tool can locate which training records belong to a given author. Existing provenance systems operate at file or dataset level, forcing catastrophic over-deletion. We present ob, a record- and token-level data provenance system that propagates author identity through data processing pipelines and resolves revocation requests into precise forget sets via deterministic queries. Evaluation on 219,555 Wikipedia pages demonstrates that record-level provenance eliminates dataset-level over-deletion (from 101x to 1.3x), while integration adds 1.3-4.0% throughput overhead (HuggingFace) and 2.1-19.0% (Datatrove) on wiki data. On a 1.7B model, provenance-based forget sets improve unlearning by 42% over random baselines.

---


### 3. [Automatic Differentiation from Scratch: How PyTorch Computes Gradients in Physics-Informed Neural Networks](https://arxiv.org/abs/2607.13042)

**<font color=#1a73e8>作者：</font>** Abdeladhim Tahimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper traces, with explicit numerical values, how PyTorch's automatic differentiation (AD) engine computes gradients for Physics-Informed Neural Network (PINN) training -- a setting that requires two levels of differentiation: computing the physics derivative $\hat{y}'(t)=d\hat{y}/dt$ through the network, and computing parameter gradients $\nabla_\theta L$ of a loss that itself depends on $\hat{y}'(t)$. Using a 1-3-3-1 multilayer perceptron and the initial value problem $y'(t)+y(t)=0$, $y(0)=1$, we trace the complete pipeline at every node: the computational graph built during the forward pass, the reverse-mode backward traversal that computes all 22 parameter gradients in a single pass, and the graph-on-graph mechanism by which \texttt{create\_graph=True} enables correct differentiation through the physics-informed residual. Every adjoint value is verified against the hand derivations of Tahimi (2026), connecting the $P/Q$ sensitivity framework to the vector--Jacobian products used by PyTorch's autograd engine.

---


### 4. [Beyond Backbone Backpropagation: A Decoupled Strategy for Efficient Transfer Learning](https://arxiv.org/abs/2607.13043)

**<font color=#1a73e8>作者：</font>** Daniel Vila-Cruz, Laura Morán-Fernández, Verónica Bolón-Canedo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models achieve state-of-the-art image classification but face deployment challenges due to computational costs and energy demands. We propose a lightweight training strategy that adapts normalization layers of the model to the new domain and decouples feature extraction from classifier optimization, reducing overhead by precomputing features only once. A redesigned classifier head with margin-based weighted loss further minimizes ambiguity without end-to-end backpropagation. Evaluated across four CNN architectures (ResNet18, ResNet50, MobileNet, DenseNet121), three Transformer models (ViT, Swin and DeiT) and three medical datasets (Brain Cancer MRI, BreakHis and PatchCamelyon), our approach significantly reduces the required training time with only a marginal accuracy trade-off, often matching or surpassing baseline performance. This efficiency translates to reducing CO2 by orders of magnitude, offering a practical and environmentally sustainable solution for resource-constrained clinical or prototyping environments.

---


### 5. [The Perplexity Trap: When Patent Law Makes Human Writing Look Like AI](https://arxiv.org/abs/2607.13044)

**<font color=#1a73e8>作者：</font>** Anubhab Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The European Patent Office (EPO) reported record filings in 2025, and the 2026 EPO Guidelines hold applicants strictly responsible for LLM-assisted content under Article 83 and Rule 42, creating pressure to triage suspected AI-generated patent text. Two constraints make this hard. First, realistic prosecution settings often have only consumer GPUs with about 8 GB VRAM, not datacenter-class scoring stacks. Second, Article 84 of the European Patent Convention requires claims to be clear and concise, pushing human drafting onto the same low-perplexity, low-burstiness manifold that LLMs occupy. We benchmark three open-source zero-shot detectors on 500 granted EPO H04 telecom patents versus 500 LLM-generated counterparts using five prompting strategies, all under the consumer hardware envelope. At claim level, all detectors exceed 60 percent false-positive rate: Binoculars 78.3 percent, Fast-DetectGPT 61.3 percent, DetectGPT 80.5 percent. The failure persists under Qwen2.5-3B-Instruct regeneration, LoRA-adapted Pythia-2.8B scoring heads, cross-IPC replication on A61K, C07D, and F03D (mean FPR 84.6 percent), and H100 re-evaluation with published Falcon-7B and GPT-J-6B heads, arguing the issue is structural rather than substitute-model capacity. A seven-feature linguistic-complexity logistic regression reaches 74.0 percent accuracy at 28.1 percent FPR, a 13 percentage-point gain over a perplexity-only baseline at a comparable operating point, without using likelihood at inference and within the same hardware budget.

---


### 6. [Federated Explainable Artificial Intelligence: Roles, Architectures, Evaluation, and Open Challenges](https://arxiv.org/abs/2607.13045)

**<font color=#1a73e8>作者：</font>** Masoume Gholizade, Fabrizio Ruffini, Pietro Ducange 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) has emerged as a key paradigm for privacy-preserving collaborative model training across distributed and heterogeneous data sources. By keeping raw data local, FL addresses data confidentiality concerns, yet it does not resolve the opacity of modern machine learning models. In parallel, Explainable Artificial Intelligence (XAI) has gained attention for improving transparency, trust, and accountability, particularly in high-stakes domains. Their intersection has given rise to Federated Explainable Artificial Intelligence (FedXAI) paradigm, which aims to jointly satisfy privacy and explainability requirements. This survey provides a systematic review of FedXAI, highlighting the transition of explainability from a post-hoc tool to an integral component of the FL lifecycle. We show how explainability supports aggregation, personalization, robustness, coordination, and system-level decision making. To organize the literature, we introduce a taxonomy that classifies FedXAI methods by the role of explainability, model and explainer types, explanation scope, integration level, FL settings, and data heterogeneity. We review approaches ranging from model-agnostic explanations to interpretable federated models and explainability-aware aggregation mechanisms. We also examine evaluation practices and discuss the lack of standardized benchmarks and metrics for measuring explanation quality, stability, privacy leakage, and computational overhead. Finally, we identify key challenges, including explainability under non-IID data, explanation-centric security threats, communication-efficient XAI, continual FedXAI, and the integration of domain knowledge and regulatory constraints. By consolidating existing work and identifying key gaps, this survey serves as a reference framework for designing trustworthy, transparent, and privacy-preserving federated AI systems.

---


### 7. [What Your Model Threw Away and Why You'll Want It Back: Masking, Fingerprinting, and Privacy from Discarded Geometry](https://arxiv.org/abs/2607.13046)

**<font color=#1a73e8>作者：</font>** Zachary P. Bradshaw  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a framework for the information discarded by machine learning models whose inputs carry a Lie group action. Given a representation $\pi$ of a Lie group $G$ on a space $V$ and a learned function $f\colon V \to \mathbb{R}$, we define two objects measuring the symmetry invisible to $f$. The null fiber at a point $x \in V$ is the set $N_G(f,x) = \{g \in G : f(\pi(g^{-1}) \cdot x) = f(x)\}$ of group elements whose inverse action on $x$ is undetectable by $f$. When $N_G(f,x)$ is independent of $x$, it coincides with the stabilizer $\mathrm{Stab}_G(f)$, the largest subgroup of $G$ under which $f$ is invariant. For smooth maps to $\mathbb{R}$, the preimage theorem guarantees that null fibers have dimension at least $\dim G - 1$ at generic inputs, regardless of architecture. For compact groups acting on themselves, the Peter--Weyl theorem yields a spectral characterization of both objects in terms of the Fourier coefficient matrices of $f$. We show that null fiber elements can be computed efficiently via Newton iteration on the orbit map, at a cost comparable to a few gradient evaluations. Applications to data masking, model fingerprinting, and privacy-preserving computation are developed and tested experimentally on molecular property prediction under $\mathrm{SO}(3)$ and spherical image classification under the Möbius group $\mathrm{PSL}(2, \mathbb{C})$. The framework applies uniformly to classical neural networks and variational quantum circuits.

---


### 8. [Targeted Recovery of Weight-Space Mechanisms From Neural Networks](https://arxiv.org/abs/2607.13047)

**<font color=#1a73e8>作者：</font>** Antoine Vigouroux, Lee Sharkey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter decomposition (PD) decomposes neural networks into interpretable computational components that faithfully reflect the original network's operations. However, scaling PD to large models requires vast compute, making it a costly and risky endeavor. Here we propose targeted PD (tPD), which identifies only the components that process specific inputs of interest -- from isolated prompts to large subtasks -- by introducing a high-rank catch-all component that handles all non-target data. We validate tPD on toy models and on transformer language models trained on The Pile, where it recovers reproducible, mechanistically faithful circuits. We extract a CSS-only submodel of a 4-block transformer using 7% of the FLOPs of its published decomposition, and in a 12-block transformer we surgically ablate and rewire memorized sequences, with negligible side effects on other inputs.

---


### 9. [Probabilistic Extension of Neuro-Symbolic AGI Robots based on Belnap's Typed Intensional FOL](https://arxiv.org/abs/2607.13073)

**<font color=#1a73e8>作者：</font>** Zoran Majkic  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neuro-symbolic AI based on $IFOL_B$ is a way to combine neural learning and symbolic reasoning to overcome limitations of purely neural systems (like lack of interpretability and logical structure) with formal logical machinery for self-reference. In this paper we expand the cognitive power of $IFOL_B$ by using the probability computation for the currently unknown sentences, based on Nilsson's probability structure for the $IFOL_B$. We introduce the global symmetry transformation that preserves the current knowledge database and logical deduction, and the local one used for real-time decisions about concrete (sub)problems that involve only a very strict subset of $IFOL_B$ predicates. The computation of probability density function $KI$ in both cases, based on the Shannon's maximum information entropy, is provided by neural networks of this probabilistic neuro-symbolic AGI.

---


### 10. [The Entanglement Wall: Activation-Space Probes as Risk Detectors, Not Context Adjudicators](https://arxiv.org/abs/2607.13075)

**<font color=#1a73e8>作者：</font>** Dominik Schwarz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Context can change whether a request is harmful without changing its topic or surface form. We ask whether residual-stream probes distinguish harmful requests from surface-matched benign controls at a useful operating point. Across three 7-8B model families, an activation sensor blocks 95.5-97.7 percent of judge-classified compliant attacks in a taxonomy-selected set. It also blocks 59.6-68.4 percent of XSTest prompts. A fully disjoint audit reconstructs near-ceiling source-contrast AUROC (0.996-0.999), but fixed transfer to matched pairs is weaker: 0.656-0.819 on the guard-selected Twin-n70 subset and 0.590-0.690 on the full Twin-n163 cohort. We test ten axes on the reference family and seven across all families with leakage, hold-out, and permutation controls. On Twin-n163, no axis evaluated without direct pair-boundary fitting reaches the specified numerical threshold. Requiring persistence on that full cohort was added at analysis time. A separately specified 24B/32B extension gives the same result. Pair-trained classifiers weaken under category and generation-batch hold-out and false-block 79.6-100 percent of XSTest at 95 percent in-corpus TPR. At the tested read points, these activation scores behave as broad-risk detectors rather than standalone context adjudicators.

---


### 11. [Beyond AI-Generated Labels: Watermarking, Co-Creation, and Conflation of AI-Generation with Disinformation](https://arxiv.org/abs/2607.13082)

**<font color=#1a73e8>作者：</font>** Federico Germani, Giovanni Spitale  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking is often presented as a straightforward solution for distinguishing AI-generated from human-generated content, enabling platforms and regulators to trace synthetic content and detect AI-generated outputs at scale. This paper examines whether such mechanisms meaningfully address the epistemic and ethical challenges that arise in domains where the central concern is not the automation of content production, but the accuracy, intent, and deceptive potential of messages. We argue that extending watermark-based approaches to these settings is conceptually and practically misguided. Invisible watermarking encodes only model origin; when operationalized into visible AI-generated labels, it reduces complex creative processes to a misleading binary and provides no information about truthfulness. Such labels may stigmatize legitimate uses of generative tools while encouraging misplaced trust in unmarked content. Here we propose an alternative approach centered on process transparency and information literacy. We argue that these measures address the epistemic and ethical dimensions of AI-generated disinformation more effectively than visible watermark labels, reframing authorship as a transparent human practice rather than a binary indicator of machine involvement.

---


### 12. [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](https://arxiv.org/abs/2607.13083)

**<font color=#1a73e8>作者：</font>** Su Wang, Pin Qian, Yifan Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-improving AI agents are designed to learn from their mistakes. We show they can also hallucinate mistakes that never happened. We study this failure mode in automated harness optimization, where an LLM-based proposer edits an agent's scaffold, including prompts, parsers, filters, validators and guardrails, to eliminate observed failures. But this process rarely asks first: was there a real failure to fix? We introduce the Counterfactual Fabrication Lab, a deterministic micro-lab where the correct action is known: do nothing. The lab plants a candidate guardrail for a failure class that provably never occurs, presents only legal episodes, and uses a byte-exact oracle to check every cited violation. The proposer behaves as expected on real violations and abstains on featureless legal input. Yet when the legal input contains a harmless pattern resembling a familiar game rule, it invents a failure: in 15/60 runs, versus 0/60 on featureless input, it enables the nonexistent-rule guardrail and cites a violation the oracle refutes. The effect is structured, not indiscriminate. In single-shot proposals it appears only when three conditions coincide: a rule-shaped pattern, an open-ended rule set and an instruction that presupposes failures. Removing any of these conditions eliminates the fabrication. Because the invented guardrail changes no true outcome and cannot improve an already-perfect suppression score, the phenomenon is neither reward hacking nor over-refusal. It is a phantom guardrail: a fix for a failure that never happened, invisible to suppression-only acceptance. Inside an add-only accept loop it re-enters even without the failure-presupposing instruction, the loop's keep-adding role supplying the demand the instruction supplied in single shot, and once in it stays. We present the Counterfactual Fabrication Lab for measuring fabricated failures in self-improving agent harnesses.

---


### 13. [Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/abs/2607.13085)

**<font color=#1a73e8>作者：</font>** Ananda Dhakal, Krish Neupane, Aarjan Chaudhary  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent autonomous penetration testing papers report high benchmark scores while adding multi-component security harnesses around frontier LLMs. Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model.
This paper presents a controlled study on the 104-task XBOW benchmark using default coding CLI agents as plain-agent baselines. We first run Codex, OpenCode, and Pi with the same GPT-5 model, budget, target interface, and scoring rule. This phase identifies the strongest same-model baseline and tests whether security-specific prompt variants improve its observed score. We then compare the default Codex scaffold with published MAPTA and PentestGPT V2 results under the closest available model matches. Finally, we repeat the plain-agent experiment with GPT-5.2 and GPT-5.5 to measure model scaling inside the same scaffold.
The results show a mixed but practical picture. Specialised harnesses can add measurable benchmark lift and may improve cost efficiency, but plain coding agents already solve a large share of the benchmark; repeated plain-agent runs can match or exceed some published architecture scores in union coverage, and newer models substantially improve the same scaffold. Future evaluations should report model-matched plain-agent baselines before attributing benchmark gains to architecture design alone.

---


### 14. [GDM AI Control Roadmap](https://arxiv.org/abs/2607.13087)

**<font color=#1a73e8>作者：</font>** Mary Phuong, Erik Jenner, Laurent Simon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are rapidly accelerating work at frontier AI companies, helping with AI R&D, cyber-defence, and advancing scientific discoveries. As these agents become more tightly integrated into our systems, unlocking their full potential requires rethinking how we do security. We should not assume that AI agents are always perfectly aligned, but should instead build in multiple layers of defence. We present the GDM AI Control Roadmap (v0.1) -- a first-of-its-kind blueprint for internal security against potentially misaligned AI. This report provides:
* Threat modelling: We adopt a conservative approach to threat modelling and assume a hypothetical AI adversary pursuing undesirable goals in internal deployment. We introduce TRAIT&R, a taxonomy of tactics and techniques available to such a hypothetical AI adversary, building on the established security framework MITRE ATT&CK.
* Capability-based mitigation: Because controlling more capable models requires more costly interventions, we link specific defensive measures to evolving model capabilities (such as the ability to reason opaquely or execute complex cyberattacks). As models get more powerful, our defences should escalate accordingly. We outline four Detection tiers (D1-D4) and three Prevention and Response tiers (R1-R3).
* A portfolio of practical defences: We suggest 15 concrete, tiered mitigations. These range from low-cost interventions for current models (e.g., chain-of-thought monitoring, asynchronous alerts) to advanced safeguards for future models (e.g., real-time access control, system-level anomaly detection, internal activations monitoring, and shutdown infrastructure).
AI control is a nascent field, and implementing these mitigations requires navigating difficult trade-offs between security and developer velocity. We expect the roadmap to evolve as we gain more experience and as the field in turn evolves.

---


### 15. [TSSM: Triaxial State Space Model for Global Station Weather Forecasting with Temporal-Variable-Historical Modeling](https://arxiv.org/abs/2607.13101)

**<font color=#1a73e8>作者：</font>** Songru Yang, Zili Liu, Tao Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global Station Weather Forecasting (GSWF) is pivotal for localized and extreme weather prediction over key regions. Despite efforts to exploit look-back windows, existing methods show limited accuracy gains and struggle with extreme events and error accumulation. These limitations stem from overreliance on short-term patterns, which are insufficient to capture chaotic weather dynamics, especially under partial observations. To address this problem, we propose a novel Triaxial State Space Model (TSSM) with a history-enhanced Temporal-VariableHistorical paradigm, which incorporates period-aligned historical weather data to compensate for long-term, large-scale periodic, and full-window weather patterns beyond the temporal lookback window. Specifically, TSSM stacks historical samples into period-aligned batches, where forecasting is causally supported by historical and current observations. Temporal, variable, and historical scanning are designed to capture axial temporal dependencies, variable correlations, and historical evolution. This structure is hierarchically shared to model seasonal to extreme events while alleviating misalignment across historical patterns. TSSM achieves SOTA performance on Weather-5K, the largest station weather dataset to date, with 10% and 61% gains in accuracy and extreme event metrics, and obtains 95% best or second-best results on human-involved datasets. Its advantages are more pronounced in long-horizon and iterative forecasting, reaching a 37.5% gain at 240h and up to 103.5% under a 48h times 5 iterative setting. Moreover, TSSM retains > 90% performance under up to 80% missing observations, compared with < 43% for baselines, demonstrating robustness and practical potential for reliable GSWF in global in-situ observation networks.

---


### 16. [Disentangling Knowledge States with Ability and Proficiency Modeling for Knowledge Tracing](https://arxiv.org/abs/2607.13103)

**<font color=#1a73e8>作者：</font>** Duantengchuan Li, Yingqian Bi, Jinsong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) aims to predict students' future performance by modeling their evolving knowledge states from historical interactions. Existing KT methods usually treat the raw interaction sequence as a unified behavioral process, overlooking the phase-specific nature of learning behaviors. Our preliminary observations show that students are more likely to correctly answer previously failed knowledge concepts after sufficient practice, suggesting a transition from ability-building to proficiency-oriented learning. Motivated by this, we propose Phase-Aware Knowledge Tracing (PAKT), a KT framework that decomposes student interactions into ability and proficiency phases based on the tailored decomposition mechanism. To effectively exploit the decomposed sequences, we design a multi-branch Transformer with a type-aware readout module to jointly capture phase-specific and holistic knowledge states. We further provide a causal analysis to reveal the confounding bias caused by entangling complex learning behaviors in phase-agnostic KT models. Extensive experiments on six public benchmarks demonstrate that our method consistently outperforms representative baselines, with a maximum AUC gain of 1.33% and an average gain of 0.82%.

---


### 17. [STKAN: Kolmogorov-Arnold Networks for Spatio-Temporal Forecasting](https://arxiv.org/abs/2607.13108)

**<font color=#1a73e8>作者：</font>** Sicong Lai, Yuehong Hu, Siru Zhong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world traffic data exhibit heterogeneous spatial correlations and nonlinear temporal dynamics, posing substantial challenges for accurate spatio-temporal forecasting. Existing approaches have developed increasingly sophisticated graph, attention, and decomposition architectures, while the influence of the underlying nonlinear function approximator has received comparatively less attention. In this work, we propose STKAN, a spatio-temporal forecasting architecture that introduces Taylor-polynomial Kolmogorov--Arnold Network modules into spatial and temporal token mixing. STKAN first constructs high-level spatial representations through a learnable soft node-group assignment mechanism, applies group-wise spatial mixing, and subsequently models temporal dependencies over the compressed sequence. Spatial and temporal self-attention layers are further employed to capture long-range interactions. Experiments on five traffic forecasting benchmarks show that STKAN achieves competitive performance and performs better than the evaluated MLP-based variant in the tested settings. These results suggest that the design of nonlinear function approximators can serve as a useful complement to architectural design in spatio-temporal forecasting.

---


### 18. [A Hybrid Mamba for Audio-Visual Navigation](https://arxiv.org/abs/2607.13110)

**<font color=#1a73e8>作者：</font>** Yi Wang, Yinfeng Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since the paradigm centered on convolutional neural networks and recurrent architectures was established in 2020, the fundamental backbone networks for audio-visual navigation have undergone no essential changes for more than five years, making them inadequate to support efficient representation of dynamic multimodal sequences. This paper proposes Samba(A Hybrid Mamba for Audio-Visual Navigation). It uses the adaptive selection-enabled Mamba State Encoder (M-SE) to replace conventional GRUs for temporal aggregation, and constructs an Audio Mamba Encoder (AME) to remedy the limitations of convolutional operators in capturing global time-frequency dependencies in spectrograms. Experiments demonstrate that Samba exhibits exceptional generalization performance when facing unheard sound sources and unseen scenes. On the Matterport3D dataset, it improves the navigation success rate (SR) by 11.3\% compared with existing state-of-the-art models, and the performance gain is even more pronounced on the Replica dataset, which features finer scene structures. Such modernized architectural reconstruction unlocks stronger embodied representation capabilities at a lower computational cost, thereby providing a highly robust technical pathway for paradigm evolution in the field of audio-visual navigation.

---


### 19. [C-Norm: Cell-Distribution Normalization Enables Precision Recognition of Medical-Cell Image](https://arxiv.org/abs/2607.13116)

**<font color=#1a73e8>作者：</font>** Yang Qianl, Liu Xiany, Dai Daw 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ThinPrep Cytologic Test (TCT) enables early cervical cancer screening, but manual reading is time-consuming and yields inconsistent diagnostic results among cytopathologists. Existing AI detection models perform poorly under real clinical conditions, primarily restricted by two key constraints: unbalanced spatial distribution of cell populations in TCT slides, and limited high-quality annotated cytology data relying on professional pathologist labeling. To address these limitations, we propose a Cell-Distribution Normalization (C-Norm) method. By decoupling abnormal and normal cells from the original TCT images and re-synthesizing them, this method ensures a uniform distribution of cell populations, thereby mitigating generalization degradation caused by distribution bias. Building upon this, we integrate the YOLOv12 framework with a DINOv3 module. This hybrid architecture leverages the advanced detection capability of YOLO models and the superior feature representations of DINOv3 to capture subtle morphological nuances essential for precise recognition of TCT images. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance, significantly outperforming mainstream detection algorithms. The complete implementation is available at: this https URL

---


### 20. [CoDiffGRN: Rethinking Gene Regulatory Network Inference via the BEELINE-KGC Benchmark and Co-evolutionary Discrete Diffusion](https://arxiv.org/abs/2607.13120)

**<font color=#1a73e8>作者：</font>** Jiaze Song, Runhao Zhao, Minghao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring gene regulatory networks (GRNs) from single-cell transcriptomic data is crucial for biological discovery, yet existing approaches suffer from a fundamental misalignment with real-world needs. Researchers typically seek a small set of high-confidence regulatory interactions for experimental validation, often involving previously unseen genes. However, current benchmarks rely on transductive splits with global classification metrics, while prevailing models struggle to generalize under inductive settings. To bridge this gap, we reformulate GRN inference as an inductive, ranking-centric graph completion problem and introduce \textbf{\benchmark}, a new benchmark that incorporates an inductive gene-holdout split together with knowledge graph completion metrics to better evaluate top-ranked predictions. Building on this, we propose \textbf{\method}, the first co-evolutionary discrete diffusion framework that jointly models biologically coherent discretized gene expression states and regulatory interactions for robust inductive generalization and improved top-ranked regulatory discovery. We further introduce TF-ALL Subgraph Sampling (TASS) for scalable training. Extensive experiments on {\benchmark} show that {\method} establishes new state-of-the-art performance, significantly outperforming existing methods in novel regulatory discovery, and ablation studies further verify the effectiveness of our design.

---


### 21. [Designing a GDPR-Compliant Security Architecture for Remote Elderly Care Systems: A Privacy-by-Design Approach](https://arxiv.org/abs/2607.13122)

**<font color=#1a73e8>作者：</font>** Md. Rahid Parvez, Mikael Soini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IoMT-based remote elderly care systems generate continuous streams of sensitive health data, yet existing security architectures have not simultaneously addressed three interdependent challenges: GDPR-compliant edge-layer pseudonymisation, elderly-specific zero-interaction usability as a binding architectural constraint, and integrated STRIDE-based threat validation within a single unified design. This paper presents the Secure Edge Gateway (SEG) framework - a software-simulation-validated integrated IoMT security architecture for elderly care designed to resolve all three dimensions of this tripartite gap simultaneously. An ESP32-WROOM-32 residential gateway enforces MAC address whitelisting, HMAC-SHA256 cryptographic pseudonymisation before any network transmission, AES-128-CBC payload encryption, and TLS 1.3 transport security, in compliance with GDPR Articles 25 and 32. The framework is validated through software-based simulation, full STRIDE threat modelling across all six categories, attack tree analysis, GDPR compliance mapping across nine regulatory obligations, and a Data Protection Impact Assessment (DPIA) under Article 35. Published benchmarks confirm MQTT consumes 6-8% less energy than HTTP in comparable IoT deployments, and edge processing achieves sub-50 ms response latency versus 200-700 ms for cloud-only systems. The results demonstrate that GDPR compliance and operational efficiency are complementary - not competing - objectives in resource-constrained IoMT deployments for elderly care.

---


### 22. [AI in Cyberpsychology: A systematic literature review of Cybersecurity enhancement by using AI for analyzing psychology of Victims, Attackers, and Defenders](https://arxiv.org/abs/2607.13123)

**<font color=#1a73e8>作者：</font>** Georg Thamer Francis, Malek Malkawi, Sevim Eyüpoğlu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybersecurity is the practice of protecting systems, networks, and data from digital attacks. Cyberpsychology (CPSY) is defined as the use of psychology to enhance cybersecurity applications. Since the early 2010s, the evolution of Artificial Intelligence (AI) has increasingly integrated with CPSY, leveraging advanced data analysis to decode the distinct personality traits and behavioral patterns of victims, attackers, and defenders. In this systematic literature review (SLR), we carefully analyze 34 collected research studies of AI usage in cyberpsychology (AI-CPSY) using the preferred reporting items for systematic reviews and meta-analyses (PRISMA) methodology. The review presents a comprehensive taxonomy of the cyber-security applications, the AI methodologies used, and the psychological concepts employed across the studies . We sort the research studies into four cybersecurity applications: Anomaly Detection (AD), Vulnerability Risk Prediction (VRP), Security Awareness Training (SAT), and Authentication/Identity Verification (AIV). Within each application area, studies are further sorted according to the AI method used including machine learning (ML), deep learning (DL), natural language processing (NLP), and reinforcement learning (RL). Furthermore, the review identifies the most commonly utilized psychological concepts, quantify the datasets used in the field, and present their current implementation and deployment status. At last, it detect research gaps, present open challenges, and deduce the trending and most effective and emerging methodologies used across the AI-CPSY landscape.

---


### 23. [HEDGEHOG: Hierarchical Evaluation of Drug Generators Through Rigorous Filtration](https://arxiv.org/abs/2607.13155)

**<font color=#1a73e8>作者：</font>** Daria A. Ryabchenko, Pavel Gurevich, Shamil Kadyrov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative molecular models can support early drug discovery by proposing new candidate compounds de novo. In practice, useful candidates must balance target-relevant activity, synthetic accessibility, physicochemical properties, and other multiparameter design constraints. However, metrics commonly used to evaluate molecular generators only weakly reflect whether the generated compounds are medicinally plausible and suitable for downstream computation. This can produce false positives in model evaluation, incorrect assumptions, and inefficient use of computational resources. We introduce HEDGEHOG, a unified six-stage filtration benchmark that is inspired by industrial hit identification workflows: (i) preprocessing; (ii) physicochemical descriptor screening; (iii) structural alerts and graph-sanity checks; (iv) synthesis feasibility; (v) docking and binding affinity estimation; and (vi) three-dimensional pose and interaction checks. We evaluate 23 molecular generators across three model classes under a standardized protocol. Across 230,000 generated molecules, only 0.65% of initial molecules survive all stages. Our results expose a central limitation of current molecular generators: molecules that appear acceptable under isolated criteria rarely satisfy medicinal chemistry, synthesis, docking, and 3D pose filters simultaneously.

---


### 24. [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](https://arxiv.org/abs/2607.13157)

**<font color=#1a73e8>作者：</font>** Richmond Alake, Cesare Bernardis, Paul Cayet 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. These requirements extend beyond document retrieval: a memory layer must determine which interactions become durable state, how that state is scoped, how it is retrieved under latency constraints, and how it is revised or removed over time. This report studies Oracle Agent Memory as a database-native memory substrate built on Oracle Database. Three themes organize the discussion: memory as a lifecycle spanning ingestion, extraction, consolidation, retrieval, summarization, and revision or removal; a layered architecture that separates an active memory core from a passive memory-store interface with explicit scope control across users, agents, and threads; and evaluation methodology in which downstream task accuracy is complemented by memory-centric measures such as evidence retrieval, recall, latency, and estimated token use. The report summarizes LongMemEval results, reaching 93.8% accuracy, compares Oracle Agent Memory against flat-history baselines, using about 10.7x fewer tokens, and published or reported external baselines where available, and closes with implementation-oriented appendix material covering setup, thread lifecycle, and search semantics.

---


### 25. [Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164)

**<font color=#1a73e8>作者：</font>** Ruize Xia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign language is a primary communication channel for millions of Deaf and hard-of-hearing people, yet text-to-signer video generation remains costly because video diffusion models are expensive to train and evaluate. This paper presents Text2Sign, a text-conditioned diffusion model for short sign-language clips that runs on a single NVIDIA L4 GPU. It combines a frozen vision-language text encoder with a 3D encoder-decoder and factorized spatiotemporal attention to reduce the cost of full-video attention while preserving motion coherence.
We compare convolution-only and transformer-style backbones, frozen pretrained and task-specific text encoders, and factorized versus full attention. On a signer-disjoint How2Sign split, the best short-run ablation reaches a validation loss of 0.0648, while a longer-run checkpoint reaches 0.00999. On a compact evaluation slice, the latter achieves an SSIM of $0.2403 \pm 0.0238$, a PSNR of $15.11 \pm 0.42$ dB, and temporal consistency of $1.0000 \pm 0.0000$ using 8-step DDIM sampling with a guidance scale of 5.0. It generates a 32-frame, $64 \times 64$ clip in 12.60 seconds, or 2.54 frames per second, with peak inference memory of 3.12 GB.
A held-out denoising audit shows only weak prompt sensitivity: removing text increases late-timestep loss from 0.9875 to 0.9891, while shuffled prompts perform similarly to correct prompts. Frozen text conditioning therefore improves short-budget validation loss, but prompt-specific separation remains limited. The system is restricted to low-resolution, short clips and lacks expert linguistic evaluation, so it should be viewed as a single-GPU research baseline rather than a complete sign-language production system. Code is available at this https URL.

---


### 26. [SteinGate: Tail-Sensitive Safe Reinforcement Learning via Stein Discrepancy](https://arxiv.org/abs/2607.13175)

**<font color=#1a73e8>作者：</font>** Yassine Chemingui, Chenhua Fan, Honghao Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning typically enforces safety by bounding expected cumulative costs, a criterion that often fails to detect rare but catastrophic tail events. To overcome these limitations, this paper introduces SteinGate, a boundary-aware distributional safety certificate that replaces fragile tail fitting with a robust consistency check using Kernelized Stein Discrepancy while accounting for boundary atoms induced by clipped costs. SteinGate evaluates whether observed policy rollout costs remain consistent with a safe reference distribution, providing a non-parametric safety certificate. This certificate is used to dynamically adapt the learning regime: favoring reward-improving policy updates when rollouts remain consistent with the safe reference and switching to recovery behavior when the cost tail deviates. Experiments on continuous-control benchmarks demonstrate that SteinGate significantly reduces both the frequency and severity of constraint violations during training while maintaining competitive returns relative to state-of-the-art baselines.

---


### 27. [A Masked Autoencoder Approach to Unsupervised Steel Surface Defect Recognition](https://arxiv.org/abs/2607.13178)

**<font color=#1a73e8>作者：</font>** Shrey Patel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated visual inspection of steel surface defects is a recurring quality control task in which labeled defect data is scarce and costly to obtain, while unlabeled surface images are abundant, which motivates self supervised methods that learn useful representations without class labels. A Transformer based Masked Autoencoder is used here to learn representations of steel surface defects for unsupervised grouping. During pretraining, 75% of the input image patches are randomly masked, and a lightweight decoder reconstructs the masked regions from the visible 25%. The encoder is trained jointly with an auxiliary defect localization objective, used only as a training signal and not evaluated as a detector. The decoder reaches a structural similarity score of 0.92 and a mean squared error of 0.47. Features from the pretrained encoder are then clustered using UMAP for dimensionality reduction and Agglomerative clustering, reaching a Hungarian matched accuracy of 91.3% against the six known defect categories.

---


### 28. [SoftBoard: A Multi-Agent Tool for the Creation and Evaluation of Low-Fidelity Prototypes](https://arxiv.org/abs/2607.13179)

**<font color=#1a73e8>作者：</font>** Gabriel R. S. Scapim, Gislaine C. L. Leal, Guilherme C. Guerino  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User Experience (UX) is recognized as a critical factor for the success of digital products, particularly in software startups, environments marked by time constraints, limited resources, and low maturity in design practices. Building Minimum Viable Products (MVPs) through low-fidelity prototyping represents a well-established strategy for rapid validation cycles at reduced cost. A systematic literature mapping, however, revealed gaps in the ecosystem of available tools: a predominance of general-purpose solutions adapted for prototyping, the absence of integrated methodological guidance, and the incipient use of Artificial Intelligence in the design process. This paper presents SoftBoard, a web-based tool for the creation and evaluation of low-fidelity prototypes in the context of MVP development. The tool integrates a prototype editor, team-based project organization, and a multi-agent system based on large language models that supports requirements elicitation and refinement, automates prototype generation, and evaluates interface quality based on usability heuristics. This integration aims to reduce reliance on prior UX expertise, standardize the prototyping process, and support teams in building MVPs aligned with user needs. As future work, a feasibility study with software professionals is currently underway.

---


### 29. [MGFace: Mask-Gated Face Matching via Conditional Similarity Routing](https://arxiv.org/abs/2607.13187)

**<font color=#1a73e8>作者：</font>** Huy Che, Hoang-Minh Trinh, Dinh-Duy Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face identification has achieved remarkable performance under normal conditions. Yet, its accuracy often degrades significantly when query faces are partially occluded, especially by facial masks. Existing re-ranking approaches improve robustness by exploiting patch-level similarities. Still, they often rely on costly, fine-grained matching mechanisms, which limit their efficiency in large-scale retrieval scenarios. In this paper, we propose MGFace, a mask-gated face identification pipeline that predicts the mask status of a query face and conditionally routes the similarity computation accordingly. Specifically, MGFace distinguishes between masked and unmasked queries, applies global embedding matching to unmasked queries, and activates mask-aware patch-level re-ranking only for masked queries. This design focuses on reliable upper-face regions while avoiding unnecessary fine-grained computation. Experiments on the extended LFW-Mask dataset show that MGFace achieves over 80% identification accuracy with the FaceNet backbone and over 90% with the ArcFace backbone. Compared with a previous EMD-based re-ranking method, MGFace achieves better identification performance while reducing query time by approximately 20x. These results demonstrate the effectiveness of MGFace in improving masked-face identification accuracy with low computational overhead. The source code is available at this https URL.

---


### 30. [Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes](https://arxiv.org/abs/2607.13188)

**<font color=#1a73e8>作者：</font>** Minh-Quan Le, Armand Comas, Alexandros Lattas 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human cognition does not separate understanding and generation. A teacher at a whiteboard speaks and draws $\textit{together}$, each modality reshapes the other. In this paper, we bring this coupled loop to artificial systems. Masked Diffusion Models (MDMs) are ideally suited to this task, yet existing samplers either decode text and image interleavedly or independently update them in parallel branches that share only previous-step history, but not the other modality's latest decisions $\textit{within}$ the same step; combined with MDMs' inability to remask, cross-modal contradictions are neither detected nor repaired. We introduce $\textbf{Self-Correcting Coupled Markov Jump Processes (SC-CMJP)}$, a framework in which one modality's transition rates are functionals of the other modality's confidence score, as weighted by cross-modal attention. Furthermore, a remasking jump retracts commitments the moment cross-modal evidence turns against them. In conjunction with SC-CMJP, we introduce $\texttt{CO}_\texttt{2}\texttt{Jump}$ (Self-$\underline{\text{CO}}$rrecting $\underline{\text{CO}}$upled $\underline{\text{Jump}}$), a novel training-free single-pass sampler for joint multimodal geneneration. For training and evaluation purposes, we have created and will release three large-scale joint multimodal generation corpora: $\text{JEdit-1M}$, $\text{JMaze-200K}$, $\text{JNono-200K}$, with matching in- and out-of-distribution benchmarks. $\texttt{CO}_\texttt{2}\texttt{Jump}$ achieves best joint performance for image understanding and editing as well as visual reasoning (maze and nonogram solving). The performance of the sampler scales monotonically with the number of denoising steps, evidence that the benefits of cross-modal coupling $\textit{compound}$ across the trajectory. Project page: this https URL

---


### 31. [Self-Supervised Visual Representation Learning: Pretrain-Finetuning or Joint Training?](https://arxiv.org/abs/2607.13192)

**<font color=#1a73e8>作者：</font>** Nusrat Munia, Tyler Ward, Nishat Nayla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervision is a powerful technique for learning visual representations from unlabeled data. Existing techniques primarily adopt a two-stage approach for self-supervised learning (SSL): a pretraining stage on unlabeled data followed by a finetuning stage on labeled data. While this pipeline has demonstrated extreme effectiveness, the interaction between self-supervised and supervised learning objectives remains insufficiently understood. In this work, we systematically investigate whether jointly optimizing the self-supervised and supervised objectives during training provides a better alternative. We compare two training paradigms: (1) the aforementioned pretraining followed by finetuning (PFT) and (2) joint training (JT), where self-supervised and supervised losses are optimized simultaneously in the same network. Across eight representative SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data, we evaluate performance under varying percentages of labeled data. Our results reveal that the relative effectiveness of PFT and JT depends strongly on the task at hand, the availability of labeled data, and the complexity of the domain. We find that JT consistently improves data and training efficiency while being robust in low-label settings, while PFT is more reliable in more specialized domains. We further analyze representation quality, robustness, and cross-domain generalization, providing new insights into how self-supervised and supervised objectives interact during optimization. We establish a comprehensive empirical benchmark for hybrid SSL-based semi-supervised learning and offer practical guidance for selecting appropriate training strategies across diverse vision applications.

---


### 32. [BARS: Benign-Anchored Ranking and Selection for False Alarm Reduction in Network Intrusion Detection](https://arxiv.org/abs/2607.13203)

**<font color=#1a73e8>作者：</font>** Abu Fuad Ahmad, Istiaque Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> False alarms remain a major barrier to deploying network intrusion detection systems (NIDS). In high-volume environments, even a sub-1% false positive rate can generate tens of thousands of daily alerts. Filter-based feature selection is attractive because it operates upstream of the classifier and adds no inference-time cost. However, classical filters use class-symmetric criteria that ignore the asymmetry of intrusion detection, where benign traffic defines the baseline and attacks are deviations from it. A recent class-asymmetric filter, Classwise Mean Deviation (CMD), addresses this issue but anchors its score to a global mean that shifts toward attack distributions under class imbalance, weakening the deviations it aims to capture.
We propose Benign-Anchored Ranking and Selection (BARS), a two-stage filter that replaces CMD's global anchor with the benign-class mean and applies an order-preserving decorrelation step. We evaluate BARS on CICIDS2017, CICDDoS2019, and UNSW-NB15 using feature budgets k = {5, 10, 20, 30, 40}. On attack-majority datasets, where global-anchor bias is strongest, BARS reduces false positive rate relative to CMD by 15.4% on UNSW-NB15 at k = 20 and by 21% to 23% on CICDDoS2019 at small feature budgets while preserving true positive rate and macro-F1. On benign-majority data, BARS and CMD converge, consistent with the theoretical limit where global- and benign-anchored scores coincide. BARS is a principled refinement of CMD rather than a universally dominant filter. Although Pearson Correlation and Mutual Information often achieve lower false positive rates, they exceeded 1 TB of memory on the largest benchmarks in our evaluation. BARS retains linear-time scoring and a low memory footprint, making it suitable for resource-constrained deployments.

---


### 33. [Why Not Fix It Once and for All? An Empirical Study of Multiple Patches for Vulnerability Fixes in Open-Source Software](https://arxiv.org/abs/2607.13206)

**<font color=#1a73e8>作者：</font>** Weiliang Qi, Youpeng Li, Xinda Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security patches for open-source software constitute a foundational resource for vulnerability remediation research and practice. However, analyzing and applying multiple patches remains challenging, especially when trying to determine at what point in a patch sequence a vulnerability is fully remediated. This paper presents a systematic analysis of multi-patch vulnerability fixes, focusing on their root causes, characteristics, and methods for verifying remediation status throughout the fixing process. Through a manual examination of 1,646 multi-patch fix records, we develop a taxonomy with three primary categories and six subcategories based on their causes. We then compare the distinctive characteristics of multi-patch fixes with those of single-patch fixes and analyze feature variations across categories. In addition, we assess representative vulnerability detection methods for validating complete remediation during multi-patch fixing. Our findings provide new insights into multi-patch fixes and lay a foundation for future research in this field.

---


### 34. [CayleyR: Solving the TopSpin puzzle via cycle intersection](https://arxiv.org/abs/2607.13219)

**<font color=#1a73e8>作者：</font>** Yuri Baramykov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present cayleyR, an R package for solving permutation puzzles by detecting cycle intersections in Cayley graphs. The core algorithm performs an iterative bidirectional search: from both the initial and target permutation states, random operation sequences generate cycles in the Cayley graph of the symmetric group Sn; their intersection yields a connecting path. When no direct intersection is found, a distance-guided bridge selection narrows the gap, and the process repeats. The package targets the TopSpin(n,k) puzzle, whose state space is a Cayley graph of Sn generated by a cyclic shift and a prefix reversal. We describe the mathematical framework, the algorithm, and its implementation, which combines a C++ hash-indexed state store with optional Vulkan GPU acceleration. The software is publicly available on CRAN.

---


### 35. [Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science](https://arxiv.org/abs/2607.13220)

**<font color=#1a73e8>作者：</font>** Sutanay Choudhury, Jeffrey J. Czajka, Lummy M. O. Monteiro 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most AI-for-science systems focus on scaling a single reasoning process through better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, challenging scientific problems are rarely solved by one reasoner alone. They are solved by teams whose members bring different priors, experimental backgrounds, tacit knowledge, and domain-trained intuitions. The open problem is therefore not only how to scale models, but how to cultivate networked intelligence: scaling the connections between humans and AI systems so that a result or hypothesis produced in one context reaches another person, agent, instrument, or robot that can act on it. We introduce Mycelium, an active shared workspace that automatically connects researchers and AI agents as a multi-user co-scientist. As human users and agents work, the system captures important observations and hypotheses, tracks how they relate to the team's evolving model, and routes them to the person or agent whose next decision they can inform. We evaluate Mycelium in its first empirical test, a biological multi-omics campaign in which routed shared context turned a local analytical finding into a cross-expert mechanistic constraint and ultimately into an experimental design. We also give networked intelligence a computational account as sparse conditional computation over distributed scientific contexts. This account distinguishes when a scaled standalone agent can match the network from when independent expertise and non-mergeable contexts make the network irreducible.

---


### 36. [Continuously Evolving Deepfake Detection: An Architecture and Public-Benchmark Evaluation of a Dynamic Detection System](https://arxiv.org/abs/2607.13234)

**<font color=#1a73e8>作者：</font>** Ken Jon Miyachi, Dylan Uys  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detectors that achieve near-perfect scores on academic benchmarks collapse on real-world content: recent in-the-wild evaluations report AUC drops of 45-50% for state-of-the-art open-source models. We argue this gap is structural: static detectors are trained once against a moving generative frontier. We present BitMind Forensics (BMF), trained through Bittensor SN34, an open adversarial competition that continually refreshes the training distribution. We evaluate one dated export comprising image, general-video, and human-video checkpoints across nineteen public datasets: the canonical face-swap suites (FaceForensics++, Celeb-DF v1/v2/++, DFDC, DFD, UADFV, DF40) and recent in-the-wild and AI-generated-media benchmarks (Sumsub, Deepfake-Eval-2024, WildRF, Community Forensics, AIGCDetectBench, GenImage, AI-GenBench, AIGIBench, RAID, GenVidBench, GenVideo-100K). BMF reaches 0.936 AUC on Sumsub's original images and 0.872 pooled AUC over its full four-condition manipulation battery (1.4M images), staying robust under perturbation (0.855 JPEG, 0.799 downscaled), while GPEN enhancement improves detection (0.996). On Deepfake-Eval-2024, it matches the best commercial detector on images (0.915 vs 0.90) and exceeds it on video (0.822 vs 0.79), far above the best open-source detectors (0.56 and 0.63). It reaches 0.991 AUC on a 21-generator AI-image panel and 0.918 on GenVidBench, and exceeds the FF++-trained frontier on DFDC (0.947 vs 0.843) and Celeb-DF v2 (0.9985 vs 0.956), both contamination-audited, with statistical parity on Celeb-DF++. In a temporal study, successive dated exports improve on held-out media from generators absent from the static baseline's training (image 0.842 to 0.902; video 0.864 to 0.936). Our evaluation harness is public, and at publication the production API serves the exact evaluated snapshot for independent verification.

---


### 37. [Proof in a Bottle: Long-Lived Verifiable Secret Sharing via Pre-Quantum Commitment and Immutable Ledger Binding](https://arxiv.org/abs/2607.13235)

**<font color=#1a73e8>作者：</font>** Markus Jakobsson, Keir Finlow-Bates  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional secret sharing techniques such as Verifiable Secret sharing (VSS) are vulnerable to quantum attacks by a Cryptographically Relevant Quantum Computer (CRQC) running Shor's algorithm. We observe that the binding a VSS needs is required only at the moment of dealing, and this binding can be made before any CRQC exists. We propose Proof in a Bottle (PiB), which decouples verifiability from long-term binding: standard Pedersen commitments provide zero-knowledge, publicly checkable consistency during a pre-quantum window, while a salted, index-bound hash of the share set, anchored to an immutable public ledger, preserves the binding established in that window into the post-quantum era. The guarantee is explicitly a commit-now, reveal-later one: it protects today's honest dealings against tomorrow's quantum adversary.

---


### 38. [Active Learning for Efficient Annotation of Surgical Videos with Weak Supervision](https://arxiv.org/abs/2607.13237)

**<font color=#1a73e8>作者：</font>** Manasa Dendukuri, Matjaz Jogan, Daniel A. Hashimoto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise spatial-temporal annotation of laparoscopic videos is time-consuming and requires expert knowledge. We propose a human-in-the-loop knowledge acquisition framework that combines active learning with dual-loss optimization to significantly reduce the annotation effort needed for automatic localization and segmentation of objects in the surgical field. Our method employs a foundation model to generate temporally consistent class activation maps (CAMs) from video using two complementary training objectives: a weak supervision loss on video-level tool presence labels for weakly annotated data, and an image-level mask loss on human-corrected annotations obtained through active learning. Rather than requiring dense pixel-level annotation upfront, our pipeline iteratively proposes pseudo-masks that guide the expert annotator to refine the knowledge previously captured by the model. We demonstrate that our framework reduces the effort of surgical video annotation by 50% by the end of training in comparison to fully manual annotation. Through eliminating the need for large, fully annotated datasets from the start, this framework enables scalability to the development of surgical tool segmentation models. This iterative human-in-the-loop refinement supports efficient knowledge acquisition with minimal expert input, providing a practical and deployable strategy for expanding tool segmentation to larger, more diverse datasets and real-world clinical settings.

---


### 39. [EMAGN: Efficient Multi-Attention Graph Network via Learned Clustering for Scalable Traffic Forecasting](https://arxiv.org/abs/2607.13241)

**<font color=#1a73e8>作者：</font>** Mingxing Xu, Rakesh Chowdary Machineni, Ke Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic forecasting is highly challenging due to complex and nonlinear spatial and temporal dependencies. Self-attention mechanisms have been widely adopted to model dynamic and long-range dependencies, achieving state-of-the-art performance, but suffer from limited scalability due to quadratic computational and memory complexity. To address this, we propose an Efficient Multi-Attention Graph Network (EMAGN) that linearises the spatial attention mechanism itself, inspired by the theory of fast high-dimensional Gaussian filtering. Two learned clustering matrices C_k and C_v adaptively group key and value vectors into M super-clusters, reducing complexity from O(N^2 d) to O(NMd) without sacrificing the flexibility of attention for dynamic dependency modelling. Experimental results on PEMS-BAY and METR-LA show that EMAGN achieves accuracy within 2.7-3.2% MAE of full-attention GMAN while reducing training time by 32%, inference time by 38%, and GPU memory by 58%. Critically, at K=16 attention heads, full-attention GMAN runs out of memory on a standard 11 GB GPU entirely while EMAGN continues to operate, demonstrating a categorical expansion of feasible model configurations. EMAGN also surpasses Linformer and Performer in both accuracy and efficiency within the same backbone, owing to its traffic-network-aware adaptive clustering.

---


### 40. [Reassessing Muon for Matrix Factorization](https://arxiv.org/abs/2607.13246)

**<font color=#1a73e8>作者：</font>** Ali Parviz, Gal Mishne, Alex Cloninger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a strong optimizer for large-scale deep learning, where it reshapes gradient updates through approximate orthogonalization and has been reported to outperform Adam and AdamW in large language model training. Its empirical success has motivated a growing body of theoretical work that interprets Muon as steepest descent under the spectral norm. Yet it remains unclear which of Muon's advantages stem from its update rule itself and which are artifacts of the scale, architecture, and data of modern deep networks. In this work, we isolate the optimizer from these confounding factors by studying Muon on a simple, well-understood, and spectrally structured problem: low-rank matrix factorization. Through a controlled comparison against carefully tuned adaptive baselines, we find that Muon does not consistently outperform AdamW in this setting and that several previously reported advantages are sensitive to hyperparameter choices. Our results provide a more nuanced picture of when spectrum-aware orthogonalization is beneficial and argue for evaluating modern optimizers on controlled problems in addition to end-to-end benchmarks.

---


### 41. [AffectFlow-DINO: Uncertainty-Aware Multi-Task Affect Estimation via Conditional Rectified Flow](https://arxiv.org/abs/2607.13250)

**<font color=#1a73e8>作者：</font>** Salah Eddine Bekhouche, Abdellah Zakaria Sellam, Fadi Dornaika 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present \textbf{AffectFlow-DINO}, a multi-task learning system for the 11th ABAW challenge that extends a standard deterministic architecture with a conditional rectified-flow head to model the inherent ambiguity of in-the-wild facial behavior. Instead of predicting a single affect estimate, the model learns a conditional generative distribution, enabling uncertainty-aware one-to-many predictions through Monte Carlo sampling. The system jointly estimates continuous valence-arousal, classifies eight facial expressions, and detects twelve Action Units from static face images. Built on a frozen DINOv3 ViT-S/16 backbone, extensive ablation studies show that rectified-flow decoding consistently improves deterministic prediction, particularly for valence-arousal estimation (CCC-V $+0.058$). We further show that post-hoc threshold calibration effectively recovers performance on severely imbalanced rare classes (e.g., Fear: $3.8\% \rightarrow 33.1\%$) without retraining. Combined with backbone fine-tuning and flow retuning, the final model achieves $\mathbf{P_{MTL}=1.177}$, substantially outperforming the official challenge baseline of $P_{MTL}=0.45$.

---


### 42. [Differentiable Polarized Path Tracing](https://arxiv.org/abs/2607.13265)

**<font color=#1a73e8>作者：</font>** Pramod Rao, Jérémy Riviere, Xilong Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically based differentiable rendering has proven to be a powerful tool for inverse rendering problems (e.g., 3D reconstruction, reflectance estimation, lighting estimation). However, most existing methods operate solely on radiometric intensity, discarding valuable polarization cues that constrain scene geometry and material properties. While forward simulation of polarized light is well-defined via Mueller-Stokes calculus, extending reverse-mode differentiation to this domain presents significant challenges. The rank-deficient nature of common polarimetric operators, such as linear polarizers and diffuse reflections, violates the invertibility assumptions of standard gradient estimators like path replay backpropagation and results in numerical instability. We address this by proposing a robust, polarization-aware differentiable path tracing method. Our approach estimates unbiased gradients through a combination of path replay and local caching. This formulation enables efficient and stable optimization of material and lighting parameters in complex scenes, broadening the applicability of physically based inverse rendering. Project page: this https URL

---


### 43. [Deconstructing Actor-Critic: A Large-scale Empirical Study of Design Components for Practitioners](https://arxiv.org/abs/2607.13274)

**<font color=#1a73e8>作者：</font>** Haseeb Shah, Lingwei Zhu, Adam White 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is increasingly being considered for controlling real-world systems, from fusion plasma and autonomous vehicles to drug discovery and drinking water treatment, where reliability is essential and tuning budgets are limited. Actor-critic algorithms share a set of design decisions, such as how the policy is updated, how it represents the distribution over actions, how its gradient is estimated, and how often it is updated relative to the value estimator. Using a control task derived from a real water treatment plant, we analyze over 33,000 experiments to determine how these components affect variability across runs and sensitivity to hyperparameters. Common defaults, such as Gaussian action distributions with pathwise gradient estimators, are among the least reliable configurations, whereas bounded distributions with adaptive update schedules remain robust across a wide range of settings. These findings offer empirical guidance to practitioners across scientific and engineering domains for understanding and making component-level decisions when adapting actor-critic methods to new real-world control settings.

---


### 44. [Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable](https://arxiv.org/abs/2607.13285)

**<font color=#1a73e8>作者：</font>** Ruhan Wang, Yucheng Shi, Zongxia Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. Before such a change can be made, a developer or coding agent must identify all code locations that implement the target behavior. This is difficult because production harnesses are large, tightly coupled, and behaviorally distributed, while modification requests describe what the system should do and repositories are organized by files and modules. Code search, repository indexing, and long-context processing ease inspection, but still leave this behavior-to-code mapping to be recovered by hand. Behavior localization is therefore a central bottleneck in harness evolution. We introduce the Harness Handbook, a behavior-centric representation synthesized automatically from a harness codebase via static analysis and LLM-assisted structuring, linking each behavior to its corresponding source. We also introduce Behavior-Guided Progressive Disclosure (BGPD), which guides agents from high-level behaviors to relevant implementation details and verifies candidate locations against the current source. On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions. Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

---


### 45. [Theory-Level Autoformalization: From Isolated Statements to Unified Formal Knowledge Bases](https://arxiv.org/abs/2607.13292)

**<font color=#1a73e8>作者：</font>** Marcus J. Min, Mike He, Zhaoyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoformalization translates informal natural language into formal, machine-verifiable languages. While most work focuses on individual statements, real formalization efforts are inherently theory-level: they require an entire web of axioms, definitions, and lemmas before target theorems can even be stated. In this position paper, we argue for theory-level autoformalization: formalizing complete theories, including all their inter-dependencies, as structured libraries. We examine the significance of this shift, address alternative views, identify open challenges, and propose three promising paths forward. Our survey of autoformalization is available at this https URL.

---


### 46. [FOLIO: Focused Semantic Memory for Streaming Video Understanding](https://arxiv.org/abs/2607.13298)

**<font color=#1a73e8>作者：</font>** Haoyang Fan, Dhruv Parikh, Anvitha Ramachandran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In online streaming video understanding, a video stream continues to arrive and queries may be issued at any time. Because streaming frames grow without bound, the system must continuously compress and retain information from the observed video prefix while future frames and future queries remain unknown. The core challenge is deciding what information to retain and how to organize the maintained history: as this history grows with the stream, memory cost increases and many redundant visual details are retained, whereas later queries often depend on specific entities, actions, and their temporal changes. To address this challenge, we introduce FOLIO, a training-free focused semantic memory system that records important parts of the stream in higher detail while keeping surrounding context compact. As the stream arrives, FOLIO updates memory at the segment level, guided by a dynamic focus state, combining a short-term visual buffer with a long-term semantic memory organized around observed entities and linked to a visual-evidence cache. At query time, lightweight hybrid retrieval combines direct matching over the structured memory with semantic query expansion. FOLIO achieves state-of-the-art performance, reaching 82.0/69.1 Perception/Backward accuracy on OVO-Bench with Qwen3-VL-8B and 74.5 overall accuracy on StreamingBench, while substantially reducing the cost of maintaining streaming memory by reserving detailed records for focused entities and storing surrounding context compactly.

---


### 47. [Improving Medical Image Generative Models with Fréchet Distance Loss](https://arxiv.org/abs/2607.13300)

**<font color=#1a73e8>作者：</font>** Andrew Marshall, Xuanang Xu, Xiaoran Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion generative models have demonstrated immense potential for synthetic medical image generation. However, these models often struggle to capture complex morphological characteristics of heterogeneous tumors with irregular boundaries, limiting their utility for downstream clinical tasks such as segmentation. This limitation stems from the standard denoising objective: minimizing a per-pixel error, which smooths high-variance irregular structures characteristic of tumors. To address this, we propose finetuning these generative models with Fréchet Distance loss (FD-loss). FD-loss aligns the first and second order feature statistics of real and generated images in a pretrained encoder space, encouraging the generator to capture complex structural variations characteristic of heterogeneous tumors. We integrate FD-loss across diverse architectural settings, using both natural- and medical-image encoders on multiple liver and brain cancer datasets spanning CT and MRI modalities. Downstream segmentation networks trained on our FD-regularized synthetic data consistently achieve superior performance, improving tumor DSC by $>$$5\%$ over unregularized synthetic augmentation alone. Qualitative analysis suggests these gains are associated with more faithful tumor synthesis and fewer segmentation hallucinations. Our results show FD-loss as an effective regularizer for medical image generative models to improve clinical workflows.

---


### 48. [Finding the Right Tables and Columns: A Benchmark and Corpus-Adaptive Embeddings for SQL Schema Retrieval](https://arxiv.org/abs/2607.13311)

**<font color=#1a73e8>作者：</font>** Qingcheng Zeng, Puxuan Yu, Aman Mehta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval in the SQL setting has largely been studied as the task of finding, within a large collection of SQL statements, the statement that answers a natural-language question. At scale, however, a more fundamental retrieval problem precedes generation: schema retrieval, identifying the tables and columns a question requires in a database that may contain thousands of them, far more than fit in a model's context. We argue that this step warrants first-class evaluation. To this end, we recast five text-to-SQL datasets (Spider, BIRD, BEAVER, and two LiveSQLBench variants) as retrieval tasks at both table and column granularity, covering realistic and enterprise-scale schemas under two document representations, and we show that off-the-shelf text and code embedders transfer poorly to this setting. We then propose corpus-adaptive fine-tuning: natural-language queries are synthesized directly from the target schema corpus, granularity-aware hard negatives are mined, and a 305M-parameter embedder is fine-tuned contrastively. This procedure raises average recall@10 from 60.4 to 75.6 (nDCG@10 from 51.9 to 68.0), making the 305M model the strongest retriever under one billion parameters and competitive with state-of-the-art embedders of 4-8B parameters, more than an order of magnitude larger. The same recipe improves an 8B state-of-the-art embedder from 77.8 to 78.4 recall@10, matching the best result on the benchmark and indicating that the adaptation is backbone-agnostic. Leave-one-corpus-out experiments and a leakage audit show that these gains reflect a transferable schema-retrieval ability rather than memorization of the evaluation data. Our results establish schema linking as a standalone retrieval task and lightweight, label-free corpus adaptation as a practical route to deploying it at enterprise scale.

---


### 49. [Reflecting Process Expertise in Procedural Material Generation](https://arxiv.org/abs/2607.13318)

**<font color=#1a73e8>作者：</font>** Kunal Gupta, Gaurav Joshi, Yen-Ru Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Procedural material creation underpins applications in digital content creation, visual effects, and 3D asset design. Achieving high-quality results requires more than reproducing node graphs -- it demands understanding the process by which experts construct materials. We formulate procedural material generation as retrieval-time process reasoning over expert demonstrations, elevating process to a first-class representation beyond graph-only synthesis. Concretely, we represent expert workflows as process traces: textual records of construction steps, parameters, and design intent. To instantiate this idea, we use a pretrained LLM-based ProcessSynthesizer to synthesize a process trace aligned with a user's intent and a pretrained LLM-based Compiler to ground the process trace into an executable Blender material graph. Because procedural expertise is most naturally conveyed through demonstrations, we leverage tutorial videos as a source of process knowledge and extract textual, LLM-compatible traces using automated video analysis tools. In an expert study with five Blender artists (avg. 7.5 years of experience), materials generated by reflecting expert demonstrations were found to produce workflows requiring fewer edits, and more closely match professional design strategies than methods operating solely on static artifacts. A user study with 150 participants further shows that our approach achieves superior generation and editing performance compared to prior procedural systems. All code, models, and data will be available at this https URL

---


### 50. [Privacy Preserving Recommender Systems Balancing Personalization with Privacy](https://arxiv.org/abs/2607.13328)

**<font color=#1a73e8>作者：</font>** Ranjeet K Jha, Venkata Suresh Gummadilli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personalized recommendation systems are central to modern e-commerce and retail platforms, but they typically rely on centralized storage of detailed user interaction data, creating significant privacy and regulatory challenges. With increasing requirements from regulations such as GDPR, CCPA, and CPRA, organizations must develop recommendation systems that preserve user privacy without substantially degrading recommendation quality.
This work presents and evaluates a privacy-preserving recommendation framework that combines federated learning, differential privacy, cohort-level modeling, and privacy-aware intelligent agents. The framework keeps raw user data decentralized while introducing mathematically bounded noise to model updates. Experiments were conducted on synthetic retail datasets that emulate customer clickstream and purchase behavior. Recommendation quality was evaluated using Click-Through Rate (CTR), Precision@K, Recall@K, and Normalized Discounted Cumulative Gain (NDCG@K) across multiple differential privacy budgets.
We evaluate matrix factorization, neural collaborative filtering, and GRU4Rec under varying privacy constraints and analyze the trade-off between privacy and utility. An interactive Streamlit dashboard was developed to visualize recommendation performance, ranking stability, privacy-utility trade-offs, and fairness metrics. Results show that the proposed framework maintains competitive recommendation quality at moderate privacy budgets (approximately $\epsilon \approx 5$), demonstrating that strong privacy guarantees can be achieved with limited impact on recommendation effectiveness.
This work provides a practical framework for deploying privacy-preserving recommendation systems that balance personalization, regulatory compliance, and business objectives, offering a scalable approach for next-generation AI-driven retail platforms.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
