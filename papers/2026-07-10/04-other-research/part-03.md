# 📦 其他研究 | 2026年07月10日

> 本类共 **207** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-207](./part-05.md)

---

### 101. [Is Randomness Necessary for Adaptive Data Analysis?](https://arxiv.org/abs/2607.07085)

**<font color=#1a73e8>作者：</font>** Edith Cohen, Haim Kaplan, Yishay Mansour 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Adaptive Data Analysis (ADA) problem formalizes the challenge of preventing false discovery and overfitting when a dataset is repeatedly reused. Formally, our input is a dataset containing $n$ i.i.d. samples from an unknown distribution $\mathcal{P}$ over a domain $\mathcal{X}$, and our goal is to answer a sequence of $k$ adaptively chosen statistical queries with respect to $\mathcal{P}$. The main question is how many queries we can support (i.e., how large $k$ can be), primarily as a function of the number of samples $n$. This question has been intensively studied and is relatively well-understood for randomized mechanisms: there are computationally efficient mechanisms that support $k \approx n^2$ queries, and no computationally efficient mechanism can answer $k \gg n^2$ queries. In this paper, we address a fundamental question: is randomness necessary for ADA?
Despite a decade of work on ADA, this question remains open. A folklore observation dating back to the initial works on ADA is that randomness is not necessary when the analyst is computationally bounded. Yet, the necessity of randomness against computationally unbounded analysts has remained elusive. Our main contribution resolves this gap in the information-theoretic Random Oracle model. Perhaps surprisingly, we show that randomness is strictly necessary to answer a non-trivial number of adaptive queries: when the analyst is unbounded, any deterministic mechanism can be forced to fail after just $k = \tilde{O} (n)$ queries.

---


### 102. [Structural Adversarial Attacks on Relational Deep Learning under Integrity Constraints](https://arxiv.org/abs/2607.07089)

**<font color=#1a73e8>作者：</font>** Alan Gany, Bogdan Cautis, Silviu Maniu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational Deep Learning (RDL) has become a standard methodology for machine learning on relational databases: the database is encoded as a heterogeneous temporal graph in which tuples become nodes and primary-key to foreign-key (PK-FK) dependencies become typed edges, over which a graph neural network is trained for downstream prediction. We study the adversarial robustness of this pipeline. We consider a white-box attacker who knows how the graph is built and the model is trained, reasons about perturbations on the graph, but can only act on the upstream database, by rewiring foreign-key references while preserving the integrity constraints of the schema (foreign-key validity, the degree-one FK constraint, and functional dependencies). This restricts the attacker to a constrained, combinatorial set of admissible edits under a global perturbation budget, which is intractable to explore exhaustively and made non-additive by GNN message passing. We investigate seven attack heuristics - two random sampling baselines and five gradient-guided variants that exploit differentiable edge masks - and evaluate them on the RelBench rel-f1 benchmark. Gradient-based attacks consistently outperform random baselines on regression tasks, whereas gains on classification are smaller, which we attribute to low label-flip rates and greater local stability of classification outputs.

---


### 103. [Video-Based Detection of squint and cataract for accessibility-aware adaptive web interface rendering](https://arxiv.org/abs/2607.07099)

**<font color=#1a73e8>作者：</font>** Amar Ranjan Dash, Manas Ranjan Patra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Squint and cataract are major ocular disorders that majorly affect visual perception and interaction capability. This paper proposes a real-time video-based automated detection system for squint and cataract detection based on computer vision and image processing methods. The proposed system uses a media-pipe face-mesh (a 478-point facial landmark detection model) to extract geometric ocular features for multi-class squint classification. Simultaneously, The presence and severity cataract is estimated through grayscale intensity and histogram-based lens opacity analysis. The system records short video sequences with standard laptop or mobile cameras, which can be deployed at low costs and on a large scale. The experimental performance has shown great accuracy in the detection of squint (98.39%) and classification of cataract (96.90%). Besides automatic ocular analysis, the proposed framework is also made accessible for visual impairment inference which will be integrated with future adaptive user interface and Web accessibility systems for people with visual impairment.

---


### 104. [CompoVista: A Composition-Graph-Based Visual Analytics System for Compositional Analysis of Traditional Chinese Paintings](https://arxiv.org/abs/2607.07105)

**<font color=#1a73e8>作者：</font>** Dekun Qian, Ruiqi Yu, Fengling Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Composition in Traditional Chinese Paintings (TCPs) carries spatial, narrative, and cultural-aesthetic meaning. Systematic compositional analysis is therefore important for understanding their visual language and artistic meaning. Traditional compositional analysis is mainly qualitative and interpretation-driven. It supports close reading of individual paintings, but it is difficult to discover, compare, and verify compositional patterns across large painting collections. To better understand these challenges, we conducted a literature review and in-depth interviews with two art historians. Based on these findings, we introduce the Composition Graph, a scene-graph-based representation for TCP composition. It models a painting through four layers: entities, relations, void space, and context. Based on this representation, we develop CompoVista, a canvas-based visual analytics system for composition-oriented exploration of TCPs. CompoVista allows art historians to construct and revise format-aware painting cohorts through visual queries and context queries. It also supports cohort-level inspection of entity distributions and relations, comparison of compositional differences across cohorts, and tracing aggregate patterns back to painting-level this http URL evaluated CompoVista through a task-based user study with 12 domain participants, two case studies, and expert interviews. The results show that CompoVista supports composition-oriented cohort construction, pattern discovery, iterative refinement, and evidence inspection. The evaluation also reveals future needs, including clearer result explanations, fuzzier composition queries, and stronger exploration history management. Our work contributes a composition-specific structured representation and an integrated visual analytics workflow for studying TCP composition at collection scale.

---


### 105. [Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act](https://arxiv.org/abs/2607.07109)

**<font color=#1a73e8>作者：</font>** Víctor Mayoral-Vilches  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The EU Cyber Resilience Act (CRA) makes a smart bet. It does not demand that products be free of vulnerabilities, but only that manufacturers run a process: assess risk, handle flaws, ship updates. The bet pays off if four things about the world stay true: (P1) finding vulnerabilities is slow, skilled, human work; (P2) a product's exploitable flaws are knowable the day it ships; (P3) exploitation is rare enough to notice; and (P4) fixes keep pace with discovery. Cybersecurity AI (CAI) agents, AI put to work finding and exploiting flaws in other products, falsify all four. The regime answers in two opposite ways. Against the sheer volume of flaws that agents surface it bends (P1): built for scarce attention, it re-centres compliance on defensible, documented prioritisation, and holds. But agents also collapse the speed and economics of the vulnerability lifecycle, and here it breaks (P2, P3, P4): a product that passed every check becomes exploitable without anyone touching it, so its market-entry test, its reporting trigger, and its one-and-done certificate vouch for a security that has quietly expired. The fault is in the landscape, not the product, so running the process more diligently cannot repair it. We map each mechanism to the force that strains or snaps it, and find the cure and the disease cut from the same cloth: because defenders and attackers wield the same AI, the only conformity that survives is one that never stops running. We also carry the remedy from proposal to proof on two CRA-scope robots, a humanoid and a lawn mower, where an agentic defender holds a line their undefended selves cannot. On the evidence already in hand, the CRA reaches full force in December 2027 certifying products against a world that has already changed. Static, human-paced security is finished; what replaces it must be continuous and agent-operated, and that is no longer a matter of taste.

---


### 106. [Bringing robustness to end-user programming](https://arxiv.org/abs/2607.07116)

**<font color=#1a73e8>作者：</font>** Mickaël Baron, Patrick Girard  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In some cases, end-user programming allows the design of stand-alone applications. But none of the existing approaches is concerned by safety aspects of programming. Heavy techniques exist to develop safe applications, particularly in non-interactive domains. They involve software engineering techniques, and sometimes, formal methods. All these techniques are very far from end-users. Our idea is to let this part to experts, and to connect end-user programming onto this safe conventional development. Starting from an existing functional core, we built an interactive end-user programming environment called GenBuild, which allows designing interactive stand-alone applications. GenBuild is composed of two distinct modules. The Generator is the first one. It is a specialized tool developed for a domain expert who sets out a safe functional core. The Builder is the second module. It is a purely interactive tool that allows an end-user to develop some complete interactive application among an existing functional core. It allows the verification of some properties that are a first step towards the development of safe end-user programming.

---


### 107. [ColorFM: An Optimization-to-Learning Framework for Color Transfer via Flow Matching](https://arxiv.org/abs/2607.07119)

**<font color=#1a73e8>作者：</font>** Yuhang He, Kai Zhang, Xiaoming Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color transfer aims to align the color distribution of a source image with that of a reference image while preserving structural and semantic consistency. However, existing methods often suffer from inaccurate global mapping, semantic misalignment, and visual artifacts. To address these issues, we propose ColorFM, an optimization-to-learning framework. ColorFM connects online optimization to offline inference by reformulating color transfer as the transport of pixel distributions along velocity fields via Flow Matching. Specifically, we introduce ColorFM-O, an instance-specific optimization scheme that fits the velocity field through hierarchical color coupling guided by semantic priors. By numerically integrating the induced flow trajectories, ColorFM-O produces precise and semantically consistent color transfer results, while generating high-quality paired data as pseudo-supervision. Building upon this, we design ColorFM-L, an efficient feed-forward model trained on the generated pairs. Through implicit state modeling, ColorFM-L extracts deep semantic features to predict flow parameters for bidirectional linearized transport, ensuring accurate color transfer. Extensive experiments demonstrate that ColorFM-L outperforms state-of-the-art methods in visual quality, structural fidelity, and semantic consistency, successfully combining the accuracy of optimization with the speed of feed-forward inference.

---


### 108. [Widest-Path Reachability Fields for Connectivity-Preserving Slender Structure Segmentation](https://arxiv.org/abs/2607.07123)

**<font color=#1a73e8>作者：</font>** Youcheng Zong, Runda Jia, Minxuan Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmenting slender curvilinear structures such as retinal vessels, cracks, and roads demands topological correctness, as even a single-pixel discontinuity can fragment a continuous network and invalidate downstream analysis. Under standard binary-mask supervision, models optimized for pixel-level overlap frequently produce topologically broken predictions. We trace this to a fundamental mismatch: pixel-wise losses distribute gradients uniformly, yet connectivity hinges on a sparse set of bottleneck pixels. These pixels are vastly outnumbered by thick structures and background, rendering their aggregate gradient contribution negligible. We term this phenomenon topological gradient starvation (TGS). To address it, we propose Widest-Path Reachability Fields (WPRF), a differentiable Max-Min reachability objective that redirects gradient flow to connectivity bottlenecks. The module is plug-and-play, backbone-agnostic, and incurs no inference overhead. WPRF implements a differentiable Max-Min objective via dynamic programming on a domain-restricted graph, coupled with a bottleneck-aware observation term that balances gradient contributions across varying structures. Compared to prior topology-aware losses that rely on post-hoc skeletonization or homology computation, WPRF directly optimizes end-to-end reachability via differentiable Max-Min algebra, enabling gradient flow to concentrate on connectivity bottlenecks without auxiliary structures. We introduce OMVIS, a new oral microvessel segmentation dataset. Experiments across nine architectures and six datasets validate the bottleneck-focused gradient routing mechanism. WPRF improves 87\% of experiments with fixed hyperparameters and achieves clDice gains of 7.2 percentage points on structurally fragile datasets.

---


### 109. [Sparse Attention for Dense Open-Vocabulary Prediction in CLIP](https://arxiv.org/abs/2607.07135)

**<font color=#1a73e8>作者：</font>** Fatimah Zohra, Chen Zhao, Shuming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastive Language-Image Pre-training (CLIP) relies on softmax-based self-attention, a strictly positive distribution that assigns probability mass to every pair of tokens-even semantically irrelevant ones. While these dense softmax weights are effective for gathering broad context during pre-training, they spread attention across many low-salience tokens, producing noise that obscures the fine-grained, spatially localized cues required for dense, open-vocabulary prediction. We study an inference-time substitution of the row-wise softmax in the final visual self-attention layers with the $\alpha$-entmax transform, applied across both the standard query-key attention and self-correlation variants. Because entmax applies a data-dependent threshold that maps low scores exactly to zero, it acts as an implicit denoiser, zeroing contextually irrelevant dependencies while redistributing mass onto the most relevant tokens. We evaluate on open-vocabulary tasks-dense semantic segmentation (Pascal VOC, Pascal Context, ADE20K) and fine-grained retrieval (FG-OVD)-and find the gain from attention sparsification is proportional to how much the baseline attention spreads off the target class.

---


### 110. [From Text to Parameters: Predicting Item Parameters from Embedding Regularization with Reliability and Design Ceilings](https://arxiv.org/abs/2607.07141)

**<font color=#1a73e8>作者：</font>** Shi-Ting Chen, Jinsong Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Newly developed items must ordinarily be field tested before their psychometric properties are known, creating a cold start problem for item calibration. Predicting item parameters from features is a long standing measurement problem dating back to the Linear Logistic Test Model; modern text embeddings now automate the design matrices traditionally specified by hand. We propose an evaluation framework combining regularized regression on item text embeddings, repeated cross validated R squared reported with its resampling standard deviation, and two performance upper bounds: a reliability ceiling derived from parameter standard errors, and a design ceiling derived from simulation based power calibration. Applying this framework to a mathematics item bank (EEDI) and a medical licensure benchmark (BEA 2024), we find that item difficulty is highly predictable from text (repeated cross validated R squared = 0.53, or about 57% of its reliability ceiling), whereas discrimination and pseudo guessing appear less predictable. However, evaluating these results against our ceilings reveals that this apparent hierarchy stems from target reliability rather than text signal strength: text uniformly recovers 57 to 63% of the reliable variance across difficulty targets, whereas the 3PL pseudo guessing parameter has a reliability ceiling near zero, making it an unviable target at current precision. On BEA, embedding based regression matches leaderboard RMSE despite explaining almost no variance, highlighting the critical need for scale free metrics and explicit ceilings in benchmarking. Finally, we show that a single train and test split can inflate apparent accuracy by 0.1 to 0.15 in R squared, underscoring the necessity of repeated cross validation for calibration support applications and future benchmark construction.

---


### 111. [Prior-matched evaluation of operational Earth-observation classifiers: a three-number reporting method demonstrated on Sentinel-1 internal-wave detection](https://arxiv.org/abs/2607.07146)

**<font color=#1a73e8>作者：</font>** Joao Pinelo, Joao Goncalves, Arun Shukla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Internal Waves Service screens the Sentinel-1 Wave-mode archive for internal solitary waves, routing detections to experts whose adjudication time is the resource the effort exists to conserve. Because attention is the cost of error, precision leads. Its classifier was trained and reported at a one-to-one class balance, fixed before the operational rate could be known. That rate has since emerged at roughly one scene in twenty, and a balanced-test score badly overstates the precision a validator meets. A model that scores 0.794 balanced-test precision scores 0.192 in real operation: the gap is a systematic artefact of reporting at the wrong prior, invisible to the metric most work quotes. We show the mismatch to be an evaluation problem in the costume of a training one at a fixed recall, prior correction and calibration cannot move precision, and answer it with a prior-matched reporting method based on three figures: balanced-test, operational-prior, and real post-deployment, whose contrast is the honest measure. A precision-first, leakage-controlled development cycle then improves the classifier lever by lever, each promoted only against a pre-registered margin; added capacity not clearing it, calibration inert, feature aggregation the one real lift, so the honest negatives are as much a result as the gain. Holding recall at a floor of 0.80 and certifying against a sealed, single-read lockbox, the promoted model reports 0.927 precision at the operational prior; an out-of-time check confirms discrimination transfers to unseen periods while a fixed operating point does not. Prior-matched reporting, begin balanced, then move to the prior as the stream reveals it, transfers to any operational Earth-observation service bootstrapping a rare-event detector under a prior it has yet to discover.

---


### 112. [Information Allocation Dynamics in Neural Network Optimization](https://arxiv.org/abs/2607.07156)

**<font color=#1a73e8>作者：</font>** Zhang Gongyue, Liu Donghan, Ren Weihong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Different optimizers have different update biases, but these biases are usually implicit. Existing studies mainly analyze or control such biases from the geometry of the final solution. However, how optimizer bias forms during training still lacks a clear internal mechanism.
This paper proposes an information allocation dynamics perspective. It interprets optimizer implicit bias as the relative allocation of training signals between weight-like and bias-like parameter pathways. This allocation can be described and adjusted by a continuous preconditioning exponent \(p\).
To characterize this mechanism, we first analyze the update contributions of weight and bias to the same residual signal in a minimal linear model. The weight correction term preserves input-dependent residual signals, while the bias correction term preserves the residual mean direction. They therefore correspond to different projection pathways of the residual signal. After substituting the preconditioned update into the residual update equation, the optimizer can change the relative strength of the weight correction term and the bias correction term through different preconditioning factors. Therefore, optimizer implicit bias is not only reflected in the final solution or the global training trajectory. It is also reflected in the relative write-in ratio of training signals across different parameter pathways.
Overall, this paper moves the analysis of optimizer implicit bias from solution-space geometry to update dynamics during training. It reveals that the relative update allocation between weight and bias-like parameters is an important dynamical mechanism that affects parameter trajectories and generalization behavior.

---


### 113. [NoDrift3R: Raymap-Guided Coupling for Drift-Robust Unposed Feed-Forward 3D Reconstruction](https://arxiv.org/abs/2607.07168)

**<font color=#1a73e8>作者：</font>** Xiangyu Sun, Liu Liu, Seungkwon Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-Free Feed-forward 3D Gaussian Splatting (3DGS) has recently emerged as a powerful paradigm for fast scene reconstruction. However, its performance degrades significantly in long image sequences due to cumulative camera pose estimation drift, which propagates errors into geometric modeling and severely limits rendering fidelity. In this work, we revisit the long-sequence bottleneck and identify pose drift as the primary factor restricting reconstruction quality. Furthermore, while SfM-based pseudo ground-truth poses introduce sensor noise, purely rendering-based supervision often leads to optimization instability and local minima due to the entangled optimization of geometry and pose. To address the challenges, we propose a synergistic pose-free framework that explicitly couples geometry and appearance via a Raymap-Guided Coupling Module (RGC). Concretely, we anchor Gaussian centers to raymap-induced geometry and jointly optimize RGB reconstruction, raymap consistency, and camera regularization under a unified objective, yielding a bidirectional feedback loop: stronger geometry improves rendering, and appearance supervision in turn refines geometry and pose. To further stabilize learning across wide temporal ranges, we introduce a Dual-Frequency Viewpoint Scheduling strategy that combines easy-to-hard interval expansion with replay of short-interval pairs. Extensive experiments across in-domain and cross-domain datasets show consistent gains in both rendering and pose estimation, with notably improved robustness on long sequences. Ablation studies validate our central insight: explicitly designed geometry-appearance synergy is the key to scalable and drift-robust pose-free feed-forward 3D reconstruction.

---


### 114. [TACoS: Weakly Supervised Learning of Two-Dimensional Materials from Scribble Annotations to Precise Segmentation](https://arxiv.org/abs/2607.07169)

**<font color=#1a73e8>作者：</font>** Jiabei Chen, Liping Zhang, Jiang-Bin Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The precise pixel-level localization of 2D material flakes is crucial for high-throughput screening. However, traditional fully supervised methods rely on dense annotations, which are costly and time-consuming, severely limiting the practical deployment of segmentation models. This paper proposes TACoS, a specialized scribble segmentation framework tailored for 2D materials. First, we design a unified framework that integrates semi-supervised consistency learning with structured tree energy constraints. This framework comprises two core components: an unlabeled weak-strong distribution alignment module and a tree energy regularization module. The former employs cosine consistency constraints to enhance prediction alignment across views. Meanwhile, the latter utilizes minimum spanning trees to establish pixel affinity relationships and generate structure-aware soft pseudo labels for online semantic guidance. Next, we introduce asymmetric regional contrast learning. This approach fuses high-confidence predictions from the weak augmentation branch with scribbles to form augmented labels, and construct category prototypes in the representation space. Simultaneously, we prioritize contrastive constraints on challenging pixels in boundary-unlabeled regions. This strategy enhances intra-class cohesion and inter-class separation at the representation level, effectively reducing category confusion in low-contrast edges and complex backgrounds. Experiments conducted on the constructed graphene and MoS2 datasets demonstrate that our method TACoS achieves over 96% of fully supervised performance using less than 0.6% annotated data. Furthermore, it exhibits superior structural coherence and boundary stability in scenarios with weakly contrasting edges and complex backgrounds, providing an efficient and scalable solution for automated high-throughput screening of 2D material flakes.

---


### 115. [PUF: Plug-and-Play Uncertainty-Aware Fusion for Online 3D Scene Graph Generation](https://arxiv.org/abs/2607.07170)

**<font color=#1a73e8>作者：</font>** Yi Yang, Myrna Castillo, Bodo Rosenhahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online 3D scene graph generation builds a persistent, structured representation of a scene by incrementally fusing 2D observations into a global 3D graph. Existing online methods treat this fusion as a fully deterministic pipeline, where we identify three sources of uncertainty that are overlooked: observation, 2D model, and 3D representation. We propose PUF: a Plug-and-play, Uncertainty-aware, and training-free Fusion framework. Scene graph node association is reformulated as a probabilistic likelihood over semantic and spatial factors, replacing binary accept/reject gates. Dirichlet evidence accumulation distributes class and relationship evidence across plausible candidates proportional to association likelihood. An optional class-conditional prior completes edges for sparsely or never co-observed object pairs. We instantiate PUF with both a 3D Gaussian and a 3D voxel backend and observe consistent improvements, demonstrating its ability to generalize across different representations. Experiments on the 3DSSG and ReplicaSSG benchmarks show that our method substantially outperforms existing approaches while maintaining real-time latency. These results establish uncertainty-aware fusion as a principled and effective paradigm for online 3D scene understanding. The source code is publicly available at this https URL.

---


### 116. [Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation](https://arxiv.org/abs/2607.07173)

**<font color=#1a73e8>作者：</font>** Wenyan Xu, Alizer Wong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. However, a uniform low-rank constraint or a uniform adapter strength cannot explicitly distinguish the capacity requirements of different denoising stages. Moreover, inference-time candidate selection driven mainly by identity similarity may compress the selected samples in the visual representation space. We decompose the problem into two complementary components: SPaRa denotes training-side stage-aware low-rank adaptation, DCAL denotes inference-side distribution-calibrated candidate selection, and SPaRa-DCAL denotes the combined framework. Theoretical analysis shows that timestep-dependent scaling controls the effective perturbation magnitude of a low-rank adapter, while identity-biased candidate selection restricts the radius of selected features around the reference center under explicit conditions. Auditable experiments under the SDXL and DreamBooth 30-subject protocol show that DCAL improves 1-LPIPS, CLIP-I, DINO-I, and CLIP-T on a fixed LoRA candidate pool, while revealing a clear trade-off with CLIP/DINO pairwise diversity and pairwise LPIPS. These results indicate that personalized generation should be evaluated through identity consistency, text alignment, and representation diversity rather than identity metrics alone.

---


### 117. [Comparative Study of Domain-adapted VLMs for General Document Visual Question Answering](https://arxiv.org/abs/2607.07179)

**<font color=#1a73e8>作者：</font>** Miguel Lopez-Duran, Elena Marrero, Julian Fierrez 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Document Visual Question Answering (DocVQA) presents a complex multimodal challenge, requiring models to exploit visual, textual, and layout information from documents. Although Vision-Language Models (VLMs) have shown remarkable performance in text-vision tasks, their robustness and transferability to different document domains remains underexplored. In this study, we present a comprehensive evaluation of 8 open-source pretrained VLMs on DocVQA in three different document domains: industrial documents of varying type, infographics, and presentation slides. We systematically assess model performance under zero-shot evaluations, fully supervised finetuning with inter- and intra-dataset evaluations, and few-shot learning evaluations of knowledge transfer between domains. Our findings demonstrate that while large pretrained VLMs possess strong zero-shot baselines for structured layouts, their performance strongly decreases on visually complex layouts of infographics and slides. Although parameter scaling is a dominant factor on performance, supervised finetuning yields higher relative gains in smaller architectures. Furthermore, our cross-domain and few-shot experiments show that visual understanding is the main bottleneck for DocVQA, not a lack of knowledge from the VLMs. Using 50 target domain samples, the models finetuned in DocVQA with datasets of different domains rapidly adapt to the target domain documents, even surpassing their fully supervised counterparts in some cases.

---


### 118. [Clinical Translation of Brain-Computer Interface in China: A Landscape Analysis of Investigator-Initiated Trials, Registered Clinical Trials, and Regulatory Approval](https://arxiv.org/abs/2607.07185)

**<font color=#1a73e8>作者：</font>** Long Chen, Wanyi Qing, Lifen Mo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Neurological injury affects hundreds of millions of people worldwide, yet the loss of motor or communication functions resulting from stroke, spinal cord injury, and neurodegenerative disease remains largely irreversible with existing therapies. Brain-computer interfaces (BCIs) offer a promising pathway for restoring these functions by decoding neural activity into commands that control an external device. Here, we present the first quantitative analysis of China's BCI translational ecosystem, integrating evidence from three pillars: investigator-initiated trials (IITs), registered clinical trials, and regulatory-approved products. We analyzed 134 clinical trials from the Chinese Clinical Trial Registry (ChiCTR), 26 IITs, and five BCI-related products approved by the National Medical Products Administration as of June 2026. Results demonstrate that clinical trial registration has increased rapidly since 2020, with research centers concentrated primarily in Guangdong, Shanghai, and Jiangsu. Non-invasive systems predominated, accounting for 79.1% of registered studies, with stroke rehabilitation as the leading indication (65.0%). As of June 2026, five BCI-related products received regulatory approvals, including the world's first approved semi-invasive implantable BCI, an invasive closed-loop deep brain stimulation system with real-time local field potential recording, and three non-invasive EEG-based rehabilitation systems. Collectively, these findings characterize a rapidly expanding BCI translational pipeline in China, spanning from early clinical research to regulatory approval. However, long-term implant stability, standardization of clinical infrastructure and workflows, and generalizability of decoding algorithms remain critical barriers to widespread clinical adoption. Addressing these challenges will be essential for integrating BCI technologies into routine clinical practice.

---


### 119. [EditVerse3D: High-Quality 3D Object Editing with Region-Aware Learning](https://arxiv.org/abs/2607.07187)

**<font color=#1a73e8>作者：</font>** Youtan Yin, Yanning Zhou, Jiacheng Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Local editing of 3D objects remains a long-standing challenge. When interacting with 3D content, humans naturally tend to specify a coarse region of interest for modification rather than defining precise editing boundaries. However, previous methods rely on fully edited 2D images, precise 3D masks, or redundant pipelines, which present a gap. To bridge this gap, we propose EditVerse3D, a novel 3D editing framework that enables high-quality object editing under such coarse guidance. Our approach takes as input a 3D object to be edited, a coarse 3D bounding box indicating the target region, and a reference 2D image describing the desired modification. It produces a coherent, high-fidelity edited 3D object. To facilitate this editing, we introduce a novel region-aware adaptive loss that emphasizes hard-to-learn regions and balances the objective between target and preserved areas. Complementing our loss function, we enhance model robustness and generalization through targeted data augmentations, such as training with scaled 3D masks and filtering out unrealistic editing pairs. We construct a large-scale 3D editing dataset derived from parts information. Extensive experiments demonstrate that EditVerse3D achieves superior visual quality and quantitative performance compared to existing 3D editing approaches. Please visit our project page at this https URL.

---


### 120. [Evaluating Endpoint Detection Robustness Against Genetic Algorithm Driven Code Transformations](https://arxiv.org/abs/2607.07191)

**<font color=#1a73e8>作者：</font>** Alvina Rwaichi Minja, Jema David Ndibwile  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Post-compromise test variants are widely used in controlled security evaluation and endpoint robustness benchmarking. However, modern Antivirus (AV) and Endpoint Detection and Response (EDR) systems increasingly combine signature- and behavior-based detection, challenging the reliability of conventional detection pipelines under adaptive variation. This study introduces ShellForge, a Genetic Algorithm (GA)-driven framework that evolves post-compromise variants representative of remote command execution to generate functionally equivalent variants for systematic detection evaluation. ShellForge applies syntactic transformations, encoding schemes, and structural permutations guided by a multi-objective fitness function informed by AV and EDR detection feedback. We compare ShellForge against representative baseline transformation frameworks under identical sandbox configurations. Our findings highlight measurable robustness gaps in baseline signature- and behavior-oriented detection pipelines under controlled variant generation. In addition, we propose a reproducible benchmark for endpoint detection robustness evaluation, motivating the need for robustness-aware defensive monitoring and behavioral correlation.

---


### 121. [Prototype-Anchored Generalized Manifold Regression for Unknown-Domain Object Detection](https://arxiv.org/abs/2607.07192)

**<font color=#1a73e8>作者：</font>** Zihao Zhang, Aming Wu, Yang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we study Single-Domain Generalized Object Detection (Single-DGOD), which aims to transfer a detector trained on a single source domain to multiple unseen domains. Existing methods mainly rely on simulation-driven strategies, such as data augmentation or textual prompts, to enlarge the training distribution. However, finite simulations can hardly cover the dynamic variations of real-world scenarios, often causing overfitting to synthetic styles and limited robustness to complex structural degradations. Inspired by the manifold hypothesis, we argue that semantic features, despite diverse visual changes, should lie on a compact and stable low-dimensional manifold. Therefore, robust generalization requires rectifying deviant samples back to this semantic manifold, rather than exhaustively simulating external perturbations. To this end, we propose Manifold Regression with Visual-Text Dual Chain-of-Thought (MR-DCoT), which formulates unknown-domain generalization as a manifold regression problem. MR-DCoT first uses a Visual-Text Dual Chain-of-Thought module to combine VLM-guided semantic evolution with diffusion-based structural perturbation, generating structured off-manifold hard examples. It then introduces Class-Specific Prototype Anchoring to learn a rectification operator that projects deviant features toward the source semantic manifold. By integrating outlier generation and semantic correction into a closed loop, MR-DCoT effectively narrows the distribution gap and improves robustness under unseen shifts. Extensive experiments on three complementary benchmarks, including adverse-weather detection, real-to-art generalization, and zero-shot semantic segmentation, demonstrate the effectiveness and versatility of our method.

---


### 122. [DiffCVE: Diffusion-based Compressed Video Enhancement](https://arxiv.org/abs/2607.07195)

**<font color=#1a73e8>作者：</font>** Wenqiang Xiao, Wenzhuo Ma, Junxi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perceptual quality enhancement of severely compressed videos remains challenging due to complex artifact patterns and substantial information loss. Recent diffusion models have demonstrated strong generative capability for visual restoration, but directly applying them to compressed video often ignores compression degradation characteristics and may introduce structure-inconsistent hallucinations. To address this issue, this paper presents a diffusion-based compressed video enhancement method, named DiffCVE. Coding Prior-enhanced Dual Conditioning (CPDC) branches are designed to jointly model compressed video and coding prior conditions, where coding priors including residuals and motion vectors provide complementary structural and motion guidance during the diffusion denoising process. To make the diffusion process aware of compression severity, a Compression Degradation Semantic Prompting (CDSP) mechanism is introduced to leverage QP-conditioned textual prompts together with LoRA fine-tuning. In addition, a Coding Prior-guided Weighted Fusion (CPWF) module is incorporated into the VAE decoder to fuse VAE encoder and coding prior encoder features with QP-predicted weights. Extensive experiments demonstrate the effectiveness of the proposed method in improving perceptual quality, especially under severe compression settings. The project page with enhanced video demonstrations is available at this https URL.

---


### 123. [Geometric--Nongeometric Optimizer Calculus: A Modular Language for Reachable Gradient Methods](https://arxiv.org/abs/2607.07206)

**<font color=#1a73e8>作者：</font>** Zavier Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers mix several mechanisms: a metric or preconditioner maps gradients to descent directions, while estimation, memory, step-size control, constraints, stochasticity, target modification, and discretization determine which directions are available and how they are used. We introduce geometric--nongeometric optimizer calculus, a modular language for auditing reachable gradient methods under explicit oracle, budget, state, and rule constraints. The geometric module is a positive cometric family that maps covectors to parameter-space directions; the nongeometric modules are information, memory, control, operator, noise, target, and discretization mechanisms. The main formal result is a direction-expressivity theorem: away from critical points, full positive-definite geometry expresses exactly the strict descent directions. We then define restricted direction residuals for admissible metric families, prove exact expressivity conditions for diagonal and block geometries, and separate this direction-level diagnostic from condition-number geometric complexity. The resulting design problem is a Pareto optimization over module budgets, not a single universal optimizer ordering. We also lift pointwise residuals to a trajectory-level residual complexity that couples direction mismatch with the variation of the explaining geometry. We include diagnostic prototypes only as evidence for the language: a high-information full-metric probe solves deterministic quadratic benchmarks to numerical precision, while a practical Muon-style PyTorch candidate gives small-scale evidence that matrix-operator updates can be audited by the calculus. The paper is a theory and benchmark-language manuscript; it does not claim large-scale optimizer state-of-the-art performance.

---


### 124. [Continual Learning With Participation Privacy: An Auditable Buffering-Aggregation Recipe](https://arxiv.org/abs/2607.07209)

**<font color=#1a73e8>作者：</font>** T-H. Hubert Chan, Elaine Shi, Mengshi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern federated and streaming learning systems often release intermediate models, so privacy must hold for the full trajectory under adaptive interaction. Motivated by participation privacy, we study single-edit neighboring user streams, where one insertion/deletion shifts all subsequent updates and defeats standard Hamming-neighbor continual-release analyses. We give an auditable modular recipe. A randomized buffering wrapper emits bins of size $[U,2U]$, reducing single-edit streams to a Hamming-style per-bin update stream with explicit backlog/delay guarantees, where $U$ is calibrated by the privacy parameters $(\varepsilon,\delta)$. We then prove a certification theorem identifying when a non-adaptive Hamming-neighbor DP proof for a continual primitive lifts to adaptive inputs: the primitive must use fresh per-round randomness and have a stable one-round privacy profile under common adaptive context. Together, these ingredients yield trajectory-level $(\varepsilon,\delta)$-DP for single-edit streams using standard primitives (e.g., tree prefix sums), with an explicit privacy--latency link via $U$.

---


### 125. [Why Fake ? Unveiling the Semantic Vocabulary of Deepfake Detectors](https://arxiv.org/abs/2607.07216)

**<font color=#1a73e8>作者：</font>** Vazgken Vanian, Alexandros Doumanoglou, Dimitris Zarpalas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake (DF) technology poses a significant threat to information integrity, driving the need for robust detection methods. Most DF detectors only consider predicting a binary label for whether the input is real or fake, lacking the justification required for real-world applications like legal proceedings. Explainable DF Detection has emerged to address this limitation, but existing techniques frequently fall short by either relying on human annotations for precise artifact localization or generating superficially plausible textual explanations without grounding. This work investigates the use of post-hoc explainable AI (XAI) to analyze the decision-making process of state-of-the-art black-box DF detectors. Specifically, we employ Encoding-Decoding Direction Pairs (EDDP), a technique suitable for uncovering the concept space of DF detectors (their semantic vocabulary) as well as the mechanism for writing and reading concept information to and from internal representations. Our analysis reveals previously hidden real and fake features learned implicitly during detector training, offering nuanced explanations unattainable through conventional methods. This enables global model understanding, spatially aware concept localization, and counterfactual what-if analysis, all contributing to a deeper comprehension of DF detection strategies.

---


### 126. [Monitoring Vulnerabilities in Next-Generation Automotive Operating Systems](https://arxiv.org/abs/2607.07226)

**<font color=#1a73e8>作者：</font>** Dimitri Simon, Badis Hammi, Joaquin Garcia-Alfaro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software-defined vehicles (SDVs) are revolutionizing transportation by integrating complex, interconnected hardware, and software systems. This evolution introduces significant security challenges. We present a comprehensive security analysis for SDVs, focusing on software vulnerabilities. We note that existing vulnerability assessment tools fall short in addressing operating systems vulnerabilities, particularly when it comes to efficiently analyzing diverse software stacks in realistic environments. We present and release a vulnerability assessment solution that efficiently addresses these limitations. Our approach combines systematic vulnerability discovery, leveraging public Common Vulnerabilities and Exposures (CVE) databases, within a dockerized development environment that evaluates exploitability risks. The results reveal both breadth of potential threats and the practical constraints we faced during exploitation. We discuss the implications for industry and research, and propose directions for building more resilient SDVs.

---


### 127. [Reasoning Consistency Scanning: A Framework for Auditing Chain-of-Thought Validity in AI Safety Evaluations](https://arxiv.org/abs/2607.07229)

**<font color=#1a73e8>作者：</font>** Silvia Santano  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prior work has shown that chain-of-thought (CoT) reasoning is often unfaithful: a model's stated reasoning does not reliably reflect the process that produced its output. Detecting unfaithfulness, though, requires controlled experimental interventions, which cannot be applied to evaluation transcripts after the fact. We turn instead to a more tractable question that has received less attention: whether the stated reasoning is logically consistent with the answer it accompanies. Unlike faithfulness, consistency can be assessed from a transcript alone, with no intervention. We introduce reasoning consistency scanning, a reusable method for detecting this property in AI safety evaluation transcripts. Our contributions are fourfold. First, we formalize reasoning consistency as distinct from faithfulness and define a six-subtype taxonomy of inconsistency. Second, we build a validated benchmark of 60 transcripts, manually adapted from InstrumentalEval outputs. Third, we implement a working scanner for InspectScout, the first to target this property in safety evaluation transcripts. Fourth, we report results across four generator models and three evaluations from inspect_evals, showing that reasoning inconsistency is present, detectable, and varies systematically across both models and task types.

---


### 128. [`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation](https://arxiv.org/abs/2607.07230)

**<font color=#1a73e8>作者：</font>** Waqas Arshid, Mohammad Awrangjeb, Alan Wee-Chung Liew 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video object segmentation (VOS) is a fundamental task in video understanding, requiring accurate delineation and consistent tracking of objects across frames. While supervised methods achieve strong performance, they rely on densely annotated datasets that are costly to obtain and have limited domain coverage. Self-supervised learning offers a promising alternative by removing the need for manual labels; however, existing approaches often struggle to jointly maintain spatial accuracy and temporal coherence, particularly in unconstrained multi-object scenarios. Many rely on optical flow, synthetic motion cues, or task-specific pretraining, limiting scalability and generalisation. We propose a self-supervised framework, Cross-Temporal Consistency and Clustering, that learns mid-level, part-aware representations by combining attention-guided token selection with lightweight temporal clustering. Instead of operating at the pixel or whole-object level, the method aligns soft part assignments across time using a saliency-weighted symmetric consistency objective. The framework leverages a frozen transformer backbone with lightweight modules for adaptive token selection and multi-offset temporal alignment, enabling efficient scaling across resolutions and motion patterns.

---


### 129. [HPG-Diff: Hierarchical physics-guided diffusion with differentiable connectivity constraints for topology optimization](https://arxiv.org/abs/2607.07233)

**<font color=#1a73e8>作者：</font>** Jinbo Yang, Mingyue Yuan, Boyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep generative models offer a promising paradigm for topology optimization, enabling rapid design exploration. However, these approaches lack intrinsic physics guidance, often leading to poor generalizability across unseen boundary conditions and the formation of floating material artifacts. To address these limitations, we propose Hierarchical Physics-Guided Diffusion (HPG-Diff), a novel diffusion framework that enforces physics consistency through two synergistic mechanisms. First, we introduce a hierarchical physics-guided strategy that aligns different precomputed physics features with the denoising process, guiding material distribution toward optimal load paths to enhance generalizability. Second, we propose a floating material suppression loss as a differentiable connectivity constraint inspired by thermal conduction to improve topological connectivity. By simulating a virtual heat propagation process from load positions, this mechanism explicitly penalizes floating material during training. Quantitative evaluations demonstrate that HPG-Diff achieves average compliance errors of 0.87% (in-distribution) and 5.29% (out-of-distribution), while reducing floating material ratios to 2.90% and 2.44%, respectively. Furthermore, case studies on a 3:1 rectangular domain, including cantilever and bridge benchmarks, provide preliminary evidence that lightweight LoRA fine-tuning with a small dataset can support the adaptation of HPG-Diff to rectangular non-square domains.

---


### 130. [ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies](https://arxiv.org/abs/2607.07235)

**<font color=#1a73e8>作者：</font>** Ignacio D. Lopez-Miguel, Ezio Bartocci, Thomas Eiter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainability remains a key issue in reinforcement learning (RL). Distilling an interpretable policy from an agent trained in a complex environment is particularly challenging when the action space is continuous. We introduce ORCAID, a novel method for extracting interpretable rule-based policies from RL agents operating in mixed continuous-discrete environments with continuous action spaces. Our main contribution is an efficient oblique decision tree training algorithm that partitions the state space by hyperplanes and fits local linear models. The key idea lies in a three-stage split search: efficient random initialization, local refinement, and backward elimination. Finally, adjacent leaves are merged to yield a concise set of interpretable rules describing a given deep RL policy. We evaluate ORCAID across multiple RL environments, demonstrating that the extracted rule-based policies maintain strong performance with a low number of parameters and can even be used to improve the performance of the original deep RL policy.

---


### 131. [Unraveling Machine Behavior by Multi-Level Bias Analysis and Detection: Methodology and Application to Computer Vision](https://arxiv.org/abs/2607.07236)

**<font color=#1a73e8>作者：</font>** Ignacio Serna, Aythami Morales, Julian Fierrez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study investigates the presence and propagation of bias within Neural Networks through a comprehensive multi-level analysis spanning the learned latent space, layer activations, and the network's parameters. Based on this taxonomy, we propose three bias detection approaches: 1) SpaceBias (new method), which characterizes the latent space prior to the final classification layer using neighbor-probability distributions and quantifies bias with the two-sample Kolmogorov-Smirnov test on the per-group distributions. 2) ActivationBias (extension of the existing method InsideBias), which analyzes the activations of neural network filters and quantifies bias via a Mann-Whitney U test, based on the observed fact that underrepresented groups exhibit lower activation levels in the final convolutional layers. 3) WeightBias (extension of the existing method IFBiD), which uses a secondary neural network trained to identify biased patterns directly in the parameters of task-specific models. Unlike conventional methods, which assess neural network outcomes and treat the model as a black box, our proposed techniques provide insight into how biases manifest within the network architecture itself at different levels, offering a more nuanced and detailed understanding. Experiments are conducted on two complementary applications: gender classification in the DiveFace dataset (72,000 face images) and digit classification on a colored-MNIST benchmark with controlled bias severity. In total, more than 127,000 models with varying degrees and types of bias were trained and evaluated. The severity sweep shows that the internal disparity, and with it the detection performance, decreases smoothly as the training distribution approaches balance. The results highlight the importance of methods that provide deeper insight into the behavior of AI models.

---


### 132. [An Edge-aware Prompt-enhanced SAM for Ultrasound Image Segmentation](https://arxiv.org/abs/2607.07240)

**<font color=#1a73e8>作者：</font>** Wenhao Li, Fangyi Liu, Bo Du  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound image segmentation is essential for delineating anatomical structures and lesions, providing the foundation for accurate diagnosis. While the Segment Anything Model (SAM) has demonstrated remarkable success on natural images, its performance on ultrasound data is often hindered by poor boundary delineation. To address this limitation, we propose EP-SAM, an edge-aware and prompt-enhanced adaptation of SAM. Specifically, we leverage multi-block feature extraction from the image encoder to enrich coarse-to-fine semantic representations, while edge-aware supervision of the image encoder improves robustness to contour ambiguity and speckle noise. By integrating these complementary cues, EP-SAM generates high-quality prompts that effectively guide the model toward target regions of interest. Experimental results on multiple benchmarks demonstrate that EP-SAM consistently outperforms existing SAM-based methods.

---


### 133. [Safe Reinforcement Learning using Ideas from Model Predictive Control](https://arxiv.org/abs/2607.07252)

**<font color=#1a73e8>作者：</font>** Georg Schäfer, Jakob Rehrl, Stefan Huber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world physical systems, violating mechanical limits can cause irreversible damage, necessitating that exploration remains strictly within safe operational regions. We propose a generalized framework that combines the adaptive, high-performance nature of deep reinforcement learning (DRL) with the formal safety guarantees of model predictive control (MPC). Using a mathematical model of the system dynamics, offline MPC computations define a feasible state-action space, representing all safe combinations of system states and control inputs that guarantee constraint satisfaction. During training and deployment, the RL agent's instantaneous actions are projected onto this globally verified feasible set via a safety filter. We systematically evaluate our generalized approach on a non-linear 1-DoF laboratory testbed, demonstrating successful exploration and stable policy convergence on physical hardware.

---


### 134. [FMMVCC: Fuzzy Mamba-based Multi-View Contrastive Clustering for Univariate Time Series](https://arxiv.org/abs/2607.07258)

**<font color=#1a73e8>作者：</font>** Donato Cerciello, Leonardo Schiavo, Angel Panizo-LLedot 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many realistic scenarios, large volumes of time series data are generated with limited or expensive annotations. This limitation makes supervised learning methods difficult to apply and leads to the use of unsupervised approaches capable of discovering meaningful structures directly from raw data. Clustering therefore plays a crucial role in organizing time series into groups that share similar temporal patterns, enabling exploratory analysis and downstream tasks without requiring manual labeling. However, existing deep clustering methods often struggle to capture long-range temporal dependencies or rely on architectures with high computational cost. This paper introduces FMMVCC, a Mamba-based deep clustering framework for time series that leverages state space sequence modeling to efficiently learn temporal representations with linear complexity. Additionally, it utilizes multi-view self-supervised learning with temporal masking and augmentations. Experimental evaluation in 15 benchmark datasets proves that FMMVCC consistently outperforms state-of-the-art baselines, achieving the best overall performance in 29 of 60 total metric evaluations and the highest average rank in all tested scenarios.

---


### 135. [Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for Faithful Explanation](https://arxiv.org/abs/2607.07264)

**<font color=#1a73e8>作者：</font>** Ahsan Habib Akash, Dipkamal Bhusal, Stacey Jones 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are widely deployed in high-stakes visual applications where interpretability is critical, yet existing explanations face a trade-off: post-hoc concept methods recover factors that are faithful to a model's behavior but unnamed, while naming and by-design methods attach human-readable concepts only by retraining or altering the classifier. We propose Language-Anchored Decomposition (LAD), a post-hoc framework that delivers concepts which are simultaneously named, faithful, and obtained without modifying the model. For each class, a large language model proposes a concept vocabulary that CLIP-based similarity maps localize across image regions. Inverting standard non-negative matrix factorization, LAD fixes these language-grounded maps as the coefficient matrix and learns only a concept basis that reconstructs the frozen encoder's activations, so naming becomes a structural constraint and the model's own feature geometry determines which concepts are retained. Removing this anchor preserves accuracy but collapses attribution faithfulness. Across natural-image, scene, and medical-imaging benchmarks, LAD produces spatially precise explanations that are decision-relevant under both concept insertion and deletion, while uniquely providing stable, human-interpretable concept names.

---


### 136. [MoLIFE: Methodology, Technologies, and Challenges for Mobile Live Intelligent Forensics Examination](https://arxiv.org/abs/2607.07269)

**<font color=#1a73e8>作者：</font>** Silvia Lucia Sanna, Cristina Alcaraz, Alessandro Sanna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nowadays, mobile forensics is less explored in Digital Forensics case analysis due to the increase in data protection mechanisms implemented by tech companies (i.e., Google for Android and Apple for iOS). For example, the physical acquisition or analysis of specific directories under super-user protection would corrupt the evidence; access to such data is protected, and bypassing this protection requires either privilege escalation or custom ROM installation, leading to the modification of the device state. At the same time, the demand for mobile technologies and their respective communication systems is increasing exponentially, exposing numerous security threats and risks. For that reason, this paper presents a Mobile Live Intelligent Forensics Examination (MoLIFE), a novel Digital Forensics (DF) methodology for data acquisition and analysis of mobile devices. The proposed methodology is based on NIST SP800-101 for the DF process. MoLIFE can be integrated with new and emerging technologies by exploiting their power (e.g., AI, blockchain, quantum computing). MoLIFE can also be used to prevent cyber threats and incidents, as well as DF post-mortem analysis, offering examples of applying the MoLIFE methodology and good practices for the future. To prove the technical feasibility of the methodology, a small case study on Android devices data acquisition via the mDT will be presented. As the methodology is based on new and emerging technologies, it depends on their limitations that would be overcome in a few years.

---


### 137. [Safe2Hail: A Forensic-Driven Post-Trip Tracking Framework for Ride-Hailing Safety in Africa](https://arxiv.org/abs/2607.07271)

**<font color=#1a73e8>作者：</font>** Alvina Minja, Robert Maina, Mahmud Oloyede 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Ride-hailing mobile apps have become an essential feature in the mobility ecosystem in Africa, offering much safer and much more affordable rides. Although user bases have increased and the number of daily trips has proliferated, reports of imminent safety threats, particularly after the cancellation of the ride or the ride is prematurely terminated, remain unresolved challenges. Current safety measures offer features such as SOS alerts, safety notifications, and live location sharing for the duration of the trip, but they are not in place when the trip is over. Safe2Hail presents a framework that is forensically driven to ensure continuous safety and certainty beyond the trip. The Safe2Hail framework combines forensic tracking with a temporary post-trip synchronization mechanism that can securely log all proximal data between a passenger and a driver after an event. The Safe2Hail framework was beta-tested and demonstrates the effectiveness of the system. Although the research team did not pilot on actual deployment, the Safe2Hail design format was in part inspired by actual crime events reported in Nairobi and Dar-es-Salaam. The findings of the study referenced Safe2Hail's feasibility, light weight nature of resources, as well as the scalability for the framework.

---


### 138. [BubbleSH: A Dataset of Rising Bubbles with Deformable Interfaces](https://arxiv.org/abs/2607.07275)

**<font color=#1a73e8>作者：</font>** Rachna Ramesh, Kiet Bennema ten Brinke, Douwe Orij 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bubbly flows exhibit complex multiscale dynamics, with deformable bubbles interacting through the surrounding liquid and giving rise to strongly coupled kinematic and morphological behavior. We present BubbleSH, a bubbly flows dataset consisting of transient, three-dimensional bubble-swarm dynamics obtained from high-fidelity direct numerical simulations of bubbles rising in a periodic domain. The dataset provides time-resolved bubble trajectories, velocities, and shape evolution, with bubble morphology compactly represented using spherical harmonics. Designed to be lightweight yet physically expressive, the dataset enables data-driven modeling of bubbly flow simulators where shape deformation and bubble-bubble interactions play a central role. We characterize the dataset with bubble kinematics, morphology, and interaction patterns, and introduce evaluation metrics for both trajectory and shape prediction. The sensitivity of bubble-swarm dynamics to local perturbations makes BubbleSH particularly well suited to generative models that learn distributions over possible future trajectories. We evaluate a permutationally and translationally equivariant probabilistic emulator on BubbleSH given the proposed metrics. Therefore, we establish a compact, high-fidelity dataset and a benchmark for developing and evaluating data-driven models of deformable, chaotic multiphase systems.

---


### 139. [Understanding Interpretation Difficulty in Harmful Online Communication: Insights from Cybercrime Communities](https://arxiv.org/abs/2607.07277)

**<font color=#1a73e8>作者：</font>** Tomohiro Okatsu, Naoki Takada, Yin Min Pa Pa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harmful online communication often contains slang, coded terms, abbreviations, and community-specific expressions, which make messages difficult to interpret. This paper presents an exploratory study of interpretation difficulty in Discord chats related to cybercrime. We construct reference interpretations of purposefully selected difficult messages, which were reviewed by an expert. We then use them to evaluate human and large language model (LLM) interpretations under different context conditions. The results show that local context alone is often insufficient for humans, while external knowledge and extended conversational context substantially improve human interpretation. For LLMs, local context also improves interpretation, and the larger model performs better. We further conduct a qualitative error analysis and propose a preliminary classification of factors that make harmful chats difficult to interpret. These findings suggest that harmful-content analysis should treat interpretation as an evidence-integration problem, rather than as message-level classification alone.

---


### 140. [A Word-Level Digital Reader of the Prasthanatrayi with Sankara's Bhasya: Corpus, Method, and an Open, Offline Reading Aid for the Advaita Vedanta Canon](https://arxiv.org/abs/2607.07282)

**<font color=#1a73e8>作者：</font>** Tamal Maharaj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Prasthanatrayi -- the ten principal Upanisads, the Brahmasutra, and the Bhagavadgita, with Sankara's commentaries (bhasya) -- is the foundational corpus of Advaita Vedanta. Continuous euphonic combination (sandhi), long compounds (samasa), and dense scholastic prose make it hard to read at the word level: where one word ends, and what each word means grammatically, are both obscured. We present an open, fully offline, word-level digital reader of the entire Prasthanatrayi with Sankara's bhasya. Every word -- of both the root text (mula) and the commentary -- is clickable and resolves to a pop-up giving its split (padaccheda), morphological analysis, and gloss. Because every word carries a lemma, the reader also acts as a concordance: a search on a dictionary headword retrieves all of that word's inflected and sandhi-hidden occurrences, and its occurrences inside compounds, across both layers. The resource covers thirteen commentarial units (2,971 verses, sutras, and prose sections; 36,881 analysed word-occurrences of root text) and a global dictionary of 95,587 distinct commentarial surface forms. We describe the corpus, the hybrid pipeline -- a rule-based sandhi splitter over an inflected-form lexicon and attested-corpus look-ups, with LLM-assisted analysis under an adversarial two-pass verification protocol -- and a durable human-review loop whose corrections survive every regeneration. An intrinsic evaluation against independent Sanskrit resources finds high-confidence analyses agree with an authoritative inflectional lexicon on over 99% of attested forms, and a band-blind adjudication confirms that quality degrades predictably across confidence bands, with errors concentrated in the low-confidence tier the review loop targets. The reader is a single self-contained HTML file needing no server or network, offered as a freely redistributable teaching and reading aid.

---


### 141. [CarbonCLIP: Enhance Carbon Prediction from Satellite Imagery via Integrated Street-View Semantics and Temporal Context Training](https://arxiv.org/abs/2607.07292)

**<font color=#1a73e8>作者：</font>** Zeru Yang, Fang-Ying Gong, Steve H.L. Yim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately estimating urban carbon emissions is critical for sustainable urban planning, yet many existing approaches remain difficult to apply consistently across cities due to data-source heterogeneity and the lack of fine-grained semantic-temporal context in remote sensing data. We propose CarbonCLIP, a task-oriented multimodal distillation framework that improves satellite-based carbon emission prediction by transferring contextual knowledge into a unified satellite representation through dual-branch contrastive learning. Unlike conventional methods that rely on static visual features, CarbonCLIP explicitly bridges the gap between top-down satellite views and ground-level human activities. Specifically, the spatial branch uses fine-grained textual descriptions automatically generated from street-view images by Large Multimodal Models (LMMs) to provide semantic priors reflecting building functions, infrastructure, and urban activities, while the temporal branch employs a month encoder to encode temporal priors associated with monthly emission variation. CarbonCLIP requires multimodal data only during the pretraining phase; during inference, it relies solely on satellite imagery, thereby supporting scalable deployment when ground-level data are unavailable at inference. Experiments on Beijing and Singapore demonstrate that CarbonCLIP outperforms baselines in both study cities. The results validate that our method effectively transfers multimodal knowledge into satellite representations, offering a robust solution for satellite-based urban carbon modeling.

---


### 142. [Nonlinear Bandit](https://arxiv.org/abs/2607.07304)

**<font color=#1a73e8>作者：</font>** Tianshuo Zheng, Ting Wu, Zhi-Hua Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we first study the problem of generalized linear bandit (GLB) under heavy-tailed noise. The characteristics of heavy-tailed distributions are widely observed in real-world applications such as personalized recommendation, financial markets, and medical treatments. Based on the online mirror descent (OMD) method, we propose an algorithm EHM that extends the adaptive Huber loss method (Wang et al., 2025) with one-pass update ($\mathcal{O}(1)$ computational complexity with respect to current round $t$ and the time horizon $T$), which simultaneously achieves an almost optimal regret of $\widetilde{\mathcal{O}}(T^{\frac{1}{1+\epsilon}})$ where $T$ is the time horizon. In addition, by utilizing a special property of some link function (Sawarni et al., 2025), our algorithm eliminates the need to know a commonly used parameter. Next, we study the GLB problem under the case when contextual characteristic becomes piecewise constant, and we slightly revised former algorithm to obtain the PGLB-EHM algorithm. After theoretical analysis, we prove that the regret upper bound order stays the same. Furthermore, we look deeper into a special case of nonlinear bandit (NB) and present the NB-EHM algorithm with bisection method and special restriction. Eventually we utilize the affine lifting approach and show that the general NB problem can be applied with NB-EHM to achieve a sublinear regret bound.

---


### 143. [FedCVESA: Taking Away Training Data in Federated Learning via Correlation Value Encoding and Segmented Aggregation](https://arxiv.org/abs/2607.07314)

**<font color=#1a73e8>作者：</font>** Chongkai Li, Bang Zhang, Wenjian Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) avoids explicit data exposure by keeping raw data on local clients, yet privacy risks remain in the training process and the learned model itself. Recently, centralized Taking Away Training Data (TATD) attacks have shown that malicious training could abuse the memorization capacity of deep models to store and later recover training data. However, this memorization-based threat has not been systematically studied under FL environments, where multi-client averaging could overwrite encoded training data. In this paper, we study a white-box TATD attack in which a malicious server selects n target clients from K participating clients and actively writes private training data into the global model during federated training. We propose FedCVESA, a federated variant of Correlation Value Encoding Attack (CVEA), by adding a Pearson-correlation regularizer to the loss function of target clients, so that private training data are gradually encoded into selected model parameters, referred to as carrier parameters. To reduce the overwriting of carrier parameters during server aggregation, we further propose segmented aggregation over dispersed carrier parameters, preserving selected carrier parameters while keeping standard averaging on the remaining parameters. Experiments on MNIST, Fashion-MNIST, and CIFAR-10 under Dirichlet non-IID partitions show that the proposed method can steal semantically meaningful private training images from the trained model while maintaining acceptable main-task utility in a controlled proof-of-concept setting. These results demonstrate that FL can become a parameter-level memorization channel for active TATD attack under the studied white-box malicious-server setting.

---


### 144. [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](https://arxiv.org/abs/2607.07316)

**<font color=#1a73e8>作者：</font>** Pranav Sawant, Jakub Krejčí  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly addresses the opaque "black box" nature of machine learning models, which is essential for ensuring safety and auditability in high-stakes deployments. The paper provides a detailed examination of Transformer circuit analysis, exploring how internal components like the residual stream, attention mechanisms, and induction heads drive complex tasks and in-context learning. It subsequently tackles the core challenge of superposition and polysemanticity, demonstrating how tools like Sparse Autoencoders (SAEs) and transcoders can decompose tangled network activations into distinct, human-interpretable features. Furthermore, the paper explores methods for actively controlling and modifying model behavior through steering vectors and causal interventions. Finally, it connects these mechanistic insights with neurosymbolic AI frameworks designed to translate neural representations into explicit, executable logical rules.

---


### 145. [R^3: Advertisement Compliance Rectification via Group-Relative Experience Extractor and Curriculum Reinforcement](https://arxiv.org/abs/2607.07318)

**<font color=#1a73e8>作者：</font>** Yuan Chen, Zhenyu Hu, Mengge Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rigorous content moderation is crucial for online advertising but leads to millions of daily rejections. This scale renders manual rectification infeasible, particularly for video advertisements. However, existing safety-driven methods often suffer from aggressive over-editing, which compromises the advertiser's original semantic intent merely to satisfy compliance. In this work, we target the rectification of textual violations in video ads, covering both speech transcripts and on-screen text. We propose R^3, a novel framework designed to harmonize compliance with original semantic intent preservation. Our approach integrates three key innovations: (1) an experience-driven data synthesis framework that bootstraps high-quality supervision via a group-Relative compliance experience extractor; (2) a curriculum Reinforcement learning strategy with hierarchical rewards designed to enforce compliance while maximizing semantic consistency; and (3) a comprehensive video Rectification framework seamlessly integrating text recognition, rewriting, and re-rendering for industrial deployment. Extensive experiments on industrial datasets and online A/B testing demonstrate that R^3 significantly outperforms state-of-the-art baselines, achieving an optimal trade-off between violation rectification and intent preservation.

---


### 146. [SoccerNet 2026 Challenges Results](https://arxiv.org/abs/2607.07320)

**<font color=#1a73e8>作者：</font>** Anthony Cioppa, Silvio Giancola, Håkan Ardö 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The SoccerNet 2026 Challenges constitute the sixth annual edition of the SoccerNet open benchmarking effort, dedicated to advancing computer vision research in sports video understanding. This year's challenges span five vision-based tasks: (1) Ball Action Anticipation, predicting the timing and class of ball-related actions within a short future window from a preceding observation window; (2) Player-Centric Ball Action Spotting, temporally localizing and classifying ball-related actions while assigning each action to the acting player through team affiliation and jersey number; (3) Novel View Synthesis, rendering images from unobserved camera poses in multi-view football scenes; (4) Spiideo SoccerNet Synloc, localizing athletes in real-world pitch coordinates from a single calibrated static-camera image; and (5) Visual Question Answering, answering multiple-choice questions about football broadcasts across text, image, and video inputs. For each task, participants were provided with annotated data, a unified evaluation protocol, and a public baseline. This edition saw broad participation, with 427 teams submitting 1,129 entries across the five tasks and 28 teams contributing reviewed technical reports. This paper describes each task and its evaluation protocol, presents the challenge leaderboards, and summarizes the leading submissions, with the aim of documenting the current state of each task as measured on held-out challenge data.

---


### 147. [HAJJv2-CrowdCount: Zero-Shot Benchmark for Dense Crowd Counting](https://arxiv.org/abs/2607.07322)

**<font color=#1a73e8>作者：</font>** Reem AlYabis, Fares AlTuwaim, AlJawharh AlOtaibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated crowd counting in Hajj video is difficult not because current models lack capacity, but because the footage violates the assumptions those models were built on: cameras observe the crowd from steep, near-vertical angles, individuals occlude one another extensively, and a single frame can contain well over a thousand people. Benchmarks that test crowd counting in such an environment are either private or not detailed per second. We revisit the HAJJv2 dataset and contribute HAJJv2-CrowdCount: per-second human-annotated crowd counts for its testing videos. Using these annotations, we benchmark three recent zero-shot counting paradigms: an open-vocabulary detector (YOLO-World), a point-based counter (APGCC), and a promptable segmentation-based counter (SAM3Count). SAM3Count attains the lowest overall mean absolute error (MAE 70.4, 95% CI 56.0-86.1), ahead of YOLO-World (92.0) and APGCC (152.9). This ordering reverses, however, in the regime most relevant to deployment: on the densest frames, the detection- and segmentation-based counters both degrade sharply (MAE exceeding 300), while the point-based counter degrades far more gracefully (MAE 114.9). This inversion is decision-relevant for Hajj crowd management, where reliable counts are needed most precisely in the densest and most occluded scenes. The annotations are released to support reproduction and extension of these results.

---


### 148. [Hypergraph Neural Stochastic Diffusion: An SDE Framework for Uncertainty Estimation](https://arxiv.org/abs/2607.07330)

**<font color=#1a73e8>作者：</font>** Zhiheng Zhou, Mengyao Zhou, Dengyi Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraph neural networks have shown powerful capability in modeling higher-order relations, yet their predictive uncertainty remains underexplored. Unlike pairwise graphs, uncertainty in hypergraphs arises not only from noisy attributes and ambiguous labels, but also from variations in node-hyperedge incidence structures and complex higher-order dependencies. Existing approaches mainly estimate uncertainty from final predictions or rely on computationally expensive ensembles and Bayesian inference, limiting their ability to capture uncertainty evolution during representation learning. In this paper, we propose Hypergraph Neural Stochastic Diffusion(HyperNSD), a stochastic differential equation framework for uncertainty estimation on hypergraphs. HyperNSD models hypergraph representations as stochastic processes evolving over node-hyperedge incidence structures. A learnable drift function captures deterministic higher-order diffusion dynamics, while a learnable stochastic forcing function characterizes structural ambiguity and representation noise. Predictive uncertainty is directly quantified through the variability of stochastic representation trajectories, providing an intrinsic uncertainty measure beyond post-hoc confidence scores. We formulate HyperNSD with neural drift and diffusion networks, enabling joint learning of prediction and uncertainty propagation. Theoretical analyses establish well posedness, perturbation stability,permutation equivariance, and numerical convergence of the proposed stochastic dynamics. Experiments on multiple hypergraph benchmarks demonstrate that HyperNSD achieves reliable uncertainty estimation for out-of-distribution and misclassification detection while preserving competitive prediction accuracy. These results provide a principled stochastic-dynamical framework for trustworthy higher-order representation learning.

---


### 149. [Latency-Aware Bid Acceptance under Operational Feasibility: A Public Benchmark with Hindsight Ceilings](https://arxiv.org/abs/2607.07343)

**<font color=#1a73e8>作者：</font>** Aswin Chandrasekaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online truckload bid acceptance is a closed-loop stochastic decision problem in which a carrier or broker must, in real time, accept or reject a tendered load subject to operational feasibility, fleet repositioning costs, and opportunity cost against future demand. Public, reproducible benchmarks for this problem are scarce: existing routing benchmarks are static, while dynamic-fleet studies typically rely on private operator data. We introduce FreightBidBench, a public-calibrated, dependency-free, closed-loop benchmark in which feasibility (pickup reach, appointment windows, simplified hours-of-service, stochastic yard delays) and economics (service-failure penalty, terminal fleet value, daily price-premium window) are explicit, versioned, and reproducible from public Freight Analysis Framework and U.S. Department of Agriculture truck rate data. We develop two full-horizon hindsight ceilings: a simple LP style relaxation and a tighter Lagrangian-per-truck information relaxation that retains per-truck hours-of-service and sequencing structure and is 20.7% tighter than the LP relaxation on a tight-capacity scenario and 39.3% tighter on a scarce-capacity scenario. We introduce a parametric surrogate-rollout cascade with boundary-band and scarcity-pressure escalation triggers. On ten-seed tight and scarce scenarios, the best simple policy retains 91.0% and 86.5% of rollout profit and the standard-library surrogate 94.2% and 89.3%; a cascade at a single escalation band recovers roughly 98% on both at 40-56% of rollout's mean decision latency, and on the tight scenario is statistically indistinguishable from the rollout teacher (paired-bootstrap 95% CI on the profit delta spans zero).

---


### 150. [The AI Resilience Gap: Bringing Artificial Intelligence Inside the Operational Resilience Perimeter](https://arxiv.org/abs/2607.07359)

**<font color=#1a73e8>作者：</font>** Jonathan Shelby  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of artificial intelligence across regulated firms has produced an extensive governance response oriented around trustworthiness: the EU AI Act, ISO IEC 42001, the NIST AI Risk Management Framework, and the United Kingdom's principles-based approach all address safety, fairness, transparency, and model risk. That response is necessary but incomplete. It does not, on its own, address operational resilience: the continuity of important business services under severe but plausible disruption, the substitutability of AI components, and the concentration of dependency on the small number of firms that supply frontier models. This paper argues that AI adoption creates a resilience obligation that is distinct from, and inadequately covered by, the trustworthy AI stack, and that United Kingdom financial authorities are already closing this gap through the Financial Policy Committee's systemic analysis, the Critical Third Parties regime, and the May 2026 joint statement on frontier AI and cyber resilience. We map the two regulatory logics, identify the structural gap between them, and propose the AI Resilience Framework: a regime-agnostic method for bringing AI dependencies inside the operational resilience perimeter through dependency mapping, a criticality-substitutability tiering, the extension of impact tolerances to AI-specific failure modes, an explicit fallback doctrine, and provider level concentration management. The framework gives chief information security officers, security architects, and boards an actionable route from AI governance policy to demonstrable resilience. This work extends a companion analysis of the United Kingdom cyber resilience regulatory stack into the artificial intelligence dimension.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-207](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
