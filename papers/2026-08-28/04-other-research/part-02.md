# 📦 其他研究 | 2026年08月28日

> 本类共 **171** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-171](./part-04.md)

---

### 51. [Long-Term Behavioral Evaluation for Trusted Collaborator Selection via Bidirectional Mamba](https://arxiv.org/abs/2608.25232)

**<font color=#1a73e8>作者：</font>** Botao Zhu, Xianbin Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective selection of trustworthy collaborators is crucial to ensuring the successful completion of collaborative tasks, which requires accurate assessments of both long-term device behavior and short-term collaborative dynamics. Consistent device behavior patterns, which are learned from historical collaborations, can be used to predict their reliability in future collaborations. However, accurately assessing device behavior based on historical collaborations remains challenging. First, behavior assessment from limited historical collaborations captures only instantaneous past behavior, failing to represent the devices' true behavior. Second, due to the temporal dependencies of device behavior, a unidirectional evaluation that relies only on earlier collaborations loses the opportunity to learn from subsequent collaborations. Addressing these challenges requires evaluating device behavior based on long-term collaborations while considering both forward and backward temporal dependencies. To this end, this work proposes a bidirectional Mamba-enabled model (BM) for long-term behavioral evaluation. For each short time slot, a graph is constructed among devices based on historical collaborations, and device behavioral features within the slot are then aggregated accordingly. Subsequently, a bidirectional Mamba model integrates these short-term representations across all time intervals, producing a stable and reliable long-term behavior evaluation for each device. Experimental results demonstrate that BM achieves higher evaluation accuracy than baseline methods, thereby enabling the selection of collaborators that maximize the value of task completion.

---


### 52. [ShuttleArena: Interpretable Self-Play in Physics-Based Badminton](https://arxiv.org/abs/2608.25246)

**<font color=#1a73e8>作者：</font>** Peize Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Badminton is a compact but challenging domain for game AI: a player must choose a physically feasible shuttle trajectory, anticipate the opponent's interception, and recover to a court position whose value depends on the opponent's next response. The central challenge is that shot selection and recovery are not separable: the best recovery depends on the shot-induced opponent response, while the value of the shot depends on whether the hitter can cover the reply. This paper presents ShuttleArena, a physics-based singles badminton self-play environment that couples continuous shuttle flight, player interception, structured shot generation, and post-shot recovery. The policy uses role-conditioned outputs: a masked interception choice on receiver turns and a factorized hitter action over shot azimuth, shot elevation, shot speed, and recovery target, enabling interpretable tactical probes. Episodes are single rallies rather than full scored games, and training uses Proximal Policy Optimization (PPO) self-play against a staged checkpoint opponent pool with sparse terminal rally-outcome rewards and a factor-specific recovery update. Evaluation with frozen checkpoint play, controlled tactical probes, recovery ablations, qualitative rollouts, and a human-data sanity check shows competitive improvement together with interpretable opponent-conditioned changes in shot geometry and recovery behavior. The learned policies produce recognizable badminton-like structure while also reflecting the abstractions of the simulator, and the recovery intervention shows that learned recovery behavior is competitively important. These results suggest that physics-based racket sports are a useful testbed for interactive digital entertainment AI because they require agents to coordinate execution, positioning, and opponent-relative tactical value.

---


### 53. [Neural-Bayesian Structure Learning for Discrete Choice Modeling](https://arxiv.org/abs/2608.25258)

**<font color=#1a73e8>作者：</font>** Hyunsoo Yun, Eun Hak Lee, Jiaru Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conventional discrete choice and machine learning models are estimated primarily from observational data and typically treat explanatory covariates as parallel inputs, providing no internal mechanism for determining how related attributes should adjust when one is deliberately changed. This paper proposes Neural-Bayesian Structure Learning (Neural-BSL), a framework coupling differentiable structure learning with random-utility-based discrete choice estimation in a single differentiable procedure. To prevent mutually exclusive choice outcome from distorting the recovered attribute structure, the observed choice is maintained outside the graph as an alternative-specific utility comparison, while the attribute structure and random-utility parameters are learned jointly. The learned structure enters the choice model through structure-weighted attribute interactions and provides the structural basis for propagating interventions through downstream attributes. An intervention is evaluated by updating the intervened attribute, propagating its model-implied downstream changes in topological order, and then recomputing utilities and choice probabilities. This yields both predicted mode-share responses and the associated changes in downstream traveler or trip attributes. We evaluate Neural-BSL using stated-preference data from Seoul and the revealed-preference data from London. Neural-BSL achieves predictive performance comparable to conventional benchmarks while recovering behaviorally coherent dependency structures. Across policy scenarios, propagating interventions through the learned structure changes the predicted redistribution across modes while exposing the downstream traveler and trip adjustments underlying those responses.

---


### 54. [OpenCVL: An Open, Diverse, and Large-Scale Dataset for Fine-Grained Cross-View Localization](https://arxiv.org/abs/2608.25274)

**<font color=#1a73e8>作者：</font>** Zimin Xia, Mubariz Zaffar, Junsheng Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained Cross-View Localization (CVL) estimates the precise position and orientation of a ground-level image by aligning it with geo-referenced aerial imagery, offering a scalable alternative to Global Navigation Satellite Systems (GNSS) in challenging urban environments. Existing datasets rely on data collected with high-end sensor suites, which inherently limit image diversity and scalability. While in-the-wild images are abundant, their noisy geo-tags make them unsuitable for reliable evaluation. To bridge this gap, we introduce OpenCVL, a large-scale, diverse, and open dataset containing 617,388 ground-aerial image pairs spanning 41 cities across four European countries. All images are sourced from permissive platforms, ensuring long-term accessibility and supporting open and reproducible research. The training set combines images captured with high-end sensors with diverse in-the-wild imagery. We further develop a data curation framework that filters and corrects pose annotations to construct reliable in-the-wild evaluation data. In addition, OpenCVL includes dedicated cross-area and snowy test sets to assess generalization and robustness. Experiments with a state-of-the-art CVL model on OpenCVL show that incorporating noisy in-the-wild data consistently improves performance on clean test sets, suggesting a promising direction for scaling CVL with diverse real-world imagery.

---


### 55. [PhaseShift: Topology-Aware Data Harmonization and Model Consolidation Across Signalized Intersections](https://arxiv.org/abs/2608.25275)

**<font color=#1a73e8>作者：</font>** Yash Ranjan, Artur Kumik, Rahul Sengupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned traffic-behavior models are commonly trained separately for each intersection, creating model portfolios that cannot share evidence across sites. We present PhaseShift, a topology-aware framework that harmonizes heterogeneous roadside trajectories into a shared actor-centric representation and trains one reusable backbone. Ego-relative coordinates, trajectory-induced movement paths, normalized signal context, and variable-cardinality interaction tokens remove site conventions while preserving behaviorally relevant topology. The backbone supports pooled operation, zero-shot at a held-out intersection, and low-data adaptation. We evaluate five intersections in two Florida regions on balanced field data, 100k training windows and equal-sized test sets per site under a replay-conditioned, best-of-sampled-trajectory protocol. At 10s, one pooled model lowers both minADE and minFDE relative to trained local models at all five sites, with median reductions of 36.8% and 22.0%. Leave-one-intersection-out deployment, including one cross-region fold, beats local training on both 10-s metrics at four of five sites, although short-horizon performance is less uniform. Fine-tuning with 1,000 target update windows improves on zero-shot at three sites and is the strongest regime at one. At site 7, every cross-site mixture sharply lowers long-horizon error under a fixed 100k-window budget; test-likelihood gains argue against a best-of-sample dispersion-only explanation. Local models fall behind calibrated IDM at the two highest-flow sites after long autoregressive rollouts; pretrained-backbone regimes do not. Within this five-site evaluation, PhaseShift demonstrates consolidation across heterogeneous physical control settings while identifying sites that still require adaptation. The protocol measures conditional single-vehicle generation under replayed context, not closed-loop traffic simulation.

---


### 56. [SHSP: Structure-Aware Hierarchical Solution Prediction for Mixed-Integer Linear Programming](https://arxiv.org/abs/2608.25282)

**<font color=#1a73e8>作者：</font>** Zherong Zhang, Guanlin Li, Chengrui Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-Integer Linear Programming (MILP) is a fundamental optimization paradigm in combinatorial optimization and has been widely applied across real-world domains. Due to its NP-hard nature, obtaining optimal solutions for large-scale or highly constrained MILP instances remains computationally prohibitive. Learning-based solution prediction has therefore emerged as a promising approach to provide high-quality variable assignment for solver acceleration. However, existing methods typically adopt a one-shot prediction paradigm that predicts the marginal probabilities of all variables simultaneously. As a result, the conditional dependencies among variables are only implicitly captured through message passing, with the burden of modeling the combinatorial structure falling entirely on the representational capacity of graph neural networks. To address this limitation, we propose the Structure-Aware Hierarchical Solution Prediction (SHSP) framework that replaces the parallel marginal decoding of one-shot methods with a novel hierarchical conditional decoding mechanism. Specifically, SHSP constructs a variable coupling graph from the constraint structure, decodes variables sequentially along a hierarchy of increasing coupling strength, and conditions each hierarchy on previously predicted assignments. To mitigate error accumulation during the decoding process, SHSP further incorporates a confidence-aware mask-and-repair mechanism to identify and correct unreliable intermediate predictions. We integrate SHSP with multiple learning-guided search methods, and evaluate it on four standard MILP benchmarks. Experimental results demonstrate that SHSP significantly outperforms existing one-shot prediction baselines, achieving a 54% average reduction in solution gap.

---


### 57. [WAVE: Reversing the Guidance Hierarchy for Coarse-to-Fine Guided Depth Super-Resolution](https://arxiv.org/abs/2608.25302)

**<font color=#1a73e8>作者：</font>** Tayyab Nasir, Daochang Liu, Ajmal Mian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guided depth super-resolution (GDSR) typically extracts RGB guidance features through convolutional hierarchies, inheriting their fine-to-coarse bias. Thus, low-level spatial cues surface in early layers, leaving the deeper layers to suppress those that do not correspond to true depth boundaries, which risks artifacts and blurred edges. The same fine-to-coarse bias persists in semantics-based methods that consume low-level tokens early and global tokens late. We present WAVE, which introduces a multi-level discrete wavelet transform (ML-DWT) as an explicit and interpretable feature-control mechanism, enabling a coarse-to-fine reconstruction by consuming sub-bands and semantic tokens in reverse of their generation order. WAVE further exploits these sub-bands to treat high- and low-frequency content separately, filtering at its source the misleading RGB color and texture cues that often lead to blurred boundaries and artifacts, offering an intuitive alternative to the suppression learned implicitly by an opaque network. WAVE separates structure and detail reconstruction into dedicated modules that: i) model interactions within and across wavelet sub-bands, depth features, and semantic priors, ii) apply semantic gating to the high-frequency bands, and iii) fuse modalities through an invertible coupling mechanism that prevents collapse onto a single modality. Extensive experiments across multiple benchmarks demonstrate that WAVE matches or outperforms existing methods, with the largest gains at high upsampling factors, where low-resolution depth contains the least structure.

---


### 58. [MulVec: Fine-Grained Role-Aware Matching for Training-Free Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2608.25305)

**<font color=#1a73e8>作者：</font>** Zihao Zhang, Dayan Wu, Xinze Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free zero-shot composed image retrieval finds a target image in a gallery from a reference image and a text edit without learning from task-specific image triplets. Existing methods typically describe the target as a whole and match this description with a global image representation. This global matching can mix different semantic cues and lose fine- grained details. We propose MULVEC, a role-aware method whose compiler produces a structured query record that is mapped to four retrieval roles: Global describes the full target, Desired states what should appear, Preserve states what should remain, and Forbidden states what should disappear. Frozen encoders map the query to one target description vector and role-specific probe vectors, while each candidate is represented by one global visual vector and a bank of local visual vectors. The retrieval roles then use this shared evidence for their respective purposes, and a fixed weighted sum of their scores ranks the entire gallery in a single retrieval pass. Across CIRCO, CIRR, and FashionIQ and three backbone scales, MULVEC improves CIRCO mAP@5 by up to 23.0% over the strongest compared method and gives the best CIRR and FashionIQ results in our comparison.

---


### 59. [AVI-Personality: A Trait-Activated Multimodal Dataset for Personality and Competency Assessment in Asynchronous Video Interviews](https://arxiv.org/abs/2608.25316)

**<font color=#1a73e8>作者：</font>** Tianyi Zhang, Jinwenxi Shang, Antonis Koutsoumpis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rapid development of AI-based personality and job-related competency assessment, Asynchronous Video Interviews (AVIs) are increasingly used in recruitment. However, existing multimodal personality datasets are often based on short, task-free social media videos and crowdsourced apparent personality labels, which limits their construct validity and relevance to structured interview assessment. To address these limitations, we introduce AVI-Personality, a trait-activated multimodal dataset for personality and job-related competency assessment from AVIs. The dataset contains 3,876 interview videos from 646 participants who completed a simulated management traineeship application. Participants answered two generic questions and four personality-targeted questions designed according to Trait Activation Theory. Our dataset provides both self and observer-reported HEXACO personality traits and job-related competency. We validate AVI-Personality through reliability, construct validity, internal nomological association, fairness, and benchmark analyses. Validation results show that the observer-rated personality traits have moderate to high reliability, especially when ratings are based on personality-targeted questions. Benchmark results show that text-based AI algorithms provide strong personality-relevant cues, while multimodal methods achieve the best overall performance but only modestly outperform text-based baselines. In general, AVI-Personality provides a psychometrically grounded dataset for developing and evaluating AI-based models for personality and competency assessment. The dataset is available are released at this https URL

---


### 60. [Two Dimensions Govern Agnostic Multiclass Transductive Learning](https://arxiv.org/abs/2608.25326)

**<font color=#1a73e8>作者：</font>** Pahan Dewasurendra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In transductive classification, an adversary fixes a labeled population, one label is hidden uniformly, and the learner sees all remaining labels. For binary classes, agnostic transductive and PAC learning have the same minimax rate. Whether this extends to multiclass learning was open, especially for unbounded label spaces where uniform convergence can fail. We resolve the question up to logarithmic factors. For every multiclass class $\mathcal H$ with DS dimension $d_{DS}$ and Natarajan dimension $d_{\mathrm N}$, the optimal agnostic transductive excess error satisfies $\widetilde\Theta\left(\frac{d_{DS}}{n}+\sqrt{\frac{d_{\mathrm N}}{n}}\right).$ The result holds for arbitrary label spaces. The two terms are both necessary. A DS pseudo-cube gives the realizable $d_{DS}/n$ obstruction, while a Natarajan cube with repeated points and fair labels gives the agnostic $\sqrt{d_{\mathrm N}/n}$ obstruction. The upper bound uses a random-reservation principle. The learner deliberately ignores a constant fraction of the visible labels, which makes the true test point uniform in a large unseen block. We combine realizable compression, a label-space reduction, and inside-menu agnostic compression across this finite-population split. A new without-replacement multiplicative-weights lemma preserves the fast $d_{DS}/n$ term. Consequently, agnostic multiclass PAC and transductive learning obey the same two-dimension law up to logarithmic factors.

---


### 61. [Neither Precision Nor Architecture Alone: Controlled Tests of Failure Remedies for Physics-Informed Neural Networks](https://arxiv.org/abs/2608.25327)

**<font color=#1a73e8>作者：</font>** Jinyuan Zhang, Peng He, He Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) frequently fail on stiff or advection-dominated PDEs, and two recent accounts offer competing remedies: switching from FP32 to FP64 to repair an L-BFGS stopping artifact, or replacing the MLP with a state-space-model (SSM) backbone plus sub-sequence alignment to counter architectural simplicity bias. We test both under matched, seed-paired controls in a pre-registered 144-run study spanning convection, reaction, and wave, plus an independent 85-run convection/wave study; success is relative $\ell_2$ error below $0.05$. The two remedies act on disjoint regime-and-seed slices: neither substitutes for the other. On hard convection ($\beta{=}50$), alignment recovers 2/5 seeds in FP32 and 3/5 in FP64, where the unaligned SSM succeeds on 0/5 seeds at either precision and the vanilla MLP moves only from 0/5 to 1/5 across the precision switch---the recoveries trace to the alignment objective, not the backbone. On reaction the backbone alone already succeeds on 3/5--4/5 seeds, so each remedy covers a regime the other does not. Responses are also seed-specific: the same precision switch flips individual seeds in opposite directions and, on wave, lowers median error with no statistically significant success gain. Tightening the inner L-BFGS tolerance in an independent repeated-step runner likewise lowers median error at a large runtime cost, with success counts unchanged. Precision, stopping, backbone, and alignment must therefore be evaluated jointly and reported per seed.

---


### 62. [GraftSR: Grafting Authentic Textures for Real-World Image Super-Resolution via Identical-Instance Guidance](https://arxiv.org/abs/2608.25334)

**<font color=#1a73e8>作者：</font>** Qifan Yu, Haoran Bai, Zongyao He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based real-world image super-resolution (SR) achieves impressive perceptual quality but inherently suffers from severe texture hallucination. To overcome this limitation, we propose GraftSR, a texture-reference-guided generative SR framework that leverages reference images of the identical instance to anchor the restoration of authentic textures. However, severe spatial misalignment between low-quality inputs and their references poses significant challenges, often leading to ambiguous transfer targets and background feature leakage. To address these issues, GraftSR employs a novel dual-mask reference guidance mechanism that systematically decouples the cross-view texture injection process. By explicitly isolating what authentic textures to extract from the reference and precisely localizing where to apply them within the target, GraftSR achieves robust texture transfer without relying on brittle spatial alignment. Furthermore, to bridge the critical gap in appropriate training data, we construct TexRefSR-141K, the first large-scale dataset providing high-quality reference tuples equipped with complementary spatial masks. Extensive experiments on our newly established benchmark, TexRefSR-Eval, demonstrate that GraftSR sets a new state-of-the-art. Notably, it reduces LPIPS by 20.2\% over top-performing baselines, achieving superior reference-faithful restoration.

---


### 63. [HRGuard: Gating Relationship Manipulation in Multi-Turn Agentic AI Conversations](https://arxiv.org/abs/2608.25340)

**<font color=#1a73e8>作者：</font>** Pei-Sze Tan, Tasuku Igarashi, Isao Echizen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Agentic AI assistants are increasingly used in everyday life. However, they may also be misused to support harmful manipulation in interpersonal relationships. This problem is role-sensitive. Requests from users who seek to manipulate others should be blocked. Users who seek protection from manipulation should instead receive supportive guidance. We study agentic relationship harm, which describes harm to human-human relationships that is mediated or assisted by AI agents. In multi-turn settings, individually plausible actions may combine into a harmful workflow. We introduce a benchmark of 1,000 five-turn conversations. It covers both attacker-side and victim-side scenarios. It also includes direct and adversarially paraphrased variants. We further propose HRGuard. It includes an online pre-generation gate and a turn-level post-generation gate. The post-generation gate maintains a decayed cumulative risk state and interrupts emerging manipulative workflows. Across eight generation models, HRGuard reduces harmful compliance while preserving victim-side protective guidance. It also outperforms a generic safety prompt and three general-purpose guard models. Independent-judge evaluation supports the main findings. Under our evaluation protocol, the tested generic prompt and general-purpose guards leave substantial residual risk, motivating turn-aware relationship-specific evaluation.

---


### 64. [CoRE: Weakly Supervised Coarse-to-Fine Risk Evidence Learning in Driving Videos](https://arxiv.org/abs/2608.25344)

**<font color=#1a73e8>作者：</font>** Kaiser Hamid, Can Cui, Nade Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceived risk in driving evolves over time and may be supported by specific scene entities, yet supervision is typically limited to coarse video-level judgments. Learning \emph{when} supporting evidence emerges and \emph{which entities} support a risk predictor would ordinarily require costly temporal- and entity-level annotations. We introduce \textbf{CoRE}, a weakly supervised coarse-to-fine framework that learns fine-grained prediction support from coarse video supervision. CoRE first trains a video-level predictor and then freezes it. Structured interventions over candidate temporal regions or entity tracks measure how each candidate changes the coarse prediction, producing graded prediction-effect targets. These targets are distilled into a student that directly predicts temporal and entity support from the original video, without requiring interventions at inference. We evaluate this learning principle across three complementary settings: RISEE tests perceived-risk support from subjective clip-level judgments without temporal or entity-level risk annotations; DoTA provides independent temporal event annotations for evaluating weakly supervised traffic-anomaly localization; and UCF-Crime tests whether the same coarse-to-fine mechanism extends to a standard non-driving anomaly-detection benchmark. Across these settings, CoRE learns informative fine-grained support from coarse supervision, with strong temporal localization on DoTA and competitive performance on UCF-Crime. These results show that coarse video predictions can provide useful supervision for recovering the fine-grained evidence supporting them, without requiring corresponding fine-grained labels.

---


### 65. [Leveraging Speech Acts for Low-Data and Cross-Domain Conversation Derailment Forecasting](https://arxiv.org/abs/2608.25359)

**<font color=#1a73e8>作者：</font>** Angela Yifei Yuan, Christine De Kock, Christopher Leckie  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational derailment forecasting aims to predict when online discussions will escalate into hostility, enabling proactive moderation. Existing approaches often struggle in low-data settings and to generalize across domains. This poses a challenge for new platforms and smaller communities where annotated data is limited. We propose modeling pragmatic representations of conversations to reduce lexical noise and improve generalizability. Specifically, speech act information is used as an auxiliary learning signal alongside textual semantics. Experimental results show improved performance across three datasets, particularly in low-data and cross-domain settings.

---


### 66. [FlashNormal: Detailed Surface Normal Estimation from Flash and No-Flash Images](https://arxiv.org/abs/2608.25360)

**<font color=#1a73e8>作者：</font>** Ruiyang Chen, Feiran Li, Heng Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality surface normal estimation is preferred for detailed surface shape recovery and image editing. Existing single image-based methods, though being a practical setup, often struggle to recover fine surface details and are sensitive to inherent shape-reflectance ambiguity. While photometric stereo achieves high-fidelity surface normal estimation from images under varying lights, its applicability is strictly limited by requiring a multi-illumination capture setup. To this end, we propose FlashNormal, a diffusion-based surface normal estimator from flash/no-flash image pairs. While retaining high practicability on modern smartphones, our proposal takes advantage of flash-induced shading variations, and leverages curvature-guided detail enhancement strategy, improving surface detail recovery and mitigating shape-reflectance ambiguity effectively. To evaluate our proposed method, we further present EvalFlash, the first real-world flash/no-flash evaluation dataset containing 20 objects aligned with ground-truth surface normals for quantitative benchmarking. Extensive experiments demonstrate the effectiveness of FlashNormal over state-of-the-art single image-based methods and show a significant out-performance over flash/no-flash-based normal estimation method on EvalFlash.

---


### 67. [PaSta: Noisy Node Classification with Partial Label Learning](https://arxiv.org/abs/2608.25365)

**<font color=#1a73e8>作者：</font>** Yujing Liu, Yixin Liu, Yu Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Noisy node classification problem is a fundamental yet challenging task for real-world graph-related web services, where node labels are often corrupted or unreliable due to weak supervision or automatic annotation. However, existing methods typically train models based on one-hot labels, which not only makes models susceptible to overfitting on noisy labels, but also leads to error accumulation after pseudo-label-guided enhancement. In this paper, we propose a novel Partial label-based Self-training framework (PaSta for short) that leverages partial label learning technique to overcome the limitations of existing methods. Specifically, PaSta first trains multiple annotators to comprehensively capture the class distribution of nodes and aggregates their predictions to construct high-quality partial labels. Subsequently, we design a partial label-based classification model with two well-crafted loss functions to guide the model learning at both label and representation spaces. To further enhance the robustness against noisy labels, we introduce a self-training strategy where the labels refined by partial label learning are then used to further optimize the annotators in a closed-loop iterative manner. Extensive experiments on five datasets demonstrate that, compared with existing state-of-the-art methods, PaSta achieves an average improvement of 1.1% in classification performance under various noise settings.

---


### 68. [RSFusionDet: Underwater RGB-Sonar Multimodal Object Detection](https://arxiv.org/abs/2608.25367)

**<font color=#1a73e8>作者：</font>** Zhuoyan Liu, Yihan Wang, Bo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater unimodal object detection faces many challenges in sensor imaging, such as optical images limited by underwater noise and visible distance, and sonar images limited by less object structural information. While, optical images have rich object structural information, and sonar images are less affected by underwater noise and have a longer visible distance. Optical (RGB modality) and sonar (Sonar modality) images have complementary information underwater. In this paper, we create an RGB-Sonar multimodal object detection dataset, \textbf{R}GB-\textbf{S}onar \textbf{Fusion} (RSFusion) and propose evaluation metrics for the benchmark. And we propose the \textbf{R}GB-\textbf{S}onar \textbf{Fusion} \textbf{Det}ector (RSFusionDet) with a new RGB-Sonar multimodal object detection result expression for RGB-Sonar multimodal object detection. We analyze the features of RGB and Sonar modal information, and design a Cross-Attention Fusion (CAFusion) module to fuse RGB-Sonar spatial misalignment features and Object Matching Head (OMHead) with Loss (OMLoss) to match identical objects in RGB-Sonar modalities. Our RSFusionDet achieves 76.4/48.6 AP (RGB/Sonar) for object detection and 83.4 \(\text{F1-Score}_{match}\) for object matching, on RSFusion, which outperforms other object detection models. Compared with the DINO baseline, our method improves by 0.7/1.4 AP (RGB/Sonar) while simultaneously providing reliable cross-modal object matching. The code and datasets are publicly available at this https URL.

---


### 69. [Capacity Overflow: A Blind Spot for Backdoor Attacks in Vision MoE](https://arxiv.org/abs/2608.25371)

**<font color=#1a73e8>作者：</font>** Xiaocheng Zou, Tiancheng Zheng, Xiaolin Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become a prevalent paradigm for scaling Vision Transformers efficiently. To ensure computational scalability and prevent expert overload, Vision MoE architectures employ a capacity-bounded token dispatch mechanism, where each expert's processing budget depends on the inference batch size. This work identifies this batch-dependent behavior as an overlooked attack surface, and proposes a stealthy supply-chain backdoor attack that exploits this property through a three-phase framework. First, we inject a backdoor into an early MoE layer. Second, we train a neutralizer in a deeper MoE layer that suppresses the backdoor under normal capacity. Third, we configure a batch-adaptive capacity factor that preserves high capacity for small batches while reducing it for large batches, naturally disabling the neutralizer via token overflow at deployment-scale batch sizes. The attack remains in dormant mode during small-batch security audits and enters activation mode during large-batch deployment. Experiments on V-MoE and Swin-MoE across ImageNet-100 and GTSRB demonstrate activation-mode attack success rates of 76-87% with dormant-mode ASR below 9%, while evading Neural Cleanse, STRIP, Fine-Pruning, and Activation Clustering. Our findings reveal a fundamental security risk arising from batch-dependent execution in scalable Vision MoE architectures.

---


### 70. [PIVOT: A Multi-Trajectory Dataset and Testbed for Pose, Intrinsics, and Novel Viewpoint Evaluation in Real-World 3D Reconstruction](https://arxiv.org/abs/2608.25401)

**<font color=#1a73e8>作者：</font>** Mary Raymond  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural radiance fields (NeRFs), 3D Gaussian Splatting (3DGS), and related novel-view synthesis methods are commonly evaluated under capture and reconstruction conditions cleaner than those encountered by robots, drones, and autonomous systems. Benchmarks often rely on reconstruction-friendly trajectories, optimized camera poses and intrinsics, and held-out views sampled from trajectories represented during training. These assumptions can obscure performance with measured poses, reusable camera calibration, and structurally different camera paths.
We introduce PIVOT (Pose, Intrinsics and Viewpoint Oriented Testbed), a multi-trajectory dataset, processing pipeline, and evaluation framework for independently studying these factors. PIVOT captures each scene using diverse camera trajectories and retains, where available, both sensor-derived measured poses and COLMAP-optimized poses, together with calibrated and optimized camera intrinsics. It defines three benchmark families: (1) seen versus unseen trajectory novel-view generalization, (2) measured versus optimized pose sensitivity, and (3) calibrated versus optimized intrinsics sensitivity. We also introduce a directed pose-space Chamfer distance to quantify how well training poses cover an evaluation trajectory.
PIVOT v1 contains five real-world scenes captured with a DJI Mini 4 Pro and provides an open processing and Nerfstudio-based evaluation toolchain. Benchmark results show a consistent quality gap between held-out views on represented trajectories and unseen trajectories, as well as substantial sensitivity to pose source and camera intrinsics.

---


### 71. [AdaptiveEmbed: Sample-Adaptive Multi-Vector Representation for Multimodal Retrieval](https://arxiv.org/abs/2608.25412)

**<font color=#1a73e8>作者：</font>** Xinze Liu, Lei Yang, Dayan Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-vector representations have emerged as an effective paradigm for multimodal retrieval, representing each sample with multiple complementary embeddings to capture fine-grained cross-modal information. However, existing approaches typically employ a fixed representation capacity, assigning the same number of vectors to all samples regardless of their individual retrieval demands. Such a fixed-capacity formulation overlooks the fact that different samples may require different amounts of representation capacity for effective retrieval. In this work, we introduce \emph{Sample-Adaptive Multi-Vector Representation} (SAMVR), a new problem setting for multimodal retrieval that studies how multi-vector representation capacity can be allocated at the sample level. Under SAMVR, each sample is represented by a \emph{content-adaptive embedding set} (CAES), whose capacity is determined according to the sample-specific retrieval utility of additional representation vectors. To instantiate SAMVR, we propose \emph{AdaptiveEmbed}, a unified framework for learning sample-adaptive multi-vector representations. AdaptiveEmbed learns structured multi-vector representations through \emph{Multi-Group Contrastive Learning} (MGCL) with the symmetric \emph{set-to-set similarity} (SetSim), and further employs \emph{Utility Policy Optimization} (UPO) to determine sample-specific representation capacity via \emph{Marginal Utility Allocation} (MUA). Experiments across multimodal retrieval benchmarks involving image, text, video, and audio show that sample-adaptive capacity allocation achieves overall better retrieval performance than fixed-capacity multi-vector representations, validating the effectiveness of SAMVR for multimodal retrieval. These results establish SAMVR as a viable formulation for adaptive capacity allocation in multi-vector multimodal retrieval.

---


### 72. [Paint What You See: Benchmarking Dexterous Visual Tool Use in Multimodal Agents](https://arxiv.org/abs/2608.25417)

**<font color=#1a73e8>作者：</font>** Shudong Liu, Dongyang Chen, Enci Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation is shifting from static QA toward agentic settings where models act through external tools. We identify a critical yet underexplored capability within this space - dexterous visual tool use: fine-grained, closed-loop parameterized visual action in which models infer tool parameters from visual evidence, and those parameters directly govern the final result. Existing benchmarks cover web navigation, GUI operation, and software engineering, but rarely target this coupling between visual evidence and execution precision. We propose EASEL, a benchmark evaluating a controlled instance of dexterous visual tool use that adopts reference-guided visual reconstruction as its primary proxy task: the agent incrementally paints a canvas to match a reference image. EASEL additionally includes semantic tasks spanning region annotation, handwriting, and path planning. We further provide EASEL-Data, a 440k-sample two-stage curriculum dataset for trajectory supervision, and EASEL-9B to investigate its effect on this capability. Evaluation of 25 models reveals that current multimodal agents systematically struggle on EASEL. Reconstruction similarity bottlenecks at low levels (0.40-0.54), while trajectory diagnostics expose severe closed-loop instability - models typically saturate early or degrade post-peak. Semantic tasks reveal sharp capability boundaries in precision annotation and path planning. EASEL-9B, trained on EASEL-Data, surpasses the base model by a relative 6.3%, ranking third among all evaluated models.

---


### 73. [BVR Sim: An Open and High-Throughput Environment for Heterogeneous Air-Combat Reinforcement Learning](https://arxiv.org/abs/2608.25419)

**<font color=#1a73e8>作者：</font>** Haocheng Sun, Mulai Tan  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Beyond-visual-range (BVR) air combat is a challenging reinforcement-learning domain characterized by partial observability, long-horizon decision making, energy management, and limited weapons. We present BVR Sim, an open-source Gymnasium-style environment designed for heterogeneous air-combat reinforcement learning. BVR Sim supports multiple JSBSim aircraft models, including the F-15, F-16, F/A-18, and F-22, with configurable weapons, sensors, controllers, and opponents. A unified tactical action interface specifies desired heading, altitude, speed, and weapon release above aircraft-specific inner-loop controllers, enabling policies to operate across heterogeneous platforms. The environment provides interchangeable Python and accelerated C++ backends, entity-oriented observations, compositional rewards, scripted opponents, replay and visualization, and adapters for multi-agent learning frameworks. At a 0.4-s decision interval, the C++ backend achieves 104 simulated seconds per wall-clock second in 1-vs-1 and remains practical through 10-vs-10 scenarios. A policy trained only on the F-16 transfers without retraining to four unseen aircraft, reaching a 45.5% mean win rate with aircraft-specific controller adaptation. MAPPO and HAPPO experiments further verify end-to-end compatibility with standard multi-agent reinforcement-learning pipelines.

---


### 74. [Saliency-Depth Conditioning for Zero-Shot Segmentation of Communication-Tower Components in Cluttered UAV Imagery](https://arxiv.org/abs/2608.25435)

**<font color=#1a73e8>作者：</font>** Ali Lesani, Chul Min Yeum, Su-Min Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained segmentation of communication-tower components in UAV imagery is essential for automated inspection, yet task-specific models are hard to develop due to limited instance-level annotations. Zero-shot segmentation models offer a promising alternative, but in cluttered scenes, visually similar background structures interfere with component localization, causing missed instances and false positives. We propose a model-agnostic saliency-depth foreground-conditioning strategy combining appearance-based saliency with monocular relative depth to construct a coarse tower prior and suppress irrelevant content. We integrate this module with Grounded-SAM and SAM 3, yielding SD-Grounded-SAM and SD-SAM 3. SD-Grounded-SAM further applies geometric and depth-aware box refinement before mask generation, while SD-SAM 3 relies on SAM 3's internal setup. On TOW-300, a dataset of 340 communication-tower UAV images, our strategy improves both baselines: SD-SAM 3 achieves the strongest instance-segmentation performance, while SD-Grounded-SAM produces fewer false positives. Ablations confirm complementary gains from saliency, depth, and box refinement, improving robustness in cluttered scenes.

---


### 75. [Joint Initialization of Flux Networks and Effective Multiplication Factor for Physics-Informed Neural Networks Solving Neutron Diffusion Problems](https://arxiv.org/abs/2608.25443)

**<font color=#1a73e8>作者：</font>** Qin Hang, Yangdi Yi, Jiayi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient determination of the effective multiplication factor (keff) is an important computational task in reactor core neutronics analysis. Physics-informed neural networks (PINNs) incorporate neutron diffusion equations and boundary conditions into network training to efficiently determine the neutron flux distribution and keff. To further improve the efficiency of keff calculations using PINNs, a Joint Initialization Physics-Informed Neural Network (JI-PINN) is proposed in this work. In this method, a low-resolution approximate solution to the K-eigenvalue problem is used to construct a joint initial state for the flux network parameters and keff, and both are then jointly optimized under physical constraints. The proposed method was validated on a two-dimensional two-group two-material case, the IAEA 2D benchmark, a two-dimensional two-group four-material case, and a three-dimensional single-group case. For these test cases, the total computational time was reduced by 25.4%, 38.2%, 49.4%, and 28.9%, respectively, while comparable solution accuracy was maintained. The occurrence of anomalous results associated with marked deviations of keff from the reference value was also reduced. The proposed method provides a more efficient and robust initialization strategy for solving neutron diffusion K-eigenvalue problem with PINNs.

---


### 76. [Automatic weld seam segmentation for industrial quality control: a comparison of RGB and polarimetric imaging with CNN and transformer architectures](https://arxiv.org/abs/2608.25465)

**<font color=#1a73e8>作者：</font>** Simone Garbin, Leonardo Venturoso, Marco Todescato  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual inspection of welded assemblies remains one of the least automated stages in many industrial production processes, still depending largely on the experience of human operators and thus subject to inter-operator variability; the manufacturing of special-purpose machinery cabins, the setting of this study, is one representative case. This work evaluates the feasibility of automatic weld seam segmentation from RGB and polarimetric imagery, comparing controlled laboratory acquisitions with images captured under real, uncontrolled conditions. Convolutional neural network (CNN) architectures and transformer-based architectures are benchmarked under a unified, threshold-independent protocol, training each CNN with three random seeds to separate genuine effects from seed noise. In controlled RGB conditions, CNN models reach a mean mask mAP50 of up to 0.87, but drop to 0.22-0.48 under uncontrolled acquisition, showing that the acquisition setup is a first-order component of the inspection system. Polarimetric imaging with alignment-preserving geometric augmentation localizes previously unseen welds with a mean mask mAP50 up to 0.93: on par with, rather than ahead of, the best controlled-RGB result, but reaching that accuracy on uncontrolled RGB without requiring acquisition control. The clearest architectural finding concerns viewpoint robustness. In-distribution, transformers and CNNs are broadly comparable; but under a test-time viewpoint shift, the transformer models, and RF-DETR in particular, retain high accuracy while every CNN collapses. The gap holds across three seeds and a resolution-matched control, pointing to architecture rather than training resolution. Within the CNN family, capacity brings no reliable in-distribution gain once seed variance is accounted for: small CNNs suffice for fixed viewpoints, transformers for variable ones.

---


### 77. [Resolving Multi-Modal Regression by Difference-Quotient-Based Clustering:Fast Coarse Conditional-Label Assignment](https://arxiv.org/abs/2608.25467)

**<font color=#1a73e8>作者：</font>** Huang Weiquan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal regression suffers from the mean-collapse pathology: under squared loss, an unconstrained regressor converges to the conditional mean, which for K > 1 lies away from all modes. We attribute this failure to pairwise contradictions--samples with nearly identical inputs but distant outputs--and propose Difference-Quotient Clustering (DQC), which partitions data to minimize intra-cluster output-vs-input discrepancy. Each sample is assigned to the cluster that minimizes its maximum contradiction ratio; a logits generator and a conditional network are then trained on the resulting labels. Since the generating modality is unknown at test time, we evaluate via minimum squared error (minMSE) against all K true outputs. On synthetic benchmarks (K=5, 10), DQC achieves test minMSE 0.19 (K=5, nx=500), versus 0.09 for an oracle, 1.08 for random labels, and 1.33 for mean collapse. We observe two empirical regularities: larger intra-cluster contradictions require deeper networks, and oracle labels generalize from fewer samples than cluster-derived equivalents. The clustering is a hard, parallelizable O(n^2/2) front-end for coarse conditional assignment, reducing the burden of downstream generative refinement. A second-stage re-clustering on residual errors is outlined as future work.

---


### 78. [PAGS: Autofocusing Photoacoustic Tomography via Speed-of-Sound-Adaptive Gaussian Splatting](https://arxiv.org/abs/2608.25472)

**<font color=#1a73e8>作者：</font>** Jiarui Ge, Jintao Ma, Bangxu Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photoacoustic computed tomography (PACT) combines optical absorption contrast with acoustic detection for high-resolution deep-tissue imaging. A persistent challenge is that unknown speed-of-sound (SoS) heterogeneity changes acoustic time-of-flight, causing defocusing artifacts when reconstruction assumes a uniform SoS. Existing SoS-adaptive methods either rely on calibrated acoustic priors or optimize dense physical medium models, which becomes expensive and difficult to scale in 3D. We propose PAGS, a differentiable framework for blind autofocusing PACT via speed-of-sound-adaptive Gaussian splatting. PAGS represents the initial pressure field with sparse Gaussian photoacoustic (PA) sources and replaces explicit medium recovery with a compact anisotropic path-averaged SoS (ASoS) field parameterized by spherical harmonic probes. This latent propagation field directly controls source-to-transducer arrival-time alignment, while an analytic Gaussian acoustic projection maps the source representation to transducer signals efficiently. The resulting closed-loop signal-domain optimization jointly updates the Gaussian PA source parameters and the ASoS field from measured data, without calibrated SoS priors. Experiments on simulated and physical phantom data demonstrate improved reconstruction sharpness under heterogeneous acoustic media, robustness to sparse-view sampling, and computational benefits from the analytic Gaussian projection.

---


### 79. [Separating Disclosure from Authorization: Field-Tier Minimization for Agent Action Mediation](https://arxiv.org/abs/2608.25474)

**<font color=#1a73e8>作者：</font>** Jiten Oswal, John Cadeddu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A system that authorizes an action must see enough of it to decide, and a system that attests to its decision must record enough to be audited. Both pressures push raw action parameters -- recipients, payment memos, record identifiers -- into an append-only ledger that cannot delete them. We show the two are separable. We classify each parameter field, not each action class, into three tiers: fields a policy may legitimately match on, which cross raw; fields that are policy-relevant but identifying, which cross only as projections such as an email domain or a templated route shape; and fields with no legitimate policy use, which never leave the workload. The central property is that the ledger's commitment is a canonical digest of the full, unminimized parameters, computed before minimization runs. The commitment is therefore independent of the tier table: reclassifying a field changes what is disclosed without invalidating a historical entry, reopening a hash, or altering what an offline verifier checks. Tier table, policy schema and wire schema are generated from one per-action declaration, so the deciding and recording parties cannot hold different rules. We then address a question the architecture forces: which party should compute each attested fact? We argue it is settled by which party could lie about it undetectably, and derive three answers within one request -- the client computes the parameter digest, being the only party holding the data; it is structurally prevented from naming the definition that governed it, since that would write a false statement into a signed ledger; and it attests which tier table it applied, so divergence is detectable. We give a leakage analysis of each projection, report an incident in which a first-cut projection preserved the identifier it was written to remove, and state the residual trust the design does not eliminate.

---


### 80. [4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479)

**<font color=#1a73e8>作者：</font>** Shiqian Li, Chenguo Lin, Zhiguang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video models now synthesize footage nearly indistinguishable from reality. Their promise as interactive tools hinges on fine-grained control of how objects and the camera move over time, yet each existing approach captures only part of this: camera-parameter methods steer the viewpoint but cannot move objects, 2D-trajectory methods act in the image plane and ignore depth and occlusion, and recent 3D methods add geometry but run only offline at a fixed length. In particular, none combines 3D-consistent control of both camera and objects with real-time, streaming generation. Here we show that camera motion, object trajectories, and depth can be unified into a single 3D point-track representation, from which one model performs joint camera and object control, depth editing, and motion transfer in a single forward pass. To learn this interface at scale, we mine in-the-wild video for 3D motion supervision, yielding OpenVidHD-Motion3D, and encode it with a lightweight Geometric Motion Head that plugs into a pretrained video diffusion model. Because this encoder is temporally separable, we distill the model into a causal streaming student that generates arbitrarily long video in four denoising steps at memory independent of length. This unified design surpasses prior camera-only, 2D, and offline-3D methods in motion-control precision while covering modalities they address only in isolation. 4DStreamCtrl runs at 20 FPS on a single high-end GPU for 480p video and stays temporally coherent over hundreds of frames, enabling, to our knowledge, interactive 4D-controllable streaming generation for the first time. More broadly, grounding generation in explicit 3D geometry with efficient causal inference points toward interactive world models with closed-loop spatiotemporal control, from controllable simulators to real-time visual imagination for embodied agents.

---


### 81. [DeCO: Discriminative Evidence Composition for Fine-Grained Dataset Distillation](https://arxiv.org/abs/2608.25480)

**<font color=#1a73e8>作者：</font>** Chuixuan Fan, Guang Li, Shijie Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dataset distillation compresses a large training set into a compact synthetic set while preserving its downstream utility. However, existing methods primarily preserve global image statistics and may overlook the localized evidence essential for fine-grained visual classification (FGVC), such as object parts, subtle textures, and region-specific structures. We formulate fine-grained dataset distillation as budgeted discriminative-evidence preservation and propose Discriminative Evidence Composition (DeCO). DeCO uses attention rollout from a pretrained TransFG teacher to identify informative patches, applies spatial diversification to reduce redundant coverage, and organizes the resulting regions into class-wise evidence banks. Multiple same-class regions are then packed into compact grid-composed images. The teacher is used only for dataset construction, whereas downstream students are trained with standard hard-label supervision without teacher logits. Experiments on CUB-200-2011, FGVC-Aircraft, and Stanford Cars show that DeCO consistently outperforms representative coreset and dataset-distillation baselines under different IPC budgets.

---


### 82. [Gaussian Splatting Underwater: A Controlled Cross-Regime Study](https://arxiv.org/abs/2608.25483)

**<font color=#1a73e8>作者：</font>** Olaya Álvarez-Tuñón, Stella Graßhof  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The underwater environment is challenging for 3D reconstruction, because particles suspended in the water scatter and diffuse light, turbidity varies, absorption depends on wavelength, and illumination is rarely uniform. Methods based on Gaussian splatting have generally been developed for conditions that allow good image quality, and have primarily been tested on relatively shallow water. This paper examines how well Gaussian splatting performs across publicly available underwater datasets representing different degrees of turbidity, loss of illumination, and colour attenuation, together with an industrial survey. Five systems with public code are run under one protocol, with shared poses, initialisation, budget, and evaluator, to establish their relative advantages, disadvantages, and limitations. What these methods can do turns out to depend more on the setup than on the architecture. Water clarity binds upstream of rendering, since structure-from-motion registers 99.5 \% of frames in clear water and 0.0 \% at 12 NTU. Illumination geometry decides whether a medium model helps at all: under an artificial light that moves with the camera, medium-blind splatting beats both medium-aware systems. On the survey the benchmark's photometric leader comes last, beaten on geometry by a restoration pre-pass in front of vanilla 3DGS---and none of it is visible in the scores the field reports. Scene builds, per-run configurations, and evaluation code are released at this https URL

---


### 83. [ScentEcho: Exploring Adsorbent Materials for Accurate Odor Collection and Playback](https://arxiv.org/abs/2608.25494)

**<font color=#1a73e8>作者：</font>** Chih-Hung Lee, Yuchi Sun, Rui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Delivering odors that feel realistic and recognizable remains a core challenge for olfactory interaction systems, particularly in applications that demand precise scent delivery. A key limitation lies in the difficulty of capturing, preserving, and playing back real-world scent sources in a reliable and scalable manner. This study explores the potential of adsorbent materials for supporting realistic scent playback. We present ScentEcho, a portable system that enables modular scent collection and release. Through user evaluations, we identify which adsorbent materials tend to perform better for specific odors, and observe that perceived intensity strongly influences similarity ratings. In addition, odor recognition follows a graded pattern, with users moving from broad category identification to more specific source recognition as similarity increases. These findings offer practical insights for designing olfactory interfaces that are both expressive and perceptually aligned with user expectations.

---


### 84. [Pose-Anchored Optical Flow for Low-Latency Human Action Anticipation in Human-Robot Teaming](https://arxiv.org/abs/2608.25495)

**<font color=#1a73e8>作者：</font>** Lewis de Zoete Grundy, Chris McCarthy, Christopher Fluke  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-robot interaction (HRI) requires robots to interpret human actions early in their execution in order to respond safely, efficiently, and naturally. However, many existing approaches to human action recognition rely either on sparse skeletal representations, which lack fine-grained motion cues, or dense optical flow, which can be computationally expensive for low-latency perception pipelines. In this paper, we propose PoseOFF, a pose-anchored optical flow representation that captures local motion information around human joints to support earlier human intent understanding. By conditioning motion feature extraction on human pose, PoseOFF encodes localised motion dynamics at semantically meaningful body locations, forming a structured motion representation that is explicitly aligned with human kinematics. We evaluate PoseOFF across multiple benchmark datasets and backbone architectures for action anticipation, demonstrating consistent improvements in recognition accuracy, particularly at early observation ratios. Our results show that PoseOFF enables models to achieve comparable or improved performance while observing less of the action sequence, highlighting its effectiveness for early prediction. Importantly, these gains are achieved without requiring full-frame motion processing, making the approach practical for real-time and resource-constrained settings. These findings suggest that pose-centred motion representations such as PoseOFF can enhance the ability of interactive robot systems to infer human actions earlier, supporting more responsive and anticipatory behaviour in human-robot interaction scenarios.

---


### 85. [FedQoS: Federated QoS-Risk Learning for Heterogeneous Indoor-Outdoor Access Selection](https://arxiv.org/abs/2608.25496)

**<font color=#1a73e8>作者：</font>** Nguyen Van Thieu, Ti Ti Nguyen, Ons Aouedi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable access selection in dynamic and heterogeneous indoor-outdoor environments is challenging because instantaneous radio measurements alone cannot capture future QoS degradation caused by mobility, blockage, traffic load, and resource competition. This paper proposes FedQoS, a federated QoS-risk learning framework for predicting the future reliability of candidate access links and supporting access-node selection without centralizing user-level network data. In FedQoS, each access node locally learns from its observed network logs, including radio, traffic, load, and service-context features, while a global QoS-risk predictor is trained through federated aggregation. The learned model estimates the probability of QoS failure for each candidate link, and the controller uses these risk scores to select reliable access nodes under dynamic network conditions. To evaluate the framework, we construct physics-based synthetic indoor-outdoor wireless datasets using the Sionna framework, covering normal traffic, mobility, event-driven congestion, and non-IID client observations. Simulation results show that learning-based access selection substantially reduces the QoS-failure rate compared with signal-based and historical-QoS heuristic methods. FedQoS achieves near-centralized predictive performance and provides clear reliability gains under mild non-IID data while remaining competitive under the more challenging severe non-IID condition. These results demonstrate the potential of federated QoS-risk learning for reliable, data-local access selection in dynamic wireless environments.

---


### 86. [OpenVeinNet: Robust Open-Set Finger Vein Verification with Dynamic Snake Convolution and Graph Learning](https://arxiv.org/abs/2608.25515)

**<font color=#1a73e8>作者：</font>** Sushrut Patwardhan, Raghavendra Ramachandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finger vein verification is a promising biometric modality for secure authentication because vascular patterns are internal, difficult to observe externally, and relatively resistant to presentation attacks. However, reliable verification remains challenging in open-set settings, where test identities are unseen during training and non-enrolled probes must be rejected at inference. This paper presents OpenVeinNet, a finger vein verification framework designed for cross-dataset and open-set evaluation. The proposed model combines Dynamic Snake Convolution with graph-based feature modelling. Dynamic Snake Convolution extracts local curvilinear and tubular vein structures using adaptive sampling, while the graph convolutional backbone models long-range topological relationships between vein regions. To improve the discriminative quality of the embedding space, we introduce a Centroid Angular Hybrid Loss, which jointly encourages intra-class compactness and inter-class angular separation for cosinesimilaritybased verification. Experiments are conducted on five public finger vein datasets: FV-300, MMCBNU, FV-USM, PolyU, and VERA. The method is evaluated using leaveonedatasetout training under both enrolmentbased unknownrejection and fullsubject verification protocols, and is compared with handcrafted and recent deep learning-based baselines. The results show that OpenVeinNet achieves strong cross-dataset generalisation, consistently low equal error rates, and competitive true accept rates at fixed false accept rate operating points. Ablation studies further confirm the individual and combined contributions of adaptive tubular feature extraction, graph-based relational modelling, and the proposed loss function. These findings indicate that explicitly modelling local vein geometry, global vascular relationships, and angularly compact embeddings is effective for openset finger vein verification.

---


### 87. [Asymmetric Cross-Modal Fine-Grained Visual Categorization: ACF-Net and the BirdPro Benchmark](https://arxiv.org/abs/2608.25520)

**<font color=#1a73e8>作者：</font>** Bohan Deng, Shuo Ye, Zitong Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual cross-modal Fine-Grained Visual Categorization (FGVC) aims to identify fine-grained categories by jointly leveraging visual and auditory information. However, FGVC under asymmetric cross-modal scenarios has received limited attention, where paired video and audio are not strictly synchronized and may not even correspond to the same individual or moment. Such weak and ambiguous cross-modal correspondence poses substantial challenges to effective representation learning and modality alignment. To address these issues, we propose ACF-Net, a novel optical flow-guided framework for asymmetric audio-visual fine-grained learning. ACF-Net consists of two key modules: Optical Flow-Guided Motion (OFGM) and Asymmetric CrossModal Adaptive Fusion (ACAF). OFGM captures motion-sensitive visual cues and suppresses irrelevant background interference, thereby enhancing discriminative dynamic representations in videos. ACAF estimates modality reliability under weakly matched audio-video pairs and performs uncertainty-aware adaptive fusion to improve category-level recognition robustness. To support research on asymmetric cross-modal FGVC, we further construct BirdPro, a new bird-oriented audio-visual benchmark, since existing datasets often lack large-scale category-level audio-video associations under non-strict temporal and instance correspondence. BirdPro contains 1,919 audio recordings and 11,965 videos covering 194 bird species. Extensive experiments show that ACF-Net achieves the best results compared with representative baseline methods, outperforming the strongest baselines by 2.97% and 1.92% in the fused and mismatched settings, respectively.

---


### 88. [The Well-Being Palette: An Action-Word Selection Tool Designed for Low-Burden Reflection on Workplace Well-Being](https://arxiv.org/abs/2608.25527)

**<font color=#1a73e8>作者：</font>** Nobuhiko Muramoto, Takayuki Nagaya, Tomoko Tanaka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Background: Workplace well-being interventions need formats that can be used repeatedly with minimal disruption to daily work. We developed the Well-Being Palette, a web-based action-word selection tool designed for brief, low-burden reflection on workplace well-being. Methods: In a three-month exploratory field study at a private-sector corporate research institute in Japan, 88 analyzed participants selected up to three well-being-related action words after reflecting on positive actions or experiences from each workday. We examined application usage, PERMA Profiler scores, selected-word patterns across departments, selected-word diversity using Shannon entropy, and exploratory associations with sharing workshops. Results: During the formal intervention period, the application captured 3,480 input records and 10,104 selected words, and all 72 available action words were selected. Overall PERMA scores increased from baseline to post-intervention, and no clear decline was observed at the one-month follow-up among available cases. Application logs revealed departmental differences in selected-word categories. Cumulative selected-word diversity increased over time, and sharing workshops showed exploratory associations with more sustained PERMA patterns and broader cumulative selected-word diversity. Conclusion: The Well-Being Palette was feasible for repeated use in a real workplace and provided complementary log-based information on how workers recognized and labeled well-being-related experiences. The findings should be interpreted as exploratory and hypothesis-generating, because the study did not include a randomized control condition and did not directly measure perceived burden or completion time.

---


### 89. [Resilient Decentralized Wireless Federated Learning via Gradient Tracking with AdamW](https://arxiv.org/abs/2608.25535)

**<font color=#1a73e8>作者：</font>** Nguyen Van Thieu, Ti Ti Nguyen, Ons Aouedi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wireless Internet-of-Things (IoT) edge networks require decentralized learning (DecL) methods that can operate reliably under both heterogeneous local data and communication-constrained wireless links. However, existing decentralized optimization schemes often incur substantial communication overhead and degraded performance when transmissions are constrained by strict airtime budgets, fading channels, and packet losses. This paper proposes QEF-GT-AdamW, a communication-efficient and outage-resilient algorithm for DecL over wireless communication (WCom) networks. The proposed method combines gradient tracking to mitigate the effect of non-IID data, AdamW-based adaptive optimization to improve training stability, and dual-stream biased quantization with error feedback to reduce communication payloads for both model and tracking exchanges. To address unreliable broadcast communication, the proposed framework further employs a local fallback strategy when scheduled packets are not successfully received. We explicitly model the effect of bandwidth, transmit power, airtime constraints, and fading channels on DecL performance, and establish convergence guarantees for the proposed algorithm under compressed and unreliable wireless communication. Experimental results on heterogeneous MNIST and CIFAR-10 settings show that QEF-GT-AdamW consistently improves robustness and convergence performance over representative DecL baselines while achieving favorable accuracy-communication trade-offs under limited wireless resources.

---


### 90. [CropCop: An Auditable 120-Class Plant-Health Model from Benchmark Reconstruction to a Quantised Runtime Artifact](https://arxiv.org/abs/2608.25539)

**<font color=#1a73e8>作者：</font>** Rana Muhammad Ahmed, Sabahat Abbas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A plant-health score can appear precise while resting on duplicated image families, a long-tailed label space, or a runtime file that was never evaluated. We present CropCop, a closed-set recognition system spanning 120 operational plant-health classes and an evidence chain from corpus reconstruction to direct execution of the final quantised artifact. Starting from 117,546 audited images, we rejected the inherited partition after confirming 3,233 duplicate relationships across split boundaries and froze a 109,107-image benchmark with zero crossings among the audited trusted leakage groups and a 151.7 largest-to-smallest class ratio. A fully fine-tuned DINOv3 ConvNeXt-Tiny reference achieved 98.51% accuracy and 96.87% macro-F1 on the locked internal test. A compact MobileNetV4 Conv-Medium derivative achieved 98.46% accuracy and 96.27% macro-F1 without being presented as evidence for a new distillation method. Validation-only post-training quantisation selected dynamic activations with per-channel weights, and the final 22.60 MiB ExecuTorch/XNNPACK PTE achieved 98.46% accuracy and 96.23% macro-F1 when executed directly. Only six of 16,363 top-1 decisions changed between the converted INT8 graph and the PTE, while paired analysis showed a modest class-balanced loss; an exploratory post hoc fruit-label slice localized a larger recall decline than aggregate accuracy revealed. CropCop establishes strong leakage-controlled internal recognition and software-runtime fidelity; it does not establish performance on unseen farms, camera pipelines, or physical Android hardware.

---


### 91. [Beyond Optimal Rates in Stochastic Optimization: Trajectory-Adaptive Stopping Rules](https://arxiv.org/abs/2608.25551)

**<font color=#1a73e8>作者：</font>** Liviu Aolaritei, Lucas Lévy, Francis Bach 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic gradient descent (SGD) is typically analyzed at a deterministic horizon chosen before the algorithm is run, even though practical stopping decisions are made adaptively by inspecting the evolving trajectory. This mismatch creates a fundamental certification problem: fixed-time guarantees do not generally remain valid at data-dependent stopping times, while deterministic horizons derived from worst-case bounds can be highly conservative. We address this problem for strongly convex stochastic optimization by constructing fully observable, trajectory-adaptive upper confidence sequences for the squared distance of the last iterate to the optimizer and the suboptimality of a weighted average. These bounds hold simultaneously over time, attain the optimal $1/t$ decay rate up to iterated-logarithmic factors in the worst case, and adapt to the realized stochastic gradients, allowing SGD to stop as soon as a prescribed accuracy is certified without sacrificing statistical validity. Our approach treats the evolving SGD trajectory as a sequential experiment whose observations provide evidence about the unknown optimization error. To formalize this perspective, we develop new recursive confidence-sequence techniques and a general time-uniform empirical Bernstein inequality for adapted processes with time-varying conditional means and predictable ranges that may grow without bound. We further extend these confidence-sequence constructions to minibatch SGD, with the empirical Bernstein bounds exploiting the realized second-moment structure within each minibatch. Numerical experiments show that the resulting stopping rules can require several orders of magnitude fewer iterations than natural deterministic horizons.

---


### 92. [AdaVDR: Adaptive Tool Use and Reflection for Video Deep Research](https://arxiv.org/abs/2608.25559)

**<font color=#1a73e8>作者：</font>** Xintong Zhang, Xiaomeng Fan, Shilin Yan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video deep research answers complex questions by jointly understanding video content and retrieving external knowledge from the open Web. However, diverse questions and videos require different tool-use strategies, and inappropriate tool calls can produce incorrect results. Uncertain grounding and retrieval also make unnecessary interactions costly and error-prone, increasing latency and reasoning errors. To address these challenges, we propose AdaVDR, an adaptive video deep research agent with adaptive tool invocation and reflection. AdaVDR selects tools according to the task and its capabilities, and backtracks only when unreliable intermediate results require correction. To enable these capabilities, we develop a video deep research data construction pipeline. We first discover retrieval-relevant events and entities in diverse videos and acquire detailed information through grounding and external retrieval to construct high-quality QA pairs. For each QA, task-specific prompts organize the information acquisition process into a tool-use trajectory, allowing different question and video types to follow different grounding and retrieval strategies. We further introduce model-conditioned tool necessity filtering, which evaluates tool calls against the target model's video understanding and internal knowledge, removing tools or tool chains the model can bypass. This yields trajectories tailored to the target model's video understanding capability and knowledge. Using this pipeline, we construct training data and VDR-EE, a benchmark covering entity-centric and event-centric questions. We perform supervised fine-tuning followed by reinforcement learning with a redundancy-aware reward to strengthen adaptive tool invocation and reflection. Experiments show that our method performs best among the evaluated open-source models on VDR-EE and substantially improves over its base models on VideoDR.

---


### 93. [Physics-Informed Foresight Pruning for Sparse PINN Solvers of Nonlinear PDEs](https://arxiv.org/abs/2608.25564)

**<font color=#1a73e8>作者：</font>** Ahmad Ishaque Karimi, Uvini Balasuriya Mudiyanselage, Kookjin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) often rely on over-parameterized models to optimize coupled solution and differential-residual objectives, leaving unclear how much capacity is necessary and what pruning should preserve. We study foresight pruning at initialization for sparse PirateNet PDE solvers. Standard neural tangent kernel spectrum-aware pruning (NTK-SAP) aims to preserve output-side training dynamics but may overlook parameters whose main influence arises through derivatives in the governing equations. We introduce physics-informed spectrum-aware pruning (PI-SAP), which assigns saliency using sensitivity of the PDE residual. Experiments on the Gray-Scott equations, complex Ginzburg-Landau equation, Burgers' equation, and linear convection equation show that PI-SAP more consistently preserves Gray-Scott residual fidelity and is competitive under aggressive sparsity. However, no criterion is uniformly optimal across equations or sparsity levels. Small-batch PINN-NTK diagnostics further show that residual fidelity, solution accuracy, and kernel conditioning are distinct objectives, motivating pruning methods that explicitly balance solution-side and residual-side training dynamics during optimization.

---


### 94. [Maru: Information Architecture as a Shared Language for Generating Aligned and Persistent User Interfaces](https://arxiv.org/abs/2608.25565)

**<font color=#1a73e8>作者：</font>** Eunhye Kim, DaEun Choi, Bryan Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative user interfaces (GenUIs) promise on-demand components tailored to users' needs. As users iterate on information tasks, they construct personal structures over information they encounter---how items are grouped, what gets prioritized, and what terms mean in their context. Yet, current systems leave these structural decisions to the model at each generation, ignoring the structural logic users have established. Without a persistent representational structure shared between user and system, GenUIs have no basis to remain aligned with what users have established. We draw on Information Architecture (IA), a design practice for organizing and structuring information, as a shared language to bridge user-constructed structure and system generation. We present a framework identifying four IA elements---partition, hierarchy, order, and vocabulary---and characterize how each maps to concrete UI generation decisions. We instantiate this framework in Maru, a conversational system that captures user prompts and interactions as IA preferences, persisting as rules both user and system draw on across generations. A user study revealed that IA persistence kept generated UIs aligned as sessions progressed, while alignment without it degraded, with diverse patterns emerging across users and contexts, pointing to the value of IA persistence in aligning GenUI to individual needs.

---


### 95. [CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression](https://arxiv.org/abs/2608.25568)

**<font color=#1a73e8>作者：</font>** Haobo Xiong, Shaobo Liu, Kai Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To reduce deployment cost and retraining overhead, adapting pretrained learned image compression (LIC) models to downstream machine vision tasks has attracted growing attention. However, existing methods typically insert fine-tuning modules independently into frozen backbones, lacking explicit mechanisms for cross-layer coordination. To address this limitation, we propose a novel framework named CrossMambaTuning, which integrates State Space Models with cross-layer interaction mechanisms for parameter-efficient fine-tuning. Specifically, we design an efficient Mamba adapter equipped with task-specific prompts and multi-scale branching to precisely capture both local features and global dependencies. Furthermore, we introduce a Scale-Invariant Cross-Layer Adapter (SICA) utilizing a parameter-sharing strategy to fuse task information across different scales and reduce redundancy. Extensive experiments demonstrate that CrossMambaTuning achieves state-of-the-art (SOTA) performance on multiple machine vision tasks, reducing parameter overhead by 72\% compared to SOTA methods. Code is available at this https URL.

---


### 96. [Are Concept Bottleneck Models Effective as Decision-Support Systems?](https://arxiv.org/abs/2608.25581)

**<font color=#1a73e8>作者：</font>** Alessandro Bogani, Nicola Debole, Emanuele Marconato 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs) are interpretable-by-design neural networks that detect human-understandable concepts from the input and use them to generate predictions. By allowing users to inspect the concepts underlying a prediction and explore how predictions change under alternative concept configurations, CBMs have emerged as one of the most prominent approaches to supporting human-AI collaboration. However, user studies investigating their actual effectiveness as decision-support systems remain limited. We present two large-scale user studies (N participants = 705, N observations = 6,959) evaluating how concept-based explanations and user interventions on the model's concepts affect the performance of the human-AI team in two distinct binary classification tasks. Our results show that CBMs, and particularly their interactive component, can improve human-AI team accuracy relative to both unaided human performance and performance with non-interpretable AI support. However, these benefits emerge only under certain conditions: classification tasks perceived as difficult, easily identifiable concepts, and active interaction with the model. We also discuss how inaccurate concept detection may undermine users' trust in the model. Overall, this work provides practical guidance for the deployment of CBMs as effective decision-support tools.

---


### 97. [Individual Fairness in Hierarchical Clustering](https://arxiv.org/abs/2608.25586)

**<font color=#1a73e8>作者：</font>** Binita Maity, Shrutimoy Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical clustering produces ultrametric representations that impose strong global geometric constraints and may distort local similarities in ways that disproportionately affect individual data points. We study hierarchical clustering under an individual fairness requirement that bounds relative distortion within local $k$-nearest neighborhoods. We formulate this requirement as a feasibility problem over dominated ultrametrics and characterize the minimal multiplicative slack required for feasibility. We identify a sharp local threshold, prove stability under bounded perturbations, establish monotonicity in $k$, and show an intrinsic $\Theta(\log n)$ separation between local and global realizability. Experiments on synthetic and real world datasets support our theoretical results.

---


### 98. [M-Fibration Theory with Applications to Neural Network Compression](https://arxiv.org/abs/2608.25598)

**<font color=#1a73e8>作者：</font>** Paolo Boldi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The purpose of this paper is to provide a general, comprehensive, theoretical framework that allows one to deal with fibrations on graphs labelled on a commutative monoid. This is a genuine extension of the theory of graph fibrations (as introduced in "Fibrations of Graphs" [Discrete Math., vol. 243, pp. 21-66, 2002]), that makes it possible to deal with weighted graphs, and also graphs labelled with other algebraic structures. The derived theory also lends itself naturally to consider approximate fibrations. As an example, we show how this framework can be applied to the compression of arbitrary neural networks (including CNNs), providing a strong theoretical underpinning to the recent results in "The role of fibration symmetries in geometric deep learning" [Proc. Natl. Acad. Sci. USA, vol. 123, no. 4, p. e2416552123, 2026]

---


### 99. [Defending the Peg: Real-Time Dynamic Protection and Anomaly Detection in DeFi Stablecoins](https://arxiv.org/abs/2608.25600)

**<font color=#1a73e8>作者：</font>** Hengxing Zeng, Shipeng Ye, Xiaoqi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of the Decentralized Finance (DeFi) ecosystem, stablecoins have emerged as a critical infrastructure bridging the cryptocurrency market with traditional financial paradigms. However, stablecoin systems rely heavily on smart contracts to execute automated operations. The immutable nature of these systems post-deployment means that the exploitation of security vulnerabilities can lead to irreversible, massive economic losses and potentially trigger systemic financial risks. Current research on stablecoin smart contract security faces challenges such as a lack of domain-specific targeting and the obsolescence of static defense models. To address this, this paper systematically analyzes common attack vectors in stablecoin environments and proposes a practical, real-time dynamic defense architecture. By analyzing 12 real-world security incidents, we elucidate the underlying mechanisms of high-risk patterns such as reentrancy attacks, oracle manipulation, and composite flash loan attacks. Concurrently, we construct a real-time anomaly detection model utilizing multi-dimensional on-chain temporal features and the Bi-LSTM algorithm. Experimental results demonstrate that this model achieves a classification accuracy of 96.61\%, with an average recall rate of 97.70\% for malicious attack samples, and a single inference latency ranging from 1.5 to 2.8 milliseconds.

---


### 100. [A Dual-Transformer for Multi-Camera View Recommendation](https://arxiv.org/abs/2608.25601)

**<font color=#1a73e8>作者：</font>** Josep Cabacas-Maso, Carles Ventura, Ismael Benito-Altamirano  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-camera systems are foundational to modern media production, and multi-camera editing is a critical task. This involves the proper selection of the appropriate camera view at each moment. In this paper, we propose a novel Dual-Transformer architecture with Cross-Attention that heavily outperformed the current SOTA models over the TVMCE dataset (TV Shows Multicamera Editing dataset). Our model decouples these tasks: (1) a dedicated temporal encoder first processes the sequence of past frames to build a rich memory of the recent history, and (2) the candidate camera views then act as queries to this memory via a cross-attention module, allowing each candidate to independently interrogate the historical context and find the most relevant information for its own evaluation.
Our approach achieved 56.60% Precision@0.5, representing a substantial improvement over the prior best result of 37.16%. We further conducted an ablation study exploring the use of lightweight backbone architectures, where the SwinV2 backbone yielded the best performance, achieving 69.65% Precision@0.5.
Using this best-performing configuration, we then investigated the feasibility of adapting the model to replicate the editing style of a specific human editor. To this end, we fine-tuned the model using varying proportions of the initial segment of a target video. Our results demonstrate that even with only 20% of the video used for fine-tuning, the model exhibited measurable improvements in Precision@0.5, indicating strong potential for data-efficient personalization of editing style adapted to each individual TV show or producer.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-171](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
