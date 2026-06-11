# 📦 其他研究 | 2026年06月12日

> 本类共 **248** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-248**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-248**

---

### 201. [nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding](https://arxiv.org/abs/2606.12146)

**<font color=#1a73e8>作者：</font>** Boyang Li, Yulin Wu, Sizhe Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary Position Embedding (RoPE) is widely adopted in Transformer models, yet its extension to high-dimensional domains lacks a unified theoretical formulation. Most existing approaches either apply rotations independently along each axis or empirically mix frequencies, which limits cross-dimensional interactions and yields direction-dependent representations. To address these limitations, we propose nD-RoPE, a decomposition-free generalization of RoPE to arbitrary dimensions. From a translation-invariant formulation in continuous Hilbert space, we derive a spectral condition for isotropy that requires treating positions and frequencies as coupled \(n\)-dimensional vectors. We instantiate this formulation with a multi-scale regular-simplex wave-vector design, which provides non-degenerate spatial coverage and a symmetric, directionally balanced second-order response. Experiments across images, videos, and point clouds demonstrate consistent performance gains and improved generalization in high-dimensional settings.

---


### 202. [Towards Responsibly Non-Compliant Machines](https://arxiv.org/abs/2606.12147)

**<font color=#1a73e8>作者：</font>** Marija Slavkovik, Marie Farrell, Louise Dennis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider the problem of engineering autonomous intelligent agents that are capable to responsibly not comply with user requests. We argue that machine non-compliance comes in many different forms, and sketch the issues we should pursue on the road of accomplishing responsibly non-compliant intelligent machines. We anchor responsible non-compliance in justifications for task refusal, pathways to override the non-compliance, as well as careful tracking of security risks and liability transfers.

---


### 203. [TopoCap: Learning Topology-Agnostic Motion Priors for Monocular Video-to-Animation](https://arxiv.org/abs/2606.12153)

**<font color=#1a73e8>作者：</font>** Cheng-Feng Pu, Jia-Peng Zhang, Meng-Hao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The explosion of generative 3D assets has created a massive demand for animation, yet current motion capture methods remain brittle, restricted to species-specific templates (e.g., SMPL) or requiring labor-intensive manual rigging. We introduce TopoCap, the first unified framework capable of extracting motion from monocular video and retargeting it onto characters with arbitrary, unseen skeletal topologies, i.e., from bipeds to hexapods and inanimate objects, without test-time optimization. Our key insight is that while skeletal structures are combinatorial and discrete, the underlying physics of motion occupy a continuous, low-dimensional manifold. We materialize this insight via a two-stage generative pipeline. First, we learn a Universal Motion Manifold using a Graph CVAE that compresses heterogeneous kinematic chains into a shared, fixed-length latent code. By explicitly conditioning the decoder on a structural embedding of the target rig, we disentangle motion dynamics from skeletal topology. Second, we treat video-to-animation as a conditional flow matching problem, predicting these topology-agnostic codes from visual features. To learn this generalized prior, we introduce Mobjaverse, a massive-scale dataset curated from Objaverse-XL. Comprising over 5,000 unique skeletal topologies and 2 million frames, it exceeds the structural diversity of existing datasets by two orders of magnitude. Extensive experiments demonstrate that \MethodMotion outperforms specialist models on human and quadruped benchmarks while enabling zero-shot retargeting for the long tail of 3D creatures. Dataset is publicly available at this https URL.

---


### 204. [Beyond Dark Knowledge: Mixup-Based Distillation for Reliable Predictions](https://arxiv.org/abs/2606.12171)

**<font color=#1a73e8>作者：</font>** José Medina, Paul Honeine, Abdelaziz Bensrhair 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge Distillation (KD) and mixup have proven effective at inducing smoothness in class boundaries; KD captures inherent class relationships in probability distributions, and mixup enforces them through convex combinations of inputs. Their interaction, however, remains poorly understood, particularly when mixup is applied only during student training. In this setting, the teacher is queried on inputs drawn from a vicinal distribution it never saw during training, a controlled mismatch whose effect on knowledge transfer has not been characterised. We show that this mismatch causes the teacher's supervisory signal to be dominated by distributional confusion rather than inter-class structure. Despite it, the student does not merely imitate the teacher: it independently acquires greater linearity in the vicinal region, a structural property that the teacher lacks, and goes beyond dark-knowledge transfer. KD with mixup consistently improves student accuracy and reduces overconfidence by an order of magnitude relative to the baseline, across CIFAR and ImageNet with varying-capacity teachers. Crucially, calibration propagates from teacher to student independently of accuracy transfer, and temperature scaling governs a measurable accuracy-calibration trade-off that becomes more pronounced under vicinal training. These results reframe mixup distillation not as a degraded version of standard KD, but as a richer transfer channel that simultaneously shapes discriminative performance, uncertainty estimation, and representational geometry.

---


### 205. [How Low Can You Go? Active Learning for Sparse Model Discovery in the Ultra-Low-Data Limit](https://arxiv.org/abs/2606.12182)

**<font color=#1a73e8>作者：</font>** Ana Larrañaga, Urban Fasel, Steven L. Brunton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying the governing equations of complex dynamical systems remains a fundamental challenge across science and engineering. While early approaches relied on empirical data and heuristics, modern data-driven methods offer greater flexibility and fewer assumptions. However, data acquisition in real-world settings is often expensive. This work addresses this challenge by introducing an active learning strategy for dynamics discovery in the ultra-low data limit. Rather than sampling randomly, our method iteratively prioritizes regions that are most informative for model identification. This approach builds on Sparse Identification of Nonlinear Dynamics (SINDy), and utilizes an ensemble extension, E-SINDy, to estimate epistemic uncertainty and guide the sampling for both ordinary and partial differential equations (ODEs/PDEs). For ODEs, an exhaustive analysis is conducted on the Lorenz system across varying data budgets and noise levels. For PDEs, two systems with contrasting dynamical characteristics are examined: the Burgers' equation, where a sharp shock front creates a distinction between informative and uninformative regions, and the Kuramoto-Sivashinsky equation, which presents a more spatially complex sampling landscape. Across all scenarios, the proposed method accurately identifies the governing dynamics with significantly fewer data samples than random sampling.

---


### 206. [A Resource for Enthymeme Detection in Controversial Political Discourse](https://arxiv.org/abs/2606.12186)

**<font color=#1a73e8>作者：</font>** Martial Pastor, Nelleke Oostdijk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enthymemes, arguments with unstated premises or conclusions, are pervasive in persuasive discourse, yet their annotation remains notoriously subjective. We present a resource of 1,482 tweets from politically controversial discourse, annotated by five annotators for the presence of enthymemes and their argument structure, designed to study label variation. We first revisit the definition of enthymemes and propose annotation guidelines anchored in Walton's argumentation schemes, offering a structured and constrained approach that nonetheless preserves room for the interpretive nature of the task. This contrasts with past resources, which tend to eliminate disagreement, obscuring its sources and preventing investigation of its potential benefits for model performance. We further propose a complexity analysis of the task, identifying where annotation imposes high cognitive load and may give rise to inconsistent annotation. Our preliminary experiments show that models trained on annotator disagreement outperform models trained on hard majority-vote labels. We close by reflecting on how structural openness in enthymeme definitions and guidelines enables the study of variation in subjective inferential processes for future resources and downstream NLP applications concerned with human inference.

---


### 207. [DynaTok: Token-Based 4D Reconstruction from Partial Point Clouds](https://arxiv.org/abs/2606.12189)

**<font color=#1a73e8>作者：</font>** Weirong Chen, Keisuke Tateno, Hidenobu Matsuki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address 4D reconstruction from partial point cloud sequences, where depth-sensor observations are incomplete, unordered, and lack explicit temporal correspondences. This geometry-only setting is challenging due to missing observations and ambiguous dynamics. While recent progress has largely relied on image-based methods, existing point-based approaches typically focus on single objects, assume relatively complete inputs, or require explicit correspondences. To address these limitations, we propose DynaTok, a point-based framework for correspondence-free 4D reconstruction from partial point cloud sequences without images. DynaTok encodes frames into compact latent tokens, aggregates incomplete observations over time with a Transformer-based spatiotemporal encoder, and decouples geometry and motion through residual tokens in a unified model. A flow-matching decoder then reconstructs complete, temporally consistent 4D point-cloud sequences conditioned on the latent tokens. Experiments on object- and scene-level benchmarks demonstrate improved reconstruction quality and temporal coherence from partial point cloud observations. Project page: this https URL.

---


### 208. [Implicit Neural Representations of Individual Behavior](https://arxiv.org/abs/2606.12200)

**<font color=#1a73e8>作者：</font>** Andrew Kang, Priya Narasimhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study policy representation learning from unlabeled multi-policy behavioral data. Each episode is generated by a fixed policy, but policy labels are unavailable. This setting appears in robotics play, demonstrations, games, racing, and other datasets where heterogeneous behaviors are mixed without annotations. We introduce \emph{Behavioral INR}, a self-supervised generative model that adapts implicit neural representations (INRs) from vision to behavior. Instead of mapping coordinates to RGB values, Behavioral INR represents a policy as a state-action function mapping states to subsequent actions. An episode-level latent modulates this function through FiLM layers, yielding a generative prior over policies and allowing policy identity to be inferred without supervision. Because INRs treat each datapoint as samples from an underlying function, the same model naturally accommodates variable episode lengths and different sampling granularities, as in vision INRs with different image resolutions. We also define policy-level out-of-distribution (OOD) shifts along state-distribution and action-distribution axes, which arise when policies overlap in states or actions but are not captured by standard behavioral OOD settings based only on new agents or environments. We evaluate on synthetic Gaussian random field data, MuJoCo demonstrations with controlled OOD splits, and real-world chess, Formula 1 racing, robotics, and Seek-Avoid datasets. Behavioral INR most consistently improves policy identifiability in the hardest continuous state-action settings, especially when longer episodes, more policies, and OOD splits reduce the usefulness of marginal shortcuts; amortized history encoders remain competitive when policy identity can be recovered from symbolic repetition or low-dimensional action statistics. We release code and checkpoints.

---


### 209. [Can News Predict the Market? Limits of Zero-Shot Financial NLP and the Role of Explainable AI](https://arxiv.org/abs/2606.12210)

**<font color=#1a73e8>作者：</font>** Ali M Karaoglu, Shreyank N Gowda  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can financial news reliably predict short-term stock movements? Despite advances in large language models, this question remains unresolved. We revisit this problem using a zero-shot natural language processing framework, investigating whether models can extract actionable signals from financial news without domain-specific training. We design a structured pipeline that combines zero-shot natural language inference with temporal aggregation, explicitly modelling recency and event-dependent impact horizons when integrating information across articles. To address the need for transparency in high-stakes settings, we introduce a multi-layered explainability framework that links predictions to token-level, article-level, and aggregate evidence, and produces grounded natural language rationales. Across multiple models and prediction horizons, we find that zero-shot approaches consistently fail to outperform simple baselines, with particularly weak performance on negative movements, suggesting deeper structural limitations in mapping news sentiment to short-term price dynamics. However, explainability signals reliably distinguish between trustworthy and unreliable predictions, offering practical value even when accuracy is limited. These findings highlight the limits of zero-shot financial NLP and motivate a shift toward decision-support systems that prioritise transparency and uncertainty awareness. Code: this https URL

---


### 210. [SHERPA: Seam-aware Harmonized ERP Adaptation for Open-Domain 360$^\circ$ Panorama Generation](https://arxiv.org/abs/2606.12213)

**<font color=#1a73e8>作者：</font>** Jungwoon Kang, Jaehun Kim, Yiwon Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic imagery is increasingly used in world-generation, games, and simulation, where users may need not only photorealistic scenes but also stylized and non-photorealistic environments. Large-scale text-to-image diffusion and flow models provide broad style and semantic priors for this goal, but planar image training misaligns them with the wrap-around topology and polar regions of $360^\circ$ panoramas represented in equirectangular projection (ERP). We present SHERPA, a lightweight adaptation framework that combines frequency-selective Circular RoPE, Circular Latent Encoding/Decoding, image-side FFN adapters, and a Dual-Path Training Scheme. Circular RoPE replaces only the seam-sensitive high-frequency horizontal RoPE band with integer-periodic harmonics while preserving the pretrained lower-frequency spectrum. The Paired Panorama Path supervises geometry, while the Unpaired Style Path uses self-supervised yaw consistency for target-free stylized prompts. As a result, SHERPA generates $360^\circ$ panoramas across both photorealistic panorama domains and open-domain stylized prompts.

---


### 211. [Identifying cybersickness causes in virtual reality games using symbolic machine learning algorithms](https://arxiv.org/abs/2606.12214)

**<font color=#1a73e8>作者：</font>** Thiago Porcino, Erick Oliveira Rodrigues, Flavia Bernardini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Virtual reality (VR) and head-mounted displays are constantly gaining popularity in various fields such as education, military, entertainment, and health. Although such technologies provide a high sense of immersion, they can also trigger symptoms of discomfort. This condition is called cybersickness (CS) and is quite popular in recent virtual reality publications. This work proposes a novel experimental analysis using symbolic machine learning to rank potential causes of CS in VR games. We estimate CS causes and rank them according to their impact using classical machine learning. Experiments are performed using two virtual reality games and 6 experimental protocols along with 37 valid samples from a total of 88 volunteers. Our results show that rotation and acceleration triggered cybersickness more frequently in a flight game in contrast to a race game. We could also observe that subjects that are less experienced with VR are more prone to feel discomfort. Former experience plays a more important role on the race game, as this game provides more liberty to the user in terms of controllers, more displacement alternatives and a more user-controlled acceleration. Furthermore, different causes that trigger discomfort arise based on short or long term VR exposures. We suggest strategies for mitigating CS for these two scenarios: short and long term exposure experiences and compare the two highlighted scenarios (race and flight).

---


### 212. [MLT-Dedup: Efficient Large-Scale Online Video Deduplication via Multi-Level Representations and Spatial-Temporal Matching](https://arxiv.org/abs/2606.12215)

**<font color=#1a73e8>作者：</font>** David Yuchen Wang, Haoying Li, Hailun Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The explosive growth of user-generated video content on online platforms is accompanied by the emergence of numerous near-duplicate videos--videos that are identical or highly similar but differ by partial edits. These duplicates degrade user experience and increase storage and bandwidth costs, making large-scale video deduplication a critical task. Existing video deduplication frameworks face a fundamental challenge in retrieving sufficient high-quality candidates under a limited index budget, as well as trade-offs between efficiency and precision. To address these issues, we propose MLT-Dedup, an efficient large-scale online video deduplication framework with Multi-Level representations and spatial-Temporal matching. Our approach employs a Multi-Level Video Encoder (ML-VE) to extract both fine-grained frame-level and sparse clip-level embeddings: sparse embeddings support efficient candidate retrieval, while fine-grained embeddings are loaded for precise pairwise matching. During matching, we introduce DiF-SiM, a Differential Feature-enhanced Similarity Module capable of locating duplicated temporal segments and providing reliable similarity evidence to support policy-driven deduplication decisions. Extensive experiments on a real-world large-scale platform demonstrate that MLT-Dedup reduces online repetition rates by 91% at 90% precision. Furthermore, our sparse retrieval design achieves a 5x increase in indexing capacity, enabling broader candidate coverage in real-world deployment.

---


### 213. [Bridging the Smart City Cybersecurity Data Gap Through AI-Driven Synthetic Dataset Generation](https://arxiv.org/abs/2606.12225)

**<font color=#1a73e8>作者：</font>** Stephanie Polczynski, John D. Hastings, Varghese Vaidyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart cities rely on interconnected cyber-physical systems that integrate sensors, IoT devices, cloud platforms, and AI-driven services and decision-making. While these systems enhance city services, they also introduce complex cybersecurity challenges due to their large attack surfaces, heterogeneous data flows, and evolving threat vectors. Developing and validating cybersecurity tools for smart cities requires high-quality datasets that accurately represent real operational conditions. However, real-world datasets are often incomplete, contain privacy-sensitive data, are difficult to access, or lack sufficient malicious activity to support tool development. This research addresses this critical gap by proposing an AI-based synthetic data generation (SDG) framework designed specifically for smart city cybersecurity research. The proposed framework leverages generative artificial intelligence models to produce high-fidelity synthetic cybersecurity datasets that replicate realistic device behaviors, network interactions, and cyber-attack scenarios. The synthetic datasets are evaluated for conformity to protocol standards, statistical similarity to original datasets, and utility in common security tools. The resulting synthetic data generation framework and evaluation metrics are expected to advance smart city cybersecurity by enabling researchers to model threats more effectively and evaluate defensive techniques more comprehensively to better protect critical smart city infrastructures.

---


### 214. [An Electric Potential-Augmented Benchmark Dataset for Physics-Guided Image Reconstruction of Electrical Capacitance Tomography](https://arxiv.org/abs/2606.12226)

**<font color=#1a73e8>作者：</font>** Xinqi Zhang, Qiming Ma, Lihui Peng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While deep learning has significantly advanced image reconstruction of Electrical Capacitance Tomography (ECT), most data-driven methods map directly between capacitance and permittivity distribution, treating the sensor as a black box. This overlooks the electric potential field -- the fundamental physical link governing the nonlinear and ill-posed ``soft-field'' effect. To address this, we propose an electric potential-augmented ECT benchmark dataset designed to explicitly integrate latent physics behind ECT into the learning process. Generated via a COMSOL-MATLAB pipeline for an eight-electrode sensor as an example, the dataset comprises 20,000 randomized samples across four typical flow patterns. Crucially, alongside the conventional capacitance vectors and permittivity distributions depicted as images, each sample preserves eight excitation-wise full-field potential maps. Beyond data release, we provide illustrative evaluation protocols for both forward and inverse problems of ECT. Through comprehensive testing on both in-distribution (IID) and out-of-distribution (OOD) scenarios, we systematically demonstrate how the inclusion of electric potential maps enhances modeling accuracy and robustness. Fundamentally, the explicit inclusion of latent field information significantly lowers the barrier to integrating physical laws into ECT modeling, thereby establishing a standardized foundation for future physics-guided machine learning of ECT image reconstruction.

---


### 215. [VIA-SD: Verification via Intra-Model Routing for Speculative Decoding](https://arxiv.org/abs/2606.12243)

**<font color=#1a73e8>作者：</font>** Yuchen Xian, Yang He, Yunqiu Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding (SD) addresses the high inference costs of LLMs by having lightweight drafters generate candidates for large verifiers to validate in parallel. Existing draft-verify methods use binary decisions: accept or fully recompute. Yet we find that many rejected tokens can be verified correctly by a slim submodel derived from the full verifier via intra-model routing, instead of the full verifier. This motivates our slim-verifier to handle tokens requiring moderate verification resources, reducing expensive large-model calls. We propose Verification via Intra-Model Routing for Speculative Decoding (VIA-SD), a multi-tier framework using a routed slim-verifier. Draft tokens are processed hierarchically: direct acceptance for high-confidence cases, slim-verifier regeneration for medium-confidence cases, and full-model verification for uncertain cases. Across four representative tasks and multiple model families, VIA-SD reduces rejection rates by 0.10-0.22 and delivers 10-20% speedups over strong SD baselines, while achieving 2.5-3x acceleration over non-drafting decoding. Moreover, VIA-SD is compatible with existing SD frameworks without modifying their training procedures. Our results suggest multi-tier SD as a general paradigm for scalable and efficient LLM inference. Project page: this https URL

---


### 216. [Damage-TriageFormer: A Foundation-Model Framework for Typology-Based Building Damage Assessment from Mono-Temporal Imagery](https://arxiv.org/abs/2606.12248)

**<font color=#1a73e8>作者：</font>** Yiming Xiao, Yu-Hsuan Ho, Sanjay Thasma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Decision-relevant building damage assessment is critical for prioritizing resources and recovery after a disaster, yet most automated methods either flatten damage into a single severity scale (no damage, minor, major, destroyed) or require paired pre- and post-event imagery that is often unavailable for emerging hazards. This paper presents Damage-TriageFormer, a single-image, post-event, footprint-conditioned model that produces a damage typology rather than a severity scale. We contribute: (1) DamageTriage-Bench, a new benchmark built from NOAA Emergency Response Imagery across Hurricane Michael (2018), Hurricane Helene (2024), and the 2025 Los Angeles wildfire complex, with five typology classes that distinguish roof damage from structural damage and, within each, partial from total extent; and (2) Damage-TriageFormer, which extends a DINOv3 ViT-L backbone with a Simple Feature Pyramid for higher-resolution instance pooling, a two-stage gated damage head, and an auxiliary severity-regression objective. Our model achieves macro F1 of 0.624 on validation and 0.619 on a held-out stratified test set, performing strongest where operational triage needs it most, with per-class F1 of 0.91 and 0.84 on undamaged buildings and total structural collapse, respectively. While the rare Total Roof Damage class remains difficult due to its limited examples and an inherently ambiguous label boundary, our results show that single-image post-event imagery can support actionable building damage typing, enabling targeted emergency response and resource allocation without a pre-event reference.

---


### 217. [Reinforcement Learning Disrupts Gradient-Based Adversarial Optimization](https://arxiv.org/abs/2606.12251)

**<font color=#1a73e8>作者：</font>** Xinhai Zou, Chang Zhao, Alireza Aghabagherloo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based adversarial attacks remain a dominant threat to deep neural networks (DNNs), as they exploit gradient information to efficiently optimize adversarial perturbations. To address this, we investigate whether reinforcement learning (RL) training can disrupt the gradient structure used by attackers by training image classifiers with policy-gradient objectives and epsilon-greedy exploration. Through systematic experiments across CIFAR-10, CIFAR-100, and ImageNet-100 with multiple architectures, we find that RL-trained classifiers significantly disrupt gradient-based adversarial optimization. To explain this, we conduct a comprehensive mechanism analysis using loss landscape visualization, static and dynamic gradient indicators, and predictive entropy. Our analysis reveals that RL acts as an implicit regularizer, producing models with highly unstable gradient directions and smaller gradient magnitudes. This combination makes each PGD step both unreliable in direction and limited in magnitude, causing gradient-based attacks to fail within practical iteration budgets. We further show that combining RL with adversarial training (RL-adv) provides a dual-layer defense operating at two complementary levels: RL degrades gradient information available to attackers (gradient-level defense), while adversarial training strengthens decision boundaries (boundary-level defense). RL-adv achieves the highest robustness across all major attack types evaluated, including gradient-based (PGD, AutoAttack), transfer-based, and query-based attacks, outperforming SL-adv by a significant margin. These findings identify RL-induced gradient disruption as a complementary robustness mechanism and motivate future research on hybrid SL-RL training schedules that combine SL's efficiency with RL's gradient-regularization properties.

---


### 218. [Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification](https://arxiv.org/abs/2606.12252)

**<font color=#1a73e8>作者：</font>** Veerendhra Kumar Dangeti, Xiao Gu, Ying Weng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training deep neural networks for clinical time-series analysis is computationally demanding, yet many healthcare settings lack the resources required for repeated model development and deployment. This challenge is particularly evident in electrocardiogram classification, where large datasets and long training schedules make efficiency practically important. Progressive Data Dropout reduces training cost by excluding samples from gradient updates once they are learned, but it relies on model confidence and may retain samples that are difficult due to noise or ambiguity rather than useful signal. In this work, we introduce ERTS, an explainability-based reliability training signal for efficient ECG classification. ERTS uses explanation quality during training to distinguish between informative and unreliable uncertainty. Building on progressive data selection, we compute Grad-CAM attention maps for candidate samples and derive a focus score that measures whether model predictions are supported by coherent and localised patterns. Samples with low focus are filtered out, while those with meaningful attention are prioritised for gradient updates. We evaluate ERTS across three ECG datasets and multiple backbone architectures, showing consistent improvements in macro-F1 alongside reduced effective training cost. These results suggest that explanation quality can serve as a practical signal for improving both efficiency and reliability in clinical time-series learning. Code will be released.

---


### 219. [Bridging Day and Night: Unsupervised Cross-Domain Re-Identification with Synergistic Prompt and Prototype Learning](https://arxiv.org/abs/2606.12258)

**<font color=#1a73e8>作者：</font>** Jiyang Xu, Rui Liu, Hang Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain day-night re-identification (ReID) is fundamentally challenged by the substantial visual appearance discrepancies between daytime and nighttime scenes. Existing fully supervised methods rely heavily on labor-intensive annotations, which are costly and exhibit limited generalization across domains. In this work, we investigate unsupervised day-night ReID and propose a novel framework that synergistically combines prompt learning and prototype-based representation learning to associate identities across domains without requiring manual labels. Our approach follows a progressive two-stage training strategy. In the first stage, we exploit the vision-language model to generate instance-specific textual prompts in an annotation-free manner. We employ an instance-level alignment mechanism to embed visual features and textual prompts into a unified semantic space, aligning unlabeled day/night images with learnable prompts via instance-aware dynamic-bias adaptation. In the second stage, we construct domain-specific prototype memory banks and introduce two complementary modules: i) an intra-domain identity association module to enhance feature discriminability within each domain, and ii) a cross-domain prototype matching module to reliably identify positive and negative prototype pairs, thereby establishing robust identity correspondences across day and night. Extensive experiments on public benchmarks validate the effectiveness of our method. Under the unsupervised setting, our framework attains Rank-1 accuracy comparable to state-of-the-art fully supervised methods.

---


### 220. [Partitioned Tags, Shared Data: Reconciling Strict Cache Isolation with Write-Shared Coherence](https://arxiv.org/abs/2606.12259)

**<font color=#1a73e8>作者：</font>** Kartik Ramkrishnan, Stephen McCamant, Antonia Zhai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cache partitioning is among the strongest structural defenses against eviction-based cache side channels, yet a decade-old design issue has blocked its widespread deployment in secure shared-OS settings. The issue is that write-shared coherence collapses under strict partitioning. We present SCP (Secure and Coherent Partitioning), which combines strict eviction isolation with write-shared coherence by partitioning only the tags, sharing a single data pool, and sizing the data pool so capacity-driven cross-partition eviction cannot occur. Timing obfuscation extends protections to the inter-partition lookup path. Coherence-based leakage on shared-writeable lines is mitigated by routing those writes through to the LLC once a leakage threshold is crossed, which makes attacker write probe latency independent of victim activity.
Using gem5 for implementation, SCP mitigates Prime+Probe and Flush+Reload, which are the basis for more sophisticated cache attacks. We also demonstrate that a shared-writeable-line attack is mitigated. All these attacks yield results no better than random guessing. SCP's hardware cost is a modest +2.8% LLC SRAM. Performance matches DAWG within 0.3% IPC on the SPEC CPU2017 benchmarks that we evaluated. Sharing-intensive microbenchmarks demonstrate a tunable security-performance tradeoff based on a system-specified leakage threshold.

---


### 221. [VOID: Defeating Unauthorized Mimicry in Latent Diffusion Models](https://arxiv.org/abs/2606.12263)

**<font color=#1a73e8>作者：</font>** Chunlin Qiu, Ang Li, Tianxiao Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Latent Diffusion Models (LDMs) have revolutionized visual synthesis, they are increasingly exploited for unauthorized mimicry of individuals. Existing defenses inject deceptive perturbations to steer the generated images toward irrelevant targets. However, this approach hinges on an ungrounded assumption: subtle perturbations can maintain their deceptive efficacy throughout an LDM's extensive generation process. In reality, the model's innate restoration mechanism will remove such perturbations and cause individual identities to re-emerge in the images generated.
We propose VOID, a defense framework that overcomes this conundrum by manipulating an LDM's intrinsic stochasticity. VOID perturbs the diffusion pipeline in two novel ways: 1) amplifying the latent encoding errors to shatter an image's semantic structure, and 2) counteracting the target guidance signals to suppress the model's restoration capabilities. This results in a semantic corruption that thwarts any unauthorized mimicry. Notably, the security gain does not come at the price of visual utility, as VOID simultaneously manages to confine perturbations to human-imperceptible regions of protected images. Our comprehensive evaluation of 24 state-of-the-art defenses against 10 mimicry attacks on 5 datasets demonstrates VOID's unprecedented protection power: it increases the average Frechet Inception Distance (FID) from 113 to 365, a 223% improvement over the strongest defense to date.

---


### 222. [The Impossibility of Eliciting Latent Knowledge](https://arxiv.org/abs/2606.12268)

**<font color=#1a73e8>作者：</font>** Korbinian Friedl, Francis Rhys Ward, Paul Yushin Rapoport 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advanced AI systems have extensive knowledge of their environments; in fact, their knowledge may (far) exceed that of their developers or users. Consequently, a desirable property for an AI system is that it is honest -- that it accurately reports its beliefs about the world. Designing an AI system to be honest may be difficult, especially if we want to ask it questions about latent variables in the environment -- variables which are hidden from the human interacting with it. This gives rise to the problem of eliciting latent knowledge (ELK): the problem of training an AI agent to honestly report its beliefs. In this paper, we make ELK formally precise using Causal Influence Diagrams (CIDs). CIDs can be used to describe the relationship between an agent's training environment and its subjective representation of the world. We use CIDs to formalise the distinction between observable and latent variables, to specify what exactly it means for an agent to be honest, and to formally define goal misgeneralisation. We show that, under certain circumstances, developers can incentivise an agent to honestly answer questions by providing correct feedback during training. However, a natural, but undesirable, way for an agent to generalise is to provide answers which humans would evaluate as true, rather than honest answers. We prove an impossibility theorem stating: There is no feedback-based training strategy that depends only on agent behaviour and with certainty produces an honest agent, even if feedback is perfect during training.

---


### 223. [Finding Multiple Interpretations in Datasets](https://arxiv.org/abs/2606.12277)

**<font color=#1a73e8>作者：</font>** Matthew Chak, Paul Anderson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose an approach to finding sets of similar-performing models (in terms of loss/accuracy measurements) with highly different context-aware characteristics. Through experiments on the METABRIC dataset, we show that the proposed method finds multiple models with highly different gene expressions than those found by the control methodology without performance penalties. We argue that the proposed methodology is important whenever one aims to analyze any global characteristic of a model to extract insight into the underlying phenomenon being studied.

---


### 224. [Finding Sparse Subnetworks in One Training Cycle via Progressive Magnitude-Based Pruning](https://arxiv.org/abs/2606.12278)

**<font color=#1a73e8>作者：</font>** Romana Qureshi, Hafida Benhidour, Said Kerrache 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural network pruning reduces model size by removing less important parameters while aiming to preserve predictive performance. Although the Lottery Ticket Hypothesis (LTH) shows that sparse subnetworks can match dense networks when trained from suitable initializations, its iterative pruning procedure requires multiple complete training cycles. This work evaluates progressive magnitude-based pruning as a single-cycle alternative. The method gradually increases sparsity during training using a linear schedule and updates pruning masks based on active weight magnitudes. We conduct systematic experiments on CIFAR-10 and MNIST across ResNet, VGG-style, and LeNet architectures, comparing the proposed method with representative iterative and initialization-based pruning baselines, including LTH, SNIP, and GraSP. On CIFAR-10, the method achieves 95.12\% accuracy on ResNet-18 at 72.9\% sparsity, compared with 90.5\% reported for LTH. At extreme sparsity, it achieves 93.13\% accuracy on a VGG-like architecture at 97\% sparsity, compared with approximately 92.0\% for SNIP, and 93.44\% accuracy on VGG-19 at 97.97\% sparsity, compared with 92.19\% for GraSP at 98\% sparsity. A sparsity-accuracy analysis on ResNet-18 further shows that accuracy remains within 0.1 percentage points of the dense baseline across 70--85\% sparsity. These results indicate that progressive magnitude-based pruning provides an effective single-cycle approach for neural network sparsification under the evaluated settings.

---


### 225. [CCKS: Consensus-based Communication and Knowledge Sharing](https://arxiv.org/abs/2606.12281)

**<font color=#1a73e8>作者：</font>** Jinyuan Zu, Xiaowei Lv, Yongcai Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In Decentralized Training and Decentralized Execution (DTDE) for cooperative Multi-Agent Reinforcement Learning (MARL), action-advising-based knowledge sharing promotes interpretable and scalable cooperation among agents. However, current action advising approaches often adhere too much to the teacher's guidance without evaluating teacher-student compatibility, which causes excessive advising, suboptimal stability, and degraded performance. To overcome these challenges, this paper presents a Consensus-based Communication and Knowledge Sharing (CCKS) framework, which allows agents to adopt recommendations based on consensus-derived constraints and to follow the teacher's instructions more smartly. This mechanism enables agents to balance exploration and learning from experienced teachers, improving overall performance. The key is the consensus model construction, for which we propose to employ contrastive learning to construct consensus models based on local observations in the agents' training phase. In action selection, agents score and choose actions based on consensus and shared knowledge. Designed as a plug-and-play solution, CCKS integrates seamlessly with existing DTDE algorithms. Experiments conducted in the Google Research Football environment and the complex StarCraft II Multi-Agent Challenge demonstrate that the integration with CCKS significantly improves cooperation efficiency, learning speed, and overall performance compared with current DTDE baselines. The code is available at this https URL.

---


### 226. [CellNet -- Localizing Cells using Sparse and Noisy Point Annotations](https://arxiv.org/abs/2606.12286)

**<font color=#1a73e8>作者：</font>** Benjamin Eckhardt, Dmytro Fishman, Stuart Fawke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counting living cells is an important step in many biological research workflows. Our collaborators at the Wellcome Sanger Institute study vital genes in humans via large scale saturation genome editing screening, which requires repeatedly counting cells a great number of times. Computer Vision based automation is crucial for high throughput and resource efficiency. In this work, we develop a regression-based deep learning computer vision algorithm to detect and count cells in phase-contrast microscopy images. To reduce annotation effort, which in practice often becomes a bottleneck, we focus on counting cells only using sparse point annotations, which are fast and easy to acquire. By comparison to state-of-the-art 0-shot methods, we show that regression-based counting is a promising alternative in low data regimes. Through developing methods to automatically count living cells in microscopy images, we contribute to valuable research on the human genome. The code is available at this https URL.

---


### 227. [The Standard Interpretable Model: A general theory of interpretable machine learning to deductively design interpretable methods using Lagrangian mechanics](https://arxiv.org/abs/2606.12289)

**<font color=#1a73e8>作者：</font>** Pietro Barbiero, Giovanni De Felice, Mateo Espinosa Zarlenga 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence models grow in complexity, interpretability has become an indispensable tool for understanding, debugging, and controlling their computations. However, interpretability lacks general theories to deductively design interpretable methods. This gap between theories and methods results in a fragmented literature and inconsistent evaluation protocols.
To fill this gap, we introduce the Standard Interpretable Model (SIM), a general theory grounded in Lagrangian mechanics that enables the deductive design of interpretable methods. Specifically, the SIM summarises, in a set of premises, what interpretability is for a target user. From these premises, the SIM systematically derives interpretability symmetries and corresponding constraints, which shape the landscape of a Lagrangian whose minima correspond to optimal interpretable models. To reach the minima, one can either update the parameter values of an opaque model to make it more interpretable or compile constraints into an interpretable architecture.
We empirically show that the SIM identifies and solves limitations of existing methods (including traditional, concept-based, and mechanistic interpretability), highlights underexplored research directions, and informs the design of core programming interfaces. Beyond being a research method, the deductive nature of the SIM offers pedagogical grounding for interpretability curricula and may shift the scientific community's perspective of a discipline that has long been fragmented.

---


### 228. [Findings of the MAGMaR 2026 Shared Task](https://arxiv.org/abs/2606.12295)

**<font color=#1a73e8>作者：</font>** Alexander Martin, Dengjia Zhang, Joel Brogan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This overview paper presents the results of the shared task for the second workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR). In this shared task participants submitted systems focused on either (i) video retrieval or (ii) grounded generation of articles given retrieved videos. Teams could submit to either task. For the retrieval task, we had 2 participating teams that submitted a total of 17 systems -- all of which beat a baseline derived from the winner of last year's shared task. On the generation side, we had 4 teams submit 16 systems. All teams had at least one generated report that was labeled the best by a human annotator.

---


### 229. [Natural-Language Temporal Grounding in Hour-Long Videos is a Search Problem: A Benchmark and Empirical Decomposition](https://arxiv.org/abs/2606.12300)

**<font color=#1a73e8>作者：</font>** Sukmin Seo, Geewook Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal grounding--returning the interval $[t_s, t_e]$ for a natural-language query over a video--is the language interface to long-form video, yet has been studied on short videos; the dynamics of hour-scale natural-language grounding remain underexplored. We take the position that at hour-scale, the binding constraint is search, not recognition: Video-LLMs are bottlenecked not by localizing a nearby event, but--given a natural-language query--by searching for the relevant region of a long video. To test this, we release ExtremeWhenBench, the first open hour-scale grounding benchmark (2,273 queries over 194 videos, mean 75.7 min, max 9 hr) with an open-form query distribution. Every open Video-LLM collapses while a frame-level retrieval baseline outperforms them; a failure taxonomy attributes 85% of failures to search; and a retrieve-then-ground hybrid recovers 6.7x over the monolithic Video-LLM--mirroring retrieve-then-read in open-domain QA.

---


### 230. [Anatomically Conditioned Recurrent Refinement for Topology-Aware Circle of Willis Segmentation](https://arxiv.org/abs/2606.12319)

**<font color=#1a73e8>作者：</font>** Juraj Perić, Marija Habijan, Dario Mužević 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting the Circle of Willis (CoW) from Magnetic Resonance Angiography (MRA) is challenging due to complex topology and thin vascular structures that are prone to fragmentation. Standard Convolutional Neural Networks (CNNs) often fail to capture these topological constraints, resulting in "broken vessel" artifacts. To address this, we propose the Anatomically Conditioned Recurrent Refinement U-Net (AC2RUNet). Our architecture decouples segmentation into two streams: a Static Stream that extracts invariant anatomical features and a lightweight Dynamic Stream that iteratively refines topological errors over time. We further introduce a dynamic curriculum learning strategy that transitions from high-recall geometric supervision to topology-aware constraints. Validated on the TopCoW dataset, AC2RUNet substantially reduces Hausdorff Distance (4.72 mm vs 9.17 mm) and Betti number errors (0.19 vs 0.40), improving topological connectivity over the nnU-Net baseline while maintaining comparable volumetric Dice.

---


### 231. [A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents](https://arxiv.org/abs/2606.12320)

**<font color=#1a73e8>作者：</font>** Krti Tallam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise security was built to govern data boundaries: the protected surface was data at rest and in transit, and the controls -- access control, data-loss prevention, perimeter inspection -- governed crossings of that boundary. Production AI agents dissolve this assumption. An agent reads context, calls tools, invokes connectors, and modifies systems of record on an enterprise's behalf, so risk moves inside the workflow, into sequences of individually-permitted actions that may transform a business process no one authorized. Existing policy engines do not extend to this regime: they evaluate request-time decisions against atomic principals, where agentic systems require stateful evaluation against composite principals whose authority attenuates through delegation chains.
We present a reference architecture for the runtime governance of production agents, built from four composable primitives: a five-plane decomposition (a reasoning plane that adjudicates intent, and four enforcement planes -- network, identity, endpoint, data -- that realize the decision), stop-anywhere mediation, composite principals with capability attenuation, and audit as a structured evidence substrate. We define a taxonomy of six interruption primitives that generalize allow and deny, state and argue for four correctness invariants, and demonstrate the foreclosure of seven production-agent threats across five concrete workflows. A reference implementation of the policy-engine core supplies measured evidence: attenuation correctness and evidence reconstructability hold on every trial, adjudication runs in single-digit microseconds, and the audit substrate's tamper-evidence behaves exactly as designed. We are explicit about scope: the architecture governs delegated action, not model behavior, and a full-system evaluation against a live agent benchmark is the invited next step.

---


### 232. [PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents](https://arxiv.org/abs/2606.12329)

**<font color=#1a73e8>作者：</font>** Ripon Chandra Malo, Tong Qiu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI coding assistants now support a growing share of software work, from quick scripts to production applications. Yet these agents remain largely stateless: each new session re-reads project files, re-derives prior decisions, and - most costly - may repeat debugging attempts that already failed. Reconstructing this context can consume an estimated 5,000-20,000 tokens per session; the bottleneck is often not model capability but missing project memory. We present projectmem, an open-source, local-first memory and judgment layer for AI coding agents. projectmem records development as an append-only, plain-text event log of typed events - issues, attempts, fixes, decisions, and notes - and deterministically projects that log into compact, AI-readable summaries served through the Model Context Protocol (MCP). Beyond storage, projectmem adds a deterministic pre-action gate that warns an agent before it repeats a previously failed fix or edits a known-fragile file. We frame this as Memory-as-Governance: memory that does not merely answer the agent but acts on its next action. The system runs fully offline with no telemetry; its immutable log also serves as a provenance trail for reproducible, auditable AI-assisted development. projectmem ships as a three-dependency Python package (14 MCP tools, 19 CLI commands, 37 automated tests) and is evaluated through a two-month self-study across 10 projects comprising 207 logged events. Source code: this https URL.

---


### 233. [Measuring Semantic Progress in Multi-turn Dialogue via Information Gain](https://arxiv.org/abs/2606.12332)

**<font color=#1a73e8>作者：</font>** Paul He, Shiva Kasiviswanathan, Dominik Janzing  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating multi-turn dialogue is challenging because quality emerges across turns rather than within individual responses. We focus on a key dimension of information-seeking dialogue: semantic progress, defined as the accumulation of new, question-relevant, and non-redundant information over the course of a conversation. We formalize semantic progress as question-conditioned uncertainty reduction and introduce an information-theoretic metric that approximates it in embedding space. Our main estimator uses a tractable Gaussian formulation with closed-form updates, while a complementary maximum-entropy argument shows why log-determinant structure arises more broadly when only second-order embedding information is retained. This formulation yields desirable theoretical properties, including monotonicity, additive decomposition of total information gain across turns, and diminishing returns for redundant evidence. Unlike LLM-as-a-judge approaches, our metric requires no autoregressive inference at evaluation time and is fully reproducible for a fixed embedding model. Experiments on MT-Bench, Chatbot Arena, and UltraFeedback show that the proposed metric achieves competitive agreement with human judgments despite targeting only semantic progress, with improved alignment on MT-Bench and UltraFeedback compared to several LLM-based judges. Notably, the method remains effective with lightweight embedding models under CPU-only execution, indicating that semantic progress can be captured without reliance on large model capacity.

---


### 234. [Fourier Features Let Agents Learn High Precision Policies with Imitation Learning](https://arxiv.org/abs/2606.12334)

**<font color=#1a73e8>作者：</font>** Balázs Gyenes, Emiliyan Gospodinov, Jan Frieling 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-precision robotic manipulation requires fine-grained spatial reasoning that is often difficult to achieve with RGB-only policies due to depth ambiguity and perspective scale issues. Policies that leverage 3D information directly, such as those based on point clouds, offer a stronger geometric prior over purely image-based ones, yet their performance remains highly task-dependent. We hypothesize that this discrepancy may be due to the spectral bias of neural networks towards learning low frequency functions, which especially affects architectures conditioned on slow-moving Cartesian features. We thus propose to map point clouds from Cartesian space into high-dimensional Fourier space, effectively equipping the point cloud encoder with direct access to high-frequency features. We experimentally validate the use of Fourier features on challenging manipulation tasks from the RoboCasa and ManiSkill3 benchmarks and on a real robot setup. Despite their simplicity, we find that Fourier features provide significant benefits across diverse encoder architectures and benchmarks and are robust across hyperparameters. Our results indicate that Fourier features let policies leverage geometric details more effectively than Cartesian features, showing their potential as a general-purpose tool for point cloud-based imitation learning. We provide source code and videos on our project page: this https URL

---


### 235. [Echoes of the Prior: A Computational Phenomenology of Forgetting](https://arxiv.org/abs/2606.12340)

**<font color=#1a73e8>作者：</font>** Gege Gao, Bernhard Schölkopf, Andreas Geiger  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Memory is not merely the storage of data; it is the scaffolding of reality. When biological memory fades, the world does not simply turn black; it regresses into an unrecognizable chaos. Echoes of the Prior is an interactive installation that attempts to visualize this subjective phenomenology of forgetting. By inducing controlled synaptic decay within a Feed-Forward 3D Reconstruction model, we create an artistic analogy for the erosion of the brain's predictive priors. We position the Neural Network not as a tool for engineering, but as a cognitive proxy - a silicon brain whose structural degeneration evokes the disorienting, poetic, and terrifying experience of losing one's grip on the world. Ultimately, we offer this framework as a catalyst, inviting the wider community to explore the uncharted potential of neuromorphic aesthetics in visualizing the fragility of intelligence. Interactive demo see this https URL.

---


### 236. [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks](https://arxiv.org/abs/2606.12344)

**<font color=#1a73e8>作者：</font>** Mengyu Zheng, Kai Han, Boxun Li 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-purpose agents such as OpenClaw are increasingly used as autonomous tool users, but their coding ability is difficult to measure under SWE-bench: a generic agent does not by itself satisfy the clean Docker workspace, patch, and prediction contract required for scoring. We introduce Claw-SWE-Bench, a multilingual SWE-bench-style benchmark and adapter protocol that makes heterogeneous agent harnesses, or claws, comparable under fair settings including a fixed prompt, runtime budget, workspace contract, patch extraction procedure, and evaluator. The full benchmark contains 350 GitHub issue-resolution instances across 8 languages and 43 repositories, drawn from SWE-bench-Multilingual and SWE-bench-Verified-Mini after future-commit cleanup. We also release Claw-SWE-Bench Lite for faster validation, which is an 80-instance subset selected by a cost-aware, rank-aware procedure over 17 calibration columns. On the full benchmark, OpenClaw with a minimal direct-diff adapter scores only $19.1\%$ Pass@1, whereas the full adapter reaches $73.4\%$ with the same GLM 5.1 backbone, showing that adapter design is essential for enabling OpenClaw-style harnesses to perform coding tasks effectively. Across an OpenClaw $\times$ nine-model sweep and a five-claw $\times$ two-model sweep, model choice changes Pass@1 by $29.4$ pp and harness choice by $27.4$ pp under fixed models; systems with similar accuracy can differ substantially in total API cost. Claw-SWE-Bench therefore treats harness and cost accounting as first-class axes of SWE-style coding-agent evaluation, providing both a full benchmark and a low-cost reference set for reproducible comparison. The data is available at this https URL and this https URL.

---


### 237. [Atlas H&E-TME: Scalable AI-Based Tissue Profiling at Expert Pathologist-Level Accuracy](https://arxiv.org/abs/2606.12346)

**<font color=#1a73e8>作者：</font>** Kai Standvoss, Miriam Hägele, Rosemarie Krupar 等 28 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hematoxylin and eosin (H&E) staining is the cornerstone of histopathology, yet scalable, quantitative analysis of H&E whole-slide images (WSIs) remains a central challenge in computational pathology. We present Atlas H&E-TME, an AI-based system built on the Atlas family of pathology foundation models that predicts tissue quality, tissue region, and cell type labels across multiple cancer types, yielding over 4,500 quantitative readouts per slide at cell-level resolution. A key challenge to validating such systems is overcoming morphological ambiguity inherent to H&E-only ground truth and the limited scalability of more informed references drawing on modalities such as immunohistochemistry (IHC). We address this with a dual validation framework combining biologically grounded depth with technical and morphological breadth. For depth, we propose an IHC-informed multi-pathologist consensus protocol that substantially improves inter-rater agreement over conventional H&E-only annotation. This yields a molecularly grounded reference against which we compare Atlas H&E-TME and pathologists working from H&E alone. For breadth, we benchmark Atlas H&E-TME on over 200,000 high-confidence H&E-only pathologist annotations across 1,500+ cases spanning eight cancer types and their most common metastatic sites, with subtypes covering >90% of clinical cases per cancer type, drawn from 25+ sources and 8+ scanner models. Benchmarked against the IHC-informed consensus, Atlas H&E-TME matches or exceeds pathologist H&E-only performance and generalizes consistently and robustly across this broad morphological and technical scope. In doing so, Atlas H&E-TME turns the H&E slide -- the most ubiquitous data in pathology -- into a scalable, quantitative window into the tumor and its microenvironment, laying a foundation for the next generation of tissue-based biomarkers in translational and clinical research.

---


### 238. [Nonslop: A Gamified Experiment in Human-AI Collaborative Writing](https://arxiv.org/abs/2606.12350)

**<font color=#1a73e8>作者：</font>** Maria Edwards, Julian Togelius  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of large language models (LLMs) raises critical questions about human creativity and individual expression in an era of AI-assisted creation. When do humans adopt AI suggestions, and what are the implications for individual voice?
This study examines these questions through a gamified writing exercise where 74 participants (214 responses) replied to prompts while AI-generated word suggestions were available as they wrote. The game simulates a dystopian future in which an AI is attempting to learn from what remains of human individuality, and disincentivizes AI-like writing. In doing so, it attempts to create conditions that reveal authentic user preferences rather than default behaviors, such as accepting a readily available AI-generated suggestion. Note that this is a deliberate inversion of the "helpful assistant" design pattern; the system is explicitly forbidding you from accepting AI suggestions.
We analyze user behavior patterns across different task types, user behaviors, and response characteristics to understand the factors influencing human-AI interaction in creative tasks. The study focuses on when users choose to maintain creative autonomy versus violating the rules of the game and accepting AI assistance. It also explores how these choices relate to response patterns, task characteristics, and user behavior. This gamified approach offers both a framework for studying authentic human-AI interaction and a provocative lens for understanding the tension between efficiency and authenticity in AI-augmented creativity.

---


### 239. [ECYSAP EYE: From Cyber Situational Awareness to Mission-Centric Decision Support for Enhanced Cyberspace Operations](https://arxiv.org/abs/2606.12354)

**<font color=#1a73e8>作者：</font>** Pantaleone Nespoli, Daniel Díaz-López, Sergio Lopez Bernal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Operational organizations increasingly require Cyber Situational Awareness (CySA) capabilities that go beyond isolated technical alerts, providing mission-relevant artefacts that can be embedded into heterogeneous toolchains and cyber security or cyber defense processes. ECYSAP EYE addresses this need through an adoption-oriented System-of-Systems (SoS) architecture centered on seven groups of mission-focused artefacts: the Recognized Cyberspace Picture (RCyP), Cyber Situational Reports (CySRs), the What-If Analysis Report (WIAR), Option Recommendations (OPRE), an operator Dashboard/HMI (DSH), Action Enforcement (AE), and After-Action Reports (AAR). The ECYSAP EYE architecture structures the transition from perception (full-spectrum RCyP views), to decision-oriented reasoning (WIAR/CySRs/OPRE), and to operational execution and learning (DSH/AE/AAR), with explicit integration surfaces that support incremental deployment and validation. This paper presents this innovative project from a technology transfer perspective, summarizing the updated architecture, the functional role of seven groups of artefacts, and the expected impact of cyber situations on the decision-making process in the context of a mission planning and execution.

---


### 240. [DepthMaster: Unified Monocular Depth Estimation for Perspective and Panoramic Images](https://arxiv.org/abs/2606.12368)

**<font color=#1a73e8>作者：</font>** Pengfei Wang, Shihao Wang, Liyi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While monocular depth estimation has achieved significant progress, achieving generalized metric depth estimation for both narrow field-of-view (FoV) perspectives and $360^\circ$ panoramas remains an unsolved challenge. Existing methods are often tailored to specific camera types and struggle to produce accurate metric depth that generalizes across diverse settings. This limitation stems from two key challenges: the inherent geometric discrepancy between perspective and panoramic cameras, and the scarcity of panoramic training data with metric annotations. In this work, we introduce DepthMaster, a unified metric depth estimation framework. Rather than employing specialized networks to learn spherical distortions, we reformulate the problem by decomposing panoramic images into overlapping perspective patches. Crucially, distinct from prior projection-based methods that rely on ad-hoc architectural modifications to handle boundaries, we introduce a novel Correspondence Consistency Loss (CCL) and inject virtual projection cameras as geometric priors, allowing us to seamlessly stitch the patches while avoiding specialized operators and keeping the backbone largely compatible with standard Transformer designs. This strategy also resolves the geometric differences by unifying all inputs into a canonical perspective representation, and effectively circumvents data scarcity by directly unlocking powerful metric priors from vast perspective datasets. Trained on a mixed dataset that contains only one panorama dataset, DepthMaster achieves state-of-the-art zero-shot performance on 13 diverse datasets, outperforming not only universal methods but also leading specialist models in both perspective and panoramic domains.

---


### 241. [A Turbo-Inference Strategy for Object Detection and Instance Segmentation](https://arxiv.org/abs/2606.12371)

**<font color=#1a73e8>作者：</font>** Zhen Zhao, Gang Zhang, Xiaolin Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection and instance segmentation tasks are closely related. Existing top-down instance segmentation methods usually follow a detect-then-segment paradigm, where an initial detector is used to recognize and localize objects with bounding boxes, followed by the segmentation of an instance mask within each bounding box. In such methods, the detection accuracy directly influences the subsequent segmentation performance. However, previous research has seldom explored the impact of the instance segmentation task on object detection. In this paper, we present a turbo-inference strategy for the top-down methods that leverages the complementary information between detection and segmentation tasks iteratively. Specifically we design two modules: turbo-detection head and turbo-segmentation head, which facilitate communication between the tasks. The two modules form a closed loop that interlaces the detection and segmentation results without retraining the model. Comprehensive experiments on the COCO, iFLYTEK, and Cityscapes datasets demonstrate that our method substantially enhances both detection and segmentation accuracies with a certain increase in computational cost. The proposed method represents a tradeoff between prediction accuracy and inference speed. Codes are available at this https URL.

---


### 242. [Illumination-Robust Camera-Based Heart-Rate Estimation for Physiological Sensing in Robots](https://arxiv.org/abs/2606.12378)

**<font color=#1a73e8>作者：</font>** Zhi Wei Xu, Torbjörn E. M. Nordling  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physiological awareness is important for service, social, and assistive robots that interact with humans in everyday environments. Remote photoplethysmography (rPPG) enables non-contact heart-rate (HR) estimation from an RGB camera, making it a promising sensing modality for robot-mounted vision systems. However, illumination variation remains a major barrier to robust deployment. This paper presents an end-to-end spatial-temporal transformer framework for remote HR estimation on a new dataset with varied illumination. Our estimator integrates PRNet-based 3D face alignment, clip-level illumination augmentation, the Residual Temporal Standardization Module, and controlled hybrid temporal-frequency supervision. The training objective combines a Soft-Shifted Pearson waveform loss with a spectral Kullback-Leibler divergence loss, where a tuned weight ($\mathbf{\beta}$) controls the contribution of frequency-domain heart-rate guidance. Experiments on a static all-level mix protocol covering three illumination levels show that $\mathbf{\beta}=5$ provides the strongest result among the tested beta settings, achieving a best-run HR mean absolute error (MAE) of 0.79 bpm and an HR correlation of 0.982. Compared with the PhysFormer baseline evaluated on our dataset, our estimator reduces HR MAE by 93.6 %, while increasing HR correlation from 0.088 to 0.982, making it usable when illumination varies.

---


### 243. [ATLAS: Active Theory Learning for Automated Science](https://arxiv.org/abs/2606.12386)

**<font color=#1a73e8>作者：</font>** Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science, we introduce ATLAS (Active Theory Learning for Automated Science), an active learning framework for the data-driven discovery of interpretable behavioral models. ATLAS iterates between generating mechanistic hypotheses--instantiated as a diverse ensemble of sparse neural networks (Disentangled RNNs)--and designing experiments that optimally distinguish between them. We test this approach on the problem of recovering reinforcement learning agents from their behavior in bandit tasks. ATLAS designs varied sequences of qualitatively novel experiments with temporal structure tailored to underlying agent characteristics. The models trained on these experiments are evaluated against a comprehensive set of metrics for mechanistic modeling that capture behavioral, structural, and computational similarity. ATLAS achieves a 5-10x improvement in sample efficiency across all metrics compared to random experimentation, and its performance is further validated against expert-designed experiments derived from literature. These in silico results showcase ATLAS's potential to accelerate human-interpretable insights in cognitive science and other domains where scientific inquiry relies on discovering mechanistic models.

---


### 244. [MARCIM-WG: A cyber wargame proposal based on math modeling applied in a naval scenario](https://arxiv.org/abs/2606.12395)

**<font color=#1a73e8>作者：</font>** Diego Cabuya-Padilla, Daniel Díaz-López, Carlos Castaneda-Marroquín  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As maritime operations increasingly depend on interconnected digital ecosystems, cyber incidents can propagate across maritime networks and degrade critical services. Strengthening strategic Cyber Situational Awareness (CSA) therefore requires training mechanisms that expose decision-makers to evolving attack dynamics, constrained resources, and the need to align actions with incident-response procedures. This paper introduces MARCIM-WG, a learning-oriented maritime cyberdefense wargame designed following the NATO wargaming methodology and implemented as a hybrid tabletop experience combining a physical board (tokens, indicators, and special cards) with analytically-assisted adjudication supported by a computational simulation model. The proposal is specified through High-Level Design (HLD) and Low-Level Design (LLD) specifications and instantiated in a fictional maritime cyber crisis scenario to enable structured decision cycles, friction, and measurable consequences. Validation combines (i) an operational scenario-based assessment under three configurations (pessimistic, neutral/most likely, optimistic) to verify decision sensitivity and outcome coherence, and (ii) a CSA competency and learning-outcome evaluation using a comparative design against an equivalent control group. Results show a +34.0 percentage-point improvement in the intervention group, with the largest gains in comprehension-related competencies.

---


### 245. [VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.12396)

**<font color=#1a73e8>作者：</font>** Jin Yao, Dhruva Dixith Kurra, Tom Lampo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models can describe scenes and reason about them in language, yet still struggle to ground their actions in the dense 3D world around them. Existing approaches either inject features from a frozen 3D foundation model without an objective that ensures the policy uses them, or constrain geometry with sparse box and map losses that provide no dense spatial signal. We introduce VLGA, the first vision-language-action model supervised to reconstruct the dense 3D world it drives through. VLGA introduces geometry as a fourth modality alongside vision, language, and action through a dedicated expert supervised by a per-pixel pointmap regression loss against LiDAR. Extensive experiments conducted on challenging nuScenes and Bench2Drive datasets for open-loop and closed-loop evaluations, respectively, show the superiority of VLGA over counterpart VLA methods. In particular, on open-loop nuScenes, VLGA sets a new state of the art among VLA methods without ego status, with the lowest L2 (0.50\,m average) and 3-second collision rate (0.18\%). On closed-loop Bench2Drive, VLGA attains the state-of-the-art driving score of 79.08, +0.71 over the strongest prior VLA, at comparable efficiency and comfort.

---


### 246. [Redesign Mixture-of-Experts Routers with Manifold Power Iteration](https://arxiv.org/abs/2606.12397)

**<font color=#1a73e8>作者：</font>** Songhao Wu, Ang Lv, Ruobing Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Router is the cornerstone component to the Mixture-of-Experts models. Serving as expert proxies, the rows of the router matrix compute their similarity to the MoE inputs to determine which subset of experts is activated. Ideally, each router row is designed to encode the expert matrix into this representative vector, such that its dot-product with token can better reflect token-expert affinity. However, there exists no design principles to enforce this condensation. In this paper, we propose to align each router row with the principal singular direction of the associated expert, as this direction provides the most expressive mathematical description of a matrix. Based on this principle, we propose a router redesign with Manifold Power Iteration (MPI). Specifically, it introduces a "Power-then-Retract" paradigm, where a power iteration step is performed on the router weights, followed by a retraction to impose a norm constraint to ensure both efficiency and stability. Theoretically, we show that MPI drives router rows to converge toward the principal singular directions of associated experts. Empirically, we pretrain MoE model across scales from 1B to 11B parameters to confirm that this alignment facilitates more effective MoE models.

---


### 247. [Doc-to-Atom: Learning to Compile and Compose Memory Atoms](https://arxiv.org/abs/2606.12400)

**<font color=#1a73e8>作者：</font>** Xingjian Diao, Wenbo Li, Yashas Malur Saidutta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long input sequences are central to document understanding and multi-step reasoning in Large Language Models, yet the quadratic cost of attention makes inference both memory-intensive and slow. Context distillation mitigates this by compressing contextual information into model parameters, and recent work such as Doc-to-LoRA amortizes context distillation into a single forward pass that generates one LoRA adapter per document. However, producing a single monolithic adapter for all queries leads to irrelevant-query interference, limited compositional recall, and poor scalability to long-document reasoning. To address these challenges, we propose Doc-to-Atom (Doc2Atom), a compositional parametric memory framework that decomposes each document into semantically typed knowledge atoms. Each atom is compiled into an independent micro-LoRA adapter and a provenance retrieval key. At inference time, a lightweight query router selects and assembles only the relevant atoms into a query-specific adapter, which is then injected into a frozen base model. The entire system is trained end-to-end through a multi-objective distillation framework. Experiments on six diverse QA benchmarks demonstrate that Doc2Atom outperforms Doc-to-LoRA baselines while reducing the memory cost of document internalization.

---


### 248. [Context-Driven Incremental Compression for Multi-Turn Dialogue Generation](https://arxiv.org/abs/2606.12411)

**<font color=#1a73e8>作者：</font>** Yeongseo Jung, Jaehyeok Kim, Eunseo Jung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern conversational agents condition on an ever-growing dialogue history at each turn, incurring redundant attention and encoding costs that grow with conversation length. Naive truncation or summarization degrades fidelity, while existing context compressors lack cross-turn memory sharing or revision, causing information loss and compounding errors in long dialogues. We revisit the context compression under conversational dynamics and empirically present its fragility. To improve both efficiency and robustness, we introduce Context-Driven Incremental Compression (C-DIC), which treats a conversation as interleaved contextual threads and stores revisable per-thread compression states in a single, compact dialogue memory. At each turn, a lightweight retrieve, revise, and write-back loop shares information across turns and updates stale memories, stabilizing long-horizon behavior. In addition, we adapt truncated backpropagation-through-time (TBPTT) to our multi-turn setting, learning cross-turn dependencies without full-history backpropagation. Extensive experiments on long-form dialogue benchmarks demonstrate superior performance and efficiency of C-DIC; notably, C-DIC shows stable inference latency and perplexity over hundreds of dialogue turns, supporting a scalable path to high-quality dialogue modeling.

---


> [!TIP]
> 当前位于：**201-248**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-248**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
