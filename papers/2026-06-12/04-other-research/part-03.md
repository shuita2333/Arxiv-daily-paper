# 📦 其他研究 | 2026年06月12日

> 本类共 **248** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-248](./part-05.md)

---

### 101. [Runtime Skill Audit: Targeted Runtime Probing for Agent Skill Security](https://arxiv.org/abs/2606.11671)

**<font color=#1a73e8>作者：</font>** Tu Lan, Chaowei Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills let LLM agents reuse instructions, resources, tools, and workflows, but they also create a new place for malicious behavior to hide. A skill may look benign in its documentation or code while becoming harmful only when it is invoked with particular user requests, local assets, persistent state, or multi-step tool interactions. This makes purely static vetting brittle. We present Runtime Skill Audit (RSA), a dynamic analysis method that audits skills by asking what the skill-mediated agent actually does under targeted runtime conditions. Instead of testing every skill with the same generic tasks, RSA profiles risk-relevant interfaces, prepares the execution context needed to exercise them, and assigns security labels from the resulting trace evidence. We instantiate RSA on OpenClaw and evaluate it on 100 skills against representative static baselines. RSA achieves 90.0\% accuracy with an 88.0\% true positive rate and an 8.0\% false positive rate, improving accuracy by 13.0 percentage points over the best static baseline. Under self-evolving attacks, static detectors collapse after one or two rounds, while RSA continues to detect 19--20 out of 20 malicious skills across rounds.

---


### 102. [UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction](https://arxiv.org/abs/2606.11681)

**<font color=#1a73e8>作者：</font>** Sangmin Lee, Eekgyun Ahn, Woongjib Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose UR-BERT, a Romanized transcription-based text-to-speech (TTS) encoder for massively multilingual TTS systems. Conventional grapheme-to-phoneme (G2P)-based approaches are limited to around 100 languages due to the availability of reliable G2P resources. In contrast, UR-BERT scales to 495 languages by unifying diverse writing systems into a shared Romanization representation. To further enhance phonetic fidelity and text-speech alignment, we introduce a speech token prediction objective during training, which encourages the encoder to learn speech-aware phonetic representations in a data-efficient manner. Experiments show that TTS systems built on UR-BERT consistently outperform recent text encoder baselines across a wide range of languages and resource conditions, and demonstrate strong generalization to unseen languages.

---


### 103. [Reason, Then Re-reason: Cross-view Revisiting Improves Spatial Reasoning](https://arxiv.org/abs/2606.11683)

**<font color=#1a73e8>作者：</font>** Chaofan Ma, Zhenjie Mao, Yuhuan Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning from egocentric videos is inherently challenging because the observable evidence is constrained by the camera trajectory. Existing methods rely on single-turn inference, forcing models to resolve geometric ambiguity through semantic priors rather than verifiable evidence. We argue that spatial reasoning should be revisitable: conclusions formed under limited evidence should remain open to revision when complementary viewpoints become available. Building on this insight, we propose Reason, then Re-reason (ReRe), a training-free, inference-time framework with two phases: in the Reason Phase, an MLLM forms a spatial hypothesis from the original video; in the Re-reason Phase, it verifies or revises the hypothesis by observing a synthesized novel-view video. To enable effective cross-view revisiting, we design a Geometry-to-Video pipeline that renders strategically complementary novel views from predicted 3D geometry. These views feature an elevated, oblique perspective with scene-spanning coverage, while preserving the MLLM's native video interface without architectural modifications. Extensive evaluations on VSI-Bench and STI-Bench demonstrate that ReRe substantially boosts open-source MLLMs to rival proprietary state-of-the-art performance. Project page: this https URL

---


### 104. [DroneShield-AI: A Multi-Modal Sensor Fusion Framework for Real-Time Autonomous Drone Threat Detection, Behavioral Intent Classification, and Swarm Intelligence in Contested Airspace](https://arxiv.org/abs/2606.11687)

**<font color=#1a73e8>作者：</font>** Marius Bayizere  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned Aerial Vehicle (UAV) threats have emerged as a defining security challenge of the 21st century. This paper presents DroneShield-AI, a unified open framework integrating six processing layers: RF signal classification, acoustic motor-signature detection, YOLOv8-based visual detection, evidence-weighted sensor fusion, a Behavioral Intent Classification Engine (BICE), and a Graph Neural Network Swarm Intelligence Module (GNN-SIM). BICE introduces the first systematic six-class threat taxonomy for drone flight patterns, enabling predictive operator alerts with a 30-second advance-warning horizon. GNN-SIM is the first open framework for adversarial multi-drone formation analysis using Graph Attention Networks. Evaluated on three publicly available real-world datasets, the fused pipeline achieves 96.1% detection accuracy, 3.2% false alarm rate, AUC-ROC: 0.981, and 142ms end-to-end latency on commodity CPU-class hardware at approximately $500-$780 USD total system cost. All code, model weights, and simulation datasets are publicly released at submission.

---


### 105. [Goal-Autopilot: A Verifiable Anti-Fabrication Firewall for Unattended Long-Horizon Agents](https://arxiv.org/abs/2606.11688)

**<font color=#1a73e8>作者：</font>** Youwang Deng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents are not trusted to run unattended: with no human watching, they confidently report success they never verified. We treat honesty -- bounding what an agent may claim at termination -- as a first-class metric for unattended autonomy, distinct from capability. We present Autopilot, an execution model that makes silent fabricated success structurally impossible rather than merely rarer. Autopilot externalizes all working state into a durable, gated finite-state machine that a scheduler advances one stateless tick at a time; a hard floor forbids any terminal "done" claim whose falsifiable gate did not actually execute and pass. We prove a No-False-Success theorem -- under gate soundness, floor enforcement, and plan coverage, termination implies the goal holds -- whose only trust points are empirically measurable, and show the worst case degrades to an honest stall, never a fabricated success. Because each tick rehydrates only the state machine, per-step context cost is constant in the horizon. Across a 3,150-cell paired corpus (70 tasks $\times$ 3 systems $\times$ 3 models $\times$ 5 seeds, including 50 SWE-bench Lite tasks across 11 OSS repos), Autopilot fabricates on 0.95% of cells [95% CI 0.38--1.62] while Reflexion and StateFlow baselines fabricate on 8.10% [6.48--9.81] and 25.05% [22.48--27.62] respectively. The headline contrast lives in the hard regime: on SWE-bench Lite, the firewall reduces fabrication from 33.7% (StateFlow) to 0.67%, a paired difference of $-33.07$ pp [95% CI $-36.53, -29.73$]. The mechanism is the gate, not the model: all ten Autopilot fabrications come from the strongest model, while two weaker mid-tier models never fabricate across 700 paired cells. The firewall trades coverage for honesty by design -- an honest stall is recoverable; a confident wrong output shipped downstream is not.

---


### 106. [RankVR: Low-Rank Structure Perception and Value Recalibration for Robust Composed Image Retrieval](https://arxiv.org/abs/2606.11689)

**<font color=#1a73e8>作者：</font>** Jiale Huang, Zixu Li, Zhiheng Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) constitutes a pivotal paradigm requiring models to perform joint reasoning on reference images and modification texts. However, the prevalence of Noisy Triplet Correspondence (NTC) in large-scale datasets severely constrains model performance. Existing denoising methods either target binary mismatches or rely on scalar-based point-wise estimation, neglecting rich global structural correlations among sample populations and dynamic value variations during training, thereby yielding suboptimal results. This paper identifies two critical unresolved challenges: Global Structural Inconsistency of Semantic Correlations and Hard Sample Discrimination Uncertainty. To address these, we propose RankVR, a framework designed to construct a robust CIR model via global structure consistency and dynamic value perception. Specifically, we introduce the Global Structure Consistency Perception (GSCP) module, which utilizes the Effective Rank of the Correlation Matrix to decouple clean samples from structural noise. By measuring rank difference, GSCP identifies samples disrupting macroscopic semantic symmetry. Furthermore, we develop the Adaptive Semantic Value Calibration (ASVC) module to distinguish high-value hard clean samples. By integrating training potential and reliability, it dynamically quantifies the semantic value of each triplet, ensuring effective utilization of hard samples while suppressing noise characterized by logical conflicts. Extensive experiments on the FashionIQ and CIRR benchmark datasets demonstrate that RankVR significantly outperforms existing state-of-the-art methods, validating its superior robustness in noisy environments.

---


### 107. [Spectrally Regularized Latent Flow Matching for Turbulence Generation](https://arxiv.org/abs/2606.11691)

**<font color=#1a73e8>作者：</font>** Khalid Rafiq, Aditya G. Nair  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent diffusion and flow matching have emerged as leading approaches for synthetic turbulence generation, yet they systematically under-represent dissipation-range amplitudes. We introduce a latent flow matching framework with a spectrally regularized compression stage that directly targets this failure mode. On a 256^2 DNS dataset at Re_f \approx 2250, replacing an MSE-trained VAE with a zone-weighted log-spectral objective raises deep-dissipation retained spectral power from 25% to 94% in reconstruction and from 20% to 79% in unconditional generation. The improved latent representation also yields a substantially better sampling cost-fidelity tradeoff: the MSE-trained latent space imposes a fundamental quality ceiling near DD bias -0.70 that no integrator or step-count can overcome, while the spectrally regularized latent space reaches DD bias -0.117 at just 20 function evaluations. Mechanistically, encoder-decoder swap experiments show that the improvement is driven primarily by encoder-induced latent reorganization rather than decoder capacity, while a support-amplitude decomposition reveals that MSE-trained models behave as conservative suppression models, minimizing pointwise error by attenuating intermittent high-wavenumber structure. Both pipelines recover the second-order structure function and the correct sign of S_3, indicating the correct cascade direction without explicit supervision. A small residual gap in the magnitude of S_3 suggests that phase-coherent triadic organization remains a complementary axis to amplitude fidelity for future generative turbulence models.

---


### 108. [Understanding and Supporting Online Discussion with Opinionated Chatbots](https://arxiv.org/abs/2606.11693)

**<font color=#1a73e8>作者：</font>** Tianqi Song, Chi-Lan Yang, Zihan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Opinionated chatbots are increasingly present on online platforms and have the potential to shape public discourse by influencing individuals' viewpoints before they engage in discussions. Despite their growing presence, the impact of interacting with opinionated chatbots on subsequent online interactions remains largely unexplored. This study investigated how exposure to different types of opinionated chatbots, specifically those expressing opposing, reinforcing, or balanced viewpoints, affected participants' subsequent online discussions. In a controlled experiment with 83 participants, we found that interacting with an opinionated chatbot that consistently opposed participants' arguments led to greater shifts in opinion, indicating enhanced openness to revising one's initial stance. Conversely, participants who interacted with a chatbot that consistently reinforced their views were more likely to adopt more agreeable communication styles in subsequent conversations with others. Furthermore, interactions with different types of opinionated chatbots resulted in varying levels of trust, as well as different perceptions of chatbots and human interlocutors. Our findings indicate that opinionated chatbots can influence both individuals' opinions on social topics and their communication behaviors in online environments. This presents a trade-off for future designers seeking to facilitate cognitive flexibility in changing opinions while maintaining positive user experiences and trust in the chatbots during public discourse. We discuss the implications for designing opinionated chatbots to promote more constructive and less polarized online

---


### 109. [Noise-Aware Framework for Correcting Corrupted Labels](https://arxiv.org/abs/2606.11695)

**<font color=#1a73e8>作者：</font>** Ha-Linh Nguyen, Hong-Anh Nguyen, Minh-Duc La 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality labeled data is essential for training reliable ML/DL models. However, real-world datasets often contain a considerable proportion of corrupted labels, which can severely degrade model performance. To address this problem, we propose CANOLA, a novel framework for correcting corrupted labels through noise-aware learning and iterative label refinement. CANOLA explicitly estimates the underlying noise distribution of the dataset and incorporates this information into the training of a noise-aware Deep Neural Network. By incorporating noise characteristics during learning, CANOLA enables the model to down-weight unreliable supervision signals and focus on trustworthy patterns, thereby improving robustness and generalization. Label correction is performed via cautious, iterative soft label refinement, in which model predictions are blended with observed labels to prevent premature or erroneous updates. This progressive refinement allows the dataset to be repaired in a stable and controlled manner. We evaluate CANOLA on six widely used datasets under realistic noisy labeling scenarios. Experimental results show that CANOLA consistently outperforms SOTA label correction methods, achieving relative improvements ranging from 19% to 52% in error reduction. Moreover, models trained on datasets corrected by CANOLA obtain substantial downstream performance gains. Even simple classifiers trained on CANOLA's corrected data can outperform complex model-centric approaches by margins of up to 67%.

---


### 110. [T2S: A Rehearsal-Based Approach for Extraction-Resistant Model Watermarking](https://arxiv.org/abs/2606.11698)

**<font color=#1a73e8>作者：</font>** Jian-Ping Mei, Weibin Zhang, Ao Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model watermarking safeguards AI model intellectual property by embedding distinctive knowledge that induces unique behavioral signatures. The primary technical challenge lies in ensuring watermark robustness against various post-processing attacks on the watermarked model. Model extraction attacks emerge as the most severe threat, where adversaries exploit prediction outputs to train surrogate models that illegally replicate the original model's functionality. In this work, we propose a rehearsal-based watermark embedding framework to enhance the robustness of model watermarks against model extraction attacks. By simulating the extraction process, our method leverages the loss of a \textit{simulated stolen model} on a trigger set as a training signal to fine-tune the watermark knowledge within the target model. This fine-tuning step encourages the watermark to be embedded in a way that boosts transferability, thereby increasing its chances of persisting and remaining detectable in stolen models. Comprehensive experiments conducted under diverse settings demonstrate that the proposed method significantly improves the robustness of model watermarks against both model extraction and subsequent watermark removal attacks.

---


### 111. [A Data-Centric Framework for Detecting and Correcting Corrupted Labels](https://arxiv.org/abs/2606.11699)

**<font color=#1a73e8>作者：</font>** Ha-Linh Nguyen, Hong-Anh Nguyen, Minh-Duc La 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The performance of machine learning and deep learning models largely depends on the quality of the training data. However, the quality of the real-world datasets is often compromised by noisy labels, which can substantially degrade model accuracy and reliability. To address this challenge, we propose Relabeler, an end-to-end data-centric framework for detecting and correcting corrupted labels. For corrupted label detection, Relabeler jointly leverages both local and global relationships among data instances to identify potentially noisy samples. After detecting suspicious instances, Relabeler further performs label correction by estimating the most probable clean label for each instance based on both its input features and observed noisy label. Extensive experiments across multiple datasets, noise types, and noise rates demonstrate that Relabeler consistently outperforms state-of-the-art baselines, achieving up to 58% improvement in label correction precision and 6% improvement in downstream task performance.

---


### 112. [MedCTA: A Benchmark for Clinical Tool Agents](https://arxiv.org/abs/2606.11702)

**<font color=#1a73e8>作者：</font>** Tajamul Ashraf, Hyewon Jeong, Fida Mohammad Thoker 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To make clinically grounded decisions, medical AI agents are expected to go beyond simple recognition and be capable of tool retrieval, evidence acquisition, and integration. Existing benchmarks largely evaluate isolated perception or single-turn question answering, and therefore provide limited visibility into failures of planning, tool recruitment, and rollout reliability. We introduce MedCTA, a benchmark for evaluating medical tool agents on clinician-validated, step-implicit tasks grounded in realistic multimodal clinical inputs, including radiology images, pathology slides, and reports. MedCTA comprises 107 real-world clinical tasks with clinician-verified executable trajectories over 5 deployed tools, and supports process-aware evaluation of tool selection, argument validity, execution stability, trajectory fidelity, and outcome quality. We benchmark 18 open- and closed-source multimodal models and find that even frontier systems remain brittle in multi-step clinical tool use: autonomous rollouts are dominated by protocol failures, premature stopping, and incorrect tool recruitment, while gold-standard tool routing yields large but still incomplete gains. These results show that strong backbone perception does not translate into reliable agentic behavior in clinical settings. MedCTA provides a rigorous testbed for auditing, diagnosing, and advancing trustworthy medical AI agents. The dataset and evaluation suite are available at this https URL

---


### 113. [RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation](https://arxiv.org/abs/2606.11709)

**<font color=#1a73e8>作者：</font>** Leyi Pan, Shuchang Tao, Yunpeng Zhai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) provides dense, token-level supervision for reasoning models by aligning a model's own distribution with the distribution it produces under privileged context, typically a verified solution. However, we show that the learning signal drawn from this distributional gap concentrates on style tokens rather than task-bearing ones, as the hinted model tends to produce more direct, shorter outputs. We term this pathology \emph{privilege-induced style drift}, which destabilizes training or causes response length to shrink. To address this, we propose \textbf{RLCSD} (Reinforcement Learning with Contrastive on-policy Self-Distillation), which mitigates this drift by contrasting the teacher-student gap under a correct hint against that under a wrong hint, suppressing the style shift that conditioning on a hint tends to induce regardless of correctness, and yielding a signal that is more concentrated on task-bearing tokens. Experiments on Qwen3 (1.7B/4B/8B) and Olmo-3-7B-Think across mathematical and logical reasoning show that RLCSD consistently outperforms GRPO and prior OPSD methods. We further show that the contrastive principle is general: it plugs into existing OPSD methods to improve them, and its underlying insight extends to the broader cross-model on-policy distillation setting.

---


### 114. [ERN-Net : Evolving Reason Node-Net for Document Binarization](https://arxiv.org/abs/2606.11710)

**<font color=#1a73e8>作者：</font>** Hsin-Jui Pan, Sheng-Wei Chan, Jen-Shiung Chiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents ERN-Net, an Evolving Reason Node-Net for efficient document image binarization. ERN-Net enhances degradation-sensitive regions, such as faint strokes, broken characters, and noisy backgrounds, through evolving reason nodes and multi-scale reasoning. We further compare ResNet-101, ConvNeXt-Tiny, and ConvNeXt-Base, and find that ConvNeXt-Tiny provides the best practical trade-off between accuracy and memory usage. In addition, DIBCO-based pretraining improves binarization performance without increasing model memory consumption, requiring only about 1.5 additional training hours. Experiments on DIBCO-style benchmarks show that ERN-Net is effective under low-data and low-memory settings.

---


### 115. [Capacity-Constrained Online Convex Optimization with Delayed Feedback](https://arxiv.org/abs/2606.11711)

**<font color=#1a73e8>作者：</font>** Alexander Ryabchenko, Idan Attias, Daniel M. Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online learning with delayed feedback typically assumes that the learner can track all pending rounds until their feedback arrives. In practice, tracking resources are finite, and feedback from untracked rounds is permanently lost. In this paper, we study delayed online convex optimization (OCO) under a hard capacity constraint, where at most $C$ pending rounds can be tracked at any time. To model delay information, we introduce a semi-clairvoyant model that refines the clairvoyant assumption from prior work: rather than requiring delays to be known at prediction time, the learner observes delay expirations online, consistent with the classical unconstrained delayed setting. Our approach proceeds via a reduction to a novel ``delayed and weighted'' OCO problem, using a scheduler that randomizes tracking decisions and importance-weights the resulting observations. For this base problem, we propose and analyze Delayed-Weighted FTRL and its bandit analogue, establishing regret bounds that explicitly characterize the interaction between time-varying weights and delayed feedback. Combining these base learners with our schedulers yields the first regret guarantees for capacity-constrained OCO under convex and strongly convex losses, for both first-order and bandit feedback. For first-order feedback, capacity $C = \Omega(\log T)$ suffices to recover standard delayed OCO rates up to logarithmic factors. For bandit feedback, the regret rates are modulated by powers of $(1 + \sigma_{\text{max}}/C)$, where $\sigma_{\text{max}}$ is the maximum number of pending observations at any time. This allows the regret bound to degrade gracefully when $C < \sigma_{\text{max}}$, while remaining sublinear.

---


### 116. [Mind the Perspective: Let's Reason Recursively for Theory of Mind](https://arxiv.org/abs/2606.11724)

**<font color=#1a73e8>作者：</font>** Chao Lei, Guang Hu, Meng Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory of Mind (ToM) reasoning requires inferring agents' beliefs from partial and asymmetric observations, which remains an open challenge for LLMs. Existing prompting-based approaches improve ToM reasoning through observable-event filtering or temporal belief chains, without explicitly modeling nested beliefs. We introduce RecToM, an inference-time framework for ToM reasoning that models nested beliefs via recursive perspective construction. RecToM constructs each character perspective from the preceding character perspective along the character chain specified by the question, reducing higher-order belief questions to actual-world questions within the final constructed perspective. We further provide a KD45 analysis showing that RecToM's perspective construction induces a well-formed belief modality beyond simple event filtering. Experiments on ToM benchmarks, including Hi-ToM, Big-ToM, and FanToM, across multiple LLM backbones show that RecToM consistently outperforms recent advanced approaches, achieving state-of-the-art performance. Notably, RecToM reaches 100\% accuracy on Hi-ToM with GPT-5.4 and Qwen3.5, a benchmark requiring higher-order ToM reasoning.

---


### 117. [A VPN-as-a-Service Tailored Enabler for Computing-constrained Environments](https://arxiv.org/abs/2606.11729)

**<font color=#1a73e8>作者：</font>** Carolina Fernández-Martínez, César Cajas Parra, Shuaib Siddiqui  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industry has embraced Zero Trust (ZT) architectural tenets and implementations for cloud-native environments, following stricter security requirements to both internal and external tenants. Among others, these approaches combine fine-grained identity management and monitoring for both inventorying and better analysing the devices' security posture for overall protection, along with strict separation of concerns and isolation to enforce minimal privilege. Networking-wise, ZT approaches rely as well on isolation and least privilege; enacted by separate, secure tunnels per tenant connecting to a given infrastructure. Such implementations can also be applied to the connectivity within and towards experimental infrastructures. In this sense, this work contributes the design and evaluation of a cloud-native VPN-as-a-Service (VPNaaS) that can be (i) easily orchestrated to deploy on-the-fly, separate tunnels per each tenant remotely connecting to the infrastructure; (ii) integrated with common Identity and Access Management (IAM) tools, key to ZT deployments; and (iii) adapt to computing- or entropy- constrained environments. This solution is customisable and allows, among others, to select from RSA or Elliptic Curves (EC) as key generation algorithm and their parameters to achieve more secure keys and adapt to resource-constrained environments.

---


### 118. [MHOT: Height-Optimized Authenticated Data Structure for Blockchain State Commitment](https://arxiv.org/abs/2606.11736)

**<font color=#1a73e8>作者：</font>** Sipeng Xie, Qianhong Wu, Minghang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> State root computation dominates (78%) blockchain block processing time. Ethereum's canonical authenticated data structure, i.e., Merkle Patricia Trie (MPT), suffers from severe tree-height growth and is vulnerable to \textit{Nurgle attacks} (SP'24), where adversaries inflate path depth via hash collisions and degrade system performance at negligible cost. Existing defenses increase node fanout (span) to bound tree height, but higher span inflates proof size exponentially. Prior work mitigates this trade-off using vector commitments, at the cost of trusted setup or expensive verification.
We present \textsc{Mhot}, a height-optimal authenticated data structure for blockchain state commitment that preserves standard hash-based verification without trusted setup. Unlike MPT's fixed-prefix indexing, which couples span and fanout exponentially, \textsc{Mhot} indexes by discriminative bits that actually distinguish keys, achieving adaptive span with linear fanout coupling and provably minimal height. To prevent high fanout from inflating proofs, we introduce hierarchical proofs, a two-layer Merkle construction that reduces per-node proof overhead from O(k) to O(log k).
On Ethereum mainnet workloads, \textsc{Mhot} achieves up to 9X higher write throughput, 4X lower write amplification, and 2X smaller proofs than MPT. Under Nurgle attacks, even when the adversary consumes an entire block's gas budget, \textsc{Mhot} maintains a 0% attack success rate (v.s., 99.97% for MPT). Our results, somewhat surprisingly, show that height optimality (not new crypto primitives!) is the key abstraction for scalable and attack-resilient blockchain state commitment.

---


### 119. [Multi-View In-Cabin Monitoring System for Public Transport Vehicles](https://arxiv.org/abs/2606.11739)

**<font color=#1a73e8>作者：</font>** Evgeny Gorelik, Kenny Dean Karrow, Fikret Sivrikaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a multi-view in-cabin monitoring dataset for public transportation with synchronized RGB and depth images from four inward-facing cameras and a rotating LiDAR covering the vehicle interior of a digitalized and partly automated German city bus. The dataset contains 9.136 synchronized samples with annotations and is accompanied by a calibration and pseudo-labeling pipeline that generates 3D human pose estimates and oriented 3D bounding boxes for occupants. We further provide a nuScenes-format conversion and benchmark representative multi-view 3D detection models (e.g., Lift-Splat-Shoot and BEVFusion), supporting comparative evaluation and small-scale training of multi-view in-cabin perception models. The dataset and tools are available at this https URL.

---


### 120. [UniReason-Med: A Shared Grounded Reasoning Interface for 2D-to-3D Transfer in Medical VQA](https://arxiv.org/abs/2606.11740)

**<font color=#1a73e8>作者：</font>** Mengzhuo Chen, Yan Shu, Chi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study whether grounded reasoning supervision from abundant 2D medical images can improve 3D medical VQA when both input types are aligned through a common reasoning interface. We introduce UniReason-Med, a single-checkpoint framework that processes either a 2D image or a slice-serialized 3D volume at inference time, generating interleaved textual reasoning and localized visual evidence through shared box syntax, region-token injection, and a common grounded reasoning policy. To train this interface, we construct UniMed-CoT, a 220K instruction-tuning dataset with interleaved textual reasoning and grounded visual evidence, including 170K 2D and 50K 3D samples. Through supervised fine-tuning followed by outcome-level reinforcement learning, UniReason-Med learns to generate grounded reasoning traces without IoU/Dice-based localization rewards during RL. Data-mixture and component ablations show that joint 2D+3D grounded supervision substantially improves 3D reasoning over 3D-only training, while grounding and region-token injection consistently benefit both 2D and 3D tasks. These results suggest that a shared grounded reasoning interface can transfer reasoning structure from 2D images to slice-serialized volumetric medical understanding. The code and data are publicly available at this https URL.

---


### 121. [Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild](https://arxiv.org/abs/2606.11744)

**<font color=#1a73e8>作者：</font>** Sidney Tio, Arunesh Sinha, Pradeep Varakantham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are now widely used for everyday learning, but the underlying interactions are typically unstructured chats rather than following a curriculum. Unlike formal online learning systems, these interactions carry no prior record of the student, so any estimate of what the student already knows must be inferred from the dialogue itself. We show that this gap is not closed by scaling models alone. Frontier and education-tuned LLMs perform poorly when asked to tutor a student over an extended session, because doing so requires three things at once. The tutor must sequence a curriculum, conduct Socratic dialogue, and infer the student's knowledge state from that dialogue. We propose separating these responsibilities. Given a student query, our system constructs a prerequisite knowledge graph in which subtopics are nodes and dependencies are edges, and frames tutoring as deciding which node to teach next and how many dialogue turns to spend on it before moving on. A lightweight PPO policy handles this sequencing decision, while an LLM conducts the Socratic exchange at the chosen node and returns a signal of student progress. Across held-out STEM and non-STEM topics, our PPO-paired tutor outperforms heuristic baselines, frontier general-purpose models, and a model specialised for Socratic dialogue: on both the rate at which students reach full curriculum mastery and the number of turns required. Explicit curriculum structure delivers gains that scaling the underlying model does not.

---


### 122. [AnchorEdit: Maintaining Temporal Consistency in Multi-turn Image Editing via Causal Memory](https://arxiv.org/abs/2606.11751)

**<font color=#1a73e8>作者：</font>** Hang Xu, Xiaoxiao Ma, Guohui Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-turn image editing is essential for iterative design, yet current models often struggle with identity drift and error accumulation over successive steps. While existing research leverages video priors for consistency, their reliance on bidirectional attention is fundamentally misaligned with the causal, sequential nature of interactive editing. In this paper, we propose AnchorEdit, the first autoregressive (AR) diffusion-based framework designed specifically for high-resolution, long-term multi-turn editing. AnchorEdit bridges the gap between video priors and causal inference through a three-stage training curriculum: identity-preserving sing-turn pretraining, causal AR forcing fine-tuning with a novel self-rollout strategy to mitigate exposure bias, and consistency distillation for efficient 4-step generation. During inference, we introduce a memory mechanism to anchor the initial subject identity and ensure stable extrapolation across extended editing trajectories. To evaluate performance, we provide a new high-resolution multi-turn editing benchmark designed to stress-test long-horizon stability. Extensive experiments demonstrate that AnchorEdit achieves state-of-the-art results, maintaining exceptional subject fidelity and instruction following even over 10+ interaction rounds.

---


### 123. [RCAP: Robust, Class-Aware, Probabilistic Dynamic Dataset Pruning](https://arxiv.org/abs/2606.11761)

**<font color=#1a73e8>作者：</font>** Atif Hassan, Swanand Khare, Jiaul H. Paik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic data pruning techniques aim to reduce computational cost while minimizing information loss by periodically selecting representative subsets of input data during model training. However, existing methods often struggle to maintain strong worst-group accuracy, particularly at high pruning rates, across balanced and imbalanced datasets. To address this challenge, we propose RCAP, a Robust, Class-Aware, Probabilistic dynamic dataset pruning algorithm for classification tasks. RCAP applies a closed-form solution to estimate the fraction of samples to be included in the training subset for each individual class. This fraction is adaptively adjusted in every epoch using class-wise aggregated loss. Thereafter, it employs an adaptive sampling strategy that prioritizes samples having high loss for populating the class-wise subsets. We evaluate RCAP on six diverse datasets ranging from class-balanced to highly imbalanced using five distinct models across three training paradigms: training from scratch, transfer learning, and fine-tuning. Our approach consistently outperforms state-of-the-art dataset pruning methods, achieving superior worst-group accuracy at all pruning rates. Remarkably, with only $10\%$ data, RCAP delivers $>1\%$ improvement in performance on class-imbalanced datasets compared to full data training while providing an average $8.69\times$ speedup. The code can be accessed at this https URL

---


### 124. [When Do Data-Driven Systems Exhibit the Capability to Infer?](https://arxiv.org/abs/2606.11769)

**<font color=#1a73e8>作者：</font>** Maximilian Poretschkin, Tabea Naeven  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The European AI Act is the first comprehensive regulation of artificial intelligence (AI), setting out extensive obligations, particularly for so-called high-risk and general-purpose AI systems. A key distinguishing feature of AI systems under the AI Act is the capability to infer. Since the AI Act does not clearly define what inference is, there is a gray area for certain data-driven systems. A specific example is credit scoring systems, which are listed by Annex III of the AI Act. At the same time, however, these are often implemented using statistical models for which it is unclear whether they have the capability to infer and thus fall under the AI definition of the AI Act at all.
Motivated by statistical learning theory, this work develops a framework for grading different levels of the capability to infer. Based on the AI Act and the Commission Guidelines on the definition of an artificial intelligence system, we analyze which levels constitute sufficient capability to infer within the meaning of the AI Act and where further regulatory clarity is needed. We illustrate the framework by creating two realistic credit scoring workflows and show whether and where inference occurs in them. Our analysis illustrates that not only individual models but the entire data processing workflow must be considered. It also shows that the involvement of human experts during development can have significant influence on the capability to infer. Code can be found at this https URL.

---


### 125. [Battery detection of XRay images using transfer learning](https://arxiv.org/abs/2606.11779)

**<font color=#1a73e8>作者：</font>** Nermeen Abou Baker, David Rohrschneider, Uwe Handmann  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The need for detecting and sorting batteries is drastically increasing for many applications. This study proves the potential of transfer learning in predicting whether the image contains a battery or not, the location and identifying three types of batteries, namely: prismatic, pouch, and cylindrical Lithium-Ion Batteries (LIB). Particularly, it focuses on the transfer learning method in two applications: Training a large-scale dataset to detect electronic devices using a pre-trained YOLOv5m, then using these latter trained weights to detect and classify the batteries. The precision of battery detection achieves 94%, which outperforms the pretrained YOLOv5m weights with 5%, in 22 ms inference time.

---


### 126. [Seeing What Matters: Perceptual Wrapper with Common Randomness for 3D Gaussian Splatting](https://arxiv.org/abs/2606.11782)

**<font color=#1a73e8>作者：</font>** He-Bi Yang, Jing-Zhong Chen, Yen-Kuan Ho 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) achieves impressive real-time rendering, it frequently struggles to synthesize high-frequency textures, a limitation heavily exacerbated in memory-constrained and rate-distortion-optimized (RDO) pipelines. To address this, we propose a versatile 2D perceptual wrapper that enhances the rendered outputs of existing 3DGS representations in a content- and view-dependent manner. Our method leverages a lightweight synthesis network conditioned on pseudo-random Gaussian noise to synthesize perceptually plausible textures. Supervised by Wasserstein Distortion, the network learns to match local feature statistics rather than strictly enforcing pixel-wise reconstruction fidelity, effectively mitigating the blurriness inherent in standard frameworks. We demonstrate the broad applicability of our plug-and-play approach across vanilla, memory-constrained, and RDO 3DGS methods. Comprehensive subjective and objective experiments confirm that our method significantly improves over existing baselines, yielding superior perceptual quality at sharply reduced file or model sizes.

---


### 127. [A Comprehensive Ecosystem for Open-Domain Customized Video Generation](https://arxiv.org/abs/2606.11783)

**<font color=#1a73e8>作者：</font>** Jingxu Zhang, Yuqian Hong, Daneul Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in video generation has shown impressive visual synthesis capabilities. However, open-domain customized video generation remains limited by the lack of large-scale, annotated datasets capturing diverse identity-specific attributes. To address this, we introduce PexelsCustom-1M, the first publicly available million-scale dataset for identity-preserving video generation, containing one million curated <identity, text, video> triplets across 8,000+ categories. Leveraging this, we propose CustoMDiT, a parameter-efficient framework that adapts a pretrained multimodal Diffusion Transformer into a customized video generator with only 8% additional learnable parameters. Our method surpasses prior state-of-the-art. However, benchmarks such as DreamBooth cover only 100 classes, which is insufficient for real-world applications. To overcome this, we construct OpenCustom, a new benchmark with 1,000+ categories, created via cross-dataset knowledge fusion from ImageNet and MS-COCO. Extensive experiments confirm the advantages of both our dataset and model. We will open-source the entire ecosystem--including dataset, pipeline, benchmark, and implementations--to support further research.

---


### 128. [AI4Land: Scalable Deep Learning for Global High-Resolution Land Use Reconstruction](https://arxiv.org/abs/2606.11793)

**<font color=#1a73e8>作者：</font>** Amirpasha Mozaffari, Marina Castaño, Stefano Materia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty in the terrestrial carbon cycle remains a major constraint in climate projections, partly driven by the uncertainties affecting the land surface representation and variability in Earth system models. To address this limitation, we present a data-driven framework AI4Land, for generating high-resolution historical reconstructions and future projections of key land surface variables. The framework follows a two-phase approach using a U-Net architecture. In the first phase, which is the focus of this work, it reconstructs annual land use and land cover by integrating coarse-resolution scenario data with static geophysical features. In a planned second phase, the resulting high-resolution maps will be used to predict dynamic biophysical variables, particularly leaf area index, at finer temporal scales. Trained on Earth observation data, the models learn to reproduce spatially explicit and physically consistent land surface patterns, extending temporal coverage to periods lacking direct observations. AI4Land was developed and trained on MareNostrum5, demonstrating how GPU-accelerated HPC infrastructure enables global-scale climate AI pipelines. The final product is a suite of open-source emulators designed for real-time coupling with digital twin platforms, such as those developed under the Destination Earth initiative. By delivering realistic and evolving land surface conditions on demand, this work aims to reduce critical uncertainties and improve the predictive power of next-generation climate simulations.

---


### 129. [Space-sampled Value Decay: Forgetting Mechanisms for Non-stationary Deep Reinforcement Learning](https://arxiv.org/abs/2606.11797)

**<font color=#1a73e8>作者：</font>** Felix Störck, Fabian Hinder, Barbara Hammer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studies on rodents such as mice have shown the capabilities to adapt their behavior when dealing with changing parameters (``drift'') of the environment even if no information about change is provided (uncertainty) -- a behavior that can be modeled by forgetting mechanisms. Non-stationary Reinforcement Learning (NSRL) deals with adapting state-of-the-art RL methods to deal with changing environments: these however usually require (partially) perfect information about the drift such as ``task IDs'' or ``context''. To mitigate the effects of drift, this work develops \emph{Space-sampled Value Decay} as an explicit forgetting mechanism for value-based deep RL architectures as a simple yet effective approach. In particular we demonstrate and discuss positive effects but also limitations in achieved returns for modifications of Deep Q-networks (DQN) and Soft Actor-Critic (SAC) when evaluated on non-stationary environments.

---


### 130. [SwarmSense-DNN: A Trustworthy and Decentralized Neural Framework for Proactive Anomaly Defense in Consumer IoT](https://arxiv.org/abs/2606.11803)

**<font color=#1a73e8>作者：</font>** Jing Yang, Vijay Govindarajan, Saad Arif 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of consumer IoT devices has introduced unprecedented challenges in trustworthy anomaly detection against AI-enabled cyber threats, requiring real-time, privacy-preserving, and scalable defense mechanisms. Traditional centralized strategies face critical limitations, including communication bottlenecks, single points of failure, and privacy vulnerabilities when processing distributed consumer data. We propose SwarmSense-DNN, a novel decentralized neural framework employing swarm intelligence for secure, cooperative anomaly detection across distributed IoT environments. The framework integrates autonomous agents with deep neural networks to form a self-organizing defense system that detects evolving anomalies without centralized coordination. It utilizes hierarchical federated learning with graph neural networks and attention mechanisms to capture local and global anomaly behaviors while ensuring data privacy. Extensive experiments demonstrate SwarmSense-DNN's superior performance: it achieves 95.44% average detection accuracy across five benchmark datasets while reducing communication overhead by 67%. The framework maintains robust resilience against adversarial threats through differential privacy safeguards and demonstrates strong fault tolerance under node failures and AI-enabled attacks.

---


### 131. [Toward Trustworthy AI: Multi-Target Adversarial Attacks and Robust Defenses for Continuous Data Summarization](https://arxiv.org/abs/2606.11804)

**<font color=#1a73e8>作者：</font>** Yuefang Lian, Longkun Guo, Zhongrui Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trustworthy AI requires reliable data-processing pipelines, not only robust downstream predictive models. As an upstream component, data summarization determines which information is retained and passed to subsequent learning or decision modules. Therefore, adversarial perturbations to the summarization process can compromise trustworthy AI in an upstream manner: they may alter the selected summary, reduce its representativeness, and further degrade the utility of subsequent learning tasks. In this paper, we study adversarial attacks on continuous data summarization under similarity-level perturbations through DR-submodular optimization. We show that a class of multi-resolution image summarization objectives can be formulated as multilinear extensions of non-negative submodular set functions and satisfy DR-submodularity with $m$-weak monotonicity. We then formulate multi-target attack generation as a min-max problem, where one admissible perturbation of the similarity structure is optimized to degrade multiple target summarization models. To mitigate such perturbations, we formulate robust defense against mixed attack types as a regularized max-min problem. For both problems, we develop approximation algorithms with theoretical guarantees. Experiments on real-data and controlled clustered benchmarks show that the proposed attack is effective in representative low-to-moderate budget regimes and can induce downstream task-performance loss. The proposed defense improves the robustness--mitigation trade-off in structured settings, while also revealing the parameter sensitivity of robust protection on real data.

---


### 132. [TextHOI-3D: Text-to-3D Hand-Object Interaction via Discrete Multi-View Generation and Joint Mesh Optimization](https://arxiv.org/abs/2606.11805)

**<font color=#1a73e8>作者：</font>** Zixiong Hao, Zhencun Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned 3D generation has progressed rapidly for images and isolated objects, but producing a hand-object mesh remains challenging: the output must preserve language semantics, cross-view consistency, object geometry, articulated hand shape, and physically plausible contact. We present TextHOI-3D, a staged framework that uses generated multi-view observations as an explicit interface between text-conditioned visual generation and geometry-aware hand-object recovery. TextHOI-3D learns a compact VQ token space for fixed-camera hand-object observations, predicts multi-view visual tokens from text with a CLIP-conditioned visual autoregressive model, and recovers a unified hand-object mesh through prior initialization, multi-view joint optimization, and anti-penetration refinement. The design separates semantic generation from geometric recovery while keeping both stages connected by a discrete multi-view representation. On HO3D-derived evaluations, the multi-view setting reduces object CD from 17.26 mm to 4.92 mm and penetration volume from 5.3721 cm^3 to 0.2193 cm^3 compared with a single-view counterpart, while improving hand errors and surface F-scores. These results support multi-view visual tokens as an effective intermediate representation for text-driven 3D hand-object mesh creation.

---


### 133. [Jaguar: Fast Private CNN Inference with Power-of-Two Homomorphic Arithmetic](https://arxiv.org/abs/2606.11827)

**<font color=#1a73e8>作者：</font>** Yewon Jeong, Nayoung Jung, Hyeri Roh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hybrid HE/2PC private CNN inference remains bottlenecked by prime-modulus homomorphic arithmetic in convolution and by a precision flow that runs ReLU at doubled bitwidth before invoking a separate truncation protocol. We present Jaguar, a system built on a single design choice--a power-of-two ciphertext ring--that addresses both. The choice enables SPA-Conv, a coefficient-domain convolution kernel that replaces NTT-centric polynomial multiplication with scalar-polynomial accumulation, and an exact ciphertext-side truncation by local right shifts that lets ReLU run directly at the target fixed-point precision and eliminates the post-ReLU truncation protocol. Where NTT remains genuinely useful--at the client, for the single polynomial multiplication during decryption--we recover it through an auxiliary NTT prime, preserving the power-of-two protocol substrate while keeping decryption O(N log N). On ImageNet-scale ResNet-18, ResNet-50, and MobileNetV2 with AVX disabled, Jaguar achieves 2.07-3.72x lower end-to-end latency than Cheetah and 2.16-3.36x lower than Rhombus, with 1.16-1.76x lower communication than Cheetah.

---


### 134. [Skill-Augmented AI Agents for Medical Research Analysis: An Exploratory Multi-Model Human Evaluation in an NSCLC Transcriptomic Biomarker Task](https://arxiv.org/abs/2606.11830)

**<font color=#1a73e8>作者：</font>** Qianyu Yao, Fei Sun, Bocheng Huang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background. Large language models and AI agents are increasingly used to support biomedical research, but native model outputs may omit key analytical steps, misuse methods, or overstate conclusions. We evaluated whether autonomous access to a medical research skill package was associated with higher-quality AI-generated transcriptomic research-analysis outputs compared with native AI without skills. Methods. We conducted an exploratory multi-model human evaluation using a non-small cell lung cancer immunotherapy biomarker task. Six model backbones were tested. The evaluation included 21 anonymized outputs: 9 native-AI outputs and 12 skill-augmented outputs generated through an AI agent implementation represented by OpenClaw. Four non-expert biomedical reviewers and two blinded experts evaluated each output, with two ratings from each reviewer type. The primary outcome was expert-rated overall quality. Results. Skill-augmented outputs showed directionally higher expert overall quality than native-AI outputs (mean 5.50 vs 5.11; difference=0.39; bootstrap 95\% CI, -0.04 to 0.90; Welch p=0.156). Non-expert reviewer quality showed the same direction (mean 4.72 vs 4.47; difference=0.26; bootstrap 95\% CI, -0.25 to 0.80; Welch p=0.373). Expert agreement was limited (single-rating ICC=-0.15), and model-specific effects were descriptive and heterogeneous. Conclusions. Autonomous skill access showed a directional quality signal in this exploratory sample, but the signal was smaller than expert-rating noise and should not be interpreted as confirmatory evidence. The findings primarily motivate larger evaluations of skill-augmented AI agents with stronger reliability controls, platform replication, and biological-validity assessment.

---


### 135. [From Uniform to Learned Graph Priors: Diffusion for Structure Discovery](https://arxiv.org/abs/2606.11831)

**<font color=#1a73e8>作者：</font>** Qi Shao, Hao Guo, Jiawen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural relational inference (NRI) methods discover interaction graphs from trajectories through variational reasoning on discrete potential edges. However, these methods typically rely on oversimplified, factorized graph priors. Such priors, typically nearing uniform distributions, treat edges as independent entities. This systemic misalignment does not match the real-world systems and yields diffuse and indecisive edge posteriors limiting the reliability of structural discovery. To address this, we propose \textit{Diff-prior}, a diffusion-parameterized adaptive prior used to calibrate latent graph distribution rather than generate graphs. Our core insight is to reframe prior integration as a learnable denoising-style calibration that organizes scattered, uncertain edge posteriors into a more reliable overall structure which can be trained by the diffusion model. Diff-prior learns an adaptive structure prior that performs structured calibration on the edge posteriors during inference, guiding it towards a distribution closer to the underlying structure. The diff-prior operates before structural sampling and acts as a denoising calibrator directly on the encoder edge distribution, which provides a generic training paradigm over structured variables. Experiments on standard benchmarks validated our framework, and the results indicate that Diff-prior improves the performance of structure inference and generates more decisive edge posteriors across multiple NRI-family architectures. The code is available on this https URL.

---


### 136. [Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics](https://arxiv.org/abs/2606.11833)

**<font color=#1a73e8>作者：</font>** Sam Gijsen, Michał Łukomski, Marc-André Schulz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching and diffusion models enable conditional generation across domains ranging from images to proteins, with recent extensions to out-of-distribution contexts. Yet generative models of neural time series have largely remained restricted to categorical conditioning, precluding compositional and zero-shot generalization. In this work, we propose a per-timestep conditioned diffusion transformer for generating realistic fMRI brain dynamics during unseen cognitive tasks by injecting both compositional language and optional spatial priors in-context. Such zero-shot generation could enable counterfactual neuroscience by supporting in-silico design and evaluation of novel cognitive experiments before empirical validation. Leveraging this model, we evaluate across hundreds of held-out task conditions and characterize predictive performance in relation to the training manifold. From language alone, the model recovers region-specific recruitment across tasks and held-out spatial activation patterns. Spatial priors, when available, complement the text pathway by anchoring generation in regions of task space where language alone degrades, while retaining the compositional structure needed for counterfactual task specification. To our knowledge this is the first generative model of whole-cortex fMRI dynamics for unseen cognitive tasks, advancing counterfactual neuroscience and data-driven experimental design.

---


### 137. [Designing AI-Supported Focus Groups: A Role x Modality Playbook](https://arxiv.org/abs/2606.11835)

**<font color=#1a73e8>作者：</font>** Zhiqing Wang, Steven Dow  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collecting participants' lived experiences is central to design research. Focus groups are uniquely valuable because participants not only share individual accounts but also respond to one another, surfacing comparison, disagreement, and collective sensemaking. However, focus groups are resource-intensive and highly sensitive to facilitation: moderators must probe for specificity, balance participation, manage topic flow, and sustain psychological safety, and subtle facilitation choices can shape what becomes salient. Recent HCI work and commercial meeting tools show that generative AI can scaffold live conversation through prompting, turn regulation, thematic mapping, and real-time summarization. Yet UXR teams lack a clear map of what these capabilities mean in focus groups and what methodological risks they introduce. We synthesize AI supports for live conversation and translate them into a focus-group-specific playbook organized by AI role (tool, co-host, host) and modality (text, voice, embodied).We synthesize prior work on AI-supported live conversation and propose a focus-group-specific playbook of AI supports organized by role (tool, co-host, host) and modality (text, voice, embodied). We characterize interactional trade-offs and identify open questions for evaluating AI-supported focus groups as methodological configurations.

---


### 138. [LASA: A Weak Supervision Method for Open-Vocabulary Scene Sketch Semantic Segmentation](https://arxiv.org/abs/2606.11837)

**<font color=#1a73e8>作者：</font>** Liwen Yi, Xianlin Zhang, Yue Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary scene sketch semantic segmentation aims to assign dense semantic labels to sparse line drawings based on flexible category vocabularies specified at inference time, without relying on pixel-level annotations during training. Unlike natural images, sketches lack texture and color cues, making semantic understanding heavily dependent on stroke layout and spatial configuration, a challenge that renders single-layer vision-language features inherently unstable. Our key observation is that attention maps from different Vision Transformer layers encode complementary spatial cues: shallow layers capture global structural layouts, while deeper layers focus on local stroke intersections and object parts. This suggests that cross-layer aggregation provides a more robust structural prior than any individual layer alone. Leveraging this insight, we propose a structure-aware framework built upon \textbf{L}ayer-wise \textbf{A}ccumulated \textbf{S}tructural \textbf{A}ttention (\textbf{LASA}), which aggregates multi-layer attention to guide hierarchical semantic alignment under weak supervision and refine predictions during inference. Experiments on FS-COCO, SFSD, and FrISS show that LASA improves mIoU by $+3.43$, $+8.01$, and $+15.74$ over the prior weakly supervised baselines, demonstrating consistent gains in both segmentation accuracy and spatial coherence. Our source code will be made publicly available.

---


### 139. [Plan-and-Verify Video Reward Reasoning with Spatio-Temporal Scene Graph Grounding](https://arxiv.org/abs/2606.11838)

**<font color=#1a73e8>作者：</font>** Hyomin Kim, Junghye Kim, Joanie Hayoun Chung 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models for text-to-video (T2V) generation guide post-training but often fail at fine-grained semantic alignment. We trace this to two structural weaknesses in existing reasoning-based reward models: they do not systematically verify every condition described in the prompt, and the visual evidence supporting each judgment remains implicit in their free-form reasoning. We propose SG-PVR, a video reward model that addresses these limitations through plan-and-verify reasoning grounded in spatio-temporal scene graphs. The verification plan decomposes the prompt into atomic claims, ensuring every requirement is checked. The spatio-temporal scene graph, encoding entities, attributes, and temporally-grounded relations, is extracted from the video and maintained as a persistent structured visual reference throughout reasoning. Each claim is verified against both the video and the scene graph, anchoring judgments in explicit visual evidence. SG-PVR achieves strong performance on semantic alignment, including fine-grained temporal semantics. As a test-time reranker, it further enhances compositional alignment in T2V generation.

---


### 140. [Systematic Cybersecurity Risk Analysis of European Rail Traffic Management System](https://arxiv.org/abs/2606.11839)

**<font color=#1a73e8>作者：</font>** Kacper Darowski, Sebastian N. Peters, Lukas Lautenschlager  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> European Rail Traffic Management System (ERTMS) is a widely adopted standard unifying train management in the EU. While the standard allows for use cases like fully autonomous driving, cybersecurity has been an afterthought. Risk analysis enables the systematic assessment and prioritization of threats and mitigations. To date, it remains unclear which threats are most significant in ERTMS. This study systematically models components of ERTMS and analyzes their security in light of threats identified in the underlying technologies. The results suggest a concerning state of ERTMS, despite its critical role in railway safety. The use of legacy standards like EuroBalises and GSM-Railway (GSM-R) introduces vulnerabilities that persist across minimal ERTMS implementations, deployments incorporating various optional safety measures, and prospective future evolutions of the system, e.g., adopting Future Railway Mobile Communication System (FRMCS). Fully transitioning to European Train Control System (ETCS) level 2 was identified as the most significant measure for advancing ERTMS cybersecurity. The results indicate that a shift of ERTMS toward security is required to ensure availability and safe operation. While the chosen methodology proved its feasibility and shows remaining weaknesses of ERTMS, future work is needed to develop railway-centric adaptations to improve the quantification and evaluation of the computed risks.

---


### 141. [Scene-Adaptive Nonlinear Tone Curves for Pseudo Ground-Truth Generation in Low-Light 3D Gaussian Splatting](https://arxiv.org/abs/2606.11841)

**<font color=#1a73e8>作者：</font>** Mingzhe Lyu, Jinqiang Cui, Hong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light novel view synthesis is challenging because dark multi-view images contain noise, weak structural detail, and compressed dynamic range. Recent 3D Gaussian Splatting (3DGS) methods address these challenges by generating pseudo ground-truth (pseudo-GT) images as supervision targets when paired normal-light references are unavailable. Existing pseudo-GT methods apply a uniform linear gain to all pixels, which clips bright regions while providing insufficient enhancement in dark regions, limiting reconstruction quality. We observe that nonlinear tone mappings, long established in 2D low-light enhancement, have not been explored for pseudo-GT generation in 3D reconstruction. Accordingly, we propose a scene-adaptive nonlinear tone-curve framework that replaces linear pseudo-GT with nonlinear alternatives. The framework introduces percentile-based normalisation for scene-agnostic curve application, a scene-adaptive offset for automatic black-level adjustment, and two complementary curves: Adaptive SoftExp (ASE), a bounded exponential curve, and Adaptive Poly3 (AP3), a data-driven cubic polynomial. The module changes only the pseudo-GT computation and leaves the 3DGS backbone unchanged. Experiments on three benchmarks covering 21 scenes show that both curves consistently outperform the linear baseline with PSNR improvements up to +4.34 dB on LOM and +3.25 dB on RealX3D. Both curves achieve similar performance despite their different mathematical forms, suggesting the improvement is curve-agnostic. Code is available at this https URL

---


### 142. [TaskFusion: Continual Anomaly Detection for Heterogeneous Tabular Data](https://arxiv.org/abs/2606.11844)

**<font color=#1a73e8>作者：</font>** Dayananda Herurkar, Federico Raue, Joachim Folz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual anomaly detection in tabular data is challenging and remains largely underexplored, particularly in settings with heterogeneous feature schemas, distribution shifts, and severe class imbalance. In many real-world applications, data arrive sequentially from diverse domains, rendering conventional continual learning methods ineffective due to their reliance on a fixed input space. We propose a continual learning (CL) method, which can overcome these challenges and continually learn from different tasks. Our method consists of three main parts: our AGF model, Taskfusion augmentation, and outlier exposure. The AGF-model maps task-specific features into a shared space, then aligns distributions to reduce representation drift, and learns anomaly decision boundaries in the aligned space. To improve stability, we introduce Taskfusion augmentation, combining boundary-aware interpolation within tasks to refine the model anomaly boundaries and cross-task mixing to transfer anomaly structure across datasets. To handle class imbalance and memory constraints, we employ tabular dataset distillation to store compact synthetic replay samples, which are jointly used with augmented data in an outlier exposure objective for robust anomaly detection. We evaluate the approach on 21 heterogeneous datasets across multiple domains. Results show that our approach substantially improves continual anomaly detection performance over sequential fine-tuning and other CL baselines while reducing catastrophic forgetting and maintaining stable detection across heterogeneous datasets.

---


### 143. [SheafStain: Sheaf-Theoretic Schrödinger Bridge for Spatially and Biologically Coherent Virtual Staining](https://arxiv.org/abs/2606.11846)

**<font color=#1a73e8>作者：</font>** Hyeongyeol Lim, Hongjun Yoon, Eunjin Jang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current virtual staining approaches offer the potential for time- and cost-efficient biomarker quantification in cancer diagnostics and prognostics. However, patch-wise inference for gigapixel whole slide images (WSIs) fails to maintain spatial continuity, yielding artifacts that cause catastrophic mismatches with ground-truth images. Although pathology Vision Foundation Models (VFMs) offer rich representations, their self-attention causes varying global contexts to produce inconsistent embeddings for the same physical region. We formalize and validate this ``context contamination'' as a sheaf-theoretic problem where these embeddings form a presheaf that violates the gluing axiom. To address this, we propose SheafStain, a new approach that reinterprets VFM features as sheaf-like sections for spatially and biologically coherent virtual staining. Specifically, SheafStain integrates class and patch tokens into a Schrödinger Bridge framework as sheaf-like sections. While the class token anchors biological consistency, patch tokens form a per-position spatial map. A backbone co-pretrained on Hematoxylin \& Eosin (H\&E) and Immunohistochemistry (IHC) yields non-degenerate cross-stain stalks, so a single VFM feature space supervises both input conditioning and output stain alignment. Departing from prior work that evaluates on isolated $256 \times 256$ patches and either random-crops or resizes the $1024 \times 1024$ ground truth, we translate at $256 \times 256$ and evaluate on the stitched $1024 \times 1024$ outputs across HER2, ER, PR, and Ki-67. SheafStain demonstrates promising results against six prior methods while mitigating patch-boundary stitching artifacts. Code will soon be released.

---


### 144. [StatefulDiscovery: Evidence-Calibrated Claim Formation in Open-Ended Scientific Discovery](https://arxiv.org/abs/2606.11851)

**<font color=#1a73e8>作者：</font>** Jiayao Chen, Shi Liu, Linyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-ended scientific discovery asks agents to move beyond executing analyses for predefined questions. Across multiple rounds of exploration, a discovery agent must decide which phenomena warrant investigation while avoiding overinterpretation, where emerging claims exceed the evidential scope of the analyses supporting them. This creates an evidence-calibration problem: the exploration trajectory must be coupled with claim status so that evidence can guide both what to investigate next and what can be claimed. We introduce StatefulDiscovery, a discovery framework that externalizes investigation state and uses it to coordinate frontier selection, evidence acquisition, and claim adjudication. We evaluate StatefulDiscovery across 40 real-data discovery tasks. Compared with several baselines, StatefulDiscovery produces more claims overall judged to be both well-supported and high-value. Ablations indicate that structured hypotheses, local adjudication, and frontier control contribute to performance. Together, these results suggest that explicit discovery state can couple exploration with evidence-calibrated claim formation.

---


### 145. [RePAIR: Predictive Self-Supervised Representation Learning in Chess](https://arxiv.org/abs/2606.11860)

**<font color=#1a73e8>作者：</font>** Christoph Koller, Johannes Fürnkranz, Timo Bertram  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce Representation Prediction via Autoencoding using Iterative Refinement (RePAIR) - a novel self-supervised representation learning architecture that synthesizes Masked Autoencoders (MAE), Joint Embedding Predictive Architectures (JEPA), and Bidirectional Encoder Representations from Transformers (BERT). We demonstrate how it can be used to encode objects in sequential data like consecutive chess positions into compact yet meaningful representations. The basic principle of the architecture is to mask large portions of a sequence of latent states, similar to BERT and MAE. Then, we apply a lightweight Predictor to the latent representations that repairs gaps in the sequence in a lower-dimensional embedding space akin to JEPA. Our experiments in the domain of chess show that the Encoder refines the board representations such that meaningful chess concepts emerge clustered in the latent space. Furthermore, reconstructions of the masked board states show that the model is able to reason about the piece movements without relying on costly reinforcement learning methods. Lastly, we find that the resulting representation space allows for quick and intuitive dissections of chess games by observing the game path trajectories in this semantically rich space.

---


### 146. [MemNovo: Look Back at the Spectrum for Balanced De Novo Peptide Sequencing from Mass Spectrometry](https://arxiv.org/abs/2606.11868)

**<font color=#1a73e8>作者：</font>** Dongxin Lyu, Jingbo Zhou, Hongxin Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> De novo peptide sequencing from tandem mass spectrometry is pivotal in proteomics, enabling identification of novel peptides without reference databases. While recent Transformer-based encoder-decoder models have achieved remarkable performance, we uncover a critical pathology in their inference dynamics. Through comprehensive feature scaling experiments, we demonstrate that existing auto-regressive peptide decoders tend to over-rely on generated-sequence priors while progressively under-utilizing fine-grained physical evidence from the input mass spectrum. This phenomenon leads to suboptimal results, where generated peptide sequences are biologically plausible yet not faithful to the input spectrum. To rectify this, we propose MemNovo, a training-free and plug-and-play mechanism that re-balances peptide and spectral contributions at inference time. MemNovo alleviates the information bottleneck by establishing a persistent spectral memory bank and injecting retrieved features directly into the final decoding stage via an ultra-conservative residual connection. Theoretical analysis confirms that this mechanism restores the mutual information between the decoder state and the raw spectrum. Extensive experiments on the Nine Species benchmark with two representative baselines, Casanovo and InstaNovo, demonstrate that MemNovo consistently improves both amino acid precision and peptide precision, achieving up to 39.1% relative improvement in peptide precision for Casanovo and up to 3.9% for InstaNovo, with negligible computational overhead.

---


### 147. [WarpGuard: Protected-Site Control-Flow Integrity for CUDA SASS Binaries](https://arxiv.org/abs/2606.11871)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent CUDA exploitation work shows that GPU memory bugs can escalate into device-side control-flow corruption, as kernels later consume corrupted return continuations, function pointers, dispatch-table entries, or branch targets. For deployed CUDA binaries, the relevant security boundary is executed NVIDIA SASS, after PTX lowering, inlining, ABI decisions, register allocation, spills, predication, and SIMT execution; source- or PTX-level policies do not capture this boundary.
We present WarpGuard, to our knowledge the first protected-site CFI system for CUDA device binaries operating on executed SASS. WarpGuard enforces at protected sites: recovered SASS instructions or sequences that consume control-flow state, provide sufficient binary evidence to derive policy, are checked before release, and fail closed on violation. It authenticates backward-edge continuation state for instrumented returns, validates recoverable forward targets per site, and reports fixed-edge, unsupported, profile-excluded, fallback, and no-surface outcomes outside the protected denominator.
On 77 CUDA artifacts, WarpGuard classifies 51,621 SASS control-flow sites, including 1,343 returns and 154 supported forward target-set entries, and records 52.2 million dynamic checks. In representative backward- and forward-edge corruption attacks, native execution reaches attacker-selected behavior, detect-only mode records the expected violation, and enforcement fails closed before releasing the invalid protected transfer. Public-code evidence shows that the same SASS consumption patterns occur in real CUDA systems, including runtime dispatch tables, cuFFT callbacks, generated callable tables, and uploaded device-function pointers. WarpGuard delivers auditable protected-site CFI for CUDA SASS and separates dynamic-instrumentation enforcement from callback-free SASS timing and patch-cache feasibility.

---


### 148. [AutoMine Solution for AV2 2026 Scenario Mining Challenge](https://arxiv.org/abs/2606.11874)

**<font color=#1a73e8>作者：</font>** Songliang Cao, Jiele Zhao, Yuru Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the development of autonomous driving systems, mining high-value, safety-critical, and planning-relevant scenarios from large-scale driving logs has become essential for data-driven evaluation. In this paper, we propose AutoMine, a robust self-refining scenario mining method based on LLMs and VLMs. AutoMine uses semantics-preserving prompt augmentation to reduce LLM prompt sensitivity, combines robust trajectory atomic functions with VLM-based functions to handle perception noise and open-world visual cues, and refines generated code through execution feedback from real logs. In the Argoverse 2 Scenario Mining Competition at CVPR 2026, AutoMine achieves a HOTA-Temporal score of 36.38 and a Timestamp BA score of 77.21.

---


### 149. [I Understand How You Feel: Enhancing Deeper Emotional Support Through Multilingual Emotional Validation in Dialogue System](https://arxiv.org/abs/2606.11875)

**<font color=#1a73e8>作者：</font>** Zi Haur Pang, Yahui Fu, Koji Inoue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotional validation - explicitly acknowledging that a user's feelings make sense - has proven therapeutic value but has received little computational attention. Emotional validation in dialogue systems can be decomposed into (i) validating response identification, (ii) validation timing detection, and (iii) validating response generation. To support research on all three subtasks, we release M-EDESConv, a 120k English-Japanese multilingual corpus created through hybrid manual and automatic annotation, and M-TESC, a multilingual spoken-dialogue test set. For timing detection, we propose MEGUMI, a Multilingual Emotion-aware Gated Unit for Mutual Integration, that fuses frozen XLM-RoBERTa semantics with language-specific emotion encoders via cross-modal attention and gated fusion. MEGUMI shows superior performance on both the M-EDESConv and M-TESC datasets, both objectively and subjectively. Finally, our EmoValidBench benchmarks of GPT-4.1 Nano and Llama-3.1 8B indicate that current LLMs generate contextually similar and diverse validating responses, but emotional understanding remains a major area for improvement. Project page: this https URL

---


### 150. [Gerrymandering the Warp: Non-Control-Data Attacks on CUDA Collective Decision](https://arxiv.org/abs/2606.11878)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CUDA collective operations often sit on security decision paths: votes accept batches, reductions aggregate evidence, shuffles select representatives, and barriers order checked state before use. Such decisions depend not only on computed values, but also on which lanes are represented, what evidence they contribute, which lane speaks for the group, and which checked state reaches commit. We identify this participation metadata as decision-making non-control data.
We define Collective Semantic Corruption (CSC), a non-control-data attack family in which range-valid masks, predicates, source lanes, descriptors, group labels, or epochs cause a CUDA-conforming collective to authorize a decision over the wrong membership, contribution, role, or validation-to-use state. The kernel reaches the intended collective site and executes the expected primitive; the primitive represents the wrong authority set.
We model CSC with a site-local participation-authority contract. A protected collective derives, recomputes, checks, or freezes membership, contribution, role, and temporal state before authorization. We evaluate CSC across NVIDIA CUDA collective primitives, trigger channels, compact workload-style kernels, reduced idiom bridges, and admission-guard harnesses. In a CUDA-defined contract-conformance suite spanning the four authority dimensions, corrupted participation metadata causes a trusted-reference mismatch in 102/102 instances, while hardened variants preserve that reference in 102/102. We report 13 synchronization-sensitive instances separately. We then introduce Collective Integrity Contracts (CIC), a wrapper discipline that binds participation metadata before collective use. For CUDA collective decisions, security depends on both the values computed and the participants represented.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-248](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
