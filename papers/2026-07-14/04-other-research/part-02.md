# 📦 其他研究 | 2026年07月14日

> 本类共 **147** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-147](./part-03.md)

---

### 51. [DETRAM: End-to-end DEtection, Tracking and Recovery of HumAn Meshes](https://arxiv.org/abs/2607.09089)

**<font color=#1a73e8>作者：</font>** Chunggi Lee, Seonwook Park, Wanhua Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the task of human mesh recovery (HMR), multi-person scenes are particularly difficult to handle due to the many entities that appear and occlusions between them over time. In particular for video inputs, there is a need to track each entity reliably and consistently. Existing methods rely on pretrained human detection modules, increasing their runtime and limiting the number of tracked entities. We present DETRAM, a unified framework for multi-person HMR and tracking that simultaneously detects, reconstructs, and tracks humans across time, both automatically and via user prompts. DETRAM uses a single transformer decoder with an identity-consistent set of learnable query embeddings that persist across frames: detection queries discover new people, tracking queries maintain pose and shape for existing individuals, and prompt queries follow user-specified identities. Our approach achieves state-of-the-art tracking results on PoseTrack21, 3DPW, BEDLAM, and MuPoTS-3D, and competitive reconstruction accuracy on BEDLAM and 3DPW, while uniquely supporting prompt-based tracking of individuals in multi-person scenes. To our knowledge, this is the first method to unify promptability and multi-person HMR with tracking in an end-to-end trainable framework, enabling user-directed human analysis in videos.

---


### 52. [EXHOLD: Experience-Aware Real-Time Hold Control for Large-Scale Ride-Hailing Matching at DiDi](https://arxiv.org/abs/2607.09090)

**<font color=#1a73e8>作者：</font>** Xu Liu, Kai Wan, Zihao Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In large-scale ride-hailing, hold control is a critical mechanism for improving passenger-driver experience. By selectively delaying certain driver-order pairs, the system waits for better opportunities, reduces cancellations, and mitigates wasted driver effort. However, existing industrial hold strategies often rely on heuristic thresholding over multiple predictive models, which can be brittle under non-stationary traffic and hard to optimize for multi-objective experience signals.
We propose EXHOLD, a deployable two-stage framework decoupling experience-aware pair assessment from hold-time execution. In Stage I, we learn a decision model assigning each driver-order pair to discrete, interpretable experience tiers by optimizing a unified objective that aggregates satisfaction signals across the matching funnel. In Stage II, we solve for a monotone hold-time schedule via constrained optimization over empirical quantiles. This explicitly enforces service guardrails bounding the unnecessary holding of promising matches while maximizing overall experience improvement.
We evaluate EXHOLD through randomized A/B experiments in DiDi's production system in Brazil. Results show consistent gains in marketplace efficiency and experience: EXHOLD increases trip completion and driver income, significantly reduces passenger cancellations, and improves funnel efficiency. Ablations and behavioral analyses confirm both stages are essential and that the policy makes calibrated decisions under spatiotemporal heterogeneity. EXHOLD is currently deployed, serving production traffic in Brazil.

---


### 53. [PRecG: Legal Precedent Retrieval with Graph Neural Networks and Rhetorical Role Segmentation](https://arxiv.org/abs/2607.09094)

**<font color=#1a73e8>作者：</font>** Devanshu Verma, Vasudha Bhatnagar, Vikas Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal precedent retrieval is a fundamental task in legal case preparation, planning, litigation strategy, and legal research. Current approaches for automatic precedent retrieval map legal documents to a low-dimensional semantic space and compute similarity based on the proximity of their representations. These approaches treat legal documents as monolithic texts, ignoring the rhetorical organization of the legal technicalities. Ergo, they overlook nuanced legal meanings and fail to distinguish the contextual significance of legal entities and concepts that vary based on their rhetorical roles within the document.
To address this insufficiency, we propose the PRecG pipeline that computes the similarity between pairs of legal judgments by hierarchically learning their representations. The process begins by decomposing each document into distinct semantic units (segments) based on the rhetorical roles of sentences. For each rhetorical segment, a knowledge graph is constructed to capture the legal entities and their relationships within the segment. Contextual representations of the entities are then learned and aggregated to derive segment-level embeddings. These embeddings are further integrated to produce a unified document-level representation, and finally, the semantic similarity between a pair of documents is computed. We validate the performance of the proposed approach through extensive experiments on a benchmark Indian legal dataset, comparing it against state-of-the-art baselines to demonstrate its effectiveness.

---


### 54. [L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning](https://arxiv.org/abs/2607.09099)

**<font color=#1a73e8>作者：</font>** Tan-Minh Nguyen, Hoang-Trung Nguyen, Huu-Dong Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While multi-agent debate (MAD) frameworks have shown significant potential in general reasoning, their effectiveness in highly structured, knowledge-heavy legal domains remains under-explored. In this work, we introduce the Legal Multi-Agent Debate (L-MAD) framework to systematically evaluate different debate structures and aggregation methods within Legal Textual Entailment. By assigning distinct expert personas to multiple agents, L-MAD improves upon strong single-agent baselines by up to 8\%. Furthermore, analyzing how debate scales reveals a clear trade-off: increasing the agent population reduces inconsistency and improves accuracy, whereas extending discussion rounds induces a detrimental \textit{over-deliberation drift} where agents reinforce each other's mistakes. Ultimately, our findings outline the practical boundaries and safety margins of deploying collaborative multi-agent systems in high-stakes legal reasoning environments.

---


### 55. [A Coreset Selection Framework with Ensemble Aggregation for Image Classification](https://arxiv.org/abs/2607.09100)

**<font color=#1a73e8>作者：</font>** Pedro Rocha Dantas, Lucas Pascotti Valem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of image data has produced large-scale datasets, raising concerns about the time and memory costs of model training. Selecting representative training subsets, however, remains challenging: individual sample contributions are unclear, and model behavior varies across datasets and runs. We address these challenges with a framework that combines coreset selection with an ensemble aggregation over multiple runs. For coreset selection, we propose SCOre-Stratified Selection (SCOSS), which partitions the training data into intervals based on a chosen score and samples from each interval. The ensemble combines predictions from multiple runs, each performed on an independently sampled training subset. As baselines, we use moderate and random selection, each in original and class-balanced versions. We assess the framework with Simple Graph Convolution (SGC) and Support Vector Machine (SVM) classifiers under different sampling ratios. Experiments show that SCOSS is competitive with baselines, often the best choice for SGC, and enables favorable trade-offs between accuracy and efficiency. On the fine-grained dataset, SGC with SCOSS outperforms SVMs when using fewer labeled samples. The code and supplementary materials are publicly available at this http URL.

---


### 56. [Equivariant Filter for High Performance Image Tracking using an Event Camera](https://arxiv.org/abs/2607.09103)

**<font color=#1a73e8>作者：</font>** Angus Apps, Yixiao Ge, Timothy L. Molloy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image tracking is the problem of estimating the transformation that relates a moving image of a scene to an original reference image. The problem is important in control of autonomous vehicles or robots, where the image encodes information about the motion of the camera or environment, as well as in pure computer vision applications. In this paper, we present an equivariant filter design for high performance tracking of planar image transformations using an event camera. The design exploits the Asynchronous Event Blob (AEB) tracker (Wang et al., 2024) to extract feature-position measurements from the raw event stream, and an equivariant filter to compute an affine image translation and rotation using the special Euclidean group symmetry. The equivariant filter incorporates an equivalent-measurement update step that de-correlates the (highly temporally correlated) feature-position measurements provided by the AEB tracker. We evaluate the design experimentally using two datasets involving general and fast rotational motion. We benchmark results against direct optimisation (estimating the relative transformation from the raw blob tracks), and a covariance intersection approach for overcoming data correlation. Our design provides smooth image tracking for features moving up to 7000 pixels per second on the image plane.

---


### 57. [Quantum Circuits in Diffusion Models: A Fair-Comparison Study and a Mechanistic Analysis of Angle-Embedding Failures](https://arxiv.org/abs/2607.09108)

**<font color=#1a73e8>作者：</font>** Jaeuk Kim, Sanghoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the integration of variational quantum circuits (VQCs) into diffusion models through a squeeze-and-excitation (SE) channel-modulation scaffold that isolates the quantum contribution. Using a role-matched classical control and multi-seed significance testing across DDPM and latent diffusion on MNIST and CIFAR-10, with a score-based NCSN study on MNIST, we find that quantum cores achieve comparable mean FID to the classical control across DDPM and latent diffusion, while paired sampling-seed tests for EfficientSU2 detect no statistically significant difference. Although the quantum cores use $4.5$--$9\times$ fewer core parameters than the role-matched control, parameter-matched classical controls attain comparable mean FID, so the experiments do not establish a quantum parameter-efficiency advantage. We further identify a structural failure in score-based NCSN: the unbounded score target, proportional to $1/\sigma$, drives angle-embedding inputs far beyond the $2\pi$ period of rotation gates, causing phase aliasing and collapse of the quantum modulator. A bounding transformation, $\theta \leftarrow \pi \tanh(\cdot)$, maps inputs to the non-aliasing domain and substantially improves both quantum cores. Since all circuits are classically simulated at a few-qubit scale, we do not claim quantum advantage. Instead, the study provides a fair-comparison protocol for quantum-enhanced generative models and a mechanistic account of when and why angle embeddings fail.

---


### 58. [Event Stream based Multi-Modal Video Anomaly Detection: A Benchmark Dataset and Algorithms](https://arxiv.org/abs/2607.09114)

**<font color=#1a73e8>作者：</font>** Peipei Zhu, Yueqing Niu, Lin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) is critical for automated surveillance but remains fragile under challenging conditions such as illumination variations, fast motion, and complex backgrounds when relying solely on visible light videos. To address these limitations, we propose EVAD, an event enhanced VAD framework that jointly exploits conventional video and event streams captured by bio inspired event cameras. Event sensors asynchronously capture brightness changes with high temporal resolution, offering robustness to motion blur and extreme lighting, and providing motion salient cues complementary to video based visual information. To support multi modal VAD research, we construct a large scale visible event benchmark comprising 6.3 billion events and 376,368 video frames collected under diverse illumination levels, motion patterns, and background complexities, filling the gap of realistic and scalable datasets for event based anomaly detection. Building upon this dataset, we design a contrastive multi modal pretraining framework to learn discriminative event representations by aligning semantic embeddings across event streams, visible videos, and textual descriptions. An adaptive fusion module then dynamically integrates event based temporal cues with video based spatial semantics, improving robustness to environmental disturbances. Experiments on benchmarks and the proposed TJUTCM Pha dataset demonstrate that E VAD consistently outperforms methods, validating the effectiveness of event-based sensing for VAD in real world scenarios.

---


### 59. [Event Burst Trigger: An Availability Backdoor Attack on Event-Based SNN Object Detection](https://arxiv.org/abs/2607.09115)

**<font color=#1a73e8>作者：</font>** Jaesun Baek, Chanwook Lee, Eun-Kyu Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based vision and spiking neural networks (SNNs) are increasingly adopted for edge intelligence under strict latency and energy constraints. However, the vulnerability of event-based SNN object detection models to availability backdoor attacks remains insufficiently studied. This paper presents Event Burst Trigger (EBT), an availability backdoor attack targeting SNN-based object detection models. EBT injects carefully crafted event-based triggers into the training data, which induce temporally concentrated event streams during inference. These burst-like activations increase the number of phantom (i.e., spurious) object candidates, and consequently inflate the computational cost of the post-processing stage, particularly Non-Maximum Suppression (NMS). We evaluate EBT on SpikeYOLO, the state-of-the-art SNN-based object detector, under a poison-only threat model that does not require modifications to the model architecture, loss function, or inference pipeline. Experimental results show that while detection accuracy remains largely preserved, with mAP@0.5 decreasing by less than 0.099, the latency of the NMS stage increases by up to 38%. This indicates that NMS can become a dominant availability bottleneck in event-based SNN object detection. Experiments on an edge platform further show that the proposed attack elevates baseline resource utilization and reduces scheduling slack without inducing conspicuous peaks in resource usage. In addition, STRIP-based backdoor detection fails to reliably distinguish the proposed attack from benign inputs. These results characterize a previously underexplored availability backdoor threat in event-based SNN object detection systems.

---


### 60. [Power Flow Feasibility Assessment Using Variational Graph Autoencoders](https://arxiv.org/abs/2607.09122)

**<font color=#1a73e8>作者：</font>** Ferran Bohigas-Daranas, Hamid Latif-Martinez, Eduardo Prieto-Araujo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven methods, including graph neural networks, have been studied for accelerating power flow calculations in recent years, but very little attention has been paid to the solution feasibility, which can be obtained by traditional solvers. This paper presents a Variational Graph Autoencoder (VGAE) that detects the power flow solution feasibility, using the IEEE 118-bus case, to assess the validity of the solutions provided by AI-driven solvers.

---


### 61. [4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125)

**<font color=#1a73e8>作者：</font>** Minhyuk Hwang, Sangmin Kim, Seunguk Do 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing volumetric capture of dynamic human performance achieves high fidelity with dense camera arrays. However, in real-world scenarios, only a handful of low-overlap cameras are available, which degrades the output quality and leaves large areas unobserved. Recent 4D reconstruction methods have focused on low-overlap settings, yet they still produce noticeable artifacts in under-observed regions. Video diffusion models have emerged as another option, but they show geometrically inconsistent results for humans. To address these limitations, we propose StudioRecon, a pipeline that reconstructs 4D human scenes from sparse, low-overlap cameras by decoupling background and humans. We densify background supervision by synthesizing hundreds of camera-controlled novel views with a video diffusion model. We also robustly initialize deformable Gaussian humans with cross-view identity association and triangulated multi-view keypoint fitting. Finally, our recursive enhancement module with motion-adaptive consistency injection harmonizes the composed output, thereby further avoiding remaining artifacts. We achieve state-of-the-art novel view synthesis across four real-world datasets and demonstrate applications such as novel trajectory rendering and human replacement.

---


### 62. [IB-Flow: Information Bottleneck-Guided CFG Distillation for Few-Step Text-to-Image Generation](https://arxiv.org/abs/2607.09133)

**<font color=#1a73e8>作者：</font>** Yiting Wang, Jingyi Zhang, Wenhu Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While large-scale text-to-image generative models have achieved unprecedented visual performance, their inherent reliance on multi-step iterative solvers incurs severe inference latency. Few-step distillation targeting the Classifier-Free Guidance (CFG) trajectory has emerged as the prevalent dual-dimensional compression paradigm. However, existing frameworks remain subjugated by a coarse-grained blind injection paradigm that perpetually enforces a globally static guidance strength while indiscriminately sampling the supervisor timestep. This state-agnostic design completely disregards the intrinsic nature of image generation as a dynamic evolutionary process characterized by progressive entropy reduction, which not only restricts the performance boundary of few-step compression but also precipitates severe CFG over-conditioning artifacts. To transcend these limitations, we re-examine the distillation procedure through the theoretical lens of Information Theory, formally modeling it as a dynamic mutual information game constrained by the Information Bottleneck (IB) principle. Specifically, we dismantle traditional blind assumptions via a dual-track adaptive framework. To determine the injection target, we propose an instance-aware selection mechanism that transmutes the intractable KL divergence constraint into a zero-overhead closed-form solution predicated on the local vector field norm. To regulate the injection strength, we introduce an entropy-aware schedule that dynamically decays alongside the SNR, applying maximal thrust for initial structural anchoring before smoothly reverting to the natural manifold to refine micro-details. Extensive empirical evaluations corroborate that our framework fundamentally eradicates over-conditioning artifacts, shattering the performance ceiling to achieve SOTA generative fidelity under extremely stringent 2-step configurations.

---


### 63. [Super-Generalist: Towards Comprehensive and Accurate Medical Image Understanding via Generalist-Specialist Synergy](https://arxiv.org/abs/2607.09135)

**<font color=#1a73e8>作者：</font>** Shaoteng Zhang, Weiwei Cao, Wanxing Chang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical images require comprehensive and accurate interpretation to support the diagnosis of diverse clincial conditions. Recent vision-language generalist models offer broad task coverage and promising zero-shot capabilities, yet often lack fine-grained anatomical and lesion awareness for reliable diagnosis and spatial interpretability. In contrast, supervised specialist models achieve strong performance on specific tasks but typically lack generalization across diseases and anatomies. In this work, we present SuG, a Super-Generalist framework that unifies generalist vision-language learning with specialist objectives, enabling both broad generalization and specialist-level diagnostic capability. We perform specialist-enhanced vision-language alignment in SuG by incorporating spatial priors from multiple segmentation experts, including anatomy, class-specific lesion and class-agnostic lesion segmentors that captures lesions beyond anatomies annotated during training. To improve lesion grounding capability, we leverage lesion masks as spatial priors to calibrate text-conditioned visual attention, encouraging disease-related semantics to focus on clinically relevant regions. We evaluate SuG on extensive chest and abdominal CT benchmarks, including CT-RATE, Merlin, MedVL-CT69K, and several in-house tumor datasets. SuG achieves state-of-the-art performance across a wide range of disease diagnosis tasks and surpasses specialist models on several critical tumor diagnosis benchmarks. Furthermore, SuG demonstrates strong lesion grounding capability, including robust generalization to lesion types lacking class-specific supervision.

---


### 64. [Weaving Light and Time: Unified Harmonic-Geometric Representation Learning for Dense RGB-Event Parsing](https://arxiv.org/abs/2607.09143)

**<font color=#1a73e8>作者：</font>** Chenxu Peng, Chongtian zhou, Dicheng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fusing standard RGB frames with asynchronous event streams has emerged as a definitive paradigm for robust perception in degraded environments. Although unified backbones have recently gained traction in multi-modal vision, adapting them to the RGB-Event domain remains fundamentally challenging. Existing architectures either resort to decoupled dual encoders that double computational overhead, or adopt generic unified designs that fail to resolve implicit geometric parallax and cross-spectral aliasing under the extreme representational divide between dense intensity grids and sparse kinematic spikes. To transcend these bottlenecks, we present Evita, the first unified backbone specifically engineered for dedicated dense RGB-Event parsing. To achieve profound modal synergy, Evita explicitly embeds a suite of intrinsic co-learning modules directly into every encoder layer. Specifically, it features Geometric Parallax Rectification for adaptive spatial alignment, Harmonic Spectral Resonance for texture transfer exclusively in the complex frequency domain, and Transient Global Routing for event-driven asymmetric attention. To guarantee robust feature extraction against spatial misalignments and decouple representations from specific event encodings, we construct N-ImageNetV2 alongside a stochastic event representation mixing pretraining protocol, empowering the network to seamlessly accommodate arbitrary event formats in downstream tasks. Extensive evaluations across the DELIVER, DDD17, and DSEC benchmarks confirm that Evita establishes new state-of-the-art metrics while delivering a superior accuracy-latency trade-off for real-time multimodal this http URL code are publicly available at: this https URL.

---


### 65. [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://arxiv.org/abs/2607.09153)

**<font color=#1a73e8>作者：</font>** Peng Kuang, Haibo Jin, Xiaoyu Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-agent rollouts, the scoring cost, growing quadratically with respect to sequence length L, creates a severe computational bottleneck, severely limiting PRMs' application in long-context scenarios. To resolve this, we introduce KV-PRM, a highly efficient process reward model that eliminates the heavy text re-encoding by directly reading the KV cache produced naturally during the LLM's generation phase. By processing a single "verify token" against the pre-existing KV cache, KV-PRM reduces the scoring cost from O(L^2) to O(L). We formally prove that the KV cache contains strictly greater information capacity than text, and is more efficient for downstream reward modeling. Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.

---


### 66. [Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering](https://arxiv.org/abs/2607.09156)

**<font color=#1a73e8>作者：</font>** Lucas Pinto  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Additive activation steering (injecting a scaled residual-stream direction during generation) is calibrated almost entirely in single-turn chat, yet the models it targets are increasingly deployed as tool-using ReAct agents. We present the first systematic chat-to-agent transfer study of additive steering, coupling behavioral measurement with a representation read-out in a matched-information design: the same items rendered as plain chat or as a ReAct tool-use episode, with matched-norm random-direction controls and the transcript re-encoded every turn to exclude KV-cache contamination. Transfer is real but rescaled, and the right description is a dissociation: the injected direction reaches the late layers at near-full strength in every setting and model tested (install-site agent-over-chat ratios 0.83-1.16 across three families), while the behavioral coupling is reset per model and context. On Qwen2.5-7B a refusal bypass vector amplifies in the agent (T = 1.45, CI [1.20, 1.78], N = 300); across a powered uniform-protocol distribution the coupling spans amplification (Gemma-2-9B T = 2.00) to attenuation (Yi-1.5-9B T = 0.43, CI [0.29, 0.60]), with no universal constant and a single clean attenuator against a universal sign. Directional ablation of the same axis does not amplify (T = 0.93, CI including 1) while additive injection amplifies (T = 1.50), a 20.1-point gain difference (CI [13.4, 26.8]) that identifies an additive-specific mechanism. Two pre-registered instruments converge to localize the rescaling to the ReAct format scaffold, before any tool observation, rather than to the observation boundary where a dilution account would predict it. The safety implication is immediate and unpredictable: agentic deployment amplifies steering-based refusal bypass by up to 2.00x on some models while others attenuate, so a deployment cannot assume a given model is safe under additive steering.

---


### 67. [What Pixels Are Enough? SEAMS: Sufficiency Saliency via MSE-Preservation Soft-Masks](https://arxiv.org/abs/2607.09164)

**<font color=#1a73e8>作者：</font>** Magdalena Trędowicz, Łukasz Struski, Arkadiusz Lewicki 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency maps are most useful when they identify the image regions that are sufficient to preserve a model's behaviour. We introduce SEAMS, a sufficiency-based saliency method that directly optimises a soft mask using a preservation objective. Given a frozen differentiable model output, such as a class probability, CLS embedding, or token representation, SEAMS searches for a compact mask that preserves the selected output. The approach relies on a simple optimisation framework based on soft masks, a learnable budget, and a three-way image composite generated entirely from the query image. As a result, it requires no auxiliary distractor dataset, architecture-specific attribution mechanism, or differentiable top-k relaxation. Experiments with frozen ViT-S/16 and ConvNeXt models show that the same optimisation pipeline can generate object-level, class-conditioned, and token-level explanations by changing only the preserved target. The resulting masks are compact, interpretable, stable across random initialisations, and competitive on insertion and deletion benchmarks. Our results also indicate that different architectures often rely on different sufficient evidence while achieving similar preservation fidelity, highlighting the architecture-dependent nature of visual explanations.

---


### 68. [A Personalized Computational Framework for Assessing the Sufficiency of Partially Observed Data in Healthcare AI models](https://arxiv.org/abs/2607.09165)

**<font color=#1a73e8>作者：</font>** Qingchu Jin, Felistas Mazhude, Jamie B. Rabb 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving early and timely diagnosis and treatment for disease is a major challenge. Recent applications of machine learning (ML) algorithms trained on patient data have shown promise in many different settings for predicting the patient health state. A challenge often faced when applying these ML algorithms is that at any given time, not all clinical variables (features) needed as input to perform prediction tasks are available. We define the concept of full-feature-capacity (FFC) to refer to prediction performance when such algorithms make use of all features on which they were trained. We then introduce Feature Sufficiency Analysis (FSA) - an analysis for determining whether a subset of all clinical features needed by an AI model is sufficient to achieve FFC. FSA estimates the underlying distributions of missing variables conditioned on features that are available. FSA provides a patient-specific assessment of whether the existing set of measured features achieves FFC. If yes, then there is no need to acquire further inputs and a ML-based prediction. We provide two case studies: prediction of need for postoperative prolonged ventilation in patients recovering from heart surgery; 10-year mortality prediction in an outpatient cohort. We also demonstrate that FSA also provides a clinically interpretable feature-ranking methodology based on prediction sufficiency, identifies intrinsically hard-to-predict patient populations, and has the potential to perform cost-aware optimization for clinical data acquisition. FSA provides a generic computational approach for determining whether incomplete clinical information is sufficient to support trustworthy AI-assisted clinical decision-making, thereby facilitating the prospective deployment of healthcare AI systems across diverse clinical settings.

---


### 69. [COAST: Context-Aware Differential Learning for Gene Expression Prediction in Spatial Transcriptomics](https://arxiv.org/abs/2607.09166)

**<font color=#1a73e8>作者：</font>** Keunho Byeon, Sunhong Park, Jeewoo Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics enables profiling of spatial gene expression but is limited by high cost and low throughput, motivating prediction from H&E histopathology images. Existing context-aware methods mainly supervise absolute expression, while relative expression relationships between spots are rarely used explicitly. We propose COAST, a context-aware differential learning framework for spatial gene expression prediction. COAST conditions the local and global context features with type-specific modulation and aggregates the target and context spot tokens using a Transformer encoder to capture both fine-grained local patterns and slide-level structure. It is trained with a joint objective that combines absolute expression regression with signed differential regression between the target and context spots. Experiments on multiple spatial transcriptomics datasets show consistent improvements in correlation- and distribution-based metrics, demonstrating the effectiveness of context-aware differential learning for histology-based spatial gene expression prediction.

---


### 70. [Understanding Schedule-Free Methods in Nonconvex Optimization: Rate Guarantees and Escaping Saddles](https://arxiv.org/abs/2607.09167)

**<font color=#1a73e8>作者：</font>** Jiseok Chae, Donghwan Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schedule-Free methods have attracted growing interest for alleviating the burden of designing and tuning a learning rate scheduler, while matching and sometimes even outperforming optimizers with tuned schedulers. Despite their strong empirical results, their convergence theory in nonconvex optimization, where modern machine learning objectives typically arise, has remained largely unexplored. In this paper, we provide worst-case analyses of Schedule-Free gradient descent and Schedule-Free stochastic gradient descent, in their standard form and without auxiliary modifications or restrictive conditions, for smooth but possibly nonconvex objectives. Based on a Lyapunov analysis derived from the continuous-time limiting ordinary differential equation associated with these methods, we show that Schedule-Free gradient descent and Schedule-Free stochastic gradient descent achieve the optimal worst-case convergence rates attainable among first-order methods. We further formulate Schedule-Free gradient descent as a nonautonomous dynamical system and prove strict-saddle avoidance under an arbitrarily small one-time perturbation. These theoretical results provide a better understanding of the strong performance that Schedule-Free methods demonstrate.

---


### 71. [TSR-Ego: Temporally Guided Stereo Refinement Framework for Egocentric 3D Human Pose Estimation](https://arxiv.org/abs/2607.09169)

**<font color=#1a73e8>作者：</font>** Md Mushfiqur Azam, John Quarles, Kevin Desai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric 3D human pose estimation from head-mounted stereo cameras is challenging due to fisheye distortion, severe self-occlusion, and frequent truncation of body joints outside the camera field of view. Recent stereo egocentric methods have improved performance through heatmap lifting, stereo correspondence, and transformer-based refinement, but they often rely heavily on frame-local evidence or use temporal information only as auxiliary pose-level context. This limits robustness when current-frame stereo cues are weak, occluded, or ambiguous. We propose TSR-Ego, a temporally guided stereo framework that couples short-term motion evidence with projection-guided feature sampling. The model first enriches dense stereo feature maps using a causal depthwise-separable temporal convolution, allowing past visual evidence to influence the feature space before deformable cross-attention. A single-stage causal stereo decoder then refines learned 3D joint queries through temporal self-attention, joint self-attention, and fisheye deformable stereo cross-attention, using the evolving pose estimate to generate 2D sampling references. Unlike methods that apply temporal reasoning mainly after pose prediction, TSR-Ego uses motion context to shape both the sampled stereo features and the joint representations while preserving online inference without future frames. Experiments on UnrealEgo2 and UnrealEgo-RW show state-of-the-art performance, with especially strong gains on real-world sequences.

---


### 72. [HiHR: Hierarchical Hyperbolic Representation for Aerial-Ground Person Re-Identification](https://arxiv.org/abs/2607.09186)

**<font color=#1a73e8>作者：</font>** Qiwei Yang, Pingping Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial-Ground Person Re-IDentification (AG-ReID) aims to retrieve the same person across heterogeneous aerial and ground camera platforms. Although great progress has been made, existing methods remain suboptimal due to the direct feature alignment across views, overlooking view-specific cues. To address this issue, we propose a novel Hierarchical Hyperbolic Representation (HiHR) framework for AG-ReID. More specifically, we first extract multi-granularity features based on pre-trained visual-text encoders. Then, we propose a Text-guided Multi-granularity Fusion (TMF) to fuse multi-granularity features and enhance the representation ability of identity features. Furthermore, we introduce the Hierarchical Hyperbolic Learning (HHL) to construct a hierarchical feature structure in a hyperbolic space. This hierarchy includes a coarse level that ensures identity separability and cross-view consistency, and a fine level that preserves view-specific discriminative cues. As a result, our proposed framework can effectively aggregate view-invariant and view-specific discriminative features for AG-ReID. Extensive experiments on four AG-ReID benchmarks demonstrate the effectiveness of our framework. The source code is available at this https URL.

---


### 73. [YeTI: You Only Need Two Noisy Images for Real-World sRGB Noise Generation](https://arxiv.org/abs/2607.09193)

**<font color=#1a73e8>作者：</font>** Jaekyun Ko, Byung Wan Lim, Soomin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world sRGB image denoising remains challenging due to the nonlinear characteristics of sensor noise and the difficulty of acquiring aligned clean-noisy image pairs. Supervised denoisers often overfit to limited paired datasets, while self-supervised methods still depend on sufficiently diverse noisy observations. These limitations motivate scalable noise synthesis methods that can model real-world noise without clean ground truth or camera metadata. We propose YeTI, a real-world sRGB noise generation framework that learns from only two noisy observations of the same scene. YeTI uses a Reconstruction Autoencoder to disentangle scene structure and noise characteristics, and models the latent noise distribution with a one-step Conditional Diffusion Transformer trained using consistency objectives. Given a single noisy input at inference time, YeTI generates realistic, signal-dependent noise while preserving the underlying scene content. Extensive experiments demonstrate the effectiveness of YeTI across real-world benchmarks. We evaluate noise generation on SIDD and further assess generalization on SIDD+, MAI2021, and SID, covering smartphone and diverse consumer-camera sensors. Downstream denoising results on DND further show that denoisers trained with YeTI-synthesized images achieve strong real-world performance, highlighting the practical value of clean-image-free and metadata-free noise generation.

---


### 74. [Application of machine learning to monster level prediction in tabletop RPG game design](https://arxiv.org/abs/2607.09196)

**<font color=#1a73e8>作者：</font>** Jolanta Śliwa, Jakub Adamczyk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing balanced adversaries is a central but labor-intensive task in tabletop role-playing game (TTRPG) development. In systems such as Pathfinder, each monster is described by many numerical attributes that jointly determine its power, summarized as an ordinal level. We investigate whether machine learning can support designers by predicting this level from a monster's attributes, framing the task as tabular ordinal regression. We introduce what is, to our knowledge, the first dataset built specifically for TTRPG monster-level prediction, derived from publicly available Pathfinder Second Edition data. Using it, we compare classical regression models with rounding schemes, dedicated tabular ordinal regression algorithms, and neural networks with ordinal-aware losses. To mirror real design workflows, we evaluate all models under chronological and expanding-window protocols with several complementary metrics. Results show that tree-based ensembles outperform linear models and neural approaches, achieving near-perfect ordinal ranking and high predictive accuracy. Explainable AI analyses, such as feature importance and error distributions, show that the model is aligned with human intuition and follows patterns grounded in game rules. Together, these results show that machine learning can reliably approximate designer judgments and serve as an effective computer-aided tool for monster balancing and broader TTRPG system design.

---


### 75. [Interference and Retention in Continual Learning](https://arxiv.org/abs/2607.09202)

**<font color=#1a73e8>作者：</font>** Julius Störk  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning commonly relies on post-hoc mechanisms such as replay, elastic regularization, or distillation. This work argues that forgetting should instead be modeled directly as interference between tasks. In the frozen-feature regime, forgetting from learning a new task is exactly the interference energy induced on the old task. In deep networks, the same quantity is recovered through path-averaged curvature with minimal additional forward passes.
When task supports are disjoint, forgetting can be eliminated structurally and when task supports overlap in conflicting directions, a non-zero distortion floor is unavoidable. The same geometry optimally merges models through task-aware orthogonalization. From this analysis we derive Interference-Gated Functional Allocation (IGFA), a replay-free, Fisher-free method that shares directions when tasks align and protects them when they conflict. Across benchmarks, IGFA achieves lossless retention when tasks are structurally separable and moves unavoidable cost from irreversible forgetting into deferred but recoverable plasticity when they are not. It matches the strongest replay-free structural baselines on dissimilar-task streams and improves on unconditional projection when similarity makes transfer worth preserving.

---


### 76. [Configurable AI Coding Assistants: Designing For Developers Who Like to Be in Control](https://arxiv.org/abs/2607.09215)

**<font color=#1a73e8>作者：</font>** Ekaterina Koshchenko, Jovana Stankovic, Ilya Zakharov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI coding assistants are now widely used in professional development, yet they offer only limited ways for developers to control how they behave. In this paper, we investigate what kinds of configurations experienced developers want in coding assistants, how they prioritize different types of configuration needs, and which interface mechanisms they prefer. We first synthesize product documentation and prior research on trust and personalization to compile a list of 33 configuration options, grouped into four categories: Code suggestions, System & policies, Human-assistant interaction, and Users & their personal context. We then conduct a survey with 56 professional developers and 7 design sessions in which participants arrange configurations into their perfect control board and talk about their needs and experiences in more depth.
Developers report strong interest in configurability: 72.6% of usefulness ratings are positive, while only around a third indicate that the corresponding configuration is known to participants in their tools. Demand is particularly high for task-related controls such as minimum confidence thresholds, visibility of suggestion quality, and response length, whereas many persona-related configurations are seen as unnecessary. In this paper, we discuss the implications for designing more unified and discoverable configuration surfaces for future coding assistants

---


### 77. [Temporal Knowledge Graph Forecasting under Distribution Shifts: A Synthetic Evaluation](https://arxiv.org/abs/2607.09232)

**<font color=#1a73e8>作者：</font>** Konrad Özdemir, Julia Gastinger, Lukas Kirchdorfer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal knowledge graphs (TKGs) represent evolving relational systems, whose underlying data-generating processes often change over time. Yet, TKG forecasting models are commonly evaluated only on empirical benchmark datasets that provide limited insight into the models' robustness to such distribution shifts. Recognising this issue, we study TKG forecasting under controlled shift environments using a synthetic TKG generator that encodes three temporal and structural properties -- recurrence, homophily, and periodicity -- as data-generating mechanisms. This allows us to evaluate seven forecasting architectures under stationary and shifting regimes. Our experiments suggest that robustness in TKG forecasting is highly signal-dependent. Recurrence-based and periodic regularities are largely recoverable under stationary conditions, and simple memory-based baselines can be competitive when recurrence dominates the data. However, structural breaks reveal limitations in model adaptivity, with shifts in latent entity-community structure posing the strongest challenge in our study. Overall, our findings improve the understanding of the capabilities and limitations of current TKG models confronted with temporal distribution shifts.

---


### 78. [All you need is SAMPAT](https://arxiv.org/abs/2607.09235)

**<font color=#1a73e8>作者：</font>** Jayadeva, Madhur Aswani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The current state of the art in AI/ML rests on deep neural architectures, which, in general, suffer from a lack of interpretability. Interpretability is crucial to gleaning insights while analyzing experimental data, where quantitative predictions may not be adequate for a scientist. We present a three layer neural architecture, SAMPAT (Smooth Approximation via Multivariate Polynomials and Analytic Transformations), that can provably learn a continuous, everywhere differentiable function, that can approximate any smooth function arbitrarily closely. SAMPAT's approximant can be expressed as a closed and compact algebraic, analytic expression, providing complete interpretability. Experiments on synthetic and benchmark datasets indicate that SAMPAT yields competitive performance with simpler representations. For many tasks, a two layer SAMPAT suffices. By imposing restrictions on the connectivity between neurons, SAMPAT may be used to provide a range of approximants, including regular and trigonometric polynomials, rational expressions, Gaussians, mixtures of Gaussians, as well as arbitrary combinations of the same; without restrictions, it learns a suitable structure. SAMPAT may be used to factorize polynomials and model nonlinear systems. With the addition of skip connections, a 4 to 6 layer SAMPAT is adequate to represent a substantive range of methods widely used in AI/ML, allowing the choice of a model's family, not just its parameters, to also be optimized as part of the learning process.

---


### 79. [Forget Narrowly, Retain Broadly: Unlearning as an Asymmetric Generalization Problem](https://arxiv.org/abs/2607.09236)

**<font color=#1a73e8>作者：</font>** Amit Peleg, Naman Deep Singh, Naama Pearl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning in LLMs is the targeted removal of specific knowledge while preserving all other capabilities, critical for privacy and safety. Yet existing benchmarks measure it unreliably. They miss knowledge that resurfaces under paraphrased or indirect queries, a failure we call under-forgetting, and lack the semantic, syntactic, and lexical probes needed to verify that unrelated knowledge is preserved, a failure we call over-forgetting. Both failures reflect an asymmetric generalization problem. Forget evaluation must cover diverse query formulations of the same target facts, testing whether forgetting holds beyond exact training prompts. Retain evaluation must probe a far larger and implicitly defined set, namely every fact disjoint from the forget target. The retain set thus defines the effective forget set, yet current datasets provide no fine-grained annotation of this forget-retain boundary. We address this with SUITE, an evaluation protocol and training corpus that captures forget-retain structure for real-world factual domains. Methods trained on SUITE improve substantially, showing that training data is as important as algorithmic design. Building on the obtained insights, we introduce JensUn++, an unlearning algorithm that achieves the best forget-retain utility trade-off across three LLMs, in both sequential and joint unlearning settings. Code and datasets are available at this https URL

---


### 80. [Blockchain-Linked Auditable Decision Management for Telecom/IoT Fraud-Control Requests](https://arxiv.org/abs/2607.09259)

**<font color=#1a73e8>作者：</font>** Saviz Changizi, Nasibeh Mohammadzadeh, Mohammad Shojafar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Telecom fraud-control studies often stop at detector-level classification, but deployment use requires request-level policy resolution, lifecycle traceability, and auditability. This paper reframes fraud control as blockchain-linked auditable decision management for synthetic telecom/IoT fraud-control requests, and its main result is that the QLoRA-tuned LLM branch becomes much more usable than zero-shot prompting but mainly approaches, rather than outperforms, a lower-cost centralized ensemble. The framework maps each synthetic deployment record to a managed request, blocks explicit out-of-boundary cases through a deterministic hard-fraud gate, scores non-hard requests using centralized ML (M1), federated meta-learning (M2), or LLM-family risk sources (M3), and resolves actions through a shared five-state policy, two-zone refinement mechanism, and local Ethereum-compatible audit layer. Evaluation uses separate synthetic training data and a 100,000-record deployment replay corpus, so the study should be read as controlled drift-replay evidence rather than field validation or proof of live deployability. On validation, M1 gives the strongest balance, with legitimate-request FPR 0.0890 under the 0.10 operating cap and soft-fraud recall 0.8341. On labeled deployment replay, however, the legitimate-FPR gap becomes large: M1 rises to 0.1646 and M3-QLoRA to 0.1801, while M3-QLoRA reduces the M3-Base legitimate FPR from 0.3915 and reaches 0.8240 soft-fraud recall. Blockchain telemetry shows that lifecycle gas, cost, latency, and throughput differences are driven by submitted off-chain decision profiles rather than changes in fraud logic.

---


### 81. [AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration](https://arxiv.org/abs/2607.09260)

**<font color=#1a73e8>作者：</font>** Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a novel integrated architecture for robust online 3D Gaussian splatting, real-time VR exploration, and speech-driven Vision-Language-Model interaction. Unlike methods assuming clean depth or external poses, our system combines ORB-SLAM3-based pose estimation with online Gaussian reconstruction for noisy real-world data. A VR pipeline enables immersive exploration of incremental reconstructions; a semantic module transcribes voice commands, generates scene descriptions, and records points of interest. Against state-of-the-art online Gaussian splatting methods, we improve image quality on our dataset (+14.5% PSNR, +8.6% SSIM, -14.3% LPIPS) and TUM-RGBD (+11.7% PSNR, +7.8% SSIM, -21.6% LPIPS), with comparable or superior frame rates via quality-speed configurations. We achieve an 88% VLM object-recognition rate.

---


### 82. [Semantic Hardness Is Not Visual Hardness: Sign-Aware Hard Negative Mining for Sign Language Retrieval](https://arxiv.org/abs/2607.09263)

**<font color=#1a73e8>作者：</font>** Junmyeong Lee, Chan Hur, ChangSu Choi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign Language Retrieval (SLRet) enables efficient access to sign language content but remains fragile in fine-grained scenarios where visually similar signs must be distinguished. We show that this limitation does not stem from model capacity, but from ineffective hard negative supervision. Specifically, we formulate fine-grained retrieval failures as a negative distribution mismatch: semantically distinct yet visually confusable signs are rarely treated as hard negatives, while existing text-based mining strategies fail to capture such visual ambiguity. To address this issue, we propose Sign-Aware Hard Negative Mining (SAN), which constructs hard negatives based on visual confusability in the sign embedding space rather than linguistic similarity. Experiments on PHOENIX-2014T demonstrate that SAN substantially improves fine-grained retrieval performance while preserving coarse-grained accuracy, highlighting the importance of aligning negative supervision with visual ambiguity in sign language retrieval.

---


### 83. [LionVote: Per-Layer Learning Rate Adaptation for Lion](https://arxiv.org/abs/2607.09266)

**<font color=#1a73e8>作者：</font>** Kris Atallah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-layer diagnostics reveal that, at the prescribed learning rate, Lion's effective scale is 2.6-2.8x too high for attention and MLP parameters and ~2x too high for normalization layers on ViT-Tiny/CIFAR-100; this 32% cross-layer-type disparity cannot be reproduced by a single global rate. The measurement comes from LionVote, a per-layer learning rate mechanism in which each parameter tensor maintains a compound level, a persistent integer updated every c epochs by two diagnostics (gradient direction stability and momentum health) resolved by a validation loss tiebreaker. Voting thresholds derive from geometric identities, the EMA time constant, and a noise-floor estimate; cadence is bounded structurally and selected by ablation. On ViT-Tiny/CIFAR-100, LionVote achieves 69.7% top-1 accuracy vs. Lion's 69.0% (p < 0.02, Welch's t-test) and AdamW's 68.8%. Per-layer adaptation value depends on both architectural heterogeneity and task; on uniform CNN architectures tuned SGD with cosine annealing remains dominant, and on ViT architectures gains are task-dependent.

---


### 84. [REMIND: RE-Identification with Memory for INDoor Navigation](https://arxiv.org/abs/2607.09267)

**<font color=#1a73e8>作者：</font>** Pablo Diaz-Pereda, Alejandro Rodriguez-Ramos, David Perez-Saura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile robots operating indoors must re-identify previously observed objects after long temporal gaps, significant viewpoint changes, and severe illumination variations. This remains a challenging problem: multi-object tracking methods are optimized for short-term association of pedestrians and vehicles at video rates, person and vehicle re-identification approaches lack persistent memory mechanisms, and state-of-the-art video object segmentation techniques rely on reactive distractor filtering rather than enforcing global identity consistency.
To address these limitations, we present REMIND, an online tracker designed for long-term multi-object re-identification of generic indoor objects from monocular RGB imagery, requiring neither camera pose nor depth. Motivated by evidence from visual cognition that humans rely on accumulated appearance familiarity and spatial context rather than explicit self-localization, REMIND combines frozen DINOv3 features with a dual-bank multi-prototype appearance memory, part- and background-level descriptors, a neighbour-context reasoning module exploiting spatial co-occurrence, and joint Hungarian assignment with ambiguity-aware safeguards. On a purpose-built indoor dataset featuring controlled revisits and dense same-class clutter, REMIND reaches 90.35% IDF1, nearly 20 points above a state-of-the-art video object segmentation baseline and more than 36 above a strong tracking-by-detection baseline. On ScanNet++, it attains the highest IDF1 in every setting but one, end-to-end detection over all scenes, where the tracking-by-detection baseline is marginally ahead while REMIND still associates and recovers identities more accurately; it also completes every scene, whereas the video object segmentation baseline exhausts GPU memory on 66.9% under YOLO detections. The complete system, evaluation framework, and dataset are publicly released.

---


### 85. [Autoregressive latent diffusion for 3D molecule generation](https://arxiv.org/abs/2607.09277)

**<font color=#1a73e8>作者：</font>** Federico Ottomano, Gaopeng Ren, Yingzhen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Three-dimensional (3D) molecule generation has been dominated by diffusion models, which achieve strong generation quality but typically require the molecular size to be specified a priori. Recent autoregressive approaches have substantially narrowed the performance gap while naturally supporting variable-length generation and conditioning on partial molecular context. However, balancing unconditional and context-conditioned generation remains challenging. We introduce KRONOS, a latent autoregressive diffusion framework that generates molecules in the latent space of a pre-trained autoencoder, jointly modeling molecular graph topology and geometry, while retaining the flexibility of autoregressive generation. We further introduce a mixed training strategy inspired by Fill-in-the Middle (FIM) paradigm, enabling both unconditional and fragment-conditioned molecular generation within a single left-to-right autoregressive model. Experiments on QM9 and GEOM-Drugs demonstrate that KRONOS achieves leading unconditional generation performance among autoregressive methods, while remaining competitive with diffusion models. Moreover, fragment-conditioned generation is achieved with negligible impact on unconditional generation performance, demonstrating that both generation paradigms can be supported within a single architecture.

---


### 86. [Rethinking Monocular Depth Embedding for Generalized Stereo Matching](https://arxiv.org/abs/2607.09284)

**<font color=#1a73e8>作者：</font>** Libo Lin, Shuangli Du, Minghua Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generally, monocular methods capture rich contextual priors but lack geometric precision, whereas stereo methods are geometrically accurate yet struggle in textureless and occluded regions. Several approaches attempt to combine their strengths to enhance the generalization of stereo matching (SM) by aligning monocular depth with stereo information. However, establishing a stable and generalizable alignment is challenging, and unreliable monocular cues can substantially degrade performance. This paper rethinks monocular depth embedding. First, to prevent shortcut learning, we reduce branch coupling instead of expanding network width. Second, we construct soft constraints instead of hard ones from monocular depth to improve tolerance to monocular depth errors. Based on the principles, we integrate monocular information into both feature extraction and GRU iterations. Specifically, the monocular depth map is fused with the RGB image to sharpen depth boundary perception and suppress matching ambiguities. The fused image is then used for feature extraction, allowing the contextual features to encode global geometric information. Furthermore, the monocular depth gradient feature is employed to guide disparity updates, helping to escape local oscillations. Finally, to address the boundary blurring of supervised disparity caused by data augmentation, we propose an edge confidence estimation method and an edge-aware loss function. Our method achieves state-of-the-art (SOTA) performance on multiple standard benchmarks, demonstrating excellent generalization while improving accuracy. The code is available at this https URL.

---


### 87. [Letter Lemmatization: One-to-one and Banded RNNs for Reversing Character-Set Simplification and Abbreviation in Medieval Text](https://arxiv.org/abs/2607.09291)

**<font color=#1a73e8>作者：</font>** Anguelos Nicolaou, Maria Pia Tiseo, Tamas Kovacs 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medieval document transcribers have very different practices; on top of that, heterogeneous digitization policies have resulted in corpora where the character-set must be viewed as fluid. In this paper we address the problem of changing between character-sets in a flexible manner. We focus on one-to-one character mappings and train characterlevel one-to-one RNNs to undo them with self-supervision; recovering half the CER even with 20 text lines. We analyse the use of these one-to-one networks for HTR post-correction and we see that they obtain significant improvements while totally ignoring ins-dels. We then use the exact same networks with character-level alignment groundtruth compiled from parallel corpora in a training and inference mode we call Banded RNNs. We use such networks to successfully expand abbreviations in medieval charter transcriptions. Finally we introduce an elaborate heuristic which takes the characters of two arbitrary character-sets and defines a metric encapsulating what we consider to be semantic similarity of characters. We call the construction of such mappings letter lemmatization and present a rich Python library that efficiently performs all presented methods.

---


### 88. [Risk-Aware General-Utility Markov Decision Processes](https://arxiv.org/abs/2607.09298)

**<font color=#1a73e8>作者：</font>** Pedro P. Santos, Fábio Vital, Alberto Sardinha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study general-utility Markov decision processes (GUMDPs) with risk-aware objectives. In this framework, an agent aims to optimize a risk measure of the distribution of objective values, where the objective function depends on the frequency of visitation of states induced by the agent's policy. First, we motivate, propose, and formalize risk-aware GUMDPs, which enable agents and decision makers to trade off expected performance by risk aversion while benefiting from the rich set of objectives that can be cast under the framework of GUMDPs. We focus our attention on the entropic risk measure (ERM). Second, we show how we can solve risk-aware GUMDPs with ERM objectives by resorting to online planning techniques. In particular, we propose an approach based on Monte Carlo Tree Search (MCTS) to provably solve risk-aware GUMDPs up to any desired accuracy. Third, we provide a set of experimental results showcasing that our approach is successful when optimizing for a spectrum of risk-aware behaviors in the context of GUMDPs under diverse tasks (standard MDPs, maximum state entropy exploration, imitation learning, and multi-objective MDPs).

---


### 89. [TextileNet: Towards Zero-shot Text-style Segmentation of Manuscripts](https://arxiv.org/abs/2607.09299)

**<font color=#1a73e8>作者：</font>** Anguelos Nicolaou, Antonella Ambrosio, Desiree Di Donato 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic writer identification systems have progressed remarkably in recent years, yet their deployment in archival paleography remains limited by the scarcity of labeled training data, open scribe sets, and degraded image quality. We present TextileNet, a fully convolutional multi-task network trained exclusively on synthetic data to produce dense pixel-level texture embeddings, which we transfer zeroshot to historical manuscript analysis. As an original contribution to evaluation methodology, we designed a paleographic visual quiz of 80 pair and triplet questions and administered it to a range from lay participants to senior paleographers under strict anonymity, establishing to our knowledge for the first time a human baseline for script-style discrimination on late medieval text. We employ TextileNet embeddings to perform zero-shot retrieval on sub-word granularity for hand and gender identification. Our experimental results help in building the credibility of TextileNet in the paleographic domain, but more than that demonstrate in experimental terms that the question of gender in handwriting needs to be treated with caution.

---


### 90. [From Classification to Localization and Clinical Validation: Large-Scale Development of a Deep Learning System for Thoracic Disease Detection on Chest Radiographs in Thailand](https://arxiv.org/abs/2607.09305)

**<font color=#1a73e8>作者：</font>** Isarun Chamveha, Tretap Promwiset, Napat Wanchaitanawong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chest radiography (CXR) remains the most widely used thoracic imaging modality, yet expert interpretation is constrained by a severe shortage of radiologists in Thailand and across Southeast Asia. Local adaptation of deep learning models to Thai data has been shown to substantially improve accuracy on Thai populations. Here we present the development and comprehensive validation of the chest radiograph analysis model in Inspectra CXR version 5, a deep learning system that performs multi-label thoracic disease classification and weakly supervised lesion localization within a single model. The architecture couples a DenseNet-121 backbone with Attend-and-Compare Modules (ACM) and a Probabilistic Class Activation Map (PCAM) aggregation layer, producing a per-condition classification score and heatmap simultaneously. The model was developed on 874,858 frontal chest radiographs with paired radiologist reports from Siriraj Hospital, Bangkok. On a held-out, radiologist-verified in-domain test set of 19,871 cases, it achieved a mean AUROC of 0.994 (mean sensitivity 92.4%, specificity 98.6%) across nine clinically important conditions. On an independent generalization set of 5,992 cases from 13 hospitals across Thailand, the mean AUROC was 0.970, indicating robust transfer across sites. For localization, evaluated on 4,549 radiologist-annotated cases, the model attained a mean lesion-localization fraction (LLF) of 77.9% at 0.59 non-lesion localizations per image. In a usability evaluation with five thoracic radiologists, the system reached a classification concordance of 93.6%, a localization concordance of 94.7%, and a mean System Usability Scale (SUS) score of 89. These results indicate that a locally developed, localization-capable CXR system can deliver high accuracy, generalize across heterogeneous Thai hospitals, and earn the trust of practicing radiologists.

---


### 91. [LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making](https://arxiv.org/abs/2607.09322)

**<font color=#1a73e8>作者：</font>** Yanzhen Chen, Zihan Xu, Xiaocheng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making. Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use. However, real-world medical care is inherently longitudinal, and clinicians must aggregate evidence across repeated visits, tests, and evolving treatments. Therefore, long-horizon interaction is essential for realistic assessment. LongMedBench is constructed via a reproducible pipeline that integrates MIMIC-IV admission records and clinical notes into time-series event streams and long-context memory datasets, enabling long-horizon, multi-session interactions between agents and a clinical environment. It comprises 335 patients, with 19.72 inpatient visits per patient on average and 44.91 medical events per visit. Guided by the long-horizon decision process, we propose an evaluation taxonomy with three suites: fact-based QA, temporal reasoning, and long-horizon decision-making. This taxonomy measures how agents understand and leverage historical patient information over extended horizons. Our experiments show that while recent LLMs can make good use of explicit timestamps, they have challenges in implicit time inference; The RAG and agent memory system can improve the performance of information retrieval tasks, but the performance of decision-making tasks is highly dependent on the model's immediate context.

---


### 92. [Letting the Data Speak: Extracting Keywords from Crowdsourced Collections with AI](https://arxiv.org/abs/2607.09324)

**<font color=#1a73e8>作者：</font>** Miguel Arana-Catania, Catherine Conisbee, Matthew Kidd  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying and assigning keywords at scale is a technical, practical, and ethical challenge for crowdsourced collections. This article reports the findings of the "Extracting Keywords from Crowdsourced Collections" project, which used the Their Finest Hour Online Archive, a crowdsourced Second World War digital collection hosted by the University of Oxford, as a case study. The project evaluated three Natural Language Processing approaches to automate keyword extraction: Named Entity Recognition, Keyword Extraction, and Topic Modelling. It tested these approaches across a range of artificial intelligence techniques, from traditional statistical methods to modern GenAI neural networks. Our quantitative and qualitative findings indicate that Natural Language Processing approaches offer real potential for keyword extraction at scale in crowdsourced collections, but that no single method offers a complete solution and that model choice significantly shapes results. We argue that in crowdsourced collections, where metadata is the direct product of engagement with living contributors, automated keyword extraction raises distinct stewardship responsibilities that must be addressed alongside technical performance. Open-weight, extractive models emerge from our evaluation as best placed to support responsible deployment, while generative AI, despite its abstractive potential, introduces accountability risks that anyone managing crowdsourced collections should weigh carefully.

---


### 93. [WILDTRACE: Benchmarking Natural Evidence Trails in Long-Context Reasoning](https://arxiv.org/abs/2607.09328)

**<font color=#1a73e8>作者：</font>** Zixin Chen, Peng Liu, Haobo Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering complex questions over long documents frequently requires integrating evidence that the source itself disperses naturally across distant passages. In an incident report, the operating condition, design flaw, and missed safety check that jointly explain a disaster may appear dozens of sections apart; in a novel, a character's true motive may surface only through scenes far removed from the moment it becomes relevant. This source-internal evidence integration is central to real-world long-document analysis, yet existing benchmarks largely sidestep it. Needle probes, planted facts, and reverse-engineered multi-hop chains embed evidence that may differ from the host text in distribution, placement, or register, making it unclear whether strong performance reflects genuine source reasoning or distributional artifacts. We introduce WILDTRACE, a benchmark of 481 tasks over 214 naturally occurring long-form sources such as technical incident reports and lesser-known literary narratives, where all evidence trails arise from the document's own causal, temporal, and narrative logic. Drawing on Pearl's causal hierarchy and prior multi-hop reasoning typologies, we define seven source-internal evidence geometries that characterize the distinct relational demands of analytical reading in long documents. A source-first construction pipeline mines candidate trails from document structure before writing questions; each item then undergoes multi-stage validation covering clue necessity, answer groundedness, rubric fidelity, contamination resistance and answerability. As models are increasingly entrusted with real-world high-stakes analytical tasks, this gap between accessing information and reasoning over naturally dispersed evidence emerges as a defining challenge for the next stage of long-context research.

---


### 94. [Dynamic Inverse Rendering for Enhanced Material-Lighting Decomposition](https://arxiv.org/abs/2607.09329)

**<font color=#1a73e8>作者：</font>** Raza Yunus, Benjamin Ummenhofer, Jan Eric Lenssen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decomposing outgoing surface radiance into material and illumination during inverse rendering is essential for applications such as relighting and augmented reality, yet it is severely ill-posed since multiple combinations can result in the same observed colour. Capturing an object under multiple lighting conditions usually helps resolve this ambiguity as it constrains the optimization towards correct solutions. In this work, we explore the potential of reconstructing rigidly moving objects -- which provides observations of diverse light-surface interactions -- to resolve the material-lighting ambiguity in inverse rendering. For this purpose, we introduce a relightable approach that marries object tracking and reconstruction with inverse rendering for general rigidly moving objects. Our experimental analysis on synthetic data demonstrates that motion can be an advantage for disentangling material and lighting: the reconstructed material is significantly more accurate when the object is observed under rigid motion than when it is static. Moreover, results on RGB videos of real hand-held objects show that our pipeline preserves this advantage even under noisy real-world conditions.

---


### 95. [Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning](https://arxiv.org/abs/2607.09336)

**<font color=#1a73e8>作者：</font>** Guanquan Wang, Yoshimasa Tsuruoka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

---


### 96. [Towards Detecting Inconsistencies in End-to-end Generated TODs](https://arxiv.org/abs/2607.09338)

**<font color=#1a73e8>作者：</font>** Tiziano Labruna, Giovanni Bonetta, Bernardo Magnini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative AI is profoundly transforming the core technologies behind conversational systems, shifting from component-based to end-to-end approaches. However, Large Language Models (LLMs) may still generate inconsistencies, a critical issue particularly in Task-Oriented Dialogues (TODs), where system responses must strictly adhere to information from a domain knowledge base (e.g., restaurants in a city). A single hallucination (e.g., suggesting a non-existent restaurant) can lead to severe task failures. We investigate a method for automatically detecting inconsistencies by conceptualizing TODs as a Constraint Satisfaction Problem (CSP), where variables represent dialogue segments referencing the conversational domain, and constraints among variables capture dialogue properties such as turn coherence and adherence to domain knowledge. We propose a pipeline that first identifies variables in a target dialogue and then applies a CSP solver to identify valid solutions. By comparing the target dialogue with valid variable assignments, we can detect inconsistencies and suggest minimal changes to ensure dialogue consistency. We demonstrate the high accuracy of the CSP-based approach in detecting inconsistencies, and provide a detailed analysis of our findings.

---


### 97. [Simon-SR: Spatially Adaptive Modulation and Visual Prompt Adaptation for Text-Reinforced Super-Resolution](https://arxiv.org/abs/2607.09351)

**<font color=#1a73e8>作者：</font>** Haotong Cheng, Yuxuan Li, Zijie Cui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single Image Super-Resolution (SISR) reconstructs high-quality images from low-resolution inputs. While recent multi-modal methods improve perceptual quality, they remain sensitive to erroneous priors and require expensive annotations. To address these issues, we propose Simon-SR, a multi-modal SISR framework leveraging learnable prompts for efficient semantic mining and robust text-image fusion. Our approach combines Contrastive Prompt Learning with Prompt-Guided Spatially Adaptive Refinement to enhance multi-modal alignment. Experiments demonstrate that Simon-SR surpasses state-of-the-art methods, achieving maximum improvements of 0.50 dB in PSNR, 0.0133 in SSIM, and 0.0695 in LPIPS. Code will be released.

---


### 98. [CtrlVTON: Controllable Virtual Try-On via Visual-Instance-Prompt Segmentation](https://arxiv.org/abs/2607.09362)

**<font color=#1a73e8>作者：</font>** Seungyong Lee, Hyun Jun Jang, Sangoh Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on (VTO) has made significant progress in realistically transferring garments onto a target person. Yet most systems give the user little control over how a garment should be worn -- its size (loose or fitted), style (e.g., tucked in or untucked, open or closed), and spatial placement on the body. We address this gap with two complementary contributions. First, we define and solve Visual-Instance-Prompt Segmentation via VIP-SAM: given a flatlay image of a garment, segment that specific instance in a photograph of a person wearing it. This is an instance-level task, distinct from the typically studied category-level segmentation. Second, we introduce CtrlVTON, a controllable VTO framework that recasts try-on as an image editing problem and adds segmentation masks as pixel-level control over garment layout, including style, size, and spatial placement on the body. VIP-SAM and CtrlVTON each achieve state-of-the-art results on their respective tasks. In particular, CtrlVTON generates images that follow user-provided layouts far more faithfully than the strongest proprietary editing systems while matching them on garment fidelity.

---


### 99. [SFDS: Selective File Disclosure System](https://arxiv.org/abs/2607.09370)

**<font color=#1a73e8>作者：</font>** Aditya Mitra, Quazi Fariha Tasnim, Hristina Mihajloska Trpcheska  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Access control to networked resources has been a longstanding challenge. The conventional solution relies on authentication mechanisms, which introduce additional complexities associated with Identity and Access Management (IAM). Such systems require user authentication, identity management, and authorization services, while also introducing security risks arising from vulnerabilities, misconfigurations, or implementation flaws. Furthermore, different file formats employ different mechanisms for ensuring authenticity and integrity through digital signatures. For example, PDF documents support the PDF Advanced Electronic Signature (PAdES) standard, whereas plain text files typically lack a standardized mechanism for embedding digital signatures. This paper proposes an architecture based on the Selective Disclosure JSON Web Token (SD-JWT) standard for securely sharing read-only files. The proposed architecture embeds cryptographic signatures and integrity protection directly into the shared resource, providing verifiable authenticity without relying on complex IAM infrastructures, such as centralized user databases, authentication services, or authorization mechanisms. By eliminating these components, the proposed solution simplifies deployment while maintaining strong security guarantees for the distribution of immutable resources.

---


### 100. [Graph Neural Networks for Scalable and Transferable Node Centrality Approximation](https://arxiv.org/abs/2607.09372)

**<font color=#1a73e8>作者：</font>** Samra Sana, Giorgio Mantica, Saul Imbrici  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) provide a learning-based framework for approximating graph quantities that are expensive to compute exactly. This paper investigates GNNs for scalable approximation of betweenness and closeness centrality, formulated as a node-ranking problem. Exact centrality values are used as supervision, and ranking quality is evaluated using Kendall's tau rank correlation. We study whether message-passing GNNs can learn transferable structural representations across different graph topologies rather than only fitting the distribution used during training. On unseen Erdos renyi graphs, the proposed models achieve tau = 0.851 for betweenness and tau = 0.894 for closeness. A large-scale betweenness model trained on graphs with N = 5,000 nodes achieves tau = 0.938, demonstrating scalability. Mixed-distribution training on Erdos renyi, Barabasi-Albert, and Gaussian Random Partition graphs improves betweenness transfer across graph families. In contrast, closeness centrality remains more sensitive to community-structured graphs and shows reduced transfer to real-world topologies. Finally, GNN inference achieves up to a 97.7x speedup over exact computation. These results show that mixed-distribution training can improve structural transfer in GNN-based centrality approximation, while identifying closeness centrality's sensitivity to topology as an open challenge.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-147](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
