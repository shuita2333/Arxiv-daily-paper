# 📦 其他研究 | 2026年06月09日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

---

### 101. [StainFlow: Entity-Stain Tracking and Evidence Linking for Process Rewards in GUI Agents](https://arxiv.org/abs/2606.07027)

**<font color=#1a73e8>作者：</font>** Haojie Hao, Longkun Hao, Yihang Lou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has become a promising approach for improving GUI Agents in long-horizon, stochastic digital environments, but trajectory-level success feedback is too sparse to provide reliable credit assignment for intermediate exploration steps. To mitigate this issue, recent studies introduce Process Reward Models (PRMs), which provide finer-grained training feedback through global milestone verification or local step-level evaluation. However, these methods still suffer from two level-specific limitations: global milestone decomposition is subjective and singular, making it difficult to accommodate the multiple valid execution paths in real GUI tasks, while fixed local judging windows may miss long-range key evidence or dilute the decision signal with irrelevant frames. Inspired by stain-tracing mechanisms in network flow analysis, we propose StainFlow, an entity-stain-flow process reward model for GUI Agents. To reduce the subjectivity of global partitioning, we introduce the Global Entity Stain Tracking module, which extracts visually verifiable task entities and tracks how their stain concentrations and states evolve along the trajectory, allowing task phases to be objectively separated by changes in the entity evidence flow. To improve the accuracy of local verification, we introduce the Local Stain Evidence Linking module. Centered on the triggering entities of each candidate key node, it retrieves relevant steps based on their stain concentrations and state changes, and dynamically constructs high-density evidence windows for verifying true key nodes. Extensive experiments on AndroidWorld and OGRBench show that StainFlow relatively improves online RL success by 3.2% and trajectory completion judgment accuracy by 1.8%.

---


### 102. [CF-JEPA: Mask-free forward prediction with asymmetric encoder utilization for time-series representation learning](https://arxiv.org/abs/2606.07031)

**<font color=#1a73e8>作者：</font>** Jaehoon Lee, Sunghyun Sim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning (SSL) for time-series representation learning is dominated by two paradigms: contrastive methods, which face challenges in constructing positive or negative pairs, and masking-based methods, which disrupt the temporal continuity of time-series signals. Joint-Embedding Predictive Architecture (JEPA) offers a promising alternative by predicting in representation space rather than reconstructing raw inputs. However, existing time-series JEPA variants still rely on masking and therefore inherit its continuity problem. Crop-based Forward JEPA (CF-JEPA) is proposed as an innovative mask-free framework that replaces masking with multi-horizon forward prediction: random crops serve as context views, and short-, mid-, and long-horizon future representations are predicted in the forward temporal direction, directly leveraging the inherent temporal ordering of time-series data as a learning signal. A strong asymmetry is also identified between the online encoder and the exponential moving average (EMA) target encoder, both produced from a single training run: the online encoder develops higher-rank discriminative features, while the EMA target encoder develops smoother, lower-rank temporal features. Exploiting this asymmetry, classification is routed to the online encoder and forecasting or anomaly detection to the EMA target encoder, achieving a 27% reduction in multivariate forecasting mean squared error (MSE) at no additional training cost. Across 126 University of California, Riverside (UCR) and 26 University of East Anglia (UEA) classification datasets, eight electricity transformer temperature forecasting benchmarks, and Key Performance Indicator /Yahoo anomaly detection, CF-JEPA achieves the highest average accuracy and rank on UCR and UEA among self-supervised baselines and ranks second on univariate forecasting and k-nearest neighbors-scored anomaly detection.

---


### 103. [Never Seen Before: Benchmarking Genuine Zero-Shot Composed Image Retrieval with Consistent Video-Sourced Datasets](https://arxiv.org/abs/2606.07032)

**<font color=#1a73e8>作者：</font>** Zhenyu Yang, Zemin Du, Shengsheng Qian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-Shot Composed Image Retrieval (ZS-CIR) aims to retrieve a target image based on a query composed of a reference image and a relative caption without training samples. Existing ZS-CIR datasets often suffer from complete irrelevance between reference and target images due to noisy image sources, and do not achieve a true zero-shot scenario as they use public image datasets that models like CLIP have been trained on. To tackle these challenges, we introduce ZeroSight, a novel benchmark for ZS-CIR. It includes a dataset with consistent reference-target pairs sourced from videos, a data construction pipeline, and evaluation methods that consider the ranking of multiple positive and negative target images. We ensure visually and semantically consistent reference-target pairs by extracting frames from a single video and generating relative captions using LLM-assisted methods. To ensure a true zero-shot scenario, we use video data published after March 31, 2022, ensuring it was not included in CLIP's pre-training data. Additionally, we propose a training-free MLLM-driven method, SC4CIR (Symmetric Consistency for CIR), which can effectively identify hard negative targets through 3 symmetric consistency checks. This method is plug-and-play, seamlessly integrating with various CIR methods and significantly improving performance. Our experimental results from 27 methods reveal that current ZS-CIR datasets and evaluation metrics result in inflated retrieval performance, exaggerating the capabilities of CIR methods. Our benchmark and models can be accessed at this https URL.

---


### 104. [Hierarchical Semantic-Constrained Heterogeneous Graph for Audio-Visual Event Localization](https://arxiv.org/abs/2606.07033)

**<font color=#1a73e8>作者：</font>** Zhe Yang, Ruyi Zhang, Hongtao Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary audio-visual event localization (OV-AVEL) jointly models audio-visual cues to recognize and temporally localize events, including categories unseen during training. Existing methods primarily learn joint audio-visual representations in Euclidean space, but still face two significant challenges. First, the lack of supervision signals for unseen categories makes it difficult to maintain audio-visual consistency across multiple temporal scales. Second, the lack of hierarchical constraints between segment- and video-level semantics prevents the model from establishing semantic consistency across different levels. To address these challenges, we propose a hierarchical semantic constrained heterogeneous graph (HSCHG) for audio-visual event localization framework. We first construct a heterogeneous hierarchical graph in Euclidean space, which includes audio and visual segment nodes and their corresponding video-level nodes. We use multi-directional temporal edges to capture complete temporal information within each modality. Simultaneously, we employ a dual-threshold filtering gated fusion strategy, introducing cross-modal information only when the alignment confidence is high. Furthermore, we introduce bidirectional semantic constraints between segment- and video-level representations to achieve semantic consistency across different levels. Based on this, we map the multi-level audio-visual representations and text prototypes uniformly into hyperbolic space. We use a hierarchical entailment regularization loss to characterize the hierarchical relationships between videos and segments. Extensive experimental results show that our method outperforms existing methods on the OV-AVEL benchmark. Ablation studies further validate the effectiveness of our method.

---


### 105. [ForensicConcept: Transferable Forensic Concepts for AIGI Detection](https://arxiv.org/abs/2606.07034)

**<font color=#1a73e8>作者：</font>** Menyanshu Zhou, Ziyin Zhou, Ke Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated image detectors achieve high accuracy on in-distribution data but often fail on unseen generators. A key obstacle to understanding this failure is the black-box nature of current detectors: they do not reveal which evidence drives their decisions. We propose ForensicConcept, a framework that extracts explicit forensic concepts from detectors and enables their transfer across backbones. Our method localizes decision-critical patches via Transformer attribution, clusters them into a compact concept codebook, and uses a concept-aligned projection to produce auditable evidence readouts. Motivated by prior studies showing that DINO representations can guide diffusion generation and exhibit concept-level correspondence with diffusion features, we introduce a generation-trace reference based on CleanDIFT diffusion features and quantify backbone-trace alignment via neighborhood-structure consistency (CKNNA). We further propose concept codebook injection to transfer diffusion-derived concepts into target backbones. Experiments on GenImage, GAN-family, and Chameleon benchmarks show consistent improvements over prior methods. We also find that CKNNA alignment predicts transfer effectiveness, providing a principled explanation for why some backbones yield more transferable forensic evidence than others.

---


### 106. [STREAM: Stochastic Riemannian Flow Matching with Anisotropic Decoder for Digital Histopathology Image Generation](https://arxiv.org/abs/2606.07036)

**<font color=#1a73e8>作者：</font>** Won June Cho, Daeky Jeong, Hyeongyeol Lim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic histopathology image generation addresses critical challenges in computational pathology, including patient privacy and the growing need for large-scale training data for foundation models. Latent diffusion models have dominated the image generation domain, with recent works emphasizing that the choice of latent space is critical to the quality of generated images. Existing state-of-the-art generative models in histopathology use pretrained Vision Foundation Models (VFMs) as conditioning signals, and we observe that this leads to "conditioning collapse," where the conditioning signal dominates the latent space and lowers the quality and diversity of generated samples. Therefore, we instead use pretrained histopathology VFMs as the latent space itself, leveraging their patch-token features that encode rich semantic information. We empirically show that these features are $\ell_2$-normalized and lie on the unit hypersphere $\mathcal{S}^{d-1}$ with strong angular dominance and intrinsic curvature, making them naturally suited for a Riemannian formulation. We therefore present STREAM, the first framework to apply Riemannian flow matching in the pathology domain. STREAM consists of two stages: 1) a bridge-type stochastic perturbation that establishes per-token rectifiability on $\mathcal{S}^{d-1}$ for training a Diffusion Transformer (DiT) in latent space, and 2) a novel anisotropic decoder that allocates robustness to low-energy directions of the velocity-field Jacobian while preserving fidelity along its high-energy directions. Together, STREAM achieves state-of-the-art reconstruction and generation performance on breast and colorectal cancer datasets. The code will be publicly released upon acceptance.

---


### 107. [Beyond Rubrics: Exploration-Guided Evaluation Skills for Reward Modeling](https://arxiv.org/abs/2606.07040)

**<font color=#1a73e8>作者：</font>** Xing Yue, Linjuan Wu, Daoxin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-ended reward modeling requires judges that can follow subtle, domain-specific preferences when verifiable answers are unavailable. Existing rubric-based methods often address this by generating criteria online for each query, but the extra generation step can add inference overhead and produce rigid or misaligned guidance. We introduce Eval-Skill, an exploration-guided method that synthesizes reusable evaluation skills for reward modeling and reframes reward guidance as context evolution rather than parameter training or per-query rubric generation. Using only 100 cases per domain for skill evolution, Eval-Skill synthesizes reusable domain-level evaluation skills through two progressive stages, workflow generation followed by principle generation, with exploration and selection interleaved across both stages. Once generated, a skill is directly injected into the judge context. Across multiple RM benchmarks, Eval-Skill consistently improves diverse judge backbones; on RewardBench 2, it yields significant gains over vanilla judging for each main backbone (+13.44% for Qwen3-8B, and 18.51% for DeepSeek-V4-Flash). Further analyses of evolution-time scaling, generalizability, and transferability show that compact evaluation skills offer an efficient new paradigm for LLM-based evaluation. Code is available at this https URL.

---


### 108. [Hierarchical Forecast Reconciliation for Urban Rail Transit Demand Prediction under Operational Disruptions](https://arxiv.org/abs/2606.07044)

**<font color=#1a73e8>作者：</font>** Dang Viet Anh Nguyen, Alma Fazlagic, Kristine Pryds Loft 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate and coherent passenger demand forecasting is essential for Urban Rail Transit (URT) operations. Passenger demand has a hierarchical structure in which origin-destination (OD) flows aggregate to station-level inflows and outflows through conservation constraints. In practice, station-level and OD-level forecasts are often generated independently, producing incoherent predictions that violate these constraints and introduce inconsistencies into operational decision-making. Such issues become more severe during disruptions, when forecasting reliability is most critical. This paper presents the first hierarchical forecast reconciliation framework for joint station-level and OD-level URT demand prediction. A neural Fully Connected Reconciler (FCR) learns a non-linear mapping from incoherent base forecasts to coherent hierarchical predictions while guaranteeing exact structural consistency by construction. The method is benchmarked against OLS, WLS, and Minimum Trace (MinT) variants using Rejsekort smart-card data from the Copenhagen S-train network under one-step, multi-step, and disruption forecasting scenarios. Results show that reconciliation consistently improves OD forecasting accuracy while ensuring hierarchical coherence. Under normal conditions, FCR performs competitively with MinT-based methods. An oracle analysis indicates that perfect station-level forecasts could reduce OD prediction error by up to 34 percent, highlighting the value of improved base forecasts. Under severe disruptions, FCR outperforms classical methods, reducing OD forecasting error by up to 17.45 percent in multi-step destination-side delay scenarios. These findings establish hierarchical reconciliation as an effective mechanism for improving forecast robustness, with the largest benefits occurring under the most challenging operating conditions.

---


### 109. [Front-to-Attractors: Modifying the Front-to-Front Heuristic in Bidirectional Search](https://arxiv.org/abs/2606.07047)

**<font color=#1a73e8>作者：</font>** Alvin Zou, Muhammad Suhail Saleem, Maxim Likhachev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heuristics play a central role in the performance of bidirectional search algorithms, which commonly rely on two main classes. Front-to-end (F2E) heuristics estimate the distance from a state s to the target of the search (the goal for forward search or the start for backward search). In contrast, front-to-front (F2F) heuristics estimate the distance from s to the opposite search frontier using a pairwise function h(s, s'), where s' ranges over frontier states. Although F2F heuristics are typically more informative and therefore reduce the number of node expansions, their reliance on extensive pairwise evaluations incurs substantial computational overhead. To address this limitation, we introduce a new heuristic class, front-to-attractors (F2A), that preserves much of the informativeness of F2F while dramatically reducing its computational cost. Rather than evaluating distances to all states on the opposite frontier, F2A estimates the distance from s to a small, dynamically maintained set of attractors in the opposite search direction. These attractors serve as a surrogate for the full frontier, enabling rich heuristic guidance at a fraction of the computational expense while maintaining the optimality guarantees offered by F2F. We evaluate F2A across multiple domains and show that it reduces the number of pairwise evaluations by up to 11.2x compared to F2F, while achieving 4.8x fewer node expansions than F2E on average.

---


### 110. [TrioPose: Native Triple-Stream Diffusion Transformers for Pose-Guided Text-to-Image Generation](https://arxiv.org/abs/2606.07053)

**<font color=#1a73e8>作者：</font>** Dian Gu, Zhengyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-guided text-to-image generation often suffers from limb distortions and feature crosstalk in complex multi-person scenarios. While existing UNet-based adapters struggle with long-range spatial dependencies, emerging Multimodal Diffusion Transformers (MM-DiTs) offer superior global modeling. However, naive signal concatenation in MM-DiTs severely disrupts pre-trained latent distributions. To address this, we propose TrioPose, a native pose-driven framework built upon the SD3.5M architecture. Specifically, we introduce a Triple-Stream Pose-Aware DiT (TSPA-DiT) that treats pose as an independent modality. It employs layer-wise activation and zero-initialized dual-residual injection to smoothly enforce geometric constraints while preserving pre-trained latent stability. To resolve severe multi-instance occlusions, we design a Learnable Relational Bias Mask that categorizes topological connectivity into fine-grained physical states, mapping them into continuous attention soft constraints to effectively decouple inter-instance interference. Furthermore, a Pose-Guided Spatial Loss Weighting strategy modulates the native diffusion objective using heatmap-derived error maps, focusing anatomical supervision strictly on distortion-prone regions. Extensive experiments demonstrate that TrioPose achieves state-of-the-art performance across challenging benchmarks, including Human-Art, CrowdPose, and OCHuman. Notably, it attains an AP of $64.33$ on Human-Art, representing a $30\%$ improvement over prior arts, while setting new standards for visual fidelity and text-image semantic alignment in complex multi-human generation.

---


### 111. [Constructing VAE Latent Spaces with Prescribed Topology](https://arxiv.org/abs/2606.07058)

**<font color=#1a73e8>作者：</font>** Jilles S. van Hulst, Jakub M. Tomczak, W.P.M.H. Heemels 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational autoencoders (VAEs) learn low-dimensional latent representations of high-dimensional data. When the data lies on a manifold with non-Euclidean topology, the standard Gaussian prior introduces a topological mismatch that degrades reconstruction quality and prevents faithful representation. We present a constructive mathematical framework that resolves this mismatch for all manifolds that admit a product covering space. These are manifolds expressible as products of elementary factors (circles, intervals, or lines) or as quotients of such products by a finite symmetry group. The class includes cylinders, tori, Möbius strips, Klein bottles, and real projective spaces. Factorized distributions over the elementary factors yield product topologies with closed-form, decoupled KL divergences, so that each latent factor can be shaped independently while keeping training tractable. We catalogue reparametrizable encoder-prior pairs for periodic, bounded, and unbounded supports, and provide coordinate transformations that allow standard neural networks to output non-Euclidean parameters with smooth gradients. For quotient manifolds, the decoder receives group-invariant features of the covering-space coordinates, so that identified points produce identical outputs. Anchor constraints fix the coordinate system relative to the data or create soft topological holes. Experiments on synthetic manifolds and real-image datasets (rotated and cyclically shifted MNIST) confirm that a topology-matched prior aligns KL regularization with the data manifold. The resulting topology-aware models outperform the Gaussian baseline at all practically relevant regularization strengths. The code is available at this https URL.

---


### 112. [Bias in Filter Feature Selection Evaluation: A Meta-Analysis of Datasets, Baselines, and Experimental Design Choices](https://arxiv.org/abs/2606.07068)

**<font color=#1a73e8>作者：</font>** Malick Ebiele, Malika Bendechache, Rob Brennan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Since 1990 many feature selection methods have been proposed across heterogeneous applications. To validate the usefulness of a new method, it needs to be compared against at least one baseline method from the existing literature on a feature selection task using at least one dataset. Recent developments in tabular Deep Learning (DL) and data valuation in Machine Learning (ML) suggest that the evaluation of new methods, algorithms, and models may be consciously or unconsciously biased. We hypothesise that a similar trend exists in feature selection (FS), particularly in filter feature selection (FFS). The aim of this study is therefore to examine FFS studies to identify factors that influence the evaluation and that might consist entry point for biases in order to recommend stronger principles for FFS evaluation.
Methods: We analyse a sample of 28 high profile FFS studies published between 1994 and 2025. The analysis provides reflections on how to examine FFS studies, highlights lessons learned throughout the process, and gives five evidence-based recommendations for future FFS evaluation.
Results: Multivariate Linear Regression analysis achieved a score of $R^2=0.33$. It means that 33% of the variance in the performance of new methods against chosen baselines (win rate) is explained by the number of datasets (#Datasets), the number of baselines (#Baselines), and the number of new methods (#NewMethods).
Discussion: $R^2=0.33$ is considered medium explanation; which is promising given that this is the first such study. The medium explanation result is due to the fact that win rate is influenced by additional factors such as the maturity of the feature selection domain, the type of datasets and baselines, and the simplicity of the regression model used to explain the relationship.

---


### 113. [SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating](https://arxiv.org/abs/2606.07074)

**<font color=#1a73e8>作者：</font>** Zequn Xie, Junjie Wang, Dan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep research agents have demonstrated remarkable capabilities in complex information-seeking tasks, yet this power comes at a steep computational cost. Driven by accuracy-focused training paradigms, current models adopt brute-force strategies characterized by blind tool dependency and performative reasoning-generating long, redundant trajectories that are far from necessary for resolving these tasks, leading to wasteful tool calls and excessive token consumption. To overcome this efficiency trap, we propose SlimSearcher, a principled framework that pushes the Pareto frontier between accuracy and computational cost across both Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). In the SFT stage, SlimSearcher employs Pareto-efficient filtration to distill trajectories that are both successful and economical, guiding the model toward inherently efficiency-aware search behaviors. During RL, we introduce Adaptive Reward Gating, a dynamic reward-shaping mechanism that evaluates relative tool and token efficiency within a sampled cohort. By cascading these adaptive efficiency metrics with a strict correctness gate, our approach effectively avoids the brevity bias associated with absolute penalties and mitigates reward hacking. Extensive experiments on long-horizon benchmarks, including GAIA, BrowseComp, and XBenchDeepSearch, demonstrate that SlimSearcher reduces average tool-call rounds by 17%-58% while maintaining or improving accuracy.

---


### 114. [AsyncPatch Diffusion: spatially-flexible image generation](https://arxiv.org/abs/2606.07079)

**<font color=#1a73e8>作者：</font>** Samuele Papa, Valentin De Bortoli, Guillaume Couairon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard diffusion models corrupt an entire sample with a single shared noise level, forcing all spatial regions to follow the same denoising trajectory. We introduce AsyncPatch Diffusion, a joint-diffusion framework that assigns distinct noise levels to different input dimensions, such as image pixels, or latent tokens. We show how this asynchronous corruption defines a valid generative process while supporting a richer family of spatially heterogeneous denoising trajectories, and prove the first valid ELBO for this process. We show that a single pretrained model can perform spatially adaptive generation, where different regions are denoised on different schedules. A key challenge is training: naive independent noise-level sampling overemphasizes highly heterogeneous configurations and underrepresents homogeneous noise levels, that are crucial during sampling. We address this with a controlled noise-level sampler that regulates both the average corruption level and its spatial variability. AsyncPatch achieves generation quality comparable to conventional diffusion on ImageNet 256 and LSUN, while being natively suited for inpainting without task-specific fine-tuning. We further introduce input guidance, which uses clean or partially corrupted regions to guide the generation of unknown regions, improving local consistency and texture matching. Finally, we demonstrate adaptive generation strategies including uncertainty-guided acceleration and autoregressive sampling.

---


### 115. [An Adaptive Data cleaning Framework for Noisy Label Detection](https://arxiv.org/abs/2606.07086)

**<font color=#1a73e8>作者：</font>** Chen-Hsuan Fang, Wei-Hsinag Chen, Pin-Hsuan Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) excel in computer vision tasks given large annotated datasets. In real-world applications, however, labels are often corrupted by ambiguity, human error, or dynamic environments. Over-parameterized DNNs easily memorize these noisy labels during training, degrading model accuracy and generalization. Existing data-cleaning and sample-selection strategies often rely on manually specified thresholds, prior knowledge of the noise ratio, or a single metric (either learning dynamics or geometric structure), making them unstable in complex data regimes. This paper proposes a self-adaptive data-cleaning framework that integrates local, global, and learning dynamics cues for robust noisy-label detection. Samples are mapped into a unified low-dimensional feature space through a modular feature concatenation paradigm. We provide two instantiations: a 2D metric integrating class-adaptive KNN-based local disagreement with k-means-based global centroid distance, and a 3D multi-metric that additionally incorporates a z-normalized score. Unlike conventional 1D Gaussian Mixture Models applied to a single scalar metric, our framework performs multi-metric clustering on the feature space to adaptively partition samples into clean-dominant and noise-dominant components without requiring manual thresholds or noise priors. Experiments on CIFAR-10, MNIST, and ImageNet-100 with 5% to 40% symmetric label noise show high recall across settings, including near-perfect recall (>=98%) on ImageNet-100 at 40% noise. Subsequent training yields accuracy gains across evaluated settings, especially under severe corruption on ImageNet-100. These findings suggest that multi-metric integration provides a threshold-free, practical, and low-tuning strategy for noisy label detection.

---


### 116. [Residual-Controlled Multiplier Learning for Stochastic Constrained Decision-Making](https://arxiv.org/abs/2606.07088)

**<font color=#1a73e8>作者：</font>** Kang Liu, Jianchen Hu, Ziyu Qu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic constrained decision-making requires optimizing performance objectives while enforcing statistical requirements such as safety or fairness. However, standard primal--dual methods struggle to update multipliers robustly under stochastic mini-batch feedback, as the noise of mini-batch gradients and constraint estimates can be directly accumulated into the multiplier memory. To address this issue, we propose Residual-Controlled Multiplier Learning (RCML), which reformulates multiplier updating as projected-pressure feedback. The central idea is to decompose the projected multiplier into an effective pressure signal for primal descent and a pressure-memory residual for finite-gain multiplier tracking. To handle heterogeneous and noisy observations, we further augment this residual-integral backbone with modular stochastic stabilization components. For the convex-affine backbone, we establish finite-gain convergence, derive a stochastic residual bound under mini-batch feedback, and show that the residual feedback law admits a local KKT-residual interpretation near regular KKT points of nonconvex problems. Experiments across optimization, allocation, and fair-ranking tasks show that RCML improves feasibility control and multiplier stability while maintaining competitive objective performance. Code is available here.

---


### 117. [Detecting Temporally Localized Manipulations in Authentic Video Streams](https://arxiv.org/abs/2606.07090)

**<font color=#1a73e8>作者：</font>** Okan Umur, Ali Emre Güşlü, Ibrahim Delibasoglu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of video editing and generative artificial intelligence technologies has made realistic video manipulation increasingly accessible. Although existing datasets have significantly advanced research in deepfake detection, object removal, and video inpainting, they do not adequately model scenarios in which a short manipulated segment is inserted into an otherwise authentic video and the original video continues afterward. In this study, we review representative datasets from the literature, analyze their characteristics, and discuss their limitations with respect to temporally localized realistic manipulation detection. Based on this analysis, we motivate the need for a new dataset specifically designed for authentic videos containing short and highly realistic manipulated intervals. Finally, we evaluate two complementary approaches on our custom-curated test set to establish an initial benchmark for this challenging scenario. The first employs a linear probe on DINOv3 features, assessed under three thresholding strategies. The second leverages DINOv3 features with a consecutive frame similarity-based method to detect temporal manipulation boundaries. Together, these experiments provide an initial benchmark for partially manipulated video detection and highlight the need for content-adaptive thresholding mechanisms. The dataset, code, and supplementary materials are publicly available at this https URL.

---


### 118. [The discovery of the effects of women employment participation on the fertility of developing countries: A panel data approach](https://arxiv.org/abs/2606.07093)

**<font color=#1a73e8>作者：</font>** Thi Kim Ngan Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The fertility trend in developing countries has experienced a significant decline in the last few decades; at the same time, the role of women in the workplace has improved. To have a better insight of the causality of the rate of women participation in the labor market on the total fertility rate in developing world, this paper divides the dataset of 115 developing countries in the period of 1991-2018 into four continents group (Africa, North/South America, Asia/Pacific, Europe) and then applies a data-driven panel data econometric procedure to mitigate omitted bias. The results suggest that the fertility behaviors of women in the North/South America continents are influenced by their career choice; meanwhile in society of other regions, other factors might be more important to women when thinking of having children. In conclusion, policymakers can reference to the paper and formulate policies to have more incentives in making reproductive decisions and further research in the field needs to consider family policies and patrilocality of developing countries as important data.

---


### 119. [CANote: Empowering Fact-checking Note Writing Through Scaffolded and Provenance-based Human-AI Collaboration](https://arxiv.org/abs/2606.07101)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Jingruo Chen, Yuwei Chuai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Crowdsourced fact-checking mechanisms, such as X's Community Notes, play a critical role in mitigating the spread of misinformation. However, drafting high-quality, evidence-based debunking notes imposes a substantial burden on contributors. We present CANote, an AI-assisted debunking note writing system featuring evidence correlation and structured co-drafting. CANote scaffolds the workflow by extracting subclaims from social media posts, providing provenance through explicit links between subclaims and retrieved evidence, and generating neutral, structural drafts to support human reasoning. We evaluated CANote against manual writing (N=52 fact-checkers, N=52 lay users) on simulated X platform, where we found CANote significantly improves note quality. Notably, CANote enables lay users to write notes that have comparable quality to those written by experts. While the task completion time and perceived cognitive load remain comparable to manual drafting, CANote significantly increases user satisfaction. However, this assistance introduces a trade-off, resulting in a reduced sense of user ownership and control over the debunking note.

---


### 120. [Style or Content? Evaluating Style Classifiers with Controlled Content Overlap](https://arxiv.org/abs/2606.07103)

**<font color=#1a73e8>作者：</font>** Zhuo Liu, Haozheng Du, Xiangxiang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Style classifiers can use content cues that correlate with style labels in naturally collected data, yet we lack a systematic way to measure this reliance. We study this problem with a controlled content overlap setup built on parallel Bible translations. Specifically, we define the overlap parameter $\alpha$ as the normalized residual of mutual information between content identity and style label, so that it measures how much content is shared across style classes: from no shared content ($\alpha=0$) to fully shared content ($\alpha=1$). Cross-overlap evaluation of RoBERTa-based classifiers shows that low-overlap models degrade when content cues are removed, while high-overlap models transfer more robustly. A cross-style content retrieval probe further shows that content becomes less recoverable as $\alpha$ increases, with training dynamics showing this removal occurs gradually. Together, these results suggest that controlled overlap provides a simple diagnostic for separating style learning from content shortcuts.

---


### 121. [DyCon: Dynamic Reasoning Control via Evolving Difficulty Modeling](https://arxiv.org/abs/2606.07108)

**<font color=#1a73e8>作者：</font>** Tengyao Tu, Yulin Li, Hui-Ling Zhen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Reasoning Models (LRMs) demonstrate remarkable performance improvements by iteratively reflecting, exploring, and executing complex tasks, yet suffer from inefficiencies due to redundant reasoning, known as "overthinking". Existing methods to mitigate this issue either rely on static difficulty estimates or require task-specific training, and thus fail to adapt to the dynamic complexity during reasoning. In this work, we empirically show that the problem difficulty evolves dynamically throughout the reasoning process and is linearly encoded in the LRM's step-level embeddings. Building on this insight, we propose DyCon, a training-free framework that leverages latent step-level representations to explicitly model the evolving task difficulty, enabling the dynamic control of reasoning depth to mitigate the overthinking issue. Extensive experiments conducted on four models ranging from 4B to 32B, and across twelve benchmarks in math reasoning, general question answering, and coding tasks demonstrate that DyCon significantly enhances reasoning efficiency by reducing redundant steps without sacrificing accuracy or generalization. Project page and code are available at this https URL.

---


### 122. [Beyond Post-hoc Explanation: Toward Glassbox AI via Probabilistic Mediation](https://arxiv.org/abs/2606.07113)

**<font color=#1a73e8>作者：</font>** Manuele Leonelli  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are rapidly becoming infrastructural components in high-stakes institutional settings, including public administration, legal reasoning, and healthcare, where opacity is not merely inconvenient but institutionally and legally untenable. Existing approaches to explainability are predominantly post-hoc, offering unstable, non-contestable accounts that have no formal relationship to the reasoning process that produced the output. We argue that the problem is not the absence of explanation but the absence of structured reasoning in the first place. This paper makes the case for a fundamentally different architecture, which we call the Glassbox Framework, in which Bayesian networks serve as transparent, ante-hoc mediation layers for generative models. Bayesian networks encode domain knowledge, causal assumptions, and probabilistic dependencies before inference occurs, enabling auditable reasoning traces, uncertainty quantification, and contestable outputs. We characterise the architecture of this framework and ground it in a benefit eligibility scenario, identifying the foundational challenges spanning semantic alignment, dynamic model construction, probabilistic grounding, and human governance that must be solved to realise it at scale. By shifting from post-hoc explanation to ante-hoc probabilistic mediation, this work outlines a principled path toward AI systems that are not only powerful but fundamentally accountable.

---


### 123. [3DMorph: Single-Image-Guided Local 3D Shape Editing and Morphing](https://arxiv.org/abs/2606.07115)

**<font color=#1a73e8>作者：</font>** Tobias Preintner, Yunfei Deng, Phillip Müller 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in 3D generation, intuitive editing of existing shapes remains limited. Unlike images, which benefit from well-established inpainting tools, general 3D objects such as meshes still lack simple and effective methods for local shape editing. Existing approaches are often global, domain-specific, require complex user interaction, or focus on appearance (color and texture) rather than geometry. We introduce 3DMorph, a training-free framework for single-image-guided local 3D shape editing and morphing. Given an edited image showing a desired shape modification, our method automatically localizes the relevant 3D region and transfers 2D modifications to 3D while preserving unmodified areas. 3DMorph also enables intermediate shape generation between the original and edited objects, facilitating design exploration. To benchmark editing quality, we introduce Delta3D, an image-guided local 3D editing benchmark with paired ground-truth edits. Experimental results show that 3DMorph translates intuitive 2D edits into 3D, outperforming state-of-the-art generative and editing methods.

---


### 124. [Beyond Linear and Overcomplete Regimes: A Mean-Field Analysis of Bottleneck Autoencoders](https://arxiv.org/abs/2606.07120)

**<font color=#1a73e8>作者：</font>** Santanu Das, Ramyak Bilas, Pascal Esser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoencoders (AEs) learn low-dimensional representations by mapping data into a latent space while minimizing reconstruction error. Despite their empirical success, theoretical understanding remains limited and largely restricted to linear models or settings without a bottleneck. In this work, we study nonlinear AEs with a fixed finite-dimensional bottleneck in the mean-field (MF) regime. We derive explicit MF learning dynamics for both encoder and decoder, providing a tractable characterization of training in the nonlinear setting. We show that, over finite time horizons, the empirical risk of finite-width networks trained with stochastic gradient descent closely tracks the MF risk trajectory with high probability. At optimality, we further establish that the finite-width risk converges to the MF optimum, demonstrating that finite networks are sufficiently expressive to approximate the infinite-width solution.

---


### 125. [Learning Perspectivist Social Meaning via Demographic-Conditioned Fusion Embeddings](https://arxiv.org/abs/2606.07123)

**<font color=#1a73e8>作者：</font>** Amanda Cercas Curry, Lucio La Cava, Luca Maria Aiello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social meaning in language is inherently perspectival, varying across annotator backgrounds, demographics, and ideological positions. However, most NLP systems collapse this variation into a single ground-truth label, ignoring the diversity of interpretations. In this work, we model social dimensions along a perspectivist spectrum, capturing how interpretations vary across demographic groups on a dataset consisting of 28k human annotations. We benchmark multiple modeling paradigms, including zero-shot, few-shot, and fine-tuned approaches, and propose fusion embeddings that integrate textual and demographic representations. Our fusion models yield consistent and statistically significant improvements over text-only baselines across all fusion strategies (+5.9-6.5% relative macro PR-AUC), with shuffle ablations confirming that demographic profiles carry genuine predictive signal rather than spurious correlations.

---


### 126. [Learning Explicit Behavioral Models with Adaptive Questions and World-Model Probes](https://arxiv.org/abs/2606.07127)

**<font color=#1a73e8>作者：</font>** Hikaru Shindo, Yu Deng, Teng Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive agents trained only against task return can achieve high scores while failing to represent the mechanisms that make their actions succeed. This makes brittle behavior difficult to diagnose and limits adaptation when environment dynamics change. Existing LLM reflection and policy-code repair can revise behavior from failed trajectories, but questions and world-understanding tests are usually used only after training. We introduce an Explicit Symbolic Behavioral Model (ESBM), a trainable behavioral model that couples task performance with evidence-grounded question answering and executable mechanism prediction. An ESBM represents behavior through typed predicates, weighted rules, bounded options and mechanism memory; the mechanism layer predicts symbolic events, object changes, rewards and terminal consequences under action interventions. After each rollout, adaptive questions and active world-model probes convert score failures, QA errors and transition-prediction errors into constraints for local ESBM edits. Candidate models are selected by a multi-criterion rule that jointly evaluates task score, answerability and active world-model consistency. Under the tested Atari-style protocols, ESBM learns high-scoring policies while producing explicit answers and executable mechanism predictions, indicating that adaptive questions can serve as both training pressure and reusable benchmarks for mechanistic policy learning in this setting.

---


### 127. [A machine-learning-assisted progressive digit-randomness screening framework for detecting non-random patterns in raw numerical research data](https://arxiv.org/abs/2606.07128)

**<font color=#1a73e8>作者：</font>** Zhuphua Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Raw numerical datasets remain less systematically examined in integrity screening than images, plagiarism, or summary-statistic inconsistencies. We developed the Fabrication-risk Digit Randomness Screening model (FDRS), a statistical and machine-learning framework for detecting non-random digit-pattern irregularities in numerical research data. FDRS integrates single- and joint-decimal-digit tests, Cramer's V, entropy metrics, Kullback-Leibler divergence, digit-preference indices, progressive subsampling, and semi-supervised risk scoring. It was evaluated using an instrument-derived enzymatic absorbance dataset (RawData, n=253) and a blinded manually simulated irregular dataset (ErrData, n=255). RawData showed no significant deviation in single third-decimal-digit analysis, whereas ErrData showed a significant deviation. In joint third-fourth decimal digit analysis, ErrData showed higher Cramer's V, lower normalized entropy, higher KL divergence, and a more persistent progressive-subsampling deviation signal. In internal validation, Elastic-net Logistic Regression achieved the highest AUC (0.98395) and lowest Brier score (0.048439), while Random Forest achieved the highest accuracy (0.926667) and balanced accuracy (0.935). RawData received a low ensemble risk score of 0.124627 and was classified as Grade 0; ErrData received a score of 0.740760 and was classified as Grade 3. External real-world benchmarks supported graded risk stratification: three datasets without identified public post-publication concerns were classified as Grade 0 or 1, whereas two datasets from publicly questioned or institutionally handled articles were classified as Grade 2 or 3. FDRS can prioritize raw numerical datasets for further review by integrating interpretable statistical and machine-learning features. It is an auxiliary digit-structure screening tool, not standalone evidence of fabrication or misconduct.

---


### 128. [Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/abs/2606.07130)

**<font color=#1a73e8>作者：</font>** Anar Yeginbergen, Amelie Wührl, Anna Rogers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As AI systems become more widely adopted, the demand for factual and faithful generation grows. Properly attributing information through citations becomes, therefore, crucial. This work introduces FullCite, a framework that, in contrast to most previous works, generates structured inline citations linking each claim to both its source document and supporting evidence. FullCite proposes three strategies to inline citation generation: prompt-based generation, constrained decoding over a citation grammar, and posthoc span alignment. Using three question answering benchmarks, namely, ASQA, BioASQ, and ExpertQA, we assess citation quality and faithfulness along three dimensions: document-level correctness, evidence span identification, and claim-citation faithfulness. Our evaluation shows that while LLMs are generally effective at identifying relevant documents, they struggle to identify the precise supporting spans within them. This gap suggests that achieving faithful attributed QA will require research to place greater emphasis on precise evidence span identification.

---


### 129. [Explaining Unsupervised Disease Staging in Huntington's Disease: Insights into Model Representations and Clusters](https://arxiv.org/abs/2606.07135)

**<font color=#1a73e8>作者：</font>** Lubna Mahmoud Abu Zohair, Hind Zantout  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Huntington's disease (HD) is a progressive neurodegenerative disorder that affects motor, cognitive, and behavioral functions, where accurate characterization of disease progression remains essential to improve patient outcome and quality of life. Unsupervised machine learning (ML) approaches have demonstrated the ability to uncover disease progression trajectories and meaningful latent stages from longitudinal data; however, their limited interpretability restricts clinical trust and translation. We extend a previously proposed ML-based disease staging framework by applying an explainability analysis to the extracted feature representations and discovered disease stages. Applied to the Enroll-HD dataset, we first project the learned representations into a lower-dimensional space to intuitively assess whether the resulting clusters align with the progression of established clinical measures. We then use saliency maps to identify the clinical features that most strongly contribute to the learned embeddings over time. Finally, we train a surrogate classifier and apply SHAP to quantify feature importance for cluster assignments and to analyze which clinical variables drive transitions between disease stages. The explainability analysis indicates that the learned embeddings capture clinically meaningful disease structure, aligning with established motor and functional severity scores and exhibiting progressive deterioration across clusters. Within this analysis, SHAP reveals a stratification of disease stages, ranging from early cognitive-motor impairment to severe functional dependency, consistent with known clinical progression patterns, while also highlighting intra-stage variability.

---


### 130. [REMEDI: A Benchmark for Retention and Unlearning Evaluation in Multi-label Clinical Disease Inference](https://arxiv.org/abs/2606.07141)

**<font color=#1a73e8>作者：</font>** Anurag Sharma, Sai Teja Chunchu, Prasenjit Mitra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models trained for clinical disease inference are trained on patient data, which may include sensitive and private information, and data owners may request the removal of their data from a trained model due to privacy or copyright concerns. However, exactly unlearning patient-specific data is intractable, and retraining with minor data removal is resource-intensive. While there exists several machine unlearning methods that can be used, their utility is generally restricted to non-medical domains. Moreover, the existing benchmarks for evaluating such unlearning methods primarily utilize synthetically curated datasets, which are not truly representative of real-world systems. Hence, the effectiveness of these unlearning methods in the medical domain is largely unclear. To this end, we introduce REMEDI, an extensive benchmark for machine unlearning tailored to multi-label and multiclass clinical disease inference, where label correlations, longitudinal structure, and safety constraints make unlearning particularly challenging. Unlike the existing benchmarks, REMEDI considers: (1) a relevant application domain (medical), (2) comprehensive unlearning setups involving diverse sets of forget instances, (3) challenging unlearning scenarios including multi-label and multi-class classification tasks, and (4) evaluation metrics involving performance both in terms of utility and extent of unlearning achieved. REMEDI is developed using the MIMIC-III clinical database that contains comprehensive clinical data of patients. Experiments with existing unlearning methods indicate that there exists a trade-off between utility and unlearning performance. They are also largely unsuited to multi-label classification tasks. To facilitate reproducibility, we make our benchmark publicly available.

---


### 131. [Consistent-Inversion: Reverse Consistency Guidance for Structure-Preserving Visual Editing](https://arxiv.org/abs/2606.07145)

**<font color=#1a73e8>作者：</font>** Xiaocheng Lu, Jingcai Guo, Song Guo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided diffusion models have become effective tools for real-image visual editing, where the edited image must follow a target instruction while preserving editing-irrelevant structure. Most training-free editors rely on inversion: a source image is mapped to a noisy latent trajectory and the terminal latent is reused for target-prompt denoising. This reuse is useful for preservation, but it also couples source reconstruction and target editing. The resulting trajectory mismatch may either damage background/layout details or over-constrain the intended edit. This paper presents Consistent-Inversion, a training-free reverse consistency guidance framework for structure-preserving visual editing. Instead of treating the inverted source latent as a fixed initialization, Consistent-Inversion checks whether an intermediate target trajectory can be reversed toward the source inversion trajectory under the source prompt. To make this check well-defined, we construct an auxiliary target-side noise representation, perform source-guided reverse denoising, and use the resulting reverse consistency discrepancy as a correction signal for selected early target denoising steps. The method does not update model parameters, is compatible with inversion-based editors, and introduces only a small inference overhead when applied sparsely. Experiments on PIE-Bench show that Consistent-Inversion improves background and structural fidelity under a unified SD3.5 protocol while maintaining target-prompt alignment, and compatibility experiments further verify the same correction principle on classical Stable-Diffusion inversion pipelines.

---


### 132. [Decision-Aware Evaluation of Physics-Informed Surrogates](https://arxiv.org/abs/2606.07146)

**<font color=#1a73e8>作者：</font>** Daniel Cieślak, Andrzej Czyżewski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed machine learning is often assessed by curve error, although engineering use depends on downstream decisions: ranking candidates, avoiding infeasible designs and limiting regret. We introduce pinn-gym, an open benchmark for material-conditioned lattice design that couples a transparent reduced-order crush-and-impact oracle with five printable polymer cards, dimensionless force-response targets and a protocol spanning curve fidelity, physical admissibility, top-k retrieval and mass regret.
Across per-material, pooled and cross-material settings, low nRMSE is frequently insufficient to identify useful design selections. Physics-informed losses alter trade-offs rather than monotonically improving all metrics, and dimensionless conditioning improves comparability without making transfer symmetric. The benchmark is not a certified material model; within the released oracle, candidate generator and material cards, pinn-gym provides a reproducible testbed for evaluating PIML surrogates as decision systems rather than curve predictors alone.

---


### 133. [From Privacy to Workflow Integrity: Communication-Graph Metadata in Autonomous Agent Interoperability](https://arxiv.org/abs/2606.07150)

**<font color=#1a73e8>作者：</font>** Bijaya Dangol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent-interoperability protocols such as A2A and MCP standardize what agents say to one another, but assume address-based transport over HTTP(S). Such transports protect message content, increasingly with end-to-end encryption. What they leave in the clear is the communication graph: which agent contacts which, when, and how often. In agent systems this graph is more consequential than a privacy framing suggests. Endpoints are often capability-labeled, workflows are structured and chained, and interactions are coupled to real actions, so an observer recovers more than past relationships. It can infer the pending workflow, the task being assembled and the action likely to follow. At machine speed, it can act on that inference before the workflow completes. The threat is therefore one of workflow integrity, not privacy alone: predictive leverage over autonomous action. We give a threat model for the agent communication graph; identify what makes agent metadata distinctively revealing (semanticity, prospectivity, actuation); define transport- and bootstrap-layer privacy properties and weigh candidate transports (SimpleX/SMP, Tor, mixnets) against them; and present an A2A case study in which a metadata-protecting binding is expressible but surfaces the protocol's identity assumptions. We test these on a generative model anchored to a real A2A capture. From passive metadata alone, with no payloads, a classifier recovers a task's class well above chance, from only the workflow's opening; applied together, the properties drive that recovery sharply back toward chance. Beyond what an observer can recover, we measure the leverage of acting on the leak: from a workflow's opening and under a fixed budget, an adversary choosing which workflows to act on realizes in this model most of a clairvoyant attacker's advantage over a metadata-blind one, and the same properties suppress it.

---


### 134. [Geodesics of Dynamic Graphs for Regime Change Detection](https://arxiv.org/abs/2606.07151)

**<font color=#1a73e8>作者：</font>** William Cappelletti, Étienne Voutaz, Pascal Frossard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional change point detection in dynamic networks assumes abrupt transitions between stationary states, overlooking scenarios of continuous evolution which arise in most real-world applications, such as social networks or physical systems. We address this gap by formally defining regimes as periods of coherent dynamics in temporal graphs, which we characterize as trajectories along geodesics in a suitably defined graph space. This original perspective allows us to define regime changes as significant drifts in dynamics, either toward new trajectories or with pace changes. We leverage graph regression methods to measure the cumulative distance of sequences of observed graphs from the estimated geodesics between their endpoints, in the relevant graph space, which we can combine with change point detection algorithms. We present experiments on dynamic networks, with changing trajectories and varying speeds, in which we outperform state of the art change point detection models. Then, we analyse mobility data during the Covid-19 pandemic, and show that our assumptions on regular network evolution lead to change points that are more aligned to external events compared to the outcomes of baseline methods. Our work is the first to model and detect changes between evolving regimes in graph space, providing a realistic and powerful tool for analyzing complex temporal graph data.

---


### 135. [Think Fast: Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models](https://arxiv.org/abs/2606.07157)

**<font color=#1a73e8>作者：</font>** Dewi Gould, Francis Rhys Ward, Anders Cairns Woodruff 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many efforts to ensure frontier AI models are safe rely on monitoring their chain-of-thought (CoT) reasoning. If models become able to perform sufficiently complex reasoning internally, without explicit thinking tokens, this would undermine such oversight. We measure how well frontier models reason without CoT across a suite of over 30,000 questions spanning 43 benchmarks in domains including math, coding, puzzles, causality, theory-of-mind, and strategic reasoning. To compare models against humans, we estimate the $50\%$-task-completion time horizon (TH): the human time required for tasks a model completes with $50\%$ success rate. We complement this with a $50\%$ reasoning token horizon: the minimum number of o3-mini reasoning tokens needed for tasks a model solves with $50\%$ success rate. We find that the no-CoT $50\%$ TH of frontier models has been doubling roughly every year over the past six years, with GPT-5.5's TH reaching over 3 minutes and reasoning token horizon exceeding 1,500 tokens. Our median estimates predict that frontier no-CoT THs could exceed 7 minutes by 2028, and 25 minutes by 2030, though these projections carry substantial uncertainty. We recommend frontier developers track this explicitly.

---


### 136. [Synthetic APTs: the Collapse of TTP-Based Attribution](https://arxiv.org/abs/2606.07158)

**<font color=#1a73e8>作者：</font>** Francesco Balassone, Víctor Mayoral-Vilches, María Sanz-Gómez 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence CTI attribution relies on identifying the Tactics, Techniques, and Procedures TTPs that distinguish one threat actor from another. This approach presupposes that each adversary leaves a recognizable operational fingerprint. This work investigates whether AI driven adversary emulation challenges that presupposition. We deploy agents from our Cybersecurity SuperIntelligence CSI framework, configured as five Advanced Persistent Threat APT groups, APT28, APT29, APT41, APT44, and Lazarus Group, against AI driven Defender agents across two cyber ranges provided by CYBER RANGES, equipped with defensive software Wazuh, Velociraptor, Elasticsearch and active AI driven defenders: an enterprise network and a military infrastructure. Across 20 experiments using two defender models, a binary pattern emerges: all 10 Enterprise range experiments resulted in compromise 2 to 12 hosts per experiment, while all 10 Military range experiments were successfully defended or resulted in stalemates, regardless of APT profile or defender model. In 8 of 10 Enterprise experiments, attackers independently weaponized the defender's own Velociraptor endpoint management platform as a command and control channel, a convergent behavior not encoded in any threat intelligence profile. We argue that in the AI era, wherein agents can be deployed provided the right models are available and subject to the right scaffolding and agentic configuration, the entry barrier for operating like a nation state APT collapses: beyond nation states, individuals can now act like commonly identified threat actors, and with it, fundamentally undermine TTP based attribution.

---


### 137. [UrduMMLU: A Massive Multitask Benchmark for Urdu Language Understanding](https://arxiv.org/abs/2606.07167)

**<font color=#1a73e8>作者：</font>** Ahmer Tabassum, Sarfraz Ahmad, Hasan Iqbal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meaningful multilingual evaluation must test models in the target language and educational context. Urdu, spoken by more than 230 million people, lacks a broad MMLU-style benchmark built from native educational sources. We introduce UrduMMLU, a benchmark of 26,431 Urdu MCQs across 26 subjects and five domains, collected from native Urdu MCQ banks and public examination PDFs. Unlike translation-based resources, UrduMMLU covers both standard academic subjects and Urdu- and region-specific content. We label the exam-derived portion through dual human annotation with strict consensus filtering. We evaluate 30 LLMs under English and Urdu prompts, yielding 60 zero-shot evaluations, and further evaluate four open-source LLMs under multiple few-shot settings across both prompt languages. Gemini-3.5-Flash performs best, reaching 90.20% and 90.34% accuracy, while no other model exceeds 85%. The strongest open-source model trails by 7.79 and 8.92 points, and many models lose 25 to 40 points on Urdu-centered Humanities subjects compared with STEM. Few-shot prompting yields only modest gains. UrduMMLU shows that Urdu knowledge remains uneven in current LLMs, especially for regionally grounded content.

---


### 138. [EvoGS: Constructing Continuous-Layered Gaussian Splatting with Evolution Tree for Scalable 3D Streaming](https://arxiv.org/abs/2606.07179)

**<font color=#1a73e8>作者：</font>** Yuang Shi, Simone Gasparini, Géraldine Morin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D Gaussian Splatting requires highly scalable, progressive representations. Existing progressive methods rely on \textit{discrete layering}, accumulating separate splat sets for each level of detail. This structural independence between layers inherently leads to error accumulation, severe splat redundancy, and uncontrolled quality transitions. We propose EvoGS, the first \textit{continuous-layering} representation. Organized as an Evolution Tree, EvoGS generates finer details via an explicit, wavelet-inspired parent-child refinement. This empowers child nodes to structurally correct ancestral errors, yield inherently sparse and highly compressible inter-layer signals. Extensive experiments show EvoGS eliminates splat redundancy from over 65\% to under 25\%. Compared to state-of-the-art baselines, it reduces transmission payload and GPU VRAM footprint by up to 2.4$\times$ and 5.5$\times$, respectively, and achieves smooth quality transitions optimal for real-time adaptive streaming. Project page: this https URL

---


### 139. [OPTIMUS-Prime: Minimal and Sufficient Concept Explanations for Deep Vision Models](https://arxiv.org/abs/2606.07180)

**<font color=#1a73e8>作者：</font>** Arthur Hoarau, Chenrui Zhu, Vu Linh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The growing demand for transparency in automated decision-making has propelled eXplainable Artificial Intelligence (XAI) to the forefront of machine learning research. In computer vision, however, existing explanation methods often prioritize end-user accessibility at the expense of formal guarantees, leaving a critical gap between practical utility and theoretical rigor. In this paper, we address this gap by introducing OPTIMUS, a novel framework for generating concept-based visual explanations for deep classification models. OPTIMUS explanations take the form of visual heatmaps that not only remain interpretable to end users, but are grounded in the well-established theory of prime implicants, providing formal guarantees that have been largely absent from existing saliency-based methods. Specifically, OPTIMUS explanations satisfy two desirable properties: sufficiency, ensuring that the highlighted concepts provably guarantee the classifier's prediction, and minimality, ensuring that no strict subset of those concepts retains this guarantee. Together, these properties yield explanations that are both logically tight and visually coherent. We validate our approach on a visual classification benchmark, demonstrating that OPTIMUS heatmaps naturally and faithfully surface the decision-relevant concepts underlying model predictions.

---


### 140. [RETROSPECT: RETROsynthesis via Sequential Prediction, and Chemically Transformed-ranking](https://arxiv.org/abs/2606.07181)

**<font color=#1a73e8>作者：</font>** Raja Sekhar Pappala, Shreyas Vinaya Sathyanarayana, Ronit Kumar Choudhary 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-step retrosynthesis needs both accurate first-ranked suggestions and candidate lists that are rich enough for downstream selection. We study this as a proposal-selection decomposition. Our system, RETROSPECT, combines a single Transformer proposal model, which we call the ChemAlign Transformer, with a LambdaMART reranker over structural, reaction-template, upstream-score, and optional DFT-derived descriptors. The generator is trained with hybrid root-aligned and random SMILES augmentation, Pre-LayerNorm, tied embeddings, exponential moving average weights, and a differentiable atom-balance auxiliary loss. On the full USPTO-50K test set of 5,007 reactions, the generator reaches 55.00% top-1 and 86.18% top-10 exact-match accuracy with 99.86% top-1 validity. On the merged candidate-pool benchmark used for reranking, which contains 5,007 test products and about 111 candidates per product, a LambdaMART model trained on the structural feature set reaches 59.4% top-1 with 0.7171 mean reciprocal rank. Feature ablations show that upstream proposal score and template-frequency statistics provide most of the reranking signal, while DFT and reaction-center DFT features provide smaller and less consistent gains. These results support a modular view of retrosynthesis: stronger single-model proposal and learned candidate selection are complementary, and the proposal model can serve as a drop-in component for ensemble systems such as RetroChimera (Maziarz et al., 2024)

---


### 141. [Geometry of Semantic Space: Comparative Study of Discrete and Continuous Models](https://arxiv.org/abs/2606.07183)

**<font color=#1a73e8>作者：</font>** Gabriel Bounias, Sabine Ploux  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work examines the semantic geometry underlying NLP models. We compare supervised vector embeddings, such as CamemBERT, with lexical co-occurrence graphs that encode semantic relations more directly. While transformer-based embeddings achieve strong performance, their induced geometries often display unsatisfactory distributions. In contrast, graph-based models reveal a clearer and more human-readable organization of meaning. We have implemented a methodology that allows us to perform a comparative analysis either based on the structure of the graphs or based on the topology of the embeddings induced by these two approaches. The results of the comparison -- applied to the French "Great National Debate" corpus a collection of citizen contributions to the public debate -- show a similar local topology but a very different overall structure and topology. Theses findings suggest complementary perspectives between deep supervised models and graph-based models, considering a new pathway to guide neural architectures toward more stable and interpretable convergence with graphs structures.

---


### 142. [AdaTok: Self-Budgeting Image Tokenization with Quality-Preserving Dynamic Tokens](https://arxiv.org/abs/2606.07185)

**<font color=#1a73e8>作者：</font>** Xiaocheng Lu, Yuxi Chen, Jie Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image tokenizers, from 2D grids to recent 1D sequences, typically encode every image with the same fixed number of tokens. Yet visual complexity is highly heterogeneous, so a uniform budget overspends on simple inputs and underserves complex ones. Existing elastic tokenizers expose variable-length reconstructions, but often leave token length as a deployment-time operating point, a search target, or an external prediction rather than an output of the tokenizer itself. In this work, we ask whether a discrete visual tokenizer can budget itself in one pass. Our central finding is that actionable elasticity requires a representation--allocation co-design: prefixes must remain decodable across budgets, and the tokenizer must learn which prefix each image needs. We propose AdaTok, a self-budgeting discrete 1D tokenizer. AdaTok combines Prioritized Representation Learning, which orders tokens with nested tail masking and resolves budget-dependent semantic shift through Multi-Head LoRA decoder heads, with Adaptive Token Allocation, which trains a lightweight deterministic-group GRPO policy over candidate budgets. Dynamic Pareto Weighting balances fidelity and efficiency during policy training without manual trade-off sweeps. On ImageNet-1K, AdaTok-Full reaches rFID 1.31 at 256 tokens, while AdaTok-Adaptive attains rFID 1.50 using only ~118 tokens on average, outperforming discrete 1D baselines at comparable budgets. In autoregressive image generation, the shorter adaptive representation yields ~2.1x throughput over a fixed 256-token decode, suggesting that visual token count can be learned as a content-conditioned output rather than set as a fixed hyperparameter.

---


### 143. [Structure-Preserving Correction Learning for Sparse Bayesian Inference in Brain Source Imaging](https://arxiv.org/abs/2606.07196)

**<font color=#1a73e8>作者：</font>** Marco Morik, Xiao Ruiting, Shinichi Nakajima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical sparse Type-II Bayesian methods for M/EEG brain imaging support joint estimation of source and noise hyperparameters, but rely on fixed iterative update rules. Although these updates are principled and interpretable, their dynamics cannot be adapted from data. We propose to learn the update mechanism itself while preserving the underlying Bayesian structure by unfolding a classical joint hyperparameter-learning solver into a trainable neural architecture whose layers mirror the original iterations. The resulting framework is initialized to recover the classical solver exactly before training and is enriched through progressively more expressive correction-learning mechanisms, ranging from learnable biases to adaptive MLP and attention-based contextual refinements. In this way, training does not replace Bayesian inference with a black-box predictor, but instead learns structured correction terms while retaining the interpretability and model-based character of the original update dynamics. Structured correction learning therefore aims to improve empirical reconstruction performance without replacing the original model-based inference mechanism. Experimental results show that the learned correction variants improve reconstruction performance and convergence behavior over the baseline unfolded solver while preserving its algorithmic transparency.

---


### 144. [Learning Multi-Agent Communication Protocol: Study on Information Entropy Efficiency in MARL](https://arxiv.org/abs/2606.07200)

**<font color=#1a73e8>作者：</font>** Xinren Zhang, Zixin Zhong, Jiadong Yu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-Agent Systems (MAS) have emerged as a fundamental paradigm for distributed problem-solving, where autonomous agents collaborate to achieve complex objectives. Within this framework, Multi-Agent Reinforcement Learning (MARL) with communication has demonstrated remarkable success in cooperative tasks. However, existing approaches predominantly pursue performance gains through increasingly complex architectures and expanding communication overhead, lacking principled metrics to evaluate the efficiency of information exchange. In this paper, we focus on enabling agents to learn efficient multi-agent communication protocols that balance performance and information compactness. We propose the Information Entropy Efficiency Index (IEI), a novel metric that quantifies the ratio between message entropy and task performance in learned communication protocols. A lower IEI indicates more compact and efficient message representations. By incorporating IEI into training loss functions, we encourage agents to develop communication protocols that achieve high performance with improved communication efficiency. Extensive experiments across diverse MARL algorithms demonstrate that our approach achieves equivalent or superior task performance compared to baseline methods while improving communication efficiency. These findings challenge the prevailing assumption that performance improvements require complex architectures or increased communication overhead and highlight the potential of improving both task success and communication efficiency to enable scalable MAS.

---


### 145. [Adversarial Creation and Detection of AI-Generated Social Bot Content](https://arxiv.org/abs/2606.07219)

**<font color=#1a73e8>作者：</font>** Mykola Trokhymovych, Ricardo Baeza-Yates, Alessandro Flammini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The convergence of large language models and social bots allows malicious actors to manipulate the information ecosystem by generating human-like content at scale. Existing models for detecting AI-generated content often fail in the wild, primarily due to the lack of ground-truth data. We address this gap through an adversarial methodology that models the impersonation of real social media users by malicious actors. Using this methodology, we curate a multilingual, cross-platform dataset of paired human and AI-generated messages. Training on such adversarial data yields accurate detection of AI-generated text. Our approach significantly outperforms existing models for content-based bot detection in real-world, out-of-distribution data.

---


### 146. [DualGate-Net: A Prior-Gated Dual-Encoder Framework for Histopathology Cell Detection](https://arxiv.org/abs/2606.07222)

**<font color=#1a73e8>作者：</font>** Bahman Jafari Tabaghsar, Son Tran, K. Devaraja 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cell detection in histopathology images strongly depends on surrounding tissue context, where visually similar cells may belong to different classes under different microenvironments. Recent tissue-aware methods incorporate contextual priors, but often rely on static fusion strategies that may propagate noisy information. In this work, we propose DualGate-Net, a prior-aware dual-encoder framework that combines a ConvNeXtV2-based local encoder and a SegFormer-based global encoder through a learnable prior-gated fusion mechanism. The proposed module adaptively regulates the influence of tissue priors across spatial locations, while an auxiliary foreground reconstruction branch preserves high-frequency cellular structures during training. In addition, auxiliary cellness-guided cues are incorporated to further improve localization robustness. Experiments on the OCELOT benchmark demonstrate consistent improvements, achieving macro F1-scores of 0.7722 on the validation set and 0.7345 on the test set, highlighting the effectiveness of adaptive prior integration for robust histopathology cell detection.

---


### 147. [DEFINED: A Data-Efficient Computational Framework for Fine-Grained Creativity Assessment in Debate Scenarios](https://arxiv.org/abs/2606.07226)

**<font color=#1a73e8>作者：</font>** Tongzhou Yu, Mingjia Li, Hong Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human creativity has emerged as a critical competency in the era of large language models. Assessing creativity in complex, open-ended environments is a grand challenge in data mining, currently hindered by a reliance on standardized simple tasks and the scarcity of fine-grained expert data. As an ecologically valid assessment context, debate reflects multiple dimensions of creativity, encompassing both divergent thinking and convergent thinking. Moreover, debate is a data-rich domain, with a large volume of publicly accessible materials. Current mainstream automated scoring methods are poorly suited to complex settings such as debate, and therefore still rely on costly human evaluation. To this end, this paper proposes DEFINED, a data-efficient computational framework for fine-grained creativity assessment in debate scenarios. DEFINED operationalizes debate creativity through a hierarchical eight-dimensional metric system, implemented via a pre-trained autoregressive language model with a hierarchical scoring head that supports both fine-grained and coarse-grained evaluation. Statements and their associated expert scores were obtained from authentic debate competitions, and a constrained data augmentation strategy was employed to address the elite bias inherent in the original data. DEFINED adopts a mixed-granularity training strategy enabling robust learning from limited fine-grained supervision annotated by trained graduate experts. To rigorously validate ecological validity beyond synthetic benchmarks, we incorporate an empirical study with debate-naive participants, utilizing these authentic data to serve as a qualitative case study for mid-to-low proficiency populations. Across our evaluation protocol, our scoring model achieves accurate and stable scoring, outperforming prompt-based large language model evaluators and existing debate scoring methods.

---


### 148. [Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking](https://arxiv.org/abs/2606.07233)

**<font color=#1a73e8>作者：</font>** Eduardo Borges, Luís Garrote, Urbano J. Nunes  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D Multi-Object Tracking (MOT) typically relies solely on geometric information, which is often insufficient to distinguish between targets during prolonged occlusions or in crowded human-populated environments. While integrating RGB-based Re-Identification (ReID) offers a theoretical solution for preserving identity context, existing approaches often rely on computationally expensive parallel detectors that hinder real-time robot responsiveness. This work presents a systematic study of image-based ReID in online 3D MOT, utilizing a lightweight projection-based framework to decouple geometric and appearance modeling for mobile robots. A comprehensive analysis of feature extraction architectures is conducted, employing lightweight CNNs and Vision Transformers, and evaluating various multi-modal data association strategies to balance computational latency with robust tracking. Experiments on the Pedestrian class of the KITTI dataset reveal that naive linear fusion, of appearance and motion costs, degrades performance due to visual noise. Conversely, a cascaded matching strategy successfully recovers occluded tracks without compromising overall precision, effectively preventing identity switches to maintain human-robot interaction continuity. We show that lightweight architectures can offer an optimal trade-off between the low latency required for safe navigation and the discriminative power needed for social awareness.

---


### 149. [Generative Molecular Morphing for Flexible-Size Design via Unbalanced Optimal Transport](https://arxiv.org/abs/2606.07239)

**<font color=#1a73e8>作者：</font>** Malte Franke, Stefan P. Schmid, Zarko Ivkovic 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The success of generative molecular design hinges on a model's steerability toward high-reward samples. Because many molecular properties are intrinsically linked to molecular size, accurately capturing the joint distribution of properties and the number of atoms is essential. However, current diffusion and flow-based models fix the number of atoms, which ultimately limits their ability to navigate this complex relationship. To address this, we introduce Morph, a flexible-size generative model for conditional and unconditional 3D molecular design based on geometric graphs. By dynamically adapting size, Morph can seamlessly integrate existing structural priors, like scaffolds, and significantly enhances property steering. We show that Morph matches current fixed-size state-of-the-art models while offering the benefit of unparalleled sampling flexibility. We demonstrate out-of-distribution generation in regimes where previous models fail, paving the way for enhanced generative modeling for molecular design.

---


### 150. [KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026](https://arxiv.org/abs/2606.07240)

**<font color=#1a73e8>作者：</font>** Seymanur Akti, Alexander Waibel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cross-lingual voice cloning aims to generate speech in a target language while preserving speaker identity from a source-language reference. This task is central to speech translation and is the focus of the IWSLT 2026 Cross-Lingual Voice Cloning track. A key challenge is maintaining intelligibility and naturalness in the presence of accent variation and domain-specific vocabulary. We build on a multilingual text-to-speech model, FishAudio-S2-Pro, and introduce language tag prompting to improve language control and reduce accent leakage. We further apply reinforcement learning (RL) fine-tuning for task adaptation and observe improvements in intelligibility. Finally, we propose a reference-conditioned lexical matching method that improves pronunciation of domain-specific terms when lexical overlap is present. Results show that language prompting provides the largest gains, while lexical matching yields consistent improvements on matched subsets.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
