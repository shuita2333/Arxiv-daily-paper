# 📦 其他研究 | 2026年07月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

---

### 201. [Toward a Unified Security and Privacy Framework for AI-Native 6G Networks](https://arxiv.org/abs/2607.01019)

**<font color=#1a73e8>作者：</font>** Bidushi Barua, Ahsan Khan, Kangfeng Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sixth Generation (6G) communication networks are expected to evolve into AI-native, highly autonomous ecosystems that integrate communication, computing, sensing, and artificial intelligence. While these capabilities enable unprecedented connectivity and intelligent services, they also create a highly heterogeneous security and privacy landscape that cannot be addressed through isolated, technology-specific solutions. This paper presents a comprehensive survey of security and privacy in AI-native 6G networks from a cross-layer perspective. We first examine the fragmentation of existing security and privacy approaches across emerging technologies, network architectures, AI systems, and standardization efforts, motivating the need for a unified security and privacy framework. Building upon this framework, we develop a cross-layer threat taxonomy encompassing infrastructure, network and architectural, AI, privacy, and security management domains, and analyze representative threats across key AI-native 6G technologies. Furthermore, we map these threats to corresponding cross-layer countermeasures, including standards harmonization as a security function, and identify critical research gaps and future priorities for secure, interoperable, and trustworthy AI-native 6G ecosystems. Finally, we discuss future research directions toward realizing secure, privacy-preserving, resilient, and globally interoperable 6G networks. This survey provides researchers, practitioners, and standardization communities with a holistic foundation for the design, evaluation, and deployment of trustworthy AI-native 6G systems.

---


### 202. [PedNStream: Scalable Network Flow Simulation for Pedestrian Traffic Management](https://arxiv.org/abs/2607.01021)

**<font color=#1a73e8>作者：</font>** Weiming Mai, Dorine Duives, Serge Hoogendoorn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale crowd management requires pedestrian simulations that are both computationally efficient and compatible with feedback-based control. However, most open-source tools are either microscopic or not designed for network-scale closed-loop evaluation. This paper presents PedNStream (Pedestrian Network Flow Simulation), an open-source, Python-native simulator for macroscopic pedestrian network loading based on the Link Transmission Model (LTM). The framework extends LTM-based pedestrian models by incorporating stochastic link dynamics that capture diffusion and activity-induced variability, and replaces dynamic user equilibrium route choice with a utility-based formulation suited to uncertain, intervention-driven settings. PedNStream is implemented as a modular framework with built-in controller interfaces for interventions such as gating, flow separation, and route guidance. We evaluate the framework in a staged manner. Synthetic scenarios verify key mechanisms, including queue formation, spillback, congestion dissipation, and adaptive rerouting. Real-network experiments assess large-scale behavior and consistency with observed pedestrian counts. A closed-loop case study demonstrates controller integration, and a runtime analysis quantifies scalability. These results establish PedNStream as an efficient and practical testbed for large-scale pedestrian network simulation and control.

---


### 203. [Seahorse: A Unified Benchmarking Framework for Spatiotemporal Event Modeling](https://arxiv.org/abs/2607.01022)

**<font color=#1a73e8>作者：</font>** Yahya Aalaila, Gerrit Großmann, Sebastian Vollmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal point processes (STPPs) model event data in continuous time and space, with applications in mobility, epidemiology, and public safety. Recent neural STPPs span expressive intensity models, conditional density models, continuous-time latent dynamics, normalizing-flow spatial decoders, and score-based generative mechanisms. Yet comparison remains fragile because implementations differ in preprocessing, coordinate normalization, splits, likelihood conventions, and evaluation protocols. We present SEAHORSE, a unified framework for reproducible STPP experimentation. SEAHORSE formalizes neural STPPs through a common encode-evolve-decode interface and trains, tunes, and evaluates every model family under a single executable benchmark protocol with raw-coordinate likelihood reporting. This enables fair comparisons but, more importantly, controlled diagnostic studies. We pair SEAHORSE with HawkesNest, a synthetic stress-test suite, and show that increasing event-pattern complexity exposes each family's inductive bias, degrading some models sharply and leaving others stable. Code: this https URL.

---


### 204. [Evidence-Supported Credit Risk Report Generation Using News-Centric Financial Knowledge Graphs](https://arxiv.org/abs/2607.01023)

**<font color=#1a73e8>作者：</font>** Rocio Jimenez-Villen, Ziwei Xu, Ying Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial markets evolve in response to real-world events reported in news, yet these drivers often remain implicit in text. To better explain market dynamics, event-market relations must be explicitly modeled through factual, company-centric, and environment-aware knowledge graphs. We present FinKG-News, a framework that automatically constructs such graphs by extracting news events as anchors linked to companies. Using FinKG-News as grounded evidence that integrates events, news, and company data, we develop an in-context learning architecture for credit risk report generation across three core financial dimensions. Automatic and human evaluations show that automated hallucination detection and quality assessment remain unreliable, making expert judgment indispensable. Our approach consistently outperforms baselines, improving quality by 19%-34% while reducing hallucinations. The source code and project resources are publicly available at: this https URL.

---


### 205. [EchoRisk: A Multicentre Echocardiography Dataset and Benchmark for Cardio-Oncology](https://arxiv.org/abs/2607.01039)

**<font color=#1a73e8>作者：</font>** Grigorios Kalliatakis, Georgia Karanasiou, Georgios Manikis 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Therapy-induced cardiotoxicity is the leading non-oncological cause of treatment interruption in breast cancer patients, yet early, automated risk stratification from routine cardiac imaging remains an unsolved problem. We present EchoRisk, the first curated, multicentre, longitudinal echocardiography dataset with explicit cardiotoxicity labels, released as the primary technical reference for the EchoRisk-MICCAI 2026 challenge. The dataset comprises 422 patients enrolled in the EU-funded CARDIOCARE prospective study across five European sites, yielding 2,159 echocardiography videos across 1,123 clinical exams acquired at up to five longitudinal timepoints, alongside a dedicated cohort of 280 patients with baseline imaging for early cardiotoxicity prediction. Three clinically grounded tasks are defined: automated estimation of left ventricular ejection fraction from cine video (Task 1), classification of LV dysfunction from longitudinal imaging (Task 2), and early prediction of therapy-induced cardiotoxicity from pre-therapy baseline echocardiography alone (Task 3). For each task we specify the evaluation protocol, primary and secondary metrics, and ranking procedure. We establish baseline performance using an R(2+1)D video backbone with LSTM aggregation trained from Kinetics-400 pretrained weights, demonstrating strong discriminative performance for cardiac functional assessment and LV dysfunction classification, while early cardiotoxicity prediction from a single pre-therapy video remains a significant open problem for the community. The dataset, evaluation code, and baseline implementations are publicly available to serve as a benchmark for further collaboration, comparison, and the creation of task-specific architectures in cardio-oncology.

---


### 206. [Balancing Expressivity and Learnability in Quantum Kernel Bandit Optimization](https://arxiv.org/abs/2607.01080)

**<font color=#1a73e8>作者：</font>** Yuqi Huang, Vincent Y. F. Tan, Sharu Theresa Jose  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate Gaussian process (GP) bandit optimization with quantum kernels, assuming the mean reward function lies in the reproducing kernel Hilbert space (RKHS) induced by the quantum kernel. This setting is motivated by NISQ-era tasks such as quantum control, state preparation and variational quantum algorithms. While quantum kernels can offer a `quantum advantage' via domain-specific inductive biases, naïvely using full, high-dimensional kernels increases model complexity and information gain, leading to higher cumulative regret and poor learnability. To address this, we propose projected quantum kernels and classical kernel approximation techniques that reduce feature dimensionality while preserving key quantum properties. Using these approximate kernels, we develop misspecified GP bandit algorithms and derive regret bounds that characterize the trade-off between approximation error and information gain. The regret bounds provide principled guidance for selecting the optimal model complexity. Empirically, our methods outperform full quantum kernels in sample efficiency, while substantially reducing computational overhead, enabling scalable GP optimization for quantum-native applications.

---


### 207. [When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal Point-Process Forecasting](https://arxiv.org/abs/2607.01082)

**<font color=#1a73e8>作者：</font>** Yahya Aalaila, Mouad Elhamdi, Gerrit Großmann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal point-process models must often generalise across space when local event histories are sparse. We study whether exogenous spatial context can compensate in such regimes. Using a fixed log-Gaussian Cox process backbone, we compare an event-only model with the same model augmented by AlphaEarth embeddings as linear spatial context. We evaluate spatial transfer on emergency medical services (EMS) forecasting across eight held-out regions, fixed forecast anchors, and a sweep over history length $w$, using only AlphaEarth (AE) embeddings available strictly before each anchor. AE improves out-of-region predictive performance across all history regimes, with the largest gains under scarce histories: approximately $2$--$6\times$ multiplicative improvements at $1-2$ weeks, tapering to roughly $10$--$20\%$ at $w=20$--$104$ weeks. These results show that contextual information can substantially stabilise spatially transferred point-process forecasts when event history is limited.

---


### 208. [CPDDNet: Color-Polarization Denoising and Demosaicking Network](https://arxiv.org/abs/2607.01100)

**<font color=#1a73e8>作者：</font>** Qihang Zhang, Yusuke Monno, Masayuki Tanaka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color-polarization imaging using a color-polarization filter array (CPFA) sensor captures both texture (color intensity) and physical (polarization) information of the scene in a single shot, enabling various applications in computer vision. However, the raw mosaic output from a CPFA sensor often suffers from severe noise and resolution loss, especially under low-light conditions. Existing methods generally focus on either denoising or demosaicking tasks, failing to capture the coupling between them and neglecting shared low-level features. In this paper, we propose a color-polarization denoising and demosaicking network (CPDDNet), which is a joint framework that performs noise removal and CPFA interpolation using a feature fusion module that retains the features from the CPFA raw data at both the denoising and the demosaicking stages. Experimental results demonstrate that CPDDNet significantly enhances image quality and polarization parameter accuracy, outperforming existing approaches on a real dataset.

---


### 209. [SynLaD: Latent Diffusion for Generating Synthesizable Molecules Conditioned on 3D Pharmacophore Profiles](https://arxiv.org/abs/2607.01105)

**<font color=#1a73e8>作者：</font>** Miruna Cretu, John Bradshaw, Patricia Suriana 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present SynLaD, a latent diffusion framework for small-molecule generation that unifies ligand-based drug design objectives (what to make) with synthetic accessibility (how to make it). Current models typically optimize one objective at the expense of the other, creating a bottleneck for discovering high-scoring and synthesizable molecules. SynLaD combines reaction-constrained generation with pharmacophore-conditioned 3D design by learning a latent space that decodes to both 3D structures and synthesis pathways. An encoder maps molecules to a latent representation used by two decoder heads: (i) a geometric head that reconstructs atom types and coordinates and (ii) an autoregressive synthesis head that outputs synthetic routes in a serialized, reaction-based notation. A diffusion transformer generates novel latents in the learned space, conditioned on pharmacophore profiles. Across analogue generation tasks for bioactive ligands, SynLaD outperforms existing baselines in synthesizable and diverse hit generation, demonstrating that a single model can produce shape-aligned molecules with feasible synthesis plans.

---


### 210. [Muon as a Residual Connection](https://arxiv.org/abs/2607.01124)

**<font color=#1a73e8>作者：</font>** Hao Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as one of the most effective optimizers for training large neural networks, yet its empirical success has been explained from several different perspectives. In this paper, we propose a simple mechanistic interpretation: Muon can be understood as an implicit residual connection during training. Specifically, orthogonalizing the update can sacrifice some immediate gradient fidelity while improving representation preservation for downstream layers. We study this trade-off in controlled linear optimization settings, where Muon can learn representations that are slower to fit a local target but easier for downstream layers to exploit. Our results suggest a conceptual explanation for Muon and a design perspective for optimizers that balance local descent with downstream usability.

---


### 211. [GAIA: Geometry-Adaptive Operator Learning for Forward and Inverse Problems](https://arxiv.org/abs/2607.01128)

**<font color=#1a73e8>作者：</font>** Meenakshi Krishnan, Pranav Pulijala, Ke Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Operator learning for partial differential equations (PDEs) on arbitrary geometries builds fast neural surrogates for large-scale simulation. Although recent geometry-adaptive neural operators have made substantial progress, they are mainly designed for forward problems in which inputs and outputs share the same spatial domain. This limits their applicability for boundary value problems (BVPs) and inverse problems, where inputs and outputs may live on different domains. We introduce the Geometry-Adaptive Integral Autoencoder (GAIA), an operator learning model that encodes the domain boundary and the interior field distribution into geometry tokens, and conditions integral transform layers on these tokens via cross-attention, allowing the kernel to adapt locally to geometric features. This yields a single architecture for forward (including BVPs) and inverse problems on arbitrary domains in one pass, without retraining, iterative optimization, or graph construction. We evaluate GAIA on seven 2D and 3D benchmarks, four of which are new or substantially extended benchmarks for inverse problems and BVP: electrical impedance tomography, optical tomography, 3D Darcy flow on varying geometries, and a modified setting of Poisson BVP on mechanical components benchmark (MCB). GAIA sets new state-of-the-art results on every inverse and BVP task, reducing median relative $L^2$ error by 64% on airfoil flow reconstruction and 27% on EIT relative to the next best amortized method, and outperforming all baselines on every shape category of MCB. On other forward problems, GAIA is competitive with specialized solvers while maintaining stable accuracy across point resolutions on which transformer-based baselines degrade.

---


### 212. [Towards Metric-Agnostic Trajectory Forecasting](https://arxiv.org/abs/2607.01133)

**<font color=#1a73e8>作者：</font>** Markus Knoche, Daan de Geus, Bastian Leibe  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate trajectory forecasting of surrounding traffic participants is a core capability for autonomous driving, enabling vehicles to anticipate behavior and plan safe maneuvers. We observe that current state-of-the-art forecasting models on Argoverse 2 and the Waymo Open Motion Dataset tailor their training objectives to the different benchmark metrics. Because these metrics encourage conflicting behavior, we propose a paradigm change for trajectory forecasting: training models with metric-agnostic probabilistic objectives and treating metric optimization as a downstream task applied to the predictive distribution. Concretely, we introduce Trajectory Distribution Evaluation (TraDiE) policies, metric-specific policies that map a predictive distribution to the set of $K$ trajectories and confidences required by trajectory forecasting metrics. We evaluate this framework by introducing DONUT-NLL, which adapts the training objective of the state-of-the-art trajectory forecasting model DONUT to directly optimize the predictive distribution. Using our policies, DONUT-NLL achieves state-of-the-art results on all metrics of the Waymo motion prediction benchmark.

---


### 213. [SD-RouteFusion: Ego-Trajectory Prediction with SD-Map Route Conditioning](https://arxiv.org/abs/2607.01139)

**<font color=#1a73e8>作者：</font>** Sviatoslav Voloshyn, Bruno K. W. Martens, Wangxin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents SD-RouteFusion, a deployable end-to-end ego-trajectory prediction method that fuses a front-facing camera, vehicle kinematics, and a navigation route derived from a Standard Definition (SD) map. Unlike approaches that rely on High Definition (HD) map geometry, SD-RouteFusion aligns the learning objective with scalable and production-ready SD-map route inputs, enabling route-aware prediction without requiring HD-map infrastructure. First, we demonstrate that SD-map route prior provides a powerful long-horizon semantic prior. Through a comprehensive study on a large-scale real-world dataset comprising 480k driving scenarios across 10 European countries and the U.S., we quantify the value of SD-route conditioning: incorporating SD-map routes yields a 10.5% ADE improvement over an image-and-kinematics baseline, while our full fusion strategy achieves a 16.9% ADE reduction given a prediction horizon of 8 seconds. The fusion strategy consists of a dual-hypothesis design paired with a gated classifier, to ensure robustness under route corruption and visual uncertainty. Finally, to support broader evaluation, we release an SD-route generation toolkit that enables SD-route-conditioned ego-trajectory prediction on all datasets containing ego pose and future trajectories. Together, SD-RouteFusion establishes a practical path toward robust, route-aware ego-trajectory prediction at scale.

---


### 214. [Relation-Centric Open-Vocabulary 3D Gaussian Segmentation](https://arxiv.org/abs/2607.01140)

**<font color=#1a73e8>作者：</font>** Eunsung Cha, Hyunjoon Lee, Jaesik Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary 3D Gaussian segmentation is challenging because it requires language understanding for diverse queries and accurate separation of Gaussians along object boundaries. Prior approaches either embed language knowledge into individual Gaussians to improve query responsiveness or optimize per-Gaussian instance features to encode object identity. However, these strategies may produce noisy Gaussian segmentations or rely on cost-inefficient per-scene optimization. We propose PairGS, a framework that reframes Gaussian segmentation as modeling pairwise relations between Gaussians. 3D Gaussian representations provide rich signals for relation estimation, such as view contribution weights and multi-view mask evidence. By leveraging these cues, PairGS explicitly constructs a relation graph for segmentation without a heavy optimization process. PairGS first proposes sparse edge candidates using low-dimensional descriptors, computes precise pairwise affinities only on those candidates, and builds a hierarchical cluster tree for multi-granular querying. It achieves state-of-the-art results on open-vocabulary 3D Gaussian segmentation benchmarks, while the fast variant is 50x faster than optimization-based instance-feature approaches.

---


### 215. [Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven Search](https://arxiv.org/abs/2607.01144)

**<font color=#1a73e8>作者：</font>** Binglin Ji, Anindya Sarkar, Hengchang Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While generative models have enabled training-free reward alignment, current methods typically excel in local exploration within narrow regions of the underlying distribution. These approaches struggle when preferences are unknown a priori and only revealed through sequential feedback-a scenario demanding broad exploration to uncover high-utility regions. To address this, we propose Sequentially-Controlled Interactive Multi-Particle Flow-Maps (IMPFM), a framework for sample-efficient online feedback-driven search. IMPFM progressively transports a group of interactive particles toward the target distribution, maintaining the broad coverage essential for heterogeneous preference alignment. IMPFM introduces a principled and efficient posterior sample sharing mechanism across particles powered by flow maps. By correcting individual particle drift with the collective posterior samples of the entire ensemble at each resampling step, the framework maximizes sample utility to enable global exploration while actively mitigating reward over-optimization, typical of standard control frameworks. Paired with a principled exploration-exploitation reweighting mechanism involving multi-particle interaction, this sequentially corrected multi-particle dynamics explicitly preserves structural diversity and overcomes the weight degeneracy inherent to standard SMC samplers. Crucially, we prove that the resulting sampling framework yields a multi-particle interaction-aware Feynman-Kac corrector that progressively steers the multi-particle system toward a KL-tilted target distribution, facilitating global exploration and preventing mode collapse. Extensive empirical evaluations and rigorous ablations across diverse search and alignment tasks confirm the efficacy of IMPFM over existing baselines.

---


### 216. [A Lightweight Self-Supervised Learning Framework for Multivariate Time Series using Hierarchical-JEPA on ECG Data](https://arxiv.org/abs/2607.01145)

**<font color=#1a73e8>作者：</font>** Siwon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data analysis in the medical domain often encounters scenarios involving a limited target dataset and a large, unannotated dataset with a general distribution. Under such circumstances, self-supervised learning (SSL) methods are highly effective for utilizing large datasets, making them a popular choice for electrocardiogram (ECG) analysis. This work presents the Event Reconstruction Joint-Embedding Predictive Architecture (ER-JEPA), a lightweight SSL framework for multivariate time series, whose name and two-fold hierarchical structure are inspired by the diagnostic approach of cardiologists. At its core, ER-JEPA features: (1) a two-stage structure that constructs representations for each time interval and subsequently processes these representations as a univariate time series, (2) the hierarchical integration of two Joint-Embedding Predictive Architectures (JEPAs), and (3) a Vision Transformer (ViT) backbone. The structural concatenation of two JEPAs categorizes the model as a Hierarchical JEPA (H-JEPA), designed to encode multiple levels of abstract representations for enhanced prediction on complex tasks. This study reports a successful application of H-JEPA to 12-lead ECG data as a multivariate time series alongside an analysis of the sensitivity of hierarchical representation during the pretraining stage. Pretrained on approximately 180,000 10-second recordings, the model achieves state-of-the-art downstream performance on the ST-MEM benchmark, with rapid computation and minimal resource usage.

---


### 217. [EquiSteer: Cross-Attention Steering Towards a Fairer Text-Guided Image Generation](https://arxiv.org/abs/2607.01147)

**<font color=#1a73e8>作者：</font>** Tatiana Gaintseva, Akshit Achara, Gregory Slabaugh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models power everyday creative tasks, but they still reproduce the demographic biases in their training data. On common prompts such as ``a photo of a nurse,'' ``a photo of a CEO'', they skew their outputs toward one gender, driven by the statistics of training data rather than anything in the text. Existing debiasing methods show promise in narrow settings but require retraining, batch-level control, or prompt-specific tuning, limiting their scalability. We propose \emph{EquiSteer}, a training-free method that works per sample by steering cross-attention (CA) activations at inference time. For each target attribute, EquiSteer precomputes steering vectors from contrastive prompts. Then at generation time, a prompt-aware gate leaves attribute-specific prompts untouched, while for neutral ones it clears existing attribute signals from the CA activations and injects a target attribute. Across SD-1.5, SD-2.1, SDXL, and SANA, EquiSteer reduces the average parity gap by up to $87\%$, with minimal effect on image quality and text-image alignment. Code is available at \href{this https URL}{this https URL}.%

---


### 218. [AGC-Bench: Measuring Artificial General Creativity](https://arxiv.org/abs/2607.01152)

**<font color=#1a73e8>作者：</font>** Roger Beaty, Vijeta Deshpande, Clin K.Y. Lai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to LLMs, but a unified benchmark of AI creativity remains elusive. We introduce AGC-Bench, an artificial general creativity benchmark built from a systematic review of the AI creativity literature (3,101 papers screened, 497 benchmarks identified), paired with an agentic harness that converts idiosyncratic codebases into HELM-standardized benchmarks. The first release covers 78 datasets spanning brainstorming, problem solving, STEM, narrative, figurative language, and humor. To address bias in LLM-as-judge, we apply Judge Response Theory -- a psychometric calibration of judge leniency/severity; we then fine-tune Qwen3-30B on the bias-corrected ratings of three frontier LLMs to produce AGC-Judge, an open-weight model that robustly scores new creativity benchmarks it was not trained on. Results reveal frontier models at the top of the AGC-Bench leaderboard, with open models close behind. LLMs show different creative strengths, ranking higher on some domains (e.g., writing) than others (e.g., scientific ideation). Extensive experiments yield three main findings. First, applying factor analysis across 83 LLMs, we recover a single creativity factor 'c', analogous to the 'g' factor of general intelligence, that explains 81.5% of variance, related to but separable from general knowledge/reasoning. Second, we show that prompting models to "be creative" boosts their performance far more than enabling reasoning, evidence that the benchmark tracks creativity over general ability. Third, on a human-matched subset, we find the top human still leads the top LLM on creativity. We release AGC-Bench with a public leaderboard, AGC-Judge, and human data as open infrastructure for measuring AI creativity at scale.

---


### 219. [Efficient Compression of Structured and Unstructured Volumes via Learned 3D Gaussian Representation](https://arxiv.org/abs/2607.01164)

**<font color=#1a73e8>作者：</font>** Landon Dyken, Sharmistha Chakrabarti, Nathan Debardeleben 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that implicit neural representations (INRs) can be trained to effectively compress structured and unstructured volume data, allowing for direct data querying with a reduced memory footprint. However, as existing INRs for unstructured volumes do not encode geometry, they require partial mesh storage for later sampling, limiting achievable compression. At the same time, novel view synthesis methods have shown that explicit collections of 3D Gaussians can be used to accurately visualize volume data. In this work, we introduce an explicit model for volume data compression based on 3D Gaussian primitives. We reinterpret collections of 3D Gaussians as an explicit representation of a scalar field and use a sampling strategy that reconstructs scalar values at spatial locations through weighted aggregation of intersecting Gaussians. We develop optimized CUDA-accelerated pipelines for structured and unstructured model sampling, loss functions that encourage accurate domain encoding by our models, and a novel sampling-error based densification strategy. Our explicit formulation naturally encodes domain geometry, eliminating the need for mesh storage in unstructured volumes and introducing significantly higher compression opportunities. Compared to existing INRs, we demonstrate that our explicit model achieves competitive reconstruction quality with significant training speedups on structured volumes, while markedly outperforming in all metrics on unstructured volumes.

---


### 220. [Decision-Aware Training for Sample-Based Generative Models](https://arxiv.org/abs/2607.01171)

**<font color=#1a73e8>作者：</font>** Kornelius Raeth, Nicole Ludwig  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sample-based generative models are increasingly used for probabilistic forecasting in high-stakes decision settings, yet their training objectives are blind to the decision maker's cost structure. These models are commonly trained with strictly proper scoring rules, such as the energy score, which allocate their training signal in proportion to data density, with no awareness of where forecast errors are most costly for downstream decisions. We therefore propose decision-aware training for sample-based generative models, augmenting the energy score objective with a differentiable decision loss that directly penalises the cost incurred by acting on the model's forecast. This combined loss is theoretically grounded, as the decision loss is itself a proper scoring rule. We validate our method on one synthetic and two real-world tasks, showing targeted improvements in cost-sensitive regions while retaining full probabilistic forecasts.

---


### 221. [High-dimensional Embedding Prior for Noisy K-space Domain MRIReconstruction](https://arxiv.org/abs/2607.01176)

**<font color=#1a73e8>作者：</font>** Yu Guan, Tianjia Huang, Qinrong Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging (MRI) reconstruction under realistic acquisition conditions can be fundamentally viewed as estimating the underlying k-space distribution from incomplete and noise-corrupted measurements. While diffusion models have recently shown strong potential as generative prior for inverse problems,existingapproachesstruggletohandlenoisyreconstruction settings, especially when operating directly in k-space domain. In this work, we propose a unified high-dimensional k-space reconstruction framework tailored for noisy inverse problems, whichenhancesdiffusion-based solversthroughrepresentation this http URL underlying optimization procedures, the proposed framework augments the data representation space, enabling existing diffusion-based solvers to operate on enriched k-space embeddings with improved expressiveness. Extensive experiments on both in-house and public datasets across varying noise levels and undersampled factors demonstrate that the proposed frame work consistently improves reconstruction quality for multiple diffusion-based inverse solvers. Notably, the largest gains are observed in high-noise regimes, which is consistent with our theoretical analysis of error propagation under high-dimensional representation. These results suggest that high-dimensional representation provides a general and model-agnostic mechanism for improving diffusion-based MRI reconstruction in noisy settings, offering a new perspective on robust k-space generative modeling for practical inverse problems. The code will be available at this https URL.

---


### 222. [QuasiMoTTo: Quasi-Monte Carlo Test-Time Scaling](https://arxiv.org/abs/2607.01179)

**<font color=#1a73e8>作者：</font>** Michael Y. Li, Anthony Zhan, Kanishk Gandhi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling inference compute, by generating many parallel attempts per problem, is a costly but reliable lever for improving language model capabilities. By default these attempts are generated independently, wasting inference compute on redundant solutions. This waste seems unavoidable. After all, independence is what makes parallel sampling trivial to scale. However, this tradeoff is not fundamental: there is a rich design space of samplers that generate correlated but exact samples entirely in parallel. We explore this design space as an avenue for improving sample efficiency in scaling inference compute and reinforcement learning (RL). Concretely, we introduce QuasiMoTTo, which uses correlated samples as a drop-in replacement for i.i.d. samples. To generate these samples, QuasiMoTTo uses a reparameterization of autoregressive sampling as inverse-CDF sampling and draws the underlying uniforms with quasi-Monte Carlo (QMC); because QMC spreads the uniforms out more evenly than i.i.d., the resulting samples cover the output space with far less redundancy. Even though the batch is correlated, each sample is marginally distributed according to the language model, so we can use the batch for policy-gradient training. Our empirical analysis focuses on understanding how efficiently QuasiMoTTo can turn compute into performance. To evaluate correlated samplers, whose dependence breaks standard pass@k estimators, we first develop an unbiased bootstrap estimator. Across four reasoning benchmarks, QuasiMoTTo matches i.i.d. pass@k accuracy with 25-47% fewer samples. Strikingly, QuasiMoTTo often saturates an upper bound on pass@k that holds for any marginal-preserving sampler. We also apply QuasiMoTTo to policy-gradient RL (GRPO) where it matches i.i.d. performance with 50% fewer training steps. These gains come from higher coverage, which yields a stronger learning signal per batch.

---


### 223. [Right in the Right Way: LM Training with Verifiable Rewards and Human Demonstrations](https://arxiv.org/abs/2607.01181)

**<font color=#1a73e8>作者：</font>** Mehul Damani, Isha Puri, Idan Shenfeld 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL with verifiable rewards (RLVR) has emerged as a powerful paradigm for training LMs on tasks with well-defined success metrics, such as code generation and mathematical reasoning. However, current RLVR methods optimize only what can be objectively scored, often neglecting subjective, non-verifiable aspects of human-like outputs, such as style and structure. This limitation leads to well-documented failure modes such as diversity collapse, unnatural-sounding responses, and reward hacking. We propose an adversarial generator-discriminator framework that augments verifiable rewards with a learned signal from human demonstrations. A generator model is trained using RL to maximize both task accuracy and an adversarial reward derived from a discriminator. The discriminator, trained alongside the generator policy, learns to distinguish human-written outputs from model-generated ones. The discriminator serves as a learned proxy for the human output distribution, providing feedback on aspects of generation that are difficult to formalize as scalar rewards. Across diverse domains, including bug fixing and open-ended generation, our approach consistently improves non-verifiable properties while preserving the accuracy gains of RLVR. In bug fixing, our method produces solutions with significantly lower edit distance compared to RLVR baselines while matching end performance. In story generation, our method significantly improves win rate while producing stories that are diverse and more human-like. And in a simple reward hacking benchmark, our method nearly eliminates model misbehavior while maintaining high benchmark scores. Together, these results show that our approach bridges RL and SFT, offering a scalable path toward jointly optimizing the verifiable and non-verifiable properties of a task.

---


### 224. [Neural Certificate Pricing for Combinatorial Optimization Problems](https://arxiv.org/abs/2607.01185)

**<font color=#1a73e8>作者：</font>** Jingyi Chen, Xinyuan Zhang, Xinwu Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Combinatorial optimization (CO) problems are difficult because certifiable discrete structure induces exponential search. One needs to search over the set exponentially many candidates to certify optimality, however, the structural feasibility of a path, packing, or cover can be verified in polynomial time once supplied. In this study, we introduce Neural Certificate Pricing (NCP) that exploits this asymmetry under an unsupervised learning framework. A neural network is trained to predict certificate-level dual prices, while a structured recovery layer constructs the induced primal marginal. NCP can be viewed as amortized separation: instead of enumerating violated inequalities, it learns the residual prices through which their aggregate effect enters recovery. When the certificate-consistency condition holds, the recovered marginal is globally feasible, and a local theory shows that first-order errors in the predicted price induce only second-order loss in objective value. Across three classes of CO problems, NCP either outperforms state-of-the-art neural baselines by large margins or matches them at a fraction of the computation time, and shows stronger out-of-distribution generalization.

---


### 225. [Optimal Resource Utilization for Autonomous Laboratory Orchestrators](https://arxiv.org/abs/2607.01188)

**<font color=#1a73e8>作者：</font>** Austin McDannald, Julia Tisaranni, Howie Joress  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In autonomous laboratories, AI agents suggest the next batch of experiments to do. However, planning and executing those tasks taking full advantage of the available resources is a completely different question. This can be challenging when dealing with real-world hardware constraints, especially so when there are multiple instruments with different capacities and throughputs. Here we demonstrate a 2-step method to address resource utilization for our autonomous platform for metal-organic framework synthesis. First, we use constraint programming to find optimal schedules. This finds schedules that minimizes the total time while still satisfying the limitations and capacities of the hardware. Secondly, we use a system of status dependencies for each task, which allows for the robust execution of the optimal schedules.

---


### 226. [Detecting Adversarial Evasion Attacks Against Autoencoder-Based Network Intrusion Detection Systems](https://arxiv.org/abs/2607.01194)

**<font color=#1a73e8>作者：</font>** Niklas Bunzel, Ashim Siwakoti  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Evasion attacks deliberately manipulate input to an ML-based system to produce an incorrect prediction while the manipulated input still appears benign. The PANDA framework has demonstrated that adversarial examples developed for the vision domain can be transferred to the network domain by converting packet sequences into invertible grayscale images, enabling gradient-based attacks such as masked FGSM against autoencoder-based network intrusion detection systems (NIDS). These attacks manipulate the NIDS anomaly score without altering the underlying attack semantics, leaving defenders without a straightforward way to distinguish between benign flows and carefully perturbed malicious traffic. In this paper, we propose two complementary detectors: the Residual Localisation Detector (RLD), which tracks the spatial concentration of reconstruction errors in the inter-arrival time feature region in image space; and the Feature-Space Perturbation Consistency (FPC) Detector, which operates directly on packet-level inter-arrival time features in packet-feature space. We evaluate both detectors on benign, malicious, and adversarial traffic from multiple IoT devices in the UQ-IoT dataset. Both detectors achieve near-perfect detection performance (TNR, TPR, precision, recall, and F1-score $\geq 0.99$) against adversarial examples across the evaluated IoT traffic. Our results indicate that integrating reconstruction-based scoring with perturbation consistency checks, in both image space and packet-feature space, offers a practical defence against emerging PANDA-style adversarial attacks on NIDS.

---


### 227. [Quantum vs. Classical Machine Learning: A Unified Empirical Comparison](https://arxiv.org/abs/2607.01197)

**<font color=#1a73e8>作者：</font>** Chuanming Yu, Jiaming Liu, Zihao Ge 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum computing has emerged as a promising computational paradigm for machine learning (ML), with the potential to offer computational advantages over classical approaches. At this stage, the evidence supporting the performance and advantages of quantum machine learning (QML) models relative to classical models is this http URL address this gap, this paper presents an empirical study on the performance of QML models and their classical counterparts. We compare seven model pairs spanning supervised learning and reinforcement learning. Our results indicate that the evaluated quantum machine learning models do not yet surpass the classical baselines in overall prediction performance, policy stability, or training time. Nevertheless, QML remains a promising approach for filtering noise and controlling false positives. Our research findings summarize the challenges facing quantum machine learning across hardware environments, training efficiency, and convergence stability, providing a foundation for research into the robustness and parameter optimization of QML. This work is publicly available at this https URL.

---


### 228. [World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular Video](https://arxiv.org/abs/2607.01202)

**<font color=#1a73e8>作者：</font>** Liyuan Zhu, Shengyu Huang, Amrita Mazumdar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present World from Motion, a method for generating freely renderable dynamic 3D Gaussian representations from monocular videos. Our approach conditions a video model on dense, pixel-aligned renderings that encode appearance, geometry, and 3D scene motion along both input and target camera trajectories to correct rendering artifacts and fill in missing regions from an initial reconstruction. To train this model, we construct a dataset of aligned multiview video pairs and dynamic 3DGS representations, with simulated artifacts characteristic of monocular reconstruction. At test time, we distill the model's generations, including newly observed regions and motions, back into a single consistent, high-quality dynamic 3DGS, improving both novel-view synthesis and the underlying 3D motion. Our method sets a new state of the art in 4D reconstruction and seamlessly generalizes to in-the-wild videos with large viewpoint changes and dynamic motions.

---


### 229. [TiRex-2: Generalizing TiRex to Multivariate Data and Streaming](https://arxiv.org/abs/2607.01204)

**<font color=#1a73e8>作者：</font>** Patrick Podest, Marco Pichler, Elias Bürger 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce TiRex-2, a recurrent xLSTM-based time series foundation model that generalizes the univariate TiRex to multivariate forecasting with both past and future covariates. Real-world forecasting is inherently sequential: observations arrive continuously, variables evolve jointly, and a subset of covariates is known ahead of time. Existing Transformer-based time series foundation models capture cross-variate dependencies but incur quadratic complexity in context length and require full-history recomputation as new observations arrive. TiRex-2 addresses these limitations through a memory-centric recurrent design that operates at constant per-patch cost under streaming. The model combines a bidirectional time mixer with an asymmetric grouped-attention variate mixer, enabling the integration of future-known covariates while preserving strict causality over target variables. To our knowledge, this is the first time series foundation model that achieves this combination of properties. To support scalable multivariate pretraining, we propose a synthetic coupling pipeline that composes diverse multivariate samples on the fly from large univariate corpora. Empirically, TiRex-2 achieves state-of-the-art zero-shot performance on GIFT-Eval and fev-bench, remains stable when streamed to arbitrary context lengths, and maintains constant inference cost per patch. The model uses 38.4M active parameters in univariate mode, with an additional 44.1M parameters activated for multivariate forecasting.

---


### 230. [Linkify: Learning from Interface-Augmented Assembly Graphs](https://arxiv.org/abs/2607.01205)

**<font color=#1a73e8>作者：</font>** Anushrut Jignasu, Daniele Grandi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Linkify, a framework for learning from interface-augmented assembly graphs to enable context-aware part retrieval in mechanical assemblies. While recent generative AI methods for CAD have focused largely on isolated parts or monolithic assemblies, the rich geometric information at the interfaces between parts, where function is realized, remains underexplored. We address this gap by recomputing high-fidelity interface geometry for the Fusion 360 Gallery Assembly dataset, correcting missing and erroneous contacts, and generating point-cloud representations of local contact regions. Using this data, we construct assembly graphs whose nodes encode part geometry and whose edges encode interface geometry via a pretrained point-cloud encoder. On top of this representation, we train a Graph Attention Network based on GATv2 to solve a masked part prediction task: given an assembly with one part held out, the model predicts the class of the missing component from a large vocabulary of geometrically clustered parts, thereby approximating a realistic part-retrieval scenario. Compared to non-graph baselines such as logistic regression and k-nearest neighbors operating on aggregated node features, Linkify achieves higher Top-K accuracy and F1 scores. Ablation studies on graph connectivity, edge attributes, and attention mechanisms demonstrate that accurate contact computation and dynamic attention over interfaces are critical for performance. Our corrected interface dataset and training pipeline, released publicly, provide a foundation for future interface-aware models for assembly retrieval, validation, and generative design.

---


### 231. [All-out Attack: Optimal Block Withholding Under Pay-Per-Share Scheme](https://arxiv.org/abs/2607.01209)

**<font color=#1a73e8>作者：</font>** Mustafa Doger, Sennur Ulukus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Classical Block Withholding (BWH) attacks have been extensively studied in block-dependent reward schemes, where pool members are compensated upon a block discovery within the pool. However, most contemporary mining pools operate under share-based scheme wherein participants are paid immediately upon submission of valid shares. In this paper, we analyze BWH under Pay-Per-Share (PPS) and Full-PPS (FPPS) schemes for Nakamoto-style blockchains and prove that these mechanisms are not incentive compatible -- contrary to claims in prior literature. Under PPS/FPPS, the optimal strategy for a BWH attacker is the All-out Attack (AoA): the adversary allocates its entire hashpower toward the victim pool, submitting only partial Proof-of-Work shares (pPoW) while withholding all valid blocks, i.e., full Proof-of-Work (fPoW).
Under AoA, prior to the first difficulty adjustment, the adversary incurs negligible loss due to the withheld fPoWs. After the first difficulty adjustment, which reduces block difficulty, the adversary generates more pPoWs per unit time, achieving a relative gain of $\frac{\alpha}{1-\alpha}$ compared to pre-adjustment rates, where $\alpha$ is the fraction of adversarial hashpower. Moreover, per unit time and per unit hashpower, all honest miners benefit at the same rate as the adversary. In contrast, the victim pool operator incurs losses: it pays the attacker out-of-pocket for pPoW submissions but receives no fPoW compensation in return. Finally, advanced variants of BWH, such as Fork After Withholding (FAW), do not yield additional profit to the attacker.

---


### 232. [Touching and Feeling the Data: A Reusable Software Pipeline for Tactile Statistical Graphs in Accessible Education](https://arxiv.org/abs/2607.01214)

**<font color=#1a73e8>作者：</font>** Lawrence Obiuwevwi, Krzysztof J. Rechowicz, Jessica M. Johnson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Statistical visualization is usually treated as a visual medium, but data can also be touched. Three dimensional printed tactile graphs let blind and low vision students feel distributions, trace trends, and explore relationships through direct haptic interaction. Yet classroom scale use remains limited because producing each graph in CAD software requires specialized skill and hours of manual work. We address this bottleneck as a software problem through a three layer reusable pipeline in about 1500 lines of JavaScript. The first layer derives tactile design parameters automatically from plate dimensions using tactile perception research. The second provides shared chart scaffolding and five modular builders for scatter, bar, histogram, line, and box plots. The optional third layer uses a multi-modal large language model to extract structured chart specifications from uploaded images, with mandatory teacher review before print generation. The pipeline produces print ready binary Standard Tessellation Language files in under 250 milliseconds. We present the design, performance, and limitations.

---


### 233. [The State-Prediction Separation Hypothesis](https://arxiv.org/abs/2607.01218)

**<font color=#1a73e8>作者：</font>** Giovanni Monea, Nathan Godey, Kianté Brantley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers use the same forward computation stream to both predict the next token and store useful state for future token predictions. We formulate the \emph{state-prediction separation hypothesis}: disentangling the two roles yields better language modeling performance. We design a Transformer variant that uses two computation streams to separate the two functions, and conduct pretraining experiments across various scales. Our experiments show that state-prediction separation consistently offers better data and compute efficiencies, improving validation loss and outperforming standard Transformers by 2--3 percentage points on average on downstream tasks. We also conduct extensive empirical analysis that rules out potential confounders and demonstrates the fundamental difference in the gradients our design entails.

---


### 234. [Ink3D: Sculpting 3D Assets with Extremely Complex Textures via Video Generative Models](https://arxiv.org/abs/2607.01222)

**<font color=#1a73e8>作者：</font>** Yue Han, Chong Li, Zhening Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D generative models can synthesize high-quality geometry but often struggle to reproduce intricate textures from reference images, largely due to the scarcity of large-scale 3D training data with rich surface appearance. In contrast, visual generative models are trained on datasets several orders of magnitude larger and excel at modeling complex visual patterns. Motivated by this gap, we introduce Ink3D, a framework that bridges 3D generation with large-scale video generative models to synthesize extremely complex textures. Ink3D first reconstructs a white-mesh geometry using an off-the-shelf 3D generation model. It then employs OrbitPainter, a conditional video generative model, to produce dense orbit-scan videos capturing object appearance across viewpoints. To convert these views into coherent textures, we introduce TextureOptimizer, a neural baking module that integrates dense multi-view observations while mitigating geometry inconsistencies arising from video generation. By decoupling geometry and texture synthesis and leveraging large-scale pretrained video priors, Ink3D enables significantly richer and more faithful texture generation than prior approaches.

---


### 235. [Theoria: Rewrite-Acceptability Verification over Informal Reasoning States](https://arxiv.org/abs/2607.01223)

**<font color=#1a73e8>作者：</font>** Ben Slivinski, Michael Saldivar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When should an AI system's answer be trusted? Formal proof assistants offer certainty but cannot reach most of the problem distribution; scalar LLM judges offer coverage but produce opaque scores that cannot be audited after the fact and are subject to the same coherence issues as any LLM. We present Theoria, a verification architecture that closes this gap. A candidate solution is rewritten into a sequence of typed state transitions, each licensed by an explicit justification, whether that be a citation, computation, or problem-given fact, and every transition is independently auditable. The foundational invariant is completeness of change: every difference between consecutive proof states must be accounted for, so hidden premises surface as unlicensed mutations rather than passing silently. On HLE-Verified Gold (185 text-only expert problems), Theoria certifies 105 at 91.4% strict precision (Wilson 95% CI [84.5%, 95.4%]). Every certification produces a human readable proof trace in which each step can be independently challenged. Holistic LLM judges achieve comparable precision at matched coverage but fail on different problems (Jaccard 0.14-0.36), making the approaches complementary. On 95 adversarial poisoned proofs across 15 domains, structured judges catch 94.7% versus 83.2% for holistic judging (p= 0.0017). The overall 11.5 pp gap concentrates in hidden premises (90.6% vs. 62.5%, a 28 pp difference) and fabricated citations (100% vs. 90%), the error classes where the formal analysis predicts an advantage; performance is identical on arithmetic and theorem-misapplication errors, where no advantage is predicted. On GPQA Diamond (n= 65), certified precision is 97.1% (Wilson CI [85.1%, 99.5%]).

---


### 236. [Language-Critique Imitation Learning from Suboptimal Demonstrations](https://arxiv.org/abs/2607.01225)

**<font color=#1a73e8>作者：</font>** Chih-Han Yang, Dai-Jie Wu, Yun-Ping Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior work on imitation learning from suboptimal demonstrations typically relies on compressed supervision signals such as confidence estimates, discriminator scores, or importance weights. These scalar signals are inherently limited, as they cannot explicitly express intermediate reasoning about task progress, failure modes, or corrective actions. We propose a language-critique framework for imitation learning from suboptimal demonstrations that instead leverages natural language as a structured supervision signal, avoiding the collapse of expressive feedback into scalars. Our method first constructs language labels from demonstrations that explicitly describe current progress, identify suboptimal behaviors, and provide fine-grained corrective guidance. We then introduce a language-critique loss that directly trains policies using these structured signals without reducing them to scalars, and instantiate it for both behavior cloning and diffusion policies, yielding LC-BC and LC-DP. We further provide a theoretical result showing that the proposed objective upper-bounds the expert performance gap under standard assumptions. Empirically, we evaluate on diverse continuous control tasks spanning navigation, manipulation, and gameplay, where our methods consistently outperform strong imitation learning and offline reinforcement learning baselines. These results demonstrate that language can serve as a powerful and structured form of supervision for learning robust policies from suboptimal data.

---


> [!TIP]
> 当前位于：**201-236**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-236**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
