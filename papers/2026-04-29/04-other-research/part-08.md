# 📦 其他研究 | 2026年04月29日

> 本类共 **437** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-437](./part-09.md)

---

### 351. [Self-Abstraction Learning for Effective and Stable Training of Deep Neural Networks](https://arxiv.org/abs/2604.24313)

**<font color=#1a73e8>作者：</font>** Wonyong Cho, Taemin Kim, Jungmin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large-scale deep neural networks effectively and stably is essential for applying deep learning across various fields. However, conventional methods, which rely on training a single large network, often encounter challenges such as gradient vanishing, overfitting and unstable learning. To overcome these limitations, we introduce Self-Abstraction Learning (SAL), a hierarchical framework. In SAL, networks are arranged by structural complexity, where the simplest topmost network is trained first and its hidden and output layers serve as guidance for the successively more complex networks below. This top-down sequential guidance effectively mitigates optimization issues, enabling stable training of deep architectures. Various experiments across MLP, CNN, and RNN architectures demonstrate that SAL consistently outperforms conventional methods, ensuring robust generalization even in data-scarce and complex network regimes.

---


### 352. [Don't Pause! Every prediction matters in a streaming video](https://arxiv.org/abs/2604.24317)

**<font color=#1a73e8>作者：</font>** Dibyadip Chatterjee, Zhanzhong Pang, Fadime Sener 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video models should respond the moment an event unfolds, not after the moment has passed. Yet existing online VideoQA benchmarks remain largely retrospective. They pause the video at fixed timestamps, pose questions about current or past events, and score models only at those moments. This protocol leaves streaming predictions untested. To close this gap, we introduce SPOT-Bench, featuring multi-turn proactive queries that evaluate general streaming perception and assistive capabilities required by an always-on, real-time assistant. SPOT-Bench comes with Timeliness-F1, a consolidated metric that measures streaming predictions by their temporal precision and balanced coverage across the entire video. Our benchmark reveals: (i) offline models detect events reliably but spam predictions unprompted; (ii) post-training for silence reduces spamming but induces unresponsiveness; (iii) half of the streaming video expects no response, which we term dead-time - compute spent here does not affect response latency. These findings motivate AsynKV, a training-free streaming adaptation of offline models, that retains their event perception while improving their streaming behavior. AsynKV features a long-short term memory, utilized efficiently by scaling compute during dead-time. It serves as a strong baseline on SPOT-Bench, outperforming existing streaming models, and achieves state-of-the-art on retrospective benchmarks.

---


### 353. [From Players to Participants: Citizen Science and Video Games to Understand Cognition](https://arxiv.org/abs/2604.24321)

**<font color=#1a73e8>作者：</font>** Syrine Salouhou, Edgar Dubourg, Maxwell Scott-Slade 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Citizen science is transforming how cognitive scientists study the human mind, and video games are at the heart of this shift. By embedding experimental tasks into engaging, game-like experiences, researchers can reach large, diverse populations while collecting rich behavioral data outside the lab. In this review, we explore how citizen science video games bridge the gap between players and participants, turning entertainment into large-scale cognitive research. Drawing on recent projects such as Sea Hero Quest and The Music Lab, we outline the key benefits of this approach: scalability, ecological validity, and public engagement. We also examine the challenges of designing games that are scientifically rigorous, ethically sound, and meaningful for both researchers and players. Through professional game developer insights, we highlight what it takes to develop a successful citizen science video game for cognitive science, and why this approach is still rare in the literature.

---


### 354. [Generative Design of a Gas Turbine Combustor Using Invertible Neural Networks](https://arxiv.org/abs/2604.24322)

**<font color=#1a73e8>作者：</font>** Patrick Krüger, Hanno Gottschalk, Werner Krebs 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The need to burn 100% H2 in high efficient gas turbines featuring low NOx combustion in premix mode require the complete redesign of the combustion system to ensure stable operation without any flashback. Since all engine frames featuring a power range from 4 MW up to 600 MW are affected, a huge design effort is expected. To reduce this effort, especially to transfer knowledge between the different engine classes, generative design methods using latest AI technology will provide promising potential. In this work, this challenge is approached utilizing the current advances in generative artificial intelligence. We train an Invertible Neural Network (INN) on an expandable database of geometrically parameterized combustor designs with simulated performance labels. Utilizing the INN in its inverse direction, multiple design proposals are generated which fulfill specified performance labels.

---


### 355. [X-NegoBox: An Explainable Privacy-Budget Negotiation Framework for Secure Peer-to-Peer Energy Data Exchange](https://arxiv.org/abs/2604.24326)

**<font color=#1a73e8>作者：</font>** Poushali Sengupta, Sabita Maharjan, Frank Eliassen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The decentralization of modern energy systems is transforming consumers into prosumers who continuously exchange data with aggregators, peers, and market operators. While such data is essential for peer-to-peer trading, demand response, and distributed forecasting, it can reveal sensitive household patterns and introduce privacy risks. Existing data sharing mechanisms rely on fixed policies or predefined differential privacy budgets, limiting their ability to adapt to variations in reliability, data sensitivity, and request purpose. As a result, prosumers rarely receive explanations for why a request is accepted, rejected, or modified, reducing trust and participation.
To address these limitations, we propose X-NegoBox, an explainable negotiation framework for adaptive privacy budgeting and transparent decision making. Each prosumer data is managed locally within a private DataBox, where raw data remain confined. Incoming requests are processed by an Autonomous Privacy Budget Negotiation Protocol (APBNP), which determines an appropriate privacy budget based on trust, feature sensitivity, declared purpose, historical behavior, and risk-aware pricing. When needed, APBNP generates privacy-preserving counter-offers, such as reduced resolution or duration.
An Explainable Agreement Layer (X-Contract) produces human- and machine-readable justifications for each decision. After agreement, requester code executes locally in a sandbox, and only sanitized outputs are shared. Experiments on realistic energy market settings show reduced privacy leakage, higher acceptance rates, and improved interpretability.

---


### 356. [Monocular Depth Estimation via Neural Network with Learnable Algebraic Group and Ring Structures](https://arxiv.org/abs/2604.24328)

**<font color=#1a73e8>作者：</font>** Qianlei Wang, Kexun Chen, Shaolin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation (MDE) has witnessed remarkable progress driven by Convolutional Neural Networks and transformer-based architectures. However, these approaches typically treat the problem as a generic image-to-image regression on Euclidean grids, thereby overlooking the intrinsic algebraic and geometric structures induced by perspective projection. To address this limitation, we propose LAGRNet, a novel framework that fundamentally grounds MDE in algebraic geometry by explicitly embedding learnable group, ring, and sheaf structures into the deep learning pipeline. Modeling feature maps as sections of a sheaf over an approximated image manifold, our method first establishes a Group-defined Feature Manifold (GFM) parameterized by a learned algebraic group action to enforce projective equivariance and robustness against view changes. To facilitate algebraically consistent cross-scale interactions, we subsequently introduce a Ring Convolution Layer (RCL) that formulates feature fusion as a graded ring homomorphism. Furthermore, to ensure global topological consistency, a Sheaf-based Module (SM) aggregates local depth cues via Čech nerve on the image topology. Extensive zero-shot evaluations across the KITTI, NYU-Depth V2, and ETH3D benchmarks demonstrate that LAGRNet significantly outperforms state-of-the-art methods in both accuracy and generalization capabilities.

---


### 357. [An Affordable,Wearable Stereo-Eye-Tracking Platform](https://arxiv.org/abs/2604.24331)

**<font color=#1a73e8>作者：</font>** Alexander Zimmer, Yasmeen Abdrabou, Enkelejda Kasneci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Research on video-based eye-tracking has long explored stereo and glint-based methods, yet existing wearable eye trackers - both commercial and open-source - offer limited flexibility for algorithm development and comparative evaluation. We present an affordable, wearable stereo eye-tracking platform built from off-the-shelf and 3D-printable components that explicitly targets this gap. The system combines four infrared eye cameras, infrared illumination, an optional scene camera, and software support for calibration and synchronized data acquisition. By design, the platform supports multiple eye-tracking paradigms, including stereo, glint-based, and binocular approaches, within a single hardware configuration. Rather than optimizing for end-user robustness, the platform prioritizes modularity and extensibility for research use. This paper focuses on the hardware architecture and calibration pipeline and demonstrates the feasibility of the approach using a prototype implementation. All hardware designs and documentation are made openly available.

---


### 358. [Mitigating Error Amplification in Fast Adversarial Training](https://arxiv.org/abs/2604.24332)

**<font color=#1a73e8>作者：</font>** Mengnan Zhao, Lihe Zhang, Bo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast Adversarial Training (FAT) has proven effective in enhancing model robustness by encouraging networks to learn perturbation-invariant representations. However, FAT often suffers from catastrophic overfitting (CO), where the model overfits to the training attack and fails to generalize to unseen ones. Moreover, robustness oriented optimization typically leads to notable performance degradation on clean inputs, and such degradation becomes increasingly severe as the perturbation budget grows. In this work, we conduct a comprehensive analysis of how guidance strength affects model performance by modulating perturbation and supervision levels across distinct confidence groups. The findings reveal that low confidence samples are the primary contributors to CO and the robustness accuracy trade off. Building on this insight, we propose a Distribution-aware Dynamic Guidance (DDG) strategy that dynamically adjusts both the perturbation budget and supervision signal. Specifically, DDG scales the perturbation magnitude according to the sample confidence at the ground truth class, thereby guiding samples toward consistent decision boundaries while mitigating the influence of learning spurious correlations. Simultaneously, it dynamically adjusts the supervision signal based on the prediction state of each sample, preventing overemphasis on incorrect signals. To alleviate potential gradient instability arising from dynamic guidance, we further design a weighted regularization constraint. Extensive experiments on standard benchmarks demonstrate that DDG effectively alleviates both CO and the robustness accuracy trade off.

---


### 359. [Perfecting Aircraft Maneuvers with Reinforcement Learning](https://arxiv.org/abs/2604.24338)

**<font color=#1a73e8>作者：</font>** Atahan Cilan, Mahir Demir, Özgün Can Yürütken 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper evaluates an advanced jet trainer's utilization of artificial intelligence (AI)-based aircraft aerobatic maneuvers with the intention of developing an AI-assisted pilot training module for specific aircraft maneuvers. A multitude of aircraft maneuvers have been simulated using reinforcement learning (RL) agents, which will serve as a training tool for future pilots.

---


### 360. [See Further, Think Deeper: Advancing VLM's Reasoning Ability with Low-level Visual Cues and Reflection](https://arxiv.org/abs/2604.24339)

**<font color=#1a73e8>作者：</font>** Zhiheng Wu, Tong Wang, Shuning Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Vision-Language Models (VLMs) have benefited from Reinforcement Learning (RL) for enhanced reasoning. However, existing methods still face critical limitations, including the lack of low-level visual information and effective visual feedback. To address these problems, this paper proposes a unified multimodal interleaved reasoning framework \textbf{ForeSight}, which enables VLMs to \textbf{See Further} with low-level visual cues and \textbf{Think Deeper} with effective visual feedback. First, it introduces a set of low-level visual tools to integrate essential visual information into the reasoning chain, mitigating the neglect of fine-grained visual features. Second, a mask-based visual feedback mechanism is elaborated to incorporate visual reflection into the thinking process, enabling the model to dynamically re-examine and update its answers. Driven by RL, ForeSight learns to autonomously decide on tool invocation and answer verification, with the final answer accuracy as the reward signal. To evaluate the performance of the proposed framework, we construct a new dataset, Character and Grounding SalBench (CG-SalBench), based on the SalBench dataset. Experimental results demonstrate that the ForeSight-7B model significantly outperforms other models with the same parameter scale, and even surpasses the current SOTA closed-source models on certain metrics.

---


### 361. [GoAT-X: A Graph of Auditing Thoughts for Securing Token Transactions in Cross-Chain Contracts](https://arxiv.org/abs/2604.24341)

**<font color=#1a73e8>作者：</font>** Zijun Feng, Yuming Feng, Yu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-chain bridges, the critical infrastructure of the multi-chain ecosystem, have become a primary target for attackers, resulting in over $2.8 billion in losses due to subtle implementation flaws. Existing defenses, such as bytecode-level static analysis, are ill-equipped to handle the semantic complexity of cross-chain interactions, while LLM-based approaches, which can understand source code, struggle with hallucinatory reasoning over complex, multi-contract dependencies. In this paper, we propose GoAT-X, a framework that shifts automated cross-chain smart contract codebases auditing from heuristic pattern matching toward systematic first-principles verification. GoAT-X structures the audit process as a Graph of Auditing Thoughts, explicitly mirroring how human experts decompose, reason about, and validate security logic. By anchoring LLM reasoning in statically extracted data flows and explicitly linking abstract security properties to concrete code implementations, the framework constrains semantic reasoning within well-defined structural and state boundaries. Within this constrained space, GoAT-X treats missing constraints and adversarial bypass paths in cross-chain logic as first-class vulnerability targets and dynamically explores reasoning paths to identify exploitable semantic gaps. We evaluate GoAT-X on a comprehensive benchmark covering all known cross-chain token transaction attacks. GoAT-X achieves 92% recall on fine-grained audit points and 95% coverage of vulnerable projects, while identifying 117 confirmed risks in the wild with low operational cost, establishing a new standard for scalable, logic-driven cross-chain security.

---


### 362. [SycoPhantasy: Quantifying Sycophancy and Hallucination in Small Open Weight VLMs for Vision-Language Scoring of Fantasy Characters](https://arxiv.org/abs/2604.24346)

**<font color=#1a73e8>作者：</font>** Arya Shah, Deepali Mishra, Chaklam Silpasuwanchai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed as evaluators in tasks requiring nuanced image understanding, yet their reliability in scoring alignment between images and text descriptions remains underexplored. We investigate whether small, open-weight VLMs exhibit \emph{sycophantic} behavior when evaluating image-text alignment: assigning high scores without grounding their judgments in visual evidence. To quantify this phenomenon, we introduce the \emph{Bluffing Coefficient} (\bc), a metric that measures the mismatch between a model's score and its evidence recall. We evaluate six open-weight VLMs ranging from 450M to 8B parameters on a benchmark of 173,810 AI-generated character portraits paired with detailed textual descriptions. Our analysis reveals a significant inverse correlation between model size and sycophancy rate ($r = -0.96$, $p = 0.002$), with smaller models exhibiting substantially higher rates of unjustified high scores. The smallest model tested (LFM2-VL, 450M) produced sycophantic evaluations in 22.3\% of cases, compared to 6.0\% for the largest (LLaVA-1.6, 7B). These findings have direct implications for the deployment of small, open-weight VLMs as automated evaluators within attribute-rich, synthetic image evaluation tasks, where the gap between assigned scores and cited visual evidence is both measurable and consequential.

---


### 363. [Unveiling the Backdoor Mechanism Hidden Behind Catastrophic Overfitting in Fast Adversarial Training](https://arxiv.org/abs/2604.24350)

**<font color=#1a73e8>作者：</font>** Mengnan Zhao, Lihe Zhang, Tianhang Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast Adversarial Training (FAT) has attracted significant attention due to its efficiency in enhancing neural network robustness against adversarial attacks. However, FAT is prone to catastrophic overfitting (CO), wherein models overfit to the specific attack used during training and fail to generalize to others. While existing methods introduce diverse hypotheses and propose various strategies to mitigate CO, a systematic and intuitive explanation of CO remains absent. In this work, we innovatively interpret CO through the lens of backdoor. Through validations on pathway division, diverse feature predictions, and universal class distinguishable triggers in CO, we conceptualize CO as a weak trigger variant of unlearnable tasks, unifying CO, backdoor attacks, and unlearnable tasks under a common theoretical framework. Guided by this, we leverage several backdoor inspired strategies to mitigate CO: (i) Recalibrate CO affected model parameters using vanilla fine tuning, linear probing, or reinitialization-based techniques; (ii) Introduce a weight outlier suppression constraint to regulate abnormal deviations in model weights. Extensive experiments support our interpretation of CO and show the efficacy of the proposed mitigation strategies.

---


### 364. [Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion](https://arxiv.org/abs/2604.24351)

**<font color=#1a73e8>作者：</font>** Zhongjie Duan, Hong Zhang, Yingda Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controllable diffusion methods have substantially expanded the practical utility of diffusion models, but they are typically developed as isolated, backbone-specific systems with incompatible training pipelines, parameter formats, and runtime hooks. This fragmentation makes it difficult to reuse infrastructure across tasks, transfer capabilities across backbones, or compose multiple controls within a single generation pipeline. We present Diffusion Templates, a unified and open plugin framework that decouples base-model inference from controllable capability injection. The framework is organized around three components: Template models that map arbitrary task-specific inputs to an intermediate capability representation, a Template cache that functions as a standardized interface for capability injection, and a Template pipeline that loads, merges, and injects one or more Template caches into the base diffusion runtime. Because the interface is defined at the systems level rather than tied to a specific control architecture, heterogeneous capability carriers such as KV-Cache and LoRA can be supported under the same abstraction. Based on this design, we build a diverse model zoo spanning structural control, brightness adjustment, color adjustment, image editing, super-resolution, sharpness enhancement, aesthetic alignment, content reference, local inpainting, and age control. These case studies show that Diffusion Templates can unify a broad range of controllable generation tasks while preserving modularity, composability, and practical extensibility across rapidly evolving diffusion backbones. All resources will be open sourced, including code, models, and datasets.

---


### 365. [ARETE: Attention-based Rasterized Encoding for Topology Estimation using HSV-transformed Crowdsourced Vehicle Fleet Data](https://arxiv.org/abs/2604.24353)

**<font color=#1a73e8>作者：</font>** Daniel Fritz, Dimitrios Lagamtzis, Michael Mink 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The continuous advancement of autonomous driving (AD) introduces challenges across multiple disciplines to ensure safe and efficient driving. One such challenge is the generation of High-Definition (HD) maps, which must remain up to date and highly accurate for downstream automotive tasks. One promising approach is the use of crowdsourced data from a vehicle fleet, representing road topology and lane-level features. This work focuses on the generation of centerlines and lane dividers from crowdsourced vehicle trajectories. We adopt a Detection Transformer (DETR)-based approach, where a rasterized representation of vehicle trajectories is used as input to predict vectorized lane representations. Each lane consists of a centerline with an associated direction and corresponding lane dividers that are geometrically constrained by the centerline. Our method includes the extraction of local tiles, from which crowdsourced vehicle trajectories are aggregated. Each tile undergoes a transformation into a rasterized representation encoding both the presence and direction of each trajectory, enabling the prediction of vectorized directed lanes. Experiments are conducted on an internal dataset as well as on the public datasets nuScenes and nuPlan.

---


### 366. [An Aircraft Upset Recovery System with Reinforcement Learning](https://arxiv.org/abs/2604.24355)

**<font color=#1a73e8>作者：</font>** Mahir Demir, Atahan Cilan, Seyyid Osman Sevgili 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article explores the progress made in the creation of a pilot activated recovery system (PARS) for advanced jet trainers that utilizes artificial intelligence (AI) in an effort to enhance operational efficiency. The PARS model employs an advanced reinforcement learning (RL) architecture, incorporating a cutting-edge soft-actor critic (SAC) model and hyper-parameter optimization methods. Negative-g punishments and other handcrafted features remarked upon by control engineers and domain experts regarding PARS are also taken into account by the system. When evaluated by them, the AI model's behavior is deemed more desirable than that of conventional control methods.

---


### 367. [SAGE: Sparse Adaptive Guidance for Dependency-Aware Tabular Data Generation](https://arxiv.org/abs/2604.24368)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Zheyu Zhang, Bardh Prenkaj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating high-fidelity synthetic tabular data remains a critical challenge for enhancing data availability in privacy-sensitive and low-resource domains. Recent approaches leverage LLMs by representing table rows as sequences, yet suffer from two fundamental limitations: (1) they model feature dependencies densely, introducing spurious correlations; and (2) they assume static relationships between features, ignoring how these dependencies vary with feature values. To overcome these limitations, we introduce SAGE (Sparse Adaptive Guidance), a novel LLM-based generation framework that enforces sparse and dynamic dependency guidance. SAGE discretizes features into value-aware pseudo-features and constructs a mutual information-based sparse dependency graph. This graph adaptively guides generation through explicit context selection or implicit logit correction, enabling LLMs to focus on truly relevant information during synthesis. Our extensive experiments across six datasets and multiple tasks reveal that SAGE not only improves data fidelity and downstream utility, boosting F1 scores by 10% compared to previous LLM-based methods, but also reduces policy violations by one point. These results highlight the importance of adaptive structure in tabular data generation and provide new insights into context-sensitive control of LLMs.

---


### 368. [Multispectral airborne laser scanning dataset for tree species classification: MS-ALS-SPECIES](https://arxiv.org/abs/2604.24370)

**<font color=#1a73e8>作者：</font>** Matti Hyyppä, Klaara Salolahti, Eric Hyyppä 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The shift from stand-level to individual-tree-level forest assessments supports improved biodiversity mapping, particularly in boreal ecosystems where tree species like aspen (Populus tremula L.) play a keystone role. While airborne laser scanning (ALS) is the standard for such inventories, a major limitation is the small number of publicly available ALS datasets containing high-quality, field-validated reference data. Furthermore, open multispectral ALS datasets with high-quality field reference data are completely lacking despite the potential of multispectral ALS data for tree species classification. This paper presents and details an open multispectral ALS dataset used in a recent international benchmarking study of machine learning and deep learning methods for tree species classification by Taher et al. (2026). The dataset comprises 6326 segment-level point clouds of individual trees representing nine species in Southern Finland. The point cloud data has been acquired using two multispectral laser scanning systems each operating at three laser wavelengths: a helicopter-borne system (HeliALS) with a point density exceeding 1000 points/m$^2$ and an Optech Titan system with approximately 35 points/m$^2$. We provide a detailed description of field data collection techniques developed in the study to facilitate the collection of high-quality ground truth data in an efficient and scalable manner. Additionally, our article presents new analyses on species classification using multispectral data building upon the initial findings of Taher et al. (2026). Furthermore, we study the relation between classification accuracy and tree height to highlight the versatility of the open dataset and to demonstrate the advantage of the point transformer model for small trees and minority species.

---


### 369. [PathMoG: A Pathway-Centric Modular Graph Neural Network for Multi-Omics Survival Prediction](https://arxiv.org/abs/2604.24371)

**<font color=#1a73e8>作者：</font>** Di Wang, Chupei Tang, Junxiao Kong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cancer survival prediction from multi-omics data remains challenging because prognostic signals are high-dimensional, heterogeneous, and distributed across interacting genes and pathways. We propose PathMoG, a pathway-centric modular graph neural network for multi-omics survival prediction. PathMoG reorganizes genome-scale inputs into 354 KEGG-informed pathway modules, introduces a Hierarchical Omics Modulation module to condition gene-expression representations on mutation, copy number variation, pathway, and clinical context, and uses dual-level attention to capture both intra-pathway driver signals and inter-pathway clinical relevance. We evaluated PathMoG on 5,650 patients across 10 TCGA cancer types and observed consistent improvements over representative survival baselines. The framework further provides gene-level, pathway-level, and patient-level interpretability, supporting biologically grounded and clinically relevant risk stratification.

---


### 370. [SeaEvo: Advancing Algorithm Discovery with Strategy Space Evolution](https://arxiv.org/abs/2604.24372)

**<font color=#1a73e8>作者：</font>** Sichun Luo, Yi Huang, Haochen Luo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-guided evolutionary search has emerged as a promising paradigm for automated algorithm discovery, yet most systems track search progress primarily through executable programs and scalar fitness. Even when natural-language reflection is used, it is often used locally in mutation prompts or stored without an explicit population-level organization of strategic directions. As a result, evolutionary search can struggle to distinguish syntactically different implementations of the same idea, preserve lower-fitness but strategically promising directions, or detect when an entire family of strategies has saturated.
We introduce \model, a modular strategy-space layer that elevates natural-language strategy descriptions from transient prompt context to first-class population-level evolutionary state in LLM-driven program search. \model augments each candidate program with an explicit natural language strategy description and uses this representation in three ways: Strategy Articulation turns mutation into a diagnose-direct-implement process; Stratified Experience Retrieval organizes the archive into strategy clusters and selects inspirations by behavioral complementarity; and Strategic Landscape Navigation periodically summarizes effective, saturated, and underexplored strategy families to guide future mutations. Across mathematical algorithm discovery, systems optimization, and agent-scaffold benchmarks, \model improves the underlying evolutionary backbones in most settings, with particularly large gains (21% relative improvement) on open-ended system optimization tasks. These results suggest that persistent strategy representations provide a practical mechanism for improving the robustness and efficiency of LLM-guided evolutionary search, suggesting a path toward compound AI systems that accumulate algorithmic knowledge over time.

---


### 371. [MIPIC: Matryoshka Representation Learning via Self-Distilled Intra-Relational and Progressive Information Chaining](https://arxiv.org/abs/2604.24374)

**<font color=#1a73e8>作者：</font>** Phung Gia Huy, Hai An Vu, Minh-Phuc Truong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Representation learning is fundamental to NLP, but building embeddings that work well at different computational budgets is challenging. Matryoshka Representation Learning (MRL) offers a flexible inference paradigm through nested embeddings; however, learning such structures requires explicit coordination of how information is arranged across embedding dimensionality and model depth. In this work, we propose MIPIC (Matryoshka Representation Learning via Self-Distilled Intra-Relational Alignment and Progressive Information Chaining), a unified training framework designed to produce structurally coherent and semantically compact Matryoshka representations. MIPIC promotes cross-dimensional structural consistency through Self-Distilled Intra-Relational Alignment (SIA), which aligns token-level geometric and attention-driven relations between full and truncated representations using top-k CKA self-distillation. Complementarily, it enables depth-wise semantic consolidation via Progressive Information Chaining (PIC), a scaffolded alignment strategy that incrementally transfers mature task semantics from deeper layers into earlier layers. Extensive experiments on STS, NLI, and classification benchmarks (spanning models from TinyBERT to BGEM3, Qwen3) demonstrate that MIPIC yields Matryoshka representations that are highly competitive across all capacities, with significant performance advantages observed under extreme low-dimensional.

---


### 372. [Learning Evidence of Depression Symptoms via Prompt Induction](https://arxiv.org/abs/2604.24376)

**<font color=#1a73e8>作者：</font>** Eliseo Bao, Anxo Perez, David Otero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression places substantial pressure on mental health services, and many people describe their experiences outside clinical settings in high-volume user-generated text (e.g., online forums and social media). Automatically identifying clinical symptom evidence in such text can therefore complement limited clinical capacity and scale to large populations. We address this need through sentence-level classification of 21 depression symptoms from the BDI-II questionnaire, using BDI-Sen, a dataset annotated for symptom relevance. This task is fine-grained and highly imbalanced, and we find that common LLM approaches (zero-shot, in-context learning, and fine-tuning) struggle to apply consistent relevance criteria for most symptoms. We propose Symptom Induction (SI), a novel approach which compresses labeled examples into short, interpretable guidelines that specify what counts as evidence for each symptom and uses these guidelines to condition classification. Across four LLM families and eight models, SI achieves the best overall weighted F1 on BDI-Sen, with especially large gains for infrequent symptoms. Cross-domain evaluation on an external dataset further shows that induced guidelines generalize across other diseases shared symptomatology (bipolar and eating disorders).

---


### 373. [Certified geometric robustness -- Super-DeepG](https://arxiv.org/abs/2604.24379)

**<font color=#1a73e8>作者：</font>** Noémie Cohen, Mélanie Ducoffe, Christophe Gabreau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-critical applications are required to perform as expected in normal operations. Image processing functions are often required to be insensitive to small geometric perturbations such as rotation, scaling, shearing or translation. This paper addresses the formal verification of neural networks against geometric perturbations on their image dataset. Our method Super-DeepG improves the reasoning used in linear relaxation techniques and Lipschitz optimization, and provides an implementation that leverages GPU hardware. By doing so, Super-DeepG achieves both precision and computational efficiency of robustness certification, to an extent that outperforms prior work. Super-DeepG is shared as an open-source tool on GitHub.

---


### 374. [Information-Theoretic Distributed Point Functions with Shorter Keys](https://arxiv.org/abs/2604.24385)

**<font color=#1a73e8>作者：</font>** Hang Deng, Liang Feng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A t-private n-server Information-Theoretic Distributed Point Function ((t,n)-ITDPF) allows one to convert any point function f_{alpha,beta}(x): [N] -> G into n shares (secret keys), such that each server can compute an additive share of f_{alpha,beta}(x) with a key while any <= t servers learn absolutely no information about the function. This paper constructs a novel share conversion based on the private information retrieval (PIR) of Ghasemi, Kopparty, and Sudan (STOC 2025) and proposes a perfectly secure 1-private ITDPF with output group G = Z_p, where p can be any prime. Compared with the existing perfectly secure ITDPFs for the same output group, the proposed ITDPF is more efficient with asymptotically shorter secret keys.

---


### 375. [Complexity of Linear Regions in Self-supervised Deep ReLU Networks](https://arxiv.org/abs/2604.24393)

**<font color=#1a73e8>作者：</font>** Mufhumudzi Muthivhi, Terence L. van Zyl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There has been growing interest in studying the complexity of Rectified Linear Unit (ReLU) based activation networks. Recent work investigates the evolution of the number of piecewise-linear partitions (linear regions) that are formed during training. However, current research is limited to examining the complexity of models trained in a supervised way. Self-Supervised Learning (SSL) differs in that it directly optimises the representation space using a loss function to enhance the model's performance across multiple downstream tasks. This study investigates the local distribution of linear regions produced by SSL models. We demonstrate that the evolution of linear regions correlates with the representation quality by utilising SplineCam to extract two-dimensional polytopes near the data distribution. We track the number, area, eccentricity, and boundaries of regions throughout training. The study compares supervised, contrastive, and self-distillation methods over two standard benchmark datasets, MNIST and FashionMNIST. The analysis of the experimental results shows that self-supervised methods create substantially fewer regions to achieve comparable accuracy to supervised models. Contrastive methods rapidly expand regions over time, whereas self-distillation methods tend to consolidate by merging neighbouring regions. Lastly, we can detect representation collapse early within the geometric space of linear regions. Our analysis suggests that polytopal metrics can serve as reliable indicators of representation quality and model performance.

---


### 376. [An Automatic Ground Collision Avoidance System with Reinforcement Learning](https://arxiv.org/abs/2604.24403)

**<font color=#1a73e8>作者：</font>** Seyyid Osman Sevgili, Atahan Cilan, Mahir Demir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article evaluates an artificial intelligence (AI)-based Automatic Ground Collision Avoidance System (AGCAS) designed for advanced jet trainers to enhance operational effectiveness. In the continuously evolving field of aerospace engineering, the integration of AI is crucial for advancing operations with improved timing constraints and efficiency. Our study explores the design process of an AI-driven AGCAS, specifically tailored for advanced jet trainers, focusing on addressing the AGCAS problem within a limited observation space. The system utilizes line-of-sight queries on a terrain server to ensure precise and efficient collision avoidance. This approach aims to significantly improve the safety and operational capabilities of advanced jet trainers.

---


### 377. [From Spoofing to Trust: Emergency Alerts Spoofing Testbed and Cross-Cell Verification](https://arxiv.org/abs/2604.24404)

**<font color=#1a73e8>作者：</font>** Abdallah Abou Hasna, Nada Chendeb, Ammar El Falou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public warning systems (PWS) in cellular networks enable authorities to broadcast emergency alerts to all mobile phones in a geographic region in the event of threats such as earthquakes or severe weather. If an attacker can imitate these alerts and transmit a forged warning containing fake news or phishing links, the impact could range from public panic to user compromise. In this work, we present the first open-source 5G emergency alert spoofing attack, implemented by modifying the openairinterface (OAI) radio access network (RAN) code and executed using a software-defined radio, complemented by a custom network management system to automate network and warning configuration. We conduct a detailed analysis of how different smartphones behave under various conditions. Our findings show that while devices readily display spoofed alerts, the alerting mechanism enables multiple practical attack scenarios beyond simple warning display. Finally, to address this threat, we propose and implement a lightweight cross-cell verification mechanism in OAI, in which the device compares the received warning with neighboring cell broadcasts to flag single-source alerts as suspicious.

---


### 378. [AD-Relight: Training-Free Banner Relighting via Illumination Translation with Diffusion Priors](https://arxiv.org/abs/2604.24407)

**<font color=#1a73e8>作者：</font>** Rameshwar Mishra, A V Subramanyam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The recent surge in content consumption through streaming services has driven a growing demand for personalized content. Personalized advertisements (ads) play a crucial role in enhancing both user engagement and ad effectiveness. A key aspect of ad personalization involves replacing existing regions in a frame with custom, Photoshop-generated banners. However, existing ad-placement pipelines typically rely on simple geometric warping, ignoring the scene's underlying lighting conditions. Similarly, state-of-the-art diffusion-based object insertion and relighting models struggle to accurately relight these newly inserted banners, as they are not trained on ad-banner data, and training such a model for ad banners would require millions of images. This highlights the need for an effective relighting framework that enables seamless integration of custom banners into the original scene. Motivated by this, we present AD-Relight, a novel multi-stage training-free framework that adapts a diffusion-based relighting model at test time to relight newly added Photoshop-generated ad banners. Through extensive evaluation, we demonstrate that AD-Relight outperforms both relighting baselines and existing ad-placement methods based on simple warping. User studies further show that participants consistently prefer the outputs of AD-Relight over those of prior approaches.

---


### 379. [BMD-45: A Large-Scale CCTV Vehicle Detection Dataset for Urban Traffic in Developing Cities](https://arxiv.org/abs/2604.24419)

**<font color=#1a73e8>作者：</font>** Akash Sharma, Chinmay Mhatre, Sankalp Gawali 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust vehicle detection from fixed CCTV cameras is critical for Intelligent Transportation Systems. Yet existing benchmarks predominantly feature relatively homogeneous, highly organized traffic patterns captured from ego-centric driving perspectives or controlled aerial views. This regional and sensor view bias creates a significant gap. Models trained on datasets such as UA-DETRAC and COCO struggle to generalize to the dense, heterogeneous, disorganized traffic conditions observed in rapidly developing urban centers in emerging economies. To address this limitation, we introduce BMD-45, a large-scale dataset comprising 480K bounding boxes annotated over 45K images captured from over 3.6K operational Safe City CCTV cameras. BMD-45 contains 14 fine-grained vehicle categories, including region-specific modes such as auto-rickshaws and tempo travellers, which are not present in existing benchmarks. The dataset captures real-world deployment challenges, including extreme viewpoint variation, occlusion, and vehicle density . We establish comprehensive baselines using state-of-the-art detectors and reveal a striking domain gap: models fine-tuned on UA-DETRAC achieve only 33.6% mAP@0.50:0.95, compared to 83.8% when trained in-domain on BMD-45, representing a 2.5x improvement that persists even when accounting for novel vehicle classes. This performance gap underscores the critical need for geographically diverse traffic benchmarks and establishes BMD-45 as a baseline for developing robust perception systems in underrepresented urban environments worldwide. The dataset is available at: this https URL.

---


### 380. [DYMAPIA: A Multi-Domain Framework for Detecting AI-based Video Manipulation](https://arxiv.org/abs/2604.24426)

**<font color=#1a73e8>作者：</font>** Md Shohel Rana, Andrew H. Sung  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated media are advancing rapidly, raising pressing concerns for content authenticity and digital trust. We introduce DYMAPIA, a multi-domain Deepfake detection framework that fuses spatial, spectral, and temporal cues to capture subtle traces of manipulation in visual data. The system builds dynamic anomaly masks by combining evidence from Fourier spectra, local texture descriptors, edge irregularities, and optical flow consistency, which highlight tampered regions with fine spatial accuracy. These masks guide DistXCNet, a lightweight classifier distilled from Xception and optimized with depthwise separable convolutions for fast, region-focused classification. This joint design achieves state-of-the-art results, with accuracy and F1-scores exceeding 99\% on FF++, Celeb-DF, and VDFD benchmarks, while keeping the model compact enough for real-time use. Beyond outperforming existing full-frame and multidomain detectors, DYMAPIA demonstrates deployment readiness for time-critical forensic tasks, including media verification, misinformation defense, and secure content filtering.

---


### 381. [Kwai Summary Attention Technical Report](https://arxiv.org/abs/2604.24432)

**<font color=#1a73e8>作者：</font>** Chenglong Chu, Guorui Zhou, Guowang Zhang 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context ability, has become one of the most important iteration direction of next-generation Large Language Models, particularly in semantic understanding/reasoning, code agentic intelligence and recommendation system. However, the standard softmax attention exhibits quadratic time complexity with respect to sequence length. As the sequence length increases, this incurs substantial overhead in long-context settings, leading the training and inference costs of extremely long sequences deteriorate rapidly. Existing solutions mitigate this issue through two technique routings: i) Reducing the KV cache per layer, such as from the head-level compression GQA, and the embedding dimension-level compression MLA, but the KV cache remains linearly dependent on the sequence length at a 1:1 ratio. ii) Interleaving with KV Cache friendly architecture, such as local attention SWA, linear kernel GDN, but often involve trade-offs among KV Cache and long-context modeling effectiveness. Besides the two technique routings, we argue that there exists an intermediate path not well explored: {Maintaining a linear relationship between the KV cache and sequence length, but performing semantic-level compression through a specific ratio $k$}. This $O(n/k)$ path does not pursue a ``minimum KV cache'', but rather trades acceptable memory costs for complete, referential, and interpretable retention of long distant dependency. Motivated by this, we propose Kwai Summary Attention (KSA), a novel attention mechanism that reduces sequence modeling cost by compressing historical contexts into learnable summary tokens.

---


### 382. [Envisioning Mobile Data Visualization Libraries for Digital Health](https://arxiv.org/abs/2604.24448)

**<font color=#1a73e8>作者：</font>** Bongshin Lee, Seongjae Bae, Mengying Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile health (mHealth) applications support health management through rich data collection and self-reflection, yet the quality of their visualizations varies widely. A key limitation is the suboptimal design of visualizations for small-screen devices. We argue that this gap is partly driven by a lack of specialized developer tools. Existing libraries primarily target desktop or general-purpose mobile use, providing limited support for health-specific semantics such as normal ranges, thresholds, and goals. As a result, developers often resort to custom solutions that are inconsistent or hard to interpret. We therefore advocate for dedicated mobile visualization libraries tailored to personal health data and mobile contexts, and discuss key design considerations including intelligent defaults, built-in health annotations, and fluid interactions. Such libraries can lower barriers, promote consistency, and enable more accessible and interpretable mHealth applications.

---


### 383. [TextGround4M: A Prompt-Aligned Dataset for Layout-Aware Text Rendering](https://arxiv.org/abs/2604.24459)

**<font color=#1a73e8>作者：</font>** Dongxing Mao, Yilin Wang, Linjie Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in text-to-image generation, models still struggle to accurately render prompt-specified text with correct spatial layout -- especially in multi-span, structured settings. This challenge is driven not only by the lack of datasets that align prompts with the exact text and layout expected in the image, but also by the absence of effective metrics for evaluating layout quality. To address these issues, we introduce TextGround4M, a large-scale dataset of over 4 million prompt-image pairs, each annotated with span-level text grounded in the prompt and corresponding bounding boxes. This enables fine-grained supervision for layout-aware, prompt-grounded text rendering. Building on this, we propose a lightweight training strategy for autoregressive T2I models that appends layout-aware span tokens during training, without altering model architecture or inference behavior. We further construct a benchmark with stratified layout complexity to evaluate both open-source and proprietary models in a zero-shot setting. In addition, we introduce two layout-aware metrics to address the long-standing lack of spatial evaluation in text rendering. Our results show that models trained on TextGround4M outperform strong baselines in text fidelity, spatial accuracy, and prompt consistency, highlighting the importance of fine-grained layout supervision for grounded T2I generation.

---


### 384. [Measuring Successful Cooperation in Human-AI Teamwork: Development and Validation of the Perceived Cooperativity and Teaming Perception Scales](https://arxiv.org/abs/2604.24461)

**<font color=#1a73e8>作者：</font>** Christiane Attig, Christiane Wiebel-Herboth, Patricia Wollstadt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As human-AI cooperation becomes increasingly prevalent, reliable instruments for assessing the subjective quality of cooperative human-AI interaction are needed. We introduce two theoretically grounded scales: the Perceived Cooperativity Scale (PCS), grounded in joint activity theory, and the Teaming Perception Scale (TPS), grounded in evolutionary cooperation theory. The PCS captures an agent's perceived cooperative capability and practice within a single interaction sequence; the TPS captures the emergent sense of teaming arising from mutual contribution and support. Both scales were adapted for human-human cooperation to enable cross-agent comparisons. Across three studies (N = 409) encompassing a cooperative card game, LLM interaction, and a decision-support system, analyses of dimensionality, reliability, and validity indicated that both scales successfully differentiated between cooperation partners of varying cooperative quality and showed construct validity in line with expectations. The scales provide a basis for empirical investigation and system evaluation across a wide range of human-AI cooperation contexts.

---


### 385. [Advancing Ligand-based Virtual Screening and Molecular Generation with Pretrained Molecular Embedding Distance](https://arxiv.org/abs/2604.24474)

**<font color=#1a73e8>作者：</font>** Shiyun Wa, Yifei Wang, Simone Sciabola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Molecular similarity plays a central role in ligand-based drug discovery, such as virtual screening, analog searching, and goal-directed molecular generation. However, traditional similarity measures, ranging from fingerprint-based Tanimoto coefficients to 3D shape overlays, are often computationally expensive at scale or rely on hand-crafted molecular descriptors. Meanwhile, many deep learning approaches to similarity-aware design still depend on similarity-specific supervision or costly data curation, limiting their generality across targets. In this work, we propose pretrained embedding distance (PED) as an effective alternative, computed directly from pretrained molecular models without task-specific training. Experimental results show that PED exhibits distinct correlations with traditional similarity metrics, and performs effectively in both ranking molecules for virtual screening and guiding molecular generation via reward design. These findings suggest that pretrained molecular embeddings capture rich structural information and can serve as a promising and scalable similarity measurement for modern AI-aided drug discovery.

---


### 386. [Putting a Face to the Issue: Fostering User Empathy of Open Source Software Developers With PersonaFlow](https://arxiv.org/abs/2604.24478)

**<font color=#1a73e8>作者：</font>** Boniface Bahati Tadjuidje, Jin L.C. Guo, Jinghui Cheng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open-source software (OSS) developers often struggle to understand and respond to user context, while existing tools, such as issue trackers (for handling bugs, requests, and feedback), largely focus on technical discussion. Although personas could help, limited resources and UX expertise make them hard to scale. We present PersonaFlow, a tool that generates editable user personas from OSS repository artifacts and integrates them alongside issue reports. In a user study with 13 OSS developers, most reported shifts in how they understood users, and more than half modified their responses by adding empathetic language, tailoring explanations, or raising priority ratings. We found two pathways to this change: some connected emotionally to personas as people, while others used them pragmatically for triaging. Both appeared to lead to more user-centered behavior. We contribute design implications for persona-based tools relevant to OSS and other contexts where efficiency-driven systems or workflows obscure valuable human elements.

---


### 387. [Blur Effects on User Performance in Target-Pointing Tasks](https://arxiv.org/abs/2604.24482)

**<font color=#1a73e8>作者：</font>** Ryuto Tomihari, Taiki Kinoshita, Yosuke Oba 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In projectors and head-mounted displays, an out-of-focus image appears blurred. Even when a display itself is in focus, computer operation may be hindered if the display is far from the user or if a user has poor visual acuity, because the user cannot see the screen clearly. In this study, we conducted an experiment in which participants performed a pointing task under blurred display conditions and investigated the relationship between blur strength and user performance. The results showed that movement time and error rate increased as blur became stronger, and that the effect of blur on movement time was larger when targets were smaller. We further showed that movement time can be estimated with high accuracy by a model that improves on Fitts' law. In a follow-up experiment to examine the applicability of this model, we adjusted target size for each participant and showed that the effect of blur level on movement time could be reduced. These findings suggest potential use in tools that adapt user interfaces to users' visual acuity.

---


### 388. [Deployment-Aligned Low-Precision Neural Architecture Search for Spaceborne Edge AI](https://arxiv.org/abs/2604.24492)

**<font color=#1a73e8>作者：</font>** Parampuneet Kaur Thind, Vaibhav Katturu, Giacomo Zema 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Designing deep networks that meet strict latency and accuracy constraints on edge accelerators increasingly relies on hardware-aware optimization, including neural architecture search (NAS) guided by device-level metrics. Yet most hardware-aware NAS pipelines still optimize architectures under full-precision assumptions and apply low-precision adaptation only after the search, leading to a mismatch between optimization-time behavior and deployment-time execution on low-precision hardware that can substantially degrade accuracy. We address this limitation by integrating deployment-aligned low-precision training directly into hardware-aware NAS. Candidate architectures are exposed to FP16 numerical constraints during fine-tuning and evaluation, enabling joint optimization of architectural efficiency and numerical robustness without modifying the search space or evolutionary strategy. We evaluate the proposed framework on vessel segmentation for spaceborne maritime monitoring, targeting the Intel Movidius Myriad X Visual Processing Unit (VPU). While post-training precision conversion reduces on-device performance from 0.85 to 0.78 mIoU, deployment-aligned low-precision training achieves 0.826 mIoU on-device for the same architecture (95,791 parameters), recovering approximately two-thirds of deployment-induced accuracy gap without increasing model complexity. These results demonstrate that incorporating deployment-consistent numerical constraints into hardware-aware NAS substantially improves robustness and alignment between optimization and deployment for resource-constrained edge Artificial Intelligence (AI).

---


### 389. [CA-IDD: Cross-Attention Guided Identity-Conditional Diffusion for Identity-Consistent Face Swapping](https://arxiv.org/abs/2604.24493)

**<font color=#1a73e8>作者：</font>** Md Shohel Rana, Tanoy Debnath  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face swapping aims to optimize realistic facial image generation by leveraging the identity of a source face onto a target face while preserving pose, expression, and context. However, existing methods, especially GAN-based methods, often struggle to balance identity preservation and visual realism due to limited controllability and mode collapse. In this paper, we introduce CA-IDD (Cross-Attention Guided Identity-Conditional Diffusion), the first diffusion-based face swapping approach that integrates multi-modal guidance comprising gaze, identity, and facial parsing through multi-scale cross-attention. Precomputed identity embeddings are incorporated into the denoising process via hierarchical attention layers, resulting in accurate and consistent identity transfer. To improve semantic coherence and visual quality, we use expert-guided supervision, with facial parsing and gaze-consistency modules. Unlike GAN-based or implicit-fusion methods, our diffusion framework provides stable training, robust generalization, and spatially adaptive identity alignment, allowing for fine-grained regional control across pose and expression variations. CA-IDD achieves an FID of 11.73, exceeding established baselines such as FaceShifter and MegaFS. Qualitative results also reveal improved identity retention across diverse poses, establishing CA-IDD as a strong foundation for future diffusion-based face editing.

---


### 390. [Self-Supervised Representation Learning via Hyperspherical Density Shaping](https://arxiv.org/abs/2604.24498)

**<font color=#1a73e8>作者：</font>** Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern self-supervised representation learning methods often relies on empirical heuristics that are not theoretically grounded. In this study we propose HyDeS, a theoretically grounded method based on multi-view mutual information maximization within an hyperspherical space using Shannon differential entropy with a non-parametric von Mises-Fisher density estimator.
We show that HyDeS bias the trained model towards focusing on foreground features of the images and perform well on segmentation tasks such as VOC PASCAL, while it lags in fine-grained classification. We provide a detailed analysis of the induced latent space geometry and learning dynamics, that can be used for designing other theoretically grounded self-supervised learning methods.

---


### 391. [SceneSelect: Selective Learning for Trajectory Scene Classification and Expert Scheduling](https://arxiv.org/abs/2604.24514)

**<font color=#1a73e8>作者：</font>** Xinrun Wang, Deshun Xia, Ke Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate trajectory prediction is fundamentally challenging due to high scene heterogeneity - the severe variance in motion velocity, spatial density, and interaction patterns across different real-world environments. However, most existing approaches typically train a single unified model, expecting a fixed-capacity architecture to generalize universally across all possible scenarios. This conventional model-centric paradigm is fundamentally flawed when confronting such extreme heterogeneity, inevitably leading to a severe generalization gap, degraded accuracy, and massive computational waste. To overcome this bottleneck, rather than refining restricted model-centric architectures, we propose selective learning, a novel scene-centric paradigm. It explicitly analyzes the characteristics of the underlying scene to dynamically route inputs to the most appropriate expert models. As a concrete implementation of this paradigm, we introduce SceneSelect. Specifically, SceneSelect utilizes unsupervised clustering on interpretable geometric and kinematic features to discover a latent scene taxonomy. A highly decoupled classification module is then trained to assign real-time inputs to these scene categories, and a highly extensible, plug-and-play scheduling policy automatically dispatches the trajectory sequence to the optimal expert predictor. Crucially, this decoupled design ensures excellent generalization capabilities, allowing seamless integration with different off-the-shelf models and robust adaptation across new datasets without requiring computationally expensive joint retraining. Extensive experiments on three public benchmarks (ETH-UCY, SDD, and NBA) demonstrate that our method consistently outperforms strong single-model and ensemble baselines, achieving an average improvement of 10.5%, showcasing the effectiveness of scene-aware selective learning.

---


### 392. [Prior-Agnostic Robust Forecast Aggregation](https://arxiv.org/abs/2604.24517)

**<font color=#1a73e8>作者：</font>** Zhi Chen, Cheng Peng, Wei Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robust forecast aggregation combines the predictions of multiple information sources to perform well in the worst case across all possible information structures. Previous work largely focuses on settings with a known binary state space, where the state is either 0 or 1. We study prior-agnostic robust forecast aggregation in which the aggregator observes only experts' reports, yet is ignorant of both the underlying joint information structure and the full prior, including the underlying state space. Unlike the standard model that fixes the binary state space {0, 1}, we allow the (binary) unknown state values to be arbitrary numbers in [0, 1], so the same reported probability may correspond to very different realized outcome frequencies across environments.
Our main contribution is a simple, explicit, closed-form log-odds aggregator that linearly pools forecasts in logit space, together with (nearly-)tight minimax-regret guarantees across three knowledge regimes. We first show that under conditionally independent (CI) signals, robust aggregation with an unknown state space is strictly harder than in the known-state setting by establishing a larger lower bound, and our aggregation rule can achieve a worst-case regret of 0.0255. Along the way, we also characterize tight regret bounds for Blackwell-ordered structures and for general information structures. In the classical setting with known state space {0,1}, our aggregator achieves regret strictly below 0.0226 for CI structures. To the best of our knowledge, this is the first explicit closed-form aggregator that achieves a regret upper bound strictly less than 0.0226. Finally, we extend the model where the aggregator additionally knows each expert's marginal forecast distribution; in this setting, with the CI structures, we show that a generalized log-odds rule achieves regret of 0.0228, complementing with a lower bound of 0.0225.

---


### 393. [Point Cloud Registration for Fusion between SPECT MPI and CTA Images](https://arxiv.org/abs/2604.24524)

**<font color=#1a73e8>作者：</font>** Ni Yao, Xiangyu Liu, Shaojie Tang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical fusion of Single Photon Emission Computed Tomography Myocardial Perfusion Imaging (SPECT MPI) and Computed Tomography Angiography (CTA) remains limited by cross-modality misregistration and reliance on manual landmarks, which can hinder accurate ischemia localization and lesion-level functional assessment. To address this issue, we propose a registration and fusion framework for SPECT MPI and CTA that integrates functional and structural information for comprehensive cardiac evaluation. The proposed pipeline performs U-Net-based segmentation on both modalities. On SPECT MPI, only the left ventricle (LV) is extracted, and anatomical landmarks are automatically derived from characteristic LV structures. On CTA, both ventricles are segmented, and their spatial relationship is used to automatically define landmarks at the interventricular septal junction. Scale-space consistency preprocessing and landmark-driven coarse registration are applied to mitigate initial misalignment. Based on this initialization, multiple fine registration methods are evaluated on LV epicardial surface point clouds, including ICP, SICP, CPD, CluReg, FFD, and BCPD-plus-plus. The resulting transformations are then propagated to voxel-level resampling for high-precision SPECT-CTA fusion. In a retrospective cohort of 60 patients, the proposed framework preserved sub-millimeter coronary detail from CTA while accurately overlaying quantitative SPECT perfusion. Among the evaluated methods, BCPD-plus-plus achieved the highest accuracy with a mean point cloud distance of 1.7 mm. By combining robust initialization, comparative fine registration, and voxel-level fusion, the proposed approach provides a practical solution for myocardial ischemia localization and functional evaluation of coronary lesions, while remaining independent of any specific fine registration algorithm.

---


### 394. [Interoceptive machine framework: Toward interoception-inspired regulatory architectures in artificial intelligence](https://arxiv.org/abs/2604.24527)

**<font color=#1a73e8>作者：</font>** Diego Candia-Rivera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This review proposes an integrative framework grounded on interoception and embodied AI-termed the interoceptive machine framework-that translates biologically inspired principles of internal-state regulation into computational architectures for adaptive autonomy. Interoception, conceived as the monitoring, integration, and regulation of internal signals, has proven relevant for understanding adaptive behavior in biological systems. The proposed framework organizes interoceptive contributions into three functional principles: homeostatic, allostatic, and enactive, each associated with distinct computational roles: internal viability regulation, anticipatory uncertainty-based re-evaluation, and active data generation through interaction. These principles are not intended as direct neurophysiological mappings, but as abstractions that inform the design of artificial agents with improved self-regulation and context-sensitive behavior. By embedding internal state variables and regulatory loops within these principles, AI systems can achieve more robust decision-making, calibrated uncertainty handling, and adaptive interaction strategies, particularly in uncertain and dynamic environments. This approach provides a concrete and testable pathway toward agents capable of functionally grounded self-regulation, with direct implications for human-computer interaction and assistive technologies. Ultimately, the interoceptive machine framework offers a unifying perspective on how internal-state regulation can enhance autonomy, adaptivity, and robustness in embodied AI systems

---


### 395. [A Reward-Free Viewpoint on Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2604.24532)

**<font color=#1a73e8>作者：</font>** Ying-Tu Chen, Wei Hung, Bing-Shu Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many sequential decision-making tasks involve optimizing multiple conflicting objectives, requiring policies that adapt to different user preferences. In multi-objective reinforcement learning (MORL), one widely studied approach} addresses this by training a single policy network conditioned on preference-weighted rewards. In this paper, we explore a novel algorithmic perspective: leveraging reward-free reinforcement learning (RFRL) for MORL. While RFRL has historically been studied independently of MORL, it learns optimal policies for any possible reward function, making it a natural fit for MORL's challenge of handling unknown user preferences. We propose using the RFRL's training objective as an auxiliary task to enhance MORL, enabling more effective knowledge sharing beyond the multi-objective reward function given at training time. To this end, we adapt a state-of-the-art RFRL algorithm to the MORL setting and introduce a preference-guided exploration strategy that focuses learning on relevant parts of the environment. Through extensive experiments and ablation studies, we demonstrate that our approach significantly outperforms the state-of-the-art MORL methods across diverse MO-Gymnasium tasks, achieving superior performance and data efficiency. This work provides the first systematic adaptation of RFRL to MORL, demonstrating its potential as a scalable and empirically effective solution to multi-objective policy learning.

---


### 396. [Stochastic simultaneous optimistic optimization](https://arxiv.org/abs/2604.24537)

**<font color=#1a73e8>作者：</font>** Michal Valko, Alexandra Carpentier, Rémi Munos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of global maximization of a function f given a finite number of evaluations perturbed by noise. We consider a very weak assumption on the function, namely that it is locally smooth (in some precise sense) with respect to some semi-metric, around one of its global maxima. Compared to previous works on bandits in general spaces (Kleinberg et al., 2008; Bubeck et al., 2011a) our algorithm does not require the knowledge of this semi-metric. Our algorithm, StoSOO, follows an optimistic strategy to iteratively construct upper confidence bounds over the hierarchical partitions of the function domain to decide which point to sample next. A finite-time analysis of StoSOO shows that it performs almost as well as the best specifically-tuned algorithms even though the local smoothness of the function is not known.

---


### 397. [RACANet: Reliability-Aware Crowd Anchor Network for RGB-T Crowd Counting](https://arxiv.org/abs/2604.24543)

**<font color=#1a73e8>作者：</font>** Jinghao Shi, Mengqi Lei, Kunliang He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-Thermal (T) crowd counting aims to integrate visible-spectrum and thermal infrared information to improve the robustness of crowd density estimation in complex scenes. Although existing studies generally improve counting accuracy through cross-modal feature fusion, most current methods rely on implicit cross-modal fusion strategies and lack explicit modeling of local spatial discrepancies as well as fine-grained characterization of modality reliability at the positional level, thereby limiting the accuracy and interpretability of the fusion process. To address these issues, this paper proposes a two-stage fusion framework, RACANet, a Reliability-Aware Crowd Anchor Network for RGB-T crowd counting. First, we introduce a lightweight cross-modal alignment pretraining stage, which explicitly learns cross-modal semantic correspondences through crowd-prior supervision and local bidirectional soft matching. Then, based on the priors learned during pretraining, a Local Anchor Fusion Module (LAFM) is introduced in the formal training stage. This module generates local semantic anchors by aggregating features from highly reliable regions and further enables adaptive pixel-level feature redistribution with a local attention mechanism. In addition, we propose a discrepancy-aware consistency constraint to dynamically coordinate the reliability of regions where modal representations are consistent. Experiments conducted on two widely used benchmark datasets, RGBT-CC and Drone-RGBT, demonstrate that RACANet outperforms existing methods. The anonymous code is available at this https URL.

---


### 398. [Dialysis Risk Prediction and Treatment Effect Estimation for AKI patients using Longitudinal Electronic Health Records](https://arxiv.org/abs/2604.24547)

**<font color=#1a73e8>作者：</font>** Kalyani P. Pande, Evan Yang, Bryan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Progression to dialysis or end-stage renal disease is a rare but clinically important outcome. Clinicians need evidence on how medication exposures influence downstream risk. We constructed a fixed-window EHR cohort (90-day observation, 730-day prediction; N=81401; dialysis/ESRD prevalence: 1.1%) and modeled sequences of diagnoses, procedures, and medications with kidney laboratory trends (creatinine, BUN, eGFR). A transformer-based causal multi-head model was trained to estimate drug- and ingredient-level average treatment effects (ATEs) using counterfactual exposure removal and insertion under a full medication history setup. On test set, predictive performance reached an AUC of 0.694 and PR-AUC of 0.094. At the selected decision threshold (0.883), the model achieved an F1 score of 0.201 with a Brier score of 0.018. Post-hoc causal analyses of lab changes (eGFR, creatinine, BUN) using IPTW, AIPW, naive, and covariate-adjusted OLS methods assessed clinical directionality. Results showed partial protective-direction support for ACE/ARB exposures and worsening-direction signals for loop diuretics.

---


### 399. [GradMAP: Gradient-Based Multi-Agent Proximal Learning for Grid-Edge Flexibility](https://arxiv.org/abs/2604.24549)

**<font color=#1a73e8>作者：</font>** Yihong Zhou, Hongtai Zeng, Thomas Morstyn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coordinating large populations of grid-edge devices requires learning methods that remain fully decentralised in deployment while still respecting three-phase AC distribution-network physics. This paper proposes gradient-based multi-agent proximal learning (GradMAP) to address this challenge. GradMAP trains independent neural-network policies for each agent without any parameter sharing, and each agent uses only its own local observation for online decision-making without communication. During offline training, GradMAP embeds a differentiable three-phase AC power-flow model in a primal-dual learning loop and uses implicit differentiation to propagate exact network-constraint violations to update the policy parameters. To speed up training, GradMAP reuses expensive environment gradients through a proximal surrogate within a trust region defined in the more direct policy-output (action) space, instead of the probability distribution space used in other works, such as PPO. In case studies with 1,000 agents managing batteries, heat pumps, and controllable generators on the IEEE 123-bus feeder, GradMAP learns decentralised policies that minimise three-phase AC load-flow constraint violations within 15 minutes of training on a single workstation-class NVIDIA RTX PRO 5000 Blackwell 48GB GPU. This is a 3--5x training speed-up over gradient-based self-supervised learning benchmarks and substantially better training efficiency than multi-agent reinforcement-learning benchmarks. In out-of-sample tests, GradMAP also delivers among the lowest operating cost and constraint violations.

---


### 400. [Efficient learning by implicit exploration in bandit problems with side observations](https://arxiv.org/abs/2604.24555)

**<font color=#1a73e8>作者：</font>** Tomas Kocak, Gergely Neu, Michal Valko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider online learning problems under a partial observability model capturing situations where the information conveyed to the learner is between full information and bandit feedback. In the simplest variant, we assume that in addition to its own loss, the learner also gets to observe losses of some other actions. The revealed losses depend on the learner's action and a directed observation system chosen by the environment. For this setting, we propose the first algorithm that enjoys near-optimal regret guarantees without having to know the observation system before selecting its actions. Along similar lines, we also define a new partial information setting that models online combinatorial optimization problems where the feedback received by the learner is between semi-bandit and full feedback. As the predictions of our first algorithm cannot be always computed efficiently in this setting, we propose another algorithm with similar properties and with the benefit of always being computationally efficient, at the price of a slightly more complicated tuning mechanism. Both algorithms rely on a novel exploration strategy called implicit exploration, which is shown to be more efficient both computationally and information-theoretically than previously studied exploration strategies for the problem.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-437](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
