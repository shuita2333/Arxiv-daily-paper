# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 101. [Trace: Unmasking AI Attack Agents Through Terminal Behavior Fingerprinting](https://arxiv.org/abs/2605.01186)

**<font color=#1a73e8>作者：</font>** Murali Ediga, Sudipta Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-driven penetration testing agents are now capable of autonomously executing attacks within compromised networks. Identifying the model family that controls the active sessions of such agents provides valuable information towards understanding the intent of the attack and further developing attack countermeasures. In this paper, we introduce Trace, a novel multi-stage attribution and forensic framework for AI attack agents using terminal command sequences. Once Trace identifies a model family for the attacker agents, it guides a defensive prompt injection (DPI) strategy to the attacker model via a crafted payload. This is with the aim to exfiltrate system prompts from an attacker model, thus, revealing valuable information to understand the attacker intent and facilitate further forensic investigation. We have implemented our approach revolving around a Linux capture-the-flag (CTF) box. The attacker agents are bolstered via three distinct scaffolds and seven frontier model families. Our evaluation reveals that Trace achieves a macro F1 score of 0.981 in accurately fingerprinting the attacker model family (0.815 when generalizing to unseen scaffolds). Besides, the fingerprinting guides the DPI via a crafted payload to certain model families, resulting in system prompt extraction from 81.9% of non-Claude sessions on average (up to 98.3%) at 0.736 Sentence-BERT fidelity -- 1.88x higher than blind deployment. Finally, to validate the robustness of Trace, we evaluate it with a blackbox and proprietary scaffold employing multiple model families (Gemini and Claude Opus). Our evaluation identified the model family with an average 78% accuracy. Moreover, for the Gemini model family, the DPI employed by Trace revealed the entire system prompt and this has been confirmed by the developers. Trace therefore provides a fundamental first step towards attacker agent forensics.

---


### 102. [Compute Optimal Tokenization](https://arxiv.org/abs/2605.01188)

**<font color=#1a73e8>作者：</font>** Tomasz Limisiewicz, Artidoro Pagnoni, Srini Iyer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scaling laws enable the optimal selection of data amount and language model size, yet the impact of the data unit, the token, on this relationship remains underexplored. In this work, we systematically investigate how the information granularity of tokens, controlled by the compression rate (i.e., average bytes of text per token), affects scaling trends. We train 988 latent tokenized models (BLT) ranging from 50M to 7B parameters that enable setting the desired compression rate. This flexibility allows us to study the role of compression rate well beyond 4.57 bytes per token obtained with a popular BPE tokenizer. Our experiments reveal that in compute-optimal configurations, model parameter counts scale proportionally to data size measured in bytes, not in tokens as commonly perceived (Kaplan et al., 2020; Hoffmann et al., 2022). Furthermore, we discover that the optimal compression rate differs from the one obtained with BPE and decreases with compute. These findings generalize to both latent and subword tokenization, as well as to languages other than English, guiding language model developers on tokenization scheme selection for maximal compute efficiency.

---


### 103. [NEURON: A Neuro-symbolic System for Grounded Clinical Explainability](https://arxiv.org/abs/2605.01189)

**<font color=#1a73e8>作者：</font>** Anuradha Chandrasekaran, Dimitrios Zikos, Mutlu Mete 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical AI adoption is hindered by the black-box/grey-box nature of high-performing models, which lack the ontological grounding and narrative transparency required for professional-level explainability. We present NEURON, a neuro-symbolic system designed to enhance both predictive reliability and clinical interpretability. NEURON integrates SNOMED CT ontology-informed structural representations with machine learning models to bridge the gap between raw data and medical nomenclature. To facilitate human-aligned interaction, the system utilizes a Retrieval-Augmented Generation (RAG) grounded LLM layer to synthesize SHAP feature attributions and patient-specific clinical notes into coherent, natural-language explanations. Validated on the MIMIC-IV dataset for Acute Heart Failure mortality prediction, NEURON improved the AUC from 0.74-0.77 to 0.84-0.88 and significantly outperformed raw SHAP visualizations in human-aligned metrics (0.85 vs. 0.50). Our results demonstrate that NEURON offers a robust, scalable engineering solution for deploying trustworthy, human-centered connected health applications.

---


### 104. [Linear-Readout Floors and Threshold Recovery in Computation in Superposition](https://arxiv.org/abs/2605.01192)

**<font color=#1a73e8>作者：</font>** Hector Borobia, Elies Seguí-Mas, Guillermina Tormo-Carbó  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two recent approaches to computation in superposition reach different recursive capacity regimes: Hänni et al. certify $\tilde{O}(d^{3/2})$ computable features in width $d$ via an approximate-linear recursive template, while Adler and Shavit reach near-quadratic capacity (up to logarithmic factors) using thresholded Boolean recovery. The main contribution of this paper is conceptual: we argue these results are not contradictory because they maintain different interface invariants, and we formalize the distinction.
As a tool, we record a rank-trace Welch-type lower bound for biorthogonal linear readouts: for $F \gg d$, the worst-case off-diagonal cross-talk of any unit-diagonal linear readout is $\Omega(d^{-1/2})$, and the bound is tight on average for unit-norm tight frames. At quadratic feature load $F=d^2$, random-support threshold recovery succeeds for sparsities $s=O(d/\log d)$, while linear readouts still incur $\Omega(s/d)$ average per-coordinate squared error on Bernoulli sparse states. Matching the Welch floor against the published tolerance of the Hänni correction layer explains the $d^{3/2}$ scale as a compatibility threshold for that template, not a universal upper bound. Robust nonlinear reset beyond the Hänni template is left open.

---


### 105. [Focus and Dilution: The Multi-stage Learning Process of Attention](https://arxiv.org/abs/2605.01199)

**<font color=#1a73e8>作者：</font>** Zheng-An Chen, Pengxiao Lin, Zhi-Qin John Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have achieved remarkable success across a wide range of domains, yet our understanding of their training dynamics remains limited. In this work, we identify a recurrent focus-dilution cycle in attention learning and provide a rigorous explanation in a one-layer Transformer setting for Markovian data via gradient-flow analysis. Using stage-wise linearization around critical points, we show that a single focus-dilution cycle can be decomposed into a sequence of distinct stages. First, embedding and projection rapidly condense to a rank-one structure, while attention parameters remain effectively frozen. Then, the attention parameters begin to increase, inducing a frequency-driven focus toward high-frequency tokens. As attention continues to evolve, it generates next-order perturbations in embeddings, leading to a mass-redistribution mechanism that progressively dilutes this focus. Finally, small asymmetries among low-frequency tokens lift a degenerate critical point, opening new embedding directions and initiating the next cycle. Experiments on synthetic Markovian data as well as WikiText and TinyStories corroborate the predicted stages and cyclical dynamics.

---


### 106. [GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models](https://arxiv.org/abs/2605.01203)

**<font color=#1a73e8>作者：</font>** Zhouhao Sun, Xuan Zhang, Xiao Ding 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Currently, process reward models (PRMs) have exhibited remarkable potential for test-time scaling. Since large language models (LLMs) regularly generate flawed intermediate reasoning steps when tackling a broad spectrum of reasoning and decision-making tasks, PRMs are required to possess capabilities for detecting process-level errors in real-world scenarios. However, existing benchmarks primarily focus on mathematical reasoning, thereby failing to comprehensively evaluate the error detection ability of PRMs across diverse reasoning scenarios. To mitigate this gap, we introduce GR-Ben, a process-level benchmark specifically designed for assessing PRM's performance across two primary reasoning domains (science and logic) and nine subdomains. We conduct extensive experiments on a diverse set of 22 models, encompassing both PRMs and LLMs, and derive two key findings: (1) In domains beyond mathematical reasoning, the error-detection ability of existing PRMs and LLMs is found to be markedly weaker by comparison.(2) In general, PRMs are less adept at identifying knowledge-based errors, whereas LLMs exhibit poorer performance in detecting computational this http URL hope GR-Ben can foster future researches on PRMs for general domains, thereby enhancing the reasoning capabilities of LLMs.

---


### 107. [FLRSP: Privacy-Preserving Federated Learning Using Randomly Selected Model Parameters](https://arxiv.org/abs/2605.01204)

**<font color=#1a73e8>作者：</font>** Hiroto Sawada, Shoko Imaizumi, Hitoshi Kiya  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a method for privacy-preserving federated learning that uses randomly selected model parameters to update global models. High-quality deep neural networks (DNN) models require a huge amount of training data in general, but model training raises privacy concerns when dealing with sensitive or personal information. Federated learning is a distributed machine learning framework in which multiple clients and a server train a model collaboratively. However, if the shared updates are compromised, an attacker may reconstruct the original training data. In addition, previous methods for improving robustness generally reduce the accuracy. To overcome these issues, in our method called federated learning using randomly selected model parameters (FLRSP), model parameters computed in each local server are randomly selected and shared to update a global model in a central server. In experiments, image classification tasks were carried out on the ResNet34 architecture and the Vision Transformer (ViT) under the use of Federated Stochastic Gradient Descent (FedSGD) and Federated Averaging (FedAvg), and the results demonstrated our method's effectiveness in terms of image classification accuracy and robustness against state-of-the-art attacks compared with previous methods.

---


### 108. [Phishing Detection in Ethereum via Temporal Graph Contrastive Learning](https://arxiv.org/abs/2605.01207)

**<font color=#1a73e8>作者：</font>** Cong Wu, Jing Chen, Siqi Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain and decentralized finance have revolutionized the financial ecosystem while simultaneously exposing it to cryptocurrency phishing attacks. Existing phishing detection methods primarily rely on graph learning, but they face significant limitations. Static graph learning approaches fail to account for the temporal evolution of phishing patterns, while semi-dynamic methods, such as those combining static GNNs with LSTM, struggle to capture the irregular and bursty nature of blockchain transactions. Moreover, these methods overlook the diversity of Ethereum transactions, treating them as homogeneous graphs, and heavily rely on supervised learning, which requires extensive labeled data that is not readily available. These limitations reduce their adaptability to emerging phishing threats.
In this paper, we present PhishEye, a fully dynamic self-supervised system that monitors on-chain transactions to detect phishing activities. PhishEye formulates Ethereum transactions as a heterogeneous temporal attributed multi-graph and incorporates a novel temporal graph contrastive learning model, which captures both temporal patterns and heterogeneous transaction types. The evaluation on a dataset of 161,658 addresses and 416,541 transactions shows that PhishEye outperforms existing methods, achieving an F1 score of 87.23% and an AUC of 98.43% for phishing transaction detection, and an F1 score of 94.19% and an AUC of 98.03% for phishing account detection. In real-world deployment from May 1, 2023 to July 31, 2024, PhishEye identified 1,803 previously unknown phishing addresses, providing early alerts that helped prevent losses exceeding 2 billion USD.

---


### 109. [Faithful Mobile GUI Agents with Guided Advantage Estimator](https://arxiv.org/abs/2605.01208)

**<font color=#1a73e8>作者：</font>** Haowen Hu, Pengzhou Cheng, Zheng Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language model based graphical user interface (GUI) agents have shown strong interaction capabilities. However, they often behave unfaithfully, relying on memorized shortcuts rather than grounding actions in displayed screen evidence or user instructions. To address this, we propose Faithful-Agent, a faithfulness-first framework that reformulates GUI interaction to prioritize evidence groundedness and internal consistency. Faithful-Agent employs a two-stage pipeline: (i) a faithfulness-oriented SFT stage to instill abstainment behaviors under evidence perturbations; (ii) an RFT stage that further amplifies faithfulness by introducing the guided advantage estimator (GuAE), an anchor-based and variance-adaptive advantage tempering mechanism built upon GRPO. GuAE prevents advantage collapse in low-variance rollout groups under sparse GUI rewards, and with a thought-action consistency reward, Faithful-Agent (Stage II) elevates the Trap SR from 13.88\% to 80.21\% relative to the baseline, while preserving robust general instruction-following performance.

---


### 110. [Write-Domain Separation and Non-Custodial Enforcement: A Structural Impossibility in Account-Based Ledgers, with a Commitment-Based Construction](https://arxiv.org/abs/2605.01210)

**<font color=#1a73e8>作者：</font>** Matthias Hauser  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Account-based ledgers -- standard externally-owned accounts (EOAs), ERC-4337 smart accounts, post-Pectra EIP-7702 delegated EOAs -- place the holder of the controlling key at the apex of asset authorization. We ask a structural question about ledger access control: under this authorization model, can a protocol enforce the future disposition of an asset without taking custody and without requiring the owner's cooperation at enforcement time? We formalize the target as Non-Custodial Enforced Encumbrance (NCEE), a four-property specification covering self-custody, transition restriction, irrevocability, and permissionless enforcement.
We define the Key Sovereignty Axiom (KS) and prove that any ledger satisfying KS cannot realize NCEE; standard EOAs, ERC-4337 smart accounts, and EIP-7702 delegated EOAs satisfy KS for their standard asset paths. We define Asset-Authorization Coupling (AAC) and prove it necessary for NCEE in the transfer-dichotomous asset setting. To witness the positive side, we introduce the envelope, a primitive for commitment-based private-state ledgers that binds a note, a condition tree, and a redistribution intent to protocol-maintained marker sets, separating ordinary spend nullifiers from a new encumbrance-namespace nullifier derived from note randomness rather than the owner key. We prove the envelope realizes NCEE under stated cryptographic assumptions and a deployment assumption that the marker-set registry is immutable; three concrete deployment templates are given.
We define games for encumbrance integrity, settlement security, key-compromise resilience, and encumbrance indistinguishability. A reference implementation in Noir and UltraHonk supports the empirical claims, with gas measurements, recursive aggregation benchmarks, and a practical-economics analysis.

---


### 111. [Asymmetric Invertible Threat: Learning Reversible Privacy Defense for Face Recognition](https://arxiv.org/abs/2605.01217)

**<font color=#1a73e8>作者：</font>** Jiabei Zhang, Ziyuan Yang, Andrew Beng Jin Teoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Recognition systems are widely deployed in real-world applications, but they also raise privacy concerns due to unauthorized collection and misuse of facial data. Existing adversarial privacy protection methods rely on input-space perturbations to obfuscate identity information, yet their protection can degrade when adversaries learn restoration or purification mappings that partially invert the transformation. We study this setting as an asymmetric adversarial attack, in which reverse manipulation becomes feasible because existing defense paradigms do not control reversibility. To address this problem, we propose Asymmetric Reversible Face Protection (ARFP), a restoration-aware extension of personalized face cloaking that integrates privacy protection, keyed recovery, and tamper indication in a single framework. ARFP consists of three components: Key-Conditioned Manifold Binding, which ties the protection transformation to a user-provided key; Adversarial Restoration-Aware Training, which introduces a surrogate restoration adversary during training to improve robustness against evaluated inverse purification attacks; and Authorized Reversible Restoration, which supports recovery with the correct key while providing nonce-based tamper indication. Extensive experiments under the threat models considered in this work show that ARFP improves resistance to the evaluated restoration attacks while preserving authorized recovery utility. These results provide empirical evidence of key-sensitive recovery behavior and tamper awareness in the tested settings.

---


### 112. [Visual Implicit Autoregressive Modeling](https://arxiv.org/abs/2605.01220)

**<font color=#1a73e8>作者：</font>** Pengfei Jiang, Jixiang Luo, Luxi Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive Modeling (VAR) based on next-scale prediction achieves strong generation quality, but their explicit deep stacks fix the amount of computation per scale and inflate memory at high resolutions. We introduce Visual Implicit Autoregressive Modeling (VIAR), a next-scale autoregressive generator that embeds an implicit equilibrium layer between shallow pre/post blocks. The implicit layer is trained with Jacobian-Free Backpropagation, yielding constant training memory, while inference exposes a per-scale iteration knob that enables compute control. On ImageNet 256x256 benchmark, VIAR attains FID 2.16, and sFID 8.07 with only 38.4% parameters of VAR, matching or surpassing strong AR baselines and remaining competitive with large diffusion models. By controlling the per-scale knob, VIAR can reduce peak memory from 19.24 GB to 8.53 GB and doubles throughput from 15.16 to 32.08 images/s on a single RTX 4090, without retraining. Ablations show that fewer steps are sufficient for fixed-point iterations to converge and that VIAR consistently dominates VAR across quality efficiency operating points. In zero shot in-painting and class-conditional editing, VIAR produces sharper details and smoother boundaries while preserving global structure, validating the benefits of implicit equilibria and per-scale compute control for practical, deployable visual generation.

---


### 113. [Local Hessian Spectral Filtering for Robust Intrinsic Dimension Estimation](https://arxiv.org/abs/2605.01221)

**<font color=#1a73e8>作者：</font>** Genki Osada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While diffusion models enable new approaches for estimating Local Intrinsic Dimension (LID), existing methods fail in high-dimensional spaces where noise from vast normal directions overwhelms the tangent signal. We propose Local Hessian Spectral Dimension (LHSD), which resolves this by applying spectral filtering to the log-density Hessian, explicitly cutting off large eigenvalues associated with normal directions to count zero-curvature tangent directions. Implemented using Stochastic Lanczos Quadrature (SLQ), LHSD avoids full Hessian construction, achieving linear scalability with dimension $D$. Experiments on synthetic and real data confirm LHSD's superior robustness and its utility in detecting memorization in large-scale diffusion models.

---


### 114. [Zero-Shot Signal Temporal Logic Planning with Disjunctive Branch Selection in Dynamic Semantic Maps](https://arxiv.org/abs/2605.01222)

**<font color=#1a73e8>作者：</font>** Bowen Ye, Ancheng Hou, Junyue Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Signal Temporal Logic (STL) offers verifiable task specifications and is crucial for safety-critical control. Yet STL planning remains challenging: exact optimization-based methods are often too slow, and learning-based methods struggle to generalize across varying environments. We propose a zero-shot STL planning solver for variable-map environments that generates feasible trajectories without retraining. By integrating a map-conditioned Transformer architecture with a lightweight heuristic, our approach effectively handles complex disjunctive (OR) subformulas. Furthermore, we leverage Transitive Reinforcement Learning (TRL) to ensure consistent temporal grounding and logical coherence across decomposed sub-tasks. Experiments on dynamic semantic maps with diverse obstacle layouts demonstrate consistent gains, highlighting the framework's superior zero-shot generalization to changing environments and broad STL coverage.

---


### 115. [Arbitrarily Conditioned Hierarchical Flows for Spatiotemporal Events](https://arxiv.org/abs/2605.01226)

**<font color=#1a73e8>作者：</font>** Keyan Chen, Qiwei Yuan, Zhitong Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Events in spatiotemporal systems are ubiquitous, yet modeling their complex distributions remains challenging. Existing point process models often rely on strong structural assumptions and are typically limited to autoregressive, event-by-event prediction. As a result, they struggle to support broader inference tasks such as inverse inference, trajectory reconstruction, and recovery of missing event locations. We introduce Arbitrarily Conditioned Hierarchical Flows (ARCH), a hierarchical flow matching framework for spatiotemporal event modeling. ARCH is expressive enough to capture complex event distributions while enabling tractable and accurate computation of conditional intensities, which quantify instantaneous event risk. Built on a history-encoder-generative-decoder architecture, ARCH introduces a hybrid masking strategy for flexible conditioning on arbitrary observed events. This enables a unified treatment of forecasting, inverse inference, and partial trajectory recovery within a single framework. Experiments on synthetic and real-world datasets show that ARCH consistently outperforms existing baselines across both prediction and conditional inference tasks.

---


### 116. [Attention Sinks in Massively Multilingual Neural Machine Translation:Discovery, Analysis, and Mitigation](https://arxiv.org/abs/2605.01229)

**<font color=#1a73e8>作者：</font>** Hillary Mutisya, John Mugane  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-attention patterns in neural machine translation (NMT) are widely used to study how multilingual models align linguistic structure. We report a systematic artifact in cross-attention analysis of NLLB-200 (600M): non-content tokens - primarily end-of-sequence tokens, language tags, and punctuation - capture 83 percent to 91 percent of total cross-attention mass. We term these "attention sinks," extending findings from LLMs [Xiao et al., 2023] to NMT cross-attention and identifying a causal mechanism rooted in vocabulary design rather than position bias. This artifact causes raw metrics to underestimate content-level similarity by nearly half (36.7 percent raw vs. 70.7 percent filtered), rendering uncorrected analyses unreliable. To address this, we validate a content-only filtering methodology that removes non-content tokens and renormalizes the distribution. Applying this to 1,000 parallel sentences across African languages (Swahili, Kikuyu, Somali, Luo) and non-African benchmarks (German, Turkish, Chinese, Hindi), we confirm the artifact is universal and recover masked linguistic signals: a 16.9 percentage-point gap between teacher-forcing and generation modes, clear language-family clustering in attention entropy, and a hidden Somali paradox linking SOV word order to monotonic alignment. We release our filtering toolkit and corrected datasets to support reproducible interpretability research on multilingual NMT.

---


### 117. [CombinationTS: A Modular Framework for Understanding Time-Series Forecasting Models](https://arxiv.org/abs/2605.01231)

**<font color=#1a73e8>作者：</font>** Xiaorui Wang, Fanda Fan, Chenxi Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent progress in time-series forecasting has led to rapidly increasing architectural complexity, yet many reported State-of-the-Art gains are statistically fragile or misattributed. We argue that progress requires a shift from model selection to modular attribution, identifying which components truly drive performance. We propose CombinationTS, a self-contained probabilistic evaluation framework that decomposes forecasting models into orthogonal modules--Input Transformation, Embedding, Encoder, Decoder, and Output Transformation--and evaluates them under a shared evaluation condition space. By quantifying each component via marginalized performance ($\mu$) and stability ($\sigma$), CombinationTS enables robust attribution beyond fragile point estimates. Through large-scale paired evaluation, we uncover the Identity Paradox: once the data view (Embedding) is well-designed, a parameter-free Identity Encoder often matches or outperforms complex backbones. We further show that explicit structural priors introduced via Input Transformations yield a more favorable performance-stability trade-off than increasing Encoder complexity, establishing a principled baseline for architectural necessity.

---


### 118. [TT4D: A Pipeline and Dataset for Table Tennis 4D Reconstruction From Monocular Videos](https://arxiv.org/abs/2605.01234)

**<font color=#1a73e8>作者：</font>** Nima Rahmanian, Daniel Kienzle, Thomas Gossard 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TT4D, a large-scale, high-fidelity table tennis dataset. It provides $140+$ hours of reconstructed singles and doubles gameplay from monocular broadcast videos, featuring multimodal annotations like high-quality camera calibrations, precise 3D ball positions, ball spin, time segmentation, and 3D human meshes over time. This rich data provides a new foundation for virtual replay, in-depth player analysis, and robot learning. The dataset's combination of scale and precision is achieved through a novel reconstruction pipeline. Prior methods first partition a game sequence into individual shot segments based on the 2D ball track, and only then attempt reconstruction. However, 2D-based time segmentation collapses under occlusion and varied camera viewpoints, preventing reliable reconstruction. We invert this paradigm by first lifting the entire unsegmented 2D ball track to 3D through a learned lifting network. This 3D trajectory then allows us to reliably perform time segmentation. The learned lifting network also infers the ball's spin, handles unreliable ball detections, and successfully reconstructs the ball trajectory in cases of high occlusion. This lift-first design is necessary, as our pipeline is the only method capable of reconstructing table tennis gameplay from general-view broadcast monocular videos. We demonstrate the dataset's fidelity through two downstream tasks: estimating the racket's pose \& velocity at impact, and training a generative model of competitive rallies.

---


### 119. [Degradation-Aware Adaptive Context Gating for Unified Image Restoration](https://arxiv.org/abs/2605.01236)

**<font color=#1a73e8>作者：</font>** Lei He, Jielei Chu, Fengmao Lv 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified image restoration using a single model often faces task interference due to diverse degradations. To address this, we propose DACG-IR (Degradation-Aware Adaptive Context Gating), which enables explicit perception of degradation characteristics to dynamically modulate feature representations. Our method constructs degradation-aware contextual representations from the input to modulate attention distribution, frequency-domain features, and feature aggregation. Specifically, a lightweight multi-scale degradation-aware module extracts coarse degradation information and generates layer-wise prompts. These prompts guide attention temperature and output gating in encoder and decoder blocks for adaptive feature extraction. Additionally, a spatial-channel dual-gated adaptive fusion mechanism refines encoder features, suppressing noise propagation from shallow to deep layers. This design effectively suppresses degradation-induced noise while preserving informative structures. Experiments show DACG-IR outperforms state-of-the-art methods in single-task, all-in-one, adverse weather removal, and composite degradation settings. Code: this https URL

---


### 120. [EduGage: Methods and Dataset for Sensor-Based Momentary Assessment of Engagement in Self-Guided Video Learning](https://arxiv.org/abs/2605.01238)

**<font color=#1a73e8>作者：</font>** Zikang Leng, Edan Eyal, Yingtian Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Engagement, which links to attentional, emotional, and cognitive dimensions, plays an important role in learning. In online and video-based learning environments, learners often need to regulate their own interactions with instructional materials. Measuring and reflecting on engagement can therefore support both learners and adaptive learning systems. In this study, we use wearable and camera-based sensing devices to collect physiological and motion signals, including PPG, ECG, EDA, EEG, IMU, heart rate, temperature, and eye-tracking data, to estimate learner engagement. We conducted a user study with 16 participants in a video-based learning scenario, where participants completed learning tasks and provided repeated in-situ self-reports of engagement through brief probes. We develop and evaluate a system for engagement estimation, compare different sensing modalities, and further analyze the feasibility and effectiveness of multimodal modeling for characterizing learner engagement. Across participant-based cross-validation, our model achieves an MAE of 0.81, 83.75% within-1 accuracy, 73.93% binary accuracy, and 68.45% binary Macro-F1, outperforming sensor-free, statistical, deep temporal, foundation-model, and LLM-based baselines. Our results suggest that fine-grained engagement estimation is feasible but inherently noisy, and that practical systems should prioritize lightweight combinations of behavioral and physiological signals over full multimodal instrumentation. We release the EduGage dataset, including synchronized multimodal sensor signals, probe-aligned momentary engagement labels, video metadata, quizzes, and study materials, to support reproducible research on fine-grained sensor-based engagement modeling in self-guided learning.

---


### 121. [Rhamba: Region-Aware Hybrid Attention-Mamba Framework for Self-Supervised Learning in Resting-State fMRI](https://arxiv.org/abs/2605.01240)

**<font color=#1a73e8>作者：</font>** Ruthwik Reddy Doodipala, Pankaj Pandey, Pratheek Eranki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised pretraining is promising for large-scale neuroimaging, yet the impact of region-aware masking and hybrid sequence modeling remains underexplored. In this work, we introduce Rhamba, a region-aware pretraining framework that integrates anatomically guided masking with hybrid Attention-Mamba architectures for resting state functional magnetic resonance imaging (fMRI) analysis. Models were pretrained on the ABIDE dataset using region-aligned patch embeddings and three masking strategies (Any, Majority, and Pure) with increasing spatial specificity. We evaluated four architectural variants: a Mamba only model, an Alternate architecture with interleaved Mamba and Attention blocks, and two hybrid encoder-decoder configurations (Attention-Mamba (AM) and Mamba-Attention (MA)). The pretrained models were fine-tuned on downstream classification tasks using the COBRE and ADHD-200 datasets for schizophrenia and attention-deficit/hyperactivity disorder discrimination. We employed Integrated Gradients, an explainable AI method, to identify the brain regions contributing to model predictions. Masking strategy strongly influenced reconstruction behavior, with reconstruction loss following a consistent ordering (Any > Majority > Pure). However, this trend did not directly translate into downstream performance, where differences were modest and dataset-dependent. The hybrid architecture with the MA configuration achieved the highest average AUROC across both datasets, and Rhamba outperformed state-of-the-art methods in comparative evaluation. Region-wise analysis showed that peak performance depends on the interaction between masking strategy and architecture rather than a single dominant configuration. Overall, Rhamba offers a flexible framework for balancing interpretability, scalability, and performance in large-scale fMRI representation learning.

---


### 122. [Breaking the Computational Barrier: Provably Efficient Actor-Critic for Low-Rank MDPs](https://arxiv.org/abs/2605.01242)

**<font color=#1a73e8>作者：</font>** Ruiquan Huang, Donghao Li, Yingbin Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is a fundamental framework for sequential decision-making, in which an agent learns an optimal policy through interactions with an unknown environment. In settings with function approximation, many existing RL algorithms achieve favorable sample complexity, but often rely on computationally intractable oracles. In this paper, we use supervised learning as a computational proxy to establish a clear hierarchy of commonly adopted RL oracles under low-rank Markov Decision Processes (MDPs). This hierarchy shows that policy evaluation is the most computationally efficient oracle, provided that supervised learning can be efficiently solved. Motivated by this observation, we propose a novel optimistic actor-critic algorithm that relies solely on the policy evaluation oracle. We prove that our algorithm outperforms the existing sample complexity guarantees for low-rank MDPs while avoiding computationally expensive planning or optimization oracles commonly assumed in prior works. We further extend our theoretical results to approximately low-rank MDPs and demonstrate that this setting captures a broad class of real-world environments. Finally, we validate our theoretical results with experiments on several standard Gym environments.

---


### 123. [The Garden of Forking Paths: Narrative Arc-Conditioned Gameplay Planning](https://arxiv.org/abs/2605.01245)

**<font color=#1a73e8>作者：</font>** Yunge Wen, Chenliang Huang, Hangyu Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Narrative archetypes (e.g., Hero's Journey, Three-act structure) provide universal story structures that resonate across cultures and media and are important for video game storytelling, yet existing LLM-based methods lack explicit use of these archetypes in procedurally generated games. We propose Forking Garden, a framework for narrative arc-conditioned gameplay planning that generates branching games from user-provided storylines. Our approach first generates a diverse pool of independent nodes, then assembles them into a dungeon graph via arc-guided constraint algorithms, where each node achieves multimodal alignment of gameplay elements. We develop an end-to-end interactive system that instantiates the framework.

---


### 124. [FP-Agent: Fingerprinting AI Browsing Agents](https://arxiv.org/abs/2605.01247)

**<font color=#1a73e8>作者：</font>** Ethan Wang, Zubair Shafiq, Yash Vekaria  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI browsing agents are an emerging class of AI-powered bots capable of autonomously navigating websites. Unlike traditional web bots, AI browsing agents typically operate using real browsers and perform everyday tasks, making them difficult to detect. Yet little is known about whether existing AI browsing agents can be distinguished from humans and one another based on their browser or behavioral fingerprints. In this paper, we present the first controlled measurement study of seven AI browsing agents and human users. Using an instrumented honey website, we collect browser and behavioral fingerprint features while AI browsing agents and humans perform three tasks: flight booking, online shopping, and forum interaction. We then train FP-Agent, a multi-class classifier, to evaluate the discriminative power of these features. We find that browser fingerprints provide limited discriminative power when shared by multiple AI browsing agents. Behavioral fingerprints, however, are distinctive: differences in typing, scrolling, and mouse behavior separate AI browsing agents from humans and one another. In a case study evaluating Cloudflare's bot detection, FP-Agent detects all seven AI browsing agents, whereas Cloudflare detects only one. Our findings show that behavioral fingerprints are a critical component to reliably detect and control this emerging form of web traffic.

---


### 125. [S^3-R1: Learning to Retrieve and Answer Step-by-Step with Synthetic Data](https://arxiv.org/abs/2605.01248)

**<font color=#1a73e8>作者：</font>** Harsh Goel, Akhil Udathu, Susmija Jabireddy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training has enabled newer capabilities in models, such as agentic tool-use for search. However, these models struggle primarily due to limitations with sparse outcome-based rewards and a lack of training data that encapsulates questions of differing hardness, which results in models not performing deeper searches with tools to collect evidence for question-answering. To address these limitations, we introduce S^3-R1 (Synthetic data and stabilized Search R1), a framework that couples a data-centric approach with denser learning signals. We first develop a synthetic generation and curation pipeline that programmatically derives diverse, multi-hop questions from existing documents. This pipeline incorporates a retrieval-based verification step to specifically isolate questions of intermediate difficulty. We then pair this expanded training set with a reward structure that evaluates both intermediate search quality and the correctness of the final answer. This setup directly mitigates the credit assignment problems inherent to sparse rewards. Our evaluations show that S^3-R1 outperforms existing baselines by learning more effective search and synthesis strategies, yielding up to a 10% improvement in robust generalization on out-of-domain datasets.

---


### 126. [What Does a Meow Mean? In Search of Intuitively Understandable Communication by a Nonverbal Companion Robot](https://arxiv.org/abs/2605.01251)

**<font color=#1a73e8>作者：</font>** Vivienne Bihe Chi, Claudia B. Rébola, Bertram F. Malle  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Older adults living alone have a number of challenges, and robots can help with some of them--by providing reminders, initiating activity, or offering comfort. As part of developing a cat robot with limited assistive functions, we designed a set of nonverbal communication signals, both auditory (cat sounds) and visual (icons on a small display). To evaluate these signals we used a mixed-methods, user-centered approach. After a pilot study, a focus group with older adults suggested revisions to the initial signal set. A large-sample online experiment then tested whether adults over the age of 65 could accurately infer the robot's communicative intentions. When both visual and auditory signals were present, accuracy was high. When visual signals were absent, accuracy often decreased; when auditory signals were absent, accuracy sometimes increased. So the auditory signals were less helpful, except when the robot conveyed strong sentiments (e.g., purring while being petted).

---


### 127. [Uncertainty-Aware Trip Purpose Inference from GPS Trajectories via POI Semantic Zones and Pareto Calibration](https://arxiv.org/abs/2605.01257)

**<font color=#1a73e8>作者：</font>** Bo Yang, Haoxuan Ma, Yifan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale GPS trajectory data offer rich observations of human mobility, yet assigning trip purposes to detected stops remains challenging due to the absence of individual-level ground truth, spatial uncertainty from GPS noise and incomplete points of interest (POIs) coverage, and fundamental behavioral differences across trip purposes. We propose a weakly supervised framework integrating neighborhood-level POI semantic zones with distance-weighted spatial likelihoods, differentiated inference strategies for mandatory and non-mandatory activities, and a multi-phase Pareto optimization that jointly minimizes distributional divergence from household travel survey statistics and maximizes inference reliability without requiring annotated labels. Evaluated on over 81 million staypoints in Los Angeles, the framework reduces activity type frequency Jensen-Shannon distance (JSD) by 23%, start time JSD by 48%, and duration JSD by 12% respectively relative to a comparable baseline. The proposed approach provides a scalable and uncertainty-aware path from raw GPS trajectories to semantically annotated mobility data for travel demand modeling and transportation policy analysis.

---


### 128. [Continuous Temporal Representations of Event-Based Signals via Interference-Based Wave Modeling](https://arxiv.org/abs/2605.01270)

**<font color=#1a73e8>作者：</font>** Magnus Bengtsson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal signals arising from event-driven biological processes, such as surface electromyography (sEMG), exhibit asynchronous and highly structured activation patterns that are challenging to model using conventional discrete or purely real-valued representations.
In this work, we propose a continuous temporal modeling framework based on interference-based wave representations. The approach maps event-like input signals into a complex-valued latent wave field, where temporal structure is encoded through phase modulation and interactions between latent components.
By projecting the resulting wave field onto an energy domain, the model induces structured activation patterns that capture both temporal localization and relational dependencies within finite observation windows, without relying on explicit recurrence or causal state propagation.
The proposed formulation is particularly suited for event-driven biosignals, where continuous representations enable efficient gradient-based optimization and robust feature extraction. In particular, the method is designed to support learning from sEMG data for downstream control tasks in biomechanical systems, such as prosthetic devices and exoskeletons.
Experimental results demonstrate that the proposed interference-based wave model provides improved representation quality compared to purely real-valued representations, while maintaining computational efficiency suitable for practical deployment.

---


### 129. [GameScope: A Multi-Attribute, Multi-Codec Benchmark Dataset for Gaming Video Quality Assessment](https://arxiv.org/abs/2605.01272)

**<font color=#1a73e8>作者：</font>** Rajesh Sureddi, Shreshth Saini, Avinab Saha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of video game streaming has grown rapidly, with major platforms such as YouTube and Twitch using different codecs. To support quality assessment models that work consistently across any codec, it is necessary to have access to large, diverse subjective gaming quality datasets. Currently, there are only a few available, each having limitations. To address this gap, we present the largest gaming video quality dataset to date, incorporating both user-generated content (UGC) and professional-generated content (PGC) with extensive visual diversity. Our dataset covers the most widely used codecs - H.264, H.265, and AV1 - and consists of 4,048 video samples, each annotated by an average of 37 mean opinion score (MOS) ratings. In addition to overall quality scores, we collect coarse-grained quality attributes, enabling a better understanding of perceptual factors. We study the performance of leading video quality assessment methods on this dataset, including a vision language model that outperforms all the benchmarks. To the best of our knowledge, this is the first dataset that comprehensively addresses gaming video quality assessment across multiple codecs and content types with quality attributes. Our dataset is publicly available at this https URL.

---


### 130. [CNN-based Multi-In-Multi-Out Model for Efficient Spatiotemporal Prediction](https://arxiv.org/abs/2605.01277)

**<font color=#1a73e8>作者：</font>** Hyeonseok Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, Convolutional Neural Network (CNN) or Transformer architecture based models have been proposed to overcome the limitations of Recurrent Neural Network (RNN) based models in spatiotemporal prediction. These models prevent the inefficiency of parallelization limitation due to the sequential properties and stacked error due to the recursive method, and show high performance. Novertheless, there are still some challengies. First, CNN based models have difficulty considering global information due to the local properties of the kernel, and their performance is limited. In addition, information is mixed because the time axis is combined with the channel axis of the image for processing. Models based on Transformer architecture have high complexity due to the self-attention calcuation and take a long training time. In this paper, we propose a new structure model called CNN-based Multi-In-Multi-Out model for Efficient Spatiotemporal Prediction (MIMO-ESP) to overcome these limitations. MIMO-ESP considers global information and significantly improves complexity by configuring a Transformer architecture based on CNN. In addition, it treats the time axis as an independent axis without combining it, and effectively considers spatiotemporal information together by applying dilation. This structure makes MIMO-ESP efficient and high performance. Extensive experiment results on three promising benchmark datasets which including video, traffic, and precipitation prediction tasks demonstrate that the usefulness of MIMO-ESP due to the achieved competitive efficiency while outperforming existing models. Furthermore, the ablation study results demonstrate the usefulness of the components of MIMO-ESP, emphasizing the potential of the proposed approaches.

---


### 131. [Developing a Strong Pre-Trained Base Model for Plant Leaf Disease Classification](https://arxiv.org/abs/2605.01283)

**<font color=#1a73e8>作者：</font>** David J. Richter  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Plants, crops and their yields are essential to our very existence, but diseases and pests cause large losses every year. As such it is vital to ensure that diseases can be spotted early and treated accordingly and stopping the spread while still possible. Manual and traditional methods require personal to walk through the field and check for symptoms 'by hand'. This is very laborious and very time consuming, so ML methods have been applied as a result and they have garnered promising results. CNN models are especially efficient as they can automatically extract features from images without any manual feature construction before then feeding the features to a classifier. Datasets are largely influential to the final performance of the model. Despite the importance that datasets pose to the field, there still seems to be somewhat of a discrepancy between what is publicly available for use and what would be required to sufficiently train fully capable models. To overcome these shortcomings, as part of this thesis open datasets for the field of plant leaf disease classification have been identified as well as models that can be trained on them and extensive benchmarks have been carried out to identify their suitability. Then a new dataset was constructed based on those findings as well as on the findings of a augmentation applicability study, which will be used to train a new Base Model based on the DenseNet201 architecture, which managed to outperform the baseline model on said new dataset as well as outperforming it on plant leaf disease classification domain specific Transfer-Learning experiments on another new dataset. This new model manages to train models through Transfer-Learning (TL) faster, more robust, more stable, and with less data than general model would, overcoming a large number of issues that the field still suffers from.

---


### 132. [A Theory of Saddle Escape in Deep Nonlinear Networks](https://arxiv.org/abs/2605.01288)

**<font color=#1a73e8>作者：</font>** Divit Rawal, Michael R. DeWeese  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In deep networks with small initialization, training exhibits long plateaus separated by sharp feature-acquisition transitions. Whereas shallow nonlinear networks and deep linear networks are well studied, extending these analyses to deep nonlinear networks remains challenging. We derive an exact identity for the imbalance of Frobenius norms of layer weight matrices that holds for any smooth activation and any differentiable loss and use this to classify activation functions into four universality classes. On the permutation-symmetric submanifold, the identity combines with an approximate balance law to reduce the full matrix flow to a scalar ODE, giving a critical-depth escape time law $\tau_\star = \Theta(\varepsilon^{-(r-2)})$ governed by the number $r$ of layers at the bottleneck scale rather than the total depth $L$. We find that this same $r-2$ exponent is recovered under He-normal initialization with $r$ bottleneck layers rescaled by $\varepsilon$, where the symmetry manifold is preserved by the flow but not attracting. We find close agreement between our theory and numerical simulations.

---


### 133. [Congestion-Aware Dynamic Axonal Delay for Spiking Neural Networks](https://arxiv.org/abs/2605.01291)

**<font color=#1a73e8>作者：</font>** Dewei Bai, Hongxiang Peng, Yunyun Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking Neural Networks (SNNs) are widely regarded as an energy-efficient paradigm for modeling and processing temporal and event-driven information. Incorporating delays in SNNs has been proven to be an effective mechanism for improving spike alignment in event-driven tasks. However, existing delay learning approaches predominantly assign static delays to individual synapses, resulting in a large number of delay parameters and limited adaptability to input-dependent activity dynamics. To this end, we propose a Congestion-Aware Dynamic Axonal Delay mechanism, decomposing the delay into a channel-wise static base delay for temporal structuring and a global, activity-conditioned shift that dynamically regulates the state update rate under varying spike intensities. The delay parameters are learned using differentiable linear interpolation and discretized at inference time, preserving the benefits of our dynamic delay while incurring only minimal additional cost. Experiments on speech benchmarks, including the Spiking Heidelberg Dataset, Spiking Speech Commands, and Google Speech Commands, demonstrate that introducing congestion-aware delays into synaptic signal transmission effectively improves accuracy on temporal tasks, notably achieving 93.75\% accuracy on SHD, 80.49\% accuracy on SSC, and 95.53\% on GSC-35, while reducing the parameter count by approximately 50\% compared to state-of-the-art delay-based methods with the same architecture.

---


### 134. [Autonomous Drift Learning in Data Streams: A Unified Perspective](https://arxiv.org/abs/2605.01295)

**<font color=#1a73e8>作者：</font>** Xiaoyu Yang, En Yu, Jie Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the pursuit of autonomous learning systems, the foundational assumption of stationarity, the premise that data distributions and model behaviors remain constant, is fundamentally untenable. Historically, the research community has addressed non-stationary environments almost exclusively under the scope of concept drift, focusing primarily on temporal shifts in streams. However, as learning systems become increasingly autonomous and complex, merely adapting to temporal non-stationarity is no longer sufficient. Evolving beyond this traditional perspective, we propose a novel, three-dimensional taxonomy that systematizes the field based on the operational state of the system. First, time stream drift distinguishes between stochastic arbitrary patterns and structural rhythmic dynamics. Second, data stream drift disentangles shifts in feature representations, identified as representation drift, from changes in underlying semantics, recognized as semantic drift. Third, model stream drift characterizes the internal endogenous divergence of learning systems through the lenses of sequential plasticity, decentralized heterogeneity, and policy instability. Based on this framework, we systematically review 193 representative studies and identify key open challenges. By bridging the fragmented paradigms of drift adaptation, continual learning, and temporal generalization, this survey outlines a roadmap for building self-evolving intelligent systems capable of learning autonomously through continuous change.

---


### 135. [SIFT-VTON: Geometric Correspondence Supervision on Cross-Attention for Virtual Try-On](https://arxiv.org/abs/2605.01296)

**<font color=#1a73e8>作者：</font>** Kosuke Takemoto, Takafumi Koshinaka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based virtual try-on methods achieve photorealistic synthesis through cross-attention mechanisms that transfer garment features to target body regions. However, these approaches rely on implicit learning of spatial correspondences, struggling to preserve fine details such as text and illustrations. We propose a novel approach, which we call SIFT-VTON, that utilizes SIFT keypoint matching to provide explicit geometric guidance for diffusion-based virtual try-on. Our method applies domain-specific filtering to SIFT keypoint matches between garment and person images, then converts these correspondences into spatial probability distributions that supervise cross-attention layers during training. This explicit supervision guides the model to learn precise spatial alignment, concentrating attention on geometrically consistent garment regions. Experiments on the VITON-HD dataset demonstrate significant improvements on unpaired metrics while maintaining competitive paired reconstruction metrics. Qualitative comparisons show superior preservation of text clarity and pattern alignment. Attention visualizations confirm that our method produces sharply focused attention on relevant garment details. This work demonstrates that classical geometric correspondence methods can effectively enhance modern diffusion models for conditional synthesis tasks. The source code will be available at this https URL.

---


### 136. [Checkerboard: A Simple, Effective, Efficient and Learning-free Clean Label Backdoor Attack with Low Poisoning Budget](https://arxiv.org/abs/2605.01298)

**<font color=#1a73e8>作者：</font>** Yi Yang, Jinyang Huang, Binbin Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks threaten the deep learning supply chain by poisoning a small fraction of the training data so that a model behaves normally on clean inputs but misclassifies trigger-carrying inputs to an attacker-chosen target class. Clean-label backdoor attacks are especially dangerous because poisoned samples remain label-consistent and are therefore harder to detect. Yet existing clean-label attacks typically rely on expensive optimization, surrogate-model training, or nontrivial data access.
We present Checkerboard, a theoretically grounded, learning-free clean-label backdoor attack that is effective, efficient, and simple to implement. From a linear separability formulation, we derive a checkerboard trigger in closed form, removing the need for surrogate-model training and trigger optimization. For texture-rich datasets, we introduce Complexity-driven Sample Selection, which uses only target-class data to improve trigger-to-background contrast by selecting low-complexity images for poisoning. Across four benchmark datasets, Checkerboard outperforms 8 baseline attacks and achieves state-of-the-art performance under low poisoning budgets. For example, on CIFAR-10, under a trigger perturbation budget of $10/255$, poisoning 20 training samples achieves $99.99\%$ Attack Success Rate (ASR). On ImageNet-100, a poisoning rate of only $0.46\%$ yields over $94\%$ ASR without degrading clean accuracy. The proposed attack also remains effective against state-of-the-art backdoor defenses and shows strong resistance to adaptive defenses.

---


### 137. [From Stealthy Data Fabrication to Unsafe Driving: Realistic Scenario Attacks on Collaborative Perception](https://arxiv.org/abs/2605.01301)

**<font color=#1a73e8>作者：</font>** Qingzhao Zhang, Runting Zhang, Z. Morley Mao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Collaborative perception allows connected and autonomous vehicles (CAVs) to improve perception by sharing sensory data, but it also introduces security risks from manipulated inputs. Prior work shows that attackers can spoof or remove objects by fabricating shared data, yet the practicality of such attacks in real-world driving remains unclear. Existing attacks are often detectable or evaluated in manually constructed scenarios, leaving open whether they can induce safety-critical outcomes in dynamic environments. To bridge this gap, we present a stealthy, scenario-realistic data fabrication attack that induces unsafe driving behaviors through end-to-end system effects. Instead of creating large, easily detectable anomalies, our attack subtly manipulates the poses of existing objects in shared perception results, keeping perturbations below detection thresholds. These small errors are then propagated through downstream modules, including object tracking and trajectory prediction, leading to significant deviations in predicted behaviors and ultimately unsafe driving decisions. We further design an online, scenario-aware attack framework that adapts to dynamic traffic conditions and optimizes attack strategies at runtime. Experiments on OPV2V and V2X-Real demonstrate that the attack achieves over 90% success in inducing detection errors and triggers safety-critical behaviors, such as unnecessary hard braking, in up to 50% of scenarios, while largely evading state-of-the-art defenses. We also propose a mitigation that focuses on detecting anomalies in localized, safety-critical regions, achieving an 80% detection rate on the small pose perturbation compared to 11% for the best existing methods.

---


### 138. [CUE: Concept-Aware Multi-Label Expansion to Mitigate Concept Confusion in Long-Tailed Learning](https://arxiv.org/abs/2605.01309)

**<font color=#1a73e8>作者：</font>** Ruichi Zhang, Chikai Shang, Jiacheng Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed distributions are common in real-world recognition tasks, where a few head classes have many samples while most tail classes have very few. Recently, fine-tuning foundation models for long-tailed learning has gained attention due to their excellent performance. However, most existing methods focus solely on mitigating long-tailed distribution bias while overlooking concept confusion caused by the long-tailed distribution. In this paper, we study this problem and attribute it to the mutual exclusivity of single-label supervision under long-tailed distributions, which suppresses feature sharing among related classes and amplifies the dominance of head classes, leading to disrupted inter-class discriminability. To address this, we propose CUE, Concept-aware mUlti-label Expansion, which introduces multi-label concept signals to preserve disrupted inter-class relationships. Specifically, CUE constructs concept sets by (i) extracting instance-level visual cues from zero-shot CLIP and (ii) generating class-level semantic cues with LLM; the two cues are incorporated via separately weighted Binary Logit-Adjustment (BLA) auxiliary losses and jointly optimized with the baseline Logit-Adjustment (LA) loss. Experiments on several long-tailed benchmarks, CUE achieves balanced and strong performance, surpassing recent state-of-the-art methods. Code is available at: this https URL.

---


### 139. [Enhancing Game Review Sentiment Classification on Steam Platform with Attention-Based BiLSTM](https://arxiv.org/abs/2605.01315)

**<font color=#1a73e8>作者：</font>** Abit Ahmad Oktarian, Fadhil Fitra Wijaya, Dhafin Razaqa Luthfi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates sentiment classification of Steam game reviews using an attention-based Bidirectional Long Short-Term Memory (BiLSTM) model. Using a dataset of 50,000 reviews sampled from a larger Steam review corpus, the authors compare a traditional machine learning baseline based on TF-IDF and PyCaret AutoML with a deep learning approach implemented in PyTorch. The proposed BiLSTM+Attention model is trained with class-weighted cross-entropy to address class imbalance and achieves 83% accuracy and 85% weighted F1-score on the test set, with 90% recall for negative reviews. The paper also presents attention visualizations to show interpretability by highlighting sentiment-bearing words. The study concludes that the BiLSTM+Attention model is effective for analyzing user sentiment in Steam reviews and useful for helping developers understand player feedback.

---


### 140. [Sentiment Analysis of Mobile Legends App Reviews Using Machine Learning and LSTM-Based Deep Learning Models](https://arxiv.org/abs/2605.01317)

**<font color=#1a73e8>作者：</font>** Vira Putri Maharani, Kharisa Harvanny, Daris Samudra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper compares Machine Learning and LSTM-based Deep Learning methods for sentiment analysis of Mobile Legends app reviews. Using a dataset of 10,000 reviews labeled as positive, negative, and neutral, the study evaluates traditional models with TF-IDF and PyCaret AutoML and compares them against an LSTM model designed to capture sequential text dependencies. The results show that the LSTM model outperforms the classical Machine Learning baselines, achieving 92% accuracy and a weighted F1-score of 91%. The findings indicate that deep learning is more effective for handling informal and context-dependent user review text.

---


### 141. [PACE: Post-Causal Entropy Modeling for Learned LiDAR Point Cloud Compression](https://arxiv.org/abs/2605.01320)

**<font color=#1a73e8>作者：</font>** Jiahao Zhu, Kang You, Dandan Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR point cloud compression is vital for autonomous systems to handle massive data from high-resolution sensors. While learned entropy modeling built upon octree structures yields high compression gains, it faces two critical bottlenecks: 1) prohibitive latency, particularly during decoding, caused by causal, multi-stage context modeling; and 2) a rigid performance-latency trade-off, preventing a single model from adapting to varying constraints. These limitations stem from the tight coupling between context aggregation backbone and probability prediction. To address this, we propose PACE, a new framework that reformulates ancestral context aggregation as a non-causal backbone and confines causality to a lightweight, stage-scalable predictor, eliminating repetitive backbone executions and reducing computational overhead. The predictor supports an arbitrary number of prediction stages, supporting seamless adaptation across diverse performance-latency trade-offs without reloading parameters. Experiments demonstrate that PACE sets a new state-of-the-art in compression efficiency, achieving notable BD-BR savings and reducing decoding latency by over 90% in autoregressive mode, highly attractive for practical applications.

---


### 142. [Benchmarking LightGBM and BiLSTM for Sentiment Analysis on Indonesian E-Commerce Reviews](https://arxiv.org/abs/2605.01322)

**<font color=#1a73e8>作者：</font>** Lidia Natasyah Marpaung, Vania Claresta, Iqfina Haula Halika 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study presents a comparative analysis between two primary approaches in Natural Language Processing (NLP): Machine Learning (ML) utilizing the PyCaret AutoML framework, and Deep Learning (DL). The evaluation is conducted on a sentiment analysis task using an Indonesian e-commerce review dataset sourced from Hugging Face. The dataset, consisting of 15,000 samples, is partitioned into training, validation, and testing sets. The ML experiments compare LightGBM, Logistic Regression, and Support Vector Machine (SVM) algorithms, whereas the DL experiment implements a Bidirectional Long Short-Term Memory (BiLSTM) architecture. The experimental results demonstrate that the BiLSTM model outperforms all ML models, achieving an accuracy of 98.87\% and an F1-Score of 98.87\%. Meanwhile, LightGBM emerges as the best-performing ML model with an accuracy of 98.23\% in a highly efficient training time. This research proves that the BiLSTM architecture is highly capable of capturing the sequential context of Indonesian review texts, making it the superior model for this specific classification task.

---


### 143. [Creating and Evaluating Figurative Language Dataset for Sindhi](https://arxiv.org/abs/2605.01323)

**<font color=#1a73e8>作者：</font>** Wazir Ali, Adeeb Noor, Saifullah Tumrani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this article, we introduce SiNFluD, a novel benchmark dataset for Sindhi figurative language classification. We first collect raw text from various blogs, social media platforms, and literary sources, and subsequently prepare the corpus for annotation. Two native annotators label the data using the Doccano text annotation tool, achieving an inter-annotator agreement of 0.81. We then establish baseline results using 5-fold and 10-fold cross-validation. Finally, we evaluate mBERT, XLM-RoBERTa, and XLM-RoBERTa-XL models, along with SetFit for few-shot fine-tuning of sentence transformers. Among these, the pretrained XLM-RoBERTa-XL achieves the best performance.

---


### 144. [Segment-Aligned Policy Optimization for Multi-Modal Reasoning](https://arxiv.org/abs/2605.01327)

**<font color=#1a73e8>作者：</font>** Lei Gao, Zhuoming Li, Mengxi Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing reinforcement learning approaches for Large Language Models typically perform policy optimization at the granularity of individual tokens or entire response sequences. However, such formulations often misalign with the natural step-wise structure of reasoning processes, leading to suboptimal credit assignment and unstable training in multi-modal reasoning tasks. To bridge this gap, we propose Segment-Aligned Policy Optimization (SAPO), a novel reinforcement learning paradigm that treats coherent reasoning steps, rather than tokens or full sequences as fundamental units of policy update. SAPO introduces a step-wise Markov decision process abstraction over reasoning segments, accompanied by segment-level value estimation, advantage computation, and importance sampling mechanisms that are semantically aligned with reasoning boundaries. Experiments on representative reasoning benchmarks demonstrate that SAPO consistently outperforms token-level and sequence-level policy optimization methods, achieving significant accuracy improvements while exhibiting better training stability and value estimation consistency. Our work underscores the importance of aligning reinforcement learning updates with the intrinsic structure of reasoning, paving the way for more efficient and semantically grounded policy optimization in complex reasoning tasks. Codes and models will be released to ensure full reproducibility.

---


### 145. [Truth or Tribe: How In-group Favoritism Prioritize Facts in Persona Agents](https://arxiv.org/abs/2605.01329)

**<font color=#1a73e8>作者：</font>** Shijun Lei, Hongyu Wang, Yunji Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-group favoritism refers to the phenomena of favoring members of one's in-group over out-group members and is widely observed in numerous social cooperative behaviors. Recently, in-group favoritism biases have also been identified in generative language models. However, whether the in-group favoritism exists when persona agents are faced with contradicting information (e.g., misinformation), and how to mitigate the adverse effects of in-group favoritism biases in persona agents have been understudied. To address these problems, we propose a Truth or Tribe simulation framework to study the agent cooperation within the spread of contradicting information through a triadic interaction paradigm, and conduct controlled trials to evaluate the primary moderating factors. Extensive results showcase that persona agents display strong in-group favoritism, accepting incorrect answers from identity-similar peers at much higher rates than from dissimilar peers. In-group favoritism continues to emerge in defeasible reasoning contexts where no absolute truth exists, and it intensifies as cognitive complexity increases. Furthermore, three intervention strategies--Identity-Blind Instruction, Structured Counterfactual Reasoning, and Heterogeneous Perspective Ensemble--are proposed to mitigate the in-group favoritism.

---


### 146. [Zero-Shot Interpretable Image Steganalysis for Invertible Image Hiding](https://arxiv.org/abs/2605.01331)

**<font color=#1a73e8>作者：</font>** Hao Wang, Yiming Yao, Yaguang Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image steganalysis, which aims at detecting secret information concealed within images, has become a critical countermeasure for assessing the security of steganography methods, especially the emerging invertible image hiding approaches. However, prior studies merely classify input images into two categories (i.e., stego or cover) and typically conduct steganalysis under the constraint that training and testing data must follow similar distribution, thereby hindering their application in real-world scenarios. To overcome these shortcomings, we propose a novel interpretable image steganalysis framework tailored for invertible image hiding schemes under a challenging zero-shot setting. Specifically, we integrate image hiding, revealing, and steganalysis into a unified framework, endowing the steganalysis component with the capability to recover the secret information embedded in stego images. Additionally, we elaborate a simple yet effective residual augmentation strategy for generating stego images to further enhance the generalizability of the steganalyzer in cross-dataset and cross-architecture scenarios. Extensive experiments on benchmark datasets demonstrate that our proposed approach significantly outperforms the existing steganalysis techniques for invertible image hiding schemes.

---


### 147. [A Multi-View Media Profiling Suite: Resources, Evaluation, and Analysis](https://arxiv.org/abs/2605.01336)

**<font color=#1a73e8>作者：</font>** Muhammad Arslan Manzoor, Dilshod Azizov, Daniil Orel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> News outlets shape public opinion at a scale that makes automated detection of political bias and factuality essential. However, the field still lacks unified resources, comprehensive evaluations across diverse approaches, and systematic analyses of the representations and fusion strategies that matter most, especially under label sparsity and dataset diversity. In addition, there is little empirical work reporting broad, observation-driven findings about what consistently works, what fails, and why. We address these gaps through four main contributions. First, we introduce MBFC-2025, a large-scale label set covering approximately 2,600 outlets from Media Bias/Fact Check (MBFC). Second, we construct multiview representations for ACL-2020 (Panayotov et al., 2022), which includes around 900 outlets, as well as for MBFC-2025. These representations span Alexa graphs, hyperlink graphs, LLM-derived graphs, articles, and Wikipedia descriptions. Third, we provide a systematic evaluation and analysis of embedding views and fusion strategies, including a reinforcement learning-based fusion variant. Fourth, we conduct extensive experiments that achieve state-of-the-art results on ACL-2020 and establish strong benchmarks on MBFC-2025.

---


### 148. [Robust Parameter Learning for Uncertain MDPs](https://arxiv.org/abs/2605.01339)

**<font color=#1a73e8>作者：</font>** Yannik Schnitzer, Alessandro Abate, David Parker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-based approaches to verifying unknown Markov decision processes (MDPs) often employ uncertain MDPs. These models use, for example, confidence intervals to capture transition uncertainty and allow synthesis of policies that are robust to this uncertainty. However, this approach typically quantifies uncertainty independently for individual transition probabilities, ignoring dependencies due to shared latent quantities. We propose to learn such models using parametric MDPs (pMDPs), where transition probabilities are expressions over a set of parameters. We project statistical uncertainty from empirical transition frequencies onto the pMDP's parameter space, yielding a probably approximately correct (PAC) uncertainty model for the underlying MDP that respects the algebraic dependencies between transitions. The resulting models are algorithmically challenging to solve, so we propose a hierarchy of sound polytopic outer approximations of the induced confidence set. We implement and evaluate our approach, demonstrating substantially tighter uncertainty estimates than classical interval-based uncertain MDP learning techniques.

---


### 149. [CHASE: Competing Hypotheses for Ambiguity-Aware Selective Prediction](https://arxiv.org/abs/2605.01346)

**<font color=#1a73e8>作者：</font>** Kartik Jhawar, Yuhao Geng, Atul N. Parikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard selective prediction methods typically estimate uncertainty from the output of a single predictive branch. While effective for general uncertainty estimation, these approaches often struggle under partial observability, where local temporal evidence can be contradictory and standard confidence scores become misleading. We introduce CHASE (Competing Hypotheses for Ambiguity-Aware Selective Prediction), a selective prediction framework that explicitly compares structured temporal explanations to determine whether to commit to a decision or abstain. Because genuine ambiguity causes the score gap between competing hypotheses to collapse, CHASE optimizes a ranking-aware selector over these hypothesis margins to globally separate safe commitments from fundamentally uncertain ones. We evaluate this framework on the problem of hidden connectivity inference, utilizing a controlled, physically grounded simulator inspired by the dynamics of giant unilamellar vesicles (GUVs), alongside zero-shot qualitative transfer (without retraining or fine tuning) to representative real GUV videos. Our experiments demonstrate that explicitly reasoning over competing hypotheses provides a superior balance of metrics. Compared to canonical uncertainty baselines, CHASE achieves statistically significant gains in overall no-abstain accuracy, three-way accuracy, and overall ambiguity-aligned abstention (at 80% coverage). Specifically, it yields up to an 11.0% relative mean improvement in overall alignment, alongside up to an 8.8% relative boost in three-way accuracy in the very-high ambiguity regime. By maintaining a selective risk boundary strictly at par with the best baselines at 80% coverage, and reducing overall risk by 9.9% at 90% coverage, this framework offers a more reliable approach to decision-making under structured ambiguity.

---


### 150. [MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/abs/2605.01347)

**<font color=#1a73e8>作者：</font>** Jianze Wang, Ying Liu, Jinlong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own trajectories under token-level teacher supervision, but existing methods are capped by a single-teacher capability ceiling: when the teacher errs, the student inherits the error. OPD also remains largely unexplored in agentic tasks, where per-step errors compound across long trajectories and destabilize training. We propose MAD-OPD (Multi-Agent Debate-driven On-Policy Distillation), which breaks this ceiling by recasting the distillation teacher as a deliberative collective of teachers that debate over the student's on-policy state; the debate produces an emergent collective intelligence that supplies token-level supervision, with each teacher's contribution weighted by its post-debate confidence. To extend OPD to agentic tasks, we also introduce On-Policy Agentic Distillation (OPAD), which adds step-level sampling to stabilize training under multi-step error compounding. We additionally derive a task-adaptive divergence principle, selecting JSD (Jensen-Shannon divergence) for agentic stability and reverse KL (Kullback-Leibler) divergence for code generation, and verify it both theoretically and empirically. Across six teacher-student configurations (Qwen3 and Qwen3.5; 1.7B-14B students, 8B-32B teachers) and five agentic and code benchmarks, MAD-OPD ranks first across all six configurations; on the 14B+8B$\to$4B setting it lifts the agentic average by $+2.4\%$ and the code average by $+3.7\%$ over the stronger single-teacher OPD.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
