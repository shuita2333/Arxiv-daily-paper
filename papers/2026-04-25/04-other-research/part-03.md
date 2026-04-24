# 📦 其他研究 | 2026年04月25日

> 本类共 **231** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-231](./part-05.md)

---

### 101. [Beyond Single Plots: A Benchmark for Question Answering on Multi-Charts](https://arxiv.org/abs/2604.21344)

**<font color=#1a73e8>作者：</font>** Azher Ahmed Efat, Seok Hwan Song, Wallapak Tavanapong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Charts are widely used to present complex information. Deriving meaningful insights in real-world contexts often requires interpreting multiple related charts together. Research on understanding multi-chart images has not been extensively explored. We introduce PolyChartQA, a mid-scale dataset specifically designed for question answering over multi-chart images. PolyChartQA comprises 534 multi-chart images (with a total of 2,297 sub-charts) sourced from peer-reviewed computer science research publications and 2,694 QA pairs. We evaluate the performance of nine state-of-the-art Multimodal Language Models (MLMs) on PolyChartQA across question type, difficulty, question source, and key structural characteristics of multi-charts. Our results show a 27.4% LLM-based accuracy (L-Accuracy) drop on human-authored questions compared to MLM-generated questions, and a 5.39% L-accuracy gain with our proposed prompting method.

---


### 102. [Evaluating AI Meeting Summaries with a Reusable Cross-Domain Pipeline](https://arxiv.org/abs/2604.21345)

**<font color=#1a73e8>作者：</font>** Philip Zhong, Don Wang, Jason Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a reusable evaluation pipeline for generative AI applications, instantiated for AI meeting summaries and released with a public artifact package derived from a Dataset Pipeline. The system separates reusable orchestration from task-specific semantics across five stages: source intake, structured reference construction, candidate generation, structured scoring, and reporting. Unlike standalone claim scorers, it treats both ground truth and evaluator outputs as typed, persisted artifacts, enabling aggregation, issue analysis, and statistical testing.
We benchmark the offline loop on a typed dataset of 114 meetings spanning city_council, private_data, and whitehouse_press_briefings, producing 340 meeting-model pairs and 680 judge runs across gpt-4.1-mini, gpt-5-mini, and gpt-5.1. Under this protocol, gpt-4.1-mini achieves the highest mean accuracy (0.583), while gpt-5.1 leads in completeness (0.886) and coverage (0.942). Paired sign tests with Holm correction show no significant accuracy winner but confirm significant retention gains for gpt-5.1.
A typed DeepEval contrastive baseline preserves retention ordering but reports higher holistic accuracy, suggesting that reference-based scoring may overlook unsupported-specifics errors captured by claim-grounded evaluation. Typed analysis identifies whitehouse_press_briefings as an accuracy-challenging domain with frequent unsupported specifics. A deployment follow-up shows gpt-5.4 outperforming gpt-4.1 across all metrics, with statistically robust gains on retention metrics under the same protocol. The system benchmarks the offline loop and documents, but does not quantitatively evaluate, the online feedback-to-evaluation path.

---


### 103. [Trust-SSL: Additive-Residual Selective Invariance for Robust Aerial Self-Supervised Learning](https://arxiv.org/abs/2604.21349)

**<font color=#1a73e8>作者：</font>** Wadii Boulila, Adel Ammar, Bilel Benjdira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) is a standard approach for representation learning in aerial imagery. Existing methods enforce invariance between augmented views, which works well when augmentations preserve semantic content. However, aerial images are frequently degraded by haze, motion blur, rain, and occlusion that remove critical evidence. Enforcing alignment between a clean and a severely degraded view can introduce spurious structure into the latent space. This study proposes a training strategy and architectural modification to enhance SSL robustness to such corruptions. It introduces a per-sample, per-factor trust weight into the alignment objective, combined with the base contrastive loss as an additive residual. A stop-gradient is applied to the trust weight instead of a multiplicative gate. While a multiplicative gate is a natural choice, experiments show it impairs the backbone, whereas our additive-residual approach improves it. Using a 200-epoch protocol on a 210,000-image corpus, the method achieves the highest mean linear-probe accuracy among six backbones on EuroSAT, AID, and NWPU-RESISC45 (90.20% compared to 88.46% for SimCLR and 89.82% for VICReg). It yields the largest improvements under severe information-erasing corruptions on EuroSAT (+19.9 points on haze at s=5 over SimCLR). The method also demonstrates consistent gains of +1 to +3 points in Mahalanobis AUROC on a zero-shot cross-domain stress test using BDD100K weather splits. Two ablations (scalar uncertainty and cosine gate) indicate the additive-residual formulation is the primary source of these improvements. An evidential variant using Dempster-Shafer fusion introduces interpretable signals of conflict and ignorance. These findings offer a concrete design principle for uncertainty-aware SSL. Code is publicly available at this https URL.

---


### 104. [Decoupled Travel Planning with Behavior Forest](https://arxiv.org/abs/2604.21354)

**<font color=#1a73e8>作者：</font>** Duanyang Yuan, Sihang Zhou, Yanning Hou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavior sequences, composed of executable steps, serve as the operational foundation for multi-constraint planning problems such as travel planning. In such tasks, each planning step is not only constrained locally but also influenced by global constraints spanning multiple subtasks, leading to a tightly coupled and complex decision process. Existing travel planning methods typically rely on a single decision space that entangles all subtasks and constraints, failing to distinguish between locally acting constraints within a subtask and global constraints that span multiple subtasks. Consequently, the model is forced to jointly reason over local and global constraints at each decision step, increasing the reasoning burden and reducing planning efficiency. To address this problem, we propose the Behavior Forest method. Specifically, our approach structures the decision-making process into a forest of parallel behavior trees, where each behavior tree is responsible for a subtask. A global coordination mechanism is introduced to orchestrate the interactions among these trees, enabling modular and coherent travel planning. Within this framework, large language models are embedded as decision engines within behavior tree nodes, performing localized reasoning conditioned on task-specific constraints to generate candidate subplans and adapt decisions based on coordination feedback. The behavior trees, in turn, provide an explicit control structure that guides LLM generation. This design decouples complex tasks and constraints into manageable subspaces, enabling task-specific reasoning and reducing the cognitive load of LLM. Experimental results show that our method outperforms state-of-the-art methods by 6.67% on the TravelPlanner and by 11.82% on the ChinaTravel benchmarks, demonstrating its effectiveness in increasing LLM performance for complex multi-constraint travel planning.

---


### 105. [SparseGF: A Height-Aware Sparse Segmentation Framework with Context Compression for Robust Ground Filtering Across Urban to Natural Scenes](https://arxiv.org/abs/2604.21356)

**<font color=#1a73e8>作者：</font>** Nannan Qin, Pengjie Tao, Haiyan Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality digital terrain models derived from airborne laser scanning (ALS) data are essential for a wide range of geospatial analyses, and their generation typically relies on robust ground filtering (GF) to separate point clouds across diverse landscapes into ground and non-ground parts. Although current deep-learning-based GF methods have demonstrated impressive performance, especially in specific challenging terrains, their cross-scene generalization remains limited by two persistent issues: the context-detail dilemma in large-scale processing due to limited computational resources, and the random misclassification of tall objects arising from classification-only optimization. To overcome these limitations, we propose SparseGF, a height-aware sparse segmentation framework enhanced with context compression. It is built upon three key innovations: (1) a convex-mirror-inspired context compression module that condenses expansive contexts into compact representations while preserving central details; (2) a hybrid sparse voxel-point network architecture that effectively interprets compressed representations while mitigating compression-induced geometric distortion; and (3) a height-aware loss function that explicitly enforces topographic elevation priors during training to suppress random misclassification of tall objects. Extensive evaluations on two large-scale ALS benchmark datasets demonstrate that SparseGF delivers robust GF across urban to natural terrains, achieving leading performance in complex urban scenes, competitive results on mixed terrains, and moderate yet non-catastrophic accuracy in densely forested steep areas. This work offers new insights into deep-learning-based GF research and encourages further exploration toward truly cross-scene generalization for large-scale environmental monitoring.

---


### 106. [Time, Causality, and Observability Failures in Distributed AI Inference Systems](https://arxiv.org/abs/2604.21361)

**<font color=#1a73e8>作者：</font>** Ankur Sharma, Deep Shah, David Lariviere 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed AI inference pipelines rely heavily on timestamp-based observability to understand system behavior. This work demonstrates that even small clock skew between nodes can cause observability to become causally incorrect while the system itself remains functionally correct and performant. We present controlled experiments on a multi-node AI inference pipeline, where clock skew is introduced at a single stage. Results show that no violations are observed under synchronized conditions and up to 3 ms skew, while clear causality violations emerge by 5 ms. Despite this, system throughput and output correctness remain largely unaffected. We further observe that violation behavior is not strictly static. In longer runs, negative span rates may stabilize or decrease over time, indicating that effective skew evolves due to relative clock drift between nodes. Experiments were conducted using Kafka and ZeroMQ transports, with consistent results across both. Aeron is under active exploration but is not yet included in the completed validation set. These findings suggest that observability correctness depends not only on system functionality but also on precise time alignment, and that timing must be treated as a first-class concern in distributed AI systems.

---


### 107. [KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362)

**<font color=#1a73e8>作者：</font>** Linkai Liu, Wei Feng, Xi Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Creative Generation (CG) leverages generative models to automatically produce advertising content that highlights product features, and it has been a significant focus of recent research. However, while CG has advanced considerably, most efforts have concentrated on generating advertising text and images, leaving Creative Video Generation (CVG) relatively underexplored. This gap is largely due to two major challenges faced by Text-to-Video (T2V) models: (a) \textbf{ambiguous semantic alignment}, where models struggle to accurately correlate product selling points with creative video content, and (b) \textbf{inadequate motion adaptability}, resulting in unrealistic movements and distortions. To address these challenges, we develop a comprehensive Advertising Creative Knowledge Base (ACKB) as a foundational resource and propose a knowledge-driven approach (KD-CVG) to overcome the knowledge limitations of existing models. KD-CVG consists of two primary modules: Semantic-Aware Retrieval (SAR) and Multimodal Knowledge Reference (MKR). SAR utilizes the semantic awareness of graph attention networks and reinforcement learning feedback to enhance the model's comprehension of the connections between selling points and creative videos. Building on this, MKR incorporates semantic and motion priors into the T2V model to address existing knowledge gaps. Extensive experiments have demonstrated KD-CVG's superior performance in achieving semantic alignment and motion adaptability, validating its effectiveness over other state-of-the-art methods. The code and dataset will be open source at this https URL.

---


### 108. [Channel-Free Human Activity Recognition via Inductive-Bias-Aware Fusion Design for Heterogeneous IoT Sensor Environments](https://arxiv.org/abs/2604.21369)

**<font color=#1a73e8>作者：</font>** Tatsuhito Hasegawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) in Internet of Things (IoT) environments must cope with heterogeneous sensor settings that vary across datasets, devices, body locations, sensing modalities, and channel compositions. This heterogeneity makes conventional channel-fixed models difficult to reuse across sensing environments because their input representations are tightly coupled to predefined channel structures. To address this problem, we investigate strict channel-free HAR, in which a single shared model performs inference without assuming a fixed number, order, or semantic arrangement of input channels, and without relying on sensor-specific input layers or dataset-specific channel templates. We argue that fusion design is the central issue in this setting. Accordingly, we propose a channel-free HAR framework that combines channel-wise encoding with a shared encoder, metadata-conditioned late fusion via conditional batch normalization, and joint optimization of channel-level and fused predictions through a combination loss. The proposed model processes each channel independently to handle varying channel configurations, while sensor metadata such as body location, modality, and axis help recover structural information that channel-independent processing alone cannot retain. In addition, the joint loss encourages both the discriminability of individual channels and the consistency of the final fused prediction. Experiments on PAMAP2, together with robustness analysis on six HAR datasets, ablation studies, sensitivity analysis, efficiency evaluation, and cross-dataset transfer learning, demonstrate three main findings...

---


### 109. [MKJ at SemEval-2026 Task 9: A Comparative Study of Generalist, Specialist, and Ensemble Strategies for Multilingual Polarization](https://arxiv.org/abs/2604.21370)

**<font color=#1a73e8>作者：</font>** Maziar Kianimoghadam Jouneghani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a systematic study of multilingual polarization detection across 22 languages for SemEval-2026 Task 9 (Subtask 1), contrasting multilingual generalists with language-specific specialists and hybrid ensembles. While a standard generalist like XLM-RoBERTa suffices when its tokenizer aligns with the target text, it may struggle with distinct scripts (e.g., Khmer, Odia) where monolingual specialists yield significant gains. Rather than enforcing a single universal architecture, we adopt a language-adaptive framework that switches between multilingual generalists, language-specific specialists, and hybrid ensembles based on development performance. Additionally, cross-lingual augmentation via NLLB-200 yielded mixed results, often underperforming native architecture selection and degrading morphologically rich tracks. Our final system achieves an overall macro-averaged F1 score of 0.796 and an average accuracy of 0.826 across all 22 tracks. Code and final test predictions are publicly available at: this https URL.

---


### 110. [VLAA-GUI: Knowing When to Stop, Recover, and Search, A Modular Framework for GUI Automation](https://arxiv.org/abs/2604.21375)

**<font color=#1a73e8>作者：</font>** Qijun Han, Haoqin Tu, Zijun Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous GUI agents face two fundamental challenges: early stopping, where agents prematurely declare success without verifiable evidence, and repetitive loops, where agents cycle through the same failing actions without recovery. We present VLAA-GUI, a modular GUI agentic framework built around three integrated components that guide the system on when to Stop, Recover, and Search. First, a mandatory Completeness Verifier enforces UI-observable success criteria and verification at every finish step -- with an agent-level verifier that cross-examines completion claims with decision rules, rejecting those lacking direct visual evidence. Second, a mandatory Loop Breaker provides multi-tier filtering: switching interaction mode after repeated failures, forcing strategy changes after persistent screen-state recurrence, and binding reflection signals to strategy shifts. Third, an on-demand Search Agent searches online for unfamiliar workflows by directly querying a capable LLM with search ability, returning results as plain text. We additionally integrate a Coding Agent for code-intensive actions and a Grounding Agent for precise action grounding, both invoked on demand when required. We evaluate VLAA-GUI across five top-tier backbones, including Opus 4.5, 4.6 and Gemini 3.1 Pro, on two benchmarks with Linux and Windows tasks, achieving top performance on both (77.5% on OSWorld and 61.0% on WindowsAgentArena). Notably, three of the five backbones surpass human performance (72.4%) on OSWorld in a single pass. Ablation studies show that all three proposed components consistently improve a strong backbone, while a weaker backbone benefits more from these tools when the step budget is sufficient. Further analysis also shows that the Loop Breaker nearly halves wasted steps for loop-prone models.

---


### 111. [EdgeFormer: local patch-based edge detection transformer on point clouds](https://arxiv.org/abs/2604.21387)

**<font color=#1a73e8>作者：</font>** Yifei Xie, Zhikun Tu, Tong Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge points on 3D point clouds can clearly convey 3D geometry and surface characteristics, therefore, edge detection is widely used in many vision applications with high industrial and commercial demands. However, the fine-grained edge features are difficult to detect effectively as they are generally densely distributed or exhibit small-scale surface gradients. To address this issue, we present a learning-based edge detection network, named EdgeFormer, which mainly consists of two stages. Based on the observation that spatially neighboring points tend to exhibit high correlation, forming the local underlying surface, we convert the edge detection of the entire point cloud into a point classification based on local patches. Therefore, in the first stage, we construct local patch feature descriptors that describe the local neighborhood around each point. In the second stage, we classify each point by analyzing the local patch feature descriptors generated in the first stage. Due to the conversion of the point cloud into local patches, the proposed method can effectively extract the finer details. The experimental results show that our model demonstrates competitive performance compared to six baselines.

---


### 112. [Relocation of compact sets in $\mathbb{R}^n$ by diffeomorphisms and linear separability of datasets in $\mathbb{R}^n$](https://arxiv.org/abs/2604.21393)

**<font color=#1a73e8>作者：</font>** Xiao-Song Yang, Xuan Zhou, Qi Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relocation of compact sets in an $n$-dimensional manifold by self-diffeomorphism is of its own interest as well as significant potential applications to data classification in data science. This paper presents a theory for relocating a finite number of compact sets in $\mathbb{R}^n$ to be relocated to arbitrary target domains in $\mathbb{R}^n$ by diffeomorphisms of $\mathbb{R}^n$. Furthermore, we prove that for any such collection, there exists a differentiable embedding into $\mathbb{R}^{n+1}$ such that their images become linearly separable.
As applications of the established theory, we show that a finite number of compact datasets in $\mathbb{R}^n$ can be made linearly separable by width-$n$ deep neural networks (DNNs) with Leaky-ReLU, ELU, or SELU activation functions, under a mild condition. In addition, we show that any finite number of mutually disjoint compact datasets in $\mathbb{R}^n$ can be made linearly separable in $\mathbb{R}^{n+1}$ by a width-$(n+1)$ DNN.

---


### 113. [Provably Secure Steganography Based on List Decoding](https://arxiv.org/abs/2604.21394)

**<font color=#1a73e8>作者：</font>** Kaiyi Pang, Minhao Bai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Steganography embeds secret messages in seemingly innocuous carriers for covert communication under surveillance. Current Provably Secure Steganography (PSS) schemes based on language models can guarantee computational indistinguishability between the covertext and stegotext. However, achieving high embedding capacity remains a challenge for existing PSS. The inefficient entropy utilization renders them not well-suited for Large Language Models (LLMs), whose inherent low-entropy tendencies severely constrain feasible embedding capacity. To address this, we propose a provably secure steganography scheme with a theoretically proved high capacity. Our scheme is based on the concept of list decoding: it maintains a set of candidates that contain the correct secret message, instead of directly finding the correct message with more effort. This strategy fully utilizes the information content of the generated text, yielding higher capacity. To ensure the correctness of our scheme, we further introduce a suffix-matching mechanism to distinguish the correct secret message from the candidates. We provide theoretical proofs for both the security and correctness of our scheme, alongside a derivation of its theoretical capacity lower bound.
Our approach is plug-and-play, requiring only a direct replacement of the model's standard random sampling module. Experiments on three LLMs and seven PSS baselines demonstrate that our method achieves computational efficiency comparable to prior PSS schemes while delivering a substantial improvement in embedding capacity.

---


### 114. [Supervised Learning Has a Necessary Geometric Blind Spot: Theory, Consequences, and Minimal Repair](https://arxiv.org/abs/2604.21395)

**<font color=#1a73e8>作者：</font>** Vishal Rajput  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that empirical risk minimisation (ERM) imposes a necessary geometric constraint on learned representations: any encoder that minimises supervised loss must retain non-zero Jacobian sensitivity in directions that are label-correlated in training data but nuisance at test time. This is not a contingent failure of current methods; it is a mathematical consequence of the supervised objective itself. We call this the geometric blind spot of supervised learning (Theorem 1), and show it holds across proper scoring rules, architectures, and dataset sizes.
This single theorem unifies four lines of prior empirical work that were previously treated separately: non-robust predictive features, texture bias, corruption fragility, and the robustness-accuracy tradeoff. In this framing, adversarial vulnerability is one consequence of a broader structural fact about supervised learning geometry.
We introduce Trajectory Deviation Index (TDI), a diagnostic that measures the theorem's bounded quantity directly, and show why common alternatives miss the key failure mode. PGD adversarial training reaches Jacobian Frobenius 2.91 yet has the worst clean-input geometry (TDI 1.336), while PMH achieves TDI 0.904. TDI is the only metric that detects this dissociation because it measures isotropic path-length distortion -- the exact quantity Theorem 1 bounds.
Across seven vision tasks, BERT/SST-2, and ImageNet ViT-B/16 backbones used by CLIP, DINO, and SAM, the blind spot is measurable and repairable. It is present at foundation-model scale, worsens monotonically across language-model sizes (blind-spot ratio 0.860 to 0.765 to 0.742 from 66M to 340M), and is amplified by task-specific ERM fine-tuning (+54%), while PMH repairs it by 11x with one additional training term whose Gaussian form Proposition 5 proves is the unique perturbation law that uniformly penalises the encoder Jacobian.

---


### 115. [You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes](https://arxiv.org/abs/2604.21400)

**<font color=#1a73e8>作者：</font>** Jinrang Jia, Zhenjia Li, Yifeng Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has revolutionized neural rendering, yet existing methods remain predominantly research prototypes ill-suited for production-level deployment. We identify a critical "Industry-Academia Gap" hindering real-world application: unpredictable resource consumption from heuristic Gaussian growth, the "sparsity shield" of current benchmarks that rewards hallucination over physical fidelity, and severe multi-sensor data pollution. To bridge this gap, we propose YOGO (You Only Gaussian Once), a system-level framework that reformulates the stochastic growth process into a deterministic, budget-aware equilibrium. YOGO integrates a novel budget controller for hardware-constrained resource allocation and an availability-registration protocol for robust multi-sensor fusion. To push the boundaries of reconstruction fidelity, we introduce Immersion v1.0, the first ultra-dense indoor dataset specifically designed to break the "sparsity shield." By providing saturated viewpoint coverage, Immersion v1.0 forces algorithms to focus on extreme physical fidelity rather than viewpoint interpolation, and enables the community to focus on the upper limits of high-fidelity reconstruction. Extensive experiments demonstrate that YOGO achieves state-of-the-art visual quality while maintaining a strictly deterministic profile, establishing a new standard for production-grade 3DGS. To facilitate reproducibility, part scenes of Immersion v1.0 dataset and source code of YOGO has been publicly released. The project link is this https URL.

---


### 116. [Even More Guarantees for Variational Inference in the Presence of Symmetries](https://arxiv.org/abs/2604.21407)

**<font color=#1a73e8>作者：</font>** Lena Zellinger, Antonio Vergari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When approximating an intractable density via variational inference (VI) the variational family is typically chosen as a simple parametric family that very likely does not contain the target. This raises the question: Under which conditions can we recover characteristics of the target despite misspecification? In this work, we extend previous results on robust VI with location-scale families under target symmetries. We derive sufficient conditions guaranteeing exact recovery of the mean when using the forward Kullback-Leibler divergence and $\alpha$-divergences. We further show how and why optimization can fail to recover the target mean in the absence of our sufficient conditions, providing initial guidelines on the choice of the variational family and $\alpha$-value.

---


### 117. [A Green-Integral-Constrained Neural Solver with Stochastic Physics-Informed Regularization](https://arxiv.org/abs/2604.21411)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Abedi, David Pardo, Tariq Alkhalifah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard physics-informed neural networks (PINNs) struggle to simulate highly oscillatory Helmholtz solutions in heterogeneous media because pointwise minimization of second-order PDE residuals is computationally expensive, biased toward smooth solutions, and requires artificial absorbing boundary layers to restrict the solution. To overcome these challenges, we introduce a Green-Integral (GI) neural solver for the acoustic Helmholtz equation. It departs from the PDE-residual-based formulation by enforcing wave physics through an integral representation that imposes a nonlocal constraint. Oscillatory behavior and outgoing radiation are encoded directly through the integral kernel, eliminating second-order spatial derivatives and enforcing physical solutions without additional boundary layers. Theoretically, optimizing this GI loss via a neural network acts as a spectrally tuned preconditioned iteration, enabling convergence in heterogeneous media where the classical Born series diverges. By exploiting FFT-based convolution to accelerate the GI loss evaluation, our approach substantially reduces GPU memory usage and training time. However, this efficiency relies on a fixed regular grid, which can limit local resolution. To improve local accuracy in strong scattering regions, we also propose a hybrid GI+PDE loss, enforcing a lightweight Helmholtz residual at a small number of nonuniformly sampled collocation points. We evaluate our method on seismic benchmark models characterized by structural contrasts and subwavelength heterogeneity at frequencies up to 20Hz. GI-based training consistently outperforms PDE-based PINNs, reducing computational cost by over a factor of ten. In models with localized scattering, the hybrid loss yields the most accurate reconstructions, providing a stable, efficient, and physically grounded alternative.

---


### 118. [SemanticAgent: A Semantics-Aware Framework for Text-to-SQL Data Synthesis](https://arxiv.org/abs/2604.21414)

**<font color=#1a73e8>作者：</font>** Qiang Gao, Zhenping Li, Anqi Zhuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing text-to-SQL synthesis pipelines still conflate executability with semantic validity: syntactic checks and execution-based validation can retain queries that execute successfully while violating database semantics. To address these limitations, we propose SemanticAgent, a semantic-aware synthesis framework. SemanticAgent organizes synthesis around three specialized modules: an analyzer, a synthesizer, and a verifier. Through a three-stage protocol of semantic analysis, stepwise synthesis, and diagnostic refinement, SemanticAgent transforms execution-based validation alone into a traceable reasoning process. Our framework generates synthetic data that consistently outperforms prior synthesis methods under semantic-quality evaluation, leading to stronger downstream fine-tuning performance, especially on semantically demanding benchmarks.

---


### 119. [CSC: Turning the Adversary's Poison against Itself](https://arxiv.org/abs/2604.21416)

**<font color=#1a73e8>作者：</font>** Yuchen Shi, Xin Guo, Huajie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Poisoning-based backdoor attacks pose significant threats to deep neural networks by embedding triggers in training data, causing models to misclassify triggered inputs as adversary-specified labels while maintaining performance on clean data. Existing poison restraint-based defenses often suffer from inadequate detection against specific attack variants and compromise model utility through unlearning methods that lead to accuracy degradation. This paper conducts a comprehensive analysis of backdoor attack dynamics during model training, revealing that poisoned samples form isolated clusters in latent space early on, with triggers acting as dominant features distinct from benign ones. Leveraging these insights, we propose Cluster Segregation Concealment (CSC), a novel poison suppression defense. CSC first trains a deep neural network via standard supervised learning while segregating poisoned samples through feature extraction from early epochs, DBSCAN clustering, and identification of anomalous clusters based on class diversity and density metrics. In the concealment stage, identified poisoned samples are relabeled to a virtual class, and the model's classifier is fine-tuned using cross-entropy loss to replace the backdoor association with a benign virtual linkage, preserving overall accuracy. CSC was evaluated on four benchmark datasets against twelve poisoning-based attacks, CSC outperforms nine state-of-the-art defenses by reducing average attack success rates to near zero with minimal clean accuracy loss. Contributions include robust backdoor patterns identification, an effective concealment mechanism, and superior empirical validation, advancing trustworthy artificial intelligence.

---


### 120. [FairQE: Multi-Agent Framework for Mitigating Gender Bias in Translation Quality Estimation](https://arxiv.org/abs/2604.21420)

**<font color=#1a73e8>作者：</font>** Jinhee Jang, Juhwan Choi, Dongjin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Quality Estimation (QE) aims to assess machine translation quality without reference translations, but recent studies have shown that existing QE models exhibit systematic gender bias. In particular, they tend to favor masculine realizations in gender-ambiguous contexts and may assign higher scores to gender-misaligned translations even when gender is explicitly specified. To address these issues, we propose FairQE, a multi-agent-based, fairness-aware QE framework that mitigates gender bias in both gender-ambiguous and gender-explicit scenarios. FairQE detects gender cues, generates gender-flipped translation variants, and combines conventional QE scores with LLM-based bias-mitigating reasoning through a dynamic bias-aware aggregation mechanism. This design preserves the strengths of existing QE models while calibrating their gender-related biases in a plug-and-play manner. Extensive experiments across multiple gender bias evaluation settings demonstrate that FairQE consistently improves gender fairness over strong QE baselines. Moreover, under MQM-based meta-evaluation following the WMT 2023 Metrics Shared Task, FairQE achieves competitive or improved general QE performance. These results show that gender bias in QE can be effectively mitigated without sacrificing evaluation accuracy, enabling fairer and more reliable translation evaluation.

---


### 121. [Differentially Private De-identification of Dutch Clinical Notes: A Comparative Evaluation](https://arxiv.org/abs/2604.21421)

**<font color=#1a73e8>作者：</font>** Michele Miranda, Xinlan Yan, Nishant Mishra 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protecting patient privacy in clinical narratives is essential for enabling secondary use of healthcare data under regulations such as GDPR and HIPAA. While manual de-identification remains the gold standard, it is costly and slow, motivating the need for automated methods that combine privacy guarantees with high utility. Most automated text de-identification pipelines employed named entity recognition (NER) to identify protected entities for redaction. Although methods based on differential privacy (DP) provide formal privacy guarantees, more recently also large language models (LLMs) are increasingly used for text de-identification in the clinical domain. In this work, we present the first comparative study of DP, NER, and LLMs for Dutch clinical text de-identification. We investigate these methods separately as well as hybrid strategies that apply NER or LLM preprocessing prior to DP, and assess performance in terms of privacy leakage and extrinsic evaluation (entity and relation classification). We show that DP mechanisms alone degrade utility substantially, but combining them with linguistic preprocessing, especially LLM-based redaction, significantly improves the privacy-utility trade-off.

---


### 122. [Pre-process for segmentation task with nonlinear diffusion filters](https://arxiv.org/abs/2604.21422)

**<font color=#1a73e8>作者：</font>** Javier Sanguino, Carlos Platero, Olga Velasco  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper deals with the case of using nonlinear diffusion filters to obtain piecewise constant images as a previous process for segmentation techniques.
We first show an intrinsic formulation for the nonlinear diffusion equation to provide some design conditions on the diffusion filters. According to this theoretical framework, we propose a new family of diffusivities; they are obtained from nonlinear diffusion techniques and are related with backward diffusion. Their goal is to split the image in closed contours with a homogenized grey intensity inside and with no blurred edges.
We also prove that our filters satisfy the well-posedness semi-discrete and full discrete scale-space requirements. This shows that by using semi-implicit schemes, a forward nonlinear diffusion equation is solved, instead of a backward nonlinear diffusion equation, connecting with an edge-preserving process. Under the conditions established for the diffusivity and using a stopping criterion for the diffusion time, we get piecewise constant images with a low computational effort.
Finally, we test our filter with real images and we illustrate the effects of our diffusivity function as a method to get piecewise constant images.
The code is available at this https URL.

---


### 123. [Brief chatbot interactions produce lasting changes in human moral values](https://arxiv.org/abs/2604.21430)

**<font color=#1a73e8>作者：</font>** Yue Teng, Qianer Zhong, Kim Mai Tich Nguyen Thordsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Moral judgements form the foundation of human social behavior and societal systems. While Artificial Intelligence chatbots increasingly serve as personal advisors, their influence on moral judgments remains largely unexplored. Here, we examined whether directive AI conversations shift moral evaluations using a within-subject naturalistic paradigm. Fifty-three participants rated moral scenarios, then discussed four with a chatbot prompted to shift moral judgments and four with a control agent. The brief conversations induced significant directional shifts in moral judgments, accepting stricter standards as well as advocating greater leniency (ps < 0.05; Cohen's d = 0.735-1.576), with increasing strengths of this effect during a two-week follow-up (Cohen's d = 1.038-2.069). Critically, the control condition produced no changes, and the effects did not extend to punishment while participants remained unaware of the persuasive intent, and both agents were rated equally likable and convincing, suggesting a vulnerability to undetected and lasting manipulation of foundational moral values.

---


### 124. [UHR-DETR: Efficient End-to-End Small Object Detection for Ultra-High-Resolution Remote Sensing Imagery](https://arxiv.org/abs/2604.21435)

**<font color=#1a73e8>作者：</font>** Jingfang Li, Haoran Zhu, Wen Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-High-Resolution (UHR) imagery has become essential for modern remote sensing, offering unprecedented spatial coverage. However, detecting small objects in such vast scenes presents a critical dilemma: retaining the original resolution for small objects causes prohibitive memory bottlenecks. Conversely, conventional compromises like image downsampling or patch cropping either erase small objects or destroy context. To break this dilemma, we propose UHR-DETR, an efficient end-to-end transformer-based detector designed for UHR imagery. First, we introduce a Coverage-Maximizing Sparse Encoder that dynamically allocates finite computational resources to informative high-resolution regions, ensuring maximum object coverage with minimal spatial redundancy. Second, we design a Global-Local Decoupled Decoder. By integrating macroscopic scene awareness with microscopic object details, this module resolves semantic ambiguities and prevents scene fragmentation. Extensive experiments on the UHR imagery datasets (e.g., STAR and SODA-A) demonstrate the superiority of UHR-DETR under strict hardware constraints (e.g., a single 24GB RTX 3090). It achieves a 2.8\% mAP improvement while delivering a 10$\times$ inference speedup compared to standard sliding-window baselines on the STAR dataset. Our codes and models will be available at this https URL.

---


### 125. [A Stackelberg Model for Hybridization in Cryptography](https://arxiv.org/abs/2604.21436)

**<font color=#1a73e8>作者：</font>** Willie Kouam, Stefan Rass, Zahra Seyedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Similar to a strategic interaction between rational and intelligent agents, cryptography problems can be examined through the prism of game theory. In this setting, the agent aiming to protect a message is called the defender, while the one attempting to decrypt it, generally for malicious purposes, is the attacker. To strengthen security in cryptography, various strategies have been developed, among which hybridization stands out as a key concept in modern cryptographic design. This strategy allows the defender to select among different encryption algorithms (classical, post-quantum, or hybrid) while carefully balancing security and operational costs. On the other side, the attacker, limited by available resources, chooses cryptanalysis methods capable of breaching the selected algorithm. We model this interaction as a Stackelberg cryptographic hybridization problem under resource constraints. Here, the defender randomizes over encryption algorithms, and the attacker observes the choice before selecting suitable cryptanalysis methods. The attacker's decision is framed as a conditional optimization problem, which we refer to as the ``attacker subgame''. We then propose a dynamic programming approach for the attacker's subgame, while the defender's Stackelberg optimization is formulated as a linear program.

---


### 126. [2L-LSH: A Locality-Sensitive Hash Function-Based Method For Rapid Point Cloud Indexing](https://arxiv.org/abs/2604.21442)

**<font color=#1a73e8>作者：</font>** Shurui Wang, Yuhe Zhang, Ruizhe Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of 3D scanning technology has enabled the acquisition of massive point cloud models with diverse structures and large scales, thereby presenting significant challenges in point cloud processing. Fast neighboring points search is one of the most common problems, which is frequently used in model reconstruction, classification, retrieval and feature visualization. Hash function is well known for its high-speed and accurate performance in searching high-dimensional data, which is also the core of the proposed 2L-LSH. Specifically, the 2L-LSH algorithm adopts a two-step hash function strategy, in which the popular step divides the bounding box of the point cloud model and the second step constructs a generalized table-based data structure. The proposed 2L-LSH offers a highly efficient and accurate solution for fast neighboring points search in large-scale 3D point cloud models, making it a promising technique for various applications in the field. The proposed algorithm is compared with the well-known methods including Kd-tree and Octree; the obtained results demonstrated that the proposed method outperforms Kd-tree and Octree in terms of speed, i.e. the time consumption of kNN search can be 51.111% and 94.159% lower than Kd-tree and Octree, respectively. And the RN search time can be 54.519% and 41.840% lower than Kd-tree and Octree, respectively.

---


### 127. [HiCrew: Hierarchical Reasoning for Long-Form Video Understanding via Question-Aware Multi-Agent Collaboration](https://arxiv.org/abs/2604.21444)

**<font color=#1a73e8>作者：</font>** Yuehan Zhu, Jingqi Zhao, Jiawen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-form video understanding remains fundamentally challenged by pervasive spatiotemporal redundancy and intricate narrative dependencies that span extended temporal horizons. While recent structured representations compress visual information effectively, they frequently sacrifice temporal coherence, which is critical for causal reasoning. Meanwhile, existing multi-agent frameworks operate through rigid, pre-defined workflows that fail to adapt their reasoning strategies to question-specific demands. In this paper, we introduce HiCrew, a hierarchical multi-agent framework that addresses these limitations through three core contributions. First, we propose a Hybrid Tree structure that leverages shot boundary detection to preserve temporal topology while performing relevance-guided hierarchical clustering within semantically coherent segments. Second, we develop a Question-Aware Captioning mechanism that synthesizes intent-driven visual prompts to generate precision-oriented semantic descriptions. Third, we integrate a Planning Layer that dynamically orchestrates agent collaboration by adaptively selecting roles and execution paths based on question complexity. Extensive experiments on EgoSchema and NExT-QA validate the effectiveness of our approach, demonstrating strong performance across diverse question types with particularly pronounced gains in temporal and causal reasoning tasks that benefit from our hierarchical structure-preserving design.

---


### 128. [AI-Gram: When Visual Agents Interact in a Social Network](https://arxiv.org/abs/2604.21446)

**<font color=#1a73e8>作者：</font>** Andrew Shin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AI-Gram, a live platform enabling image-based interactions, to study social dynamics in a fully autonomous multi-agent visual network where all participants are LLM-driven agents. Using the platform, we conduct experiments on how agents communicate and adapt through visual media, and observe the spontaneous emergence of visual reply chains, indicating rich communicative structure. At the same time, agents exhibit aesthetic sovereignty resisting stylistic convergence toward social partners, anchoring under adversarial influence, and a decoupling between visual similarity and social ties. These results reveal a fundamental asymmetry in current agent architectures: strong expressive communication paired with a steadfast preservation of individual visual identity. We release AI-Gram as a publicly accessible, continuously evolving platform for studying social dynamics in Al-native multi-agent systems. this https URL

---


### 129. [VARestorer: One-Step VAR Distillation for Real-World Image Super-Resolution](https://arxiv.org/abs/2604.21450)

**<font color=#1a73e8>作者：</font>** Yixuan Zhu, Shilin Ma, Haolin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in visual autoregressive models (VAR) have demonstrated their effectiveness in image generation, highlighting their potential for real-world image super-resolution (Real-ISR). However, adapting VAR for ISR presents critical challenges. The next-scale prediction mechanism, constrained by causal attention, fails to fully exploit global low-quality (LQ) context, resulting in blurry and inconsistent high-quality (HQ) outputs. Additionally, error accumulation in the iterative prediction severely degrades coherence in ISR task. To address these issues, we propose VARestorer, a simple yet effective distillation framework that transforms a pre-trained text-to-image VAR model into a one-step ISR model. By leveraging distribution matching, our method eliminates the need for iterative refinement, significantly reducing error propagation and inference time. Furthermore, we introduce pyramid image conditioning with cross-scale attention, which enables bidirectional scale-wise interactions and fully utilizes the input image information while adapting to the autoregressive mechanism. This prevents later LQ tokens from being overlooked in the transformer. By fine-tuning only 1.2\% of the model parameters through parameter-efficient adapters, our method maintains the expressive power of the original VAR model while significantly enhancing efficiency. Extensive experiments show that VARestorer achieves state-of-the-art performance with 72.32 MUSIQ and 0.7669 CLIPIQA on DIV2K dataset, while accelerating inference by 10 times compared to conventional VAR inference.

---


### 130. [Instance-level Visual Active Tracking with Occlusion-Aware Planning](https://arxiv.org/abs/2604.21453)

**<font color=#1a73e8>作者：</font>** Haowei Sun, Kai Zhou, Hao Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Active Tracking (VAT) aims to control cameras to follow a target in 3D space, which is critical for applications like drone navigation and security surveillance. However, it faces two key bottlenecks in real-world deployment: confusion from visually similar distractors caused by insufficient instance-level discrimination and severe failure under occlusions due to the absence of active planning. To address these, we propose OA-VAT, a unified pipeline with three complementary modules. First, a training-free Instance-Aware Offline Prototype Initialization aggregates multi-view augmented features via DINOv3 to construct discriminative instance prototypes, mitigating distractor confusion. Second, an Online Prototype Enhancement Tracker enhances prototypes online and integrates a confidence-aware Kalman filter for stable tracking under appearance and motion changes. Third, an Occlusion-Aware Trajectory Planner, trained on our new Planning-20k dataset, uses conditional diffusion to generate obstacle-avoiding paths for occlusion recovery. Experiments demonstrate OA-VAT achieves 0.93 average SR on UnrealCV (+2.2% vs. SOTA TrackVLA), 90.8% average CAR on real-world datasets (+12.1% vs. SOTA GC-VAT), and 81.6% TSR on a DJI Tello drone. Running at 35 FPS on an RTX 3090, it delivers robust, real-time performance for practical deployment.

---


### 131. [The Privacy Guardian Agent: Towards Trustworthy AI Privacy Agents](https://arxiv.org/abs/2604.21455)

**<font color=#1a73e8>作者：</font>** Vincent Freiberger  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The current "notice and consent" paradigm is broken: consent dialogues are often manipulative, and users cannot realistically read or understand every privacy policy. While recent LLM-based tools empower users seeking active control, many with limited time or motivation prefer full automation. However, fully autonomous solutions risk hallucinations and opaque decisions, undermining trust. I propose a middle ground - a Privacy Guardian Agent that automates routine consent choices using user profiles and contextual awareness while recognizing uncertainty. It escalates unclear or high-risk cases to the user, maintaining a human-in-the-loop only when necessary. To ensure agency and transparency, the agent's reasoning on its autonomous decisions is reviewable, allowing for user recourse. For problematic cases, even with minimal consent, it alerts the user and suggests switching to an alternative site. This approach aims to reduce consent fatigue while preserving trust and meaningful user autonomy.

---


### 132. [Tempered Sequential Monte Carlo for Trajectory and Policy Optimization with Differentiable Dynamics](https://arxiv.org/abs/2604.21456)

**<font color=#1a73e8>作者：</font>** Heng Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a sampling-based framework for finite-horizon trajectory and policy optimization under differentiable dynamics by casting controller design as inference. Specifically, we minimize a KL-regularized expected trajectory cost, which yields an optimal "Boltzmann-tilted" distribution over controller parameters that concentrates on low-cost solutions as temperature decreases. To sample efficiently from this sharp, potentially multimodal target, we introduce tempered sequential Monte Carlo (TSMC): an annealing scheme that adaptively reweights and resamples particles along a tempering path from a prior to the target distribution, while using Hamiltonian Monte Carlo rejuvenation to maintain diversity and exploit exact gradients obtained by differentiating through trajectory rollouts. For policy optimization, we extend TSMC via (i) a deterministic empirical approximation of the initial-state distribution and (ii) an extended-space construction that treats rollout randomness as auxiliary variables. Experiments across trajectory- and policy-optimization benchmarks show that TSMC is broadly applicable and compares favorably to state-of-the-art baselines.

---


### 133. [Conditional anomaly detection with soft harmonic functions](https://arxiv.org/abs/2604.21462)

**<font color=#1a73e8>作者：</font>** Michal Valko, Branislav Kveton, Hamed Valizadegan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we consider the problem of conditional anomaly detection that aims to identify data instances with an unusual response or a class label. We develop a new non-parametric approach for conditional anomaly detection based on the soft harmonic solution, with which we estimate the confidence of the label to detect anomalous mislabeling. We further regularize the solution to avoid the detection of isolated examples and examples on the boundary of the distribution support. We demonstrate the efficacy of the proposed method on several synthetic and UCI ML datasets in detecting unusual labels when compared to several baseline approaches. We also evaluate the performance of our method on a real-world electronic health record dataset where we seek to identify unusual patient-management decisions.

---


### 134. [Dynamical Priors as a Training Objective in Reinforcement Learning](https://arxiv.org/abs/2604.21464)

**<font color=#1a73e8>作者：</font>** Sukesh Subaharan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard reinforcement learning (RL) optimizes policies for reward but imposes few constraints on how decisions evolve over time. As a result, policies may achieve high performance while exhibiting temporally incoherent behavior such as abrupt confidence shifts, oscillations, or degenerate inactivity. We introduce Dynamical Prior Reinforcement Learning (DP-RL), a training framework that augments policy gradient learning with an auxiliary loss derived from external state dynamics that implement evidence accumulation and hysteresis. Without modifying the reward, environment, or policy architecture, this prior shapes the temporal evolution of action probabilities during learning. Across three minimal environments, we show that dynamical priors systematically alter decision trajectories in task-dependent ways, promoting temporally structured behavior that cannot be explained by generic smoothing. These results demonstrate that training objectives alone can control the temporal geometry of decision-making in RL agents.

---


### 135. [ID-Eraser: Proactive Defense Against Face Swapping via Identity Perturbation](https://arxiv.org/abs/2604.21465)

**<font color=#1a73e8>作者：</font>** Junyan Luo, Peipeng Yu, Jianwei Fei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake technologies have rapidly advanced with modern generative AI, and face swapping in particular poses serious threats to privacy and digital security. Existing proactive defenses mostly rely on pixel-level perturbations, which are ineffective against contemporary swapping models that extract robust high-level identity embeddings. We propose ID-Eraser, a feature-space proactive defense that removes identifiable facial information to prevent malicious face swapping. By injecting learnable perturbations into identity embeddings and reconstructing natural-looking protection images through a Face Revive Generator (FRG), ID-Eraser produces visually realistic results for humans while rendering the protected identities unusable for Deepfake models. Experiments show that ID-Eraser substantially disrupts identity recognition across diverse face recognition and swapping systems under strict black-box settings, achieving the lowest Top-1 accuracy (0.30) with the best FID (1.64) and LPIPS (0.020). Compared with swaps generated from clean inputs, the identity similarity of protected swaps drops sharply to an average of 0.504 across five representative face swapping models. ID-Eraser further demonstrates strong cross-dataset generalization, robustness to common distortions, and practical effectiveness on commercial APIs, reducing Tencent API similarity from 0.76 to 0.36.

---


### 136. [Cross-Domain Data Selection and Augmentation for Automatic Compliance Detection](https://arxiv.org/abs/2604.21469)

**<font color=#1a73e8>作者：</font>** Fariz Ikhwantri, Dusica Marijan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automating the detection of regulatory compliance remains a challenging task due to the complexity and variability of legal texts. Models trained on one regulation often fail to generalise to others. This limitation underscores the need for principled methods to improve cross-domain transfer. We study data selection as a strategy to mitigate negative transfer in compliance detection framed as a natural language inference (NLI) task. Specifically, we evaluate four approaches for selecting augmentation data from a larger source domain: random sampling, Moore-Lewis's cross-entropy difference, importance weighting, and embedding-based retrieval. We systematically vary the proportion of selected data to analyse its effect on cross-domain adaptation. Our findings demonstrate that targeted data selection substantially reduces negative transfer, offering a practical path toward scalable and reliable compliance automation across heterogeneous regulations.

---


### 137. [Drug Synergy Prediction via Residual Graph Isomorphism Networks and Attention Mechanisms](https://arxiv.org/abs/2604.21473)

**<font color=#1a73e8>作者：</font>** Jiyan Song, Wenyang Wang, Chengcheng Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the treatment of complex diseases, treatment regimens using a single drug often yield limited efficacy and can lead to drug resistance. In contrast, combination drug therapies can significantly improve therapeutic outcomes through synergistic effects. However, experimentally validating all possible drug combinations is prohibitively expensive, underscoring the critical need for efficient computational prediction methods. Although existing approaches based on deep learning and graph neural networks (GNNs) have made considerable progress, challenges remain in reducing structural bias, improving generalization capability, and enhancing model interpretability. To address these limitations, this paper proposes a collaborative prediction graph neural network that integrates molecular structural features and cell-line genomic profiles with drug-drug interactions to enhance the prediction of synergistic effects. We introduce a novel model named the Residual Graph Isomorphism Network integrated with an Attention mechanism (ResGIN-Att). The model first extracts multi scale topological features of drug molecules using a residual graph isomorphism network, where residual connections help mitigate over-smoothing in deep layers. Subsequently, an adaptive Long Short-Term Memory (LSTM) module fuses structural information from local to global scales. Finally, a cross-attention module is designed to explicitly model drug-drug interactions and identify key chemical substructures. Extensive experiments on five public benchmark datasets demonstrate that ResGIN-Att achieves competitive performance, comparing favorably against key baseline methods while exhibiting promising generalization capability and robustness.

---


### 138. [MCP Pitfall Lab: Exposing Developer Pitfalls in MCP Tool Server Security under Multi-Vector Attacks](https://arxiv.org/abs/2604.21477)

**<font color=#1a73e8>作者：</font>** Run Hao, Zhuoran Tan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model Context Protocol (MCP) is increasingly adopted for tool-integrated LLM agents, but its multi-layer design and third-party server ecosystem expand risks across tool metadata, untrusted outputs, cross-tool flows, multimodal inputs, and supply-chain vectors. Existing MCP benchmarks largely measure robustness to malicious inputs but offer limited remediation guidance. We present MCP Pitfall Lab, a protocol-aware security testing framework that operationalizes developer pitfalls as reproducible scenarios and validates outcomes with MCP traces and objective validators (rather than agent self-report). We instantiate three workflow challenges (email, document, crypto) with six server variants (baseline and hardened) and model three attack families: tool-metadata poisoning, puppet servers, and multimodal image-to-tool chains, in a unified, trace-grounded evaluation. In Tier-1 static analysis over six variants (36 binary labels), our analyzer achieves F1 = 1.0 on four statically checkable pitfall classes (P1, P2, P5, P6) and flags cross-tool forwarding and image-to-tool leakage (P3, P4) as trace/dataflow-dependent. Applying recommended hardening eliminates all Tier-1 findings (29 to 0) and reduces the framework risk score (10.0 to 0.0) at a mean cost of 27 lines of code (LOC). Finally, in a preliminary 19-run corpus from the email system challenge (tool poisoning and puppet attacks), agent narratives diverge from trace evidence in 63.2% of runs and 100% of sink-action runs, motivating trace-based auditing and regression testing. Overall, Pitfall Lab enables practical, end-to-end assessment and hardening of MCP tool servers under realistic multi-vector conditions.

---


### 139. [Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](https://arxiv.org/abs/2604.21481)

**<font color=#1a73e8>作者：</font>** Srija Anand, Ashwin Sankar, Ishvinder Sethi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.

---


### 140. [Benchmarking the Utility of Privacy-Preserving Cox Regression Under Data-Driven Clipping Bounds: A Multi-Dataset Simulation Study](https://arxiv.org/abs/2604.21491)

**<font color=#1a73e8>作者：</font>** Keita Fukuyama, Yukiko Mori, Tomohiro Kuroda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) is a mathematical framework that guarantees individual privacy; however, systematic evaluation of its impact on statistical utility in survival analyses remains limited. In this study, we systematically evaluated the impact of DP mechanisms (Laplace mechanism and Randomized Response) with data-driven clipping bounds on the Cox proportional hazards model, using 5 clinical datasets ($n = 168$--$6{,}524$), 15 levels of $\varepsilon$ (0.1--1000), and $B = 1{,}000$ Monte Carlo iterations. The data-driven clipping bounds used here are observed min/max and therefore do not provide formal $\varepsilon$-DP guarantees; the results represent an optimistic lower bound on utility degradation under formal DP. We compared three types of input perturbations (covariates only, all inputs, and the discrete-time model) with output perturbations (dfbeta-based sensitivity), using loss of significance rate (LSR), C-index, and coefficient bias as metrics. At standard DP levels ($\varepsilon \leq 1$), approximately 90% (90--94%) of the significant covariates lost significance, even in the largest dataset ($n = 6{,}524$), and the predictive performance approached random levels (test C-index $\approx 0.5$) under many conditions. Among the input perturbation approaches, perturbing only covariates preserved the risk-set structure and achieved the best recovery, whereas output perturbation (dfbeta-based sensitivity) maintained near-baseline performance at $\varepsilon \geq 5$. At $n \approx 3{,}000$, the significance recovered rapidly at $\varepsilon = 3$--10; however, in practice, $\varepsilon \geq 10$ (for predictive performance) to $\varepsilon \geq 30$--60 (for significance preservation) is required. In the moderate-to-high $\varepsilon$ range, false-positive rates increased for variables whose baseline $p$-values were near the significance threshold.

---


### 141. [How English Print Media Frames Human-Elephant Conflicts in India](https://arxiv.org/abs/2604.21496)

**<font color=#1a73e8>作者：</font>** Bonala Sai Punith, Salveru Jayati, Garima Shakya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human-elephant conflict (HEC) is rising across India as habitat loss and expanding human settlements force elephants into closer contact with people. While the ecological drivers of conflict are well-studied, how the news media portrays them remains largely unexplored. This work presents the first large-scale computational analysis of media framing of HEC in India, examining 1,968 full-length news articles consisting of 28,986 sentences, from a major English-language outlet published between January 2022 and September 2025. Using a multi-model sentiment framework that combines long-context transformers, large language models, and a domain-specific Negative Elephant Portrayal Lexicon, we quantify sentiment, extract rationale sentences, and identify linguistic patterns that contribute to negative portrayals of elephants. Our findings reveal a dominance of fear-inducing and aggression-related language. Since the media framing can shape public attitudes toward wildlife and conservation policy, such narratives risk reinforcing public hostility and undermining coexistence efforts. By providing a transparent, scalable methodology and releasing all resources through an anonymized repository, this study highlights how Web-scale text analysis can support responsible wildlife reporting and promote socially beneficial media practices.

---


### 142. [VFM$^{4}$SDG: Unveiling the Power of VFMs for Single-Domain Generalized Object Detection](https://arxiv.org/abs/2604.21502)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Ruize Han, Ningnan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world scenarios, continual changes in weather, illumination, and imaging conditions cause significant domain shifts, leading detectors trained on a single source domain to degrade severely in unseen environments. Existing single-domain generalized object detection (SDGOD) methods mainly rely on data augmentation or domain-invariant representation learning, but pay limited attention to detector mechanisms, leaving clear limitations under complex domain shifts. Through analytical experiments, we find that performance degradation is dominated by increasing missed detections, which fundamentally arises from reduced cross-domain stability of the detector: object-background and inter-instance relations become less stable in the encoding stage, while semantic-spatial alignment of query representations also becomes harder to maintain in the decoding stage. To this end, we propose VFM$^{4}$SDG, a dual-prior learning framework for SDGOD, which introduces a frozen vision foundation model (VFM) as a transferable cross-domain stability prior into detector representation learning and query modeling. In the encoding stage, we propose Cross-domain Stable Relational Prior Distillation to enhance the robustness of object-background and inter-instance relational modeling. In the decoding stage, we propose Semantic-Contextual Prior-based Query Enhancement, which injects category-level semantic prototypes and global visual context into queries to improve their semantic recognition and spatial localization stability in unseen domains. Extensive experiments show that the proposed method consistently outperforms existing SOTA methods on standard SDGOD benchmarks and two mainstream DETR-based detectors, demonstrating its effectiveness, robustness, and generality.

---


### 143. [BioMiner: A Multi-modal System for Automated Mining of Protein-Ligand Bioactivity Data from Literature](https://arxiv.org/abs/2604.21508)

**<font color=#1a73e8>作者：</font>** Jiaxian Yan, Jintao Zhu, Yuhang Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein-ligand bioactivity data published in the literature are essential for drug discovery, yet manual curation struggles to keep pace with rapidly growing literature. Automated bioactivity extraction remains challenging because it requires not only interpreting biochemical semantics distributed across text, tables, and figures, but also reconstructing chemically exact ligand structures (e.g., Markush structures). To address this bottleneck, we introduce BioMiner, a multi-modal extraction framework that explicitly separates bioactivity semantic interpretation from ligand structure construction. Within BioMiner, bioactivity semantics are inferred through direct reasoning, while chemical structures are resolved via a chemical-structure-grounded visual semantic reasoning paradigm, in which multi-modal large language models operate on chemically grounded visual representations to infer inter-structure relationships, and exact molecular construction is delegated to domain chemistry tools. For rigorous evaluation and method development, we further establish BioVista, a comprehensive benchmark comprising 16,457 bioactivity entries curated from 500 publications. BioMiner validates its extraction ability and provides a quantitative baseline, achieving an F1 score of 0.32 for bioactivity triplets. BioMiner's practical utility is demonstrated via three applications: (1) extracting 82,262 data from 11,683 papers to build a pre-training database that improves downstream models performance by 3.9%; (2) enabling a human-in-the-loop workflow that doubles the number of high-quality NLRP3 bioactivity data, helping 38.6% improvement over 28 QSAR models and identification of 16 hit candidates with novel scaffolds; and (3) accelerating protein-ligand complex bioactivity annotation, achieving a 5.59-fold speed increase and 5.75% accuracy improvement over manual workflows in PoseBusters dataset.

---


### 144. [Satisfying Rationality Postulates of Structured Argumentation Through Deductive Support -- Technical Report](https://arxiv.org/abs/2604.21515)

**<font color=#1a73e8>作者：</font>** Marcos Cramer, Tom Friese  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> ASPIC-style structured argumentation frameworks provide a formal basis for reasoning in artificial intelligence by combining internal argument structure with abstract argumentation semantics. A key challenge in these frameworks is ensuring compliance with five critical rationality postulates: closure, direct consistency, indirect consistency, non-interference, and crash-resistance. Recent approaches, including ASPIC$^{\ominus}$ and Deductive ASPIC$-$, have made significant progress but fall short of meeting all postulates simultaneously under a credulous semantics (e.g. preferred) in the presence of undercuts. This paper introduces Deductive ASPIC$^{\ominus}$, a novel framework that integrates gen-rebuttals from ASPIC$^{\ominus}$ with the Joint Support Bipolar Argumentation Frameworks (JSBAFs) of Deductive ASPIC$-$, incorporating preferences. We show that Deductive ASPIC$^{\ominus}$ satisfies all five rationality postulates under a version of preferred semantics. This work opens new avenues for further research on robust and logically sound structured argumentation systems.

---


### 145. [A temporal deep learning framework for calibration of low-cost air quality sensors](https://arxiv.org/abs/2604.21527)

**<font color=#1a73e8>作者：</font>** Arindam Sengupta, Tony Bush, Ben Marner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-cost air quality sensors (LCS) provide a practical alternative to expensive regulatory-grade instruments, making dense urban monitoring networks possible. Yet their adoption is limited by calibration challenges, including sensor drift, environmental cross-sensitivity, and variability in performance from device to device. This work presents a deep learning framework for calibrating LCS measurements of PM$_{2.5}$, PM$_{10}$, and NO$_2$ using a Long Short-Term Memory (LSTM) network, trained on co-located reference data from the OxAria network in Oxford, UK. Unlike the Random Forest (RF) baseline, which treats each observation independently, the proposed approach captures temporal dependencies and delayed environmental effects through sequence-based learning, achieving higher $R^2$ values across training, validation, and test sets for all three pollutants. A feature set is constructed combining time-lagged parameters, harmonic encodings, and interaction terms to improve generalization on unseen temporal windows. Validation of unseen calibrated values against the Equivalence Spreadsheet Tool 3.1 demonstrates regulatory compliance with expanded uncertainties of 22.11% for NO$_2$, 12.42% for PM$_{10}$, and 9.1% for PM$_{2.5}$.

---


### 146. [Architectures for Robust Self-Organizing Energy Systems under Information and Control Constraints](https://arxiv.org/abs/2604.21529)

**<font color=#1a73e8>作者：</font>** Emilie Frost, Astrid Nieße  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Applying the concept of controlled self-organization in agent-based Cyber-Physical Energy Systems (CPES) is a promising approach to ensure system robustness. By introducing an observer/controller architecture to the system, this concept allows for self-organization while still enabling intervention when disturbances occur. Thus, it is possible to respond to effects of cyber attacks, a major threat to current energy systems. However, when implementing an observer to monitor the system and a controller to execute actions for controlled self-organization in CPES, it is essential to take into account restrictions on information and actions resulting from the privacy of local distributed energy resources, regulatory constraints, and data exchange requirements. For this reason, this paper presents architecture variants for the observer and controller that take into account restrictions on access to information and limited actions. In addition, it evaluates possible controller actions in various architectures. The results underscore the importance of considering observer/controller architectures when designing agent-based systems to ensure their robustness for real-world applications.

---


### 147. [UKP_Psycontrol at SemEval-2026 Task 2: Modeling Valence and Arousal Dynamics from Text](https://arxiv.org/abs/2604.21534)

**<font color=#1a73e8>作者：</font>** Darya Hryhoryeva, Amaia Zurinaga, Hamidreza Jamalabadi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents our system developed for SemEval-2026 Task 2. The task requires modeling both current affect and short-term affective change in chronologically ordered user-generated texts. We explore three complementary approaches: (1) LLM prompting under user-aware and user-agnostic settings, (2) a pairwise Maximum Entropy (MaxEnt) model with Ising-style interactions for structured transition modeling, and (3) a lightweight neural regression model incorporating recent affective trajectories and trainable user embeddings. Our findings indicate that LLMs effectively capture static affective signals from text, whereas short-term affective variation in this dataset is more strongly explained by recent numeric state trajectories than by textual semantics. Our system ranked first among participating teams in both Subtask 1 and Subtask 2A based on the official evaluation metric.

---


### 148. [The CriticalSet problem: Identifying Critical Contributors in Bipartite Dependency Networks](https://arxiv.org/abs/2604.21537)

**<font color=#1a73e8>作者：</font>** Sebastiano A. Piccolo, Andrea Tagarelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying critical nodes in complex networks is a fundamental task in graph mining. Yet, methods addressing an all-or-nothing coverage mechanics in a bipartite dependency network, a graph with two types of nodes where edges represent dependency relationships across the two groups only, remain largely unexplored. We formalize the CriticalSet problem: given an arbitrary bipartite graph modeling dependencies of items on contributors, identify the set of k contributors whose removal isolates the largest number of items. We prove that this problem is NP-hard and requires maximizing a supermodular set function, for which standard forward greedy algorithms provide no approximation guarantees. Consequently, we model CriticalSet as a coalitional game, deriving a closed-form centrality, ShapleyCov, based on the Shapley value. This measure can be interpreted as the expected number of items isolated by a contributor's departure. Leveraging these insights, we propose MinCov, a linear-time iterative peeling algorithm that explicitly accounts for connection redundancy, prioritizing contributors who uniquely support many items. Extensive experiments on synthetic and large-scale real datasets, including a Wikipedia graph with over 250 million edges, reveal that MinCov and ShapleyCov significantly outperform traditional baselines. Notably, MinCov achieves near-optimal performance, within 0.02 AUC of a Stochastic Hill Climbing metaheuristic, while remaining several orders of magnitude faster.

---


### 149. [Component-Based Out-of-Distribution Detection](https://arxiv.org/abs/2604.21546)

**<font color=#1a73e8>作者：</font>** Wenrui Liu, Hong Chang, Ruibing Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-Distribution (OOD) detection requires sensitivity to subtle shifts without overreacting to natural In-Distribution (ID) diversity. However, from the viewpoint of detection granularity, global representation inevitably suppress local OOD cues, while patch-based methods are unstable due to entangled spurious-correlation and noise. And neither them is effective in detecting compositional OODs composed of valid ID components. Inspired by recognition-by-components theory, we present a training-free Component-Based OOD Detection (CoOD) framework that addresses the existing limitations by decomposing inputs into functional components. To instantiate CoOD, we derive Component Shift Score (CSS) to detect local appearance shifts, and Compositional Consistency Score (CCS) to identify cross-component compositional inconsistencies. Empirically, CoOD achieves consistent improvements on both coarse- and fine-grained OOD detection.

---


### 150. [Engaged AI Governance: Addressing the Last Mile Challenge Through Internal Expert Collaboration](https://arxiv.org/abs/2604.21554)

**<font color=#1a73e8>作者：</font>** Simon Jarvers, Orestis Papakyriakopoulos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under the EU AI Act, translating AI governance requirements into software development practice remains challenging. While AI governance frameworks exist at industry and organizational levels, empirical evidence of team-level implementation is scarce. We address this "Last Mile" Challenge through insider action research embedded within an AI startup. We present a legal-text-to-action pipeline that translates EU AI Act requirements into actionable strategies through internal expert collaboration by extracting requirements from legal text, engaging practitioners in assessment and ideation, and prioritizing implementation through collective evaluation. Our analysis reveals three patterns in how practitioners perceive regulatory requirements: convergence (compliance aligns with development priorities), existing practice (current work already satisfies requirements), and disconnection (requirements perceived as administrative overhead). Based on these patterns, we discuss when governance might be treated genuinely or performatively. Practitioners prioritize requirements that serve end-users or their own development needs, but view verification-oriented requirements as box-ticking exercises. This distinction suggests a translation challenge: regulatory requirements risk superficial treatment unless practitioners understand how compliance serves system quality and user protection. Expert collaboration offers a practical mechanism for transforming governance from external imposition to shared ownership and making previously invisible governance work visible and collective.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-231](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
