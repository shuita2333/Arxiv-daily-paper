# 📦 其他研究 | 2026年05月03日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

---

### 201. [Collaborative Agent Reasoning Engineering (CARE): A Three-Party Design Methodology for Systematically Engineering AI Agents with Subject Matter Experts, Developers, and Helper Agents](https://arxiv.org/abs/2604.28043)

**<font color=#1a73e8>作者：</font>** Rahul Ramachandran, Nidhi Jha, Muthukumaran Ramasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Collaborative Agent Reasoning Engineering (CARE), a disciplined methodology for engineering Large Language Model (LLM) agents in scientific domains. Unlike ad-hoc trial-and-error approaches, CARE specifies behavior, grounding, tool orchestration, and verification through reusable artifacts and systematic, stage-gated phases. The methodology employs a three-party workflow involving Subject-Matter Experts (SMEs), developers, and LLM-based helper agents. These helper agents function as facilitation infrastructure, transforming informal domain intent into structured, reviewable specifications for human approval at defined gates. CARE addresses the "jagged technological frontier", characterized by uneven LLM performance, by bridging the gap between novice and expert analysts regarding domain constraints and verification practices. By generating concrete artifacts, including interaction requirements, reasoning policies, and evaluation criteria, CARE ensures agent behavior is specifiable, testable, and maintainable. Evaluation results from a scientific use case demonstrate that this stage-gated, artifact-driven methodology yields measurable improvements in development efficiency and complex-query performance.

---


### 202. [TAFA-GSGC: Group-wise Scalable Point Cloud Geometry Compression with Progressive Residual Refinement](https://arxiv.org/abs/2604.28045)

**<font color=#1a73e8>作者：</font>** Xiumei Li, Alexander Kopte, André Kaup  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scalable compression is essential for bandwidth-adaptive transmission, yet most learned codecs are optimized for a fixed rate-distortion point, making rate adaptation costly due to re-encoding or maintaining multiple bitstreams. In this work, we propose TAFA-GSGC, a scalable learned point cloud geometry codec that enables multi-quality decoding from a single bitstream and a single trained model. TAFA-GSGC combines layered residual refinement with channel-group entropy coding, and introduces Target-Aligned Feature Aggregation module to reduce cross-layer redundancy in enhancement residuals. Our framework supports up to 9 decodable quality levels with monotonic quality improvement as more subbitstreams are received, while maintaining strong compression efficiency. Compared with the baseline PCGCv2, TAFA-GSGC attains comparable and slightly better RD performance, achieving average BD-Rate savings of -4.99% in D1 and -5.92% in D2.

---


### 203. [Agent-Agnostic Evaluation of SQL Accuracy in Production Text-to-SQL Systems](https://arxiv.org/abs/2604.28049)

**<font color=#1a73e8>作者：</font>** Taslim Jamal Arif, Kuldeep Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL (T2SQL) evaluation in production environments poses fundamental challenges that existing benchmarks do not address. Current evaluation methodologies whether rule-based SQL matching or schema-dependent semantic parsers assume access to ground-truth queries and structured database schema, constraints that are rarely satisfied in real-world deployments. This disconnect leaves production T2SQL agents largely unevaluated beyond developer-time testing, creating silent quality degradation with no feedback mechanism for continuous improvement. We present STEF (Schema-agnostic Text-to-SQL Evaluation Framework), a production-native evaluation system that operates exclusively on natural language inputs the user question, an enriched reformulation, and the generated SQL without requiring database schema or reference queries. STEF extracts semantic specifications from both natural language and SQL representations, performs normalized feature alignment, and produces an interpretable 0 to 100 accuracy score via a composite metric that encompasses filter alignment, semantic verdict, and confidence of the evaluator. Key contributions include: enriched question quality validation as a first-class evaluation signal, configurable application-specific rule injection via prompt templating, and production-robust normalization handling GROUP BY tolerance, ORDER BY defaults, and LIMIT heuristics. Empirical results demonstrate that STEF enables continuous production monitoring and agent improvement feedback loops without schema dependency, making structured query evaluation viable at scale for the first time.

---


### 204. [PROMISE-AD: Progression-aware Multi-horizon Survival Estimation for Alzheimer's Disease Progression and Dynamic Tracking](https://arxiv.org/abs/2604.28055)

**<font color=#1a73e8>作者：</font>** Qing Lyu, Jeremy Hudson, Mohammad Kawas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Individualized Alzheimer's disease (AD) progression prediction requires models that use irregular visits, account for censoring, avoid diagnostic leakage, and provide calibrated horizon risks. We propose PROgression-aware MultI-horizon Survival Estimation for Alzheimer's Disease (PROMISE-AD), a leakage-safe survival framework for predicting conversion from cognitively normal (CN) to mild cognitive impairment (MCI) and from MCI to AD dementia using ADNI/TADPOLE tabular histories. PROMISE-AD converts pre-index visits into tokens with standardized measurements, missingness masks, longitudinal changes, time-normalized slopes, visit timing, and non-diagnostic categorical attributes. A temporal Transformer fuses global, attention-pooled, and latest-visit representations to estimate a progression score and latent discrete-time mixture hazards. Training combines survival likelihood, horizon-specific focal risk loss, progression ranking, hazard smoothness, and mixture-balance regularization, followed by validation-set isotonic calibration for 1-, 2-, 3-, and 5-year risks. In held-out testing across three seeds, PROMISE-AD achieved an integrated Brier score (IBS) of 0.085 $\pm$ 0.012, C-index of 0.808 $\pm$ 0.015, and mean time-dependent AUC of 0.840 $\pm$ 0.081 for CN-to-MCI conversion, yielding the lowest IBS among compared methods. For MCI-to-AD conversion, PROMISE-AD achieved the highest C-index (0.894 $\pm$ 0.018) and near-ceiling 5-year discrimination (AUROC 0.997 $\pm$ 0.003; AUPRC 0.999 $\pm$ 0.001), although some baselines had lower IBS. Ablations and interpretability supported longitudinal change features, fused temporal representations, mixture hazards, cognitive and functional measures, APOE4 status, and recent conversion-proximal visits. These findings suggest that progression-aware survival modeling can provide interpretable multi-horizon AD conversion risk estimates.

---


### 205. [3D Reconstruction Techniques in the Manufacturing Domain: Applications, Research Opportunities and Use Cases](https://arxiv.org/abs/2604.28064)

**<font color=#1a73e8>作者：</font>** Chialoon Cheng, Kaijun liu, Zhiyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This comprehensive review examines the evolution and the current state of the art in three-dimensional (3D) reconstruction techniques in manufacturing applications. The analysis covers both traditional approaches and emerging deep learning methods, showing a critical research gap in unified 3d reconstruction frameworks. Through systematic review of 106 recent publications, we classify reconstruction techniques into three primary categories: data acquisition, point cloud generation, post-processing and applications. Non-contact methods, particularly structured light scanning and stereo vision, have shown significant adoption in manufacturing, with 47% of surveyed applications focusing on quality inspection. The integration of deep learning has enhanced reconstruction accuracy and processing speed, particularly in feature extraction and matching. Key applications span design and development (13%), machining (8%), process (17%), assembly (22%), and quality inspection (40%). While current technologies achieve sub-millimeter accuracy in controlled environments, challenges persist in handling reflective surfaces and dynamic environments. Our findings indicate a trend toward hybrid systems combining multiple sensor types and processing methods to overcome individual limitations. This survey provides a structured framework for understanding current capabilities and future directions in manufacturing-focused 3D reconstruction.

---


### 206. [A Unified Framework of Hyperbolic Graph Representation Learning Methods](https://arxiv.org/abs/2604.28070)

**<font color=#1a73e8>作者：</font>** Sofía Pérez Casulo, Marcelo Fiori, Bernardo Marenco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic geometry has emerged as an effective latent space for representing complex networks, owing to its ability to capture hierarchical organization and heterogeneous connectivity patterns using low-dimensional embeddings. As a result, numerous hyperbolic graph representation learning methods have been proposed in recent years. However, their practical adoption and systematic comparison remain challenging, as implementations are fragmented and shared tools for reproducible and fair evaluation are lacking. In this work, we introduce a unified open-source framework for hyperbolic graph representation learning that integrates several widely used embedding methods under a common optimization interface. The novel framework enables consistent training, visualization, and evaluation of hyperbolic embeddings, and interfaces seamlessly with standard network analysis tools. Leveraging this unified setup, we conduct an experimental study of hyperbolic embedding methods on real-world networks, focusing on two canonical downstream tasks: link prediction and node classification. Beyond predictive accuracy, the study offers practical insights into the strengths and limitations of existing approaches, thereby facilitating informed method selection and fostering reproducible research in hyperbolic graph representation learning.

---


### 207. [AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078)

**<font color=#1a73e8>作者：</font>** Yujin Han, Yujie Wei, Yefei He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid advances in photorealistic video generation, real-world applications such as filmmaking require video aesthetics, e.g., harmonious colors and cinematic lighting, beyond visual fidelity. Prior work on visual aesthetics largely focuses on images, often reducing aesthetics to coarse definitions, e.g., visual pleasure, without a rigorous and systematic evaluation. To improve video aesthetics, we propose a hierarchical rubric that decomposes video aesthetics into three core dimensions, Visual Aesthetics (VA), Visual Fidelity (VF), and Visual Plausibility (VP), with 15 fine-grained criteria, e.g., shot composition. This framework enables a large-scale expert-annotated preference dataset and an evaluation benchmark, AesVideo-Bench, containing about 2500 video pairs with expert annotations on VA, VF, and VP. We then build a family of Video Aesthetic Reward Models (AesRM): AesRM-Base, which directly predicts pairwise preferences on these dimensions to provide efficient post-training rewards, and AesRM-CoT, which additionally generates CoT aligned with all 15 criteria to improve assessment interpretability. Specifically, we train AesRM with a three-stage progressive scheme: (1) Atomic Aesthetic Capability Learning, which strengthens AesRM's recognition of fundamental aesthetic concepts, e.g., accurately identifying centered composition; (2) Cold-Start, aligning the model with structured reasoning protocols; and (3) GRPO, further improving evaluation accuracy. To enhance AesRM-CoT, we additionally propose self-consistency-based CoT synthesis to improve CoT quality and design CoT-based process rewards during GRPO. Extensive experiments show AesRM outperforms baselines on multiple aesthetics benchmarks and is more robust, with lower position bias. Finally, we align Wan2.2 with AesRM and observe clear aesthetic gains over existing aesthetic reward models.

---


### 208. [What Makes a Good Terminal-Agent Benchmark Task: A Guideline for Adversarial, Difficult, and Legible Evaluation Design](https://arxiv.org/abs/2604.28093)

**<font color=#1a73e8>作者：</font>** Ivan Bercovich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Terminal-agent benchmarks have become a primary signal for measuring the coding and system-administration capabilities of large language models. As the market for evaluation environments grows, so does the pressure to ship tasks quickly, often without thorough adversarial review of the verification logic. This paper is a guideline for writing good benchmark tasks, drawn from over a year of contributing to and reviewing tasks for Terminal Bench. Most people write benchmark tasks the way they write prompts. They shouldn't. A prompt is designed to help the agent succeed; a benchmark is designed to find out if it can. We argue that good tasks are adversarial, difficult, and legible, and that a large class of common failure modes -- AI-generated instructions, over-prescriptive specifications, clerical difficulty, oracle solutions that assume hidden knowledge, tests that validate the wrong things, and reward-hackable environments -- are predictable consequences of treating task authoring as prompt authoring. We catalog these failure modes, argue that real difficulty is conceptual rather than environmental, and discuss recent empirical evidence that over 15% of tasks in popular terminal-agent benchmarks are reward-hackable. We hope this serves as a useful reference for benchmark maintainers, task contributors, and researchers using benchmark scores as evidence.

---


### 209. [UHR-Net: An Uncertainty-Aware Hypergraph Refinement Network for Medical Image Segmentation](https://arxiv.org/abs/2604.28095)

**<font color=#1a73e8>作者：</font>** Shuokun Cheng, Jinghao Shi, Kun Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate lesion segmentation is crucial for clinical diagnosis and treatment planning. However, lesions often resemble surrounding tissues and exhibit ill-defined boundaries, leading to unstable predictions in boundary/transition regions. Moreover, small-lesion cues can be diluted by multi-scale feature extraction, causing under- or over-segmentation. To address these challenges, we propose an Uncertainty-Aware Hypergraph Refinement Network (UHR-Net). First, we introduce an Uncertainty-Oriented Instance Contrastive (UO-IC) pretraining strategy that couples geometry-aware copy-paste augmentation with hard-negative mining of lesion-like background regions to improve instance-level discrimination for small and visually ambiguous lesions. Second, we design an Uncertainty-Guided Hypergraph Refinement (UGHR) block, which derives an entropy-based uncertainty map from a coarse probability map to guide hypergraph refinement. By splitting hyperedge prototypes into foreground and background groups, UGHR decouples higher-order interactions and improves refinement in ambiguous regions. Experiments on five public benchmarks demonstrate consistent gains over strong baselines. Code is available at: this https URL.

---


### 210. [Mapping the Methodological Space of Classroom Interaction Research: Scale, Duration, and Modality in an Age of AI](https://arxiv.org/abs/2604.28098)

**<font color=#1a73e8>作者：</font>** Dorottya Demszky, Edith Bouton, Alison Twiner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Research on classroom interaction has long been divided between large-scale observation and in-depth ethnographic work. We propose a framework mapping this methodological space along three dimensions--scale, duration, and modality--where a study's position shapes what it reveals and obscures. We illustrate it through contrasting studies of dialogic teaching--Howe et al. (2019) and Snell and Lefstein (2018)--and an interview with the lead researchers, organized around three questions: what can be operationalized, what mechanisms become visible, and what translates to practice. We then examine how AI is expanding this space and how the framework can guide research and tool design.

---


### 211. [FiLMMeD: Feature-wise Linear Modulation for Cross-Problem Multi-Depot Vehicle Routing](https://arxiv.org/abs/2604.28102)

**<font color=#1a73e8>作者：</font>** Arthur Corrêa, Paulo Nascimento, Samuel Moniz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving practical multi-depot vehicle routing problems (MDVRP) is a challenging optimization task central to modern logistics, increasingly driven by e-commerce. To address the MDVRP's computational complexity, neural-based combinatorial optimization methods offer a promising scalable alternative to traditional approaches. However, neural-based methods typically rely on rigid architectures and input encodings tailored to specific problem formulations. In real-world settings, heterogeneous constraints create multiple MDVRP variants, limiting the applicability of such models. While multi-task learning (MTL) has begun to accelerate the development of unified neural-based solvers, prior works focus almost exclusively on single-depot VRPs, leaving the MDVRP unaddressed. To bridge this gap, we propose Feature-wise Linear Modulation for Cross-Problem Multi-Depot Vehicle Routing (FiLMMeD), a novel unified neural-based model for 24 different MDVRP variants. We introduce three main contributions: (1) to improve the model's generalization, we augment the standard Transformer encoder with Feature-wise Linear Modulation (FiLM), which dynamically conditions learned internal representations based on the active set of constraints; (2) we provide an initial demonstration of Preference Optimization in the MTL setting, establishing it as a superior alternative to Reinforcement Learning for future MTL works; (3) to mitigate the generalization gap caused by the introduction of multi-depot constraints, we introduce a targeted curriculum learning strategy that progressively exposes the model to increasingly more complex constraint interactions. Extensive experiments on 24 MDVRP variants (including 8 novel formulations) and 16 single-depot VRPs confirm the effectiveness of FiLMMeD, which consistently outperforms state-of-the-art baselines. Our code is available at: this https URL

---


### 212. [Neural Aided Kalman Filtering for UAV State Estimation in Degraded Sensing Environments](https://arxiv.org/abs/2604.28107)

**<font color=#1a73e8>作者：</font>** Akhil Gupta, Erhan Guven  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate state estimation of nonlinear dynamical systems is fundamental to modern aerospace operations across air, sea, and space domains. Online tracking of adversarial unmanned aerial vehicles (UAVs) is especially challenging due to agile nonlinear motion, noisy and sparse sensor measurements, and unknown control inputs; conditions that violate key assumptions of classical Kalman filter variants and degrade estimation performance. Neural networks (NNs) can learn complex nonlinear relationships from data, but lack principled uncertainty quantification, which is critical for state estimation tasks where confidence bounds drive downstream decisions. We address this with Bayesian Neural Networks (BNNs), which model uncertainty through distributions over network weights and produce predictive means and uncertainties via Monte Carlo sampling. Building on this, we propose the Bayesian Neural Kalman Filter (BNKF): a hybrid framework coupling a trained BNN with a Kalman correction step for robust online UAV state estimation. Unlike related neural Kalman approaches, BNKF produces full state predictions and incorporates Bayesian uncertainty directly into covariance propagation, improving robustness under high noise conditions. We evaluate BNKF under varying radar noise levels and sampling rates using synthetic nonlinear UAV flight data. Five fold cross validation demonstrates that BNKF outperforms Extended and Unscented Kalman Filters in accuracy, precision, and truth containment under degraded sensing. An ensemble variant (BNKFe) further improves precision in high-noise edge cases at a slight accuracy tradeoff. Runtime analysis confirms minimal inference overhead, supporting real-time deployment feasibility.

---


### 213. [Auto-FlexSwitch: Efficient Dynamic Model Merging via Learnable Task Vector Compression](https://arxiv.org/abs/2604.28109)

**<font color=#1a73e8>作者：</font>** Junqi Gao, Dazhi Zhang, Zhichang Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging has attracted attention as an effective path toward multi-task adaptation by integrating knowledge from multiple task-specific models. Among existing approaches, dynamic merging mitigates performance degradation caused by conflicting parameter updates across tasks by flexibly combining task-specific parameters at inference time, thereby maintaining high performance. However, these methods require storing independent parameters for each task, resulting in prohibitive storage overhead. To address this issue, we first experimentally demonstrate that the fine-tuned weight increments (referred to as task vectors) exhibit an impulse-like activation pattern and high robustness to low-bit representations. Driven by this insight, we propose T-Switch, which decomposes task vectors into three compact components: a binary sparse mask, a sign vector, and a scalar scaling factor, achieving high-fidelity approximation at high compression ratios. We then introduce Auto-Switch, a training-free merging scheme that automatically composes task vectors via feature similarity retrieval. Building on this, we develop Auto-Switch, a training-free merging scheme that automatically assembles task vectors through feature similarity retrieval. Furthermore, to transform task vector sparsification and quantization from static rules to adaptive learning, we propose FlexSwitch, a learnable framework which jointly optimizes the compression strategy for each model unit via Learnable Gating Sparsification (LGS) and Bit-width Adaptive Selection (BAS), while employing the Sparsity-Aware Storage Strategy (SASS) to select the optimal storage encoding structure. Finally, by incorporating a K-Nearest Neighbor (KNN) inference scheme with a learnable low-rank metric, we present Auto-FlexSwitch, a dynamic model merging approach that supports highly efficient task vector compression.

---


### 214. [Splitting Argumentation Frameworks with Collective Attacks and Supports](https://arxiv.org/abs/2604.28112)

**<font color=#1a73e8>作者：</font>** Matti Berthold, Lydia Blümel, Giovanni Buraglio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work proposes novel splitting techniques for argumentation formalisms that incorporate supports between defeasible elements. We base our studies on bipolar set-based argumentation frameworks (BSAFs) which generalize argumentation frameworks with collective attacks (SETAFs), as well as bipolar argumentation frameworks (BAFs), by incorporating both collective attacks and supports. Notably, BSAFs establish a crucial link to structured argumentation as they naturally capture general (potentially non-flat) assumption-based argumentation. The increase in expressiveness calls for diverse forms of splitting. We consider splits over collective attacks (thereby generalizing the recently proposed splitting techniques for SETAFs), splits over collective supports, as well as splits over both collective attacks and supports. We establish suitable splitting schemata and prove their correctness for the most common argumentation semantics.

---


### 215. [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/abs/2604.28119)

**<font color=#1a73e8>作者：</font>** Usha Bhalla, Thomas Fel, Can Rager 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are widely used to extract interpretable features from neural network representations, often under the implicit assumption that concepts correspond to independent linear directions. However, a growing body of evidence suggests that many concepts are instead organized along low-dimensional manifolds encoding continuous geometric relationships. This raises three basic questions: what does it mean for an SAE to capture a manifold, when do existing SAE architectures do so, and how? We develop a theoretical framework that answers these questions and show that SAEs can capture manifolds in two fundamentally different ways: globally, by allocating a compact group of atoms whose linear span contains the entire manifold, or locally, by distributing it across features that each selectively tile a restricted region of the underlying geometry. Empirically, we find that SAEs suboptimally recover continuous structures, mixing the global subspace and local tiling solutions in a fragmented regime we call dilution. This explains why manifold structure is rarely visible at the level of individual concepts and motivates post-hoc unsupervised discovery methods that search for coherent groups of atoms rather than isolated directions. More broadly, our results suggest that future representation learning methods should treat geometric objects, not just individual directions, as the basic units of interpretability.

---


### 216. [Beyond Gaussian Bottlenecks: Topologically Aligned Encoding of Vision-Transformer Feature Spaces](https://arxiv.org/abs/2604.28122)

**<font color=#1a73e8>作者：</font>** Andrew Bond, Ilkin Umut Melanlioglu, Erkut Erdem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern visual world modeling systems increasingly rely on high-capacity architectures and large-scale data to produce plausible motion, yet they often fail to preserve underlying 3D geometry or physically consistent camera dynamics. A key limitation lies not only in model capacity, but in the latent representations used to encode geometric structure. We propose S$^2$VAE, a geometry-first latent learning framework that focuses on compressing and representing the latent 3D state of a scene, including camera motion, depth, and point-level structure, rather than modeling appearance alone. Building on representations from a Visual Geometry Grounded Transformer (VGGT), we introduce a novel type of variational autoencoder using a product of Power Spherical latent distributions, explicitly enforcing hyperspherical structure in the bottleneck to preserve directional and geometric semantics under strong compression. Across depth estimation, camera pose recovery, and point cloud reconstruction, we show that geometry-aligned hyperspherical latents consistently outperform conventional Gaussian bottlenecks, particularly in high-compression regimes. Our results highlight latent geometry as a first-class design choice for physically grounded visual and world models.

---


### 217. [Normativity and Productivism: Ableist Intelligence? A Degrowth Analysis of AI Sign Language Translation Tools for Deaf People](https://arxiv.org/abs/2604.28125)

**<font color=#1a73e8>作者：</font>** Nina Seron-Abouelfadil, Poppy Fynes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sign languages, of any geographical or accentual variation, understandably face continuous scrutiny under the ever present popularity of verbal dictation and audism. Through this, many potential problems arise with the current lack of accessible communication for those who rely on such sign languages for essential conversation. Such AI systems regularly take the form of recognition and interpretation models, designed to provide seamless and accurate translation. In reality these systems are built from biased data and created without any input from deaf communities. Such models are widely used and accepted by their hearing counterparts who remain ignorant to the inherent culture, semantics and colloquial language present in gestural language systems.
This phenomenon is best analysed under the scope of The Technological System and Technological bluff by Ellul. Indeed, what is at play here is the standardization of language by technicians into what can be captured by technique: data, statistics, a mathematical language. For that AI technique to exist, sign language must be rationalized, in a search for profit that annihilates the conditions for communication and fails to capture the human experience of the deaf person. By that process, it presents normative effects, creating a model of Man, standardized, massified, and who has to adapt to the tool and technical milieu instead of the other way around, which we assume should have been the goal of such a technology.
Technique thus reshapes what it means to be human, to submit deaf people to the goals of productivity and efficiency. In doing so, it exhibits clear counter productivity, alienating instead of emancipating, isolating instead of nourishing human relationships. Therefore this paper argues for the idea of AI as Ableist Intelligence, as such systems seek to emphasise the humiliated and marginalised nature of sign.

---


### 218. [AdvDMD: Adversarial Reward Meets DMD For High-Quality Few-Step Generation](https://arxiv.org/abs/2604.28126)

**<font color=#1a73e8>作者：</font>** Xu Wang, Zexian Li, Litong Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models offer superior generation quality at the expense of extensive sampling steps.
Distillation methods, with Distribution Matching Distillation (DMD) as a popular example, can mitigate this issue, but performance degradation remains pronounced when sampling steps are limited.
Reinforcement learning (RL) has been leveraged to improve the few-step generation quality during distillation, with the potential to even surpass the performance of the teacher model. However, existing approaches are combinatorial in nature, merely integrating an RL process with the distillation process, which introduces unnecessary complexities. To address this gap, we propose AdvDMD, a method that seamlessly unifies DMD distillation and RL.
Specifically, AdvDMD employs the adversarially trained discriminator from DMD2 as the reward model, which assigns low scores to generated images and high scores to real ones.
It is trained on both intermediate and final states of the denoising process and updated online with the distilled model, enabling a holistic supervision of the sampling trajectories and mitigating reward hacking.
We adopt a unified SDE backward simulation and a different training schedule for DMD and RL to enable a more stable and efficient training.
Experimental results demonstrate that the 4-step AdvDMD outperforms the original 40-step model for SD3.5 on DPG-Bench, while achieving significant performance gains for SD3 on the GenEval.
On Qwen-Image, our 2-step AdvDMD achieves superior performance over TwinFlow.

---


### 219. [MoCapAnything V2: End-to-End Motion Capture for Arbitrary Skeletons](https://arxiv.org/abs/2604.28130)

**<font color=#1a73e8>作者：</font>** Kehong Gong, Zhengyu Wen, Dao Thien Phong 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent methods for arbitrary-skeleton motion capture from monocular video follow a factorized pipeline, where a Video-to-Pose network predicts joint positions and an analytical inverse-kinematics (IK) stage recovers joint rotations. While effective, this design is inherently limited, since joint positions do not fully determine rotations and leave degrees of freedom such as bone-axis twist ambiguous, and the non-differentiable IK stage prevents the system from adapting to noisy predictions or optimizing for the final animation objective. In this work, we present the first fully end-to-end framework in which both Video-to-Pose and Pose-to-Rotation are learnable and jointly optimized. We observe that the ambiguity in pose-to-rotation mapping arises from missing coordinate system information: the same joint positions can correspond to different rotations under different rest poses and local axis conventions. To resolve this, we introduce a reference pose-rotation pair from the target asset, which, together with the rest pose, not only anchors the mapping but also defines the underlying rotation coordinate system. This formulation turns rotation prediction into a well-constrained conditional problem and enables effective learning. In addition, our model predicts joint positions directly from video without relying on mesh intermediates, improving both robustness and efficiency. Both stages share a skeleton-aware Global-Local Graph-guided Multi-Head Attention (GL-GMHA) module for joint-level local reasoning and global coordination. Experiments on Truebones Zoo and Objaverse show that our method reduces rotation error from ~17 degrees to ~10 degrees, and to 6.54 degrees on unseen skeletons, while achieving ~20x faster inference than mesh-based pipelines. Project page: this https URL

---


### 220. [3D-ReGen: A Unified 3D Geometry Regeneration Framework](https://arxiv.org/abs/2604.28134)

**<font color=#1a73e8>作者：</font>** Geon Yeong Park, Roman Shapovalov, Rakesh Ranjan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We consider the problem of regenerating 3D objects from 2D images and initial 3D shapes. Most 3D generators operate in a one-shot fashion, converting text or images to a 3D object with limited controllability. We introduce instead 3D-ReGen, a 3D regenerator that is conditioned on an initial 3D shape. This conceptually simple formulation allows us to support numerous useful tasks, including 3D enhancement, reconstruction, and editing. 3D-ReGen uses a new conditioning mechanism based on VecSet, which allows the regenerator to update or improve the input geometry with consistent fine-grained details. 3D-ReGen learns a widely applicable regeneration prior from off-the-shelf 3D datasets via self-supervised pretext tasks and augmentations, without additional annotations. We evaluate both the geometric consistency and fine-grained quality of 3D-ReGen, achieving state-of-the-art performance in controllable 3D generation across several tasks.

---


### 221. [Beyond Pixel Fidelity: Minimizing Perceptual Distortion and Color Bias in Night Photography Rendering](https://arxiv.org/abs/2604.28136)

**<font color=#1a73e8>作者：</font>** Furkan Kınlı  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Night Photography Rendering (NPR) poses a significant challenge due to the extreme contrast between dark and illuminated areas in scenes, stemming from concurrent capture of severely dark regions alongside intense point light sources. Existing methods, which are mainly tailored for fidelity metrics, reveal considerable perceptual gaps and often detract from visual quality. We introduce pHVI-ISPNet, a novel RAW-to-RGB framework built on the robust HVI color space. Our network integrates four distinct key refinements: RAW-domain feature processing and Wavelet-based feature propagation to mitigate high-frequency detail loss; sample-based dynamic loss coefficients to ensure stable learning across varying exposure levels; and loss term based on feature distributions to maintain rigorous color constancy. Evaluations on the dataset introduced in the NTIRE 2025 challenge on NPR confirm our approach achieves competitive fidelity while establishing new state-of-the-art results in both CIE2000 color difference and LPIPS. This validates our perceptually-driven design for high-quality nighttime imaging.

---


### 222. [Global Optimality for Constrained Exploration via Penalty Regularization](https://arxiv.org/abs/2604.28144)

**<font color=#1a73e8>作者：</font>** Florian Wolf, Ilyas Fatkhullin, Niao He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Efficient exploration is a central problem in reinforcement learning and is often formalized as maximizing the entropy of the state-action occupancy measure. While unconstrained maximum-entropy exploration is relatively well understood, real-world exploration is often constrained by safety, resource, or imitation requirements. This constrained setting is particularly challenging because entropy maximization lacks additive structure, rendering Bellman-equation-based methods inapplicable. Moreover, scalable approaches require policy parameterization, inducing non-convexity in both the objective and the constraints. To our knowledge, the only prior model-free policy-gradient approach for this setting under general policy parameterization is due to Ying et al. (2025). Unfortunately, their guarantees are limited to weak regret and ergodic averages, which do not imply that the final output is a single deployable policy that is near-optimal and nearly feasible. In this work we take a different approach to this problem, and propose Policy Gradient Penalty (PGP) method, a single-loop policy-space method that enforces general convex occupancy-measure constraints via quadratic-penalty regularization. PGP constructs pseudo-rewards that yield gradient estimates of the penalized objective, subsequently exploiting the classical Policy Gradient Theorem. We further establish the regularity of the penalized objective, providing the smoothness properties needed to justify the convergence of PGP. Leveraging hidden convexity and strong duality, we then establish global last-iterate convergence guarantees, attaining an $\epsilon$-optimal constrained entropy value with $\epsilon$ bounded constraint violation despite policy-induced non-convexity. We validate PGP through ablations on a grid-world benchmark and further demonstrate scalability on two challenging continuous-control tasks.

---


### 223. [On the Proper Treatment of Units in Surprisal Theory](https://arxiv.org/abs/2604.28147)

**<font color=#1a73e8>作者：</font>** Samuel Kiegeland, Vésteinn Snæbjarnarson, Tim Vieira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Surprisal theory links human processing effort to the predictability of an upcoming linguistic unit, but empirical work often leaves the notion of a unit underspecified. In practice, experimental stimuli are segmented into linguistically motivated units (e.g., words), while pretrained language models assign probability mass to a fixed token alphabet that typically does not align with those units. As a result, surprisal-based predictors depend implicitly on ad hoc procedures that conflate two distinct modeling choices: the definition of the unit of analysis and the choice of regions of interest over which predictions are evaluated. In this paper, we disentangle these choices and give a unified framework for reasoning about surprisal over arbitrary unit inventories. We argue that surprisal-based analyses should make these choices explicit and treat tokenization as an implementation detail rather than a scientific primitive.

---


### 224. [Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists](https://arxiv.org/abs/2604.28158)

**<font color=#1a73e8>作者：</font>** Yujun Wu, Dongxu Zhang, Xinchen Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing research infrastructure is fundamentally document-centric, providing citation links between papers but lacking explicit representations of methodological evolution. In particular, it does not capture the structured relationships that explain how and why research methods emerge, adapt, and build upon one another. With the rise of AI-driven research agents as a new class of consumers of scientific knowledge, this limitation becomes increasingly consequential, as such agents cannot reliably reconstruct method evolution topologies from unstructured text. We introduce Intern-Atlas, a methodological evolution graph that automatically identifies method-level entities, infers lineage relationships among methodologies, and captures the bottlenecks that drive transitions between successive innovations. Built from 1,030,314 papers spanning AI conferences, journals, and arXiv preprints, the resulting graph comprises 9,410,201 semantically typed edges, each grounded in verbatim source evidence, forming a queryable causal network of methodological development. To operationalize this structure, we further propose a self-guided temporal tree search algorithm for constructing evolution chains that trace the progression of methods over time. We evaluate the quality of the resulting graph against expert-curated ground-truth evolution chains and observe strong alignment. In addition, we demonstrate that Intern-Atlas enables downstream applications in idea evaluation and automated idea generation. We position methodological evolution graphs as a foundational data layer for the emerging automated scientific discovery.

---


### 225. [Continuous-tone Simple Points: An $\ell_0$-Norm of Cyclic Gradient for Topology-Preserving Data-Driven Image Segmentation](https://arxiv.org/abs/2604.28159)

**<font color=#1a73e8>作者：</font>** Wenxiao Li, Faqiang Wang, Yuping Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Topological features play an essential role in ensuring geometric plausibility and structural consistency in image analysis tasks such as segmentation and skeletonization. However, integrating topology-preserving learning based on simple points into deep learning tasks remains challenging, as existing simple point detection methods are confined to binary images and are non-differentiable, rendering them incompatible with gradient-based optimization in modern deep learning. Moreover, morphological and purely data-driven approaches often fail to guaranty topological consistency. To address these limitations, we propose a novel method that directly computes simple points on continuous-valued images, enabling differentiable topological inference. Building on this theory, we develop an efficient skeleton extraction algorithm that preserves topological structures in binary and continuous-valued images. Furthermore, we design a variational model that enforces topological constraints by preserving topologically non-removable (i.e., non-simple) points, which can be seamlessly integrated into any deep neural network segmentation with softmax or sigmoid outputs. Experimental results demonstrate that the proposed approach effectively improves topological integrity and structural accuracy across multiple benchmarks. The codes are available in this https URL.

---


### 226. [Essential, Yet Overlooked: Identity Verification Barriers for Blind and Low Vision People in Government Services](https://arxiv.org/abs/2604.28166)

**<font color=#1a73e8>作者：</font>** Ryan John Oommen, Tanusree Sharma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Identity verification is a critical gateway to accessing government services and public benefits, yet contemporary systems are typically designed around visual interaction, leaving blind and low vision (BLV) individuals disproportionately burdened. In this work, we examine how BLV users navigate identity verification in government services and how current designs shape their access, security, and autonomy. Through a mixed methods study combining analysis of 219 Reddit posts and semi-structured interviews with 16 BLV participants, we uncover systemic accessibility breakdowns across both digital and in person verification processes. Our findings show that inaccessible verification workflows do not merely inconvenience users, they restructure how security is achieved in practice. We also identify how repeated verification demands, inaccessible physical infrastructure, and policy changes exacerbate exclusion from essential services. At the same time, participants articulate complex perspectives on AI, viewing it as both a critical accessibility aid and a growing vector for identity fraud.

---


### 227. [PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169)

**<font color=#1a73e8>作者：</font>** Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video diffusion models excel at appearance synthesis but still struggle with physical consistency: objects drift, collisions lack realistic rebound, and material responses seldom match their underlying properties. We present PhyCo, a framework that introduces continuous, interpretable, and physically grounded control into video generation. Our approach integrates three key components: (i) a large-scale dataset of over 100K photorealistic simulation videos where friction, restitution, deformation, and force are systematically varied across diverse scenarios; (ii) physics-supervised fine-tuning of a pretrained diffusion model using a ControlNet conditioned on pixel-aligned physical property maps; and (iii) VLM-guided reward optimization, where a fine-tuned vision-language model evaluates generated videos with targeted physics queries and provides differentiable feedback. This combination enables a generative model to produce physically consistent and controllable outputs through variations in physical attributes-without any simulator or geometry reconstruction at inference. On the Physics-IQ benchmark, PhyCo significantly improves physical realism over strong baselines, and human studies confirm clearer and more faithful control over physical attributes. Our results demonstrate a scalable path toward physically consistent, controllable generative video models that generalize beyond synthetic training environments.

---


### 228. [Action Motifs: Self-Supervised Hierarchical Representation of Human Body Movements](https://arxiv.org/abs/2604.28173)

**<font color=#1a73e8>作者：</font>** Genki Kinoshita, Shu Nakamura, Ryo Kawahara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective human behavior modeling requires a representation of the human body movement that capitalizes on its compositionality. We propose a hierarchical representation consisting of Action Atoms that capture the atomic joint movements and Action Motifs that are formed by their temporal compositions and encode similar body movements found across different overall human actions. We derive A4Mer, a nested latent Transformer to learn this hierarchical representation from human pose data in a fully self-supervised manner. A4Mer splits a 3D pose sequence into variable-length segments and represents each segment as a single latent token (Action Atoms). Through bottom-up representation learning, temporal patterns composed of these Action Atoms, which capture meaningful temporal spans of reusable, semantic segments of body movements, naturally emerge (Action Motifs). A4Mer achieves this with a unified pretext task of masked token prediction in their respective latent spaces. We also introduce Action Motif Dataset (AMD), a large-scale dataset of multi-view human behavior videos with full SMPL annotations. We introduce a novel use of cameras by mounting them on the feet to achieve their frame-wise annotations despite frequent and heavy body occlusions. Experimental results demonstrate the effectiveness of A4Mer for extracting meaningful Action Motifs, which significantly benefit human behavior modeling tasks including action recognition, motion prediction, and motion interpolation.

---


### 229. [Strait: Perceiving Priority and Interference in ML Inference Serving](https://arxiv.org/abs/2604.28175)

**<font color=#1a73e8>作者：</font>** Haidong Zhao, Nikolaos Georgantas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) inference serving systems host deep neural network (DNN) models and schedule incoming inference requests across deployed GPUs. However, limited support for task prioritization and insufficient latency estimation under concurrent execution may restrict their applicability in on-premises scenarios. We present \emph{Strait}, a serving system designed to enhance deadline satisfaction for dual-priority inference traffic under high GPU utilization. To improve latency estimation, Strait models potential contention during data transfer and accounts for kernel execution interference through an adaptive prediction model. By drawing on these predictions, it performs priority-aware scheduling to deliver differentiated handling. Evaluation results under intense workloads suggest that Strait reduces deadline violations for high-priority tasks by 1.02 to 11.18 percentage points while incurring acceptable costs on low-priority tasks. Compared to software-defined preemption approaches, Strait also exhibits more equitable performance.

---


### 230. [Stop Holding Your Breath: CT-Informed Gaussian Splatting for Dynamic Bronchoscopy](https://arxiv.org/abs/2604.28179)

**<font color=#1a73e8>作者：</font>** Andrea Dunn Beltran, Daniel Rho, Aarav Mehta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bronchoscopic navigation relies on registering endoscopic video to a preoperative CT scan, but respiratory motion deforms the airway by 5-20 mm, creating CT-to-body divergence that limits localization accuracy. In practice, this is mitigated through breath-hold protocols, which attempt to match the intraoperative anatomy to a static CT, but are difficult to reproduce and disrupt clinical workflow. We propose to eliminate the need for breath-hold protocols by leveraging patient-specific respiratory modeling. Paired inhale-exhale CT scans, already acquired for planning, implicitly define the patient-specific deformation space of the breathing airway. By registering these scans, we reduce respiratory motion to a single scalar breathing phase per frame, constraining all reconstructions to anatomically observed configurations. We embed this representation within a mesh-anchored Gaussian splatting framework, where a lightweight estimator infers breathing phase directly from endoscopic RGB, enabling continuous, deformation-aware reconstruction throughout the respiratory cycle without breath-holds or external sensing. To enable quantitative evaluation, we introduce RESPIRE, a physically grounded bronchoscopy simulation pipeline with per-frame ground truth for geometry, pose, breathing phase, and deformation. Experiments on RESPIRE show that our approach achieves geometrically faithful reconstruction, over 20x faster training, and 1.22 mm target localization accuracy (within the 3mm clinically relevant tolerances) outperforming unconstrained single-CT baselines. Please check out our website for additional visuals: this https URL

---


### 231. [An adaptive wavelet-based PINN for problems with localized high-magnitude source](https://arxiv.org/abs/2604.28180)

**<font color=#1a73e8>作者：</font>** Himanshu Pandey, Ratikanta Behera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, physics-informed neural networks (PINNs) have gained significant attention for solving differential equations, although they suffer from two fundamental limitations, namely, spectral bias inherent in neural networks and loss imbalance arising from multiscale phenomena. This paper proposes an adaptive wavelet-based PINN (AW-PINN) to address the extreme loss imbalance characteristic of problems with localized high-magnitude source terms. Such problems frequently arise in various physical applications, such as thermal processing, electro-magnetics, impact mechanics, and fluid dynamics involving localized forcing. The proposed framework dynamically adjusts the wavelet basis function based on residual and supervised loss. This adaptive nature makes AW-PINN handle problems with high-scale features effectively without being memory-intensive. Additionally, AW-PINN does not rely on automatic differentiation to obtain derivatives involved in the loss function, which accelerates the training process. The method operates in two stages, an initial short pre-training phase with fixed bases to select physically relevant wavelet families, followed by an adaptive refinement that adapts scales and translations without populating high-resolution bases across entire domains. Theoretically, we show that under certain assumptions, AW-PINN admits a Gaussian process limit and derive its associated NTK structure. We evaluate AW-PINN on several challenging PDEs featuring localized high-magnitude source terms with extreme loss imbalances having ratios up to $10^{10}:1$. Across these PDEs, including transient heat conduction, highly localized Poisson problems, oscillatory flow equations, and Maxwell equations with a point charge source, AW-PINN consistently outperforms existing methods in its class.

---


### 232. [Synthetic Computers at Scale for Long-Horizon Productivity Simulation](https://arxiv.org/abs/2604.28181)

**<font color=#1a73e8>作者：</font>** Tao Ge, Baolin Peng, Hao Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Realistic long-horizon productivity work is strongly conditioned on user-specific computer environments, where much of the work context is stored and organized through directory structures and content-rich artifacts. To scale synthetic data creation for such productivity scenarios, we introduce Synthetic Computers at Scale, a scalable methodology for creating such environments with realistic folder hierarchies and content-rich artifacts (e.g., documents, spreadsheets, and presentations). Conditioned on each synthetic computer, we run long-horizon simulations: one agent creates productivity objectives that are specific to the computer's user and require multiple professional deliverables and about a month of human work; another agent then acts as that user and keeps working across the computer -- for example, navigating the filesystem for grounding, coordinating with simulated collaborators, and producing professional artifacts -- until these objectives are completed.
In preliminary experiments, we create 1,000 synthetic computers and run long-horizon simulations on them; each run requires over 8 hours of agent runtime and spans more than 2,000 turns on average. These simulations produce rich experiential learning signals, whose effectiveness is validated by significant improvements in agent performance on both in-domain and out-of-domain productivity evaluations. Given that personas are abundant at billion scale, this methodology can in principle scale to millions or even billions of synthetic user worlds with sufficient compute, enabling broader coverage of diverse professions, roles, contexts, environments, and productivity needs. We argue that scalable synthetic computer creation, together with at-scale simulations, is highly promising as a foundational substrate for agent self-improvement and agentic reinforcement learning in long-horizon productivity scenarios.

---


### 233. [Representation Fréchet Loss for Visual Generation](https://arxiv.org/abs/2604.28190)

**<font color=#1a73e8>作者：</font>** Jiawei Yang, Zhengyang Geng, Xuan Ju 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We show that Fréchet Distance (FD), long considered impractical as a training objective, can in fact be effectively optimized in the representation space. Our idea is simple: decouple the population size for FD estimation (e.g., 50k) from the batch size for gradient computation (e.g., 1024). We term this approach FD-loss. Optimizing FD-loss reveals several surprising findings. First, post-training a base generator with FD-loss in different representation spaces consistently improves visual quality. Under the Inception feature space, a one-step generator achieves0.72 FID on ImageNet 256x256. Second, the same FD-loss repurposes multi-step generators into strong one-step generators without teacher distillation, adversarial training or per-sample targets. Third, FID can misrank visual quality: modern representations can yield better samples despite worse Inception FID. This motivates FDr$^k$, a multi-representation metric. We hope this work will encourage further exploration of distributional distances in diverse representation spaces as both training objectives and evaluation metrics for generative models.

---


### 234. [Generalizable Sparse-View 3D Reconstruction from Unconstrained Images](https://arxiv.org/abs/2604.28193)

**<font color=#1a73e8>作者：</font>** Vinayak Gupta, Chih-Hao Lin, Shenlong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scenes from sparse, unposed images remains challenging under real-world conditions with varying illumination and transient occlusions. Existing methods rely on scene-specific optimization using appearance embeddings or dynamic masks, which requires extensive per-scene training and fails under sparse views. Moreover, evaluations on limited scenes raise questions about generalization. We present GenWildSplat, a feed-forward framework for sparse-view outdoor reconstruction that requires no per-scene optimization. Given unposed internet images, GenWildSplat predicts depth, camera parameters, and 3D Gaussians in a canonical space using learned geometric priors. An appearance adapter modulates appearance for target lighting conditions, while semantic segmentation handles transient objects. Through curriculum learning on synthetic and real data, GenWildSplat generalizes across diverse illumination and occlusion patterns. Evaluations on PhotoTourism and MegaScenes benchmark demonstrate state-of-the-art feed-forward rendering quality, achieving real-time inference without test-time optimization

---


> [!TIP]
> 当前位于：**201-234**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-234**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
