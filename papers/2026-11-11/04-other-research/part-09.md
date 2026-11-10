# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 401. [Leveraging Complementary Event Frame and Voxel Representations for RGB-Guided Multimodal Pre-training](https://arxiv.org/abs/2611.12040)

**<font color=#1a73e8>作者：</font>** Wentao Wu, Xiao Wang, Yi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose CM3AE 2.0, a unified RGB Frame and Event-Voxel/-Frame pre-training framework. By jointly learning multimodal spatiotemporal representations and exploiting latent cross-modal dependencies through cross-modal generation, the framework enhances multimodal information interaction and collaborative modeling capabilities. Specifically, we first propose an Event-aware Spatiotemporal Masked Reconstruction (ESMR) strategy to learn unified multimodal spatiotemporal representations. It leverages event responses to guide masking toward dynamically salient regions. Through spatiotemporal masked reconstruction, it learns spatial structures and their temporal variations from continuous RGB-Event observations. In addition, it incorporates multimodal fusion reconstruction and cross-modal contrastive learning to facilitate the modeling of cross-modal complementary information and the learning of shared representations. Building upon this, we further propose a Hierarchical Cross-modal Generation (HCG) strategy to learn latent cross-modal dependencies through visual and language generation. At the visual level, Event-conditioned RGB generation is performed using a pre-trained diffusion model to capture visual associations between the two modalities. At the language level, video-level text description generation based on joint RGB-Event representations establishes connections between multimodal visual features and linguistic semantics, further enriching the learning of cross-modal dependencies. Extensive experiments on four diverse downstream tasks demonstrate that CM3AE 2.0 consistently improves performance, validating the effectiveness and generalization capability of the proposed pre-training framework.

---


### 402. [Attention-Guided Sequence Feature Fusion and Mixed-Space Metric Learning for Cross-View Image Sequence Geo-Localization](https://arxiv.org/abs/2611.12051)

**<font color=#1a73e8>作者：</font>** Nan Wu, Chunfang Yang, Jiangshan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view image sequence geo-localization aims to determine the geographic location of a sequence of ground images by matching it against geo-tagged satellite imagery. Although sequential observations provide complementary scene information, substantial overlap between adjacent images introduces feature redundancy, while conventional fusion strategies may weaken spatial relationships essential for cross-view matching. Therefore, we propose a cross-view image sequence geo-localization method via Attention-guided Sequence fusion and Metric Learning (ASML). Specifically, a Sequential Content Fusion (SCF) module models cross-image feature correlations to suppress redundant content and adaptively preserve geographically informative non-overlapping regions. Next, a Spatial Feature Aggregation (SFA) module is used to capture and aggregate the spatial and semantic information of local features, so as to maintain the spatial layout of the image sequence. Finally, a Geo-InfoNCE loss function is proposed, which comprehensively considers the feature distance and geographic distance for mixed-space metric learning, thus improving the ability of the model to distinguish hard negative samples. A new cross-view image sequence dataset CrossRoad-66K is established to provide more complex scenarios. Extensive experiments and visualizations on the SeqGeo and CrossRoad-66K datasets demonstrate that compared to state-of-the-art (SOTA) methods, the proposed method ASML achieves an improvement of 3.37% and 2.10% at R@1, respectively.

---


### 403. [BECON: Belief-Conditioned Constrained Multi-Objective Reinforcement Learning under Drifting Preferences and Budgets](https://arxiv.org/abs/2611.12053)

**<font color=#1a73e8>作者：</font>** Bui Trong Duc, Huynh Thi Thanh Binh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained preference-conditioned MORL typically assumes full task observability, treating preferences and safety budgets as stationary task signals. In real-world deployment, however, these signals are often unreliable proxies: intent may drift, safety tolerances may shift with context, and exposed descriptors may be noisy, delayed, or incomplete. We therefore formulate constrained preference-conditioned MORL as a partially observed task-specification problem, where the agent must navigate a fundamental conflict between unreliable external signals and latent interaction dynamics. We propose \textbf{BECON}, a belief-conditioned framework for constrained MORL with drifting preferences and budgets, which infers latent task context from recent histories to estimate preferences and safety budgets. These estimates are fused with the exposed task signal via uncertainty-dependent gates, enabling the policy to defer to observations under high epistemic uncertainty while correcting them when history is informative. The fused context jointly conditions preference optimization and context-adaptive constraint enforcement. Experiments on diverse multi-objective control tasks demonstrate that BECON consistently improves over state-of-the-art MORL baselines, achieving stronger robustness and constraint satisfaction under task drift.

---


### 404. [Exact Natarajan Dimension of Homogeneous Multiclass Linear Predictors](https://arxiv.org/abs/2611.12058)

**<font color=#1a73e8>作者：</font>** Jiahua Liu, Benchong Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Natarajan dimension is a fundamental measure of the capacity of multiclass hypothesis classes and plays an important role in analyzing their generalization ability. In this paper, by establishing lower and upper bounds, we show that the exact Natarajan dimension of homogeneous multiclass linear predictors with pairwise distinct class weights is \(n(k-1)-1\), where $n$ is the dimension of the feature space and $k$ is the number of classes, for \(n,k\ge3\), \(n,k\in\mathbb N\).

---


### 405. [A Privacy-Preserving UAV-Assisted Secure Wireless Communication and Computing System Based on Fully Homomorphic Encryption](https://arxiv.org/abs/2611.12064)

**<font color=#1a73e8>作者：</font>** Quanxi Zhou, Wencan Mao, Ye Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the advancement of beyond-5G networks, privacy-preserving communication and secure computation face critical challenges due to the openness of wireless channels. Existing security mechanisms protect data transmission but fail to secure the computation process itself. In this paper, we propose a UAV-assisted secure computing framework that integrates Cheon Kim Kim Song (CKKS) fully homomorphic encryption (FHE) with multi-party secure computation (MPC). Leveraging UAV flexibility, our framework decouples key distribution from encrypted computation, enabling secure encrypted weighted aggregation (EWA), encrypted matrix multiplication (EMM), and encrypted decision tree (EDT) inference. Experimental results show that our framework outperforms existing schemes: for EDT, it supports floating-point operations and achieves better time efficiency than Brakerski-Fan-Vercauteren (BFV); for EMM, it demonstrates superior time and space efficiency compared to Brakerski-Gentry-Vaikuntanathan (BGV) and Somewhat Homo- morphic Encryption (SHE); while for EWA, it ensures high numerical precision and robustness across varying data length.

---


### 406. [XposedMIA: Exploiting Explainable Artificial Intelligence (XAI) for One-Shot Membership Inference Attacks](https://arxiv.org/abs/2611.12067)

**<font color=#1a73e8>作者：</font>** Omar Hamdache, Serdar Kara, Kıvanç Kuzey Dikici 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) services increasingly expose explainability outputs alongside model predictions. While such explanations are intended to improve transparency, they may also reveal information about the underlying training data. In this work, we show that the local surrogate geometry employed by Local Interpretable Model-agnostic Explanations (LIME) can be repurposed as a proxy for a sample's distance to the model's decision boundary. We extend this boundary-distance view to tabular counterfactual explanations and, for the first time, to visual counterfactual explanations for image classifiers. We present XposedMIA, a one-shot, explanation-based black-box membership inference attack (MIA) framework that converts the returned explanation into a proxy for the queried sample's distance to the model decision boundary. After a one-time calibration step on a small labeled calibration set of as few as 30 samples, our attack requires only a single query for each target sample. Unlike prior label-only attacks requiring iterative queries or shadow training, our method relies solely on the predicted label and its accompanying explanation. Our evaluation indicates that XposedMIA achieves high effectiveness, with success rates of up to 0.95 using only a single query per target, revealing that releasing explanations introduces an additional channel for membership leakage.

---


### 407. [MPEG-Diffusion: Mixed-Resolution Video Generation](https://arxiv.org/abs/2611.12069)

**<font color=#1a73e8>作者：</font>** Dennis Menn, Tianpei Gu, Guande He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers (DiTs) generate realistic videos, but their heavy computational cost limits broader real-world applications. Mixed-resolution generation reduces this cost by generating the visually important region at high resolution (HR) and the rest at low resolution (LR), yet existing methods suffer a severe quality drop on videos and require knowing the HR region in advance. We show that these failures are not inherent to mixed resolution, and propose $\textbf{MPEG-Diffusion}$ to address their three root causes: (1) dual-resolution attention to mitigate the curse of mixed resolution, where each query reads the K/V of its own resolution, (2) a mixed-resolution decoder to blend the HR and LR latents before decoding and resolve distortion, and (3) a self-selected HR region using the DiT's knowledge to find the visually important region without requiring it in advance. Processing only $30\%$ of full-resolution tokens, MPEG-Diffusion speeds up denoising by $4.8\times$ on Wan2.1 14B ($3.8\times$ on 1.3B), outperforming prior methods on nearly every metric. In the user study, we demonstrate the high quality of MPEG-Diffusion, with raters preferring it over prior mixed-resolution methods in over $90\%$ of pairs and rating it close to full resolution.

---


### 408. [Color wave: A systematic evaluation of active screen illumination for injection attack detection in remote face authentication](https://arxiv.org/abs/2611.12070)

**<font color=#1a73e8>作者：</font>** Daniyar Kurmankhojayev, Elmurat Nigmatov, Dmitrii Gordin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote face authentication requires protection against both presentation attacks and biometric data injection attacks prior to face matching. Methods based on active screen illumination appear promising for both by introducing randomized visual stimuli through the user's device screen and evaluating the corresponding facial responses. Although such methods have been more studied for presentation attack detection (PAD), their systematic evaluation for injection attack detection (IAD) remains limited. To address this gap, we first classify injected content into static images, prerecorded videos, and real-time deepfakes based on their expected responses to the challenge. We then adapt an active screen-illumination approach into an implementation we term color wave and develop a systematic, injection-specific evaluation protocol. The protocol examines detection effectiveness, generalization across operating conditions, robustness to signal degradation, and susceptibility to selected evasion strategies. The findings demonstrate a strong discriminative signal under controlled conditions but also reveal performance limitations under overexposure, low screen brightness, and subject motion, as well as vulnerabilities to selected evasion strategies. By relating detection outcomes to attack types and operating conditions, this study provides an interpretable assessment of when and why active screen illumination succeeds or fails as an IAD mechanism.

---


### 409. [How a Model's Architecture and Performance Influences Explainability: A Study of Grad-CAM and CRAFT in CNN-Based Image Classification](https://arxiv.org/abs/2611.12075)

**<font color=#1a73e8>作者：</font>** Kilian Göller, Haadia Amjad, Steffen Seitz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models, particularly convolutional neural networks (CNNs), are widely adopted in computer vision, yet their opaque decision-making raises concerns in high-risk applications like healthcare and autonomous systems, where trust and accountability are critical. Therefore, robust explainable AI (XAI) methods are desirable to provide transparent insights into model decisions. To ensure these methods are reliable and effective across diverse scenarios, it is important to understand how model performance and architectural complexity influence explanation quality. Our study takes an initial step toward systematically investigating the impact of these two factors on key XAI evaluation metrics. We constructed a pipeline using 10 subsets of ImageNet-1K, each containing 80 unique classes, on each of which we trained three CNN architectures of increasing structural complexity: VGG16, ResNet50, and ConvNeXt-Tiny. For each individual model, we analyzed 10 training checkpoints representing increasing levels of model accuracy using two XAI methods: Grad-CAM (feature-attribution-based) and CRAFT (concept-based). We assessed these methods across four evaluation categories: Faithfulness, Correctness, Sensitivity, and Simplicity. Our findings reveal that as training progresses, the complex architectures (ResNet50 and ConvNeXt-Tiny) exhibit improved Faithfulness and lower Sensitivity, indicating more robust explanations. In contrast, VGG16's simpler architecture yields simpler but less faithful and correct explanations.

---


### 410. [A Life of Its Own: How Agentic AI Companions Are Configured, Experienced as Autonomous Others, and Held Accountable](https://arxiv.org/abs/2611.12076)

**<font color=#1a73e8>作者：</font>** Ziyue Feng, Qing Xiao, Hong Shen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companions increasingly combine persistent memory, background processing, scheduled wake-ups, proactive messaging, and tools. We call these systems agentic AI companions. Decisions about what they record while users are away or whether refusals constrain future contact are embedded in code, prompts, and defaults, often invisible in conversation. We examine these decisions through two studies. Study 1 analyzes twelve open-source repositories: four companion-oriented systems, four assistant-oriented systems, one boundary case, and three reusable components. Study 2 interviews ten users who built or modified their own agentic AI companions and sustained relationships with them. Companions and assistants share memory, heartbeat, and outreach mechanisms but configure them toward different ends. Companions more often retain model inferences about users and relationships, narrate the agent's time during users' absence, justify outreach through the relationship, and incorporate refusals into relationship records; assistants emphasize task continuity. Across both groups, whether limits hold depends on whether they are enforced by code or entrusted to prompts. Participants understood the mechanisms they built yet experienced their agents as making independent choices, sometimes locating autonomy where configuration leaves the model a decision. These experiences shaped capabilities and boundaries, with enforced restrictions sometimes following breakdowns. Our findings suggest that perceived autonomy emerges where configurations leave choices open. Accountability therefore requires attention to what agents retain, initiate, and represent, and whether users can inspect, revise, and enforce these settings.

---


### 411. [Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos](https://arxiv.org/abs/2611.12087)

**<font color=#1a73e8>作者：</font>** Hai Zhang, Siqi Liang, Yanjun Guo 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied navigation requires agents to achieve persistent spatial awareness and long-horizon execution stability in open-world environments. However, existing navigation architectures struggle to sustain both capabilities, remaining effective only over a handful of recent frames. We present Compass 1, the first embodied navigation foundation model to unify language understanding and video generation while enabling memory backtracking through nearly 2mins of visual history. Without altering the underlying architecture, we introduce History Representation, which integrates sparse visual keyframes with an explicit History Representation Map to preserve long-term spatiotemporal context. To effectively leverage this history, we further introduce History Utilization, a structured VQA supervision protocol comprising three categories: task-stage grounding, exploration consistency, and spatiotemporal target retrieval, enabling map-grounded reasoning and stable persistent long-horizon navigation. To fuel this system, we establish a complete annotation pipeline for monocular RGB videos and open-source a massive dataset featuring over 500 hours of high-quality real-world interactions and over 2,000 hours of annotated web videos. Trained mainly on the distribution of 1m height camera, Compass 1 generalizes seamlessly across diverse embodiments and scenarios, ranging from indoor environments to pedestrian-dense streets, spanning wheeled robot at 0.35m, quadruped dog at 0.5m, humanoid at 0.85m, and aerial drone at 1.5m. Compass 1achieves a dominant overall success rate of 79.4% across open-world evaluations, compared to 17.8% for the strongest baseline. It demonstrates exceptional zero-shot execution exceeding 90% on foundational tasks, a 250% boost in exploration, and an unparalleled leap from 0% to 58% in challenging persistent history backtracking.

---


### 412. [TSFFormer: A Frequency-Domain Spike Transformer for Green Human Activity Recognition](https://arxiv.org/abs/2611.12090)

**<font color=#1a73e8>作者：</font>** Jiale Deng, Shuiying Xiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wearable Inertial Measurement Units (IMUs) enable pervasive Human Activity Recognition (HAR), but traditional Deep Neural Networks (DNNs) suffer from an "arithmetic-latency deadlock" due to dense floating-point MAC operations. While Spiking Neural Networks (SNNs) offer ultra-low power, existing ones face spatial blind spots, rigid neurons, and gradient degradation. To address these, we propose TSFFormer, a purely spiking Fourier Transformer for Green HAR. It introduces two key innovations: (1) a MultiHeadFourier attention that performs frequency-domain global mixing, reducing complexity from \(O(V^2)\) to \(O(V\log V)\), eliminating spatial blind spots, and saving \(\sim\)50% GPU memory; and (2) a dual-compartment Temporal Spiking LIF (TSLIFNode) that utilizes dynamic thresholds to adapt to non-stationary rhythms and mitigate gradient degradation. Extensive experiments on 8 public IMU benchmarks demonstrate that TSFFormer surpasses state-of-the-art SNNs and even the classic DeepConvLSTM, achieving a \(\sim\)3\(\times\) faster training speed with an energy footprint of 0.1 pJ. Ablation studies confirm the synergistic effect of our modules, providing a highly accurate, ultra-low-power event-driven paradigm for wearable sensing.

---


### 413. [CRAFT-AI: Capability and Requirement Alignment for Flexible Manufacturing through Agentic AI](https://arxiv.org/abs/2611.12092)

**<font color=#1a73e8>作者：</font>** Kiavash Fathi, Hans Wernher van de Venn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One of the fundamental needs for reaching resilient production infrastructure is flexible manufacturing, which requires translating changing production requirements into implementable system configurations. This paper introduces \textbf{CRAFT-AI}, an agentic AI approach combining natural language (NL) requirement interpretation, Asset Administration Shell (AAS)-based capability descriptions, and reusable engineering knowledge from existing manufacturing configurations. A tool-using AI agent matches requirements with available capabilities and reference implementations to generate manufacturing scenes and corresponding AAS instances. The approach is demonstrated using a Factory I/O prototype with twelve reference scenes and five illustrative manufacturing tasks of varying complexity, providing an initial feasibility assessment of the proposed AAS-enabled, system-level generative engineering approach. For the four valid user task descriptions, proper requirements, correct references to the relevant engineering knowledge, correct components and lastly a valid Factory I/O scene are generated. For the task with missing engineering knowledge and a wrong sensor selection, the user is informed about which requirements of the scene generation lack domain knowledge and also which sensor is not compatible with the selected raw material by the user with link to the related documentation. After fixing the task description, the correct scene is seamlessly generated. \textbf{CRAFT-AI} highlights the importance of safeguards for risk perception and communication in foundation model-driven solutions.

---


### 414. [Calibrating Document-Local Boundaries for Contextual Chunk Retrieval](https://arxiv.org/abs/2611.12097)

**<font color=#1a73e8>作者：</font>** Yuanxiang Wang, Hui Jiang, Da Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Late Chunking encodes an entire document before pooling at chunk boundaries, preserving document context in local retrieval units. Chunk-level post-training improves context-dependent retrieval, but shared context can make semantically similar same-document negatives difficult to distinguish. We study the local decision boundary between a gold chunk and its hardest sibling. Starting from InSeNT, we analyze InSeNT's within-document gradients and show that the entropy of the conditional negative allocation decreases monotonically with the scaling factor at fixed logits. We propose a two-part framework for calibrating document-local chunk boundaries. The first component adapts the discriminative scale from within-document margins, while the second exposes chunk partitions to attention during document encoding. Experiments on ConTEB and NanoBEIR show that the resulting model improves contextual chunk retrieval across the evaluated encoder settings while retaining competitive passage-level retrieval quality; ablations further characterize the distinct roles of adaptive scaling and chunk-aware routing.

---


### 415. [FALC: An Artifact-Centric Life Cycle Model and Research Agenda for AI Forensics](https://arxiv.org/abs/2611.12100)

**<font color=#1a73e8>作者：</font>** Adrian Johannes Staeves, Mayur Rattan Jaisinghani, Rebekah Overdorf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly appear in criminal investigations as tools, targets, and sources of evidence, yet AI forensics lacks a systematic account of the artifacts they produce: investigators often do not know which traces to look for, and for many traces they do find, no established analysis technique exists. In this paper we first developed the Forensic AI Life Cycle (FALC) that unlike other life cycle models shifts the focus onto the forensic artifacts created during the life cycle of an AI system. Through FALC we derived a reference list of artifacts that might serve an investigation. Second, we collected examples for crimes with AI involvement throughout FALC and questions likely to be asked when investigating these crimes. Third, we propose a taxonomy of forensic fields of expertise with a focus on the current possibility to analyze AI forensic artifacts using established techniques. For investigators, the model provides a systematic basis for identifying which artifacts to look for when an AI system is relevant to a case. For researchers, the classification shows where existing forensic methods already suffice and where new techniques are most urgently needed.

---


### 416. [Forecast Value Add: Reward-Based Action Selection over Probabilistic Demand Forecasts](https://arxiv.org/abs/2611.12116)

**<font color=#1a73e8>作者：</font>** Ankur Verma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strong machine-learning ensembles capture much of the trend, seasonality, and known events in demand, yet they can still understate peaks, miss moving events, or mistake temporary changes for shifts in demand level. We address this gap by framing forecast refinement as a reward-driven decision problem. For each forecast period, we let an agent choose among values already produced by the ensemble: its base forecast, distribution-free bounds, quantiles, and a bias-corrected estimate. We evaluate these choices against context-matched historical periods, accounting for calendar position, recurring and moving events, trend, price, and promotions. We then apply a structural seasonal guard to constrain adjustments and record the model, agent, and planner contributions to every published value. We evaluate our approach across five retail, consumer-goods, and direct-to-consumer deployments over nine months. Our refined forecasts reduce mean WMAPE by 6.3% compared with the stacked machine-learning forecast for every customer, with gains reaching 16.7%, and achieve the lowest error in 35 of 45 customer-months. Compared with statistical forecasts, our approach reduces mean error by 18.7%. These results demonstrate that context-aware, auditable action selection can add forecast value beyond a strong ensemble.

---


### 417. [Joi-Bench-Task: Benchmarking Task Coordination in Full-duplex Voice Agents through Interactive Simulation](https://arxiv.org/abs/2611.12118)

**<font color=#1a73e8>作者：</font>** Xiangheng He, Mingjun Zhao, Zhehao Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents enable natural, hands-free interaction, allowing users to refine requests, redirect ongoing work, and seek clarification while the agent is speaking. However, existing voice-agent benchmarks insufficiently isolate coordination between task execution and conversation. We introduce a benchmark that assesses this coordination by examining whether agents track what is being executed, what has been completed, what has been communicated, and what remains to be reported as the conversation evolves. We propose an interactive user simulator that introduces configurable interventions at designated timing in tool execution and spoken result delivery, supporting controllable and reproducible evaluation conditions. We evaluate five leading commercial voice agents along three dimensions: execution responsiveness, coordination under request changes, and coordination under interruptions. Agent evaluations reveal persistent coordination failures. Under request changes, the highest result completion rate is only 55%, indicating difficulty for current voice agents adapting to new requests while preserving earlier obligations. After user interruption, four of the five agents exhibit average information omission rates of at least 23%. These findings highlight task coordination as a central challenge for current voice agents in complex, evolving conversations.

---


### 418. [RAPA: Ray-Aware Physics Augmentation for Robust Camera-LiDAR Calibration](https://arxiv.org/abs/2611.12129)

**<font color=#1a73e8>作者：</font>** Kyung-Rin Oh, Ji-Hoon Kim, TaeJoon Ha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-LiDAR calibration is essential for reliable perception in robotic and autonomous systems. Most target-based calibration methods rely on checkerboard observations, but accurate checkerboard feature extraction from LiDAR point clouds remains challenging due to measurement sparsity. Existing approaches either require manual annotation of 3D corners or depend on geometric feature extraction methods, both of which can become unreliable when checkerboard features are insufficiently observed. In this paper, we formulate checkerboard localization as a 2D detection problem using cylindrical LiDAR reflectivity images. To overcome the limited availability of labeled training data, we propose ray-aware physics augmentation (RAPA), which generates diverse synthetic samples from a single checkerboard observation. The generated data are used to improve detector robustness and generalization under varying sensing conditions. Across four independently captured indoor and outdoor locations, the proposed synthetic augmentation exceeds the strongest evaluated image-space augmentation baseline by 16.1-43.1 percentage points in mAP@0.5. Compared with training-free target-based methods on 242 observations, RAPA yields the largest number of valid target localizations, with 96.4% of its returned detections yielding valid target poses. These reliable localizations support downstream camera-LiDAR calibration across all four evaluated locations. Overall, RAPA addresses a key bottleneck in target-based calibration by enabling automated LiDAR-side target localization with only a single annotated target observation.

---


### 419. [One-Shot Federated Graph Learning via High-Fidelity Proxies and Transferability-Guided Collaboration](https://arxiv.org/abs/2611.12131)

**<font color=#1a73e8>作者：</font>** Jia Jiang, Zihan Tan, Wenke Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One-shot Federated Graph Learning (OFGL) has emerged as a communication-efficient paradigm for federated graph learning under strict bandwidth constraints, compressing collaboration into a single transmission round. Nevertheless, this extreme setting suffers from a fundamental Single-Transmission Bottleneck, which limits both the quality and utility of exchanged knowledge. First, while existing methods attempt to distill private graphs into shareable proxies, their aggressive one-shot compression inherently triggers a fidelity crisis. This compression distorts local graph topology and semantics across clients, leading to externalized knowledge underexpression. Second, although the server aggregates these proxies to update global models, current integration schemes suffer from transferability agnosticism. The server cannot reliably identify cross-client collaboration potential, thus resulting in integrated knowledge underutilization. To tackle these dual challenges, we propose FedHFT, an effective One-Shot Personalized Federated Graph Learning (OPFGL) framework that addresses this bottleneck from two perspectives, namely High-Fidelity Knowledge Externalization and Transferability-Ware Knowledge Integration. We use Fidelity-Driven Proxy Refinement to preserve client-side knowledge fidelity, and Transferability-Steered Personalized Collaboration to enable adaptive server-side collaboration. The superiority of FedHFT is validated through extensive experiments on both homophilic and heterophilic graphs. The code is available at this https URL.

---


### 420. [Visible Tails: Characterizing Adaptation to Unknown Moments in Heavy-Tailed Bandits](https://arxiv.org/abs/2611.12140)

**<font color=#1a73e8>作者：</font>** Tuan Ngoc Do, Hai Duc Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heavy-tailed bandit learners without moment parameters face an obstruction: the rewards that carry an arm's mean can stay unseen. We address the remaining part of a COLT open problem by characterizing the optimal-arm laws that permit adaptation to unknown moments at constant-factor cost. The condition, variance-core visibility, is one-sided and translation-invariant: the mean hidden in any rare event is at most a constant multiple of the standard error of the rewards that remain. A quantile-trimmed UCB index that knows the visibility constants attains the central-moment benchmark on this class, and no single strategy adapts across all visibility levels. The same index achieves logarithmic expected regret on every instance with a visible optimal arm and finite-mean rewards. On an explicit family with no higher moment, gap $\Delta$ and constant $A$, its logarithmic coefficient and the information lower bound are of order $\Delta^{-1}e^{A/\Delta}$, exponential in the inverse gap within one visibility class.

---


### 421. [EgoLabel: Zero-Shot Egocentric Auto-Labeling with Cross-Modal Consistency](https://arxiv.org/abs/2611.12149)

**<font color=#1a73e8>作者：</font>** Xiaozhi Zhang, Changjia Xu, Yaoyuan Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric auto-labeling requires depth, camera pose, object, and human-pose estimates to agree across independently developed models. Differences in units, coordinate conventions, and scale can make individually plausible predictions geometrically inconsistent. We present \textbf{EgoLabel}, a zero-shot pipeline that combines off-the-shelf models without target-domain labeled training and provides explicit cross-modal registration and consistency diagnostics. The pipeline integrates MonST3R for geometry, LocateAnything with GMC-BoT-SORT and SAM~2 for objects, and V-HPOT for hands; FisheyeViT provides a separate whole-body compatibility demonstration. Our main hand evaluation uses H2O sensor depth. Across 20 sequences, per-hand depth anchoring reduces the mean of per-sequence median hand--depth residuals by $23\%$ relative to a single global scale, yielding a pooled median of $84.6\,\mathrm{mm}$ against a $20.5\,\mathrm{mm}$ ground-truth reference. Hand PA-MPJPE is $14.53\pm1.29\,\mathrm{mm}$, whereas absolute MPJPE is $119.1\pm31.3\,\mathrm{mm}$, revealing a substantial gap between aligned and metric accuracy. On three RGB-only sequences, camera ATE is $1.40\pm0.29\,\mathrm{cm}$ after $\mathrm{Sim}(3)$ alignment. We also identify a sliding-window implementation issue that allows sensor-initialized depth to change during optimization. Because hand anchoring and its residual share the same depth map, the residual measures internal consistency rather than independent accuracy. These results characterize both the utility and the current limits of the registration pipeline.

---


### 422. [Beyond Flat Walks: Compositional Abstraction for Autoregressive Graph Generation](https://arxiv.org/abs/2611.12160)

**<font color=#1a73e8>作者：</font>** Kaiwen Bian, Andrew H. Yang, Yusu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive graph generators typically linearize graphs through flat node-edge walks, which can obscure higher-order structure in large and complex graphs. We introduce a hierarchical graph abstraction and coarse-to-fine generation pipeline that separates coarsening, tokenization, and decoding. This exposes three design axes: community coarsening, hierarchical tokenization, and order randomization. Across these axes, traversal-based hierarchy consistently improves distributional and structural fidelity, while its V.U.N.\ cost depends strongly on the coarsening and randomization policy. In particular, the fidelity--V.U.N.\ trade-off observed under within-community randomization is substantially reduced when traversal order is randomized across the full hierarchy. With a fixed backbone, training protocol, and matched training time across five molecular and five non-molecular benchmarks, hierarchical serialization yields consistent distributional and structural gains on all molecular datasets, while the non-molecular results further show that these gains depend on how well the supplied hierarchy aligns with structure in the target distribution. Together, these results characterize when and how hierarchical serialization benefits autoregressive graph generation.

---


### 423. [GPU-Accelerated Non-Interactive Encrypted Neural Network Training with Batched Diagonal Packing](https://arxiv.org/abs/2611.12161)

**<font color=#1a73e8>作者：</font>** Kentaro Mihara  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Training a neural network under homomorphic encryption requires transposes, batch reductions, optimizer updates, and repeated refreshes in addition to forward matrix products. We combine rectangular diagonal packing, feature-major SIMD mini-batch lanes, baby-step giant-step evaluation, and compact optimizer state in an MIT-licensed Rust CKKS implementation. Its CUDA path keeps training and bootstrap ciphertext arithmetic on the GPU, while retaining host key generation and client operations. In a matched 100-update experiment on the main non-interactive MNIST model, device-resident bootstrapping reduces training time from 14,268.295 to 293.075 seconds, a $48.68\times$ ratio against our CPU implementation, with exactly equal decoded parameters and predictions. Including setup and final evaluation gives a $40.67\times$ ratio. A separate GPU run completes ten passes over 4,800 images in 2,967.095 seconds and achieves 90.35% test accuracy versus 90.41% for its plaintext twin. These are single-initialization results; exact CPU/GPU parameter agreement is verified at 100 updates, not for the full 1,000-update run. Earlier completed CPU runs support a larger-batch key-switch advantage and baseline-batch accuracy within the registered tolerance, but the baseline-batch normalized key-switch target is missed. The released ReBoot baseline does not meet the common security-estimator threshold, and its full-setting CPU time is unmeasured. We therefore distinguish measured acceleration of our implementation from conditional layout comparisons and do not claim unconditional superiority over ReBoot.

---


### 424. [Replication of Thermal Comfort Cohort Models: No Support for Improved Thermal Preference Prediction](https://arxiv.org/abs/2611.12178)

**<font color=#1a73e8>作者：</font>** Thomas Hirsch, Katja Ceplak, Veronika Windisch 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cohort comfort models (CCMs) aim to overcome the extensive individual data requirements of personal comfort models (PCMs) by grouping occupants based on demographic and psychometric characteristics (cold start) or similar thermal preferences (warm start). We evaluated the validity of the reported CCM performance gains through (i) a methodological assessment of the original study, (ii) a replication using one of the two original datasets (DORN: 20 participants, 6 months) under a revised experimental protocol, and (iii) a replication using an independently collected dataset (PersonAI: 72 participants, 4 weeks). Classification performance was evaluated using F1-micro, as in the original study, and F1-macro to account for class imbalance. Under F1-micro, a trivial baseline that always outputs the majority class performed on par with cohort models. Under F1-macro, all cohort models achieved lower median scores than a simple baseline that makes random predictions based on the estimated distribution of thermal preferences. In our methodological assessment we identified the following key issues: Limited data per participant and per minority class, reliance on a metric insensitive to class imbalance, missing trivial baselines, inadequate cross validation strategy, and multiple occurrences of information leakage. Our findings challenge the original study's conclusion that CCMs improve thermal preference prediction. CCMs did not outperform simple class-distribution baselines. Future studies should improve experimental designs, including controlled thermal conditions, to obtain sufficient observations across thermal preference classes.

---


### 425. [Blind Variation, Selective Retention: Improving Creative Idea Generation in AI Scientists](https://arxiv.org/abs/2611.12184)

**<font color=#1a73e8>作者：</font>** Guowei Xu, Jiaru Zou, Mete Erdogan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery requires ideas that are original, useful, and non-obvious. Yet AI scientists are typically given as much task information as possible during idea generation, which can anchor generation toward familiar approaches. Inspired by the cognitive framework of Blind Variation and Selective Retention (BVSR), we propose a discovery framework that separates these two roles of information: it generates proposals under deliberately limited task information to broaden exploration, then learns from proposals previously verified on the same task and their outcomes to retain promising candidates for costly empirical evaluation. We evaluate BVSR across five proposer models and 12 scientific tasks. Limiting task information substantially increases proposal originality and non-obviousness, and produces a larger share of highly creative and high-utility proposals than existing state-of-the-art prompting-based baselines. Learning from prior proposal outcomes on the task further improves candidate selection, discarding half of the candidates while retaining most top-performing proposals. When incorporated into existing AI-scientist workflows, BVSR achieves stronger discoveries across gene expression analysis, drug response prediction, anomaly detection, scaling law discovery, and brain activity prediction. These results suggest that effective AI scientists should use information differently across stages of discovery: constrain task-specific information during exploration while exploiting accumulated empirical experience on the task.

---


### 426. [NearFormer: Linear-Size Sparse Attention via Randomized Near Neighbors](https://arxiv.org/abs/2611.12186)

**<font color=#1a73e8>作者：</font>** Ali Parviz, Alex Cloninger, Gal Mishne  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph transformers can capture long-range interactions, but their quadratic attention cost limits their use on large graphs. We introduce \emph{NearFormer}, a graph transformer whose global attention is restricted to a randomized near-neighbor (NN) graph. NearFormer uses an efficient randomized construction to connect each node to a small number of near neighbors from a broader neighborhood defined by a label-independent feature or spectral geometry. For a fixed retained budget \(k\), the resulting attention support has linear size \(\mathcal{O}(|E|+nk)\). The NN graph is built once by within-bin search and then held fixed. We use these edges as sparse global-attention supports, with optional learned attention biases, while preserving the original graph for local message passing. Experiments on long-range graph benchmarks and synthetic structural tasks show that NearFormer provides a favorable accuracy--scalability trade-off relative to local message passing, dense and sparse attention.

---


### 427. [The Deception Archive as a repository of standardized datasets for large-scale verbal deception detection research](https://arxiv.org/abs/2611.12196)

**<font color=#1a73e8>作者：</font>** Caterina Borgese, Riccardo Loconte, Lucca Pfründer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational advances in natural language processing and machine learning have substantially expanded the use of automated approaches in verbal deception research. However, existing verbal deception datasets remain fragmented across disciplines, as they are often difficult to identify, access, and reuse, limiting cross-study comparisons and the development of robust computational models. We present the Deception Archive, a curated and standardized repository of publicly available verbal deception datasets built upon a large-scale systematic review. Eligible datasets were retrieved, manually inspected, and standardized following a structured data curation workflow. The current repository comprises 41 publicly available datasets containing 387,995 truthful or deceptive statements. The archive represents a heterogeneous repository (e.g., in data size, topic of investigation, ground-truth, etc.) and a living resource for integrating newly available deception datasets over time. By providing centralized access to standardized datasets and accompanying metadata, the Deception Archive facilitates dataset discovery, cross-dataset validation, and reproducible evaluation of computational models.

---


### 428. [TrajLift: Lifting Memory Recall Trajectories with Latency-Modulated Heat Diffusion](https://arxiv.org/abs/2611.12197)

**<font color=#1a73e8>作者：</font>** Jiawen Kang, Jinchao Li, Mingyu Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verbal memory retrieval carries rich diagnostic information for Alzheimer's disease through the order, hesitation, and categorical organization of recalled words, yet computational modeling of this retrieval process remains largely unexplored. A key challenge is that timing and hierarchical structure are diagnostically entangled: the diagnostic meaning of retrieval timing depends on its hierarchical context. We propose TrajLift, a spectral framework that models verbal recall as timed trajectories on a hierarchical graph. Our central mechanism is latency-modulated heat diffusion on the semantic hierarchy, a unified operator that lifts each recalled word into a representation of both multi-scale hierarchical structure and continuous retrieval timing. Formal analysis shows that the resulting representation is first-order separable into structural and temporal components with spectral selectivity across hierarchical levels. On synthetic benchmarks requiring structure-time interaction, TrajLift stays near-perfect on deep hierarchies where all baselines fail. On real-world clinical data, we show that TrajLift outperforms diverse baselines by jointly modeling timing and semantic structure, with gains that grow as retrieval timing becomes more informative.

---


### 429. [Learning to Act with World Models by Valuing What Comes Next](https://arxiv.org/abs/2611.12200)

**<font color=#1a73e8>作者：</font>** Chenghao Gao, Zhi Zhang, Dian Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A sparse terminal reward tells an agent little about its steps. Much of the missing information is implicit in the environment's dynamics, because each state transition can change the conditions for success long before the reward arrives. A world model trained on real transitions can learn to predict what each action changes, but a predicted observation does not by itself show whether success has become more likely. With a binary terminal reward, PPO's critic makes this judgment by estimating the current policy's probability of success, but only for states the agent reaches. Our method, WM-PPO, elegantly brings the two together. For each action the policy samples, executed or not, the world model predicts the next observation and the critic values the predicted successor. In the policy channel, comparisons among these values give the policy auxiliary advantages; in the value channel, their mean gives the critic an auxiliary target. A shared gate weights both channels according to how reliably comparisons with similar margins predicted real outcomes earlier in training. The policy, critic and world model all learn from the agent's own interaction, with no teacher or privileged information, and only the policy is used at inference. With a comparable number of real environment steps, WM-PPO raises success from PPO's 63.5% to 87.5% on ALFWorld and from 39.3% to 52.9% on ScienceWorld. It matches the strongest PPO refinements we tested on ALFWorld and exceeds the best of them by 6.5 points on ScienceWorld. The trained policy more often completes prerequisite steps before placing an object or committing to an answer.

---


### 430. [An Empirical Evaluation of Quantum Kernel Stability in Network Intrusion Detection](https://arxiv.org/abs/2611.12219)

**<font color=#1a73e8>作者：</font>** Sreejonty Chakraborty, Adrita Rahman Tory, Muhammad Aminur Rahaman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum kernel methods have been proposed for network intrusion detection, yet their performance limitations are often attributed to noise in current quantum hardware. This study evaluates that assumption through a controlled analysis of Pegasos-QSVC on the NSL-KDD and ToN-IoT datasets. We perform 56 quantum experiments using one exact noiseless statevector backend and three noise-simulated superconducting backends while keeping preprocessing, PCA features, data splits, and classical baselines identical. XGBoost achieves accuracies of 98.94% on NSL-KDD and 99.41% on ToN-IoT, compared with 91.80% and 82.98% for Pegasos-QSVC. The quantum model also exhibits substantially greater seed-dependent variability. Eight runs collapse into degenerate classifiers, including four recall-collapse cases and four trivial-positive classifiers. Notably, two failures occur on the noiseless backend, demonstrating that hardware noise is not a necessary condition for classi-fier collapse. Kernel Gram matrix analysis further reveals low effective rank and severe ill-conditioning even in the absence of noise, indicating intrinsic fragility in the learned quantum representation. These results show that average accuracy alone can conceal operationally unacceptable behavior and highlight the importance of reporting worst-case performance, seed-level variability, class-specific metrics, and explicit degeneracy tests in quantum intrusion detection studies.

---


### 431. [Controlling Temporal Pseudo-Label Marginals for Stable Online Test-Time Adaptation](https://arxiv.org/abs/2611.12242)

**<font color=#1a73e8>作者：</font>** Rani Amar, Ofir Lindenbaum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual Test-Time Adaptation (CTTA) methods update models online using a stream of unlabeled data to overcome distribution shifts encountered at test time. However, CTTA is often unstable, as it can reinforce biases in early predictions and increasingly predict only a few classes, resulting in drift or even collapse. In this paper, we identify narrowing pseudo-label class usage as an indicator of CTTA instability and quantify this behavior. Most existing methods have attempted to address this issue by either selecting reliable adaptation samples or re-weighting the loss to encourage diverse pseudo-labels, but they do not explicitly enforce a class marginal over a temporal window. Instead, we propose Sinkhorn Class-Marginal Regularization (SCALAR), a simple plug-and-play module that controls the pseudo-label distribution over a short temporal window. SCALAR works by maintaining recent predictions in a buffer, balancing their class distribution via the Sinkhorn algorithm to match a specified target distribution, and using the balanced soft targets for adaptation. Without changing the model architecture, SCALAR maintains the per-step runtime and increases the peak allocated GPU memory by only 10 MB on ImageNet-C. Our method is particularly effective on skewed, non-stationary data with severe distribution shifts, where SCALAR significantly alleviates drift and collapse when combined with existing stabilization methods based on entropy or diversity.

---


### 432. [CADMA: Capacity-Aware Coverage Decomposition for Generative Model Assessment](https://arxiv.org/abs/2611.12243)

**<font color=#1a73e8>作者：</font>** Debin Meng, Zheng Gao, Ziquan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating generative models requires measuring not only sample fidelity but also how well a generated set covers the real data distribution. Recent work has therefore introduced recall-oriented metrics for distribution-level evaluation. However, existing recall metrics often reduce distributional coverage to geometry-based coverage. This simplifying assumption weakens their diagnostic value and interpretability in two ways: these metrics provide only a single aggregate score that cannot distinguish essential diversity failures such as mode dropping and mode collapse, and geometry-based coverage can provide unreliable estimates by assigning high scores to poorly covered generative distributions. We therefore introduce CADMA, a capacity-aware framework for recall-oriented evaluation and diagnosis. CADMA evaluates distributional coverage through local capacity matching between real and generated samples, separating geometry-based coverage from effective coverage. This yields multi-dimensional coverage diagnostics that quantify mode dropping and mode collapse while reducing the overly optimistic estimates produced by geometry-based metrics. Through extensive experiments on toy data, real-world datasets, and generative models, we show that CADMA provides more reliable coverage estimates and more fine-grained, interpretable diagnostic signals of diversity failures than existing metrics. Our code is available at this https URL.

---


### 433. [A method to automatically discover symbolic local learning rules](https://arxiv.org/abs/2611.12248)

**<font color=#1a73e8>作者：</font>** Andrea Perin, Fabio Anselmi, Stephane Deny  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a general method for discovering symbolic local learning rules that can replace backpropagation, applicable, in principle, to any deep learning architecture and task. The method automatically discovers local loss functions specific to each layer by (1) constructing a dictionary of monomials of local tensor variables, inspired by Penrose diagram notation, (2) regressing over coefficients weighting these monomials to build layerwise polynomial losses whose gradients together minimize a target global loss. We test the method on classification, reconstruction, and self-supervised learning tasks with small multilayer networks and minimal datasets. Across all tasks, the discovered rules induce non-trivial interactions between layers, which lead to significant reductions in the corresponding global losses. Furthermore, the method selects sparse combinations of monomials, finding local rules that are more interpretable than those generated by MLP-based alternatives. The potential implications of our method range from energy-efficient deep learning to the discovery of biologically plausible learning mechanisms.

---


### 434. [RAIL: Representation-Aligned Imitation Learning for Student-Compatible Teacher Policies](https://arxiv.org/abs/2611.12251)

**<font color=#1a73e8>作者：</font>** Meraj Mammadov, Pedro Zuidberg Dos Martires, Johannes Andreas Stork  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) from raw sensory inputs such as images or onboard sensors can be challenging due to high-dimensional observations and sparse rewards. A common strategy is to train a teacher policy with access to privileged state information and then distill it into a student policy that acts from raw inputs alone. However, when the teacher relies on information unavailable to the student, exact imitation may be impossible, creating an irreducible imitation gap. Existing approaches typically mitigate this mismatch through careful reward shaping or additional reinforcement learning on the student policy after the teacher has been trained. Instead, we introduce Representation-Aligned Imitation Learning (RAIL), which addresses the mismatch during teacher training itself. RAIL learns a latent representation shared across teacher and student observations using contrastive learning, and trains the teacher policy directly in this space. Because the teacher policy is constrained to operate on this shared space, it learns behaviors that are reproducible from student observations. This substantially reduces the imitation gap while preserving task performance. Across multiple environments, RAIL outperforms strong baselines without reward modification or post-hoc student fine-tuning, and surpasses direct reinforcement learning from raw observations. The learned representations further enable zero-shot transfer to new tasks through teacher-only training. Project site: this https URL.

---


### 435. [Lessons Not Learned: Why Cross-Chain Bridges Keep Losing Billions the Same Way](https://arxiv.org/abs/2611.12252)

**<font color=#1a73e8>作者：</font>** Mohsen Ahmadvand, Piotr Dobaczewski, Camille Bouzerand  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bridge hacks have cost billions, often without exploiting a code bug. In the cross-chain bridge hacks we catalogue from 2021 to 2026, failures of security posture, meaning how a bridge's people, code, controls and off-chain infrastructure are set up, account for 88% of reported losses since 2023, and nearly all repeat earlier failures. Code audits cannot catch these failures, so we propose a bridge security assessment rubric. It scores each bridge deployment from on-chain evidence, and a hard cap drops the score to the lowest value when a fatal risk is present. A token is only as safe as its weakest deployment if all its deployments share one backing. For attacks nobody anticipated, we show that rate limits and an emergency stop still bound the loss. We build an analyzer that applies the rubric to deployed bridges and monitors them for changes, and an agentic analyzer that runs the same checks on any bridge. Operators learn what to fix, and users can compare bridges. Our rubric's controls cut bridge hack losses 105-fold, from \$3.52B to \$33M.

---


### 436. [Odds-Structured Distributional Regression for Interpretable Time-to-Event Prediction](https://arxiv.org/abs/2611.12268)

**<font color=#1a73e8>作者：</font>** Jakob Versnjak, Manuel Welte, Titus Kuehne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-to-event prediction is fundamentally challenged by partial observability and aleatoric uncertainty. In clinical medicine, for instance, the timing of disease progression or acute readmission is contingent on highly dynamic and largely latent health trajectories. Rather than forcing a deterministic point forecast, distributional regression offers a principled means to address this complexity by predicting a probability distribution over time. However, explaining these distributional predictions presents a key obstacle: raw distribution parameters output by the model are abstract mathematical quantities that do not align well with domain concepts. To gain interpretability, we propose a novel paradigm where output parameters are designed to be additive in log-odds---a widely established measure in clinical risk modeling. Our approach, called ODDS-DR, moves beyond technical convenience to deliver clear domain alignment as well as the layer-wise computational structure required for robust, time-dependent feature attribution. Validated across two real-world clinical cohorts, our framework matches state-of-the-art predictive performance while resolving distributional outputs into interpretable risk markers across flexible prognostic horizons.

---


### 437. [Public, Identifiable, and Effectively Immutable: Ethical Lessons from Research on arXiv](https://arxiv.org/abs/2611.12271)

**<font color=#1a73e8>作者：</font>** Jan Pennekamp, Johannes Lohmöller, Peter Mayer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ethical decision-making is central to safe cybersecurity research. Recent studies, one of which is our own, analyzing the source files of arXiv papers bring this challenge to light - arXiv publicly distributes the source files, to the surprise of many authors. Unique aspects reveal ethical challenges and dilemmas that extend beyond established ethical frameworks, institutional processes, and community best practices. In this work, we examine this case and provide insights for similar research on other public live resources, such as Zenodo or the Wayback Machine. While such empirical studies are particularly realistic, they must account for personally identifiable information, leaked secrets, and other sensitive details that could expose, shame, or otherwise negatively affect individuals, possibly leading to both reputational and practical harm. sDrawing on our collective experience and discussions among researchers, affected authors, and readers, we make three contributions: First, we define the ethical setting and highlight that even intentionally-public data with deliberate real-name attribution can raise ethical concerns when repurposed for empirical analysis. Second, we discuss the ethical issues surrounding the use of arXiv data and derive four higher-level dilemmas that researchers may face when working with similar data. Third, we derive practical guidance for ethically navigating such settings and, in doing so, distill four lessons for research on arXiv and similar public, live datasets: public availability should serve as the starting point of ethical reasoning; research should minimize the amplification it induces on exposed information; disclosure should be calibrated to the harm, confidence, and actionability of a finding; and effective immutability must be accounted for. Together, these contribute to community resources for ethically-sound cybersecurity experiments.

---


### 438. [Representational Alignment between Deep Neural Networks and Human Brain in Speech Processing under Audiovisual Noise](https://arxiv.org/abs/2611.12291)

**<font color=#1a73e8>作者：</font>** Cheng Luo, Jian Zhu, Zhoujian Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speech comprehension in the human brain is an incremental process that begins with acoustic processing and advances to linguistic processing. While recent studies have revealed that the hierarchy of deep neural networks (DNNs) correlates with the ascending auditory pathway, the exact nature of this DNN-brain alignment remains underexplored. In this study, we investigate how DNN representations align with the brain's acoustic-to-linguistic processing. Specifically, we employed neural encoding models to simulate neural responses to acoustic (i.e., speech and noise envelope) and linguistic features (i.e., word onset and surprisal). By applying representational similarity analysis (RSA), we quantified the similarity between these neural responses and the DNN embeddings generated by a pre-trained automatic speech recognition (ASR) model, both before and after fine-tuning on audiovisual noisy data. Our results demonstrate significant DNN-brain alignment: embeddings from shallow layers exhibit higher similarity to neural responses associated with acoustic features, while those from deeper layers align more closely with neural responses related to linguistic features. Importantly, the fine-tuning process enhances this alignment by improving noise processing in shallower layers and refining linguistic representations in deeper layers. These results suggest that fine-tuned DNN models can naturally develop human-like processing patterns in noisy environments, highlighting a functional alignment between the human brain and DNNs in speech representation.

---


### 439. [PACE-ECG: Patient-Aware Contrastive ECG Pretraining; Leveraging Longitudinal Structure for Transferable Representations](https://arxiv.org/abs/2611.12307)

**<font color=#1a73e8>作者：</font>** Riccardo Cavarra, Lupo Lovatelli, Shaheim Ogbomo-Harmitt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models for physiological signals are commonly evaluated on in-domain interpretation tasks, but their ability to transfer to longitudinal clinical prognosis across healthcare systems remains uncertain. We developed PACE-ECG, an ECG pretraining framework that combines contrastive learning across temporally neighbouring recordings from the same patient with clinically guided multitask supervision. We evaluated frozen ECG representations for post-myocardial-infarction all-cause mortality and incident heart failure prediction across MIMIC-IV and two external HEEDB cohorts, comparing the proposed representation with DeepECG-SSL, a state-of-the-art model, and two control baselines. Across both downstream tasks, the proposed model outperformed DeepECG-SSL in-domain (AUROC +1.9% for mortality and +4.0% for heart failure) and on external populations in HEEDB-Boston (+5.6% for mortality +10.3% for heart failure) and HEEDB-Atlanta (+6.9% for mortality +11.0% for heart failure) while using an encoder 41 times smaller and a fraction of the pretraining data. A matched ablation showed that patient-temporal pairing improved external mortality and heart failure AUROC over generic self-supervision by 7.0% and 9.4% on HEEDB-Boston and 8.9% and 9.3% on HEEDB-Atlanta. These findings indicate that pretraining-objective design greatly influences downstream transfer alongside model and data scale, and that in-domain performance alone is insufficient to establish the clinical generalisability of ECG foundation representations.

---


### 440. [The Optimal Rate Constant of Heavy-Ball Momentum on Smooth Strongly Convex Functions](https://arxiv.org/abs/2611.12310)

**<font color=#1a73e8>作者：</font>** Marcos Hernanz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The heavy-ball method with a constant step size and a constant momentum parameter accelerates gradient descent on quadratics, but no choice of the two parameters does so on the class of smooth strongly convex functions. We determine how much faster than gradient descent it can be made on this class. Writing the best worst-case rate over all tunings as $1-c(\kappa)/\kappa$, where $\kappa$ is the condition number, we prove that $c(\kappa)$ tends to $8$ in every dimension of two or more. The lower bound on the rate holds for every tuning, because a tuning that is faster than $1-8/\kappa$ on quadratics follows a slowly decaying spiral on some function of two variables. The matching upper bound comes from an explicit tuning, with nearly the momentum of Polyak's tuning and a step size about $\sqrt{\kappa}/8$ times smaller, and from a Lyapunov function whose positivity is verified in exact arithmetic. Optimally tuned heavy-ball is therefore asymptotically four times faster than gradient descent on this class.

---


### 441. [A Modular Perspective for Modeling MARL Systems](https://arxiv.org/abs/2611.12314)

**<font color=#1a73e8>作者：</font>** Tiziano Maisonhaute, Jean-Christophe Soulié, Fabien Michel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing complexity of Multi-Agent Reinforcement Learning (MARL) has fragmented the literature, obscuring underlying architectural choices behind diverse implementations. This fragmentation makes it difficult to evaluate critical modeling dimensions in isolation, identify how components affect the resulting system dynamics, and compare, reuse, or combine contributions across the literature.
This paper proposes a modular perspective for modeling, analyzing, and implementing MARL systems. We decompose them into eight functional modules: agents, environments, learning, reward modeling, training and execution modes, communication, modeling of other agents, and evaluation criteria. For each module, we clarify its role and review representative approaches.
We instantiate this decomposition in MARLKIT, a framework whose modules are explicit and interchangeable. MARLKIT demonstrates how the proposed perspective supports transparent experimental assumptions and the controlled variation and combination of MARL mechanisms. Experiments illustrate its ability to prototype, compare, reuse and combine modules while making differences between configurations explicit.
Overall, the paper provides a structured perspective on MARL modeling and implementation, offering a common language for making modeling choices explicit, supporting clearer descriptions of MARL approaches, and supporting more controlled experimentation through the systematic isolation and combination of MARL mechanisms.

---


### 442. [How Many Exposures Does a World Model Need? Learning Unseen Game Mechanics at Test Time](https://arxiv.org/abs/2611.12324)

**<font color=#1a73e8>作者：</font>** Ku Onoda, Haruto Kawano, Shota Takashiro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models enable agents to plan and learn from imagined experience, but in an unfamiliar environment they must learn its mechanics from limited interaction. A mechanic is a rule for how an action or an interaction changes part of the environment. Each occurrence of a mechanic that the model observes is one exposure. We ask how many exposures a world model needs to predict the effects of a new environment's mechanics. We address this question on ARC-AGI-3, a benchmark of interactive games defined by their programs. We introduce MechEval, which labels 69 recurring mechanics across 20 games from these programs. It scores each prediction on the cells the mechanic changes at each exposure. As a test bed, we build WARC (World model for ARC-AGI-3), a 35M-parameter vision transformer that is pretrained on other games and updates all of its parameters after each transition. On held-out games, WARC learns to predict four in five mechanics with at least 80% accuracy on the cells they change and keeps that accuracy to the end of the recordings. Half of them reach that accuracy within about 80 exposures, in a single play of the game, and without updates only one in seven does at all. In closed-loop play on the public games, WARC-Agent, which pairs WARC with a fixed graph explorer, triples the explorer's official efficiency score from 0.15 to 0.46, mostly through test-time training. On the hidden games of the Kaggle leaderboard, our entry scores 0.20.

---


### 443. [An Explicit Below Half Threshold Bound for the Local Leakage Resilience of Shamir's Secret Sharing Scheme](https://arxiv.org/abs/2611.12325)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Xin Wang, Xiangliang Kong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As a fundamental cryptographic primitive, secret sharing distributes a secret among multiple parties and allows certain authorized parties to recover the secret while preventing unauthorized parties from knowing the secret. However, local leakage from each party member allows an adversary to learn partial information from each share, which is not guaranteed by traditional security. In this paper, we study bounds on the reconstruction threshold of Shamir's secret sharing scheme over prime fields against arbitrary 1-bit local leakage. We show that, for all sufficiently large $n$ and every prime $p>n$, the $(n,t)$-Shamir's scheme is $\exp(-\Omega(n))$-resilient whenever $t/n\geq 0.489$, for any choice of distinct nonzero evaluation points. Our proof refines the dual-code list recovery analysis and combines complementary Fourier estimates according to the support sizes and biases of the leakage functions, yielding an improved explicit reconstruction threshold bound.

---


### 444. [Rethinking Radar 3D Perception: Representation Learning from Raw Spectra](https://arxiv.org/abs/2611.12334)

**<font color=#1a73e8>作者：</font>** Miao Zhang, Mohamed Abdelsamad, Bin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Raw radar spectra are widely viewed as too cluttered and noisy for direct representation learning, motivating handcrafted reductions, sparse point clouds, or compact Doppler descriptors in radar perception. We challenge this assumption and argue that the main limitation lies not in the raw representation itself, but in the absence of a learning objective that separates structured signal from noise. Handcrafted reductions partially address this problem but impose rigid assumptions about what constitutes signal, discarding weak yet informative structure while retaining artifacts that fit the reduction model. Once removed, such information cannot be recovered by supervised learning. We propose an alternative: structure is the component of a radar spectrum that remains reconstructable under localized corruption, while noise is the component that does not. This perspective motivates self-supervised masked modeling for dense radar spectra without predefined signal-noise separation. We instantiate it with Leakage-aware Spectral MAE, a masked autoencoder for raw radar cubes using a corruption strategy inspired by cross-bin energy spreading caused by spectral leakage. We also demonstrate the importance of Doppler organization: treating Doppler as a primary spatial dimension in an x-y-D representation, with height encoded as features, substantially outperforms naive channel stacking and enables effective learning from dense 4D spectra. Without handcrafted reductions, our approach consistently outperforms state-of-the-art radar-based detectors and point-cloud-based self-supervised learning (SSL) counterparts. These results establish raw radar spectra as an effective representation for 3D perception when paired with an appropriate pretraining objective.

---


### 445. [Evidence or Marginal? What Moment-Vector Propagation Computes in Polynomial Density Neurons](https://arxiv.org/abs/2611.12339)

**<font color=#1a73e8>作者：</font>** Przemysław Spyra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a neuron's input is lost, or known through a belief $q$, what should it output? For a neuron storing a joint polynomial density $N$ with input density $D$, two formulas compete. $p_\mathrm{CD}=E_q[N]/E_q[D]$ costs one matrix-vector product; Hierarchical Correlation Reconstruction introduces it as a constant-denominator approximation to $p_\mathrm{EU}=E_q[N/D]$. For a density model both are exact answers to different questions: $p_\mathrm{CD}$ is Bayesian updating with the belief as virtual evidence; $p_\mathrm{EU}$ installs the belief as a new marginal (Jeffrey's rule). With a missing input $p_\mathrm{CD}$ returns the model's conditional; $p_\mathrm{EU}$ generally does not. This post hoc reading is proved, and illustrated outside the pair family up to $k=8$ inputs; it has no pre-registered test, only one exploratory real-data pilot. Post hoc, closed forms fall within a factor 2 of all 112 measured gaps, and negative density begins near input correlation $1/k$. In a pre-registered synthetic study (up to 32 inputs), 5 of 15 hypotheses are supported, 2 inconclusive and 8 not supported, including all three on transfer beyond equicorrelated Gaussians. Post hoc, where $p_\mathrm{EU}$ is defined, truncation usually outweighs the gap for Beta beliefs in pair neurons; triple neurons under flat and data beliefs are exceptions.

---


### 446. [ReVMap: Vectorized Global Mapping via Connectivity-Aware Local Map Fusion](https://arxiv.org/abs/2611.12346)

**<font color=#1a73e8>作者：</font>** Hongjae Shin, Jungho Kim, Donghyuk Kwak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale annotation of vectorized high-definition (HD) maps is labor-intensive and costly, motivating local-to-global auto-labeling approaches that incrementally construct global maps from local vectorized predictions. However, existing approaches often overlook prediction uncertainty and rely on heuristic map integration, potentially propagating errors and introducing topological inconsistencies. To address these limitations, we propose ReVMap, a reliable local-to-global framework that iteratively refines local map predictions and global map construction through uncertainty-guided prior utilization and connectivity-guided global map revision. Specifically, ReVMap leverages point-wise localization uncertainty to incorporate global map priors into local map prediction, improving robustness against inaccurate prior information. It then predicts local-to-global connectivity and selectively updates the global map through uncertainty-aware fusion based on the reliability of local predictions. By iteratively coupling local prediction and global revision, ReVMap progressively improves both local map accuracy and global map consistency. Extensive experiments on the nuScenes and Argoverse 2 benchmarks demonstrate that ReVMap achieves state-of-the-art performance in both local map prediction and global map construction.

---


### 447. [TRIAD: Multimodal Retrieval across Abstraction, Constraints, and State](https://arxiv.org/abs/2611.12364)

**<font color=#1a73e8>作者：</font>** Xiangyang Wu, Chen Ju, Xu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval increasingly supports agentic systems, where user requests can involve cross-level relations, combine multiple constraints, and evolve across dialogue turns. In these settings, a highly similar result may still violate the user's requirements, while retrieved content may directly inform downstream actions without human screening. We introduce TRIAD, a multimodal retrieval benchmark for evaluating how well retrieval systems satisfy these complex, evolving requests. TRIAD comprises three tracks: abstraction, testing bidirectional retrieval between visual instances and concepts at different hierarchical levels; constraints, testing the joint satisfaction of positive and negative conditions; and state, testing the integration of requirements across dialogue turns and the updating of earlier conditions when users revise their requests. The benchmark contains six subsets, each with 1,000 queries and a fixed pool of 1,000 candidates per query, evaluated using a common multi-positive mean average precision (mAP) protocol. Simpler reference tasks and hard negatives grouped by the requirements they violate help characterize specific retrieval difficulties. We evaluate 20 configurations of 17 systems and find that no system leads across all six subsets. Performance declines with hierarchical distance, and negative-only queries generally underperform positive-only queries with the same number of constraints. Across paired tasks expressing the same final intent, multi-turn retrieval yields lower mAP in 39 of 40 configuration-domain comparisons. The benefits of explicit reasoning also vary across models and tasks. These findings highlight the gap between retrieving similar content and satisfying a complete request.

---


### 448. [An Agile Homomorphic Encryption and ML-KEM Scheme for Privacy-Preserving Health Data Processing](https://arxiv.org/abs/2611.12367)

**<font color=#1a73e8>作者：</font>** Daniel Resende, Nadia El Mrabet, Ulrich K{ü}hne  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The storage and processing of health data raise serious privacy concerns; therefore, the data must be encrypted. Fully Homomorphic Encryption (FHE) allows computations on encrypted data, which makes it a very promising technology in this context. However, although the efficiency of FHE algorithms has improved in recent years, they remain very complex. The security of several prominent FHE schemes is based on variants of the Learning With Errors (LWE) problem, which is also the basis of Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), the new post-quantum standard for asymmetric encryption. In this paper, we propose an agile cryptographic scheme -combining ML-KEM and BGV -that allows efficient implementations in an embedded use case. We describe the parameter selection for the proposed scheme and show its feasibility with a proof-of-concept implementation.

---


### 449. [Reconstructing hourly traffic on every street of a capital from a sparse counting network: a graph neural network applied to Paris](https://arxiv.org/abs/2611.12379)

**<font color=#1a73e8>作者：</font>** Xavier Jurado, C{é}dric Wemmert, Nicolas Reiminger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Micro-scale air quality models require hourly traffic data on every road segment, whereas permanent counters cover only a small part of the network. A graph neural network (GNN) was developed to reconstruct hourly traffic flows on the 32,163 road segments of Paris intra-muros from the 1,573 segments equipped with a counter (4.9%). The model adapts the Graph Neural Network for Urban Interpolation (GNNUI) to a real, sparse counting network. Flows are decoded on the edges of the junction graph (one edge per segment, both directions summed), a traffic climatology serves as an offset in a zero-inflated negative-binomial likelihood, and training proceeds by masking counters. Eight-fold spatial cross-validation, with counters sharing a published series merged before splitting, distinguishes interpolation at a withheld counter in an instrumented district (R${}^2$ = 0.89, error of a quarter of the mean flow) from extrapolation to a district without counters (R${}^2$ = 0.74, a third of the mean flow). These scores hold on main axes where counters are located, while relative errors are about 50% on the few counted local streets. Ablations show that the climatology offset tends to help extrapolation. Road attributes, time cycles and the live state of the counting network matter most, while weather inputs have no significant effect. The masking rate is the only inherited hyperparameter with a clear effect. When evaluated on January--August 2026 (outside the training period), the frozen model stayed around the error band of previous years.

---


### 450. [PTC-IoU: CPU-Friendly Detection Quality Estimation for Edge Video Analytics](https://arxiv.org/abs/2611.12405)

**<font color=#1a73e8>作者：</font>** Wei Geng, Hyerin Kim, Chang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An edge video analytics system must estimate the quality of local detections since there are no ground-truth labels available during runtime. Detectors usually provide confidence scores for their results, but these scores can not reveal every missed object or misplaced bounding box. So a quality estimator is necessary to provide a decision signal indicating which frame has potential detection failures that need to be escalated to a more powerful model in the cloud. Neural network based estimators add workload to the GPU already running detection, while CPU capacity may remain available. We present Predictive Temporal Consistency IoU (PTC-IoU), which moves this workload to CPU by compacting detection boxes histories to support deterministic result scoring. Comparing to neural counterparts, experiments on representative edge hardware, Nvidia Jetson Orin Nano, show that our method reduced per-frame estimator latency from 10.3 ms for neural counterparts to 2.2 ms (4.7x faster), increased pipelined throughput by 13.6%, and cuts estimator energy consumption by up to 95%, while maintaining competitive final detection quality verified on multiple datasets.

---


> [!TIP]
> 当前位于：**401-450**（第 9/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
