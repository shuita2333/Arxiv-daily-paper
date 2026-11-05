# 📦 其他研究 | 2026年11月06日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 101. [TRACK: Multiple Instance Learning for Anti-Money Laundering in Transaction Networks](https://arxiv.org/abs/2611.06035)

**<font color=#1a73e8>作者：</font>** Seonkyu Lim, Inwoo Tae, Gwangui Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anti-money laundering (AML) investigations are organized around accounts, while the suspicious evidence for an account may reside in only a few of its transactions. Yet many account-level detectors summarize transactions before learning, and message-passing models may aggregate once more over neighboring accounts. We name this discrepancy the aggregation mismatch and study it under an account-window benchmark label defined by the presence of at least one flagged transaction. We recast account-level AML detection as multiple instance learning, in which an account-window is a bag and its transactions are instances. We propose TRACK, which encodes every transaction with a shared encoder and selectively pools the encodings into an account decision. To emulate coarse supervision, we withhold the transaction labels of five AML datasets from TRACK throughout training. Under a time-ordered protocol, TRACK achieves the highest average precision among the tabular and graph baselines trained from account labels on every dataset. Despite using only account-window supervision, it remains competitive with edge classifiers trained directly from transaction labels. Its instance scores also rank flagged transactions well above chance and approach or exceed directly supervised ranking performance across datasets.

---


### 102. [PIMROP: A Feasibility Study of Return-Oriented Programming on Commercial Processing-in-Memory Architectures](https://arxiv.org/abs/2611.06036)

**<font color=#1a73e8>作者：</font>** William C. Tegge, Shouzhi Fang, Alex K. Jones  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Processing-in-Memory places small programmable cores on the memory device, where they execute beside the DRAM banks and beyond the control-flow defenses that protect host programs. The security of this in-memory code is an attack surface that remains largely unstudied. We present PIMROP, to our knowledge the first demonstrated code-reuse attack on a commercial Processing in-Memory ISA. We show that return-oriented programming is feasible on a real, commercially shipped PIM instruction set, the UPMEM DPU, whose DRAM Processing Units run C compiled by a dedicated LLVM toolchain. We build Galileo-for-DPU, a gadget scanner adapted to the DPU's fixed-width, 8-byte-aligned RISC encoding, and run it entirely on the UPMEM functional simulator in a reproducible Docker and VM environment. We find the runtime library that every kernel links already yields 517 non-trivial gadgets covering all five canonical ROP primitive classes, and all 13 PrIM benchmarks we scanned carry gadgets as well. We then demonstrate two verified end-to-end attacks, each reproducible on 10 of 10 runs. In the first, a stack buffer overflow in a DPU kernel overwrites the saved return address and diverts control into a routine that copies a secret into host-readable memory. In the second, we leak the same secret using a chain of reused gadgets alone, without diverting control into any such routine. We further show that two standard defenses--stack canaries and _FORTIFY_SOURCE-style bounds-check fortification--fail on the DPU in ways specific to the platform (misplaced canary, silently inactive wrapper), and we verify a bounds-checked DMA that stops the attack on 10 of 10 runs with no effect on benign requests. To enable further research on PIM security, we open-source Galileo-for-DPU and our testing harness at this https URL.

---


### 103. [Act-HiMotif: Hierarchical Daily Activity Schedule Generation via Learned Activity-Structure Motifs](https://arxiv.org/abs/2611.06038)

**<font color=#1a73e8>作者：</font>** Yushi Bai, Kang Liu, Ling Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating daily activity schedules from individual attributes (e.g., age and income) is valuable for activity-based travel modeling and human behavior simulation. The task is challenging because exact activity structures follow a highly imbalanced, long-tailed distribution, while the same structure can admit multiple duration allocations under a fixed full-day budget. Direct generation must therefore learn many exact activity structures from highly uneven observations while modeling their possible temporal realizations. However, many exact structures share recurring activity organization. Based on this observation, we propose Act-HiMotif, a hierarchical motif-based generative model that introduces learned, reusable activity-structure motifs as an intermediate representation between individual profiles and specific activity structures. Act-HiMotif first distinguishes home-only days from active days, then samples a motif from a profile-conditioned prior to guide activity-structure generation, and finally applies a budget-constrained duration allocator to generate activity durations that sum exactly to the full-day horizon. This hierarchy models home-only routing, activity-structure generation, and duration allocation at their corresponding levels, while motifs allow related structures to share statistical support without losing their distinct sequences. Experiments on large-scale travel survey data show that Act-HiMotif outperforms strong baselines in both in-distribution and spatial generalization settings, demonstrating the effectiveness of hierarchical generation and reusable activity-structure motifs for producing realistic profile-conditioned daily activity schedules.

---


### 104. [DeepfakeGenome: Toward Next-Generation Deepfake Attribution](https://arxiv.org/abs/2611.06046)

**<font color=#1a73e8>作者：</font>** Shunli Wang, Xinyu Zhou, Yandan Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In recent years, AIGC technologies are capable of generating hyper-realistic forged facial images, posing severe threats to facial security safety. To tackle these challenges, early Deepfake research primarily centered on real-fake classification. Recently, growing efforts have been devoted to the Deepfake Attribution (DFA) of generated content. Nevertheless, existing research on Deepfake detection and attribution faces saturated performance in binary classification, limited diversity in datasets and algorithms, and imperfect evaluation protocols, which severely impede practical application. To address these limitations, we propose a comprehensive deepfake detection and attribution benchmark named DeepfakeGenome (DFG). It contains 100 facial forgery algorithms and 2M images in total, achieving 4x to 100x larger than prior DFA benchmarks. We further design 4 protocols for practical evaluation, including a novel retrieval-based attribution paradigm. Unlike previous open-set evaluation metrics, the proposed retrieval metrics are more aligned with the real-world active defense situation of blacklist registration mechanisms. Based on these elaborate designs, we investigate the performance ceiling of deepfake attribution task. Over 2k experimental evaluations are conducted, and 10 insightful findings are derived. We believe this work can provide new insights into the DFA research field. The Code and Benchmark of DFG are avaliable on this https URL.

---


### 105. [Alleviating Limited Effectiveness and Multi-Class Collapse in Deep Graph-level Clustering](https://arxiv.org/abs/2611.06052)

**<font color=#1a73e8>作者：</font>** Xiaoyang Lin, Renchi Yang, Yuqi Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Given a collection of $N$ graphs, graph-level clustering (GLC) seeks to partition the $N$ graphs into semantically meaningful groups, which serves as a fundamental task in analyzing graph-structured data. While Graph Isomorphism Networks (GINs) have become the de facto encoders for GLC, they still fail to distinguish graphs due to their neglect of global topology. On top of that, existing deep clustering frameworks suffer from severe "clustering collapse" issues, particularly in imbalanced multi-class scenarios. To address these challenges, we propose S$^3$GLC, a novel framework that integrates global topological characteristics with local neighborhood features for balanced GLC. Theoretically, we leverage the Hoffman-Wielandt inequality to construct Spectral Signature as a rigorous lower bound for graph edit distance (GED), providing a computationally efficient proxy for global topological features. We additionally propose a joint manifold-preserving sparse regression module to fuse Spectral Signature with Spatial Representation, eliminating noise while preserving the complementary information. Furthermore, to mitigate clustering collapse, we introduce a balanced clustering objective based on optimal transport, harnessing the Sinkhorn-Knopp normalization to enforce equipartition constraints on cluster assignments. Extensive experiments on 10 real-world datasets demonstrate that S$^3$GLC significantly outperforms 15 state-of-the-art baselines, achieving remarkable improvements on benchmark datasets such as REDDIT-12K and OGBG-PPA.

---


### 106. [TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](https://arxiv.org/abs/2611.06061)

**<font color=#1a73e8>作者：</font>** Jiaao Yu, Yanjian Zhang, Haoyang Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video world models allow users to explore generated environments through camera navigation. Continuous hand motion provides a fine-grained action channel for interacting with the people and objects encountered during exploration. We present TouchéWorld, a framework that integrates gesture-driven interaction into a camera-controlled video world model. Given an initial image and a scene-description prompt, the model generates video conditioned on temporally aligned camera and hand controls. We construct joint camera--hand training data from heterogeneous egocentric videos through annotation completion, consistency-based filtering, and temporal alignment. Building on a pretrained camera-controlled world model, we combine spatial hand-skeleton conditioning with numerical hand-motion features through parameter-efficient adaptation. Causal adaptation and few-step distillation support chunk-level online generation, allowing users to update their controls based on generated visual feedback. We further introduce TouchéBench to evaluate hand-motion following, camera--hand coordination, online interaction, and object response. Together, these components establish a framework for studying continuous exploration and hand-driven interaction within generative worlds.

---


### 107. [Learning From Static Context in Federated Time Series Forecasting](https://arxiv.org/abs/2611.06064)

**<font color=#1a73e8>作者：</font>** Viktor Walter, Andreas Wagner, Fabian Stricker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting is shifting from locally trained, per-series models to global models trained across many heterogeneous series, which requires learning what sets the series apart. When the raw data cannot be centralized, such a global model is trained with federated learning (FL), one client per data owner. State-of-the-art forecasters such as the Temporal Fusion Transformer (TFT) tell series apart through a static input that describes each series and does not change over time. In the special case of a federated setting where each client holds a single series, this static input is constant within each client and varies only across clients. We ask whether a federated TFT can learn from it. Per-batch FedAdam, which aggregates gradients after every batch, uses the static input almost as well as central training, whereas communication-efficient schemes with local epochs (FedAvg, FedAdam+Prox) extract far less from it and gain nothing significant on either application dataset. At the same local computation, an Adam-compatible SCAFFOLD keeps the static pathway responsive on wind power and gains significantly there. On building energy its error still drops, but the static pathway falls silent, so drift and communication frequency cannot be fully separated as the cause. Only per-batch FedAdam matches or beats the per-client local models across all datasets. We confirm the effect on building-energy meter data, a wind-power dataset, and a controlled synthetic dataset. The loss is not specific to the TFT: on the synthetic and the wind data two further architectures with different static-conditioning mechanisms show it as well.

---


### 108. [ProcessPrefBench: Evaluating Cross-Task Transfer of Individual Process Preferences from Naturalistic Human-AI Interaction](https://arxiv.org/abs/2611.06065)

**<font color=#1a73e8>作者：</font>** Yiwen Yang, Guanming Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In natural human-AI dialogue, users' corrections, requests, and self-descriptions carry reusable signals about how they want work to be done. These signals reveal individual process preferences, user-specific standards for evidence, depth, analytical focus, procedure, and delivery. We ask whether a preference revealed in one dialogue can shape an assistant's later answer when the task does not restate it. ProcessPrefBench uses three months of natural dialogues from two knowledge workers to build 66 source-target cases separately judged for source evidence and target applicability. Sources are preselected, so the benchmark tests application rather than retrieval. We test three models with target-only, full-history, and distilled-preference prompts. Target-specific 0-2 rubrics score preference realization, and a task gate flags severe failures. Compared with target-only prompting, full-history and imperative distilled-preference prompting raise preference realization by 0.204 and 0.244 points on the 0-2 scale, respectively, with no reliable advantage from distillation. Fabricated-evidence failures rise from 5.8% under target-only prompting to 10.1% under full-history and 10.4% under imperative prompting. ProcessPrefBench highlights a tension in learning from dialogue, where drawing on prior interactions can improve preference realization yet also invite fabricated evidence. We hope it helps build assistants that honor a user's process preferences without sacrificing factual reliability.

---


### 109. [PRISM-AMC: Replay-Free Continual Learning for Automatic Modulation Classification](https://arxiv.org/abs/2611.06066)

**<font color=#1a73e8>作者：</font>** Usman Akram, Matthew Graham, Haris Vikalo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic modulation classification (AMC) is a key component of cognitive wireless systems, enabling spectrum awareness and adaptive communication. Most deep learning approaches to AMC assume a fixed set of modulation classes and access to previously observed training data. In practice, modulation classes and channel conditions may evolve over time, while storage or data-retention constraints may preclude replay of raw baseband I/Q samples. We propose PRISM-AMC, a replay-free continual learning framework that mitigates catastrophic forgetting by preserving task-relevant subspaces of intermediate representations via gradient projection memory. We further analyze projected stochastic-gradient updates under an SNR-dependent gradient-noise model. PRISM-AMC is evaluated in both class-incremental and domain-incremental settings. Experiments on the MIGOU and DeepSig 2018.01A datasets show substantially reduced forgetting relative to sequential fine-tuning and elastic weight consolidation, while remaining competitive with or outperforming replay-based RSD-AMC in class-incremental settings, without storing raw I/Q samples.

---


### 110. [Fluidic Body: Swarm Robots as a Fluid Extension of the Hand](https://arxiv.org/abs/2611.06068)

**<font color=#1a73e8>作者：</font>** Michikuni Eguchi, Shigeo Yoshida, Mai Nishimura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Swarm robots have attracted growing interest as a physical interface for human--computer interaction, since a swarm can reshape its formation to fit the objects and surroundings it works with. For a human operator, however, adapting the swarm's behavior remains difficult. Most existing methods require the user to specify where the swarm should go, and they offer no intuitive way to change the collective's behavior as each task demands. We present Fluidic Body, a system that lets a person operate a swarm of fluid-imitating robots as an extension of the hand. The system places a virtual fluid between the hand and the swarm, and the user adapts the swarm's behavior to each task by changing the fluid's properties through simple hand movements. When the user opens the hand, the swarm becomes soft enough to deform and flow around obstacles. Closing the hand turns it into a hard, cohesive body that can push objects. We evaluated the controller's performance and its operability in two simulation experiments and one demonstration with physical robots. First, our controller handled both obstacle avoidance and object transportation better than an existing method that behaves the same way in every task. Second, in a VR user study, 17 participants completed the combined avoidance-and-transportation task faster and more reliably than with that method. They also reported a lower workload and a stronger sense of agency. Finally, this experience carried over to physical robots in a real-world demonstration (88 participants). These results suggest that treating a swarm as a fluid, a material people already understand, allows a robot swarm to work as a deformable extension of the human body.

---


### 111. [RouTex: Multi-reference 3D Texture Generation by Reprogramming Rotary Position Encoding](https://arxiv.org/abs/2611.06070)

**<font color=#1a73e8>作者：</font>** Chengyang Li, Yang Liu, Jiale Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While single-image 3D texture generation has advanced significantly, conditioning texture synthesis on multi-view reference images remains largely under-explored, despite its necessity for resolving surface ambiguity in unobserved regions. In this paper, we propose RouTex, a novel multi-reference 3D texture generation framework based on in-context Diffusion Transformers (DiT). Our key insight is that native 3D Rotary Position Encoding (RoPE) inherently possesses spatial addressing capabilities. We introduce Positional Routing (PR) to reprogram 3D RoPE along spatial and semantic dimensions, establishing explicit reference-to-view correspondence without introducing additional parameters. To execute this routing efficiently, Dual-Granularity Attention (DGA) combines per-view local attention for fine texture fidelity with global joint attention over deduplicated references for cross-view consistency. Extensive experiments demonstrate that RouTex achieves new state-of-the-art performance in multi-reference 3D texture generation.

---


### 112. [Which One Is Sounding? Binaural Sounding Instance Disambiguation for Audio-Visual Segmentation](https://arxiv.org/abs/2611.06074)

**<font color=#1a73e8>作者：</font>** Haoze Ma, Yidi Li, Yu Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing audio-visual segmentation methods mainly predict sound-related regions or category masks and often fail to identify the sounding instance when multiple same-class candidates coexist. Recent audio-visual instance segmentation methods address instance-level prediction but rely largely on motion and cross-frame association, which may become unreliable under sparse observations or inconspicuous motion. To this end, we introduce binaural audio, whose interaural differences encode source-direction information, to provide spatial constraints for distinguishing the sounding instance among same-class visual candidates. We propose Binaural Sounding Instance Disambiguation for Audio-Visual Segmentation (BiSID-AVS), which progressively refines category-level candidate responses into a mask of the true sounding instance. BiSID-AVS first grounds category-consistent candidate regions through audio prompting, then projects binaural cues into an image-plane spatial response map, and finally refines the true sounding instance through dual-level spatial conditioning at the feature and decoder levels. Experiments on the binaurally extended AVS-Synthetic benchmark and Habitat-AVS dataset for robotic indoor perception show that BiSID-AVS achieves the best performance on the multi-candidate subsets, improving instance-level mIoU by 35.19 and 41.21 percentage points, respectively, while substantially reducing false activation on non-sounding same-class regions.

---


### 113. [Catastrophic Overfitting is Weight Drift the Training Loss Cannot See](https://arxiv.org/abs/2611.06082)

**<font color=#1a73e8>作者：</font>** Chao Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast adversarial training (FAT) makes robust training affordable by replacing the multi-step attack with a single-step one, but it suffers from catastrophic overfitting (CO): partway through training, robustness to multi-step attacks collapses to near zero while the single-step attack used for training keeps being repelled. We show that CO is a quiet escape of the weights. Across the event the network's clean behavior quietly improves, and moving from the weights just before CO to those just after it changes the training objective only marginally while destroying most of the robustness. The training objective is therefore nearly blind to the displacement it causes, so it exerts no force to undo it. The exponential moving average (EMA) of the weights, which FAT protocols already maintain, does not accumulate this drift and stays robust through the entire event. This observation suggests a nearly free fix: when validation robustness drops, reset the weights to their EMA. We build this guard on top of a coupling-based base method designed so that its average stays inside the robust region. The resulting training removes CO in every one of our runs and attains the strongest AutoAttack accuracy among fast methods on all three benchmark datasets, including a clear margin on CIFAR-100, where it also clears the multi-step reference at roughly half its cost. Code is available at this https URL.

---


### 114. [STARE: Scene Text-Aware multimodal Retrieval for Everyday objects](https://arxiv.org/abs/2611.06089)

**<font color=#1a73e8>作者：</font>** Kento Tokura, Ryosuke Korekata, Daichi Yashima 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, we focus on service robots that retrieve and transport everyday objects based on free-form instructions that may refer to visual features and scene text. This is challenging because it requires a multimodal understanding of the visual features and spatial relationships of objects, as well as scene text embedded in the environment. To address this, we propose Scene Text-Aware multimodal Retrieval for Everyday objects (STARE), which leverages visual and textual cues in response to free-form instructions. STARE introduces Crosslingual Visual Prompt to enhance scene text interpretation, and models the complex relationships between named entities in the instructions and their corresponding objects. We evaluate STARE using two novel benchmarks, GoGetIt and TextCaps-test, both of which consist of real-world indoor/outdoor images and instructions involving object manipulation and navigation. The results show that STARE outperforms all baseline methods on standard multimodal retrieval metrics. Furthermore, in physical experiments conducted under a zero-shot transfer setting, STARE achieves an overall success rate of 80%. Our project page and code are provided in the Supplementary Materials.

---


### 115. [Drift-adaptive Representation Preservation for Domain-Incremental Learning](https://arxiv.org/abs/2611.06093)

**<font color=#1a73e8>作者：</font>** Hyunmin Kong, Gyutae Oh, Jitae Shin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained vision models provide strong general-purpose representations, but in Domain-Incremental Learning (DIL), where the input distribution changes sequentially, adapting to new domains often degrades performance on previously learned ones. We observe that forgetting is not uniform across domains and classes and is not explained by training order alone. This motivates us to track each past domain-class concept individually. We use representation drift, defined as the deviation of a past concept's current representation from a fixed anchor, as a measurable surrogate for forgetting risk. The measured drift then serves two complementary roles. A consolidation loss assigns stronger preservation to high-drift pairs, while prototype construction down-weights highly drifted domains to reduce their influence on the class reference. Preservation is thus allocated by measured drift rather than assumed importance. To obtain this signal during training without storing past raw data, we repurpose a Joint-Embedding Predictive Architecture (JEPA). For each domain-class pair, we store only a compact context summary in the backbone feature space and rerun it through the learned context-to-target relation to measure its drift from the fixed anchor. Across DomainNet, Office-Home, CORe50, and CDDB-Hard, our method sustains a strong accuracy-forgetting balance on every benchmark, using substantially less training memory than accuracy-competitive methods and the smallest storage among compared methods.

---


### 116. [Many Pixels, One Composition: Self-Supervised Spectra for Specimen-Level Prediction](https://arxiv.org/abs/2611.06096)

**<font color=#1a73e8>作者：</font>** Eleftheria Tetoula-Tsonga, George Arvanitakis, Theodoros Giannakas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can hyperspectral (HS) imaging be used to predict the elemental composition of physical specimens found on the Earth's surface? We approach this problem as a supervised regression task, using an open dataset of specimens, each comprising a HS cube and elemental characterization. In particular, we train an encoder in a self-supervised fashion that operates on pixel-level; then freeze the encoder and train a lightweight attention-based regression head in a supervised manner, by pairing many representations of a given specimen with its corresponding elemental label. In test specimens, our approach significantly outperforms traditional spectral matching and unmixing baselines. It also outperforms supervised learning models based on the mean spectrum (of similar model capacity), while full model fine-tuning achieves the strongest performance, at substantially higher model capacity.

---


### 117. [SenTrojan: Revealing Analog Hardware Trojan Attacks on Sensors](https://arxiv.org/abs/2611.06103)

**<font color=#1a73e8>作者：</font>** Kun Wang, Ruochen Zhou, Wenjun Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sensors bridge the physical and digital worlds, making their integrity critical to cyber-physical system security. Existing sensor attacks largely exploit unintended and sensor-specific physical vulnerabilities, limiting their generalizability and motivating a different threat model, i.e., whether an adversary can implant hidden attack surfaces into sensors before deployment. In this paper, we present SenTrojan, an analog hardware Trojan framework for sensors. SenTrojan embeds malicious functionality into analog signal circuitry commonly shared across diverse sensor architectures, and activates the hidden behavior through crafted external physical signals. Once activated, SenTrojan can induce sensor malfunctions ranging from permanent denial-of-service to static or dynamic spoofing. To achieve these effects under different architectural constraints, we introduce two complementary designs. The Logic-Rule-Driven (LRD) Trojan adds lightweight analog monitoring logic to detect trigger features such as frequency and amplitude, enabling reliable activation across various sensor types. The Physical-Effect-Driven (PED) Trojan targets sensors with exploitable native analog effects, e.g., nonlinearity and rectification, and realizes attacks with minimal component insertion. We evaluate SenTrojan on 14 sensors spanning 6 transduction principles and demonstrate its effectiveness across diverse real-world scenarios. Overall, SenTrojan achieves an average successful trigger rate above 95%, maintains over 97% similarity to benign behavior, incurs zero false-trigger rate for LRD designs, and introduces less than 5% average deviation in drift, noise floor, and response time. To our knowledge, this work is the first systematic study of analog sensor Trojans, broadening sensor security from unintended physical vulnerabilities to intentional supply-chain compromise.

---


### 118. [Semantic Prior-Guided Incomplete Cross-Modal Retrieval with Noisy Labels](https://arxiv.org/abs/2611.06113)

**<font color=#1a73e8>作者：</font>** Jiali Chen, Ruitao Pu, Yingke Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal retrieval (CMR) aims to bridge the semantic gaps between modalities by learning shared representations. Unfortunately, due to the dynamism and inconsistencies in real-world data acquisition, multimodal datasets frequently encounter severe modality incompleteness. Existing incomplete CMR methods adhere to a label-driven paradigm, relying heavily on categorical annotations as the semantic benchmark. However, label noise is difficult to avoid and often coexists with modality incompleteness. To address this challenge, we propose a novel semantic prior-guided framework for incomplete cross-modal retrieval with noisy labels, termed SPIRN. Specifically, SPIRN uses fixed semantic priors as a consistent reference for robust representation learning, noisy-label handling, and missing-modality completion. Based on this reference, Semantic Priors Guidance (SPG) establishes a stable category-level semantic space, Quality-aware Robust Learning (QRL) dynamically evaluates sample quality to distinguish clean samples from noisy ones and handles noise via reverse learning, Prior-guided Global Label Calibration (PGLC) rectifies corrupted annotations for refined supervision, and Confidence-driven Selective Imputation (CSI) recovers missing modalities from a cross-modal memory bank while filtering unreliable imputations with an increasing threshold. To the best of our knowledge, this is the first framework to jointly tackle the dual challenges of modality incompleteness and label noise in the CMR community. Extensive experiments on four widely used benchmark datasets demonstrate that SPIRN outperforms 11 state-of-the-art methods in various scenarios involving both missing modalities and noisy labels.

---


### 119. [Short-Term Forecasting of Heterogeneous Wind Power Fleets: Global Temporal Fusion Transformer Leveraging Static Covariates](https://arxiv.org/abs/2611.06130)

**<font color=#1a73e8>作者：</font>** Viktor Walter, Andreas Wagner  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate short-term wind power forecasting is critical for grid stability and electricity trading. While transformer-based deep learning is state of the art, industry practice relies mostly on local models trained for individual assets. This study investigates whether a global temporal fusion transformer (TFT), trained jointly on a heterogeneous portfolio of wind farms across Germany, outperforms site-specific local models in 48-hour-ahead forecasting. Using numerical weather prediction (NWP) data from the regional ICON-D2 and the global ECMWF HRES models, we compare the global TFT against local models and a linear regression baseline. The global model leverages static covariates, such as farm age, altitude above sea level, hub height, rotor diameter and power curve parameters, to learn shared representations across sites. We evaluate on 100 synthetic wind farm profiles and a real portfolio of 11 German wind farms, across two seasonal test periods with intermediate retraining. The global TFT outperforms the local models for 87% of the synthetic and 77% of the real wind farms and clearly surpasses the linear baseline. Wilcoxon signed-rank tests confirm that these gains are significant across both seasons and datasets. Crucially, this superiority depends on static covariates: without asset-specific context, the global model fails to generalize. The TFT's variable selection network (VSN) reveals the learned feature selection. Altitude emerges as a relevant static discriminator on both datasets, while hub height is decisive on the real portfolio. For dynamic inputs, the encoder prioritizes historical power, whereas the decoder combines upper-level wind speeds from both NWP models, consistent with averaging out model-specific errors. These findings support a shift from single-site to scalable multi-site forecasting, reducing operational complexity while improving accuracy in large portfolios.

---


### 120. [Growing One's AI Tools: A Paradigm of Practice-Grown Tools](https://arxiv.org/abs/2611.06132)

**<font color=#1a73e8>作者：</font>** Zeming Zhao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Professionals have long used software built for them by others. This article reports the growth of a professional computer-assisted interpreting (CAI) tool built by its own user, a conference interpreter without programming training. Drawing on an eight-week version-controlled record with telemetry from 133 logged sessions and over 20,000 recognized utterances, the article traces how real conference work drove the tool through 62 commits and six versions. The record shows capabilities deployed on the day their need appeared and one strategy change that cut median end-to-end delay by over a third within one afternoon. The article then proposes the paradigm of practice-grown tools, defined by the shift from using to growing, the co-evolution of tool and practice through breakdown and repair, bounded local computation, and an assessment corollary, and it formulates three propositions toward tool-inclusive assessment of practitioners, from tool-making literacy to a compute-standardized format for certifying what they and their tools achieve together.

---


### 121. [RDT-3D: Resolution-Decoupled Training for High-Fidelity 3D Geometry Generation](https://arxiv.org/abs/2611.06141)

**<font color=#1a73e8>作者：</font>** Jiale Zhang, Yang Liu, Chengyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D geometry generation requires maintaining global structural coherence alongside fine-grained surface details. While recent coarse-to-fine frameworks leverage Rotary Position Embeddings (RoPE) to condition local queries, we reveal a critical training-inference resolution discrepancy: coordinate guidance and geometric supervision are aligned during training, whereas inference decodes high-resolution geometry from coarse spatial coordinates. This mismatch introduces a severe distribution shift that degrades fine details. To overcome this, we propose Resolution-Decoupled Training (RDT), which anchors RoPE guidance at 512 resolution while supervising geometry at 1536, enabling robust detail extrapolation. Additionally, to eliminate high-resolution data bottlenecks, we present Dual3D-300K, a large-scale paired dataset comprising 300K watertight 3D point clouds explicitly aligned across 512 and 1536 resolutions. Extensive experiments demonstrate that RDT substantially improves sharp geometric regions, while Dual3D-300K offers a scalable benchmark for high-resolution 3D generation.

---


### 122. [PTQ4SAM3: Semantics-Preserving Post-Training Quantization for Segment Anything Model 3](https://arxiv.org/abs/2611.06143)

**<font color=#1a73e8>作者：</font>** Xi Xiao, Yunbei Zhang, Lin Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Model 3 (SAM 3) can segment objects from text prompts and track them across video, but its memory and computation costs make deployment difficult. Post-training quantization (PTQ) reduces these costs by using fewer bits. However, a quantized model can select the wrong object or lose track of its target across frames. We call this prompt-alignment drift. Controlled tests show that perturbing low-variance feature directions strongly affects target selection. We propose Semantics-Preserving Quantization (SPQ), which gives more calibration weight to concept-sensitive parameters, preserves residual features, and corrects the mean error in video memory. Fixed text concepts guide calibration without task annotations. All three components operate offline and add no inference operators. With a W4A8 image encoder, SPQ improves RefCOCO Pr@0.5 from 42.1 to 72.5 over PTQ4SAM while retaining 54.8 COCO mask AP. Experiments on LVIS, RefCOCO variants, and SA-V show consistent gains. A CLIP study also shows improved image-text retrieval.

---


### 123. [CARM: Conformal Adaptive Risk Masking for Reliable Scientific Super-Resolution](https://arxiv.org/abs/2611.06151)

**<font color=#1a73e8>作者：</font>** Guangtao Zhang, Haonan Wu, Junxuan Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning-based super-resolution (SR) can reconstruct fine-scale Earth-observation fields from coarse observations, but reconstruction accuracy alone does not provide a calibrated rule for identifying reliable spatial regions. Conformal Mask Calibration (CMC), built on conformal risk control, converts a spatial uncertainty score into a trust mask and controls the expected worst-case local distortion under exchangeability. However, its fixed threshold can become miscalibrated in Earth-observation streams affected by seasonality and episodic events. We propose $\textit{CARM}$ (Conformal Adaptive Risk Masking), a statistical framework for adaptive spatial risk control under temporal distribution shift. CARM maintains experts with heterogeneous update rates and aggregates their threshold proposals online using an asymmetric surrogate loss, balancing rapid adaptation to distribution changes against stability during relatively stationary periods. All updates are causal and use only mature feedback available after a fixed delay, allowing CARM to operate with any SR model that provides a spatial uncertainty score. We prove that the time-averaged mask-conditioned risk converges to at most $\alpha$ at an $O(1/T)$ rate, without distributional assumptions and for any choice of aggregation weights across experts. On a daily South China Sea chlorophyll-$\textit{a}$ SR stream, CARM reduces the empirical violation rate from $43.49\%$ to $9.38\%$ and the moving-average exceedance frequency from $47.29\%$ to $1.22\%$ at $\alpha=0.10$, while retaining a non-trivial trusted region. Experiments on ERA5 wind and OSTIA sea-surface temperature further show consistent relative improvements across multiple SR backbones.

---


### 124. [Neural Stochastic Forecasting for Lateral Molecular Diffusion Simulations](https://arxiv.org/abs/2611.06157)

**<font color=#1a73e8>作者：</font>** Jacob Ede Levine, Mario Hidalgo-Soria, Chen Yun Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the long-time diffusion of membrane proteins is challenging because molecular dynamics (MD) simulations are computationally expensive, while experimental single-particle tracking is often limited by finite observation times. Here, we introduce a neural stochastic (NS) model for forecasting the collective diffusion of membrane proteins from coarse-grained MD trajectories. The model combines a transformer-based representation of protein configurations, recurrent networks operating at multiple temporal scales, and a stochastic latent process with learned memory. A cross-attention decoder then generates correlated protein displacements while accounting for the instantaneous system geometry and periodic boundary conditions. We evaluate the model in two membrane systems: seven interacting PIEZO channels and a mixed system containing seven PIEZO and ten TREK channels. For the seven PIEZO system, the NS model reproduces the anomalous diffusion exponent measured in MD simulations $\alpha \sim 1$, substantially improving on a previously developed variational autoregressive model that exhibits superdiffusive behavior. The model also generates trajectories extending to 40,000 frames and captures the distinct diffusion characteristics of PIEZO and TREK populations in the mixed system. Comparisons of time-averaged mean-square displacements, Van Hove displacement distributions, and non-Gaussian parameters show that the model preserves key statistical features of the simulated dynamics. These results establish neural stochastic modeling as a promising approach for generating long trajectories of multi-protein membrane diffusion and extending the statistical analysis of molecular dynamics simulations.

---


### 125. [Selective Prediction Intervals: Jointly Learning to Predict, Bound, and Abstain](https://arxiv.org/abs/2611.06158)

**<font color=#1a73e8>作者：</font>** Lidor Rubi, Gilad Katz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many high-stakes regression decisions ask three things of a model at once: a point estimate to act on, an interval that bounds the risk of acting, and the option to abstain when neither can be trusted. Deep learning provides these in isolation: prediction-interval methods return an interval, and at best a value estimate inside it, for every input, while selective-prediction methods learn when to abstain, but only for point predictions and with no statement of how far the truth may lie from the estimate. We introduce SelPI, which trains interval, value and abstention heads jointly under a single loss with an explicit acceptance-rate budget. A natural objection is that interval width already tells us when to abstain. We show that it does not: across 18 tabular benchmarks, width predicts large point errors well (AUROC 0.72) but is anti-correlated with interval misses (AUROC 0.38), so abstaining on wide intervals discards precisely the inputs the interval got right. SelPI therefore selects with two gates, one trained on the interval loss and one on the value loss, coupled by a Fr'echet penalty that ties their separate budgets to the joint acceptance rate they deliver. With the base predictor held fixed, the learned gate beats width thresholding on a proper interval score on all 18 tabular datasets, closing a median 87% of the gap to an oracle selector, and it also beats selection by deep-ensemble disagreement on every dataset. The advantage grows with the heteroscedasticity of the task, and we report the settings in which it disappears.

---


### 126. [FaCoDiff: Factor-Correlated Diffusion for Multivariate Probabilistic Forecasting](https://arxiv.org/abs/2611.06166)

**<font color=#1a73e8>作者：</font>** Jiaxuan Li, Yao Liu, Yuewei Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate probabilistic forecasting requires modeling cross-variable dependence alongside marginal uncertainty. The challenge is to learn this dependence while controlling marginal noise scales and avoiding dense covariance costs. We propose Factor-Correlated Diffusion (FaCoDiff), which couples a compact conditional statistical estimator with structured denoising. History-conditioned factor loadings use distinct coefficients for forecast-center correction, scale adjustment and noise dependence. Diagonal compensation preserves the estimated marginal noise variances, while low-rank operators enable residual Gaussian likelihood evaluation and noise transport without dense covariance storage or factorization. Factor-derived feature modulation explicitly conditions the denoiser, and a geometry-aware objective accounts for errors after noise transport. The same conditional geometry governs forward perturbations and reverse sampling. Across nine datasets, FaCoDiff achieves the lowest mean variogram score on eight datasets and ranks among the top two on 43 of 54 dataset-metric combinations in the reported comparisons. Matched ablations on Solar and Weather show that factor covariance improves mean Energy and Variogram scores under all four combinations of center and scale correction. Disrupting cross-variable sample pairings while preserving marginal trajectories worsens joint and aggregate scores on both datasets, demonstrating the predictive value of generated cross-variable dependence.

---


### 127. [Network Intrusion Forensic Detection System with Explainable Artificial Intelligence and Digital Chain of Custody](https://arxiv.org/abs/2611.06173)

**<font color=#1a73e8>作者：</font>** Jose Luis Vela Alonso, Carmen Pellicer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying an explainable intrusion detection model from a validated laboratory setting into a forensic workflow requires guarantees that benchmarks do not test: that the certified model is the exact artifact applied to a case, that heterogeneous evidence can be classified reliably, and that every step is verifiable. We present MODEXRE, a forensic pipeline that extends a previously validated synthetic-data-trained XGBoost classifier with SHAP explainability (arXiv:2607.00763) into a dual-mode architecture: a Laboratory mode, where models are trained and certified on public and synthetic data, and a Formal mode, where a frozen, hash-verified model performs inference on case evidence under a SHA-256 hash-chained chain of custody. Suricata alerts, CEF firewall logs and packet captures are normalized through OCSF. Four design decisions, each triggered by an observed failure, shaped the architecture: a timestamp leak that inflated Kitsune performance (F1-macro 0.984, 0.662 after correction); a feature-coverage gap that made the 78-feature reference model misclassify a real SSH alert; causal temporal flow aggregation, which raised Kitsune multiclass F1-macro from 0.394 to 0.932; and a certification defect, exposed only by a real packet capture, whereby the pipeline had always trained a binary classifier. After correction, the same capture went from 100% of events flagged as malicious to 87% classified as Normal, with the scanning host identified as Reconnaissance. The default four-class certified model reaches F1-macro = 0.9538 on CICIDS2017-derived evidence; the recertified 18-category model reaches 0.6214, reflecting the real multiclass task. Chain-of-custody verification, model integrity hashing and per-prediction SHAP explanations are reported as measured outcomes.

---


### 128. [Rohbau3D-Semantics: Dense Semantic and Instance Labels for Point Clouds of Indoor Shell Construction Scenes](https://arxiv.org/abs/2611.06180)

**<font color=#1a73e8>作者：</font>** Lukas Rauch, Thomas Braml  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the Rohbau3D-Semantics dataset, which adds dense semantic and instance-level labels to laser scans of the previously released Rohbau3D domain data from shell construction sites. The dataset comprises 504 point cloud scenes from 14 survey sites, each captured with a terrestrial laser scanner and stored in a scanner-centered local coordinate system. Unlike point clouds sampled from reconstructed meshes or synthetic building models, the data preserve the characteristic properties of real laser scanning, including non-uniform sampling, measurement artifacts, reflections, and fine geometric detail. Combined with manual labels, expert oversight during pointwise annotation, and full-scene review, this yields a high-quality benchmark for semantic scene understanding in complex built environments. The dataset includes 17 class labels of building components and one background class, along with instance annotations for object-level analysis. In addition to the 3D point clouds, the release also provides scripts for deriving geometrically aligned panoramic and cube-map representations of color, LiDAR reflection intensity, depth, surface normals, semantic labels, and instance labels from the 3D arrays. We describe the acquisition pipeline, annotation protocol, quality-control process, and panorama-generation procedure, and provide benchmark splits and baseline experiments for semantic segmentation. By combining precise terrestrial laser scans, dense annotations, and a wide variety of shell-construction scenes, Rohbau3D-Semantics bridges the gap among synthetic indoor datasets, mesh-derived benchmarks, and smaller construction-specific resources. The dataset is intended to support research on 3D scene understanding, construction-site analytics, and multimodal scene analysis in the built environment.
Access and download the full dataset via this https URL

---


### 129. [ProGram: A Grammar for Progressive Computation Pipelines](https://arxiv.org/abs/2611.06188)

**<font color=#1a73e8>作者：</font>** Seunghoon Jung, Jaemin Jo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Progressive Visual Analytics (PVA) systems have demonstrated the effectiveness of time-bounded, incremental computation for exploring large-scale data. However, our survey reveals that existing PVA implementations are often difficult to reuse and extend, as their progressive behaviors are typically realized through ad hoc, hard-coded mechanisms distributed across servers and clients. To address this limitation, we present ProGram, a grammar for progressive computation pipelines. Informed by a comprehensive analysis of prior concepts and design practices in existing PVA systems, ProGram is designed to support core progressive features while reducing implementation burden. Furthermore, we extend the design space by introducing novel mechanisms, such as lockstepping, forking, and temporary prioritization, to better support diverse usage scenarios. Finally, we demonstrate the expressiveness and coverage of ProGram by reproducing and extending existing progressive visualization systems, presenting a gallery of progressive computation pipelines, and discussing the grammar coverage.

---


### 130. [GPUMAP: GPU-Accelerated Progressive Uniform Manifold Approximation and Projection](https://arxiv.org/abs/2611.06191)

**<font color=#1a73e8>作者：</font>** Myeongwon Jung, Jaemin Jo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensionality reduction (DR) techniques are fundamental to the analysis of high-dimensional data, yet their substantial computational cost limits their use in interactive settings. To address this limitation, we present GPU-accelerated Progressive Uniform Manifold Approximation and Projection (GPUMAP), an efficient progressive DR algorithm designed for interactive use. We identify three atomic operations within UMAP and restructure them into a progressive pipeline. As part of this adaptation, we introduce modifications to UMAP, including operation queues, instance-wise local join, and scheduling strategies. We further accelerate computation by leveraging GPU parallelism, enabling interactive analysis of million-scale datasets on commodity GPU hardware. Finally, we employ our implementation to systematically study the behavior of progressive DR, investigating how projections evolve over time relative to the ground-truth projection and how biased data streams influence the quality and stability of the resulting projections.

---


### 131. [Cross-Asset Knowledge Transfer for Early Fault Detection of Data-Scarce Assets Without Target Fault Data](https://arxiv.org/abs/2611.06194)

**<font color=#1a73e8>作者：</font>** Zekai Wang, Yuxuan Li, Zhangyue Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliability management of industrial fleets depends on early fault warnings, yet lifecycle data across similar assets are highly imbalanced. A few assets accumulate run-to-failure histories, while newly installed or rarely failing assets provide only normal-condition data. This paper asks how diagnostic knowledge can be transferred from a data-rich source asset to a data-scarce target asset when no fault data have been observed on the target. We formulate cross-asset early fault detection as a zero-shot domain adaptation problem, in which zero-shot refers to the absence of target fault samples, and propose a framework that requires only normal data from the target. The framework comprises (1) a statistical process control step that labels the source asset run-to-failure data with an exponentially weighted moving average chart, reducing manual annotation to verifying flagged segments, (2) an Adapted Domain-Adversarial Neural Network (ADANN) that combines domain-adversarial training and a Maximum Mean Discrepancy penalty with an Adapted Classification-Domain (ACD) loss, which anchors the classifier normal region to the target own normal data, and (3) an ahead-of-time labeling scheme with a prediction horizon that targets incipient faults. Under an exact-classification assumption, a theoretical analysis characterizes the domain-adversarial term for a normal-only target and the alignment state in which source fault features remain separated from target normal features. On a public run-to-failure bearing dataset, ADANN attains the highest mean F1-score among four transfer baselines, with a nominally significant precision gain over the strongest baseline, and its robustness is examined under synthetic noise.

---


### 132. [BiCG-Net: Target-Specific Image Quality Assessment via Observation Modeling and In-Image Differencing](https://arxiv.org/abs/2611.06203)

**<font color=#1a73e8>作者：</font>** Yibu Yang, Tingqiong Cui, Liming Lei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We estimate the quality of a specific target region (e.g., a train body) in an image, rather than the whole image. This differs fundamentally from whole-image No-Reference Image Quality Assessment (NR-IQA): when the target occupies a small fraction of the frame, the whole-image score is dominated by background, and no public benchmark provides target-level human Mean Opinion Score (MOS). We estimate target quality via nested sampling - a sequence of patches expanding outward from the target box - and infer quality from the relative structure of this sequence.
This motivates BiCG-Net, a student network that distills an 11-teacher ensemble through a linear observation model and an in-image differencing mechanism, which provably cancels the target term and teacher-specific bias. We train and test the student independently on each dataset, and evaluate zero-shot transfer across benchmarks. On CSIQ and LIVEC, the student reaches PLCCs of 0.9009 and 0.9133 against human MOS, exceeding the best single teacher and the teacher consensus. On a self-built MOS-free railway dataset, the student reaches a PLCC of 0.9855 against a weak label.
The student exceeds its teachers because it learns a new mapping from the relative structure of teacher readings to the ground-truth label, rather than mimicking them. Residual analysis on CSIQ and LIVEC shows the prediction residual is significantly correlated with background contamination, teacher dispersion, and label extremity, demonstrating the student extracts information the consensus does not contain. Under CSIQ-to-LIVEC transfer, the frozen student reaches a PLCC of 0.8416, exceeding the consensus by 0.1947. We position BiCG-Net as an offline target-level quality auditing and label-generation engine; its 39,482-parameter student is compact by design, acting as a unifying layer mapping heterogeneous teacher readings onto a common quality scale.

---


### 133. [Loop Before You Leap: What Recurrent Depth Can and Cannot Buy in Data-Limited Pretraining](https://arxiv.org/abs/2611.06206)

**<font color=#1a73e8>作者：</font>** Daichi Hotta, Yohei Kobashi, Takeshi Kojima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal models have often scored below text-only baselines in the BabyLM Challenge (Klerings et al., 2024; Takmaz et al., 2025). We test whether additional recurrent computation helps close this gap. Recurrence increases computation by reusing layers without adding parameters or training data. Using a single implementation, we compare standard and looped Transformers under a 100M-word budget, with three seeds per main condition. Each image is represented by one feature vector from a frozen DINOv2 encoder, used as a prefix token. Caption words count toward the budget, so multimodal training also changes the language data. In a pre-registered text-only comparison, a 12-layer stack repeated four times exceeds a standard 48-layer Transformer by 5.4 BLiMP percentage points at matched inference compute. However, multimodal training lowers BLiMP accuracy by about 3.8 points in both architectures, with no clear mitigation from recurrence. An exploratory loop-side no-image control, trained with the multimodal language data and batching schedule, scores 5.7 points below the text-only baseline. Adding the visual prefix raises accuracy by 1.85 points on average, but this contrast is uncertain with three seeds. These results suggest that changes in language data and its presentation are a major source of the drop. Diagnostic tests show that the models use visual information; its contribution to grammatical generalization remains uncertain under this single-vector interface.

---


### 134. [A Definition of Catastrophic Performance](https://arxiv.org/abs/2611.06219)

**<font color=#1a73e8>作者：</font>** Henrik Marklund, Alex Infanger, Benjamin Van Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A central challenge in AI is specifying objectives that align with human preferences. While existing theoretical results elucidate how misspecification impacts performance, they typically do not distinguish between merely suboptimal and catastrophic outcomes. To enable rigorous analysis of catastrophic risk from AI misalignment, we introduce a formal definition of catastrophic performance. Our definition is based on two reference values. The first, baseline value, captures the value attained if no agent is deployed. The second, orthogonal value, captures the value of a trajectory that is unrelated to human preferences, in a sense we describe. Orthogonal value is typically far worse than baseline value. We interpret these reference values through examples in which past human activity has altered the state of the environment to human benefit. Starting at the resulting state, an AI agent is deployed with the goal of accelerating further progress. Catastrophic performance represents this agent's undoing of benefits afforded by human activity.

---


### 135. [FedXCrop: Privacy-Preserving Crop Disease Detection via Federated Learning with Post-Aggregation Explainability under Non-IID Farm Distributions](https://arxiv.org/abs/2611.06221)

**<font color=#1a73e8>作者：</font>** Kriti Saini, Manikandan P  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning can classify crop diseases accurately from benchmark leaf images, but centralized training requires farms to share raw data, and predictions without explanations offer limited support for treatment decisions. We present FedXCrop, a federated crop disease classification pipeline that quantitatively evaluates explanations of the aggregated global model. A MobileNetV2 model trained centrally on PlantVillage achieved 99.38% test accuracy (standard deviation 0.05 over three seeds) on a fixed test set of 5,428 images across 38 classes. Federated models initialized with ImageNet weights were trained for 30 rounds across five clients. FedAvg achieved 98.81% accuracy with identically distributed clients and 98.81%, 98.59%, and 97.78% under Dirichlet label skew (alpha = 1, 0.5, and 0.1, respectively). FedProx was not significantly different from FedAvg at any heterogeneity level (McNemar p > 0.3). Grad-CAM and SmoothGrad explanations were evaluated on 380 test images. Both attributed more energy to the leaf than chance (0.70-0.78 versus 0.60), while Grad-CAM maps from federated and centralized models showed Spearman correlations of 0.74-0.76. Agreement decreased as heterogeneity increased, lesion localization was only modestly above chance, and a model-randomization test indicated that SmoothGrad maps depended substantially on image structure rather than learned parameters. In this setting, label skew reduced federated accuracy by 0.6-1.6 percentage points relative to centralized training. FedAvg largely preserved Grad-CAM behavior, while FedProx provided no measurable benefit.

---


### 136. [Explainable Anomaly Detection in 5G Networks through Continuous Time Graphs](https://arxiv.org/abs/2611.06225)

**<font color=#1a73e8>作者：</font>** Thomas Hoger, Philippe Owezarski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> 5G networks increasingly resemble distributed systems in their design. It then becomes crucial to move beyond traditional network-based detection methods and to explore alternative approaches. In this work, we propose a formalization of 5G network exchanges as a dynamic graph, on which we apply techniques from the field of graph-based learning to detect anomalies effectively. This representation allows for fine-grained analysis of packet-level semantic content, while simultaneously capturing sequential and topological contexts, both of which are essential for identifying sophisticated and multi-stage attacks. To assess the effectiveness of this formalism, we evaluate it with the most popular dynamic graph models, demonstrating its potential for 5G anomaly detection.

---


### 137. [Understanding the Perception of Transliterated Offensive Social Media Posts Among Banglish and Hinglish Users](https://arxiv.org/abs/2611.06226)

**<font color=#1a73e8>作者：</font>** Dhiman Goswami, Zhicong Lu, Sanchari Das  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective content moderation depends on understanding not just what harmful content looks like, but how users perceive and respond to it. When offensive language is written in transliterated forms such as Banglish or Hinglish (Bangla or Hindi in Latin script), it may be interpreted very differently than in native scripts, with direct consequences for whether users report, ignore, or recognize it as harmful. Yet little is known about how script choice relates to user perception, or how these perceptions vary across demographic groups. To investigate these perceptions, we conducted a user study with $310$ participants ($193$ Hindi, $60$ Bangla, $57$ Bangla-Hindi bilingual speakers) who evaluated offensive posts in native scripts and transliterations. Participants provided offensiveness scores ($4.03$ for Banglish, $3.86$ for Hinglish) to transliterated posts, yet reporting fell from $20.9\%$ (native - Bangla, Hindi) to $18.2\%$ (transliterated - Banglish, Hinglish). Ignoring remained the dominant response (range $25.38\%-44\%$ overall). Women reported at higher probability than men for native-script ($23.6\%$ vs. $17.7\%$) and showed almost identical reporting probability in comparison to men for transliterated posts ($17.5\%$ vs. $17.9\%$), and younger participants ($<40$) rated Banglish content as more offensive than older participants ($\geq 40$), (Overall offensive score: $3.99$ vs. $3.78$). These findings identify transliteration as critical blind spot for moderation, underscoring the need for linguistically sensitive approaches to online safety.

---


### 138. [Separation Is a Riesz Energy: How Many Environments Does ICA Need?](https://arxiv.org/abs/2611.06228)

**<font color=#1a73e8>作者：</font>** Yuda Bi, Yubo Guo, Jiaxiao Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can independent components be recovered when all of them are Gaussian? Yes, if their variances change across environments; but how many environments, and how many samples as the number of components $d$ grows? We answer both for the joint diagonalization of $K$ covariances. Each component has a signature, its variances across the environments. Separating component $j$ costs the Riesz 2-energy $E_j$ of this signature, a sum, over the other components, of inverse pairwise Fisher informations. For Gaussian sources no estimator in $O(d)$ beats $cE_j/(n+E_j)$ at any $n$ and $d$, and above an explicit sample size a spectral estimator attains $E_j/n$ up to a constant, for every mixing and without the signatures (given a lower bound on the pairwise information). Since signatures live in $K-1$ dimensions, the rate obeys a dimension law: $d^2/n$, $d\log d/n$ and $d/n$ for $K=2$, $3$ and $K\ge4$ well-spread environments. What counts is the dimension the signatures span, not their number, and $\log d$ well-designed environments make $d\log d$ samples suffice. Projecting the covariances onto one linear combination pays $d^2/n$ at first order instead. In simulations up to $d=1000$ the predictions hold and joint diagonalization with $K\ge4$ attains the rate once $n/d$ is in the hundreds; on task fMRI the energy says which components are hard to separate.

---


### 139. [Homology Features for X-Ray Hyperspectral Images Segmentation](https://arxiv.org/abs/2611.06230)

**<font color=#1a73e8>作者：</font>** Fethi Harkat, Guillaume Gey, Valérie Perrier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characterizing Multi-Energy X-ray Transmission (XRT) hyperspectral images presents significant challenges for traditional classification frameworks due to high-dimensional redundancy and non-linear spectral overlaps. Although manifold learning techniques such as UMAP enhance spectral representation by preserving non-linear correlations, they do not explicitly utilize the geometric structure of the embedded manifold for segmentation. This study introduces a hybrid architecture that integrates topological features derived from persistent homology with convolutional and graph neural networks. The approach computes Vietoris-Rips persistent homology on UMAP-projected superpixel point clouds to capture H 1 cyclic structures that encode spectral heterogeneity. These topological descriptors are combined with pixel-level CNN features through a broadcasting mechanism that propagates superpixel-level graph representations to full spatial resolution. Experimental results on XRT multi-energy imagery demonstrate that the proposed hybrid model significantly outperforms both CNN-only and superpixel-pooling fusion baselines, suggesting that topological features provide complementary discriminative information to local spectralspatial descriptors.

---


### 140. [Zuse: A Decision Model for European Languages](https://arxiv.org/abs/2611.06238)

**<font color=#1a73e8>作者：</font>** Umair Mehmood Imam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models read a document and return a probability for each of a fixed set of options instead of generating text. Several appeared in 2026, but none has published results outside English. We describe Zuse, three decision models (4B, 9B and 27B) that train a low-rank adapter and a pointer head on frozen open-weight bases, targeting 27 European languages, and use them to study how this design behaves across languages and tasks. On a broad European suite of 11 sources excluded from training, covering 9 task groups and 27 languages, a development set that also guided model selection, the 27B model reaches 87.5% accuracy with a pooled expected calibration error of 0.016, and 0.035 when weighted per source. Post-hoc analyses of these single-seed results give three findings. First, miscalibration is structured by task rather than language: on parallel reading and topic items in 26 languages the confidence gap varies about as much as sampling noise, while across sources it spans -0.07 to +0.09, with knowledge tasks overconfident and acceptability judgements underconfident at all three sizes, so one fitted temperature cannot correct both. Second, the share of decisions that can be automated at a 5% error budget follows chance-corrected skill (Spearman 0.97 over 33 source and model pairs) more closely than raw accuracy (0.91). Third, reach beyond the training languages is set by the base model: across 210 languages, changing the training run moved scores by at most about 2 points within a size, while languages outside the base's documented list trail by 23 to 28 points at every size. On English public suites Zuse is behind Jev and Kev, including Kev models on the same bases. We also report two pitfalls in building multi-source training data: label-word collision between topic schemes, and an injection augmentation that taught a shortcut. Zuse can be tried at this https URL.

---


### 141. [Rubric Curriculum RL: Exploiting the Generation-Verification Gap in Non-Verifiable Domains](https://arxiv.org/abs/2611.06244)

**<font color=#1a73e8>作者：</font>** Sumeet Ramesh Motwani, Tejas Krishnan, Alistair Letcher 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has led to significant gains in math and code generation. Extending these gains to open-ended domains remains challenging: ground-truth verification is unavailable, human annotation is expensive, and learned reward models are prone to reward hacking. The generation-verification gap, where judging good outputs is easier than producing them, offers a potential path to improvement. However, rubric-based judges are often imprecise and stationary, so policies can overfit or reward hack them. We introduce Rubric Curriculum RL (RcRL), which exploits this gap without new data, human annotations, or stronger teacher models. We combine pairwise preferences over rollouts with a curriculum over rubric criteria, yielding a more discriminative signal than absolute scoring and a non-stationary objective. Whereas baselines plateau within a few hundred steps, RcRL preserves output entropy and keeps improving past 1000 steps. On creative writing, RcRL achieves a 70.5% human win rate against the base model, with gains across benchmarks and judges. On HealthBench, RcRL improves over the base model by 14.6% (full set) and 25.4% (consensus subset), outperforming all training baselines, including instance-specific rubrics.

---


### 142. [CAPE-JEPA - Cross-modal Adversarial Probabilistic Embedding JEPA](https://arxiv.org/abs/2611.06247)

**<font color=#1a73e8>作者：</font>** Aniket Junghare, Biplab Banerjee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal remote sensing image retrieval (RS-CMIR) requires representations that are simultaneously modality-invariant and semantically discriminative, despite the profound physical gap between heterogeneous sensors such as Synthetic Aperture Radar (SAR) and multispectral imagery. Recent JEPA-based Predictive self-supervised approaches such as X-JEPA formulate cross-modal alignment as a deterministic latent forecasting task, implicitly assuming uniform patch predictability and leaving cross-modal distributional alignment unaddressed. We propose CAPE-JEPA, a probabilistic cross-modal Joint Embedding Predictive Architecture with three contributions: (i) a cross-attentional Gaussian predictor outputting per-patch parameters (mu, sigma^2) conditioned on opposite-modality context, trained via negative log-likelihood to model inherent cross-sensor prediction uncertainty; (ii) adversarial distributional regularization combining unimodal isotropic Gaussian regularization with a novel cross-modal adversarial variant that aligns modality distributions via worst-case Epps-Pulley characteristic function tests without explicit sample pairing; and (iii) in-training contrastive learning with attention-pooled heads for scene-level discriminative grounding. Evaluated on BigEarthNet-14K (BEN-14K) and fMoW across SAR, multispectral, and RGB modalities, CAPE-JEPA surpasses X-JEPA by up to 13.74 points on BEN-14K and 15.59 points on fMoW, outperforming all baselines including SkySense and CROMA across both unimodal and cross-modal directions while using fewer parameters (407.30M vs. 432.72M).

---


### 143. [CrossPressor: Scalable Cross-View Fusion for Feed-Forward 3D Gaussian Splatting](https://arxiv.org/abs/2611.06258)

**<font color=#1a73e8>作者：</font>** Yuxi Hu, Wenhao Dong, Jun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3D-GS) becomes increasingly difficult to scale to long multi-view sequences. Anchor-based compression methods such as ZPressor alleviate representation growth by decoding Gaussians only from a compact set of anchor feature maps, but keeping these anchors fixed forces each one to aggregate an increasing number of support views. We identify this representation--fusion mismatch and introduce \textbf{CrossPressor}, a training-free method for scalable anchor-based fusion. CrossPressor preserves all decoder-facing anchor queries while constraining the view-growing support sequence through coverage-cycled evidence routing, distributing retained spatial evidence across support views and fusion layers while keeping all support views represented. Routing before K/V projection, together with joint context packing, further reduces support-side fusion cost without retraining. CrossPressor maintains reconstruction quality close to dense fusion while achieving up to $26.12\times$ faster cross-view fusion and $1.43\times$ end-to-end acceleration on long input sequences. Our project page is at: this https URL.

---


### 144. [Learning Pseudo-Riemannian Manifolds for Heterophilic Graphs via Graph Signature](https://arxiv.org/abs/2611.06265)

**<font color=#1a73e8>作者：</font>** Yun Young Choi, Asung Kil, Sun Woo Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several widely used families of Graph Neural Networks carry a positive-definite geometric prior. Graph convolution read as heat diffusion needs a positive semi-definite operator, hyperbolic models place features on positive-definite Riemannian manifolds, and dot-product and GAT-style attention scores use positive-definite inner products. On heterophilic graphs, where edges often signify dissimilarity or structural repulsion, that prior is a mismatch: no positive-definite form can assign a negative squared distance to a direction the labels separate. To measure the mismatch, we introduce the Graph Signature Index ($s_{\mathcal{G}}$), the inertia of a class-compatibility matrix built from label topology alone, and we prove that no value of the edge or node homophily index in $(0,1)$ rules out a negative eigenvalue. We then propose the Pseudo-Riemannian Attention Network (PRAT), whose attention logit is a signed squared pseudo-distance under a learnable diagonal metric initialized from $s_{\mathcal{G}}$. The design is diagnose-then-learn: the signature supplies a sign structure that unconstrained training keeps outside near-zero directions, and the projection learns the rest of the metric around it. Across fifteen node-classification benchmarks PRAT outperforms or matches the strongest heterophily-adapted models. A controlled ablation ties that performance to the sign structure itself: with architecture and protocol fixed, forbidding the metric to be indefinite costs accuracy on the graphs $s_{\mathcal{G}}$ marks as indefinite and leaves the others unchanged.

---


### 145. [Beyond Identity Creation: Bilinear Sybil Cost in Identities and Time](https://arxiv.org/abs/2611.06268)

**<font color=#1a73e8>作者：</font>** Homayoun Maleki, Nekane Sainz, Jon Legarda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sybil defenses price the creation of an identity, yet influence goes, again and again, to active identities. We study the cost of maintaining influence. A defense has a bilinear Sybil cost with ratio $A$ if keeping $s$ identities active for $T$ periods costs at least $sT/A$ honest units: the average cost per identity-window is at least $1/A$ times an honest participant's cost. Recurrence alone does not guarantee this cost. The cost can be carried over from earlier periods, shared among many identities, or be negligible when fast hardware does the work of thousands of honest devices. We give four sufficient conditions for a defense that checks every identity each period to achieve bilinear Sybil cost: identity binding, freshness, a shared deadline, and sequential, non-batchable work. They yield two guarantees: a bilinear total cost, with $A$ the speed advantage of the adversary's fastest hardware, and, because the work must be fresh and finished by a common deadline, a bound on the identities active in a period by the processors running at that time. We prove that none of the four follows from the other three. A verifiable delay function on an identity-bound input meets all four without payments, with $A$ of 2 to 8 for CPUs and about 28 for a hypothetical ASIC, against $10^3$ to $10^7$ for hash puzzles. We measure one active identity per core per period against about 80,000 under a signed heartbeat, no gain from batching up to 1,000 identities, and rejection of all tested attacks.

---


### 146. [NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation](https://arxiv.org/abs/2611.06270)

**<font color=#1a73e8>作者：</font>** Xinhao Lou, Dongye Xie, Peng Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial training enables one- and few-step image and video generation, but conventional adversarial losses supervise critic values without directly specifying the gradients used to update the generator. We present NEXTGAN, which trains a scalar critic by regressing its input gradient onto displacements between independently paired reference and generated features at interpolated locations in frozen representation spaces. For a fixed generator, this regression is equivalent to an adversarial objective with a gradient-energy penalty, while the generator retains the standard potential-based GAN update. The same objective adapts pre-trained image and video generators with up to 14B parameters, without auxiliary losses, online teacher scores, or trajectories. On ImageNet $256 \times 256$, NEXTGAN achieves one-step FIDs of 2.87 with pixel-space JiT-B and 1.54 with latent-space DiT-XL/1; its adversarial form further reaches 1.36. For text-to-video generation, a single trained Wan2.1-1.3B model supports one-, two-, and four-step sampling, achieving the highest VBench total scores among the compared 1.3B methods at one and two steps. At two steps, NEXTGAN scores 83.13, exceeding rCM and AnyFlow by 1.25 and 0.47 points, respectively. Code is available at this https URL.

---


### 147. [Consistency Learning and Distillation for One-Step MIMO-OFDM Channel Estimation](https://arxiv.org/abs/2611.06271)

**<font color=#1a73e8>作者：</font>** Fredrik Nguyen, Qiwen Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative neural channel estimators can improve recovery under pilot contamination, but repeated network evaluations increase inference cost. This paper develops observation-anchored consistency and Consistency Mid-Training (CMT) estimators for one-step channel estimation in multiple-input multiple-output orthogonal frequency-division multiplexing (MIMO-OFDM) systems. Both estimators refine pilot-derived least-squares channel estimates in the delay-beam domain. Consistency learning couples endpoint predictions along noisy-to-clean paths. CMT then refines a compact consistency-trained student to predict a flow-matching teacher's endpoint from intermediate trajectory states. Across the evaluated SNR range, the compact CMT student reduces uncoded symbol error rate (SER) by 9.6-20.2% relative to the one-step flow-matching baseline (0.44-0.98 dB in logarithmic SER reduction), while using 74.5% fewer parameters and 73.0% fewer network multiply-accumulates.

---


### 148. [Quo Vadis, Driving Scene Reconstruction? Occlusion-Aware Gaussian Densification](https://arxiv.org/abs/2611.06273)

**<font color=#1a73e8>作者：</font>** Dung Do Tien, Kien Nguyen Do Trung, Kiet Dang Vu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent feed-forward 3D Gaussian Splatting methods enable efficient driving-scene reconstruction from surround-view images, their reliance on a single observation fundamentally hinders novel-view synthesis. Regions occluded in the input can become visible from novel viewpoints, leaving the reconstructed Gaussians under-constrained and incomplete. Moving beyond image-space inpainting for rendered views, we introduce OccSplat, a feed-forward framework whose core contribution is Occlusion-Aware Gaussian Densification, explicitly targeting missing scene geometry rather than missing pixels. By predicting new Gaussian primitives for unsupported regions, OccSplat completes the scene directly in the 3D representation. Specifically, OccSplat first identifies occluded regions that lack Gaussian support through Gaussian Occlusion Mapping. Gaussian Occlusion Completion then generates new primitives for these regions. The predicted primitives are integrated into the original representation to improve novel-view synthesis while retaining feed-forward inference without per-scene optimization. Experiments on the nuScenes benchmark demonstrate that OccSplat improves on the compared methods and yields particularly large gains in occluded regions, leading to more accurate and visually coherent driving-scene reconstruction.

---


### 149. [DyPSI: Dynamic Physics Sensing via Joint Field and Sensor-Trajectory Generation](https://arxiv.org/abs/2611.06280)

**<font color=#1a73e8>作者：</font>** Yizhou Zhang, Panqi Chen, Lei Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics sensing in evolving environments requires reconstructing dense spatiotemporal fields from sparse observations while adapting where future observations should be collected. Existing reconstruction and sensor-placement methods have made substantial progress, but they typically rely on static sensing assumptions: they either use a single layout across all frames or optimize placements independently at each frame, which limits their ability to produce temporally coherent sensing trajectories. We introduce DyPSI, a dynamic physics sensing framework that formulates this problem as the joint generation of future fields and sensor trajectories conditioned on historical observations. DyPSI lifts discrete sensor coordinates into continuous Sensor Position Fields, encodes fields and sensing configurations with a shared Functional Tucker representation, and trains a joint diffusion model to generate future fields and sensing trajectories simultaneously in the resulting latent space. A Gaussian-process temporal kernel correlates the perturbation injected during diffusion training, biasing the denoiser toward temporally smooth recoveries, and we further provide an analysis linking the EDM training objective to a sequence-aggregated A-optimality criterion and a kernel-induced bound on discrete trajectory variation. Experiments on turbulent flow, GLORYS12 sea-surface temperature, and 3D car aerodynamics show that DyPSI consistently outperforms static and frame-wise placement strategies, with substantial error reduction under tight sensor budgets. The code is available at this https URL.

---


### 150. [Clear Human Web: Where a Person Vouches for Every Client](https://arxiv.org/abs/2611.06286)

**<font color=#1a73e8>作者：</font>** Lorenzo Porcelli  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The web cannot tell whether a request comes from a person or from a program. Sites have checked the network address and puzzles in its place, and both have given way: automated traffic exceeds human traffic, and puzzles are solved for pay and by agents. This paper proposes the Clear Human Web, the part of the public web that sites open only to clients a person vouches for. A person's wallet presents their person identification data (PID) to one issuer, the only party that registers as a relying party, and receives a bounded number of blind-signed tokens, proofs of personhood that carry no attribute. The browser spends one token at each site that runs the gate, and the site learns that a valid token of a trusted issuer was spent, and nothing else. No field is added to the PID, no protocol is introduced, no site registers, and the publisher of a site holds the same proof as its readers. We define the Clear Human Web through five properties and seven adversaries, and state which properties the construction satisfies against each adversary. The identities a person can hold on one site in an epoch are bounded to k. The bound holds once the wallet limits a person to one pseudonym at the issuer. In the optimum k = 1, and a zero-knowledge proof of PID possession and a pseudonym per site replace the tokens.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
