# 📦 其他研究 | 2026年04月22日

> 本类共 **535** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-535](./part-11.md)

---

### 451. [Towards Symmetry-sensitive Pose Estimation: A Rotation Representation for Symmetric Object Classes](https://arxiv.org/abs/2604.18208)

**<font color=#1a73e8>作者：</font>** Andreas Kriegler, Csaba Beleznai, Margrit Gelautz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Symmetric objects are common in daily life and industry, yet their inherent orientation ambiguities that impede the training of deep learning networks for pose estimation are rarely discussed in the literature. To cope with these ambiguities, existing solutions typically require the design of specific loss functions and network architectures or resort to symmetry-invariant evaluation metrics. In contrast, we focus on the numeric representation of the rotation itself, modifying trigonometric identities with the degrees of symmetry derived from the objects' shapes. We use our representation, SARR, to obtain canonic (symmetry-resolved) poses for the symmetric objects in two popular 6D pose estimation datasets, T-LESS and ITODD, where SARR is unique and continuous w.r.t. the visual appearance. This allows us to use a standard CNN for 3D orientation estimation whose performance is evaluated with the symmetry-sensitive cosine distance $\text{AR}_{\text{C}}$. Our networks outperform the state of the art using $\text{AR}_{\text{C}}$ and achieve satisfactory performance when using conventional symmetry-invariant measures. Our method does not require any 3D models but only depth, or, as part of an additional experiment, texture-less RGB/grayscale images as input. We also show that networks trained on SARR outperform the same networks trained on rotation matrices, Euler angles, quaternions, standard trigonometrics or the recently popular 6d representation -- even in inference scenarios where no prior knowledge of the objects' symmetry properties is available. Code and a visualization toolkit are available at this https URL .

---


### 452. [TacticGen: Grounding Adaptable and Scalable Generation of Football Tactics](https://arxiv.org/abs/2604.18210)

**<font color=#1a73e8>作者：</font>** Sheng Xu, Guiliang Liu, Tarak Kharrat 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Success in association football relies on both individual skill and coordinated tactics. While recent advancements in spatio-temporal data and deep learning have enabled predictive analyses like trajectory forecasting, the development of tactical design remains limited. Bridging this gap is essential, as prediction reveals what is likely to occur, whereas tactic generation determines what should occur to achieve strategic objectives. In this work, we present TacticGen, a generative model for adaptable and scalable tactic generation. TacticGen formulates tactics as sequences of multi-agent movements and interactions conditioned on the game context. It employs a multi-agent diffusion transformer with agent-wise self-attention and context-aware cross-attention to capture cooperative and competitive dynamics among players and the ball. Trained with over 3.3 million events and 100 million tracking frames from top-tier leagues, TacticGen achieves state-of-the-art precision in predicting player trajectories. Building on it, TacticGen enables adaptable tactic generation tailored to diverse inference-time objectives through classifier guidance mechanism, specified via rules, natural language, or neural models. Its modeling performance is also inherently scalable. A case study with football experts confirms that TacticGen generates realistic, strategically valuable tactics, demonstrating its practical utility for tactical planning in professional football. The project page is available at: this https URL.

---


### 453. [Memorize When Needed: Decoupled Memory Control for Spatially Consistent Long-Horizon Video Generation](https://arxiv.org/abs/2604.18215)

**<font color=#1a73e8>作者：</font>** Yanjun Guo, Zhengqiang Zhang, Pengfei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatially consistent long-horizon video generation aims to maintain temporal and spatial consistency along predefined camera trajectories. Existing methods mostly entangle memory modeling with video generation, leading to inconsistent content during scene revisits and diminished generative capacity when exploring novel regions, even trained on extensive annotated data. To address these limitations, we propose a decoupled framework that separates memory conditioning from generation. Our approach significantly reduces training costs while simultaneously enhancing spatial consistency and preserving the generative capacity for novel scene exploration. Specifically, we employ a lightweight, independent memory branch to learn precise spatial consistency from historical observation. We first introduce a hybrid memory representation to capture complementary temporal and spatial cues from generated frames, then leverage a per-frame cross-attention mechanism to ensure each frame is conditioned exclusively on the most spatially relevant historical information, which is injected into the generative model to ensure spatial consistency. When generating new scenes, a camera-aware gating mechanism is proposed to mediate the interaction between memory and generation modules, enabling memory conditioning only when meaningful historical references exist. Compared with the existing method, our method is highly data-efficient, yet the experiments demonstrate that our approach achieves state-of-the-art performance in terms of both visual quality and spatial consistency.

---


### 454. [EEG-Based Emergency Braking Intensity Prediction Using Blind Source Separation](https://arxiv.org/abs/2604.18220)

**<font color=#1a73e8>作者：</font>** Zikun Zhou, Wenshuo Wang, Wenzhuo Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) signals have been promising for long-term braking intensity prediction but are prone to various artifacts that limit their reliability. Here, we propose a novel framework that models EEG signals as mixtures of independent blind sources and identifies those strongly correlated with braking action. Our method employs independent component analysis to decompose EEG into different components and combines time-frequency analysis with Pearson correlations to select braking-related components. Furthermore, we utilize hierarchical clustering to group braking-related components into two clusters, each characterized by a distinct spatial pattern. Additionally, these components exhibit trial-invariant temporal patterns and demonstrate stable and common neural signatures of the emergency braking process. Using power features from these components and historical braking data, we predict braking intensity at a 200 ms horizon. Evaluations on the open source dataset (O.D.) and human-in-the-loop simulation (H.S.) show that our method outperforms state-of-the-art approaches, achieving RMSE reductions of 8.0% (O.D.) and 23.8% (H.S.).

---


### 455. [Instruction-as-State: Environment-Guided and State-Conditioned Semantic Understanding for Embodied Navigation](https://arxiv.org/abs/2604.18223)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Yuhan Liu, Jinjun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation requires agents to follow natural-language instructions in visually changing environments. A central challenge is the dynamic entanglement between language and observations: the meaning of instruction shifts as the agent's field of view and spatial context evolve. However, many existing models encode the instruction as a static global representation, limiting their ability to adapt instruction meaning to the current visual context. We therefore model instruction understanding as an Instruction-as-State variable: a decision-relevant, token-level instruction state that evolves step by step conditioned on the agent's perceptual state, where the perceptual state denotes the observation-grounded navigation context at each step. To realize this principle, we introduce State-Entangled Environment-Guided Instruction Understanding (S-EGIU), a coarse-to-fine framework for state-conditioned segment activation and token-level semantic refinement. At the coarse level, S-EGIU activates the instruction segment whose semantics align with the current observation. At the fine level, it refines the activated segment through observation-guided token grounding and contextual modeling, sharpening its internal semantics under the current observation. Together, these stages maintain an instruction state that is continuously updated according to the agent's perceptual state during navigation. S-EGIU delivers strong performance on several key metrics, including a +2.68% SPL gain on REVERIE Test Unseen, and demonstrates consistent efficiency gains across multiple VLN benchmarks, underscoring the value of dynamic instruction--perception entanglement.

---


### 456. [Is SAM3 ready for pathology segmentation?](https://arxiv.org/abs/2604.18225)

**<font color=#1a73e8>作者：</font>** Qiuyu Kong, Shakiba Sharifi, Zanxi Ruan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Is Segment Anything Model 3 (SAM3) capable in segmenting Any Pathology Images? Digital pathology segmentation spans tissue-level and nuclei-level scales, where traditional methods often suffer from high annotation costs and poor generalization. SAM3 introduces Promptable Concept Segmentation, offering a potential automated interface via text prompts. With this work, we propose a systematic evaluation protocol to explore the capability space of SAM3 in a structured manner. Specifically, we evaluate SAM3 under different supervision settings including zero-shot, few-shot, and supervised with varying prompting strategies. Our extensive evaluation on pathological datasets including NuInsSeg, PanNuke and GlaS, reveals that: this http URL-only prompts poorly activate nuclear concepts. this http URL is highly sensitive to visual prompt types and budgets. this http URL-shot learning offers gains, but SAM3 lacks robustness against visual prompt noise. and 4.a significant gap persists between prompt-based usage and task-trained adapter-based reference. Our study delineates SAM3's boundaries in pathology image segmentation and provides practical guidance on the necessity of pathology domain adaptation.

---


### 457. [Model in Distress: Sentiment Analysis on French Synthetic Social Media](https://arxiv.org/abs/2604.18226)

**<font color=#1a73e8>作者：</font>** Pierre-Carl Langlais, Pavel Chizhov, Yannick Detrois 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated analysis of customer feedback on social media is hindered by three challenges: the high cost of annotated training data, the scarcity of evaluation sets, especially in multilingual settings, and privacy concerns that prevent data sharing and reproducibility. We address these issues by developing a generalizable synthetic data generation pipeline applied to a case study on customer distress detection in French public transportation. Our approach utilizes backtranslation with fine-tuned models to generate 1.7 million synthetic tweets from a small seed corpus, complemented by synthetic reasoning traces. We train 600M-parameter reasoners with English and French reasoning that achieve 77-79% accuracy on human-annotated evaluation data, matching or exceeding SOTA proprietary LLMs and specialized encoders. Beyond reducing annotation costs, our pipeline preserves privacy by eliminating the exposure of sensitive user data. Our methodology can be adopted for other use cases and languages.

---


### 458. [FSEVAL: Feature Selection Evaluation Toolbox and Dashboard](https://arxiv.org/abs/2604.18227)

**<font color=#1a73e8>作者：</font>** Muhammad Rajabinasab, Arthur Zimek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection is a fundamental machine learning and data mining task, involved with discriminating redundant features from informative ones. It is an attempt to address the curse of dimensionality by removing the redundant features, while unlike dimensionality reduction methods, preserving explainability. Feature selection is conducted in both supervised and unsupervised settings, with different evaluation metrics employed to determine which feature selection algorithm is the best. In this paper, we propose FSEVAL, a feature selection evaluation toolbox accompanied with a visualization dashboard, with the goal to make it easy to comprehensively evaluate feature selection algorithms. FSEVAL aims to provide a standardized, unified, evaluation and visualization toolbox to help the researchers working in the field, conduct extensive and comprehensive evaluation of feature selection algorithms with ease.

---


### 459. [Negative Advantage Is a Double-Edged Sword: Calibrating Advantage in GRPO for Deep Search](https://arxiv.org/abs/2604.18235)

**<font color=#1a73e8>作者：</font>** Jiayi Wu, Ruobing Xie, Zeqian Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep search agents can autonomously initiate multi-turn interactions with search engines, thereby exhibiting strong question-answering capabilities. Such performance critically relies on Group Relative Policy Optimization (GRPO) as its core training algorithm. However, GRPO still faces several challenges in deep search settings. First, there exists a substantial mismatch between the correctness of intermediate steps and the reward signal, causing numerous correct intermediate steps to be incorrectly penalized when the final answer is wrong. Second, training is highly unstable, often resulting in degradation of natural language ability or even catastrophic training collapse. Our analysis attributes these issues to coarse-grained advantage assignment and an imbalance between positive and negative advantages. To address these problems, we propose CalibAdv, an advantage calibration method specifically designed for deep search tasks. Specifically, CalibAdv leverages the correctness of intermediate steps to downscale excessive negative advantages at a fine-grained level. It then rebalances positive and negative advantages in the answer component. Extensive experiments across three models and seven benchmarks demonstrate that CalibAdv improves both model performance and training stability. Our code is available at this https URL.

---


### 460. [Semantic-based Distributed Learning for Diverse and Discriminative Representations](https://arxiv.org/abs/2604.18237)

**<font color=#1a73e8>作者：</font>** Zhuojun Tian, Chaouki Ben Issaid, Mehdi Bennis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale distributed scenarios, increasingly complex tasks demand more intelligent collaboration across networks, requiring the joint extraction of structural representations from data samples. However, conventional task-specific approaches often result in nonstructural embeddings, leading to collapsed variability among data samples within the same class, particularly in classification tasks. To address this issue and fully leverage the intrinsic structure of data for downstream applications, we propose a novel distributed learning framework that ensures both diverse and discriminative representations. For independent and identically distributed (i.i.d.) data, we reformulate and decouple the global optimization function by introducing constraints on representation variance. The update rules are then derived and simplified using a primal-dual approach. For non-i.i.d. data distributions, we tackle the problem by clustering and virtually replicating nodes, allowing model updates within each cluster using block coordinate descent. In both cases, the resulting optimal solutions are theoretically proven to maintain discriminative and diverse properties, with a guaranteed convergence for i.i.d. conditions. Additionally, semantic information from representations is shared among nodes, reducing the need for common neural network architectures. Finally, extensive simulations on MNIST, CIFAR-10 and CIFAR-100 confirm the effectiveness of the proposed algorithms in capturing global structural representations.

---


### 461. [AJ-Bench: Benchmarking Agent-as-a-Judge for Environment-Aware Evaluation](https://arxiv.org/abs/2604.18240)

**<font color=#1a73e8>作者：</font>** Wentao Shi, Yu Wang, Yuyang Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As reinforcement learning continues to scale the training of large language model-based agents, reliably verifying agent behaviors in complex environments has become increasingly challenging. Existing approaches rely on rule-based verifiers or LLM-as-a-Judge models, which struggle to generalize beyond narrow domains. Agent-as-a-Judge addresses this limitation by actively interacting with environments and tools to acquire verifiable evidence, yet its capabilities remain underexplored.
We introduce a benchmark AJ-Bench to systematically evaluate Agent-as-a-Judge across three domains-search, data systems, and graphical user interfaces-comprising 155 tasks and 516 annotated trajectories. The benchmark comprehensively assesses judge agents' abilities in information acquisition, state verification, and process verification. Experiments demonstrate consistent performance gains over LLM-as-a-Judge baselines, while also revealing substantial open challenges in agent-based verification. Our data and code are available at this https URL.

---


### 462. [Beyond Pattern Matching: Seven Cross-Domain Techniques for Prompt Injection Detection](https://arxiv.org/abs/2604.18248)

**<font color=#1a73e8>作者：</font>** Thamilvendhan Munirathinam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current open-source prompt-injection detectors converge on two architectural choices: regular-expression pattern matching and fine-tuned transformer classifiers. Both share failure modes that recent work has made concrete. Regular expressions miss paraphrased attacks. Fine-tuned classifiers are vulnerable to adaptive adversaries: a 2025 NAACL Findings study reported that eight published indirect-injection defenses were bypassed with greater than fifty percent attack success rates under adaptive attacks. This work proposes seven detection techniques that each port a specific mechanism from a discipline outside large-language-model security: forensic linguistics, materials-science fatigue analysis, deception technology from network security, local-sequence alignment from bioinformatics, mechanism design from economics, spectral signal analysis from epidemiology, and taint tracking from compiler theory. Three of the seven techniques are implemented in the prompt-shield v0.4.1 release (Apache 2.0) and evaluated in a four-configuration ablation across six datasets including deepset/prompt-injections, NotInject, LLMail-Inject, AgentHarm, and AgentDojo. The local-alignment detector lifts F1 on deepset from 0.033 to 0.378 with zero additional false positives. The stylometric detector adds 11.1 percentage points of F1 on an indirect-injection benchmark. The fatigue tracker is validated via a probing-campaign integration test. All code, data, and reproduction scripts are released under Apache 2.0.

---


### 463. [Where Do Self-Supervised Speech Models Become Unfair?](https://arxiv.org/abs/2604.18249)

**<font color=#1a73e8>作者：</font>** Felix Herron, Maja Hjuler, Solange Rossato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech encoder models are known to model members of some speaker groups (SGs) better than others. However, there has been little work in establishing why this occurs on a technological level. To our knowledge, we present the first layerwise fairness analysis of pretrained self-supervised speech encoder models (S3Ms), probing each embedding layer for speaker identification (SID) automatic speech recognition (ASR). We find S3Ms produce embeddings biased against certain SGs for both tasks, starting at the very first latent layers. Furthermore, we find opposite patterns of layerwise bias for SID vs ASR for all models in our study: SID bias is minimized in layers that minimize overall SID error; on the other hand, ASR bias is maximized in layers that minimize overall ASR error. The inverse bias/error relationship for ASR is unaffected when probing S3Ms that are finetuned for ASR, suggesting SG-level bias is established during pretraining and is difficult to remove.

---


### 464. [Style-Based Neural Architectures for Real-Time Weather Classification](https://arxiv.org/abs/2604.18251)

**<font color=#1a73e8>作者：</font>** Hamed Ouattara, Pascal Houssam Salmane, Pierre Duthon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we present three neural network architectures designed for real-time classification of weather conditions (sunny, rain, snow, fog) from images. These models, inspired by recent advances in style transfer, aim to capture the stylistic elements present in images. One model, called "Multi-PatchGAN", is based on PatchGANs used in well-known architectures such as Pix2Pix and CycleGAN, but here adapted with multiple patch sizes for detection tasks. The second model, "Truncated ResNet50", is a simplified version of ResNet50 retaining only its first nine layers. This truncation, determined by an evolutionary algorithm, facilitates the extraction of high-frequency features essential for capturing subtle stylistic details. Finally, we propose "Truncated ResNet50 with Gram Matrix and Attention", which computes Gram matrices for each layer during training and automatically weights them via an attention mechanism, thus optimizing the extraction of the most relevant stylistic expressions for classification. These last two models outperform the state of the art and demonstrate remarkable generalization capability on several public databases. Although developed for weather detection, these architectures are also suitable for other appearance-based classification tasks, such as animal species recognition, texture classification, disease detection in medical imaging, or industrial defect identification.

---


### 465. [Domain-Specialized Object Detection via Model-Level Mixtures of Experts](https://arxiv.org/abs/2604.18256)

**<font color=#1a73e8>作者：</font>** Svetlana Pavlitska, Malte Stüven, Beyza Keskin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models provide a structured approach to combining specialized neural networks and offer greater interpretability than conventional ensembles. While MoEs have been successfully applied to image classification and semantic segmentation, their use in object detection remains limited due to challenges in merging dense and structured predictions. In this work, we investigate model-level mixtures of object detectors and analyze their suitability for improving performance and interpretability in object detection. We propose an MoE architecture that combines YOLO-based detectors trained on semantically disjoint data subsets, with a learned gating network that dynamically weights expert contributions. We study different strategies for fusing detection outputs and for training the gating mechanism, including balancing losses to prevent expert collapse. Experiments on the BDD100K dataset demonstrate that the proposed MoE consistently outperforms standard ensemble approaches and provides insights into expert specialization across domains, highlighting model-level MoEs as a viable alternative to traditional ensembling for object detection. Our code is available at this https URL.

---


### 466. [Long-Text-to-Image Generation via Compositional Prompt Decomposition](https://arxiv.org/abs/2604.18258)

**<font color=#1a73e8>作者：</font>** Jen-Yuan Huang, Tong Lin, Yilun Du  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern text-to-image (T2I) models excel at generating images from intricate prompts, they struggle to capture the key details when the inputs are descriptive paragraphs. This limitation stems from the prevalence of concise captions that shape their training distributions. Existing methods attempt to bridge this gap by either fine-tuning T2I models on long prompts, which generalizes poorly to longer lengths; or by projecting the oversize inputs into normal-prompt space and compromising fidelity. We propose Prompt Refraction for Intricate Scene Modeling (PRISM), a compositional approach that enables pre-trained T2I models to process long sequence inputs. PRISM uses a lightweight module to extract constituent representations from the long prompts. The T2I model makes independent noise predictions for each component, and their outputs are merged into a single denoising step using energy-based conjunction. We evaluate PRISM across a wide range of model architectures, showing comparable performances to models fine-tuned on the same training data. Furthermore, PRISM demonstrates superior generalization, outperforming baseline models by 7.4% on prompts over 500 tokens in a challenging public benchmark.

---


### 467. [Enhancing Tabular Anomaly Detection via Pseudo-Label-Guided Generation](https://arxiv.org/abs/2604.18266)

**<font color=#1a73e8>作者：</font>** Wei Huang, Yuxuan Xiong, Hezhe Qiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying anomalous instances in tabular data is essential for improving data reliability and maintaining system stability. Due to the scarcity of ground-truth anomaly labels, existing methods mainly rely on unsupervised anomaly detection models, or exploit a small number of labeled anomalies to facilitate detection via sample generation or contrastive learning. However, unsupervised methods lack sufficient anomaly awareness, while current generation and contrastive approaches tend to compute anomalies globally, overlooking the localized anomaly patterns of tabular features, resulting in suboptimal detection performance. To address these limitations, we propose PLAG, a pseudo-label-guided anomaly generation method designed to enhance tabular anomaly detection. Specifically, by utilizing pseudo-anomalies as guidance signals and decoupling the overall anomaly quantification of a sample into an accumulation of feature-level abnormalities, PLAG not only effectively obviates the need for scarce ground-truth labels but also provides a novel perspective for the model to comprehend localized anomalous signals at a fine-grained level. Furthermore, a two-stage data selection strategy is proposed, integrating format verification and uncertainty estimation to rigorously filter candidate samples, thereby ensuring the fidelity and diversity of the synthetic anomalies. Ultimately, these filtered synthetic anomalies serve as robust discriminative guidance, empowering the model to better separate normal and anomalous instances. Extensive experiments demonstrate that PLAG achieves state-of-the-art performance against eight representative baselines. Moreover, as a flexible framework, it integrates seamlessly with existing unsupervised detectors, consistently boosting F1-scores by 0.08 to 0.21.

---


### 468. [MARCO: Navigating the Unseen Space of Semantic Correspondence](https://arxiv.org/abs/2604.18267)

**<font color=#1a73e8>作者：</font>** Claudia Cuttano, Gabriele Trivigno, Carlo Masone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in semantic correspondence rely on dual-encoder architectures, combining DINOv2 with diffusion backbones. While accurate, these billion-parameter models generalize poorly beyond training keypoints, revealing a gap between benchmark performance and real-world usability, where queried points rarely match those seen during training. Building upon DINOv2, we introduce MARCO, a unified model for generalizable correspondence driven by a novel training framework that enhances both fine-grained localization and semantic generalization. By coupling a coarse-to-fine objective that refines spatial precision with a self-distillation framework, which expands sparse supervision beyond annotated regions, our approach transforms a handful of keypoints into dense, semantically coherent correspondences. MARCO sets a new state of the art on SPair-71k, AP-10K, and PF-PASCAL, with gains that amplify at fine-grained localization thresholds (+8.9 PCK@0.01), strongest generalization to unseen keypoints (+5.1, SPair-U) and categories (+4.7, MP-100), while remaining 3x smaller and 10x faster than diffusion-based approaches. Code is available at this https URL .

---


### 469. [LiquidTAD: An Efficient Method for Temporal Action Detection via Liquid Neural Dynamics](https://arxiv.org/abs/2604.18274)

**<font color=#1a73e8>作者：</font>** Zepeng Sun, Naichuan Zheng, Hailun Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal Action Detection (TAD) in untrimmed videos is currently dominated by Transformer-based architectures. While high-performing, their quadratic computational complexity and substantial parameter redundancy limit deployment in resource-constrained environments. In this paper, we propose LiquidTAD, a novel parameter-efficient framework that replaces cumbersome self-attention layers with parallelized ActionLiquid blocks. Unlike traditional Liquid Neural Networks (LNNs) that suffer from sequential execution bottlenecks, LiquidTAD leverages a closed-form continuous-time (CfC) formulation, allowing the model to be reformulated as a parallelizable operator while preserving the intrinsic physical prior of continuous-time dynamics. This architecture captures complex temporal dependencies with $O(N)$ linear complexity and adaptively modulates temporal sensitivity through learned time-constants ($\tau$), providing a robust mechanism for handling varying action durations. To the best of our knowledge, this work is the first to introduce a parallelized LNN-based architecture to the TAD domain. Experimental results on the THUMOS-14 dataset demonstrate that LiquidTAD achieves a highly competitive Average mAP of 69.46\% with only 10.82M parameters -- a 63\% reduction compared to the ActionFormer baseline. Further evaluations on ActivityNet-1.3 and Ego4D benchmarks confirm that LiquidTAD achieves an optimal accuracy-efficiency trade-off and exhibits superior robustness to temporal sampling variations, advancing the Pareto frontier of modern TAD frameworks.

---


### 470. [Dissipative Latent Residual Physics-Informed Neural Networks for Modeling and Identification of Electromechanical Systems](https://arxiv.org/abs/2604.18277)

**<font color=#1a73e8>作者：</font>** Youyuan Long, Gokhan Solak, Arash Ajoudani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate dynamical modeling is essential for simulation and control of embodied systems, yet first-principles models of electromechanical systems often fail to capture complex dissipative effects such as joint friction, stray losses, and structural damping. While residual-learning physics-informed neural networks (PINNs) can effectively augment imperfect first-principles models with data-driven components, the residual terms are typically implemented as unconstrained multilayer perceptrons (MLPs), which may inadvertently inject artificial energy into the system.
To more faithfully model the dissipative dynamics, we propose DiLaR-PINN, a dissipative latent residual PINN designed to learn unmodeled dissipative effects in a physically consistent manner. Structurally, the residual network operates only on unmeasurable (latent) state components and is parameterized in a skew-dissipative form that guarantees non-increasing energy for any choice of network parameters. To enable stable and data-efficient training under partial measurability of the state, we further develop a recurrent rollout scheme with a curriculum-based sequence length extension strategy.
We validate DiLaR-PINN on a real-world helicopter system and compare it against four baselines: a pure physical model (without a residual network), an unstructured residual MLP, a DiLaR variant with a soft dissipativity constraint, and a black-box LSTM. The results demonstrate that DiLaR-PINN more accurately captures dissipative effects and achieves superior long-horizon extrapolation performance.

---


### 471. [Subcodes of Lambda-Gabidulin Codes for Compact-Ciphertext Cryptography](https://arxiv.org/abs/2604.18282)

**<font color=#1a73e8>作者：</font>** Freddy Lendé Metouké, Hervé Talé Kalachi, Hermann Tchatchiem Kamche 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper investigates subcodes of lambda-Gabidulin codes, viewed as rank-metric analogues of generalized Reed--Solomon codes, and their applications to compact-ciphertext cryptosystems. We first analyze subspace and generalized subspace subcodes of lambda-Gabidulin codes and relate them to corresponding subcodes of classical Gabidulin codes through coordinate-wise scaling. This relation yields cardinality bounds and structural properties for these families. When the extension degree equals the code length, we further characterize Gabidulin subspace subcodes in terms of linearized polynomials, which gives an explicit description of their encoding and dimension. We also study the matrix images of these subcodes over the base field through their stabilizer and annihilator algebras, showing that subspace restrictions may preserve nontrivial algebraic invariants despite the loss of extension-field linearity. Motivated by these results, we propose a generator-matrix-based construction of random subcodes designed to avoid such invariants. This construction is then used to design McEliece-like and Niederreiter-like encryption schemes in the MinRank setting. Among the parameter sets considered in this work, the most compact ciphertexts are obtained from random subcodes of classical Gabidulin codes. At the 128-, 192-, and 256-bit security levels, the resulting $\mathsf{LGS}$-Niederreiter instances achieve the smallest ciphertext sizes among the compared schemes, while maintaining competitive public-key sizes.

---


### 472. [Spike-NVPT: Learning Robust Visual Prompts via Bio-Inspired Temporal Filtering and Discretization](https://arxiv.org/abs/2604.18284)

**<font color=#1a73e8>作者：</font>** Qiugang Zhan, Anning Jiang, Ran Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision models have found widespread application across diverse domains. Prompt tuning-based methods have emerged as a parameter-efficient paradigm for adapting pre-trained vision models. While effective on standard benchmarks, the continuous and dense nature of learned prompts can lead to sensitivity against input noise, as the high-capacity prompts tend to overfit task-irrelevant details. To address this trade-off, we propose Spike-NVPT, a noise-robust visual prompt tuning method. Specifically, we design a Signal Filtering Layer based on spiking neurons, which uses the integrate-and-fire (IF) mechanism to accumulate task-relevant signals over time and filter transient noise fluctuations. A subsequent Spike Discretization Unit converts filtered signals into sparse binary prompts. This discretization acts as a strong regularizer, forcing the model to anchor decision boundaries on the most discriminative and robust features. Notably, the resulting binary prompts remain static during deployment, ensuring zero additional computational overhead during inference. Experimental results demonstrate that Spike-NVPT achieves superior robustness performance, with a maximum improvement of 11.2% over conventional methods, and retains competitive accuracy on clean datasets. To the best of our knowledge, this is the first attempt to leverage spiking neurons for fine-tuning traditional artificial neural network (ANN)-based visual models.

---


### 473. [Agent-World: Scaling Real-World Environment Synthesis for Evolving General Agent Intelligence](https://arxiv.org/abs/2604.18292)

**<font color=#1a73e8>作者：</font>** Guanting Dong, Junting Lu, Junjie Huang 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly expected to serve as general-purpose agents that interact with external, stateful tool environments. The Model Context Protocol (MCP) and broader agent skills offer a unified interface for connecting agents with scalable real-world services, but training robust agents remains limited by the lack of realistic environments and principled mechanisms for life-long learning. In this paper, we present \textbf{Agent-World}, a self-evolving training arena for advancing general agent intelligence through scalable environments. Agent-World has two main components: (1) Agentic Environment-Task Discovery, which autonomously explores topic-aligned databases and executable tool ecosystems from thousands of real-world environment themes and synthesizes verifiable tasks with controllable difficulty; and (2) Continuous Self-Evolving Agent Training, which combines multi-environment reinforcement learning with a self-evolving agent arena that automatically identifies capability gaps through dynamic task synthesis and drives targeted learning, enabling the co-evolution of agent policies and environments. Across 23 challenging agent benchmarks, Agent-World-8B and 14B consistently outperforms strong proprietary models and environment scaling baselines. Further analyses reveal scaling trends in relation to environment diversity and self-evolution rounds, offering insights for building general agent intelligence.

---


### 474. [Exploring Concreteness Through a Figurative Lens](https://arxiv.org/abs/2604.18296)

**<font color=#1a73e8>作者：</font>** Saptarshi Ghosh, Tianyu Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Static concreteness ratings are widely used in NLP, yet a word's concreteness can shift with context, especially in figurative language such as metaphor, where common concrete nouns can take abstract interpretations. While such shifts are evident from context, it remains unclear how LLMs understand concreteness internally. We conduct a layer-wise and geometric analysis of LLM hidden representations across four model families, examining how models distinguish literal vs figurative uses of the same noun and how concreteness is organized in representation space. We find that LLMs separate literal and figurative usage in early layers, and that mid-to-late layers compress concreteness into a one-dimensional direction that is consistent across models. Finally, we show that this geometric structure is practically useful: a single concreteness direction supports efficient figurative-language classification and enables training-free steering of generation toward more literal or more figurative rewrites.

---


### 475. [Circadian Phase Locking of Epilepsy Seizures in Wearable Data: A Single-Patient Case Study](https://arxiv.org/abs/2604.18297)

**<font color=#1a73e8>作者：</font>** Berenika Ewart-James, Matthew Wragg, Nawid Keshtmand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Epilepsy is a common, chronic neurological disorder characterized by recurrent seizures caused by sudden bursts of abnormal electrical activity in the brain. Seizures can often be unpredictable, leading to uncertainty and anxiety for people with epilepsy. To address this problem, the Epilepsy UK Priority Setting Partnership identified research into seizure forecasting technology as a priority. Seizure onsets are recorded as discrete events embedded within continuously sampled physiological signals that exhibit strong circadian and multi-day rhythms. Standard modelling approaches often treat time as linear or rely on clock-time features, which may not explicitly capture the underlying physiological phase. In this paper, we examine whether seizure onsets exhibit phase preference relative to circadian rhythms derived from wearable inter-beat interval (IBI) data. As a proof-of-concept, using 176 days wearable and seizure diary data from a single patient, we extract oscillatory components via band-limited filtering and Hilbert-based phase estimation, and test for non-uniform seizure-phase alignment using circular statistics. We observe significant circadian phase concentration, while multiday bands do not show consistent or statistically significant phase clustering in this dataset. Exploratory logistic baselines indicate modest but detectable structure beyond simple clock-time effects. We argue that explicit physiological phase representations provide an interpretable bridge between continuous wearable sensing and sparse clinical events and may augment existing seizure forecasting pipelines. We discuss implications for multi-scale modelling, patient-facing interfaces, and future multi-patient validation

---


### 476. [On the Importance and Evaluation of Narrativity in Natural Language AI Explanations](https://arxiv.org/abs/2604.18311)

**<font color=#1a73e8>作者：</font>** Mateusz Cedro, David Martens  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) aims to make the behaviour of machine learning models interpretable, yet many explanation methods remain difficult to understand. The integration of Natural Language Generation into XAI aims to deliver explanations in textual form, making them more accessible to practitioners. Current approaches, however, largely yield static lists of feature importances. Although such explanations indicate what influences the prediction, they do not explain why the prediction occurs. In this study, we draw on insights from social sciences and linguistics, and argue that XAI explanations should be presented in the form of narratives. Narrative explanations support human understanding through four defining properties: continuous structure, cause-effect mechanisms, linguistic fluency, and lexical diversity. We show that standard Natural Language Processing (NLP) metrics based solely on token probability or word frequency fail to capture these properties and can be matched or exceeded by tautological text that conveys no explanatory content. To address this issue, we propose seven automatic metrics that quantify the narrative quality of explanations along the four identified dimensions. We benchmark current state-of-the-art explanation generation methods on six datasets and show that the proposed metrics separate descriptive from narrative explanations more reliably than standard NLP metrics. Finally, to further advance the field, we propose a set of problem-agnostic XAI Narrative generation rules for producing natural language XAI explanations, so that the resulting XAI Narratives exhibit stronger narrative properties and align with the findings from the linguistic and social science literature.

---


### 477. [Scale-free adaptive planning for deterministic dynamics & discounted rewards](https://arxiv.org/abs/2604.18312)

**<font color=#1a73e8>作者：</font>** Peter L. Bartlett, Victor Gabillon, Jennifer Healey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the problem of planning in an environment with deterministic dynamics and stochastic rewards with discounted returns. The optimal value function is not known, nor are the rewards bounded. We propose Platypoos, a simple scale-free planning algorithm that adapts to the unknown scale and smoothness of the reward function. We provide a sample complexity analysis for Platypoos that improves upon prior work and holds simultaneously over a broad range of discount factors and reward scales, without the algorithm knowing them. We also establish a matching lower bound showing our analysis is optimal up to constants.

---


### 478. [Denoise and Align: Diffusion-Driven Foreground Knowledge Prompting for Open-Vocabulary Temporal Action Detection](https://arxiv.org/abs/2604.18313)

**<font color=#1a73e8>作者：</font>** Sa Zhu, Wanqian Zhang, Lin Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-Vocabulary Temporal Action Detection (OV-TAD) aims to localize and classify action segments of unseen categories in untrimmed videos, where effective alignment between action semantics and video representations is critical for accurate detection. However, existing methods struggle to mitigate the semantic imbalance between concise, abstract action labels and rich, complex video contents, inevitably introducing semantic noise and misleading cross-modal alignment. To address this challenge, we propose DFAlign, the first framework that leverages diffusion-based denoising to generate foreground knowledge for the guidance of action-video alignment. Following the 'conditioning, denoising and aligning' manner, we first introduce the Semantic-Unify Conditioning (SUC) module, which unifies action-shared and action-specific semantics as conditions for diffusion denoising. Then, the Background-Suppress Denoising (BSD) module generates foreground knowledge by progressively removing background redundancy from videos through denoising process. This foreground knowledge serves as effective intermediate semantic anchor between video and text representations, mitigating the semantic gap and enhancing the discriminability of action-relevant segments. Furthermore, we introduce the Foreground-Prompt Alignment (FPA) module to inject extracted foreground knowledge as prompt tokens into text representations, guiding model's attention towards action-relevant segments and enabling precise cross-modal alignment. Extensive experiments demonstrate that our method achieves state-of-the-art performance on two OV-TAD benchmarks. The code repository is provided as follows: this https URL.

---


### 479. [OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326)

**<font color=#1a73e8>作者：</font>** Lei Zhu, Xing Cai, Yingjie Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in audio-video joint generation models have demonstrated impressive capabilities in content creation. However, generating high-fidelity human-centric videos in complex, real-world physical scenes remains a significant challenge. We identify that the root cause lies in the structural deficiencies of existing datasets across three dimensions: limited global scene and camera diversity, sparse interaction modeling (both person-person and person-object), and insufficient individual attribute alignment. To bridge these gaps, we present OmniHuman, a large-scale, multi-scene dataset designed for fine-grained human modeling. OmniHuman provides a hierarchical annotation covering video-level scenes, frame-level interactions, and individual-level attributes. To facilitate this, we develop a fully automated pipeline for high-quality data collection and multi-modal annotation. Complementary to the dataset, we establish the OmniHuman Benchmark (OHBench), a three-level evaluation system that provides a scientific diagnosis for human-centric audio-video synthesis. Crucially, OHBench introduces metrics that are highly consistent with human perception, filling the gaps in existing benchmarks by providing a comprehensive diagnosis across global scenes, relational interactions, and individual attributes.

---


### 480. [FregeLogic at SemEval 2026 Task 11: A Hybrid Neuro-Symbolic Architecture for Content-Robust Syllogistic Validity Prediction](https://arxiv.org/abs/2604.18328)

**<font color=#1a73e8>作者：</font>** Adewale Akinfaderin, Nafi Diallo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present FregeLogic, a hybrid neuro-symbolic system for SemEval-2026 Task 11 (Subtask 1), which addresses syllogistic validity prediction while reducing content effects on predictions. Our approach combines an ensemble of five LLM classifiers, spanning three open-weights models (Llama 4 Maverick, Llama 4 Scout, and Qwen3-32B) paired with varied prompting strategies, with a Z3 SMT solver that serves as a formal logic tiebreaker. The central hypothesis is that LLM disagreement within the ensemble signals likely content-biased errors, where real-world believability interferes with logical judgment. By deferring to Z3's structurally-grounded formal verification on these disputed cases, our system achieves 94.3% accuracy with a content effect of 2.85 and a combined score of 41.88 in nested 5-fold cross-validation on the dataset (N=960). This represents a 2.76-point improvement in combined score over the pure ensemble (39.12), with a 0.9% accuracy gain, driven by a 16% reduction in content effect (3.39 to 2.85). Adopting structured-output API calls for Z3 extraction reduced failure rates from ~22% to near zero, and an Aristotelian encoding with existence axioms was validated against task annotations. Our results suggest that targeted neuro-symbolic integration, applying formal methods precisely where ensemble consensus is lowest, can improve the combined accuracy-plus-content-effect metric used by this task.

---


### 481. [One Pass for All: A Discrete Diffusion Model for Knowledge Graph Triple Set Prediction](https://arxiv.org/abs/2604.18344)

**<font color=#1a73e8>作者：</font>** Jihong Guan, Jiaqi Wang, Wengen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge Graphs (KGs) are composed of triples, and the goal of Knowledge Graph Completion (KGC) is to infer the missing factual triples. Traditional KGC tasks predict missing elements in a triple given one or two of its elements. As a more realistic task, the Triple Set Prediction (TSP) task aims to infer the set of missing triples conditioned only on the observed knowledge graph, without assuming any partial information about the missing triples. Existing TSP methods predict the set of missing triples in a triple-by-triple manner, falling short in capturing the dependencies among the predicted triples to ensure consistency. To address this issue, we propose a novel discrete diffusion model termed DiffTSP that treats TSP as a generative task. DiffTSP progressively adds noise to the KG through a discrete diffusion process, achieved by masking relational edges. The reverse process then gradually recovers the complete KG conditioned on the incomplete graph. To this end, we design a structure-aware denoising network that integrates a relational context encoder with a relational graph diffusion transformer for knowledge graph generation. DiffTSP can generate the complete set of triples in a one-pass manner while ensuring the dependencies among the predicted triples. Our approach achieves state-of-the-art performance on three public datasets. Code: this https URL.

---


### 482. [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](https://arxiv.org/abs/2604.18348)

**<font color=#1a73e8>作者：</font>** Haoyue Tan, Shengnan Wang, Yulin Qiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers (DiTs) suffer from prohibitive inference latency due to quadratic attention complexity. Existing sparse attention methods either overlook semantic similarity or fail to adapt to heterogeneous token distributions across layers, leading to model performance degradation. We propose AdaCluster, a training-free adaptive clustering framework that accelerates the generation of DiTs while preserving accuracy. AdaCluster applies an angle-similarity-preserving clustering method to query vectors for higher compression, and designs a euclidean-similarity-preserving clustering method for keys, covering cluster number assignment, threshold-wise adaptive clustering, and efficient critical cluster selection. Experiments on CogVideoX-2B, HunyuanVideo, and Wan-2.1 on one A40 GPU demonstrate up to 1.67-4.31x speedup with negligible quality degradation.

---


### 483. [Tight Auditing of Differential Privacy in MST and AIM](https://arxiv.org/abs/2604.18352)

**<font color=#1a73e8>作者：</font>** Georgi Ganev, Meenatchi Sundaram Muthu Selva Annamalai, Bogdan Kulynych  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> State-of-the-art Differentially Private (DP) synthetic data generators such as MST and AIM are widely used, yet tightly auditing their privacy guarantees remains challenging. We introduce a Gaussian Differential Privacy (GDP)-based auditing framework that measures privacy via the full false-positive/false-negative tradeoff. Applied to MST and AIM under worst-case settings, our method provides the first tight audits in the strong-privacy regime. For $(\epsilon,\delta)=(1,10^{-2})$, we obtain $\mu_{emp}\approx0.43$ vs. implied $\mu=0.45$, showing a small theory-practice gap.
Our code is publicly available: this https URL.

---


### 484. [PRISMA: Preference-Reinforced Self-Training Approach for Interpretable Emotionally Intelligent Negotiation Dialogues](https://arxiv.org/abs/2604.18354)

**<font color=#1a73e8>作者：</font>** Prajwal Vijay Kajare, Priyanshu Priya, Bikash Santra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion plays a pivotal role in shaping negotiation outcomes, influencing trust, cooperation, and long-term relationships. Developing negotiation dialog systems that can recognize and respond strategically to emotions is, therefore, essential to create more effective human-centered interactions. Beyond generating emotionally appropriate responses, interpretability - understanding how a system generates a particular emotion-aware response, is critical for fostering reliability and building rapport. Driven by these aspects, in this work, we introduce PRISMA, an interpretable emotionally intelligent negotiation dialogue system targeting two application domains, viz. job interviews and resource allocation. To enable interpretability, we propose an Emotion-aware Negotiation Strategy-informed Chain-of-Thought (ENS-CoT) reasoning mechanism, which mimics human negotiation by perceiving, understanding, using, and managing emotions. Leveraging ENS-CoT, we curate two new datasets: JobNego (for job interview negotiation) and ResNego (for resource allocation negotiation). We then leverage these datasets to develop PRISMA by augmenting self-training with Direct Preference Optimization (DPO), guiding agents toward more accurate, interpretable, and emotionally appropriate negotiation responses. Automatic and human evaluation on JobNego and ResNego datasets demonstrate that PRISMA substantially enhances interpretability and generates appropriate emotion-aware responses, while improving overall negotiation effectiveness.

---


### 485. [LBFTI: Layer-Based Facial Template Inversion for Identity-Preserving Fine-Grained Face Reconstruction](https://arxiv.org/abs/2604.18358)

**<font color=#1a73e8>作者：</font>** Zixuan Shen, Zhihua Xia, Kaikai Gan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In face recognition systems, facial templates are widely adopted for identity authentication due to their compliance with the data minimization principle. However, facial template inversion technologies have posed a severe privacy leakage risk by enabling face reconstruction from templates. This paper proposes a Layer-Based Facial Template Inversion (LBFTI) method to reconstruct identity-preserving fine-grained face images. Our scheme decomposes face images into three layers: foreground layers (including eyebrows, eyes, nose, and mouth), midground layers (skin), and background layers (other parts). LBFTI leverages dedicated generators to produce these layers, adopting a rigorous three-stage training strategy: (1) independent refined generation of foreground and midground layers, (2) fusion of foreground and midground layers with template secondary injection to produce complete panoramic face images with background layers, and (3) joint fine-tuning of all modules to optimize inter-layer coordination and identity consistency. Experiments demonstrate that our LBFTI not only outperforms state-of-the-art methods in machine authentication performance, with a 25.3% improvement in TAR, but also achieves better similarity in human perception, as validated by both quantitative metrics and a questionnaire survey.

---


### 486. [EAST: Early Action Prediction Sampling Strategy with Token Masking](https://arxiv.org/abs/2604.18367)

**<font color=#1a73e8>作者：</font>** Iva Sović, Ivan Martinović, Marin Oršić  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early action prediction seeks to anticipate an action before it fully unfolds, but limited visual evidence makes this task especially challenging. We introduce EAST, a simple and efficient framework that enables a model to reason about incomplete observations. In our empirical study, we identify key components when training early action prediction models. Our key contribution is a randomized training strategy that samples a time step separating observed and unobserved video frames, enabling a single model to generalize seamlessly across all test-time observation ratios. We further show that joint learning on both observed and future (oracle) representations significantly boosts performance, even allowing an encoder-only model to excel. To improve scalability, we propose a token masking procedure that cuts memory usage in half and accelerates training by 2x with negligible accuracy loss. Combined with a forecasting decoder, EAST sets a new state of the art on NTU60, SSv2, and UCF101, surpassing previous best work by 10.1, 7.7, and 3.9 percentage points, respectively.

---


### 487. [DSA-CycleGAN: A Domain Shift Aware CycleGAN for Robust Multi-Stain Glomeruli Segmentation](https://arxiv.org/abs/2604.18368)

**<font color=#1a73e8>作者：</font>** Zeeshan Nisar, Friedrich Feuerhake, Thomas Lampert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in segmentation in digital histopathology is inter- and intra-stain variations as it reduces model performance. Labelling each stain is expensive and time-consuming so methods using stain transfer via CycleGAN, have been developed for training multi-stain segmentation models using labels from a single stain. Nevertheless, CycleGAN tends to introduce noise during translation because of the one-to-many nature of some stain pairs, which conflicts with its cycle consistency loss. To address this, we propose the Domain Shift Aware CycleGAN, which reduces the presence of such noise. Furthermore, we evaluate several advances from the field of machine learning aimed at resolving similar problems and compare their effectiveness against DSA-CycleGAN in the context of multi-stain glomeruli segmentation. Experiments demonstrate that DSA-CycleGAN not only improves segmentation performance in glomeruli segmentation but also outperforms other methods in reducing noise. This is particularly evident when translating between biologically distinct stains. The code is publicly available at this https URL.

---


### 488. [Parkinson's Disease Detection via Self-Supervised Dual-Channel Cross-Attention on Bilateral Wrist-Worn IMU Signals](https://arxiv.org/abs/2604.18372)

**<font color=#1a73e8>作者：</font>** Meheru Zannat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parkinson's disease (PD) is a chronic neurodegenerative disease. It shows multiple motor symptoms such as tremor, bradykinesia, postural instability, freezing of gait (FoG). PD is currently diagnosed clinically through physical exam by health-care professionals, which can be time consuming and highly subjective. Wearable IMU sensors has become a promising gateway for passive monitoring of PD patients. We propose a self-supervised cross-attention encoder that processes bilateral wrist-worn IMU signals from a public dataset called PADS, consisting of three groups, PD (Parkinson Disease), HC (Healthy Control) and DD (Differential Diagnosis) of a total of 469 subjects. We have achieved a mean accuracy of 93.12% for HC vs. PD classification and 87.04% for PD vs. DD classification. The results emphasize the clinical challenge of distinguishing Parkinson's from other neurodegenerative diseases. Self-supervised representation learning using contrastive infoNCE loss gained an accuracy of 93.56% for HC vs. PD and 92.50% for PD vs. DD using only 20% of labelled data. This demonstrates the effectiveness of our method in transfer learning for clinical use with minimal labels. The real-time applicability was tested by deploying the optimized model with a mean inference time of 48.32 ms per window on a Raspberry Pi CPU.

---


### 489. [IceBreaker for Conversational Agents: Breaking the First-Message Barrier with Personalized Starters](https://arxiv.org/abs/2604.18375)

**<font color=#1a73e8>作者：</font>** Hongwei Zheng, Weiqi Wu, Zhengjia Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational agents, such as ChatGPT and Doubao, have become essential daily assistants for billions of users. To further enhance engagement, these systems are evolving from passive responders to proactive companions. However, existing efforts focus on activation within ongoing dialogues, while overlooking a key real-world bottleneck. In the conversation initiation stage, users may have a vague need but no explicit query intent, creating a first-message barrier where the conversation holds before it begins. To overcome this, we introduce Conversation Starter Generation: generating personalized starters to guide users into conversation. However, unlike in-conversation stages where immediate context guides the response, initiation must operate in a cold-start moment without explicit user intent. To pioneer in this direction, we present IceBreaker that frames human ice-breaking as a two-step handshake: (i) evoke resonance via Resonance-Aware Interest Distillation from session summaries to capture trigger interests, and (ii) stimulate interaction via Interaction-Oriented Starter Generation, optimized with personalized preference alignment and a self-reinforced loop to maximize engagement. Online A/B tests on one of the world's largest conversational agent products show that IceBreaker improves user active days by +0.184% and click-through rate by +9.425%, and has been deployed in production.

---


### 490. [Forecasting Ionospheric Irregularities on GNSS Lines of Sight Using Dynamic Graphs with Ephemeris Conditioning](https://arxiv.org/abs/2604.18379)

**<font color=#1a73e8>作者：</font>** Mert Can Turkmen, Eng Leong Tan, Yee Hui Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most data-driven ionospheric forecasting models operate on gridded products, which do not preserve the time-varying sampling structure of satellite-based sensing. We instead model the ionosphere as a dynamic graph over ionospheric pierce points (IPPs), with connectivity that evolves as satellite positions change. Because satellite trajectories are predictable, the graph topology over the forecast horizon can be constructed in advance. We exploit this property to condition forecasts on the future graph structure, which we term ephemeris conditioning. This enables prediction on lines of sight that appear only in the forecast horizon. We evaluate our framework on multi-GNSS (Global Navigation Satellite System) data from a co-located receiver pair in Singapore spanning January 2023 through April 2025. The task is to forecast Rate of TEC Index (ROTI)-defined irregularities at 5-minute cadence up to 2 hours ahead as binary probabilistic classification per node. The resulting model, IonoDGNN, achieves a Brier Skill Score (BSS) of 0.49 and a precision-recall area under the curve (PR-AUC) of 0.75, improving over persistence by 35\% in BSS and 52\% in PR-AUC, with larger gains at longer lead times. Ablations confirm that graph structure and ephemeris conditioning each contribute meaningfully, with conditioning proving essential for satellites that rise during the forecast horizon (receiver operating characteristic AUC: 0.95 vs.\ 0.52 without). Under simulated coverage dropout, the model retains predictive skill on affected nodes through spatial message passing from observed neighbors. These results suggest that dynamic graph forecasting on evolving lines of sight is a viable alternative to grid-based representations for ionospheric irregularity forecasting. The model and evaluation code will be released upon publication.

---


### 491. [The implicated scientist: on the role of AI researchers in the development of weapons systems](https://arxiv.org/abs/2604.18380)

**<font color=#1a73e8>作者：</font>** Alexandra Volokhova, Alex Hernandez-Garcia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) technologies are increasingly used in modern weapons systems. Notably, these systems have recently been involved in mass killings and destruction at scale. Furthermore, there is currently a strong interest and competition among powerful players to accelerate the proliferation of weapons with automated or AI-based components, a phenomenon known as AI arms race. This competition poses a risk of causing even more deaths and devastation in the future, as well as increased power and wealth inequality. In this work, we aim to shed light on the role of AI researchers as implicated subjects in the harms caused by weapons enabled by AI technologies. We investigate and discuss the specifics of this implication and explore ways to transfigure this position of implication into one of differentiated, long-distance solidarity with the victims of technologically fortified injustices.

---


### 492. [Understanding the Prompt Sensitivity](https://arxiv.org/abs/2604.18389)

**<font color=#1a73e8>作者：</font>** Yang Liu, Chenhui Chu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt sensitivity, which refers to how strongly the output of a large language model (LLM) depends on the exact wording of its input prompt, raises concerns among users about the LLM's stability and reliability. In this work, we consider LLMs as multivariate functions and perform a first-order Taylor expansion, thereby analyzing the relationship between meaning-preserving prompts, their gradients, and the log probabilities of the model's next token. We derive an upper bound on the difference between log probabilities using the Cauchy-Schwarz inequality. We show that LLMs do not internally cluster similar inputs like smaller neural networks do, but instead disperse them. This dispersing behavior leads to an excessively high upper bound on the difference of log probabilities between two meaning-preserving prompts, making it difficult to effectively reduce to 0. In our analysis, we also show which types of meaning-preserving prompt variants are more likely to introduce prompt sensitivity risks in LLMs. In addition, we demonstrate that the upper bound is strongly correlated with an existing prompt sensitivity metric, PromptSensiScore. Moreover, by analyzing the logit variance, we find that prompt templates typically exert a greater influence on logits than the questions themselves. Overall, our results provide a general interpretation for why current LLMs can be highly sensitive to prompts with the same meaning, offering crucial evidence for understanding the prompt sensitivity of LLMs. Code for experiments is available at this https URL.

---


### 493. [Randomly Initialized Networks Can Learn from Peer-to-Peer Consensus](https://arxiv.org/abs/2604.18390)

**<font color=#1a73e8>作者：</font>** Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In self-supervised learning, self-distilled methods have shown impressive performance, learning representations useful for downstream tasks and even displaying emergent properties. However, state-of-the-art methods usually rely on ensembles of complex mechanisms, with many design choices that are empirically motivated and not well understood.
In this work, we explore the role of self-distillation within learning dynamics. Specifically, we isolate the effect of self-distillation by training a group of randomly initialized networks, removing all other common components such as projectors, predictors, and even pretext tasks. Our findings show that even this minimal setup can lead to learned representations with non-trivial improvements over a random baseline on downstream tasks. We also demonstrate how this effect varies with different hyperparameters and present a short analysis of what is being learned by the models under this setup.

---


### 494. [One-Step Diffusion with Inverse Residual Fields for Unsupervised Industrial Anomaly Detection](https://arxiv.org/abs/2604.18393)

**<font color=#1a73e8>作者：</font>** Boan Zhang, Wen Li, Guanhua Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved outstanding performance in unsupervised industrial anomaly detection (uIAD) by learning a manifold of normal data under the common assumption that off-manifold anomalies are harder to generate, resulting in larger reconstruction errors in data space or lower probability densities in the tractable latent space. However, their iterative denoising and noising nature leads to slow inference. In this paper, we propose OSD-IRF, a novel one-step diffusion with inverse residual fields, to address this limitation for uIAD task. We first train a deep diffusion probabilistic model (DDPM) on normal data without any conditioning. Then, for a test sample, we predict its inverse residual fields (IRF) based on the noise estimated by the well-trained parametric noise function of the DDPM. Finally, uIAD is performed by evaluating the probability density of the IRF under a Gaussian distribution and comparing it with a threshold. Our key observation is that anomalies become distinguishable in this IRF space, a finding that has seldom been reported in prior works. Moreover, OSD-IRF requires only single step diffusion for uIAD, thanks to the property that IRF holds for any neighboring time step in the denoising process. Extensive experiments on three widely used uIAD benchmarks show that our model achieves SOTA or competitive performance across six metrics, along with roughly a 2X inference speedup without distillation.

---


### 495. [Capturing Monetarily Exploitable Vulnerability in Smart Contracts via Auditor Knowledge-Learning Fuzzing](https://arxiv.org/abs/2604.18395)

**<font color=#1a73e8>作者：</font>** Bowen Cai, Weiheng Bai, Hangyun Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart contracts extended blockchain functionality beyond simple transactions, powering complex applications like decentralized finance (DeFi). However, this complexity introduces serious security challenges, including price manipulation and inflation attacks. Despite the development of various security tools, the rapid rise in financially motivated exploits continues to pose a significant threat to the blockchain ecosystem. These financially motivated exploits often stem from Monetarily Exploitable Vulnerabilities (MEVuls), which refer to vulnerabilities arising from exploitable implementations in monetary transactions or value-transfer logic. Due to their complexity, intricate chains of function calls, multifaceted logic, and diverse manifestations across different smart contracts, MEVuls are particularly challenging for current security tools to identify. Instead of providing actionable insights, existing tools frequently generate excessive warnings that overwhelm developers without effectively mitigating risks. To address the challenge of recognizing MEVuls, we first formalize MEVuls based on common real-world financial exploits. Then, we introduce FAUDITOR, a specialized fuzzer designed to detect MEVuls in smart contracts. The key insight is that leveraging smart contracts' finance-related interfaces directly exposes critical vulnerabilities, making detection more targeted. We further integrate auditors' reports using NLP to extract valuable insights on exploitation patterns, enabling a more informed search strategy. Additionally, FAUDITOR employs a self-learning mechanism that refines its detection strategies over time, allowing it to improve based on prior fuzzing results. In our evaluation, FAUDITOR impressively reveals 220 zero-day MEVuls. Meanwhile, compared to existing fuzzers, FAUDITOR detects vulnerabilities faster and achieves better instruction coverage.

---


### 496. [AlphaContext: An Evolutionary Tree-based Psychometric Context Generator for Creativity Assessment](https://arxiv.org/abs/2604.18398)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Yue Huang, Hong Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creativity has become a core competence in the era of LLMs and human-AI collaboration, underpinning innovation in real-world problem solving. Crucially, the systematic improvement of creativity necessitates scientifically valid assessment instruments. Psychometric research recognizes context-based assessment as an effective way to measure creative thinking. However, high-quality expert-designed contexts remain scarce. Existing LLM-based generators often struggle with insufficient assessment cues, weak narrative coherence, limited stylistic diversity, and poor support for creative thinking. To address these challenges, we propose AlphaContext, an evolutionary tree-based psychometric context generator for creativity assessment. First, the HyperTree Outline Planner formalizes expert-designed outlining as a rule-guided hypertree and performs top-down hierarchical planning. The MCTS-based Context Generator fills the outline via MCTS to balance global structure and local quality. Then, the Evolutionary Context Optimizer evolves contexts with MAP-Elites by repeatedly updating niche elites to jointly improve diversity and quality. Finally, the Assessment-Guided Evolution Refiner simulates virtual participants with diverse styles and recycles weak contexts for further evolution. Experiments show that AlphaContext yields an average improvement of 8% over competitive methods across 6 quality metrics.

---


### 497. [Bridge-Centered Metapath Classification Using R-GCN-VGAE for Disaster-Resilient Maintenance Decisions](https://arxiv.org/abs/2604.18399)

**<font color=#1a73e8>作者：</font>** Takato Yasuno  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Daily infrastructure management in preparation for disasters is critical for urban resilience. When bridges remain resilient against disaster-induced external forces, access to hospitals, shops, and residences via metapaths can be sustained, maintaining essential urban functions. However, prioritizing bridge maintenance under limited budgets requires quantifying the multi-dimensional roles that bridges play in disaster scenarios -- a challenge that existing single-indicator approaches fail to address. We focus on metapaths from national highways through bridges to buildings (hospitals, shops, residences), constructing a heterogeneous graph with road, bridge, and building layers. A Relation-centric Graph Convolutional Network Variational Autoencoder (R-GCN-VGAE) learns metapath-based feature representations, enabling classification of bridges into disaster-preparedness categories: Supply Chain (commercial logistics), Medical Access (emergency healthcare), and Residential Protection (preventing isolation). Using OSMnx and open data, we validate our methodology on three diverse cities in Ibaraki Prefecture, Japan: Mito (697 bridges), Chikusei (258 bridges), and Moriya (148 bridges), totaling 1,103 bridges. The heterogeneous graph construction from open data enables redefining bridge roles for disaster scenarios, supporting maintenance budget decision-making. We contributed that (1) Open-data methodology for constructing urban heterogeneous graphs. (2) Redefinition of bridge roles for disaster scenarios via metapath-based classification. (3) Establishment of maintenance budget decision support methodology. (4) k-NN tuning strategy validated across diverse city scales. (5) Empirical demonstration of UMAP superiority over t-SNE/PCA for multi-role bridge visualization.

---


### 498. [Balance-Guided Sparse Identification of Multiscale Nonlinear PDEs with Small-coefficient Terms](https://arxiv.org/abs/2604.18414)

**<font color=#1a73e8>作者：</font>** Zhenhua Dang, Lei Zhang, Long Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven discovery of governing equations has advanced significantly in recent years; however, existing methods often struggle in multiscale systems where dynamically significant terms may have small coefficients. Therefore, we propose Balance-Guided SINDy (BG-SINDy) inspired by the principle of dominant balance, which reformulates $\ell_0$-constrained sparse regression as a term-level $\ell_{2,0}$-regularized problem and solves it using a progressive pruning strategy. Terms are ranked according to their relative contributions to the governing equation balance rather than their absolute coefficient magnitudes. Based on this criterion, BG-SINDy alternates between least-squares regression and elimination of negligible terms, thereby preserving dynamically significant terms even when their coefficients are small. Numerical experiments on the Korteweg--de Vries equation with a small dispersion coefficient, a modified Burgers equation with vanishing hyperviscosity, a modified Kuramoto--Sivashinsky equation with multiple small-coefficient terms, and a two-dimensional reaction--diffusion system demonstrate the validity of BG-SINDy in discovering small-coefficient terms. The proposed method thus provides an efficient approach for discovering governing equations that contain small-coefficient terms.

---


### 499. [BhashaSutra: A Task-Centric Unified Survey of Indian NLP Datasets, Corpora, and Resources](https://arxiv.org/abs/2604.18423)

**<font color=#1a73e8>作者：</font>** Raghvendra Kumar, Devankar Raj, Sriparna Saha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> India's linguistic landscape, spanning 22 scheduled languages and hundreds of marginalized dialects, has driven rapid growth in NLP datasets, benchmarks, and pretrained models. However, no dedicated survey consolidates resources developed specifically for Indian languages. Existing reviews either focus on a few high-resource languages or subsume Indian languages within broader multilingual settings, limiting coverage of low-resource and culturally diverse varieties. To address this gap, we present the first unified survey of Indian NLP resources, covering 200+ datasets, 50+ benchmarks, and 100+ models, tools, and systems across text, speech, multimodal, and culturally grounded tasks. We organize resources by linguistic phenomena, domains, and modalities; analyze trends in annotation, evaluation, and model design; and identify persistent challenges such as data sparsity, uneven language coverage, script diversity, and limited cultural and domain generalization. This survey offers a consolidated foundation for equitable, culturally grounded, and scalable NLP research in the Indian linguistic ecosystem.

---


### 500. [Scalable Physics-Informed Neural Differential Equations and Data-Driven Algorithms for HVAC Systems](https://arxiv.org/abs/2604.18438)

**<font color=#1a73e8>作者：</font>** Hanfeng Zhai, Hongtao Qiao, Hassan Mansour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a scalable, data-driven simulation framework for large-scale heating, ventilation, and air conditioning (HVAC) systems that couples physics-informed neural ordinary differential equations (PINODEs) with differential-algebraic equation (DAE) solvers. At the component level, we learn heat-exchanger dynamics using an implicit PINODE formulation that predicts conserved quantities (refrigerant mass $M_r$ and internal energy $E_\text{hx}$) as outputs, enabling physics-informed training via automatic differentiation of mass/energy balances. Stable long-horizon prediction is achieved through gradient-stabilized latent evolution with gated architectures and layer normalization. At the system level, we integrate learned components with DAE solvers (IDA and DASSL) that explicitly enforce junction constraints (pressure equilibrium and mass-flow consistency), and we use Bayesian optimization to tune solver parameters for accuracy--efficiency trade-offs. To reduce residual system-level bias, we introduce a lightweight corrector network trained on short trajectory segments. Across dual-compressor and scaled network studies, the proposed approach attains multi-fold speedups over high-fidelity simulation while keeping errors low (MAPE below a few percent) and scales to systems with up to 32 compressor--condenser pairs.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-535](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
