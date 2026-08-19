# 📦 其他研究 | 2026年08月20日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-173](./part-04.md)

---

### 101. [SoK: Cross-Chain Transaction Identification and Matching](https://arxiv.org/abs/2608.17532)

**<font color=#1a73e8>作者：</font>** Hang Zheng, Qishuang Fu, Joseph Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-chain bridges, instant cryptocurrency exchanges, and centralized cross-ledger platforms move assets across an increasingly multi-chain ecosystem. However, these systems have repeatedly become targets of high-value attacks and channels for cross-chain money laundering. Cross-chain transactions are substantially harder to analyze than single-chain transactions: no single ledger records an entire cross-chain transfer, its evidence is scattered across the source chain, the destination chain, and off-chain systems, and the availability and reliability of that evidence vary widely across systems. In this paper, we present a systematization of knowledge (SoK) on cross-chain transaction identification and matching. First, we classify deposit and withdrawal identification methods into four approaches and transaction matching methods into three mechanisms: deterministic identifier matching, field-constraint heuristics, and model-assisted matching. We find that their applicability and reported performance are shaped mainly by the evidence the underlying system exposes, and we further examine how matched pairs support downstream attack detection and fund tracing. Second, we assess the availability of existing datasets and artifacts, finding that fewer than half remain obtainable, and distill three artifact failure modes. Finally, we outline four open challenges toward auditable, reproducible, and actionable cross-chain analysis.

---


### 102. [TENET: Telegram Mini App (in)security](https://arxiv.org/abs/2608.17538)

**<font color=#1a73e8>作者：</font>** Andrea Ciccotelli, Federico Zappone, Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Telegram, with over 450 million daily active users, has introduced Mini Apps---web-based applications running directly within its client. However, this integration introduces notable security risks. As we demonstrate, many Mini Apps store authentication materials---such as session tokens and wallet mnemonic phrases---in plaintext on client devices, exposing users to unauthorized access, impersonation, and financial exploitation. While insecure client-side storage is a known risk in web applications, the Telegram Mini App ecosystem presents a uniquely dangerous combination of factors absent from prior work: no platform-level security review, no storage access restrictions, a financially motivated user base handling live cryptocurrency assets, and a WebView environment that offers weaker protections than standalone browsers. To investigate this threat, we present TENET, a purpose-built auditing tool whose design decisions---pattern selection, entropy thresholds, and charset validation---are grounded in the structural properties of the secrets targeted and empirically validated against a ground-truth dataset. We screened 61 Mini Apps using a stratified, popularity-weighted sampling strategy based on popularity. Of the 37 applications that met our processing criteria and were analyzed, 30 exhibited security flaws, which we classify into three severity tiers: plaintext storage, recoverable encryption, and replayable tokens. Notably, even Telegram's official Wallet exhibits a severe vulnerability that may lead to full account compromise. Following our responsible disclosure, Telegram implemented two new secure-storage APIs, and our post-remediation verification confirmed that its official Wallet no longer exposes the recovery mnemonic in plaintext. Finally, we propose mitigation measures and best practices for both Telegram platform developers and third-party Mini App creators.

---


### 103. [Software Defined Networks Key Relay for Large-Scale Quantum Key Distribution Networks](https://arxiv.org/abs/2608.17539)

**<font color=#1a73e8>作者：</font>** Stephan Laschet, Gergely Lendvay, Thomas Lorünser 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This work addresses the orchestration of large-scale Quantum Key Distribution Networks (QKDNs) using Software Defined Networking (SDN). Building on ETSI and ITU specifications, common best practices and architectures are outlined. The main task of the SDN Controller is to aggregate technical key performance indicators (KPI) from the network and, based on these, select the optimal path. Multiple path selection algorithms, based on Dijkstra or a maximum-minimum capacity algorithm, with built-in load balancing are presented. The algorithms were tested in simulations and their performances, and tradeoffs, are discussed. Additional critical aspects related to SDN controlled QKDNs are discussed, such as query batching, multi-path selection and group key capabilities. An oblivious multi-party protocol is proposed for relay path selection in a multi-domain scenario, so providers don't have to disclose sensitive information about their QKDN. These contributions aim to enhance scalability, resilience and interoperability in quantum-secure network infrastructures.

---


### 104. [No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models](https://arxiv.org/abs/2608.17542)

**<font color=#1a73e8>作者：</font>** Jack Boylan, Chris Hokamp  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future embeddings, but the objective admits a trivial solution of a constant encoder, so every practical system adds an anti-collapse mechanism (LeCun, 2022; Assran et al., 2023; Bardes et al., 2022; 2024). LeWorldModel (LeWM) prevents collapse with SIGReg, a regularizer that forces the latent distribution to match an isotropic Gaussian: the representation is stabilized by prescribing what it must look like, independently of the environment it models. We argue that the anti-collapse pressure can instead come from the transition data itself. Action-Contrastive Masked Transition Modeling (AC-MTM) keeps LeWM's forward latent-prediction objective and adds a training-only inverse-dynamics head trained with Action-NCE: each latent transition must identify the action that produced it among the other actions in the batch, a discrimination task that a collapsed encoder provably fails. The inverse branch is discarded after training, leaving test-time encoding, forward prediction, planning, and compute identical to LeWM. On four standard pixel-control tasks under a matched planning protocol, AC-MTM trains stably from scratch and matches SIGReg on average. On the harder multi-object OGBench Visual Scene task, results are consistent with the prescribed geometry becoming a bottleneck: AC-MTM reaches 80.0$\pm$2.0% success versus 58.0$\pm$2.0% for SIGReg, improving by 20-24 points in each training seed. A single 50-episode random-policy run gives a 52% baseline estimate. Contrastive inverse dynamics thus provides a distribution-free anti-collapse signal that requires no target network, stop-gradient, pretrained encoder, or reconstruction objective, and we characterize the action-space and observability assumptions under which it holds. We make our code available at this https URL

---


### 105. [MSEditor: Toward Consistent Multi-Shot Video Editing](https://arxiv.org/abs/2608.17559)

**<font color=#1a73e8>作者：</font>** Kunyu Feng, Yue Ma, Bingyuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we tackle the problem of performing consistent, unified modifications to a multi-shot video sequence. This task is particularly challenging because multi-shot videos consist of discontinuous temporal segments that vary significantly in viewpoint, camera scale, and subject pose, leading to severe identity drift and cumulative error propagation. Achieving coherent edits requires establishing reliable cross-shot semantic awareness to maintain stable subject appearance and visual continuity across these disjointed boundaries. To address this, we propose MSEditor, the first framework designed specifically for consistent multi-shot video editing. To overcome the scarcity of high-quality multi-shot training data, we repurpose existing multi-view video datasets to provide robust cross-shot supervision. Architecturally, we introduce a Supervisory Adapter that injects this cross-shot information into the diffusion backbone, enabling the model to learn identity-consistent representations. Furthermore, to effectively mitigate cumulative errors and ensure long-range temporal coherence, we design a Cross-Shot Packing strategy that dynamically aggregates information from semantically related shots within the self-attention window. Extensive experiments demonstrate that MSEditor significantly outperforms existing methods on our curated multi-shot video editing benchmark in terms of identity preservation, temporal stability, and overall visual quality.

---


### 106. [Leveraging existing sparse point annotations for benthic imagery dense segmentation](https://arxiv.org/abs/2608.17561)

**<font color=#1a73e8>作者：</font>** Cesar Borja, Breck A. McCollum, Jarret E. Byrnes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The health of marine ecosystems is a critical indicator of global environmental change, yet the physical constraints of underwater observation and the intrinsic challenges of processing marine imagery severely limit the scalability of systematic monitoring. While recent visual foundation models such as the Segment Anything Model (SAM) series show great promise, they still struggle with the fine-grained recognition required in these complex scenarios and still require expert supervision. Our work addresses this gap by bridging state-of-the-art foundation models with existing sparse supervision. Because historical benthic surveys are typically annotated with only a few sparse expert points per image, we utilize these legacy point-labels as visual prompts for SAM2. Our primary contribution is a novel mechanism to automatically identify which of these points are suitable, and which are actively harmful, when used for propagation. By filtering out unreliable points, we extract high-quality pseudo-ground-truth masks capable of training more accurate, fine-grained semantic segmentation models. We demonstrate the effectiveness of our approach on public benthic data and introduce a new, challenging benchmark featuring real-world sparse expert annotations, paving the way for scalable ecological analysis.

---


### 107. [Where a New Concept Must Enter: Entry Point Gates Cross-Task Usability in Unified Multimodal Models](https://arxiv.org/abs/2608.17564)

**<font color=#1a73e8>作者：</font>** Zongyang Qiu, Yihan Wu, Kaixuan Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) are motivated by the hope that understanding and generation reinforce each other but controlled ablations repeatedly find that adding a generation objective leaves understanding flat. Joint-training studies cannot settle the disagreement: with overlapping supervision, a gain cannot be attributed to the architecture rather than the data. To further investigate the relationship between the two directions in UMMs, we separate them by construction. A novel visual entity, a rendered 3D asset paired with a pseudo-word screened for absence from the frozen model's behavior, is bound through exactly one task direction, and the untrained direction is then measured. We find that the channel is real in both directions, but the directions differ in kind: generation training installs a name the model can only match among candidates; understanding training installs one it can also produce. What governs cross-task usability is where the binding enters the shared computation. An alignment probe predicts export across 36 configurations (Spearman $\rho = +0.68$). That objective's alignment term, maximized in closed form over activations with every weight frozen, makes a concept drawable when injected at layer 7 of 28 and is indistinguishable from the base model from layer 14 on, while the weight-based version of the same edit peaks at layers 10-14. In an observational series of four models, this window appears only where the understanding pathway is a semantic vision encoder, suggesting that unified weights are not enough: the two directions must share a semantic format at the entry point. Exploiting the rule, a mid-stack alignment objective acquires the concept for a $0.1\%$ relative loss of the model's general text-to-image ability, against $41\%$ for the standard generative route. Our code is at this https URL.

---


### 108. [SpurCon: Weighted Supervised Contrastive Learning for Mitigating Spurious Cues in Medical Imaging](https://arxiv.org/abs/2608.17598)

**<font color=#1a73e8>作者：</font>** Shenhav Nadir, Meir Yossef Levi, Eyal Gofer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite the rapid progress of deep neural networks in visual recognition, their adoption in high-risk medical applications remains limited due to reliability and robustness concerns. Models may exploit spurious correlations, particularly in medical imaging, where devices or treatment artifacts often co-occur with pathology. In small or imbalanced datasets, such cues further reduce worst-group performance and undermine clinical trust. To solve these issues, two major challenges should be addressed: identifying dataset-specific spurious cues, which typically require domain knowledge, and mitigating reliance on them. To tackle both, we propose SpurCon, a lightweight framework based on a novel supervised contrastive loss formulation that leverages available metadata and predicted spurious labels to enhance robustness. We introduce a fast few-shot procedure, without network training, to estimate spurious labels using a small number of expert-annotated samples. We then propose a weighted supervised contrastive objective, WtSupCon, that reshapes the representation geometry by assigning sample-specific weights that depend on the [pathology, spurious, metadata] combination. For example, the highest weight is assigned to samples that differ only in their spurious label. This yields highly similar representations for images with the same metadata and pathology, differing only in the predicted spurious label. Our method operates on pretrained image encoders (such as BiomedCLIP) and trains only a lightweight projection head. We evaluate SpurCon on a synthetic setting and on Waterbirds, CheXpert, a chest X-ray classification dataset, and ISIC 2020, a skin cancer classification dataset. Our approach delivers the best spurious-mitigation performance, balancing well worst-group and overall accuracy on multiple datasets.

---


### 109. [Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges](https://arxiv.org/abs/2608.17605)

**<font color=#1a73e8>作者：</font>** Syeda Faiza Ahmed, Zien Sheikh Ali, Hunzalah Hassan Bhatti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational AI is moving beyond isolated text prompts toward sustained, multimodal interaction. In real conversations, users clarify goals, revise requests, interrupt responses, switch topics, and introduce new evidence while expecting systems to preserve context across turns. This makes multi-turn dialogue a distinct challenge requiring systems to maintain and update memory, ground responses across modalities, tools, and external knowledge, and adapt across languages and cultures. This study reviews multi-turn conversational AI across text-only dialogue, AudioLLMs and speech-native systems, multimodal and omni-modal systems, and tool-augmented agents. We organize the literature around datasets and benchmarks, modeling paradigms, training strategies, evaluation setups, and cross-cutting challenges. Our analysis shows that support for multiple modalities has advanced faster than the ability to sustain coherent interaction across a session. Despite stronger capabilities to perceive, speak, and act across modalities, current systems still struggle with persistent memory, cross-turn grounding, full-duplex interaction, robust evaluation, and cultural alignment. We conclude with a research agenda for systems that can remember, revise, ground, speak, listen, act, and adapt across turns, modalities, and cultures. (this https URL)

---


### 110. [Adaptive Incentive Design in Dynamic Principal-Agent Problem via Kernelized Bandits](https://arxiv.org/abs/2608.17614)

**<font color=#1a73e8>作者：</font>** Arghya Mallick, Anuj S. Vora, Sergio Grammatico 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We consider the dynamic principal-agent problem under asymmetric information, wherein a principal sequentially designs contracts to incentivize an agent with unknown preferences and hidden actions. A fundamental bottleneck in the existing literature is the assumption of deterministic agent utility, which renders the principal's expected utility discontinuous and forces computationally intractable discretizations of the contract space. In this paper, we address this limitation by introducing a stochastic counterpart into the agent's utility model, capturing the inherent physical and behavioral variations in realistic subsystems. We formally prove that this stochastic formulation restores the continuity of the principal's expected utility. Leveraging this continuous geometric structure, we formulate the interaction as a structured multi-armed bandit problem subject to heteroscedastic noise. We propose a \texttt{Heteroscedastic GP-UCB} algorithm that utilizes a Neural Network (Arcsin) kernel, chosen to capture the non-stationary, sigmoidal geometry of the utility landscape. For an $m$-dimensional compact contract space, we establish a high-probability cumulative regret bound of $O\left(\sqrt{T}(\log T)^{m+1}\right)$. Finally, we demonstrate the practical efficacy of our theoretical framework by formulating the Vehicle-to-Grid (V2G) incentive design problem, proving its equivalence to a dynamic principal-agent problem, and showing superior economic performance for grid aggregators.

---


### 111. [MoNe: Modular Neural Memory for Efficient Long Context Inference](https://arxiv.org/abs/2608.17616)

**<font color=#1a73e8>作者：</font>** Wonguk Cho, Kyubyung Chae, Tribhuvanesh Orekondy 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present MoNe, a lightweight modular neural memory that attaches to any frozen pretrained Transformer to enable long-context inference without retraining. MoNe reads context in fixed-size segments via test-time learning of fast-weight neural memory networks with layer-localized gradient updates; at inference, the memory generates keys and values from the query tokens alone, with no context tokens re-read. This two-phase design decouples inference cost from context length, achieving $O(N)$ preprocessing and $O(1)$ query cost with peak GPU memory that does not grow with $N$. At 128K tokens, MoNe reduces both compute and peak GPU memory by approximately 80% compared to ICL with only 6.4% parameter overhead. MoNe generalizes to context lengths far beyond the backbone's native window, achieving strong performance on needle-in-a-haystack and word extraction benchmarks from RULER, where ICL degrades sharply.

---


### 112. [OOD Detection for EEG-based Machine Learning in High-Risk Environments](https://arxiv.org/abs/2608.17620)

**<font color=#1a73e8>作者：</font>** Philipp Bomatter, Henry Gouk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for electroencephalography (EEG) analysis show great promise across a wide range of applications, but their deployment in high-risk domains is hindered by their vulnerability to distribution shifts. Encountering out-of-distribution (OOD) data can lead to catastrophic, overconfident predictive failures. While OOD detection methods can mitigate these risks, they remain heavily under-explored for EEG. Moreover, evaluations in the broader literature typically evaluate OOD detection performance in isolation, ignoring their practical impact on downstream applications. To bridge this gap, we introduce a benchmark for EEG OOD detection, evaluate a broad range of methods, and furthermore evaluate their value in two clinical downstream prediction task. Our results disentangle OOD detection and model uncertainty estimation capabilities, which are frequently conflated in the literature, provide actionable insights about the current state of the art for EEG OOD detection and model uncertainty estimation, and demonstrate how complementary methods for both aspects can be combined to form a robust safety net for the deployment of EEG-based machine learning models in real-world applications.

---


### 113. [RetiWave-Mamba: A Dual-Stream Network for Retinal Disease Detection based on Multi-scale Context and Frequency-Adaptive Mamba Projection](https://arxiv.org/abs/2608.17623)

**<font color=#1a73e8>作者：</font>** Cheng Cheng, Jin Hong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal diseases are a leading cause of irreversible vision impairment, making early and accurate diagnosis essential for effective treatment. Optical Coherence Tomography (OCT) serves as a critical imaging modality for this purpose, yet its automated analysis is hindered by inherent speckle noise, varying lesion scales, and subtle inter-class similarities. To address these challenges, we propose a novel framework, RetiWave-Mamba, which integrates spatial-frequency domain learning with state-of-the-art state space models. The framework utilizes Discrete Wavelet Transform (DWT) to decompose OCT images into low- and high-frequency streams, enabling decoupled processing of structural context and fine-grained details. For the low-frequency branch, we design a Multi-scale Contextual Localization Module (MCLM), which synergizes multi-scale dilation with spatial attention to expand the global receptive field and precisely localize lesion regions. For the high-frequency branch, we introduce an Attention-Guided High-Resolution Network (AG-HRNet) equipped with an intelligent gating mechanism to suppress noise propagation during multi-scale interactions. Furthermore, a Frequency-Adaptive Mamba Projector (FAMP) is incorporated to capture long-range dependencies within disjoint high-frequency textural features. Extensive experiments on the OCT-C8 dataset demonstrate that our approach achieves a state-of-the-art (SOTA) classification accuracy of 98.25%, surpassing existing methods. These results highlight the efficacy of RetiWave-Mamba in robustly identifying retinal pathologies under noisy conditions, offering a promising tool for clinical diagnosis.

---


### 114. [Validated Adaptation for Aerial Crowd Monitoring at Mass Gathering Scale: A Deployment Protocol, a Severity Law, and a Diagnostic for Label-Free Drone Crowd Counting, Toward the FIFA World Cup 2034 (Saudi Arabia)](https://arxiv.org/abs/2608.17625)

**<font color=#1a73e8>作者：</font>** AlAnoud AllGhayth, AlJawharh AlOtaibi, Jude AlSubaie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Saudi Arabia will host the 2034 FIFA World Cup and already operates crowd management at Hajj scale. Drone-based counting must hold accuracy on footage unlike anything in its training corpus, without labels, and must warn of dangerous inflow before a crush forms. We deliver a validated answer built on 525 controlled runs, a full-resolution corpus study, five falsification ablations, and a five-condition safety-interlock evaluation. Label-free adaptation recovers 31-49% of shift-induced error across four corruptions and five severities, with the strongest method gaining 41.8 MAE over the frozen source (95% CI [34.1, 49.6], p=7.5x10^-10, d=2.52). We establish a severity law separating methods with a constant absolute margin from the one whose margin grows, and a stability budget identifying which configuration is safe to fly. On a full-resolution corpus carrying a genuine +48 MAE aerial gap (source retrained to 14.6 validation MAE, a 34% improvement), adaptation repairs the dense-scene undercounting that would otherwise under-report a forming crush, and the flux-based risk module fires on real congestion episodes in 2 of 6 full-length clips. We localise the recoverable error: in a regime built to favor a physics-informed conservation prior (300-frame clips at 200ms spacing, five times wider than standard), the adaptation signal is normalisation-driven, not flow-driven; the continuity residual is invariant to the proportional counting errors domain shift produces, confirmed by four on/off ablations correlated at r=0.999 and a 40% input corruption moving accuracy by only 0.05 MAE. A label-free shift gate shows shift magnitude and accuracy damage are rank-independent (Spearman rho=0.20; rho=-0.60 among genuine shifts), quantifying the 58% of headroom a magnitude gate forgoes. We establish unconditional adaptation with tail monitoring as policy, closing with a six-point protocol.

---


### 115. [Graph Surgery and the Do-Operator: A Precise Correspondence for Acyclic Structural Causal Models](https://arxiv.org/abs/2608.17634)

**<font color=#1a73e8>作者：</font>** Satpreet Makhija  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The $\operatorname{do}$-operator is described graphically by deleting arrows into its targets and functionally by replacing their mechanisms with constants. To call these operations equivalent is not yet a mathematical statement: one returns a graph and remembers only the targets, whereas the other returns mechanisms and also remembers the imposed values. We make a dependency-level comparison precise for deterministic acyclic structural causal models with finitely many endogenous variables. If $\operatorname{Graph}(F)$ extracts the dependencies of a mechanism family $F$, our main theorem is $\operatorname{Graph}(F^\iota)=\operatorname{Surg}(\operatorname{Graph}(F),T_\iota)$. Thus replacing target mechanisms removes exactly the dependencies removed by graph surgery. For a model $M=(G,F)$ whose graph may contain unused arrows, we characterize when the same equality holds with $G$ in place of $\operatorname{Graph}(F)$; it holds for every intervention exactly when $G$ records the dependencies of $F$ exactly. We then define the intervened model, characterize its run, show how sequential interventions combine, and prove that an outcome depends only on interventions at its actual dependency ancestors.

---


### 116. [MaLViL: Multi-axis Low-rank Vision-LSTM for Medical Image Segmentation](https://arxiv.org/abs/2608.17635)

**<font color=#1a73e8>作者：</font>** Afshin Bozorgpour, Sina Ghorbani Kolahi, Moein Heidari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-LSTM (ViL) enables efficient global modeling, but its cost still scales with the number of spatial tokens, so existing segmenters confine ViL to a coarse bottleneck and lose fine anatomical detail. Rasterizing 2D features into a 1D sequence further breaks adjacency across the orthogonal scan axis. We propose MaLViL, a Multi-axis Low-rank Vision-LSTM network that extends ViL across decoder resolutions. Bidirectional low-rank ViL (Bi-LRViL) reasons on a compact orthonormal subspace and preserves detail through an orthogonal residual; scale-aware SaLViL restores cross-axis neighbors before serialization; and a Cross-Directional Mixer (CDM) fuses orthogonal horizontal and vertical traversal paths. Statistics-Guided Skip Modulation (SGSM) further retains boundary cues in encoder skips. On skin-lesion, ultrasound, and multi-organ CT benchmarks, MaLViL achieves competitive or state-of-the-art segmentation accuracy, while reducing ViL operator memory by up to $83\times$ at fine decoder resolutions. Code is available at: this https URL.

---


### 117. [rl-triton: High-Performance Triton GPU Kernels for Reinforcement Learning Credit Assignment](https://arxiv.org/abs/2608.17641)

**<font color=#1a73e8>作者：</font>** Lars Simon Zehnder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present rl-triton, an open-source library of high-performance GPU kernels for reinforcement learning credit assignment, implemented in Triton. The core contribution is a unified associative scan framework that recasts seven distinct RL estimation algorithms - Generalized Advantage Estimation (GAE), V-Trace, Retrace($\lambda$), TD($\lambda$) returns, discounted returns, eligibility traces, and episodic prefix sums - as instances of a single first-order linear recurrence solved in $O(\log T)$ parallel steps. All algorithms share the same associative scan operator, with algorithm-specific fused Triton kernels constructing their recurrence coefficients on-chip. We verify the associative operator algebraically and define the treatment of terminated and truncated episodes explicitly. Benchmarks show a 1.6-5.70$\times$ full-call speedup over a vectorized this http URL baseline in the massively parallel simulation regime (thousands of environments, short rollouts). The reported range covers all seven algorithms on both GPUs, both with and without per-step truncation handling. For most algorithms, speedups increase at longer sequence lengths, as the baseline requires more scan stages as $\log T$ grows, each adding an intermediate HBM round-trip. The library is available at this https URL.

---


### 118. [Elimination Geometry](https://arxiv.org/abs/2608.17646)

**<font color=#1a73e8>作者：</font>** Mian Huang, Xueqin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This monograph develops elimination geometry (EG), a typed, native-loss, audit-oriented framework for studying when locally optimal objects can be realized by a shared deployment rule. Elimination and compression may erase distinctions required by prediction, inference, control, or representation. EG asks which distinctions are lost, whether the induced defect is visible to the declared task, and whether changing information, architecture, action space, or deployment domain can repair it. EG separates local solvability, global realizability, and finite-sample certifiability. It derives native defects from the original objective and distinguishes architecture obstruction from model approximation, generalization, and implementation error. The monograph synthesizes tools from geometry, optimization, information theory, statistics, and machine learning into interfaces for integrability, representation admissibility, resource constraints, observational overlap, and common deployment. Formal results address regular, coordination, singular, compositional, and resource-limited mechanisms with explicit antecedents and claim boundaries. Applications include sparse model selection, distribution-free prediction, observational treatment policies, routed expert and retrieval systems, and learned score fields. Obstruction-Aware Learning and Inference links structural diagnosis to finite-data authorization, mechanism-matched intervention, and independent validation. Reproducible synthetic and real-data studies illustrate how certificates can guide architecture repair while recording failed gates and unresolved cases. The framework requires the deployment contract, native endpoint, competing explanations, information and compute budgets, and validation rule to be fixed before a persistent performance floor is attributed to architecture.

---


### 119. [An Emulation Anchored Digital Twin Testbed for Cyberattack and Defense Analysis in Hospital IT OT Environments](https://arxiv.org/abs/2608.17650)

**<font color=#1a73e8>作者：</font>** Prashant Rawat, Ravi Kumar Bairagi, Arunima 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern hospitals increasingly rely on integrated Information Technology (IT) and Operational Technology (OT) infrastructures to support critical healthcare services. However, this convergence expands the cybersecurity attack surface and makes safe validation of defensive mechanisms difficult on live systems. Existing testbeds often focus on isolated IT or OT environments and do not capture realistic cross-domain healthcare interactions. This work presents a hospital IT and OT cybersecurity testbed coupled with a digital twin for monitoring, experimentation, and validation of countermeasures. The testbed emulates a central server, Electronic Health Record (EHR) systems, SCADA-based infrastructure, and segmented IT, OT, and DMZ networks. It supports controlled cyberattack execution, software-patch evaluation, and training of RL-based defense agents. The testbed is further extended to a digital twin that models the real-time state of the environment using log and network statistics and enables bidirectional interaction through command execution and container lifecycle orchestration. Modbus/TCP and FHIR/HL7 support realistic communication across healthcare and industrial components. Experimental evaluation shows low computation overhead, with average normalized CPU utilization below 0.4 % per container and most lightweight services operating below 0.01%. OpenPLC Modbus TCP operations achieve a median round-trip latency of 0.901 ms. The testbed also captures a multi-stage SSH-based attack propagating from the DMZ to the IT and PLC networks. The framework provides a foundation for extending the emulated environment toward a hardware-enabled hospital digital twin.

---


### 120. [Denoised Variance-Based Pruning with Optimal Brain Bias Compensation](https://arxiv.org/abs/2608.17657)

**<font color=#1a73e8>作者：</font>** Geon Tack Lee, Jaegul Choo, Kang Eun Jeon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve state-of-the-art performance but carry massive computational overhead that restricts edge deployment. Although structural pruning has emerged as a key strategy to reduce these costs, existing methods often suffer from severe accuracy degradation or require expensive retraining. Recently, Variance-Based Pruning (VBP) introduced a promising paradigm by selecting neurons based on activation variance; however, it remains limited by statistical noise in finite-sample activation covariance and reliance on bias-only updates that cannot fully account for structural reconstruction error. To address these limitations, we introduce Denoised Variance-Based Pruning with Optimal Brain Bias Compensation (DVBP + OB$^2$C). We leverage random matrix theory to filter noise from the activation covariance spectrum for robust neuron selection and mathematically prove that integrating mean-shift compensation into the Optimal Brain Compression objective reduces the layer-wise Hessian exactly to the activation covariance matrix. This enables an optimal, closed-form update of the remaining weights using the same statistics gathered for selection. Extensive experiments on DeiT, Swin, and ConvNeXt architectures demonstrate that DVBP + OB$^2$C achieves state-of-the-art training-free performance; at 50% MLP pruning, it retains over 90% of the original Top-1 accuracy on Small and Base variants, outperforming VBP by up to 29.46% (ConvNeXt-T) and 7.33% (Swin-S). The code is available at: this https URL.

---


### 121. [Is Haar Enough? Exploring Symlets and Coiflets for Wavelet Convolution Layers](https://arxiv.org/abs/2608.17662)

**<font color=#1a73e8>作者：</font>** Md Rifat Ur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wavelet convolution layers have recently emerged as an efficient mechanism for enlarging receptive fields through multiresolution analysis, but prior work has fixed the wavelet basis to Haar or Daubechies at a chosen decomposition depth, leaving open whether a different basis can shift the underlying efficiency frontier. We identify and characterize a previously unexplored trade-off in this setting: bases with stronger approximation properties (longer filters) can reduce the decomposition depth required for competitive accuracy, yielding a net reduction in parameters and FLOPs despite higher perlevel transform cost. We formalize this as an F-vs.-L tradeoff (filter length vs. decomposition levels) and study it systematically across Haar, Daubechies, Symlets, and Coiflets under controlled architectures and budgets. On image classification (CIFAR-10, ImageNet-1K) and semantic segmentation (Cityscapes), Coiflet-based wavelet convolutions match Haar at deeper levels with approximately 32% fewer additional parameters and 33% fewer additional FLOPs, providing a concrete and actionable design choice for practitioners building wavelet-based architectures.

---


### 122. [Picard Proximal Monte Carlo for Parallel Bayesian Imaging with Score-Based Generative Priors](https://arxiv.org/abs/2608.17666)

**<font color=#1a73e8>作者：</font>** Deliang Wei, Evan Bell, Wenhan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian imaging inverse problems often require sampling from high-dimensional posterior distributions. While recent score-based and diffusion models provide expressive Bayesian priors, their sampling procedures remain inherently sequential and computationally expensive for large-scale imaging applications. We propose PiX-MC, a time-parallel posterior sampling framework based on proximal Langevin dynamics and Picard iteration. The proximal-likelihood formulation exploits the fact that many imaging likelihoods admit efficient, problem-specific proximal operators, while Picard refinement exposes parallelism across discretization nodes and naturally supports multi-GPU implementation. To further improve practical scalability and sampling performance, we develop multi-block and annealed variants of the proposed framework. We establish convergence guarantees under transparent assumptions, accommodating non-log-concave posteriors, imperfect learned score models, multi-block implementations, and annealing schedules. Experiments on a diverse collection of imaging inverse problems demonstrate that PiX-MC substantially reduces wall-clock time while preserving reconstruction quality. On a $512\times512\times80$ sparse-view computed tomography (CT) problem, annealed multi-block PiX-MC achieves up to a $50\times$ runtime speedup over the standard Langevin sampler using eight GPUs.

---


### 123. [Conformal Prediction for Molecular Properties under Label Shift](https://arxiv.org/abs/2608.17678)

**<font color=#1a73e8>作者：</font>** Hyeonsu Lee, Juyeon Kim, Erkhembayar Jadamba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug discovery and development underpins healthcare but remains costly and failure-prone. A critical bottleneck lies in predicting molecular properties such as solubility, potency, and toxicity, which directly determine whether a candidate can advance from preclinical to clinical trials. Artificial Intelligence (AI) has accelerated this process, yet its reliability is often undermined by distribution shift, as experimental conditions frequently diverge from training data. In addition, conventional point predictions provide only single-value estimates, offering limited guidance for high-stakes experimental design. We address these challenges with a conformal prediction framework tailored to label shift. By weighting conformal scores using marginal label probability ratios, our method produces statistically rigorous prediction intervals without retraining. This enables robust uncertainty quantification even when property distributions drift, directly tackling one of the most pervasive obstacles to applying AI in real-world drug development. By moving beyond accuracy alone to provide actionable confidence measures, our approach enhances the trustworthiness of AI-driven predictions. This further aligns predictive modeling with regulatory demands for transparency and uncertainty reporting and ultimately supports more reliable decision-making in billion-dollar development pipelines.

---


### 124. [Differentiable Voronoi Ray Tracing Beyond Rasterization Speeds](https://arxiv.org/abs/2608.17682)

**<font color=#1a73e8>作者：</font>** Bernardo Taveira, Carl Lindström, Joakim Johnander 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time novel view synthesis is dominated by rasterized explicit primitives. These projection-based pipelines provide high throughput but require specialized extensions for non-pinhole effects such as distortion, rolling shutter, and depth of field. Ray-based rendering expresses these effects naturally but is generally assumed too slow for competitive real-time rendering. We analyze the factors governing throughput in differentiable Voronoi ray tracing and identify traversal length, per-cell work, and memory locality as principal determinants. Guided by this, we introduce VoroTracing, which co-designs the scene representation, optimization, and GPU execution to reduce these costs. Compact octahedral appearance textures reduce memory traffic, while surface-concentrated opacity promotes early termination. The fixed-budget representation is optimized without pruning or densification and rendered with a GPU implementation designed for coherent traversal. On Mip-NeRF 360, VoroTracing renders at 623 FPS on an RTX 5090, providing $3.2\times$ the throughput of the fastest prior ray-based method and $2.8\times$ that of 3D Gaussian Splatting, while maintaining competitive reconstruction quality. Our renderer supports fisheye, rolling-shutter, motion-blur, and depth-of-field effects through ray generation and sampling, requiring no specialized rasterization. These results show that real-time throughput can be achieved with the flexibility of ray-based rendering. We release our source code, see this https URL

---


### 125. [Magnitude-Direction Decoupling for Fast Video Generation with Flow Matching Models](https://arxiv.org/abs/2608.17695)

**<font color=#1a73e8>作者：</font>** Haonan Xu, Feiyang Chen, Songkui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching models for video generation achieve impressive performance but suffer from high computational overhead due to iterative denoising. In fact, the original model is not necessary for all denoising steps, allowing some steps to use lightweight alternatives for faster sampling. However, directly using caching or lightweight models can deviate from the original denoising trajectory, resulting in suboptimal performance. Through empirical analysis, we find that lightweight models can robustly capture the magnitude components of the original model's output, while caching provides reliable directional guidance. Building on this insight, we propose the Magnitude-Direction Decoupling (MDD) method, which adaptively employs a direction-calibrated lightweight model as a substitute for the original model to accelerate inference and effectively correct deviations in the denoising trajectory. Moreover, MDD further reduces inference costs by reusing magnitude information under classifier-free guidance (CFG). As a result, MDD offers a more reliable and lightweight solution to accelerate sampling. Experiments show that MDD outperforms existing acceleration methods, delivering promising speedups (e.g., up to 2.95x on Wan2.1) while preserving high visual fidelity and content richness.

---


### 126. [Environment-Invariant Subspace Learning for Generalizable Deepfake Detection](https://arxiv.org/abs/2608.17700)

**<font color=#1a73e8>作者：</font>** Shenghao Chen, Hao Jia, Chen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-distribution generalization remains a critical bottleneck in deepfake detection. While recent efforts leverage the semantic priors of large-scale visual foundation models (VFMs), a noteworthy yet underexplored challenge remains: the susceptibility of these semantic priors to environmental interference from factors such as lighting and style. Crucially, this interference establishes spurious correlations between forgery cues and environmental patterns that severely limit generalization. To address this fundamental challenge, we propose an innovative Environment-Invariant Subspace Learning (EISL) framework. The core contribution of EISL is that it aims to disentangle features into orthogonal forgery-relevant invariant factors and environment-related residual factors via a learnable low-rank projection. To facilitate robust feature disentanglement, we also design an Environmental Intervention module that generates diverse and challenging intervention pairs, simulating out-of-distribution environmental shifts to guide the model toward discovering truly invariant forgery representations. Experiments across cross-dataset, cross-generator, whole-face synthesis, and corruption settings show consistent gains and competitive or leading performance against strong detectors, demonstrating improved robustness to unseen forgery types and environmental variations. This work provides a new perspective and a valuable exploration for understanding and tackling the generalization barriers of VFMs in deepfake detection.

---


### 127. [Monitoring Pasture Restoration from Satellite Image Time Series: Caveats and Opportunities](https://arxiv.org/abs/2608.17704)

**<font color=#1a73e8>作者：</font>** Linnea Sartorius, Isak Randahl, Delia Fano Yela 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monitoring nature restoration at scale is an important but difficult ecological problem. Deep learning methods to analyze satellite image time series (SITS) have been widely used for land surface monitoring. In semi-natural grasslands - the habitat type in focus in this work - restoration outcomes develop gradually, yet satellite observations are influenced by weather, acquisition conditions, and processing artefacts, making it difficult to distinguish genuine restoration signals from unrelated temporal variation. In this work, we examine - to the best of our knowledge, for the first time - whether restoration status can be detected directly from satellite image time series by formulating pasture restoration as a binary deep learning classification problem. We evaluate two common SITS deep learning architectures on different Sentinel-2 image combinations, across 1,397 restored Swedish pastures and find that explicitly modeling intra-year variability and per-pasture normalization increases separability, reaching 0.88 accuracy for the best model. We further investigate our results and perform a targeted bias analysis finding that reliable deployment requires temporally balanced labels and evaluation protocols that explicitly test for year-related confounding. We therefore frame our contribution not as a solved restoration-monitoring system, but as a realistic case study of what works, what fails, and what future studies should control for. Code and models are available at this https URL.

---


### 128. [DynaForcing: Overcoming Dynamic Collapse in Self-Forcing Distillation for Streaming Avatar Generation](https://arxiv.org/abs/2608.17707)

**<font color=#1a73e8>作者：</font>** Yubo Huang, Sirui Zhao, Xinchen Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-driven avatar generation requires realistic lip-sync, expressive motion, and real-time streaming. Recent work achieves the latter via self-forcing with Distribution Matching Distillation (DMD), but this paradigm suffers from a critical failure that has not been systematically characterized: dynamic collapse, where the student model converges to a near-static optimum with high perceptual quality but severely suppressed temporal dynamics. We trace this to two causes: the reverse KL objective in DMD, which biases toward low-motion modes, and unanchored self-conditioning, which creates a feedback loop that amplifies collapse. This is especially harmful for avatars, where even subtle motion loss breaks lip-sync and expression.
To address this, we propose DynaForcing, a training framework with three complementary strategies applied at different levels. Specifically, Hybrid Forcing anchors rollouts to ground-truth dynamics at the data level to break the feedback loop. Dynamics-Aware Reward Regularization introduces explicit motion rewards via the RL interpretation of DMD to counteract the reverse KL bias at the loss level. Reference Perturbation perturbs reference images to decouple identity from static details, forcing the model to rely on audio for motion at the conditioning level. We further introduce computation graph pruning and gradient replay, reducing the GPU footprint of self-forcing by over an order of magnitude. Experiments show that DynaForcing recovers dynamics to teacher-comparable levels (Dyn-Deg: 0.31 -> 0.73, Sync-C: 7.03 -> 7.68) while improving visual quality, resolving the quality-dynamics trade-off throughout training without early stopping.

---


### 129. [Accuracy and Robustness of Model Cascades Under Data Perturbations](https://arxiv.org/abs/2608.17711)

**<font color=#1a73e8>作者：</font>** Pallavi Mitra, Jai Kushwaha, Felix Biessmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prediction cascades significantly reduce energy consumption of Artificial Intelligence (AI) models while maintaining high predictive performance. The idea is that easy inputs are routed through a lightweight small model, and difficult uncertain cases are deferred to a larger model. While this design can improve computational efficiency on clean data, its effectiveness depends on the reliability of confidence-based routing. Input degradations, such as static corruptions and sequential perturbations, can shift model confidence and routing decisions. In this paper, we study confidence-based cascade frameworks for image classification and investigate how such degradations affect their confidence-based deferral behavior. We select a model cascade at the pareto-optimum of accuracy, routing quality, and energy consumption that achieves competitive predictive performance with an up to 10-fold decrease in CO$_2$ emissions. We study the behavior of that model cascade under input corruptions and analyze how the cascade's routing decisions change when the input distribution shifts. Our analysis identifies three failure modes. Static corruptions either (1) break the routing signal while the large model remains useful, or (2) degrade both models so deferral no longer recovers accuracy. Sequential perturbations reveal a third mode: predictions stabilize but deferral suppresses, yielding stable but unreliable predictions. These findings demonstrate that energy efficient model cascades require evaluation beyond clean accuracy, with explicit attention to routing reliability under distribution shift.

---


### 130. [Cross-View Correspondence Is a Measurement Intervention: Two-Sided Validation for Agent Evaluation and Credit Assignment](https://arxiv.org/abs/2608.17713)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Ahmad Hafez, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agent evaluations and trace-based learning often compare outputs across transformed views through a post-response correspondence treated as neutral preprocessing. We show that this correspondence is a measurement intervention: omitting it can manufacture sensitivity, an over-aggressive map can manufacture invariance, and multiple optimal correspondences can leave mechanism labels and signed learning credit unidentified. We develop a validity theory and audit with three components: two-sided validation of nuisance removal and response preservation, all-optima identification of downstream conclusions, and uncertainty propagation after validity is established. We characterize the linear feasibility boundary for response-preserving nuisance removal, compute sharp ranges over exact-optimum correspondence sets, and give a distribution-free certificate that retains a credit coordinate only when all exact optima agree on its nonzero sign. Across public code and SQL pipelines, two deterministic optimal tracebacks disagree on temporal localization for 55.9% of 1,586 nonzero trajectory pairs; two frozen 800-rollout tool-use audits, including a task-and-seed-disjoint replication, expose exact-optimum reversals of intended turn-level credit, although a clean public quick-start subset shows none. A pre-registered transport gate failed on natural responses; frozen corrected and held-out controls then show that a map calibrated only on benign examples erases every retained harmful response, while two-sided validation selects response-preserving alternatives. Cross-view correspondence must therefore be declared, validated, and propagated into uncertainty before agent evaluation or credit assignment supports a point conclusion.

---


### 131. [Evaluation of AI-based Visual Crack Detection in Steel Bridges Using Probability of Detection](https://arxiv.org/abs/2608.17726)

**<font color=#1a73e8>作者：</font>** Andrii Kompanets, Finn Michael Sherry, Remco Duits 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bridge structures are regularly inspected for structural damage such as cracks and corrosion in order to ensure public safety and reduce maintenance costs. Much research has been done on automating this process using computer vision methods, which are often evaluated and compared using metrics such as intersection over union, mean average precision, etc. However, predicting the actual effectiveness of an inspection method within the field of structural engineering from these metrics remains challenging. To enable the systematic use of these increasingly popular methods in engineering practice, evaluating the performance of these methods in a way that is compatible with standard engineering approaches is therefore an urgent necessity. We present a new statistical evaluation framework to allow the comparison of computer vision methods with conventional visual inspection for crack detection in steel bridges. The framework is based on probability of detection curves and can account for the influence of image resolution. We apply this evaluation method to the real-world ``Cracks in Steel Bridges'' dataset, which contains annotated images of cracks in bridge structures. The quantification of the probability of detection and its uncertainty enables a practical assessment of the effect of automated methods for damage detection in structural reliability analyses. In turn, this enables the wide-spread use of automated (AI-based) damage detection in safety critical applications. This evaluation method provides evidence that the proposed computer vision approach approach is robust for the crack detection task and can have a high added value as an addition to conventional visual inspection methods.

---


### 132. [BullsEye: Directed Firmware Fuzzing](https://arxiv.org/abs/2608.17729)

**<font color=#1a73e8>作者：</font>** Lorenzo Ralli, Emilio Coppa  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of Internet of Things (IoT) devices has expanded the digital attack surface, making firmware analysis critical for modern software security. A key security concern stems from the frequent reuse of third-party software components, a practice that often introduces known vulnerabilities into firmware images. Whether a given image actually exposes such a flaw is an open question, and public proof-of concept exploits make answering it urgent. Directed Greybox Fuzzing (DGF), a technique that enables targeted exploration of specific binary locations, offers a promising solution for detecting such vulnerabilities. However, DGF has reached firmware only at function granularity, too coarse to aim at the vulnerable block itself.
This article presents BULLSEYE, the first DGF framework to schedule closed-source Linux-based firmware fuzzing by basic-block-level distance to user-specified targets. Our methodology combines static and dynamic analysis to enable DGF in the constrained firmware domain, focusing on vulnerabilities in reused third-party components. We introduce novel DGF heuristics that address limitations of traditional approaches. We compare BULLSEYE against four greybox-fuzzing baselines sharing its execution back-end, including reimplementations of AFLGO and WINDRANGER, and against GREENHOUSE, a state-of-the-art firmware re-hosting framework. On 40 vulnerability sites across 32 firmware images, BULLSEYE reproduces every target within budget, against 35 for the strongest of the four baselines, and reduces Time-to-Exposure by a geometric mean of 9.5x to 72.5x over them; against GREENHOUSE, on the 18 targets its pipeline supports, BULLSEYE is faster by a geometric mean of 9.8x.

---


### 133. [Offline Multi-Agent Reinforcement Learning with a Physics-Informed World Model for Cooperative Mixed Traffic Control](https://arxiv.org/abs/2608.17739)

**<font color=#1a73e8>作者：</font>** Lu Liu, Chi Xie, Xi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This study investigates cooperative control of connected and automated vehicles (CAVs) at partially observable highway bottlenecks in mixed traffic, aiming to mitigate congestion without relying on complete global traffic states or online trial-and-error. We propose a physics-informed world model-based offline multi-agent reinforcement learning framework that reconstructs a physically interpretable global traffic state from local CAV observation-action histories, with coupled macroscopic-microscopic traffic dynamics providing physics-based supervision. A probabilistic ensemble world model learns traffic-state transitions and system rewards, while model disagreement quantifies epistemic uncertainty. Multi-step imagined rollouts with pessimistic rewards and uncertainty-driven truncation are then used for offline policy learning. Experiments in a SUMO-based on-ramp bottleneck using approximately $1\times10^6$ offline transitions show that physics supervision improves state reconstruction and world-model prediction accuracy.

---


### 134. [Neuro-symbolic learning over OWL 2 DL via consequence-based compilation to differentiable circuits](https://arxiv.org/abs/2608.17741)

**<font color=#1a73e8>作者：</font>** Olga Mashkova, Asaad Mohammedsaleh, Fernando Zhapa-Camacho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> OWL 2 DL ontologies, grounded in the description logic $\mathcal{SROIQ}$, express large knowledge bases in biomedicine and the Semantic Web. Neuro-symbolic (NeSy) learners over description logics either embed the ontology in a continuous space, abandoning classical entailment, or restrict to the Horn fragment $\mathcal{EL}^{++}$, which has a single canonical model. We present Baobab, which compiles a $\mathcal{SROIQ}$ ontology with a finite ABox into a Sentential Decision Diagram (SDD): it saturates a propositional core under a consequence-based calculus and instantiates the remaining $\mathcal{SROIQ}$ features (nominals, number restrictions, and the role axioms) over the active domain. The SDD's evidence-conditioned weighted model count then trains a perception network to recognize real images under partial ABox supervision: on an ontology that exercises every distinctive $\mathcal{SROIQ}$ feature, a CNN learns to read MNIST digits coupled by a successor relation and recovers latent ontology concepts that an independent perception leaves at chance. When the supervision admits several ontology-consistent completions, an independent perception collapses onto one, a reasoning shortcut: we show that a mixture indexed by the query's justifications can represent the calibrated posterior no independent perception can, and that seeding it from the circuit's enumerated completions attains the Bayes-optimal posterior on a real-image MNIST task where single-WMC and learned mixtures (the BEARS-ensemble hypothesis class) do not: to our knowledge the first to characterize and mitigate reasoning shortcuts in a non-Horn description logic. Soundness of the compiler and the representation result are machine-checked in Lean 4. Code is available at this https URL.

---


### 135. [TINA+: Probing Residual Visual Knowledge in Unlearned Diffusion Models via Diffusion-Consistent Text-Free Inversion](https://arxiv.org/abs/2608.17747)

**<font color=#1a73e8>作者：</font>** Qianlong Xiang, Miao Zhang, Kun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although text-to-image diffusion models exhibit remarkable generative power, concept erasure techniques are essential for preventing harmful content. Existing adversarial probes evaluate these methods by testing whether erased concepts can still be recovered. However, existing erasure and probe methods remain largely text-centric, focusing on whether the text-to-image mapping is severed while overlooking whether the corresponding visual knowledge remains. To investigate this question from a visual perspective, we leverage diffusion inversion to probe whether a generative trajectory can reconstruct visual instances of an erased concept. Under a null-text condition, standard inversion avoids the textual pathway but amplifies approximation errors, hindering faithful trajectory recovery. To address this challenge, we introduce TINA+, a diffusion-consistent Text-free INversion Attack equipped with optimization-based inversion. We also find that unconstrained diffusion inversion may discover spurious trajectories, even allowing a randomly initialized diffusion model to reconstruct the target concept. Such trajectories may falsely indicate residual visual knowledge. TINA+ therefore introduces Diffusion-Consistent Trajectory Regularization to suppress this failure mode. By penalizing trajectories that fall far below the expected marginal energy evolution of diffusion, TINA+ suppresses spurious inversion paths while preserving its ability to recover erased concepts. Experiments across twelve erasure methods, four concept-erasure tasks, and different model architectures demonstrate that TINA+ reliably probes residual visual knowledge through diffusion-consistent visual trajectories. These results provide stronger evidence that current methods often obscure concepts by severing text-image links rather than eliminating the underlying visual knowledge.

---


### 136. [The Curious Case of Exploding DecPOMDPs: Containing the Fire through Policy Counting](https://arxiv.org/abs/2608.17749)

**<font color=#1a73e8>作者：</font>** Nazlı Nur Karabulut, tanya Braun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralised partially observable Markov decision processes (DecPOMDPs) provide a general framework for modelling multi-agent decision making under uncertainty. However, DecPOMDPs are known to suffer from exponential complexity in the number of agents. One way to combat this intractability in agent numbers is to look at partitions of agents that exhibit a form of symmetry among agents, allowing for a compact encoding by counting. However, a challenge arises as the policy space explodes, even though the model complexity and evaluation cost reduce to a polynomial dependence. In this paper, we redirect our focus from counting agents to counting policies, which actually enables tractability in agent numbers for so called policy-counted DecPOMDPs. Further, we present policy-counted dynamic programming using the compact representation to solve policy-counted DecPOMDPs efficiently.

---


### 137. [MAGPIE-Net: Predicting short-duration heavy-rainfall events in station neighborhoods from multitemporal FY-4A AGRI observations](https://arxiv.org/abs/2608.17753)

**<font color=#1a73e8>作者：</font>** Xiang Lin, Yunying Li, Chengzhi Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Short-duration heavy-rainfall warning determines whether 1 h rainfall will exceed a threshold within a target-station neighborhood over the next few hours. Multitemporal infrared and water-vapor observations from the Fengyun-4A Advanced Geostationary Radiation Imager (FY-4A AGRI) capture cloud-top cooling, moisture evolution, and cloud expansion before substantial surface rainfall develops. However, most deep-learning nowcasting methods convert these signals into local warnings by post-processing gridded precipitation predictions, preventing station-neighborhood event targets from directly supervising the satellite-to-station learning pathway. We propose MAGPIE-Net, which embeds a geographically adaptive, differentiable grid-to-station mapping in a pathway combining convection-initiation features, multiscale encoding, and auxiliary gridded precipitation diagnosis. Station-neighborhood event losses thereby constrain the satellite representation and its mapping to irregular station locations for 0-3 h event prediction. In independent 2023 warm-season tests over central and eastern China, critical success index (CSI) values under the primary 40 km/20 mm h-1 definition were 0.371, 0.304, and 0.238 at 0-1, 1-2, and 2-3 h. Across episodes, MAGPIE-Net achieved a detection rate of 65.1% and a mean lead time of 64.6 min, compared with 23.6% and 18.3 min for the best gridded-output baseline, and remained superior for smaller neighborhoods and the 50 mm h-1 threshold. During the critical early-warning stage, when antecedent 1 h rainfall within 40 km remained below 1 mm, MAGPIE-Net detected 51.9% of episodes with a mean lead time of 38.5 min. These results show that event-oriented satellite-to-station modeling converts multitemporal geostationary cloud and moisture observations into local heavy-rainfall warnings more effectively than gridded-precipitation modeling.

---


### 138. [Achievement Unlocked: Let's Get Hacked! An Empirical Study of Cybercrime in the Video Gaming Ecosystem](https://arxiv.org/abs/2608.17754)

**<font color=#1a73e8>作者：</font>** Janine Schneider, Jan Kallenborn, Tim Hoffmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The ubiquity of the video game industry and its large user base have transformed video games into complex social and economic ecosystems. Unfortunately, this growing popularity also attracts cybercriminals who deliberately exploit game-specific mechanisms to target players. Despite this growing threat, cybercrime in the gaming ecosystem has received little systematic attention in prior research.
In this work, we present an empirical study of cybercrime affecting video game players, combining qualitative and observational analyses to characterize gaming-related attacks, identify common attack vectors and motivations, and examine player responses. Our study is based on an online survey with 57 international participants, semi-structured interviews with two confirmed victims of gaming-related cybercrime, and an analysis of 2,574 publicly available posts reporting cybercrime incidents across multiple online gaming platforms. Our findings indicate that the theft of digital items is a prevalent motivation for attacks. We further observe that gaming-related features and services, such as item trading, team voting, and tournaments, create incentives for players to engage in risky interactions. In addition, our results highlight the targeted exploitation of weaknesses in customer support processes and reveal that certain security mechanisms provide only a false sense of protection.

---


### 139. [Efficient Fuzzy PSI under One-Sided Assumptions](https://arxiv.org/abs/2608.17770)

**<font color=#1a73e8>作者：</font>** Xinpeng Yang, Meng Hao, Yanxue Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fuzzy private set intersection (PSI) enables two parties to identify approximately matching elements between their input sets, where two elements are considered a match if their distance is at most a threshold $\delta$ under a given metric. Although substantial progress has been made, existing constructions for general Minkowski distances either rely on strong two-sided geometric separation assumptions or incur substantial overhead under one-sided assumptions.
In this work, we present the first concretely efficient fuzzy PSI protocols for general $L_{p\in[1,\infty]}$ distances under one-sided assumptions, relying solely on lightweight symmetric-key primitives. Our constructions support both sender-sided and receiver-sided settings. We further study sparser input distributions and present more efficient protocols tailored to this case. To reduce the overhead scaling with $\delta$, we non-trivially incorporate prefix trie techniques into our protocols, achieving $O(\log\delta)$ complexity for general $L_{p\in[1,\infty]}$ distances for the first time, improving upon $O((\log\delta)^d)$ or $O(\delta)$ complexities of prior works.
Extensive experiments, across a wide range of parameter settings, show that our protocols significantly outperform prior works under the same assumptions. Specifically, against van Baarsen and Pu (EUROCRYPT'24), our protocols achieve up to $239\times$ faster computation and up to $20\times$ lower communication. Against Dang et al. (CCS'25), we achieve up to $518\times$ speedup and up to $63\times$ communication reduction. Against Bui et al. (ASIACRYPT'25), we achieve up to $4818\times$ faster computation and up to $282\times$ lower communication.

---


### 140. [Training-Free Human-in-the-Loop Anomaly Detection via Memory Bank Correction](https://arxiv.org/abs/2608.17775)

**<font color=#1a73e8>作者：</font>** Ayusha Abbas, Saram Abbas, Kabita Adhikari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detectors are hardest to deploy exactly where training data is scarcest: a newly commissioned production line has a handful of verified "golden" samples and no machine-learning engineer on the factory floor. We present a training-free human-in-the-loop framework in which a domain expert corrects a PatchCore detector by direct memory bank editing: no retraining, no gradients, no original training data. A false-positive correction inserts the reviewed image's normal patches through a self-calibrating novelty gate admitting only those beyond the median pool-normal nearest-neighbour distance. From a bank built on only ten golden samples, operator corrections close a median 66% of the gap to an uncorrected fully trained bank (mean 80%, raised by three categories that overshoot parity), significantly improving 12 of 15 MVTec AD categories and harming none: ten samples plus corrections outperform hundreds of samples without them. On already-trained banks the headroom is smaller and concentrated where the bank undersamples normal appearance (gated: toothbrush +0.10, metal nut +0.09, zipper +0.05, screw +0.05), and no category except grid is significantly harmed. Evaluation uses a held-out protocol (20 splits per category, Holm-corrected Wilcoxon), because corrected images entering the bank inflate naive evaluation toward AUROC 1.0 by memorisation. Passive and active querying are statistically indistinguishable; a matched-label-budget control attributes gains to deployment-time label production at 43% of exhaustive-review cost; a defect-memory extension fails decisively. Feedback is simulated from ground truth; live expert trials, where mislabelling is costliest on small banks, remain future work.

---


### 141. [Diff-DDoS: Realistic Cyber-Physical Attack Synthesis and Robust Detection for 5G-Enabled CPS Using Tabular Diffusion Models](https://arxiv.org/abs/2608.17796)

**<font color=#1a73e8>作者：</font>** Bilal Hussain, Xiao Tang, Qinghe Du 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning-based DDoS detectors for 5G-enabled cyber-physical systems face scarce labeled attack data and unrealistic synthetic substitutes, which limit robustness against adaptive adversaries. Detectors trained on hand-crafted attacks with fixed scaling multipliers degrade catastrophically (F1-score drops of about 47 percent to 100 percent, depending on scenario) when confronted with realistic, distribution-preserving samples. We propose Diff-DDoS, a three-phase framework for realistic attack synthesis and robust detection using tabular diffusion models. Phase 1 trains a baseline CNN cell-level detector on spatiotemporal grids from call detail records (CDRs). Phase 2 trains a tabular denoising diffusion probabilistic model (TabDDPM) on normal CDR aggregates to generate realistic attacks and expose detector vulnerabilities. Phase 3 introduces adversarial diffusion training (ADT), using inverse classifier guidance to generate hard yet distribution-preserving samples until the detector converges. On a Milano CDR dataset across SMS-flooding, silent-call, Internet-signaling, and blended scenarios, ResNet50 with ADT recovers F1-scores of 79.62 percent (silent-call), 100 percent (Internet), and 92.79 percent (blended). After validation-based threshold calibration, ADT reaches 100 percent SMS F1 versus 47.3 percent for CTGAN, and matches the strongest gradient-based adversarial-training baseline on silent-call. These results support tabular diffusion models for stress-testing and hardening intrusion detectors in data-scarce 5G cyber-physical deployments.

---


### 142. [Training with synthetic data for drone detection in thermal imagery](https://arxiv.org/abs/2608.17799)

**<font color=#1a73e8>作者：</font>** Tanel Liiv, Sander Soodla, Nzamba Bignoumba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ground-to-Air (G2A) drone detection in medium- and long-wave infrared (MWIR/LWIR) imagery is challenging due to reduced texture information, sensor noise, weak thermal contrast, and the scarcity of annotated data. This work investigates a synthetic-first training strategy that combines synthetic scene generation with fine-tuning on real data. We show that synthetic data provides an effective basis for learning initial object representations, while real in-domain thermal imagery is still essential for reliable deployment. Even small amounts of real IR data substantially reduce domain gaps. Our experiments indicate that dataset alignment has a stronger impact on performance than model scale. Finally, our analysis of the dataset suggests that semantic alignment in feature space is the strongest predictor of model performance, while radiometric properties such as entropy and dynamic range also contribute to detection robustness. This work provides a foundation for combining synthetic and real IR data for effective G2A drone detection.

---


### 143. [Scale Matters: Adaptive Granularity Selection for Cross-Species 3D Plant Organ Segmentation](https://arxiv.org/abs/2608.17803)

**<font color=#1a73e8>作者：</font>** Carla Salazar, Lazaros Nalpantidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D foundation models provide powerful feature representations for point cloud learning by controlling spatial granularity. However, relying on a fixed spatial granularity severely limits generalization in applications like plant phenotyping, where organ morphology and size vary substantially across species and growth stages. To address this, we propose AGS-PlantSeg, a few-shot 3D plant organ segmentation method that leverages the frozen Utonia (arXiv:2603.03283) foundation model combined with Adaptive Granularity Selection. By dynamically selecting the best granularity levels for each specific plant model, our method extracts optimized geometric features for a lightweight MLP segmentation head. Extensive experiments across PLANesT-3D (arXiv:2407.21150), Pheno4D , and Crops3D demonstrate that AGS-PlantSeg significantly improves cross-species generalization, achieving 88.9% average mIoU performance and outperforming fixed-granularity baselines by 2.5 mIoU points. Despite requiring minimal annotated data, our approach is highly competitive with fully supervised, plant-specific architectures.

---


### 144. [GenRec: Knowing Where to Reconstruct and Where to Generate](https://arxiv.org/abs/2608.17832)

**<font color=#1a73e8>作者：</font>** Ata Çelen, Jaewoo Jung, Federico Tombari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative novel view synthesis from sparse input images is rarely all reconstruction or all generation: pixels visible in some source view have a unique correct value modulated only by view-dependent shading, while pixels in disocclusions or beyond the captured volume admit a distribution of plausible completions. Existing generative novel-view-synthesis methods conflate these regimes under a single uniform loss, blurring the line between geometric fidelity and creative hallucinations even when scene geometry is injected through warped point clouds or projected depth. We introduce GenRec, a multi-view flow matching model that builds the reconstruction--generation split directly into its architecture, supervision, and gradient flow. Guided by an observation mask derived from the source cameras and a monocular depth estimator, a flow matching backbone jointly denoises RGB and scene-coordinate maps across all target views, while a pixel-space refinement stage restores high-frequency detail on observed pixels; the same mask gates supervision so regression signals do not contaminate the generative prior. Across RealEstate10K, DL3DV-10K, and Mip-NeRF~360, in both single-view extrapolation and two-view interpolation, GenRec attains the best reconstruction fidelity in observed regions while also surpassing purely generative baselines on perceptual quality in unobserved ones, showing the effectiveness of our approach.

---


### 145. [Efficient Resource Optimization for Split Federated Learning](https://arxiv.org/abs/2608.17849)

**<font color=#1a73e8>作者：</font>** Wei Wei, Xianhao Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split federated learning (SFL) has emerged as a powerful paradigm for model training at the edge. However, SFL inherently involves discrete decision variables for model splitting and resource allocation, resulting in a challenging mixed-integer problem. Consequently, prior optimization schemes for SFL are either \textit{heuristic} or \textit{computationally inefficient}, which cannot handle large-scale user populations. To address this limitation, this work establishes an efficient optimization framework for SFL under resource-constrained networks. Our framework jointly optimizes model splitting and resource allocation to minimize training cost, which is defined as the weighted sum of latency and energy costs. We first study the model splitting problem and develop a polynomial-time algorithm that achieves the global optimum. Then, we extend the approach to the joint model splitting and resource allocation problem. In this case, we formulate it as a two-dimensional master problem and develop an efficient approximation method with a $(1+\epsilon)$-approximation guarantee. Extensive experiments show that the proposed approach provides efficient solutions to strike the optimal energy--latency tradeoff.

---


### 146. [CFB-GBM v2.0: An Augmented Longitudinal Dataset for Multi-Modal Glioblastoma Segmentation, Radiomics, and RANO Progression Tracking](https://arxiv.org/abs/2608.17884)

**<font color=#1a73e8>作者：</font>** Alexandre G. Leclercq, Noémie N. Moreau, Hugo Audebert 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glioblastoma (GBM) is the most aggressive primary brain tumor in adults, with a median overall survival of 15 months. Longitudinal, multi-modal imaging datasets with comprehensive clinical and treatment data are essential to support the development of reproducible computational methods for treatment response prediction, disease progression modelling, and personalized medicine. We present CFB-GBM v2.0, an extension of our previously released CFB-GBM dataset comprising 264 GBM patients treated according to the standard Stupp protocol. The primary contribution of this release is the completion of Gross Tumour Volume (GTV) delineations across all available timepoints ($t_0$, $t_1$ and $t_2$), increasing the overall GTV completion rate from 35% to 97%. This was achieved using a nnU-Net model pre-trained on BraTS 2021 and fine-tuned on CFB-GBM ground-truth contours, with the generated segmentations validated by five radiation oncologists. From these longitudinal GTV annotations, volumetric RANO 2.0 response category labels were derived for all available temporality pairs ($t_0 \rightarrow t_1$, $t_0 \rightarrow t_2$ and $t_1 \rightarrow t_2$). To further ease dataset usability and reproducibility, brain masks computed with HD-BET and pre-computed radiomic features extracted with PyRadiomics are provided for each patient timepoint and MRI modality. Additionally, the WHO classification guideline (2016 vs. 2021) applicable to each patient's diagnosis is now explicitly documented. CFB-GBM v2.0 is publicly available on The Cancer Imaging Archive (TCIA) at this https URL .

---


### 147. [Dynamic Compression in Recurrent Networks](https://arxiv.org/abs/2608.17896)

**<font color=#1a73e8>作者：</font>** Jyothish Pari, Ryan Bahlous-Boldi, Pulkit Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent models process long contexts efficiently by compressing their history into a fixed-size state, but modern architectures typically do so in a single causal pass over the sequence. Each input must therefore be compressed before the model knows how it will later be used, forcing a limited state to compromise across possible future demands. We introduce dynamic compression, which allows a recurrent model to selectively revisit past tokens and revise its fixed-size state through additional recurrent updates. The model need not preserve every part of the history at uniformly high fidelity in its recurrent state, because lower-fidelity information can be revisited from the retained raw sequence when it becomes relevant. We study this in a controlled setting where the model first learns multiple functions in-context and, later in the same sequence, encounters a series of few-shot tasks that each require it to identify and reuse one of those functions. A single-pass model must preserve every function at sufficient fidelity for any future task, whereas selective re-scanning allows the model to revisit and refine only the function currently needed. We find that dynamic compression substantially reduces the recurrent state required for accurate reuse and scales more favorably as the number of stored functions grows. These results demonstrate a computation--memory tradeoff in which recurrent models can spend more computation revisiting their history to make more effective use of a fixed-size state.

---


### 148. [AutoResearch: Insight In, Hallucination Out](https://arxiv.org/abs/2608.17906)

**<font color=#1a73e8>作者：</font>** Yiming Ren, Xiang Liu, Qumeng Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research systems are increasingly capable of executing long research workflows, yet automation alone does not ensure that the resulting process remains scientifically grounded. We introduce AutoResearch, a two-stage system that connects Idea Generation with Idea Execution to address both how research ideas are formed and how they are reliably established through experimentation. In Idea Generation, AutoResearch continuously integrates emerging research signals with accumulated domain knowledge, identifies transferable mechanistic insights, and uses multi-model generation and cross-review to produce grounded, testable research plans. In Idea Execution, coordinated agents decompose these plans into experiments, iteratively implement and diagnose them, and employ independent evidence-based review before accepting research conclusions. Across representative settings in cross-modal retrieval, systems optimization, and benchmark-driven machine learning, AutoResearch turns generated ideas into measurable progress, detects and corrects unreliable experimental results, and makes evidence-conditioned decisions to continue, revise, or terminate research directions. For example, on RSICD benchmark, an AutoResearch-generated idea improves mean Recall from 32.84 to 34.69, while recording only 5 audit-confirmed issue events compared with 11-27 for other autonomous research systems. These results demonstrate a research process in which meaningful insight is grounded before experimentation and conclusions are grounded before acceptance: Insight In, Hallucination Out.

---


### 149. [Hybrid ML for Lightweight Pre-Route Delay Estimation in Open-Source IC Design](https://arxiv.org/abs/2608.17914)

**<font color=#1a73e8>作者：</font>** Marvin Castro Castro, Erick Carvajal Barboza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Static Timing Analysis (STA) is a critical step in the design flow of digital integrated circuits, however, obtaining accurate delay estimations can represent a challenge when limited information regarding physical design is available. In response, this work presents a hybrid and light-weight machine learning (ML) based approach that combines a decision tree with linear regression to improve pre-routing delay estimations generated by the open-source RTL-to-GDSII tool OpenLane. The proposed model achieves an 80\% reduction in error compared to OpenLane's estimates, demonstrates a 71\% improvement even without utilizing OpenLane-specific parameters. Overall, this method offers an alternative to traditional delay propagation techniques and more complex machine learning models that is not only accurate, but is also over 300 times smaller, 2 times faster and offers a higher explainability.

---


### 150. [Comparative Study of Out-of-the-Box Technology for Automatic Target Detection and Recognition](https://arxiv.org/abs/2608.17917)

**<font color=#1a73e8>作者：</font>** Alma M. Liezenga, Lotte Nijskens, Henrik R. Baumann 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic Target Detection and Recognition (ATD/R) is critical for military decision support and (semi-)autonomous operations. Recent advances in object detection and artificial intelligence (AI) significantly boosted the potential performance of ATD/R. However, the scarcity of publicly available military datasets limits the application of these systems. As a solution, this paper explores the use of publicly available models and civilian datasets to achieve reasonable performance in military contexts. We benchmark several state-of-the-art models, including six iterations of the YOLO series and two variations on the DETR framework, on a newly acquired military relevant dataset. This dataset features military vehicles and challenging circumstances, including various degrees of occlusions and small targets. The out-of-the-box version of each model is validated alongside a version finetuned on the VisDrone dataset. This dataset features small objects, an Air-to-Ground (A2G) perspective and relevant classes, potentially generalizing to our military ATD/R task. We compare the performance of the models using mAP@0.5 and mAP@0.5:0.95, across A2G and Ground-to-Ground (G2G) perspective, target size and model size, giving insight into the real-time capabilities of models. Our main findings are: (1) bigger models outperform smaller models, (2) DETR-based models show promising results compared to the YOLO series,(3) fine-tuning models on an out-of-domain A2G dataset, improves their A2G performance and slightly improves their performance on small objects, but (4) all models still struggle with detecting small objects in an A2G scenario. We conclude that, despite recent advances in object detection, in-domain training is still crucial for creating capable ATD/R systems.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
