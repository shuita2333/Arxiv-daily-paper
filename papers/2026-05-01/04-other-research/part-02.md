# 📦 其他研究 | 2026年05月01日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-173](./part-04.md)

---

### 51. [HOI-aware Adaptive Network for Weakly-supervised Action Segmentation](https://arxiv.org/abs/2604.26227)

**<font color=#1a73e8>作者：</font>** Runzhong Zhang, Suchen Wang, Yueqi Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose an HOI-aware adaptive network named AdaAct for weakly-supervised action segmentation. Most existing methods learn a fixed network to predict the action of each frame with the neighboring frames. However, this would result in ambiguity when estimating similar actions, such as pouring juice and pouring coffee. To address this, we aim to exploit temporally global but spatially local human-object interactions (HOI) as video-level prior knowledge for action segmentation. The long-term HOI sequence provides crucial contextual information to distinguish ambiguous actions, where our network dynamically adapts to the given HOI sequence at test time. More specifically, we first design a video HOI encoder that extracts, selects, and integrates the most representative HOI throughout the video. Then, we propose a two-branch HyperNetwork to learn an adaptive temporal encoder, which automatically adjusts the parameters based on the HOI information of various videos on the fly. Extensive experiments on two widely-used datasets including Breakfast and 50Salads demonstrate the effectiveness of our method under different evaluation metrics.

---


### 52. [Comparative Analysis of AutoML and BiLSTM Models for Cyberbullying Detection on Indonesian Instagram Comments](https://arxiv.org/abs/2604.26229)

**<font color=#1a73e8>作者：</font>** Raihana Adelia Putri, Aisyah Musfirah, Anggi Puspita Ningrum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study compares machine learning and deep learning approaches for cyberbullying detection in Indonesian-language Instagram comments. Using a balanced dataset of 650 comments labeled as Bullying and Non-Bullying, the study evaluates Naive Bayes, Logistic Regression, and Support Vector Machine with TF-IDF features, as well as BiLSTM and BiLSTM with Bahdanau Attention. A preprocessing pipeline tailored to informal Indonesian text is applied, including slang normalization, stopword removal, and stemming. The results show that Logistic Regression performs best among the machine learning models, while BiLSTM with Attention achieves the strongest overall deep learning performance. The findings highlight the value of domain-specific preprocessing and show that although deep learning captures contextual patterns more effectively, machine learning remains a competitive option for resource-constrained deployments.

---


### 53. [DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232)

**<font color=#1a73e8>作者：</font>** Junhu Fu, Ke Chen, Weidong Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable medical video generation has achieved remarkable progress, but it still lacks interpretability, which requires the alignment of generated contents with physical priors and faithful clinical manifestations. To push the boundaries from mere controllability to interpretability, we propose DepthPilot, the first interpretable framework for colonoscopy video generation. This work takes a step toward trustworthy generation through two synergistic paradigms. To achieve explicit geometric grounding, DepthPilot devises a prior distribution alignment strategy, injecting depth constraints into the diffusion backbone via parameter-efficient fine-tuning to ensure anatomical fidelity. To enhance intrinsic nonlinear modeling under these geometric constraints, DepthPilot employs an adaptive spline denoising module, replacing fixed linear weights with learnable spline functions to capture complex spatio-temporal dynamics. Extensive evaluations across three public datasets and in-house clinical data confirm DepthPilot's robust ability to produce physically consistent videos. It achieves FID scores below 15 across all benchmarks and ranks first in clinician assessments, bridging the gap between "visually realistic" and "clinically interpretable". Moreover, DepthPilot-generated videos are expected to enable reliable 3D reconstruction, facilitating surgical navigation and blind region identification, and serve as a foundation toward the colorectal world model.

---


### 54. [LATTICE: Evaluating Decision Support Utility of Crypto Agents](https://arxiv.org/abs/2604.26235)

**<font color=#1a73e8>作者：</font>** Aaron Chan, Tengfei Li, Tianyi Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce LATTICE, a benchmark for evaluating the decision support utility of crypto agents in realistic user-facing scenarios. Prior crypto agent benchmarks mainly focus on reasoning-based or outcome-based evaluation, but do not assess agents' ability to assist user decision-making. LATTICE addresses this gap by: (1) defining six evaluation dimensions that capture key decision support properties; (2) proposing 16 task types that span the end-to-end crypto copilot workflow; and (3) using LLM judges to automatically score agent outputs based on these dimensions and tasks. Crucially, the dimensions and tasks are designed to be evaluable at scale using LLM judges, without relying on ground truth from expert annotators or external data sources. In lieu of these dependencies, LATTICE's LLM judge rubrics can be continually audited and updated given new dimensions, tasks, criteria, and human feedback, thus promoting reliable and extensible evaluation. While other benchmarks often compare foundation models sharing a generic agent framework, we use LATTICE to assess production-level agents used in actual crypto copilot products, reflecting the importance of orchestration and UI/UX design in determining agent quality. In this paper, we evaluate six real-world crypto copilots on 1,200 diverse queries and report breakdowns across dimensions, tasks, and query categories. Our experiments show that most of the tested copilots achieve comparable aggregate scores, but differ more significantly on dimension-level and task-level performance. This pattern suggests meaningful trade-offs in decision support quality: users with different priorities may be better served by different copilots than the aggregate rankings alone would indicate. To support reproducible research, we open-source all LATTICE code and data used in this paper.

---


### 55. [Apriori-based Analysis of Learned Helplessness in Mathematics Tutoring: Behavioral Patterns by Level, Intervention, and Outcome](https://arxiv.org/abs/2604.26237)

**<font color=#1a73e8>作者：</font>** John Paul P. Miranda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study applied the Apriori algorithm to analyze behavioral interaction patterns associated with learned helplessness (LH) in mathematics tutoring system logs. Interaction data were examined across three dimensions: LH level (low vs. high), system-based intervention (with vs. without), and problem-solving outcomes (solved vs. unsolved). The analysis of the complete dataset showed that skipping problems without using hints was the most frequent pattern linked to unsolved outcomes, while persistence behaviors such as not skipping were less dominant overall. Comparisons by LH level showed that low-LH students had stronger links between problem solving and not skipping, as well as positive associations between hint use and solved outcomes. High-LH students showed more avoidance patterns, with skipping strongly tied to unsolved outcomes. In the comparison of system-based intervention conditions, students without intervention had the highest lift for persistence-success links, while the with-intervention group had stronger patterns involving skipping behaviors leading to unsolved outcomes. Outcome-specific analysis showed that not skipping was consistently associated with solved problems across all groups, while skipping without hints predicted unsolved outcomes. Practical implications and recommendations are discussed.

---


### 56. [EnerGS: Energy-Based Gaussian Splatting with Partial Geometric Priors](https://arxiv.org/abs/2604.26238)

**<font color=#1a73e8>作者：</font>** Rui Song, Tianhui Cai, Markus Gross 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has been widely adopted for scene reconstruction, where training inherently constitutes a highly coupled and non-convex optimization problem. Recent works commonly incorporate geometric priors, such as LiDAR measurements, either for initialization or as training constraints, with the goal of improving photometric reconstruction quality. However, in large-scale outdoor scenarios, such geometric supervision is often spatially incomplete and uneven, which limits its effectiveness as a reliable prior and can even be detrimental to the final reconstruction. To address this challenge, we model partially observable geometry as a continuous energy field induced by geometric evidence and propose EnerGS. Rather than enforcing geometry as a hard constraint, EnerGS provides a soft geometric guidance for the optimization of Gaussian primitives, allowing geometric information to steer the optimization process without directly restricting the solution space. Extensive experiments on large-scale outdoor scenes demonstrate that, under both sparse multi-view and monocular settings, EnerGS consistently improves photometric quality and geometric stability, while effectively mitigating overfitting during 3DGS training.

---


### 57. [Camera-RFID Fusion for Robust Asset Tracking in Forested Environments](https://arxiv.org/abs/2604.26241)

**<font color=#1a73e8>作者：</font>** John Hateley, Sriram Narasimhan, Omid Abari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Passive RFID tags offer a cost-effective and scalable solution for tracking numerous deployed assets. However, in forested environments, signal attenuation and multipath effects generally limit RFID spatial accuracy to the meter level. Conversely, while cameras employing stereo vision can achieve centimeter-level precision, relying solely on computer vision fails to resolve issues arising from spatial association ambiguity and partial occlusions in dense settings. Fusing these modalities allows systems to harness the high-accuracy benefits of vision while retaining the robust, non-line-of-sight identification advantages of RFID. Yet, a primary challenge in achieving this, which is the central focus of this paper, lies in accurately associating the disparate trajectories generated by these two sensors. To overcome this limitation, we introduce a novel camera--RFID fusion framework that integrates depth and object information with advanced trajectory-matching algorithms. By successfully bridging the meter-to-centimeter accuracy gap, the proposed approach helps achieve reliable tag localization even when assets temporarily leave the camera's field of view. To the best of our knowledge, this represents the first application of camera--RFID fusion for asset tracking in natural forested environments.

---


### 58. [StratMem-Bench: Evaluating Strategic Memory Use in Virtual Character Conversation Beyond Factual Recall](https://arxiv.org/abs/2604.26243)

**<font color=#1a73e8>作者：</font>** Yerong Wu, Tianxing Wu, Minghao Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Achieving realistic human-like conversation for virtual characters requires not only a simple memorization and recall of past events, but also the strategic utilization of memory to meet factual needs and social engagement. Current memory utilization relevant (e.g., memory-augmented generation, long-term dialogue, and etc.) benchmarks overlook this nuance, treating memory primarily as a static repository of facts rather than a dynamic resource to be strategically deployed in dialogues. To address this gap, we design StratMem-Bench, a new benchmark to evaluate strategic memory use in character-centric dialogues. This dataset comprises 657 instances where virtual characters must navigate heterogeneous memory pools containing required, supportive, and irrelevant memories. We also propose a framework with different evaluation metrics including Strict Memory Compliance, Memory Integration Quality, Proactive Enrichment Score and Conditional Irrelevance Rate, to evaluate strategic memory use capabilities of virtual characters. Experiments on StratMem-Bench which leverage the state-of-the-art large language models as virtual characters show that all models perform well at distinguishing between required and irrelevant memories, but struggle once supportive memories are introduced into the decision process.

---


### 59. [MetaSR: Content-Adaptive Metadata Orchestration for Generative Super-Resolution](https://arxiv.org/abs/2604.26244)

**<font color=#1a73e8>作者：</font>** Jiaqi Guo, Mingzhen Li, Haohong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study generative super-resolution (SR) in real-world scenarios where content and degradations vary across domains, genres, and segments. For example, images and videos may alternate between text overlays, fast motion, smooth cartoons, and low-light faces, each benefiting from different forms of side information. Existing metadata-guided SR methods typically use a fixed conditioning design, which is suboptimal when useful cues are content dependent and transmission budgets are limited. We propose MetaSR, a Diffusion Transformer (DiT)-based framework that selects and injects task-relevant metadata to guide SR under resource constraints. Specifically, we use the DiT's own VAE and transformer backbone to fuse heterogeneous metadata, and adopt an efficient distillation strategy that enables one-step diffusion inference. Experiments across diverse content buckets and degradation regimes show that MetaSR outperforms reference solutions by up to 1.0~dB PSNR while achieving up to 50\% transmission bitrate saving at matched quality. We assess these gains under a rate--distortion optimization (RDO) framework that jointly accounts for sender-side bitrate and receiver/display quality metrics (e.g., PSNR and SSIM).

---


### 60. [Beyond Shortcuts: Mitigating Visual Illusions in Frozen VLMs via Qualitative Reasoning](https://arxiv.org/abs/2604.26250)

**<font color=#1a73e8>作者：</font>** Hao Guo, Fei Wang, Junjie Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Vision-Language Models (VLMs) have achieved state-of-the-art performance in general visual tasks, their perceptual robustness remains remarkably brittle when confronted with optical illusions. These failures are often attributed to shortcut heuristics, where models prioritize linguistic priors and memorized prototypes over direct visual evidence. In this work, we propose Structured Qualitative Inference (SQI), a training-free, data-centric framework designed to fortify visual grounding in frozen VLMs. SQI addresses perceptual anomalies through three systematic modules: (1) Axiomatic Constraint Injection, which suppresses erroneous metric estimations and quantitative hallucinations; (2) Hierarchical Scene Decomposition, which decouples target visual manifolds from complex background distractors; and (3) Counterfactual Self-Verification, an adversarial reasoning step that mitigates confirmation bias. By orchestrating these qualitative constraints at inference time, SQI effectively aligns high-level linguistic reasoning with low-level visual perception. Our framework was evaluated on the DataCV 2026 Challenge (Task I: Classic Illusion Understanding), where it ranked 2nd place overall. Experimental results demonstrate that SQI not only significantly enhances accuracy across diverse illusion categories but also provides superior diagnostic interpretability without any model fine-tuning. Our success underscores the potential of structured qualitative grounding as a robust paradigm for developing next-generation, illusion-resistant vision-language systems.

---


### 61. [Multi-Stage Bi-Atrial Segmentation Framework from 3D Late Gadolinium-Enhanced MRI using V-Net Family Models](https://arxiv.org/abs/2604.26251)

**<font color=#1a73e8>作者：</font>** Hao Wen, Jingsu Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We report our multi-stage framework designed for the problem of multi-class bi-atrial segmentation from 3D late gadolinium-enhanced (LGE) MRI of the human heart. The pipeline consists of a preprocessing step using multidimensional contrast limited adaptive histogram equalization (MCLAHE); coarse region segmentation from MCLAHE-enhanced and down-sampled MRI using a V-Net family model; and fine segmentation from the coarse region using another V-Net model. Asymmetric loss is adopted to optimize the model weights.

---


### 62. [OmniTrend: Content-Context Modeling for Scalable Social Popularity Prediction](https://arxiv.org/abs/2604.26252)

**<font color=#1a73e8>作者：</font>** Liliang Ye, Guiyi Zeng, Yunyao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting social media popularity requires understanding both the intrinsic appeal of content and the external context that determines how it is exposed to users. Existing methods focus on content signals but do not separate them from exposure-related patterns, which causes the learned representations to absorb platform-specific visibility effects and weakens both interpretability and cross-platform transfer. This paper introduces OmniTrend, a unified framework that models popularity as the joint outcome of content attractiveness and contextual exposure. The content module learns cross-modal representations from visual, audio, and textual cues to quantify intrinsic appeal, while the context module estimates exposure from exogenous signals such as posting time, author activity, topical trends, and retrieval-based neighborhood statistics. OmniTrend learns separate predictors for content attractiveness and contextual exposure and integrates them in the final popularity estimate, which makes the role of each factor explicit and supports robust transfer across image and video platforms.

---


### 63. [GaitKD: A Universal Decoupled Distillation Framework for Efficient Gait Recognition](https://arxiv.org/abs/2604.26255)

**<font color=#1a73e8>作者：</font>** Yuqi Li, Qian Zhou, Huiran Duan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition is an attractive biometric modality for long-range and contact-free identification, but high-performing gait models often rely on deep and computationally expensive architectures that are difficult to deploy in practice. Knowledge distillation (KD) offers a natural way to transfer knowledge from a powerful teacher to an efficient student; however, standard KD is often less effective for part-structured gait models, where supervision is formed from both part-wise classification logits and part-wise retrieval embeddings. In this paper, we propose GaitKD, a distillation framework that decouples gait knowledge transfer into two complementary components: decision-level distillation and boundary-level distillation. Specifically, GaitKD aligns the teacher and student through part-calibrated logit distillation to transfer inter-class decision relations, while preserving the teacher-induced partitioning of the embedding space through an activation-boundary objective instead of direct feature regression. With a simple aligned part-wise design, GaitKD supports heterogeneous teacher-student gait models without introducing additional inference cost. Experimental results across multiple gait recognition benchmarks and teacher-student configurations show consistent improvements over strong gait baselines. Our study demonstrates that the two transfer components are complementary, and boundary-preserving distillation provides more stable performance than direct feature regression. Source code is available at this https URL

---


### 64. [Semantic Foam: Unifying Spatial and Semantic Scene Decomposition](https://arxiv.org/abs/2604.26262)

**<font color=#1a73e8>作者：</font>** Amr Sharafeldin, Shrisudhan Govindarajan, Thomas Walker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern scene reconstruction methods, such as 3D Gaussian Splatting, enable photo-realistic novel view synthesis at real-time speeds. However, their adoption in interactive graphics applications remains limited due to the difficulty of interacting with these representations compared to traditional, human-authored 3D assets. While prior work has attempted to impose semantic decomposition on these models, significant challenges remain in segmentation quality and cross-view this http URL address these limitations, we introduce Semantic Foam, which extends the recently proposed Radiant Foam representation to semantic decomposition tasks. Our approach leverages the inherent spatial structure of Radiant Foam's volumetric Voronoi mesh and augments it with an explicit semantic feature field defined at the cell level. This design enables direct spatial regularization, improving consistency across views and mitigating artifacts caused by occlusion and inconsistent supervision, which are common issues in point-based this http URL results demonstrate that our method achieves superior object-level segmentation performance compared to state-of-the-art approaches such as Gaussian Grouping and this http URL page: this http URL

---


### 65. [Calibrated Surprise: An Information-Theoretic Account of Creative Quality](https://arxiv.org/abs/2604.26269)

**<font color=#1a73e8>作者：</font>** Bo Zou, Chao Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The essence of good creative writing is calibrated surprise: when constraints from all relevant dimensions act together, the feasible solution space collapses into a narrow region, and the surviving choices look least predictable from an unconstrained view. "Calibrated" has a precise meaning: the author's intent, the reader's reasonable expectation, and the logic of reality converge. When these three independent judgements agree on every dimension, the set of admissible writing choices is forced into a very small region. A mathematical corollary follows: full-dimensional accuracy and mediocrity are mutually exclusive -- two sides of one constraint structure, not separate goals.
We use Shannon's mutual information $I(X;Y) = H(X) - H(X|Y)$ as our analysis tool. "Calibrated" corresponds to conditional entropy going to zero; "surprise" to entropy going up; mutual information is the precise measure of the joint quantity. The argument rests on two pillars. Static: when constraints from ethos, mythos, lexis, and dianoia are imposed together, the admissible set collapses sharply, and surviving solutions show up as low-probability choices from an unconstrained view. Dynamic: the chain rule shows each writing choice is constrained by what came before and constrains what comes after; macro-level decisions naturally contribute a larger share of information, removing the need for hand-tuned weighting.
Through case studies and lightweight LLM-logprob computations, we show the framework is both analytically useful and operational, laying the theoretical groundwork for Creative Quality Alignment (CQA) and a professional evaluation benchmark.

---


### 66. [Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents](https://arxiv.org/abs/2604.26274)

**<font color=#1a73e8>作者：</font>** Hung Dang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Structured-workflow agents driven by large language models execute tool calls against sensitive external environments. We propose \codename, a telemetry-driven behavioral anomaly detection firewall. Drawing on sequence-based intrusion detection, \codename\ compiles verified benign tool-call telemetry into a parameterized deterministic finite automaton (pDFA). The model defines permitted tool sequences, sequential contexts, and parameter bounds. At runtime, a lightweight gateway enforces these boundaries via an $O(1)$ state-transition structural lookup, shifting computationally expensive analysis entirely offline. Evaluated on the Agent Security Bench (ASB), \codename\ achieves a 5.6\% macro-averaged attack success rate (ASR) across five scenarios. Within three structured workflows, ASR drops to 2.2\%, outperforming Aegis, a state-of-the-art stateless scanner, at 12.8\%. \codename\ achieves 0\% ASR on multi-step and context-sequential attacks in structured settings. Furthermore, against 1,000 algorithmically spliced exfiltration payloads, only 1.4\% matched valid structural paths, all of which failed end-to-end string parameter guards (0 successes out of 14 surviving paths, 95\% CI [0\%, 23.2\%]). \codename\ introduces just 2.2~ms of per-call latency (a 3.7$\times$ speedup over \textsc{Aegis}) while maintaining a 2.0\% benign task failure rate (BTFR) on benign workloads. Modeling the behavioral trajectory effectively collapses the available attack surface, but unmaintained continuous parameter bounds remain vulnerable to synonym-substitution attacks (18\% evasion rate). Thus, exact-match whitelisting of sensitive parameters ultimately bears the final defensive load against execution.

---


### 67. [High-Dimensional Noise to Low-Dimensional Manifolds: A Manifold-Space Diffusion Framework for Degraded Hyperspectral Image Classification](https://arxiv.org/abs/2604.26279)

**<font color=#1a73e8>作者：</font>** Boxiang Yang, Ning Chen, Xia Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, Hyperspectral Image (HSI) classification has attracted increasing attention in remote sensing. However, HSI data are inherently high-dimensional but low-rank, with discriminative information concentrated on a low-dimensional latent manifold. In real-world remote sensing scenarios, the superposition of multiple degradation factors disrupts this intrinsic manifold structure, driving samples away from their original low-dimensional distribution and introducing substantial redundant and non-discriminative variations. To better handle this challenge, this paper proposes a manifold-space diffusion framework (MSDiff) for robust hyperspectral classification under complex degradation conditions. Specifically, the proposed method first maps high-dimensional, degradation-affected HSI data into a compact low-dimensional manifold through a discriminative spectral-spatial reconstruction task, preserving class semantics and reducing redundant variations. A diffusion-based generative model is then applied to regularize the spectral-spatial distribution within the manifold, enabling progressive refinement and stabilization of latent features against residual degradations. The key advantage of the proposed framework lies in performing diffusion-based distribution modeling directly on the low-dimensional manifold, effectively decoupling degradation-induced disturbances from intrinsic discriminative structures and enhancing representation stability under complex degradations. Experimental results on multiple hyperspectral benchmarks demonstrate consistent performance improvements over state-of-the-art methods under diverse composite degradation settings. The code will be available at this https URL

---


### 68. [MedSynapse-V: Bridging Visual Perception and Clinical Intuition via Latent Memory Evolution](https://arxiv.org/abs/2604.26283)

**<font color=#1a73e8>作者：</font>** Chunzheng Zhu, Jiaqi Zeng, Junyu Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-precision medical diagnosis relies not only on static imaging features but also on the implicit diagnostic memory experts instantly invoke during image interpretation. We pinpoint a fundamental cognitive misalignment in medical VLMs caused by discrete tokenization, leading to quantization loss, long-range information dissipation, and missing case-adaptive expertise. To bridge this gap, we propose ours, a framework for latent diagnostic memory evolution that simulates the experiential invocation of clinicians by dynamically synthesizing implicit diagnostic memories within the model's hidden stream. Specifically, it begins with a Meta Query for Prior Memorization mechanism, where learnable probes retrieve structured priors from an anatomical prior encoder to generate condensed implicit memories. To ensure clinical fidelity, we introduce Causal Counterfactual Refinement (CCR), which leverages reinforcement learning and counterfactual rewards derived from region-level feature masking to quantify the causal contribution of each memory, thereby pruning redundancies and aligning latent representations with diagnostic logic. This evolutionary process culminates in Intrinsic Memory Transition (IMT), a privileged-autonomous dual-branch paradigm that internalizes teacher-branch diagnostic patterns into the student-branch via full-vocabulary divergence alignment. Comprehensive empirical evaluations across multiple datasets demonstrate that ours, by transferring external expertise into endogenous parameters, significantly outperforms existing state-of-the-art methods, particularly chain-of-thought paradigms, in diagnostic accuracy.

---


### 69. [Event-based Liveness Detection using Temporal Ocular Dynamics: An Exploratory Approach](https://arxiv.org/abs/2604.26285)

**<font color=#1a73e8>作者：</font>** Nicolas Mastropasqua, Ignacio Bugueno-Cordova, Rodrigo Verschae 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face liveness detection has been extensively studied using RGB cameras, achieving strong performance under controlled conditions but often failing to generalize across sensors and attack scenarios. In this work, we explore event cameras as an alternative sensing modality for liveness detection based on temporal ocular dynamics. Event cameras capture sparse, asynchronous changes in brightness with microsecond resolution, enabling precise analysis of fast eye movements such as saccades. Replay attacks cannot faithfully reproduce these dynamics due to temporal resampling and display artifacts, leading to distinctive spatio-temporal patterns in the event domain. We design a data collection protocol to extend RGBE-Gaze with replay-attack recordings, yielding an event-based fake counterpart for liveness detection. We analyze event-driven temporal features from eye regions and evaluate their effectiveness for ocular motion segmentation and liveness classification. Our results show that event-based representations enable reliable discrimination between genuine and replayed sequences, achieving up to 95.37% top-1 accuracy with a spiking convolutional neural network. These preliminary findings highlight the potential of event-based sensing for robust and low-latency liveness detection.

---


### 70. [Folding Tensor and Sequence Parallelism for Memory-Efficient Transformer Training & Inference](https://arxiv.org/abs/2604.26294)

**<font color=#1a73e8>作者：</font>** Vasu Shyam, Anna Golubeva, Quentin Anthony  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present tensor and sequence parallelism (TSP), a parallel execution strategy that folds tensor parallelism and sequence parallelism onto a single device axis. In conventional multi-dimensional parallelism layouts, tensor parallelism (TP) shards model weights while sequence parallelism (SP) shards tokens, reducing per-device parameter or activation memory, respectively. Traditionally, each scheme is assigned its own mesh dimension. TSP instead assigns each rank both a weight shard and a sequence shard, reducing both parameter and activation memory along the same device axis. We implement this design with two runtime schedules. For attention, ranks iterate over broadcast parameter shards and reconstruct context through a sequence-wise key/value exchange. For gated MLPs, weight shards circulate in a ring while partial outputs accumulate locally. By sharding both weights and activations across the same devices, TSP trades additional communication volume for reduced memory overhead. We provide a theoretical communication and memory analysis, describe our implementation of TSP attention and gated MLP blocks, and benchmark TSP against TP, SP, and TP+SP. These results position TSP as a hardware-aware alternative for long-context and memory-constrained model training, and as a viable axis of parallelism in concert with existing parallelism schemes such as pipeline and expert parallelism for dense and mixture-of-expert models.

---


### 71. [NeuroPlastic: A Plasticity-Modulated Optimizer for Biologically Inspired Learning Dynamics](https://arxiv.org/abs/2604.26297)

**<font color=#1a73e8>作者：</font>** Douglas Jiang, Yuechen Wang, Jiayi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization algorithms are fundamental to modern deep learning, yet most widely used methods rely on update rules based primarily on local gradient statistics. We introduce NeuroPlastic, a plasticity-modulated optimizer that augments gradient-based updates with an adaptive multi-signal modulation mechanism inspired by multi-factor synaptic plasticity, a concept from neurobiology. NeuroPlastic dynamically scales gradient updates using interacting components that capture gradient, activity-like, and memory-like statistics, forming a lightweight modulation layer compatible with standard deep learning training pipelines. Across image classification benchmarks, NeuroPlastic consistently improves over a controlled gradient-only ablation, with more pronounced gains on the Fashion-MNIST benchmark and in reduced-data regimes. In transfer experiments on CIFAR-10 with ResNet-18, the method remains stable and competitive without retuning. These results suggest that multi-signal plasticity-inspired modulation can provide a useful extension to conventional gradient-driven optimization, particularly when learning signals are limited or noisy, and offer a promising direction for gradient-based methods in deep learning.

---


### 72. [Cheeger--Hodge Contrastive Learning for Structurally Robust Graph Representation Learning](https://arxiv.org/abs/2604.26301)

**<font color=#1a73e8>作者：</font>** Mengyang Zhao, Longlong Li, Cunquan Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Contrastive Learning (GCL) has emerged as a prominent framework for unsupervised graph representation learning. However, relying on augmentation design alone to define the invariances learned by GCL can be brittle under structural perturbations. To address this issue, we propose Cheeger--Hodge Contrastive Learning (CHCL), a framework that aligns a perturbation-stable Cheeger--Hodge joint signature across augmented views for robust graph representation learning. The proposed signature combines a Cheeger-inspired connectivity signature derived from the algebraic connectivity \(\lambda_2\) with the low-frequency spectrum of the 1-Hodge Laplacian, thereby capturing both global connectivity and higher-order structural information. By aligning encoder representations with the proposed Cheeger--Hodge joint signature across augmented views, CHCL learns graph embeddings that are robust to local structural perturbations. Extensive experiments on standard benchmarks, transfer settings demonstrate that CHCL consistently improves performance, robustness, and generalization.

---


### 73. [Towards Low-Cost Low-Power Activity-Aware Soil Moisture Sensing Platform for Large-scale Farming](https://arxiv.org/abs/2604.26303)

**<font color=#1a73e8>作者：</font>** Jack Thoene, Omar Kamil, Thekra Alkadee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deep understanding of a field's soil moisture content is the leading indicator for predicting crop yields and making data driven decisions for irrigation and application of topical chemicals for drought resilience. Despite this importance, the cost of adopting and maintaining IoT infrastructure prevents modern farms from employing widespread real time soil moisture sensors. We present an end-to-end platform of buried battery-free sensor nodes and a mobile basestation that leverages the farmer's daily routine for data retrieval. Each node features a self-powered galvanic soil-moisture probe, employing a high impedance analog front end to enable durability. Operating entirely on harvested solar energy for up to 21 days on a single capacitor charge, each node collects soil moisture, temperature, and environment condition data. Using a predictable finite-state machine, handshake-based data exchanges occur with a basestation affixed to standard farming vehicles designed to listen for the nodes while moving through the farm. Our platform organizes all sensor, link-quality, and location data into an easy-to-interpret dashboard to seamlessly integrate with the farmer's everyday routine. Costing less than $35, the platform is a financially accessible, accurate, and easily scalable platform that enables persistent, regular data collection from the most rural plots without adding to or impeding farming operations. Experimental evaluation demonstrates reliable communication over 1 km at 2 dBm transmit power, stable sensor readings over 70 days of indoor operation, and continuous data recovery during multiple periods of intermittent connection.

---


### 74. [Towards a Frugal Photosynthesis Sensing Toolkit for Data-Driven Plant Science Education and Exploration](https://arxiv.org/abs/2604.26305)

**<font color=#1a73e8>作者：</font>** Qitong Li, Raj Nileshbhai Dave, Rhema Amanda Phiri 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Rapid environmental change and advances in data-driven analysis highlight the need not only to use computational tools, but also to foster understanding of the natural world and inspire creativity. Photosynthesis, the process that fuels nearly all life on Earth, provides a compelling context for such learning, particularly in understanding how plants alter their photosynthetic strategies in response to environmental changes. However, existing tools for studying photosynthesis are often inaccessible or limited to demonstrating its presence, rather than capturing its temporal dynamics. We present PhytoBits, a frugal in situ gas-exchange sensing toolkit for distinguishing and teaching photosynthetic strategies. PhytoBits combines leaf enclosure with accessible materials, an off-the-shelf CO\textsubscript{2} sensor, and a low-cost microcontroller, to support multi-day monitoring of plant gas-exchange in educational and research contexts. We validated PhytoBits against research-grade gas-exchange systems, confirming that it identifies C\textsubscript{3} and CAM (Crassulacean Acid Metabolism) photosynthetic pathways. In addition to obligate CAM, PhytoBits also resolves facultative CAM and developmental CAM dynamics in plants. This work presents an early-stage hardware validation; user deployment studies, open-source code dissemination, and automated pathway classification are planned as future work.

---


### 75. [Benchmarking PyCaret AutoML Against BiLSTM for Fine-Grained Emotion Classification: A Comparative Study on 20-Class Emotion Detection](https://arxiv.org/abs/2604.26310)

**<font color=#1a73e8>作者：</font>** Arya Muda Siregar, Arielva Simon Siahaan, Haikal Fransisko Simbolon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-grained emotion classification, which identifies specific emotional states such as happiness, anger, sadness, and fear, remains a challenging task in natural language processing. This study benchmarks classical machine learning and deep learning approaches for 20-class emotion classification using the 20-Emotion Text Classification Dataset containing 79,595 English sentences. On the machine learning side, Logistic Regression, Multinomial Naive Bayes, and Support Vector Machine are evaluated using TF-IDF features. On the deep learning side, Bidirectional Long Short-Term Memory, Gated Recurrent Unit, and a lightweight Transformer implemented in PyTorch are compared. The results show that BiLSTM achieves the best overall performance with 89% accuracy and a weighted F1-score of 0.89, slightly outperforming the best machine learning model, SVM, which reaches 88.11% accuracy. The findings indicate that while traditional machine learning models remain competitive and computationally efficient, sequence-based deep learning models better capture contextual emotional cues in text.

---


### 76. [DreamProver: Evolving Transferable Lemma Libraries via a Wake-Sleep Theorem-Proving Agent](https://arxiv.org/abs/2604.26311)

**<font color=#1a73e8>作者：</font>** Youyuan Zhang, Jialiang Sun, Hangrui Bi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce DreamProver, an agentic framework that leverages a "wake-sleep" program induction paradigm to discover reusable lemmas for formal theorem proving. Existing approaches either rely on fixed lemma libraries, which limit adaptability, or synthesize highly specific intermediate lemmas tailored to individual theorems, thereby lacking generality. DreamProver addresses this gap through an iterative two-stage process. In the wake stage, DreamProver attempts to prove theorems from a training set using the current lemma library while proposing new candidate lemmas. In the "sleep" stage, it abstracts, refines, and consolidates these candidates to compress and optimize the library. Through this alternating cycle, DreamProver progressively evolves a compact set of high-level, transferable lemmas that can be effectively used to prove unseen theorems in related domains. Experimental results demonstrate that DreamProver substantially improves proof success rates across a diverse set of mathematical benchmarks, while also producing more concise proofs and reducing computational cost.

---


### 77. [Classification of Public Opinion on the Free Nutritional Meal Program on YouTube Media Using the LSTM Method](https://arxiv.org/abs/2604.26312)

**<font color=#1a73e8>作者：</font>** Berliana Enda Putri, Lisa Diani Amelia, Muhammad Zaky Zaiddan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public opinion towards the Free Nutritious Meal Program (MBG) on YouTube social media reflects diverse community responses. This study applies the Long Short-Term Memory (LSTM) method to classify sentiments from 7,733 YouTube comments. The results show that the LSTM model achieves 89% accuracy, with strong performance on negative sentiment (F1-score 0.94) but weaker performance on positive sentiment (F1-score 0.55) due to class imbalance, as negative data account for 87.7% of the dataset. These findings confirm the effectiveness of LSTM for sentiment analysis of Indonesian text while highlighting the challenge of imbalanced data. This research contributes to social media-based public policy evaluation

---


### 78. [The Unseen Adversaries: Robust and Generalized Defense Against Adversarial Patches](https://arxiv.org/abs/2604.26317)

**<font color=#1a73e8>作者：</font>** Vishesh Kumar, Akshay Agarwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The vulnerabilities of deep neural networks against singularities have raised serious concerns regarding their deployment in the physical world. One of the most prominent and impactful physical-world adversarial perturbations is the attachment of patches to clean images, known as an adversarial patch attack. Similarly, natural noises such as Gaussian and Salt\&Pepper are highly prevalent in the real world. The current research need arises from the above vulnerabilities and the lack of efforts to tackle these two singularities independently and, especially, in combination. In this research, we have, for the first time, combined these two prominent singularities and proposed a novel dataset. Using this dataset, we have conducted a benchmark study of singularity data-point detection using features from several convolutional neural networks. For classification, rather than the popular neural network-based parameter tuning, we have used traditional yet effective machine learning classifiers. The extensive experiments across various in- and out-of-distribution (OOD) singularities reveal several interesting findings about the effectiveness of classifiers and show that it is hard to defend against adversaries when they are treated independently, and inefficient classifiers are selected.

---


### 79. [Point Cloud Registration via Probabilistic Self-Update Local Correspondence and Line Vector Sets](https://arxiv.org/abs/2604.26318)

**<font color=#1a73e8>作者：</font>** Kuo-Liang Chung, Yu-Cheng Lin, Wu-Chi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud registration (PCR) is a fundamental task for integrating 3D observations in remote sensing applications. This paper proposes a fast and effective PCR algorithm utilizing probabilistic self-updating local correspondence and line vector sets. Our dual RANSAC interaction model comprises a global RANSAC evaluating the global correspondence set and a local RANSAC operating on dynamically updated local sets. Initially, these local sets are constructed using angle histogram statistics and line vector length preservation techniques. To improve accuracy, a probabilistic self-updating strategy refines the local sets after each interaction round. To reduce runtime, we introduce a global early termination condition that optimally balances accuracy and efficiency. Finally, a weighted singular value decomposition estimates the registration solution. Evaluations on public datasets demonstrate our algorithm achieves superior time efficiency and at least a 10% root mean square error improvement over state-of-the-art methods. The C++ source code is publicly available at this https URL.

---


### 80. [Motion-Driven Multi-Object Tracking of Model Organisms in Space Science Experiments](https://arxiv.org/abs/2604.26321)

**<font color=#1a73e8>作者：</font>** Jianing You, Han Wang, Kang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated animal behavior analysis relies on long-term, interpretable individual trajectories; however, multi-animal tracking in space science experimental videos remains highly challenging due to weak appearance cues, low-quality imaging, complex maneuvering behaviors, and frequent interactions. To address this problem, we first construct the SpaceAnimal-MOT dataset to characterize the motion complexity and long-term identity preservation challenges in biological videos acquired under microgravity conditions. We then propose ART-Track (Adaptive Robust Tracking), a motion-driven tracking framework tailored to this setting. Specifically, multi-model motion estimation is introduced to handle abrupt maneuvers and nonlinear motion, motion-state-driven association is designed to reduce identity switches under dense interactions and temporary mismatch, and uncertainty-adaptive fusion is used to dynamically balance spatial and motion cues when prediction reliability varies. Experimental results show that ART-Track significantly reduces identity switches on zebrafish and fruitfly sequences, while maintaining more stable association under occlusion, deformation, and high-density interactions, thereby providing a more reliable tracking foundation for downstream quantitative behavior analysis. The code is publicly available at this https URL.

---


### 81. [Federated Medical Image Classification under Class and Domain Imbalance exploiting Synthetic Sample Generation](https://arxiv.org/abs/2604.26324)

**<font color=#1a73e8>作者：</font>** Martina Pavan, Matteo Caligiuri, Francesco Barbato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Exploiting deep learning in medical imaging faces critical challenges, including strict privacy constraints, heterogeneous imaging devices with varying acquisition properties, and class imbalance due to the uneven prevalence of pathologies. In this work, we propose FedSSG, a novel Federated Learning framework that addresses domain shifts caused by diverse imaging devices while mitigating the under-representation of rare pathologies. The key contribution is a strategy for generating synthetic samples and distributing them across clients to improve coverage of both underrepresented pathologies and imaging devices. Experimental results demonstrate that our approach significantly enhances model performance and generalization across heterogeneous institutions, with minimal computational overhead at the client side.

---


### 82. [AlphaJet: Automated Conceptual Aircraft Synthesis via Disentangled Generative Priors and Topology-Preserving Evolutionary Search](https://arxiv.org/abs/2604.26337)

**<font color=#1a73e8>作者：</font>** Boris Kriuk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conceptual aircraft design is traditionally an expert-mediated iterative process in which a human designer proposes a configuration, runs low-order physics, inspects the result, and re-proposes. We present AlphaJet, an end-to-end automated synthesis pipeline that closes this loop. From a textual mission specification (mass, range, cruise speed, hard size envelope, engine count, areal density) AlphaJet evolves a feasible 3D aircraft in real time, scored by a transparent multi-disciplinary fitness function covering aerodynamics, structures, weights, stability, packaging, and geometric mount consistency. Three contributions distinguish our approach: (i) an Anatomically-Disentangled Variational Autoencoder (AD-VAE) whose first 25 latent dimensions are supervised to align with named anatomical parameters, providing an interpretable shape prior; (ii) a topology-elitist genetic algorithm that protects the best individual from each of five tail topologies and triggers stagnation restarts, preventing premature collapse to a single configuration; and (iii) mount-aware geometric scoring that computes signed penetration between engines and other structural parts, eliminating the redundant artifacts common in generative aircraft models. The full loop runs interactively on a CPU and streams every generation to a browser viewer, making it a practical real-world automation tool for early-phase design-space exploration.

---


### 83. [Can Cross-Layer Design Bridge Security and Efficiency? A Robust Authentication Framework for Healthcare Information Exchange Systems](https://arxiv.org/abs/2604.26339)

**<font color=#1a73e8>作者：</font>** Khalid M. Ezzat, Muhammad El-Saba, Mahmoud A. Shawky  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As healthcare systems become increasingly interconnected, ensuring secure and continuous device authentication in health information exchange (HIE) networks is critical to safeguarding patient data and clinical operations. In this context, this paper proposes a novel cross-layer authentication scheme for HIE networks that integrates cryptographic mechanisms with physical (PHY) layer-based authentication to ensure reliable communication while minimizing computational and communication overheads. The initial authentication phase leverages a traditional public key infrastructure (PKI)-based approach, employing elliptic curve cryptography (ECC) and digital certificates to verify the legitimacy of communicating devices. Simultaneously, it extracts unique hardware-level features such as carrier frequency offset (CFO) and quadrature skewness from the devices. These features are then used to train a machine learning (ML) model during an offline phase managed by a regional centralized authority (RCA). For re-authentication, the system re-extracts these PHY-layer features from incoming orthogonal frequency division multiplexing (OFDM) symbols and verifies the device identity in real-time using the trained ML classifier. This cross-layer strategy enables continuous, lightweight identity verification without the need to exchange and validate cryptographic signatures for each message, thereby reducing system overhead. The proposed scheme further enhances privacy through the use of encrypted, frequently refreshed pseudo-identities, ensuring unlinkability and resistance to identity tracking. A formal security analysis using Burrows-Abadi-Needham (BAN) logic demonstrates the scheme's robustness against various threats, including impersonation, man-in-the-middle (MitM), replay, and Sybil attacks.

---


### 84. [SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness](https://arxiv.org/abs/2604.26341)

**<font color=#1a73e8>作者：</font>** Haiyi Qiu, Kaihang Pan, Jiacheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent unified image generation models have achieved remarkable success by employing MLLMs for semantic understanding and diffusion backbones for image generation. However, these models remain fundamentally limited in spatially-aware tasks due to a lack of intrinsic spatial understanding and the absence of explicit geometric guidance during generation. In this paper, we propose SpatialFusion, a novel framework that internalizes 3D geometric awareness into unified image generation models. Specifically, we first employ a Mixture-of-Transformers (MoT) architecture to augment the MLLM with a parallel spatial transformer to enhance 3D geometric modeling capability. By sharing self-attention with the MLLM, the spatial transformer learns to derive metric-depth maps of target images from rich semantic contexts. These explicit geometric scaffolds are then injected into the diffusion backbone through a specialized depth adapter, providing precise spatial constraints for spatially-coherent image generation. Through a progressive two-stage training strategy, SpatialFusion significantly enhances performance on spatially-aware benchmarks, notably outperforming leading models such as GPT-4o. Additionally, it achieves generalized performance gains across both text-to-image generation and image editing scenarios, all while maintaining negligible inference overhead.

---


### 85. [Which Face and Whose Identity? Solving the Dual Challenge of Deepfake Proactive Forensics in Multi-Face Scenarios](https://arxiv.org/abs/2604.26342)

**<font color=#1a73e8>作者：</font>** Lei Zhang, Zhiqing Guo, Dan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlike single-face forgeries, deepfakes in complex multi-person interaction scenarios (such as group photos and multi-person meetings) more closely reflect real-world threats. Although existing proactive forensics solutions demonstrate good performance, they heavily rely on a "single-face" setting, making it difficult to effectively address the problems of deepfake localization and source tracing in complex multi-person environments. To address this challenge, we propose the Deep Attributable Watermarking Framework (DAWF). This framework adopts a novel multi-face encoder-decoder architecture that bypasses the cumbersome offline pre-processing steps of traditional forensics, facilitating efficient in-network parallel watermark embedding and cross-face collaborative processing. Crucially, we propose a selective regional supervision loss. This innovative mechanism guides the decoder to focus exclusively on the facial regions tampered with by deepfakes. Leveraging this mechanism alongside the embedded identity payloads, DAWF realizes the "which + who" goal, answering the dual questions of which facial region was forged and who was forged. Extensive experiments on challenging multi-face datasets show that DAWF achieves excellent deepfake localization and traceability in complex multi-person scenes.

---


### 86. [ACPO: Anchor-Constrained Perceptual Optimization for Diffusion Models with No-Reference Quality Guidance](https://arxiv.org/abs/2604.26348)

**<font color=#1a73e8>作者：</font>** Yang Yang, Feifan Meng, Han Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have achieved remarkable success in image generation, yet their training is predominantly driven by full-reference objectives that enforce pixel-wise similarity to ground-truth this http URL supervision, while effective for fidelity, may insufficient in terms of subjective visual perception quality and text-image semantic consistency. In this work, we investigate the problem of incorporating no-reference perceptual quality into diffusion training. A key challenge is that directly optimizing perceptual signals, such as those provided by no-reference image quality assessment (NR-IQA) models, introduces a mismatch with the original diffusion objective, leading to training instability and distributional drift during fine-tuning. To address this issue, we propose an anchor-constrained optimization framework that enables stable perceptual adaptation. Specifically, we leverage a learned NR-IQA model as a perceptual guidance signal, while introducing an anchor-based regularization that enforces consistency with the base diffusion model in terms of noise prediction. This design effectively balances perceptual quality improvement and generative fidelity, allowing controlled adaptation toward perceptually favorable outputs without compromising the original generative behavior. Extensive experiments demonstrate that our method consistently enhances perceptual quality while preserving generation diversity and training stability, highlighting the effectiveness of anchor-constrained perceptual optimization for diffusion models.

---


### 87. [UIGaze: How Closely Can VLMs Approximate Human Visual Attention on User Interfaces?](https://arxiv.org/abs/2604.26352)

**<font color=#1a73e8>作者：</font>** Min Song, Yoonseong Lee, Yeonhu Seo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) have demonstrated strong capabilities in understanding visual content, yet their ability to predict where humans look on user interfaces remains unexplored. We present UIGaze, a study investigating how closely VLMs can approximate human visual attention on user interfaces using real eye-tracking data. Using the UEyes dataset - comprising 1,980 UI screenshots across four categories (webpage, desktop, mobile, poster) with eye-tracking data from 62 participants - we evaluate nine state-of-the-art VLMs through a zero-shot coordinate prediction pipeline. Each model generates gaze point coordinates that are converted into saliency maps via Gaussian blurring and compared against ground truth using CC, SIM, and KL divergence. Our experiments (1,980 images x 9 models x 3 runs x 3 durations) reveal that VLMs achieve moderate alignment with human gaze patterns, with the degree of alignment varying significantly across UI types and improving with longer viewing durations - suggesting VLMs capture exploratory gaze patterns rather than initial fixations. All code, predictions, and evaluation results are publicly available.

---


### 88. [GateMOT: Q-Gated Attention for Dense Object Tracking](https://arxiv.org/abs/2604.26353)

**<font color=#1a73e8>作者：</font>** Mingjin Lv, Zelin Liu, Feifei Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large models demonstrate the strong representational power of vanilla attention, this core mechanism cannot be directly applied to Dense Object Tracking: its quadratic all-to-all interactions are computationally prohibitive for dense motion estimation on high-resolution features. This mismatch prevents Dense Object Tracking from fully leveraging attention-based modeling in crowded and occlusion-heavy scenes. To address this challenge, we introduce GateMOT, an online tracking framework centered on Q-Gated Attention (Q-Attention), an efficient and spatially aware attention variant. Our key idea is to repurpose the Query from a similarity-conditioning term into a learnable gating unit. This Gating-Query (Gating-Q) produces a probabilistic gate that modulates Key features in an element-wise manner, enabling explicit relevance selection instead of costly global aggregation. Built on this mechanism, parallel Q-Attention heads transform one shared feature map into task-specific yet consistent representations for detection, motion, and re-identification, yielding a tightly coupled multi-task decoder with linear-complexity gating operations. GateMOT achieves state-of-the-art HOTA of 48.4, MOTA of 67.8, and IDF1 of 64.5 on BEE24, and demonstrates strong performance on additional Dense Object Tracking benchmarks. These results show that Q-Attention is a simple, effective, and transferable building block for attention-based tracking in dense tracking scenarios.

---


### 89. [Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking](https://arxiv.org/abs/2604.26360)

**<font color=#1a73e8>作者：</font>** Disha Singha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) systems typically optimize scalar reward functions that assume precise and reliable evaluation of outcomes. However, real-world objectives--especially those derived from human preferences--are often uncertain, context-dependent, and internally inconsistent. This mismatch can lead to alignment failures such as reward hacking, over-optimization, and overconfident behavior.
We introduce a dual-source uncertainty-aware reward framework that explicitly models both epistemic uncertainty in value estimation and uncertainty in human preferences. Model uncertainty is captured via ensemble disagreement over value predictions, while preference uncertainty is derived from variability in reward annotations. We combine these signals through a confidence-adjusted Reliability Filter that adaptively modulates action selection, encouraging a balance between exploitation and caution.
Empirical results across multiple discrete grid configurations (6x6, 8x8, 10x10) and high-dimensional continuous control environments (Hopper-v4, Walker2d-v4) demonstrate that our approach yields more stable training dynamics and reduces exploitative behaviors under reward ambiguity, achieving a 93.7% reduction in reward-hacking behavior as measured by trap visitation frequency. We demonstrate statistical significance of these improvements and robustness under up to 30% supervisory noise, albeit with a trade-off in peak observed reward compared to unconstrained baselines.
By treating uncertainty as a first-class component of the reward signal, this work offers a principled approach toward more reliable and aligned reinforcement learning systems.

---


### 90. [Text Style Transfer with Machine Translation for Graphic Designs](https://arxiv.org/abs/2604.26361)

**<font color=#1a73e8>作者：</font>** Deergh Singh Budhauria, Sanyam Jain, Rishav Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Globalization of graphic designs such as those used in marketing materials and magazines is increasingly important for communication to broad audiences. To accomplish this, the textual content in the graphic designs needs to be accurately translated and have the text styling preserved in order to fit visually into the design. Preserving text styling requires high accuracy word alignment between the original and the translated text. The problem of word alignment between source and translated text is long known. The industry standards for extracting word alignments are defined by Giza++ and attention probabilities from neural machine translation (NMT) models. In this paper, we explore three new methods to tackle the word alignment problem for transferring text styles from the source to the translated text. The proposed methods are developed on top of commercially available NMT and LLM translation technologies. They include: NMT with custom input and output tags for text styling; LLM with custom input and output tags; a hybrid with NMT for translation followed by an LLM with use of unigram mappings. To analyze the performance of these solutions, their alignment results are compared with the results of an attention head approach to gauge their usability in graphic design applications. Interestingly, the attention head strong baseline proves more accurate than the LLM or NMT approach and on par with the hybrid NMT+LLM approach.

---


### 91. [CO-EVO: Co-evolving Semantic Anchoring and Style Diversification for Federated DG-ReID](https://arxiv.org/abs/2604.26363)

**<font color=#1a73e8>作者：</font>** Fengchun Zhang, Qiang Ma, Liuyu Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated domain generalization for person re-identification (FedDG-ReID) aims to collaboratively train a pedestrian retrieval model across multiple decentralized source domains such that it can generalize to unseen target environments without compromising raw data privacy. However, this task is significantly challenged by the inherent stylistic gaps across decentralized clients. Without global supervision, models easily succumb to shortcut learning where representations overfit to domain specific camera biases rather than universal identity features. We propose CO-EVO, a novel federated framework that resolves this semantic-style conflict through a co-evolutionary mechanism. On the semantic side, Camera-Invariant Semantic Anchoring (CSA) learns identity prompts with cross-camera consistency to establish purified and domain-agnostic anchors that filter out local imaging noise. On the visual side, Global Style Diversification (GSD), powered by a Global Camera-Style Bank (GCSB), synthesizes realistic perturbations to expand the visual boundaries of training data. The core of CO-EVO is its co-evolutionary loop where purified anchors act as gravitational centers to guide the image encoder toward robust anatomical attributes amidst diverse style variations. Extensive experiments demonstrate that CO-EVO achieves state-of-the-art (SOTA) performance, proving that the synergy between semantic purification and style expansion is essential for robust cross-domain generalization. Our code is available at: this https URL.

---


### 92. [Beyond Fixed Formulas: Data-Driven Linear Predictor for Efficient Diffusion Models](https://arxiv.org/abs/2604.26365)

**<font color=#1a73e8>作者：</font>** Zhirong Shen, Rui Huang, Jiacheng Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To address the high sampling cost of Diffusion Transformers (DiTs), feature caching offers a training-free acceleration method. However, existing methods rely on hand-crafted forecasting formulas that fail under aggressive skipping. We propose L2P (Learnable Linear Predictor), a simple data-driven caching framework that replaces fixed coefficients with learnable per-timestep weights. Rapidly trained in ~20 seconds on a single GPU, L2P accurately reconstructs current features from past trajectories. L2P significantly outperforms existing baselines: it achieves a 4.55x FLOPs reduction and 4.15x latency speedup on FLUX.1-dev, and maintains high visual fidelity under up to 7.18x acceleration on Qwen-Image models, where prior methods show noticeable quality degradation. Our results show learning linear predictors is highly effective for efficient DiT inference. Code is available at this https URL.

---


### 93. [Seamless Indoor-Outdoor Mapping for INGENIOUS First Responders](https://arxiv.org/abs/2604.26368)

**<font color=#1a73e8>作者：</font>** Jürgen Wohlfeil, Henry Meißner, Adrian Schischmanow 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In several applications it is desired to have 3D models not only from the outdoor spaces but also from inside the building. In the context of First Responder enhancement in large scale natural and man-made disasters, a method is presented to achieve this goal with a high degree of automation. Therefore an autonomously flying aerial mapping system is combined with a person-carried indoor positioning system. Automatically recognized markers (AprilTags) are geo-referenced by the aerial system and their coordinates are sent to the ground-based system. By looking at the AprilTags before entering the building, the ground-based system is registered to world coordinates. Without the further need of any global positioning, it creates a point cloud from the indoor spaces that fits with the point could from the aerial view. This allows a co-visualization of both point-clouds as a seamless indoor-outdoor 3D model in real time.

---


### 94. [SG-UniBuc-NLP at SemEval-2026 Task 6: Multi-Head RoBERTa with Chunking for Long-Context Evasion Detection](https://arxiv.org/abs/2604.26375)

**<font color=#1a73e8>作者：</font>** Gabriel Stefan, Sergiu Nisioi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe our system for SemEval-2026 Task 6 (CLARITY: Unmasking Political Question Evasions), which classifies English political interview responses by coarse-grained clarity (3-way) and fine-grained evasion strategy (9-way). Since responses frequently exceed the 512-token limit of standard Transformer encoders, we apply an overlapping sliding-window chunking strategy with element-wise Max-Pooling aggregation over chunk representations. A shared RoBERTa-large encoder supplies two task-specific heads trained jointly via a multi-task objective, with inference-time ensembling over 7-fold stratified cross-validation. Our system achieves a Macro-F1 of 0.80 on Subtask 1 and 0.51 on Subtask 2, ranking 11th in both subtasks.

---


### 95. [Unifying Runtime Monitoring Approaches for Safety-Critical Machine Learning: Application to Vision-Based Landing](https://arxiv.org/abs/2604.26411)

**<font color=#1a73e8>作者：</font>** Mathieu Dario, Florent Chenevier, Kévin Delmas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Runtime monitoring is essential to ensure the safety of ML applications in safety-critical domains. However, current research is fragmented, with independent methods emerging from different communities. In this paper, we propose a unified framework categorising runtime monitoring approaches into three distinct types: Operational Design Domain (ODD) monitoring, which ensures compliance with expected operating conditions; Out-of-Distribution (OOD) monitoring, which rejects inputs that deviate from the training data; and Out-of-Model-Scope (OMS) monitoring, which detects anomalous model behaviour based its internal states or outputs. We demonstrate the benefits of this categorization with a dedicated experiment on an aeronautical safety-critical application: runway detection during landing. This framework facilitates design of monitoring activities, with complementary categories of monitors, and enables evaluation and comparison of different monitors using common, safety-oriented metrics.

---


### 96. [When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding?](https://arxiv.org/abs/2604.26412)

**<font color=#1a73e8>作者：</font>** Tianyu Liu, Yuhao Shen, Xinyi Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference, but SOTA hidden-state-based drafters suffer from long-range decay: draft accuracy degrades as the speculative step increases. Existing work attributes this decay to train-inference mismatch and proposes test-time training (TTT) as a remedy, yet we observe that long-range decay persists even in TTT-trained drafters. We revisit long-range decay from the perspective of context information preservation. In hidden-state reuse, we argue the target hidden state acts as a biased context compression: it aggregates historical token information according to the attention query at the current position, yielding a compact representation optimized for immediate next-token prediction. This compression can suppress information less relevant to the current query but important for later speculative steps. In contrast, the target model's KV cache serves as an explicit context, retaining the complete set of token-wise KV representations. We therefore posit the KV-Reuse Hypothesis: allowing the draft model to reuse the target KV cache can provide richer signals for long-horizon drafting. To test this hypothesis, we introduce KVShot, a diagnostic framework that compares three reuse paradigms: hidden-only, KV-only, and hybrid. Extensive evaluations on Qwen3-8B show that KV-Reuse improves long-range acceptance, although end-to-end speedups remain marginal under current training pipelines. Our analysis identifies two key structural bottlenecks: shallow drafters struggle to estimate target queries accurately, and draft-side KV projections receive sparse gradient signals. These findings suggest that realizing the full potential of KV-aware decoding requires moving beyond TTT toward block-wise training paradigms. By exposing these bottlenecks, KVShot provides a foundational diagnostic testbed and a clear roadmap for designing next-generation inference architectures.

---


### 97. [EmoTransCap: Dataset and Pipeline for Emotion Transition-Aware Speech Captioning in Discourses](https://arxiv.org/abs/2604.26417)

**<font color=#1a73e8>作者：</font>** Shuhao Xu, Yifan Hu, Jingjing Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion perception and adaptive expression are fundamental capabilities in human-agent interaction. While recent advances in speech emotion captioning (SEC) have improved fine-grained emotional modeling, existing systems remain limited to static, single-emotion characterization within isolated sentences, neglecting dynamic emotional transitions at the discourse level. To address this gap, we propose Emotion Transition-Aware Speech Captioning (EmoTransCap), a paradigm that integrates temporal emotion dynamics with discourse-level speech description. To construct a dataset rich in emotion transitions while enabling scalable expansion, we design an automated pipeline for dataset creation. This is the first large-scale dataset explicitly designed to capture discourse-level emotion transitions. To generate semantically rich descriptions, we incorporate acoustic attributes and temporal cues from discourse-level speech. Our Multi-Task Emotion Transition Recognition (MTETR) model performs joint emotion transition detection and diarization. Leveraging the semantic analysis capabilities of LLMs, we produce two annotation versions: descriptive and instruction-oriented. These data and annotations offer a valuable resource for advancing emotion perception and emotional expressiveness. The dataset enables speech captions that capture emotional transitions, facilitating temporal-dynamic and fine-grained emotion understanding. We also introduce a controllable, transition-aware emotional speech synthesis system at the discourse level, enhancing anthropomorphic emotional expressiveness and supporting emotionally intelligent conversational agents.

---


### 98. [STLGT: A Scalable Trace-Based Linear Graph Transformer for Tail Latency Prediction in Microservices](https://arxiv.org/abs/2604.26422)

**<font color=#1a73e8>作者：</font>** Yongliang Ding, Qigong Bi, Peng Pu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate end-to-end tail-latency forecasting is critical for proactive SLO management in microservice systems. However, modeling long-range dependency propagation and non-stationary, bursty workloads while maintaining inference efficiency at scale remains challenging. We present STLGT (Scalable Trace-based Linear Graph Transformer), a per-API predictor that encodes traces as span graphs for multi-step p95 tail-latency forecasting. STLGT uses a structure-aware linear graph Transformer to propagate cross-service dependencies with inference time linear in span graph size, and a decoupled temporal module to capture workload dynamics. Across a personalized education microservice application, DeathStarBench, and Alibaba traces, STLGT improves forecasting accuracy over PERT-GNN by 8.5% MAPE on average and achieves up to 12x faster CPU inference at N=32, matching the maximum span graph size after preprocessing the Alibaba traces. Ablation studies further demonstrate the effectiveness of each component, especially under bursty traffic.

---


### 99. [QYOLO: Lightweight Object Detection via Quantum Inspired Shared Channel Mixing](https://arxiv.org/abs/2604.26435)

**<font color=#1a73e8>作者：</font>** Garvit Kumar Mittal, Sahil Tomar, Sandeep Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of object detection architectures has positioned single stage detectors as the dominant solution for real-time visual perception. A primary source of computational overhead in these models lies in the deep backbone stages, where C2f bottleneck modules at high stride levels accumulate a disproportionate share of parameters due to quadratic scaling with channel width. This work introduces QYOLO, a quantum-inspired channel mixing framework that achieves genuine architectural compression by replacing the two deepest backbone C2f modules at P4/16 (512 channels) and P5/32 (1024 channels) with a compact QMixBlock. The proposed block performs global channel recalibration through a sinusoidal mixing mechanism with shared learnable parameters across both backbone stages, enforcing consistent channel importance without requiring independent per-stage parameter sets. The neck and detection head remain fully classical and unchanged. Evaluation on the VisDrone2019 benchmark demonstrates that QYOLOv8n achieves a 20.2% reduction in parameter count (3.01M to 2.40M) and 12.3% GFLOPs reduction with only 0.4 pp mAP@50 degradation. QYOLOv8s achieves 21.8% reduction with 0.1 pp degradation. When combined with knowledge distillation, full accuracy parity is recovered at no cost to compression. An expanded backbone plus neck variant achieved 38 to 41% reduction at the cost of greater accuracy degradation, motivating the backbone-only final design.

---


### 100. [Are Data Augmentation and Segmentation Always Necessary? Insights from COVID-19 X-Rays and a Methodology Thereof](https://arxiv.org/abs/2604.26437)

**<font color=#1a73e8>作者：</font>** Aman Swaraj, Arnav Agarwal, Hitendra Singh Bhadouria 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Rapid and reliable diagnostic tools are crucial for managing respiratory diseases like COVID-19, where chest X-ray analysis coupled with artificial intelligence techniques has proven invaluable. However, most existing works on X-ray images have not considered lung segmentation, raising concerns about their reliability. Additionally, some have employed disproportionate and impractical augmentation techniques, making models less generalized and prone to overfitting. This study presents a critical analysis of both issues and proposes a methodology (SDL-COVID) for more reliable classification of chest X-rays for COVID-19 detection. Methods: We use class activation mapping to obtain a visual understanding of the predictions made by Convolutional Neural Networks (CNNs), validating the necessity of lung segmentation. To analyze the effect of data augmentation, deep learning models are implemented on two levels: one for an augmented dataset and another for a non-augmented dataset. Results: Careful analysis of X-ray images and their corresponding heat maps under expert medical supervision reveals that lung segmentation is necessary for accurate COVID-19 prediction. Regarding data augmentation, test accuracy significantly drops beyond a certain threshold with additional augmented images, indicating model overfitting. Conclusion: Our proposed methodology, SDL-COVID, achieves a precision of 95.21% and a lower false negative rate, ensuring its reliability for COVID-19 detection using chest X-rays.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-173](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
