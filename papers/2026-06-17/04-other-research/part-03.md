# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 101. [False Sense of Safety in Selective Signal Classification: Auditing Bound Tightness and Exchangeability for Risk Control](https://arxiv.org/abs/2606.15153)

**<font color=#1a73e8>作者：</font>** Jingwen Zhou, Mingzhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective prediction with distribution-free risk control promises that, with confidence 1-delta over the calibration draw, the error rate of accepted inputs stays below a user budget alpha. We audit this promise on signal-domain detectors -- machine anomalous-sound detection (ASD) and AI-generated-image forensics -- for four calibration rules: uncertified empirical thresholding (NAIVE) and certified Hoeffding, Clopper-Pearson (CP), and betting (WSR) upper confidence bounds. We report three findings. (i) NAIVE thresholding, common in practice, exceeds its declared budget in 49-73% of synthetic trials (n=200 calibration points) and in up to 68% of real-data splits: a false sense of safety rather than a broken theorem, since the rule never had a certificate. (ii) Tightness matters: CP and WSR certify substantial coverage where Hoeffding certifies none, with zero observed budget overruns under exchangeable splits. (iii) Under grouped deployment (unseen machine types or generators), certified rules overrun in 9-30% of trials -- far above delta -- showing the failure lies in the broken exchangeability premise, not in the bounds; a conservative per-group threshold restores validity at a severe coverage cost.

---


### 102. [Semantic Reasoning in Medicine: The Role of Knowledge Graphs Across Five Key Domains](https://arxiv.org/abs/2606.15155)

**<font color=#1a73e8>作者：</font>** Haniye Sherafatmandjoo, Mohammad Akbari, Zahed Rahmati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) have emerged as a promising solution for integrating and reasoning over complex biomedical and clinical data in healthcare. By representing structured relationships among entities such as diseases, drugs, symptoms, and patient records, KGs provide a semantic backbone for decision-making, prediction, recommendation, and personalized care. Recent advances have demonstrated their utility across diverse medical applications--including clinical decision support systems, disease and treatment outcome prediction, health recommender systems, precision medicine, and medical question answering--where KGs often enhance interpretability, semantic coherence, and patient-specific reasoning. In parallel, a growing body of work focuses on medical KG generation itself, proposing frameworks that construct graphs from EHRs, clinical narratives, biomedical literature, and web resources using ontologies, semantic web technologies, deep-learning-based information extraction, and hybrid neuro-symbolic pipelines. Despite this progress, significant challenges remain, including limited and fragmented knowledge coverage, difficulties in aligning heterogeneous data sources, the fragility of current reasoning and representation-learning methods on dense multi-relational graphs, and unresolved issues related to privacy, bias, and accountability. This survey reviews and categorizes current research on KGs in medicine along both application-oriented and methodology-oriented dimensions, discusses their benefits and technical foundations, and outlines key limitations and open research directions. By analyzing trends, architectures, and evaluation practices, this work aims to guide future developments in KG-driven medical AI systems and support their safe and effective integration into healthcare environments.

---


### 103. [RefGC-SR$^2$: Reference-guided Generated Content Super-Resolution and Refinement](https://arxiv.org/abs/2606.15158)

**<font color=#1a73e8>作者：</font>** Jeahun Sung, Dahyeon Kye, Soo Ye Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided generation (e.g., object compositing, customization) has progressed rapidly, yet current pipelines share a fundamental limitation: the object-centric high-resolution reference image (HRRI) provided by users is downsampled to a fixed low-resolution (LR) before being fed into the model, so the fine-grained details are discarded before the output is even produced. In addition, the generation step then introduces its own artifacts (e.g., identity distortion) on top of this loss. Existing reference-guided generated content refinement (RefGCR) methods can correct some of these artifacts but still operate in the LR domain; reference-guided super-resolution (RefSR) methods recover resolution but assume natural-image degradations and ignore the artifact distribution of generative pipelines. To address both gaps in a single formulation, we introduce a new task: reference-guided generated content super-resolution-refinement (RefGC-SR$^2$), where the original HRRI is reused at the post-processing stage to recover lost details, refine generative artifacts, and upscale the output simultaneously. We construct the first real-world triplet data generation pipeline for this RefGC-SR$^2$ task, training a diptych-conditioned generator to synthesize paired low-quality anchors that public pretrained models cannot provide. We further present a frequency-aware diffusion transformer model for RefGC-SR$^2$ that selectively injects fine details from the HRRI while removing generative artifacts. Extensive experiments demonstrate that our RefGC-SR$^2$ model successfully (i) refines the object identity faithfully with respect to the reference, and (ii) recovers high-resolution details, so that the final result is significantly higher quality and practically more usable compared to existing RefGCR and RefSR baselines.

---


### 104. [Beyond Layer Importance in Layer-wise Sparsity: An Inter-Layer Perturbation-Absorption Perspective](https://arxiv.org/abs/2606.15161)

**<font color=#1a73e8>作者：</font>** Tao Jing, Ningxin Wu, Chen Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The considerable layer-wise redundancy in large language models (LLMs) has established non-uniform sparsity allocation across layers as the standard pruning approach for efficient compression. Existing layer-wise allocation methods that estimate allocation strategy from local signals such as activation outliers or weight spectra mainly derive from local layer importance, whereas the final post-pruning performance is also influenced by the network's subsequent compensatory capacity. In this paper, we directly characterize this property through controlled perturbation experiments. We make the following empirical findings. First, layers exhibit highly heterogeneous responses to pruning-scale perturbations. In most cases, early layers amplify perturbations, while middle and late layers actively absorb them, with relative L2 drift decreasing monotonically across depth and direction realigning toward the unperturbed hidden-state trajectory. Second, absorption is a large-perturbation phenomenon. Under small perturbations the network exhibits amplification across all layers, and the transition to absorption occurs smoothly as perturbation magnitude grows to pruning scale. This enriches the linearized accumulation theory underlying related works. Building on these findings, we define an absorption coefficient per layer and propose absorption-aware correction, an orthogonal augmentation that improves OWL and AlphaPruning by reducing perplexity by 7.13% and boosting zero-shot accuracy by 1.02% across multiple model families at 70% sparsity.

---


### 105. [GeoStream: Toward Precise Camera Controlled Streaming Video Generation](https://arxiv.org/abs/2606.15162)

**<font color=#1a73e8>作者：</font>** Yizhou Zhao, Yifan Wang, Xiaoyuan Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate interactive camera control is essential for video-based world models, but most existing approaches learn camera motion implicitly, leading to inaccurate control under out-of-distribution trajectories. Explicit geometric conditioning improves controllability, but existing methods are non-autoregressive and rely on a static 3D cache built from an initial frame, which becomes ineffective once the viewpoint moves beyond the original frustum. We propose GeoStream, a framework that enables precise metric-scale camera control in autoregressive streaming video generation. Our method maintains a self-refreshing 3D cache that is periodically updated online from the model's own outputs: we estimate depth from the most recently generated frame, unproject to 3D, and reproject into the target view to produce point reprojections as geometric conditioning for subsequent synthesis. By the same principle, the conditioning seen during training is also rendered from the student's own generated frames, yielding a fully on-policy distillation that naturally aligns the train and inference conditioning distributions. Unlike prior work that uses off-policy condition noising, our approach trains the model against the exact error distribution it encounters at inference, mitigating both standard autoregressive drift and the second-order geometric feedback loop that arises when the cache itself is derived from generated outputs. Quantitative and qualitative results show that our approach substantially improves camera controllability.

---


### 106. [VLALeaks: Membership Inference Attacks against Vision-Language-Action Models](https://arxiv.org/abs/2606.15165)

**<font color=#1a73e8>作者：</font>** Xukun Luan, Jinyan Liu, Xuesong Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models enable end-to-end robot control and have garnered widespread attention. However, the memorization of training data inherent to VLA, coupled with the high cost of robotic data acquisition, raises serious concerns regarding data privacy leakage and intellectual property infringement. Membership inference attacks (MIAs) aim to determine whether a given sample belongs to the training set. While representing a significant privacy threat, this attack remains underexplored in the context of VLA models. To bridge this gap, we propose VLALeaks, which is based on attention discrepancies in VLA models. We reveal, for the first time, the privacy vulnerabilities of VLA models. Specifically, it comprises a two-stage process: (1) membership feature extraction, and (2) attack model construction. Experimental results across multiple VLA benchmarks demonstrate that VLALeaks readily reveals membership information and achieves optimal attack AUC and TPR@1\%FPR, highlighting the privacy vulnerabilities in current VLA model deployments. Our work is the first systematic study of MIAs on VLA models, aiming to provide insights for secure and trustworthy VLA models.

---


### 107. [Variational Network with Wavelet-based UNET in Accelerated MRI Reconstruction from Under Sampled K-space Data](https://arxiv.org/abs/2606.15167)

**<font color=#1a73e8>作者：</font>** Yasir Arafat Prodhan, Shaikh Anowarul Fattah  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fully sampled MRI requires dense k-space acquisition, leading to long scan times, reduced clinical throughput, and increased sensitivity to patient motion. Accelerated MRI addresses this by acquiring undersampled k-space data and reconstructing the missing information computationally. However, reconstruction from undersampled measurements is highly ill-posed and can introduce aliasing artifacts, noise amplification, and loss of anatomical detail. Although conventional parallel imaging and compressed sensing methods mitigate these issues, and deep learning methods have further improved reconstruction quality, preserving high-frequency structures under aggressive undersampling remains challenging. In this work, we propose a Variational Network with a Wavelet-based U-Net (W-UNet) for accelerated MRI reconstruction. The framework combines physics-guided iterative reconstruction with learnable multi-scale frequency representations. Standard pooling operations are replaced with Discrete Wavelet Transform and Inverse Wavelet Transform modules, enabling lossless downsampling while preserving low-frequency structure and high-frequency edge details. Integrated into the refinement and sensitivity map estimation stages, the proposed design improves artifact suppression, feature preservation, and reconstruction fidelity in both single-coil and multi-coil settings. Experiments on fastMRI knee and M4Raw brain datasets show state-of-the-art performance. Ablation studies further confirm the effectiveness of wavelet-based feature decomposition for accelerated MRI reconstruction.

---


### 108. [Towards a Unified Generative Model for Scarce Time Series with Domain Experts](https://arxiv.org/abs/2606.15172)

**<font color=#1a73e8>作者：</font>** Zihao Yao, Qi Zheng, Jiankai Zuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthesizing realistic time series with generative models has wide-ranging applications in real-world scenarios. Despite recent progress, most existing methods are trained under the assumption of abundant training data, which substantially limits their effectiveness in data-scarce settings. In this paper, we propose TimeMoDE, a novel framework that integrates Diffusion Transformers with Mixture-of-Experts to exploit both domain adaptability and diffusion-stage awareness for time series generation under data scarcity. It is pre-trained on a large-scale collection of multi-domain datasets to extract domain-agnostic temporal representations and domain-specific information benefiting generalization during fine-tuning. We propose Domain Prompts to condition expert assignment for indistinguishable noised tokens, mitigating the limitations of capturing inter-dataset relationships. Moreover, we incorporate diffusion timestep signals to equip the experts with awareness of time series degradation variations, facilitating adaptive calibrate to stage-dependent denoising requirements. Extensive experiments demonstrate that TimeMoDE outperforms existing methods under diverse low-data settings. It establishes an innovative paradigm for advanced time series few-shot generation.

---


### 109. [Enabling Real-Time Point-of-Care Ultrasound Segmentation: A GPU-Free Deployment in Resource-Limited Settings](https://arxiv.org/abs/2606.15176)

**<font color=#1a73e8>作者：</font>** Weihao Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultrasound imaging is the most widely adopted medical modality globally due to its low cost and portability, yet artificial intelligence (AI) deployment remains constrained by reliance on GPU-accelerated models, creating a structural paradox where the cost of "intelligence" exceeds that of the imaging device itself. Here, we present the systematic adaptation and extensive evaluation of UltraSeg, an ultra-lightweight architecture originally developed for colonoscopic polyp segmentation, now engineered for point-of-care ultrasound (POCUS) across ten public datasets spanning six anatomical sites (breast, thyroid, kidney, carotid, fetal, and small-animal tumor). We systematically validate both variants in ultrasound domains: UltraSeg-130K (0.13M parameters) achieves 89.7 FPS on single-core CPUs and 34.8 FPS on a refurbished mobile device, while UltraSeg-500K (0.5M parameters) delivers 44.6 FPS on CPU and 16.1 FPS on mobile device. UltraSeg-500K matches or exceeds the Dice performance of the 31M-parameter UNet and approaches 105M-parameter TransUNet in average performance, with superior zero-shot cross-dataset generalization on external validation sets (UDIAT, DDTI). By enabling clinical-grade segmentation without GPU dependency, this work brings AI costs in line with ultrasound accessibility, making advanced diagnostics available in resource-limited settings.

---


### 110. [Adaptive Inference-Time Scaling via Early-Step Latent Verification for Image Editing](https://arxiv.org/abs/2606.15188)

**<font color=#1a73e8>作者：</font>** Yue Yu, Yang Jiao, Jiayu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-based image editing has made notable progress with recent advances in generative models. However, the quality of the edited result is still influenced by the randomly sampled initial noise, particularly in complex editing scenarios. An unsuitable initial noise may lead to unsatisfactory editing results. Recent inference-time scaling methods address this issue by sampling multiple initial noises and selecting better candidates. Nevertheless, most of them follow a decode-then-verify scheme which introduces an efficiency-accuracy trade-off. When decoding is performed after limited inference steps, the decoded images often remain too noisy for reliable assessment, whereas sufficiently denoised images require much higher computational cost. To address this issue, we propose VeriLatent, a plug-and-play adaptive inference-time scaling framework with early-step latent verification for image editing. Specifically, we propose a novel verifier that scores each initial noise through a latent-space editing activation map at an early stage. It identifies promising candidates by assessing whether they can induce an effective edit in the correct region. This enables efficient early pruning without decoding latents into images. Building on this, we further develop an adaptive search strategy for inference-time scaling. It allocates inference budgets according to editing difficulty, thereby reducing the number of function evaluations (NFE). Extensive experiments on multiple benchmarks and different base models demonstrate that VeriLatent consistently improves both editing performance and inference-time scaling efficiency.

---


### 111. [AmchiBias: Measuring Stereotypical Bias in Goan Identity Groups with a Minimal Pair Dataset in English and Konkani](https://arxiv.org/abs/2606.15191)

**<font color=#1a73e8>作者：</font>** Michelle Barbosa, Sebastian Padó, Franziska Weeber  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Socio-cultural stereotypical bias is an important consideration in the development and deployment of NLP systems. It is however often considered only at the national level, despite rich subnational socio-cultural structures. We present AmchiBias, the first benchmark for measuring socio-cultural stereotypical bias for the Indian state of Goa with its unique historically multicultural setting. It covers various Goan identity groups and comprises 313 minimal pairs across eight sociodemographic dimensions in both English and Devanagari Konkani. We then evaluate stereotypical bias in five multilingual encoder models on this benchmark. We find near-chance scores in Konkani, reflecting language incompetence for general multilingual models and a lack of Goan cultural competence for Indian language models. Queried in English, models with a stronger Indian language coverage show higher bias for pan-Indian groups than hyperlocal Goan groups. This suggests the English signal reflects pan-Indian pretraining associations rather than genuine Goan cultural knowledge. Our findings highlight a critical gap in low-resource multilingual NLP evaluation for hyperlocal community identities.

---


### 112. [StarOR: Synergizing Tree Search and Test-Time Reinforcement Learning for Optimization Modeling](https://arxiv.org/abs/2606.15197)

**<font color=#1a73e8>作者：</font>** Jiajun Li, Yu Ding, Shisi Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimization modeling is inherently hierarchical, requiring a precise sequence of symbolic commitments. Traditional learning-based automated optimization modeling methods improve modeling policies through large-scale annotated or curated training data, but are costly to adapt to new problem distributions. Meanwhile, one-shot generation remains brittle in hierarchical modeling, where early symbolic errors can propagate into invalid formulations. Test-time scaling offers a promising alternative by enabling structural exploration with additional instance-level computation; however, existing search-based methods typically rely on a fixed policy, causing repeated rollouts to inherit similar modeling biases and providing limited credit assignment for intermediate decisions. To address these limitations, we propose StarOR, a synergistic search-and-adaptation framework that couples MCTS with Test-Time Reinforcement Learning for optimization modeling. StarOR decomposes the modeling process into four stages and updates a transient LoRA adapter via GRPO at each non-terminal node. By using MCTS-generated siblings as local comparison sets, StarOR transforms search-time exploration into instance-specific policy refinement. Moreover, an unsupervised multi-faceted reward system provides fine-grained feedback for intermediate formulation decisions without ground-truth labels. Experiments across five optimization benchmarks show that StarOR achieves state-of-the-art performance even with a 4B backbone, outperforming existing methods and the frontier LLMs.

---


### 113. [City landscape in sight: A crowdsourced framework for unlocking urban-scale window view perceptions from real estate imagery](https://arxiv.org/abs/2606.15198)

**<font color=#1a73e8>作者：</font>** Chucai Peng, Sijie Yang, Ang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> City landscapes viewed through home windows influence quality of life, yet perceptions of actual window views at the urban scale remain understudied. This study presents an approach for large-scale mapping of perceptions using 12,334 window view images (WVIs) collected from actual residential properties listed on real estate platforms in Wuhan, China, representing a rarely explored form of urban view imagery that offers advantages over the rendered or simulated window views commonly examined in previous studies. Through a non-immersive virtual reality platform, we collected 27,477 pairwise comparisons across six perceptual dimensions (e.g.\ Vivid) from 304 participants based on 499 WVIs. A hybrid neural network model was trained to predict human perceptions of all crowdsourced WVIs and map their spatial distribution. Results reveal significant spatial autocorrelation with distinct hot and cold spots across the whole city. Floor level strongly influences human perceptions: while higher floors offer more preferred and extensive window views, lower-floor windows provide residents with quiet and vivid views. An inference model further shows that window view composition matters considerably: high ratios of sky, trees, and low-rise buildings enhance people's preferences and perceptions of vividness, whereas high ratios of high-rise buildings increase perceptions of monotony and oppression. Importantly, these effects are non-linear: the excessive presence of certain elements can alter their impact on human perception. This work advances urban-scale understanding of residents' visual experiences and provides evidence-based guidance for human-centric urban planning and real estate to optimise visual landscapes from windows.

---


### 114. [Keep It in Mind: User Centric Continual Spatial Intelligence Reasoning in Egocentric Video Streams](https://arxiv.org/abs/2606.15200)

**<font color=#1a73e8>作者：</font>** Yun Wang, Junbin Xiao, Han Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce UCS-Bench, a dataset spanning 170+ hours of egocentric visual observations with 8.1K+ timestamped questions for diagnosing User-Centric Continual Spatial intelligence in egocentric video streams. UCS-Bench targets a new problem that emphasizes dynamic spatial reasoning, long-term memory, and their alignment with users' real-time locations. We propose DirectMe, a framework that incrementally constructs and maintains a structured spatial memory from streaming egocentric observations. DirectMe enables robust tracking and recall of object locations, all relative to the user's movement over time. By tightly coupling visual perception with memory updates and spatial reasoning, our approach supports long-horizon queries that require recalling interactions, resolving viewpoint-induced ambiguities, and adapting to dynamic scenes. Our experiments show that DirectMe significantly improves the spatial reasoning of leading multimodal LLMs; it also surpasses many spatially aware and long-form streaming video models. We hope our benchmark and solution will advance spatial intelligence research for egocentric AI assistants. Data and code are available at this https URL.

---


### 115. [Controlled Dynamics Attractor Transformer](https://arxiv.org/abs/2606.15207)

**<font color=#1a73e8>作者：</font>** Cheng Zhang, Minnan Luo, Zesheng Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer architectures have dramatically advanced representation learning and inference in deep models through self-attention mechanisms. In parallel,associative memory (AM) frameworks map representations onto energy landscapes, offering interpretable retrieval mechanisms. However, their continuous-time inference dynamics lack the biological plausibility of classical Continuous Attractor Neural Networks (CANNs). To bridge this gap, we propose Controlled Dynamics Attractor Transformer (CDAT), which couples a mixture von Mises-Fisher (Mo-vMF) attention energy with a Hopfield refinement energy, while augmenting energy descent with a CANN-inspired excitation-inhibition modulation. CDAT instantiates a topology-constrained dynamical system whose couplings encode relational structure among tokens, thereby linking attractor-style dynamics to modern energy-based attention. We further provide a constructive dissipation analysis to formally establish their controlled inference dynamics. Benefiting from these robust and structured dynamics, CDAT achieves state-of-the-art performance across multiple benchmarks in graph anomaly detection and graph classification.

---


### 116. [Attribute Inference from Interactive Targeted Ads](https://arxiv.org/abs/2606.15209)

**<font color=#1a73e8>作者：</font>** Peihao Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Targeted advertising systems can pair audiences selected by advertisers with ad units that expose visible user actions. When an interaction remains linked to the campaign that elicited it, the advertiser may receive an observation tied to a user rather than only an aggregate report. We model that channel as a noisy oracle for attribute inference. The model separates targeting predicates, exposure, interaction, and disclosure. These boundaries capture the gap between eligibility and delivery, and the gap between interaction and advertiser visibility.
We build a reproducible benchmark using synthetic populations calibrated with public data, each with known sensitive labels. A generated campaign semantics layer provides topic variants and response priors. The simulator generates the ground truth, event traces, disclosed observations, and metrics. The evaluation compares Bayesian, supervised, positive and unlabeled, and adaptive attacks under common campaign and disclosure definitions.
The final evaluation uses four topic variants, seven simulator seeds, and two interaction settings. Repeated campaigns with identity exposure produce measurable but bounded inference signal. At $160$ campaigns, Bayesian and supervised attacks reach about $0.64$ AUC in the main setting and about $0.65$ AUC in the higher interaction setting. Disclosure policy is the strongest control. Aggregate reporting removes the evaluated oracle input tied to users. Type filtering and randomized disclosure reduce the released signal. The result is a model, artifact, and defense evaluation method for privacy in interactive targeted advertising. The code is available at this https URL.

---


### 117. [Spokes: Optimizing for Diverse Pretraining Data Selection](https://arxiv.org/abs/2606.15216)

**<font color=#1a73e8>作者：</font>** Clarence Lee, Yejin Choi, Luke Zettlemoyer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diversity plays a critical role in data selection, improving performance under fixed data budgets by reducing redundancy and repetition. However, optimizing for diversity is inherently challenging, as it is a set-level property that depends on interactions between data points rather than individual examples. As a result, existing approaches typically rely on proxies or approximations, which often fail to ensure sufficiently diverse subsets. In this work, we directly optimize diversity by introducing a probabilistic diversification framework based on the G-Vendi score, optimized via exponentiated gradient descent. Our method produces subsets that are substantially more diverse than those obtained via random sampling, achieving a +489 increase in G-Vendi score on a 500k-sample subset. We evaluate our approach on FineWeb and DCLM, where it consistently outperforms existing methods. Notably, SPOKES (diversity-only) improves average downstream performance by +0.4 and +0.5 points over random sampling on DCLM and FineWeb, respectively. More importantly, jointly optimizing for both quality and diversity yields the strongest results: SPOKES achieves gains of +1.5 and +1.4 points on DCLM and FineWeb, outperforming all baselines, including semantic deduplication and quality filtering.

---


### 118. [Can Neural Networks Achieve Optimal Computational-statistical Tradeoff? An Analysis on Single-Index Model](https://arxiv.org/abs/2606.15219)

**<font color=#1a73e8>作者：</font>** Siyu Chen, Beining Wu, Miao Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we tackle the following question: Can neural networks trained with gradient-based methods achieve the optimal computational-statistical tradeoff in learning Gaussian single-index models? Prior research has shown that any polynomial-time algorithm under the statistical query (SQ) framework requires $\Omega(d^{s^\star/2}\lor d)$ samples, where $s^\star$ is the generative exponent representing the intrinsic difficulty of learning the underlying model. However, it remains unknown whether neural networks can achieve this sample complexity. Inspired by prior techniques such as label transformation and landscape smoothing for learning single-index models, we propose a unified gradient-based algorithm for training a two-layer neural network in polynomial time. Our method is adaptable to a variety of loss and activation functions, covering a broad class of existing approaches. We show that our algorithm learns a feature representation that strongly aligns with the unknown signal $\theta^\star$, with sample complexity $\widetilde{O} (d^{s^\star/2} \lor d)$, matching the SQ lower bound up to a polylogarithmic factor for all generative exponents $s^\star\geq 1$. Furthermore, we extend our approach to the setting where $\theta^\star$ is $k$-sparse for $k = o(\sqrt{d})$ by introducing a novel weight perturbation technique that leverages the sparsity structure. We derive a corresponding SQ lower bound of order $\widetilde{\Omega}(k^{s^\star})$, matched by our method up to a polylogarithmic factor. Our framework, especially the weight perturbation technique, is of independent interest, and suggests potential gradient-based solutions to other problems such as sparse tensor PCA.

---


### 119. [Robust and Precise Application Fingerprinting on 5G Physical Uplink Channel](https://arxiv.org/abs/2606.15221)

**<font color=#1a73e8>作者：</font>** Yu Li, Liqi Zhuang, Dong Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Air fingerprinting infers application activity by sniffing metadata from cellular control channels. 5G encrypts these channels, breaking the attack chain that prior attacks depend on. This paper reveals a physical-layer side channel that bypasses encryption: under the link adaptation mandated by the cellular communication standard, the uplink Modulation and Coding Scheme (MCS) remains stable, so the number of Physical Resource Blocks (PRBs) occupied by a transmission accurately reflects the IP packet length. Combined with the uplink control channel that carries downlink information, an attacker can reconstruct a bidirectional traffic profile. This bidirectional information recovery can be achieved simply by observing the uplink spectrum, without decoding any channel. Building on this side channel, we design Crosshair, a passive three-step attack. First, a blind extraction stage recovers the uplink physical channel occupancy from raw IQ samples via energy detection, reconstructing bidirectional traffic from uplink spectrum. Second, we design a data augmentation method that synthesizes spectral profiles across diverse channel conditions, eliminating the need for prior knowledge of the communication environment. Third, cross-modal alignment embeds the spectral and IP domains into a shared space, enabling new applications to be enrolled from a collected IP trace alone. Extensive experiments on a 5G NR testbed demonstrate the robustness and precision of Crosshair: it outperforms the State-of-the-Art (SOTA) physical layer fingerprinting method in application recognition accuracy, and maintains high accuracy in cross-MCS scenarios.

---


### 120. [Edu-Theater: A Data-Efficient Agent Framework for Scalable Learner Behavior Simulation through Staging Roll-Call](https://arxiv.org/abs/2606.15225)

**<font color=#1a73e8>作者：</font>** Weibo Gao, Qi Liu, Linan Yue 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale learner-task interaction data are crucial for intelligent educational systems but are costly to collect and constrained by privacy and learner engagement. Learner simulators play a critical role in simulating scalable learner behavior without the need for continuous involvement of real learners. However, existing methods are predominantly \textbf{individual-centric}, pairing a simulator with each learner to iteratively infer latent knowledge states from dense interaction histories, which is both data- and computation-intensive, and fragile in cold-start scenarios. We propose a \textbf{cohort-aware roll-call simulation paradigm} that first constructs cohort-level proficiency priors and refines individual learner states through a small number of targeted diagnostic queries. Based on this paradigm, we introduce \textbf{Edu-Theater}, an LLM-powered agent system that performs cohort-aware learner simulation via a teacher agent and retrospective roll-call probing over learner logs. Edu-Theater enables scalable future behavior simulation without the need for dense per-learner histories. Experiments on two real-world datasets demonstrate that Edu-Theater achieves higher simulation accuracy with significantly fewer LLM calls, producing synthetic data that enhances downstream applications such as adaptive testing.

---


### 121. [Show the Signal, Hide the Noise: Spectral Forcing for Pixel-Space Diffusion](https://arxiv.org/abs/2606.15236)

**<font color=#1a73e8>作者：</font>** Weichen Fan, Haiwen Diao, Penghao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space diffusion models are trained on full-bandwidth noisy images, yet the useful signal available to the denoiser is strongly frequency dependent. Under rectified-flow diffusion and natural-image power-law spectra, the per-band data-to-noise contour $k^{*}(t) = (1-t)^{-2/\alpha}$ separates a signal-bearing low-frequency region from a noise-dominated high-frequency region at each time $t$. We show that this implicit coarse-to-fine structure is not merely descriptive: it induces a capacity-allocation problem. A standard pixel-space denoiser must discover the moving bandwidth boundary internally and can spend computation on frequency-time regions where the optimal prediction collapses to deterministic baselines rather than data-distribution modeling. To make this boundary explicit, we introduce Spectral Forcing, a parameter-free, time-conditional 2D-DCT low-pass operator applied to the noisy input before the patch embedder. Its cutoff expands monotonically with the diffusion time and becomes the identity at the data endpoint. Through controlled synthetic experiments, we identify the regime in which the operator is beneficial: coarse patch tokenization and data whose high-frequency content is predominantly noise rather than essential signal. On ImageNet-256 with JiT-700M/32, Spectral Forcing consistently improves both FID and Inception Score across different training epochs, demonstrating robust gains throughout training; at finer tokenization, the spectral forcing is still competitive. We further insert the unchanged operator into SenseNova-U1, a unified text-to-image model, where it improves DPG-Bench and GenEval, showing that the input-side spectral prior transfers beyond class-conditional generation. These results suggest a route to capacity-efficient pixel-space diffusion by showing the signal and hiding the noise.

---


### 122. [EnvShip-Bench: An Environment-Enhanced Benchmark for Short-Term Vessel Trajectory Prediction](https://arxiv.org/abs/2606.15240)

**<font color=#1a73e8>作者：</font>** Kun Ma, Qilong Han, Chengjing Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vessel trajectory prediction is important for intelligent shipping, maritime surveillance, and navigation safety. However, existing public maritime AIS resources are often limited by inconsistent forecasting protocols, uneven data quality, and the lack of benchmark-ready contextual annotations, which hinder fair comparison and context-aware modeling. To address this gap, we present EnvShip-Bench, a unified benchmark for short-term vessel trajectory prediction built from large-scale raw AIS data from the Danish Maritime Authority (DMA) and NOAA through a common processing pipeline. EnvShip-Bench adopts a standardized forecasting protocol with 10 minutes of observation, 10 minutes of prediction, and 20-second sampling in vessel-centric local metric coordinates. Beyond the large-scale core benchmark, it provides a quality-first compact subset for efficient and reproducible experimentation, together with synchronized environmental and nearby-vessel context extensions. As a result, EnvShip-Bench supports trajectory-only, environment-aware, and interaction-aware forecasting under a unified evaluation framework. Extensive benchmark statistics and analysis demonstrate that EnvShip-Bench offers a standardized, extensible, and context-aware foundation for maritime trajectory forecasting research.

---


### 123. [Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosystems](https://arxiv.org/abs/2606.15242)

**<font color=#1a73e8>作者：</font>** Yi Xie, Jiawei Du, Yu Cheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skills are becoming the capability layer through which LLM agents turn plans into actions, but their use introduces security risks such as data leakage, unauthorized operations, and tool misuse. Existing vetting usually evaluates each skill in isolation, while real agent tasks often invoke multiple skills in a shared execution context. This creates Skill Composition Risk (SCR): a skill that appears benign alone can become harmful when its outputs, trust signals, authorization cues, or side effects influence later invocations along an activated path. We introduce SCR-Bench to evaluate this risk in controlled, sandboxed skill environments. Rather than relying only on textual intent or surface behavior, SCR-Bench records downstream state changes and path-level outcomes across composed skill executions. It contains three sub-benchmarks: SCR-CapFlow for capability-flow composition, SCR-TrustLift for trust-transfer composition, and SCR-AuthBlur for authorization-confusion composition. Across SCR-Bench, composed paths expose risks that are largely absent under isolated evaluation. In SCR-CapFlow, attack success rate reaches 33.6 percent under composition, compared with near-zero isolated baselines. In SCR-TrustLift, attack success rate exceeds 96.5 percent on four of five backends. In SCR-AuthBlur, the risky-approval rate increases by 71.8 percent relative to the L0 isolated baseline under the L1 context setting. These results show that agent skill security should be assessed at the level of activated paths rather than isolated artifacts. SCR and SCR-Bench provide a foundation for path-aware risk evaluation and defense in LLM agent skill ecosystems. Benchmark: this https URL.

---


### 124. [SPARK: Spatial Policy-driven Adaptive Reinforcement learning for Knowledge distillation](https://arxiv.org/abs/2606.15243)

**<font color=#1a73e8>作者：</font>** Mohamed Jismy Aashik Rasool, Shabir Ahmad, Gisong Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization enables deployment of image restoration (IR) networks on resource-constrained devices, but introduces rounding noise that disproportionately degrades high-frequency regions such as edges and fine textures. Existing knowledge distillation (KD) methods apply distillation signals uniformly across all spatial locations, overlooking the varying reconstruction difficulty across image regions. To address this, we propose SPARK (Spatial Policy-driven Adaptive Reinforcement Learning for Knowledge Distillation), a framework that adaptively allocates distillation effort using a lightweight reinforcement learning (RL) policy network. At each training step, a difficulty feature extractor computes four signals, namely Laplacian variance, pixel variance, student reconstruction error, and teacher-student knowledge gap, which are fed into a compact policy CNN that produces a stochastic spatial weight map to modulate the KD loss during quantization-aware training (QAT). SPARK is IR task-agnostic, adds no inference cost, and integrates into any existing QAT pipeline without architectural changes. Experiments on benchmark datasets demonstrate that SPARK consistently outperforms PTQ, QAT, and state-of-the-art (SOTA) KD approaches across multiple student architectures, achieving reconstruction quality closest to the full-precision teacher under significant computational constraints.

---


### 125. [M-CTX: Exact and Scalable Spatial Context Retrieval for Trajectory Analytics](https://arxiv.org/abs/2606.15244)

**<font color=#1a73e8>作者：</font>** Kun Ma, Qilong Han, Chengjing Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern trajectory predictors increasingly condition on external spatial context, such as map geometry, signed distance fields (SDFs), and nearby moving agents. While this context improves prediction quality, constructing it for every training anchor has become a hidden systems bottleneck. In a representative maritime AIS pipeline, spatial context construction requires roughly 17 CPU-days for a 5.48M-anchor corpus, dominating the cost of the downstream predictor. We present M-CTX, an exact and scalable spatial context-retrieval framework for trajectory analytics. M-CTX recasts context construction as an ingest-once, query-many spatial database workload and replaces three brute-force stages -- OSM range retrieval, SDF computation, and moving-vessel neighbour lookup -- with composable, index-backed operators. Its learned range-index backend, BR-LZ, provides recall-complete MBR-overlap range retrieval and reduces candidate amplification by 1.1x--2.7x relative to global-expansion one-curve baselines. Across four maritime regions, eight baseline systems, synthetic workloads with up to 40M spatial features, and 10^7-record AIS streams, M-CTX reproduces the reference context exactly. On the 5.48M-anchor corpus, it reduces context construction from about 17 CPU-days to 1.8 hours, a measured 226x end-to-end speed-up. An optional storage mode further compresses SDF context by 64x with only a 0.04 m ADE change. These results establish exact spatial context retrieval as a first-class database problem in modern trajectory analytics. Code and datasets are publicly available at this https URL.

---


### 126. [Exploring Starts Are Not Enough: Counterexamples and a Fix for Monte Carlo Exploring Starts](https://arxiv.org/abs/2606.15247)

**<font color=#1a73e8>作者：</font>** Octave Oliviers, Glenn Vinnicombe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The asymptotic behaviour of Monte Carlo Exploring Starts (MCES) is a long-standing open question in reinforcement learning, even in the tabular setting. We investigated the convergence properties of tabular MCES by constructing examples in which the algorithm converges to suboptimal solutions. This paper presents new counterexamples for both initial-visit and first-visit MCES and gives a convergence-restoring modification for the initial-visit case. We show that stable suboptimal solutions may exist for initial-visit MCES with sample-average updates even when greedy actions are updated more often than non-greedy actions on average. However, by scaling learning rates inversely to update frequencies on a state-by-state basis, convergence to optimality is guaranteed. Unlike previous uniformisation methods, this modification is applicable to large-scale problems that require approximating the estimated value function. We then extend the example to show that sample-average first-visit MCES may also converge to suboptimal solutions. This largely settles a fundamental open problem and shows that exploring starts alone do not guarantee convergence to optimality. More broadly, these results highlight that convergence depends critically on the relative size and frequency of updates applied to different actions, making the choice of learning rates and the balance between exploration and exploitation central to the analysis of MCES and the implementation of scalable Monte Carlo control methods.

---


### 127. [Focus, Align, and Sustain: Counteracting Gradient Dilution in Incremental Object Detection](https://arxiv.org/abs/2606.15253)

**<font color=#1a73e8>作者：</font>** Aoting Zhang, Dongbao Yang, Chang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting Detection Transformers to Incremental Object Detection (IOD) poses a systemic challenge, as set-based optimization is inherently destabilized by sequential learning. In this work, we identify Gradient Dilution as the root cause of performance degradation, wherein optimization signals required to preserve old knowledge are progressively weakened. This phenomenon manifests as a cascading erosion of preservation gradients in magnitude, direction, and support coverage, driven by three tightly coupled factors: Signal Dispersion, where foreground gradients are overwhelmed by background noise; Assignment Drift, where stochastic query-target matching induces inconsistent gradient trajectories; and Support Attrition, where gradients from retained samples insufficiently cover the old-class feature space, weakening decision boundaries under interference from new classes. To counteract this, we propose FAS, a unified framework that Focuses, Aligns, and Sustains gradient flow throughout incremental learning. Specifically, we introduce prior-injected queries to focus discriminative signals by filtering background interference at the source. We further propose deterministic anchor distillation to align query-target assignments and enforce semantic consistency across stages under unstable matching. Finally, we devise manifold-support replay to sustain distributional support of old classes, counteracting representational erosion induced by continual updates. Extensive experiments show that FAS restores robust optimization dynamics and outperforms state-of-the-art methods, achieving over 5.0 AP improvement in the challenging 40+10x4 incremental setting.

---


### 128. [AI for Social Good: An Investigation of the Causal Relationship Between Environmental Regulations and Their Effects on Air Pollution in London, UK](https://arxiv.org/abs/2606.15257)

**<font color=#1a73e8>作者：</font>** Yang Han, Jacqueline CK Lam, Victor OK Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Air pollution regulation is central to urban public health governance, but estimating its effects is difficult because policies are implemented non-randomly and pollution trajectories are shaped by meteorology, socioeconomic change, temporal trends, and overlapping interventions. This study develops an uncertainty-aware Bayesian deep learning framework to estimate the aggregate effect of air pollution regulations on PM$_{2.5}$ concentrations in London from 2010 to 2020. The framework integrates daily PM$_{2.5}$ observations from Inner London monitoring stations, meteorological covariates, annual socioeconomic indicators, month-of-year and day-of-week indicators, and daily regulation status data for 32 policy measures. A Bayesian LSTM captures temporal dependencies in environmental and socioeconomic covariates, Bayesian embedding layers represent temporal and regulation status inputs, and a regulation status prediction branch supports propensity score-based adjustment for non-random policy implementation. Regulatory effects are estimated by comparing observed PM$_{2.5}$ concentrations with counterfactual predictions under a hypothetical no-regulation scenario, with uncertainty summarized across repeated Bayesian training runs and bootstrap resampling. Results show that London's regulations were associated with an average PM$_{2.5}$ reduction of 1.88 $\mu$g/m$^3$, a relative reduction of 12.35%, with a 95% confidence interval of 1.64-2.12 $\mu$g/m$^3$. Estimated effects were limited before 2013, became clearer from 2013 to 2017, and were strongest in 2018 and 2019. The findings suggest that sustained and cumulative regulatory interventions contributed to measurable improvements in London's air quality. This study demonstrates how uncertainty-aware causal AI can support environmental accountability, public health protection, and evidence-based governance for environmental decision-making.

---


### 129. [Trust-Region Diffusion Policies for Massively Parallel On-Policy RL](https://arxiv.org/abs/2606.15260)

**<font color=#1a73e8>作者：</font>** Huy Le, Onur Celik, Denis Blessing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with massively parallel simulations has become a standard framework for developing robust, deployable policies; however, most existing approaches still rely on simple Gaussian policy parameterizations. Diffusion models provide a more expressive policy class and have shown strong performance on challenging control problems, yet most diffusion-based RL methods are designed for offline or off-policy training. In this work, we ask whether diffusion policies can be trained effectively in the massively parallel, on-policy regime. To this end, we introduce Trust-region Diffusion Policies (TruDi), which enables diffusion policies for on-policy RL with massively parallel simulations. This setting is particularly challenging because the data distribution changes quickly across updates, making stable training with complex policies difficult. TruDi addresses this by integrating a trust-region optimization rule to enforce a KL-divergence constraint over the entire diffusion trajectory. Empirically, we evaluate TruDi on a diverse set of 4 massively parallel RL benchmarks comprising a total of 73 tasks. Across these tasks, TruDi consistently outperforms or is on-par with strong baselines on standard tasks and achieves clear gains on more challenging humanoid control tasks, establishing a strong new baseline for massively parallel on-policy RL.

---


### 130. [Trusted Multi-View Deep Learning Classification of Fetal Congenital Heart Disease with Feature-level and Decision-level Fusion](https://arxiv.org/abs/2606.15265)

**<font color=#1a73e8>作者：</font>** Tan Zhou, Shifa Yao, Suncheng Xiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Congenital heart disease (CHD) refers to the abnormal anatomical structure caused by the abnormal development of the heart and great vessels during embryonic development. Traditional diagnostics often fail to achieve high accuracy and efficiency, especially given the complexity of cardiac anatomy. This study presents a specialized multi-view deep learning framework for CHD binary classification using echocardiographic images. A large-scale CHD dataset, including five views, was used to train the model, enabling it to integrate multi-angle image data. The framework utilizes advanced feature extraction and attention mechanisms to improve diagnostic precision and reliability. An uncertainty-based decision-making component is also integrated to handle low-quality images, enhancing diagnostic outcomes. Experimental results show that this method achieves top-tier performance on our dataset and provides a robust tool for early CHD detection, underscoring its potential for clinical use. The dataset and source code will be released upon paper acceptance.

---


### 131. [Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation](https://arxiv.org/abs/2606.15266)

**<font color=#1a73e8>作者：</font>** Yuchen Song, Xi Chen, Mingze Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech translation (S2ST) systems have achieved impressive progress in semantic accuracy and speech naturalness. However, the cross-lingual transfer of lexical stress, a vital cue for emphasis and speaker intent, remains heavily underexplored, compounded by a lack of reliable automatic evaluation metrics for tonal languages like Chinese. We investigate English-to-Chinese S2ST stress transfer by constructing a stress-annotated Chinese dataset and an XLS-R-based Mandarin stress detector. Integrating this with the English EmphAssess system, we propose a novel objective metric for cross-lingual stress evaluation. Furthermore, we fine-tune CosyVoice3 to build a stress-aware S2ST system. Experiments demonstrate that our proposed S2ST architecture significantly outperforms existing systems in stress translation capability while maintaining competitive translation quality. Furthermore, our evaluation metric exhibits a strong correlation with human subjective judgments.

---


### 132. [When to use what Schatten-$p$ norm in deep learning?](https://arxiv.org/abs/2606.15268)

**<font color=#1a73e8>作者：</font>** Thomas Pethick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Schatten-$\infty$ based optimizers such as Muon have shown promising empirical performance, but there remains seemingly conflicting observations regarding whether they are beneficial. We resolve this conflict by showing that the conclusion is regime dependent. Even when the objective is smooth in the Schatten-$\infty$ geometry, smaller Schatten-$p$ geometries can be optimal, specifically in the low-dimensional regime, which we show includes Chinchilla scaling. This conclusion follows from a new noise-robust acceleration result for the SODA framework for $p>2$. The same analysis explains why Muon-like methods do not require warmup, why they naturally favor large batches, and yields a batch size scaling rule for arbitrary $p$.

---


### 133. [Feature Attribution in Directed Acyclic Graphs Using Edge Intervention](https://arxiv.org/abs/2606.15273)

**<font color=#1a73e8>作者：</font>** Qiheng Sun, Junxu Liu, Xiaokai Mao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shapley value-based feature attribution methods face challenges in scenarios involving complex feature interactions and causal relationships, even when a causal structure is provided. Existing methods typically adopt a node-centric view, attributing importance solely to individual features. Consequently, they often fail to simultaneously capture the externality and exogenous influence of features, leading to unreasonable interpretations. To overcome these limitations, we propose a novel feature attribution method called DAG-SHAP, which is based on edge intervention. DAG-SHAP treats each feature edge as an individual attribution object, ensuring that both externality and exogenous contributions of features are appropriately captured. Additionally, we introduce an approximation method for efficiently computing DAG-SHAP. Extensive experiments on both real and synthetic datasets validate the effectiveness of DAG-SHAP. Our code is available at this https URL.

---


### 134. [MamBOA: State-Space Architecture for Video Recognition](https://arxiv.org/abs/2606.15275)

**<font color=#1a73e8>作者：</font>** Mustafa Bora Çelik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained action recognition demands temporal reasoning that general-purpose architectures address through different cost-accuracy tradeoffs: 3D dense operators couple computation to the input volume, while difference-based methods approximate motion through rigid, hand-crafted subtraction of uncontextualized features - each reflecting a deliberate design choice with corresponding limitations in expressiveness or flexibility. We present MamBOA, a backbone-agnostic temporal framework built upon a novel interleaved scan structure that recasts the selective state-space recurrence (S6) as a native motion synthesizer. By interleaving consecutive feature representations extracted from a pretrained backbone into a single alternating sequence, the proposed scan structurally drives the recurrence to encode both temporal observations of each position within a shared hidden state, separated by only a single decay step - rendering the inter-frame transition an intrinsic component of the state dynamics rather than an externally computed quantity. A cascade of dedicated alignment and decoding operations then distills this joint encoding into an explicit motion representation, which a dual-path pooling mechanism adaptively aggregates by balancing attention-driven selection with uniform temporal coverage. The framework interfaces seamlessly with CNN, Transformer, and Mamba backbone families, adding only ~2.1 GFLOPs per feature pair. On Diving48, MamBOA achieves 85.02% Top-1 accuracy with an image-pretrained backbone and 86.24% with a video-pretrained backbone processing the entire video in a single forward pass - demonstrating that structurally induced state-space dynamics constitute a principled and general foundation for motion modeling.

---


### 135. [RECTOR: Masked Region-Channel-Temporal Modeling for Affective and Cognitive Representation Learning](https://arxiv.org/abs/2606.15278)

**<font color=#1a73e8>作者：</font>** Jinhan Liu, Mahsa Shoaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Affective and cognitive disorders manifest as distributed, time-varying brain network dynamics across regions, channels, and time, challenging robust representation learning from EEG/sEEG for clinical diagnosis. We propose RECTOR (Masked Region-Channel-Temporal Modeling), an end-to-end self-supervised framework that unifies joint region-channel-temporal representation learning beyond fixed anatomical priors. At its core, RECTOR-SA is a hierarchical, block-sparse self-attention induced by Adaptive Functional Partitioning that evolves region structures from static anatomical definitions to adaptive functional regions. The self-supervision is driven by Masked Topology and Representation Learning, which jointly optimizes three complementary objectives: Masked Predictive Modeling, Topological Structure Modeling, and Cross-View Consistency. Across diverse benchmarks, RECTOR sets a new state-of-the-art in EEG emotion recognition and sEEG task-engagement classification. Crucially, its strong robustness to missing channels and cross-montage generalization underscores its potential for large-scale pre-training on heterogeneous EEG/sEEG, providing interpretable insights at both region and channel levels.

---


### 136. [Rethinking Structural Anomaly Detection: From Decision Boundaries to Projection Operators](https://arxiv.org/abs/2606.15280)

**<font color=#1a73e8>作者：</font>** Alexander Bauer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most existing anomaly detection methods rely on estimating a probability density or learning an enclosing decision boundary, implicitly assuming that normal data occupies a region of non-zero volume in the ambient space. In contrast, structural anomaly detection considers data that lies near a low-dimensional manifold, creating a mismatch between the inductive bias of existing methods and the structure of the data, often resulting in degraded performance. To address this mismatch, we introduce a geometric perspective. Specifically, we learn a projection operator onto the manifold of normal samples and define a sample as anomalous if it is altered by this projection. This formulation naturally integrates the inductive bias of manifold-supported data and reframes anomaly detection in terms of a projection residual, thereby resolving issues arising from modeling degenerate distributions. Notably, it provides a unifying interpretation of reconstruction-based methods by explaining their success and failure in terms of projection quality. In particular, it explains the strong generalization ability of projection-aligned models as a consequence of contraction behavior toward the manifold. Moreover, by decoupling anomaly detection from probabilistic modeling, it reduces the tendency to misclassify rare but normal samples, a widely recognized limitation of existing approaches. Empirically, we demonstrate that projection-aligned methods achieve strong performance, outperforming boundary-based methods while improving upon existing reconstruction-based approaches.

---


### 137. [Enhancing Precision Agriculture with a Hybrid Deep Learning Framework for Multi-Class Plant Disease Classification and Interpretability](https://arxiv.org/abs/2606.15282)

**<font color=#1a73e8>作者：</font>** Hasibul Islam Sufi, Ridam Roy, Shayla Alam Setu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study proposes an overall deep learning architecture for multi-class classification of plant diseases from high-resolution leaf imagery, with a particular interest in investigating the behavior of ResNet-50 and a hybrid ResNet + Vision Transformer (ViT) design. A specially gathered image database with 15,200 training images and 3,800 validation images spanning 38 classes across multiple crops, including tomato, apple, grape etc. were subjected to preprocessing steps such as resizing, normalization, and data augmentation to enhance model robustness. Multiple architectures, including ResNet-50, MobileNetV2, and EfficientNet-B0, were trained and compared with the hybrid ResNet + ViT model. All models were fine-tuned using the AdamW optimizer and cross-entropy loss, with early stopping applied to prevent overfitting and ensure generalization. Furthermore, interpretability techniques such as Grad-CAM and saliency maps were implemented to indicate disease-relevant regions, while segmentation-based analysis was performed to identify the affected parts of a leaf. For every one of the considered architectures, ResNet-50 led to the highest accuracy of 98.74%, whereas the hybrid ResNet + ViT model achieved a competitive accuracy of 98.58%, showing that the hybrid architectures were effective in capturing both local and overall information. The experimental results showcase the promise of transformer-based models to achieve highly accurate, interpretable, and computationally efficient computer-based multi-class multi-disease classification systems, providing helpful assistance for cultivation management practices as well as for precision farming.

---


### 138. [Decoupled Motion Representation Learning for Moving Infrared Small Target Detection](https://arxiv.org/abs/2606.15286)

**<font color=#1a73e8>作者：</font>** Guoyi Zhang, Peiwen Wu, Han Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection in dynamic scenes remains challenging due to the highly coupled motions among targets, imaging platforms, and dynamic backgrounds. Existing multi-frame methods usually perform implicit temporal modeling, where coherent background dynamics dominate motion correspondence learning, leading to an inherent trade-off between detection and false alarms. In this work, we observe that background motions exhibit strong global coherence, whereas small targets mainly correspond to sparse local motion anomalies. Moreover, many false-alarm responses maintain high consistency with globally coherent motion patterns, indicating that they mainly originate from coherent background dynamics rather than genuine target motions. Based on these observations, we propose a decoupled motion representation learning framework for moving infrared small target detection. Specifically, an explicit motion branch is introduced to model globally coherent motion dynamics using pretrained optical flow priors, together with a structure-preserving self-supervised adaptation strategy for infrared motion correspondence learning. Meanwhile, an implicit motion branch based on deformable feature alignment is designed to capture target-sensitive local motion anomalies under coherent motion guidance. Furthermore, a coherent-motion-guided local anomaly reasoning module is proposed to identify and suppress coherent-motion-induced false responses during localized motion modeling. Extensive experiments on two challenging infrared small target detection benchmarks demonstrate that the proposed method consistently outperforms existing state-of-the-art approaches, particularly in dynamic scenes with complex motions, while maintaining favorable inference efficiency.

---


### 139. [G2IA: Geometry-Guided Instance-Aware Retrieval and Refinement for Cross-Modal Place Recognition](https://arxiv.org/abs/2606.15287)

**<font color=#1a73e8>作者：</font>** Xianyun Jiao, Jingyi Xu, Zhongmiao Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal place recognition (CMPR) enables camera-only robots to localize against pre-built LiDAR maps in autonomous navigation scenarios. This image-to-point-cloud setting is challenged by two coupled ambiguities: the modality gap between perspective RGB appearance and sparse metric geometry, and perceptual aliasing among urban places with similar roads, facades, intersections, and object arrangements. Instead of treating CMPR as a single global descriptor matching problem, we argue that reliable retrieval requires both geometry-aware representation alignment and fine-grained candidate verification. In this paper, we propose G2IA, a geometry-guided instance-aware framework for image-to-point-cloud place recognition. In the retrieval stage, visual geometry priors from VGGT and instance features are integrated to construct place descriptors that are more compatible with LiDAR-derived map representations. In the refinement stage, the retrieved candidates are re-ranked by explicitly verifying whether local instance shapes and their relative spatial layouts are consistent across modalities. Experiments on public benchmarks demonstrate that G2IA consistently improves image-to-point-cloud place recognition under different localization thresholds, and exhibits strong cross-dataset generalization.

---


### 140. [CODA-BENCH: Can Code Agents Handle Data-Intensive Tasks?](https://arxiv.org/abs/2606.15300)

**<font color=#1a73e8>作者：</font>** Yuxin Zhang, Ju Fan, Meihao Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Advanced agents are increasingly demonstrating the potential to operate as autonomous engineers, creating a growing demand for evaluation benchmarks that capture the complexity of real-world development. Such environments typically involve both complex code and large-scale data (i.e., file system). However, existing benchmarks usually evaluate code-centric or data-centric capabilities in isolation, leaving a clear gap with real development scenarios. In this paper, we bridge this gap by introducing CODA-BENCH, the first benchmark to jointly evaluate code and data intelligence in a data-intensive environment. We construct a data-intensive Linux sandbox based on the Kaggle ecosystem (containing hundreds of datasets), where agents must actively explore complex file hierarchies to identify relevant resources and generate code for data-driven analytical tasks. CODA-BENCH comprises 1,009 tasks spanning 31 communities, with each task environment containing an average of 980 files, simulating realistic data scale and noise. Evaluations of advanced agents reveal that even top-performing systems struggle to effectively integrate data discovery with code execution, achieving a success rate of only 61.1%. These results highlight a substantial gap in current agentic capabilities for data-intensive tasks and point to promising directions for future research.

---


### 141. [Discovering Lattice Reduction Strategies via Self-Play](https://arxiv.org/abs/2606.15301)

**<font color=#1a73e8>作者：</font>** Mohamed Malhou, Kristin Lauter, Ludovic Perret  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Lenstra-Lenstra-Lovász (LLL) algorithm is a seminal contribution to computer science used for lattice basis reduction, yet its polynomial-time outputs produce bases that are far from optimal as the dimension grows. We show that deep reinforcement learning can discover strictly superior, generalizable reduction strategies by interacting with the primitive action space of LLL. We formulate lattice reduction as a single-player Markov Decision Process (MDP) and train a deep residual network using an AlphaZero-style self-play pipeline augmented with adaptive-horizon MCTS (Monte Carlo Tree Search), which couples multi-step network predictions with an entropy-gated expansion mechanism. The resulting policy, DeltaStar, is trained exclusively on small $8$-dimensional $q$-ary lattices and requires fewer primitive row operations than LLL. Crucially, it generalizes zero-shot to unseen moduli and higher dimensions up to $n=32$ without retraining.

---


### 142. [HemExp: Clinically-Guided Latent Diffusion for Modeling Hematoma Expansion](https://arxiv.org/abs/2606.15304)

**<font color=#1a73e8>作者：</font>** Orhun Utku Aydin, Satoru Tanioka, Tzu I Chuang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hematoma expansion (HE) after spontaneous intracerebral hemorrhage (ICH) is a major determinant of acute triage and treatment decisions in neurosurgical care. However, most existing methods provide either a binary expansion risk or a single follow-up volume, limiting uncertainty-aware decisions. We introduce HemExp, a clinically-guided latent diffusion model that generates patient-specific follow-up non-contrast CT images, along with segmentations of intraparenchymal and intraventricular hemorrhage. Generation is conditioned on baseline imaging, clinical variables, and an explicit expansion indicator, enabling controllable simulation of realistic clinical scenarios. HemExp uses a hemorrhage-aware multi-head variational autoencoder and models progression as the difference between baseline and follow-up latent representations with a conditional diffusion model. The model is trained on paired scans from 450 patients across multiple centers and evaluated on 107 patients from a held-out institution. HemExp produces spatial HE probability maps by generating multiple synthetic follow-up images per patient to estimate distributions of plausible follow-up hematoma volumes. Perturbing clinical inputs such as symptom-onset-to-imaging time or anticoagulant status shifts the predicted follow-up volume distribution. HemExp extends binary predictors and demonstrates robust estimation of clinically relevant outcomes in the imaging space, such as hematoma volume, intraventricular involvement, and mass effects. Overall, our results support controllable latent diffusion as a promising direction for uncertainty-aware modeling of early ICH progression.

---


### 143. [CoMNeT: A MedNeXt-CorrDiff Framework for Volumetric Brain Tumor Segmentation](https://arxiv.org/abs/2606.15305)

**<font color=#1a73e8>作者：</font>** Michael L. Evans, MD Fayaz Bin Hossen, MD Shibly Sadique 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate brain tumor segmentation from multiparametric magnetic resonance imaging (MRI) is critical for treatment planning, response assessment, and quantitative neuro-oncology research. However, automated segmentation remains a difficult task in computer vision because of variation in tumor appearance and MRI protocols across patient scans. Moreover, clinically important regions such as enhancing tumor (ET) and tumor core (TC) are often small relative to the full brain volume, furthering increasing the difficulty of achieving high voxel-level precision. In this paper, we show that combining a modern 3D convolutional segmentation model with corrective diffusion-based refinement and ensembling improves volumetric glioma segmentation on the UTSW-Glioma dataset. We propose CoMNeT, a MedNeXt-CorrDiff framework that uses four MRI modalities as input and predicts ET, TC, and whole tumor (WT) regions for automated brain tumor segmentation. MedNeXt is used as the primary segmentation model with Global Response Normalization for feature learning, while CorrDiff is trained as a postprocessing residual refinement method to correct errors in the probability maps before final thresholding. Using five-fold cross-validation, CoMNeT achieved the highest Dice score for most tumor regions, with ET, TC, WT, and average Dice scores of 0.7543 +/- 0.0261, 0.6806 +/- 0.0166, 0.9049 +/- 0.0128, and 0.7798 +/- 0.0184, respectively. CoMNeT outperformed two selected baseline models: SegResNet (0.7555 +/- 0.0190 average Dice) and standalone MedNeXt (0.7697 +/- 0.0154 average Dice). Our findings support the use of corrective diffusion and fold-level probability ensembling as practical additions to existing state-of-the-art 3D convolutional models for automated glioma segmentation.

---


### 144. [PPDM: Pixel Puzzling Diffusion Model for Speed and Memory Efficient Volumetric Medical Image Translation](https://arxiv.org/abs/2606.15323)

**<font color=#1a73e8>作者：</font>** Tianqi Chen, Jun Hou, Yinchi Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have demonstrated superior fidelity for medical image-to-image translation, but their extension to high-resolution 3D volumes is severely constrained by prohibitive computational cost and GPU memory requirements. Existing memory-efficient strategies often compromise global volumetric consistency or fine anatomical detail. In this work, we propose the Pixel Puzzling Diffusion Model (PPDM), a simple and effective framework for memory- and speed-efficient 3D medical image translation. PPDM introduces a reversible pixel puzzle-unpuzzle operator that trades spatial resolution for channel dimensionality, substantially reducing activation memory while preserving global context. To further improve efficiency and stability, we adopt a direct bridge diffusion formulation that starts from the conditional input rather than pure noise, enabling the model to focus on task-relevant residuals. In addition, a puzzle-gradient loss is incorporated to enforce spatial coherence and suppress grid-like artifacts introduced by spatial rearrangement. We evaluate PPDM on multiple challenging 3D medical image translation tasks, including low-count PET denoising, joint PET denoising and attenuation correction, and cross-modal MRI translation. Across all tasks, PPDM consistently matches or outperforms full 3D diffusion models while reducing training GPU memory usage by up to an order of magnitude and significantly accelerating inference, and it outperforms existing memory-efficient diffusion approaches based on latent compression or frequency decomposition. These results demonstrate that PPDM provides a practical and scalable solution for high-fidelity 3D diffusion-based medical image translation under limited computational resources.

---


### 145. [Probabilistic Signature Inversion: Learning Conditional Distributions from Truncated Signatures](https://arxiv.org/abs/2606.15332)

**<font color=#1a73e8>作者：</font>** Junoh Kang, Kiseop Lee, Bohyung Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The signature transform is a principled feature map for continuous-time paths, valued for its uniqueness and universality. Recovering a path from its truncated signature is, however, structurally ill-posed because the truncated signature map is not injective. We therefore reframe truncated signature inversion as a probabilistic problem -- learning the conditional distribution of a path given its truncated signature -- and adopt a signature-conditioned flow matching model as a practical estimator. This probabilistic formulation elucidates the fundamental difficulty of inversion: Bayes reconstruction error quantifies the irreducible uncertainty remaining after conditioning on a statistic. We derive the Bayes-optimal error under linear statistics, obtaining a closed form for log-GBM and numerically tractable formulas for log-fBM and OU, yielding a concrete theoretical baseline for model validation. This baseline upper-bounds the Bayes error under truncated-signature conditioning, since truncated signatures provide richer information than linear statistics. Experiments show that empirical reconstruction errors under linear-statistics conditioning faithfully align with the theory-derived baseline, while errors decrease when the statistic is replaced with truncated signatures. Moreover, generated paths faithfully recover the conditioning signature while preserving key distributional and temporal structures, indicating that the estimator is well-calibrated to the target conditional distribution. Together, these results establish a well-posed probabilistic framework for truncated-signature inversion, with applicability demonstrated on real financial data beyond the parametric process families covered by theory.

---


### 146. [Privacy-Preserving Text Sanitization for Distributed Agents Collaboration via Disentangled Representations](https://arxiv.org/abs/2606.15335)

**<font color=#1a73e8>作者：</font>** Xuan Liu, Hefeng Zhou, Sicheng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When distributed agents exchange text across organizational boundaries, privacy leakage arises not only from explicit identifiers but also from distributional signatures such as formatting conventions, vocabulary choices, and syntactic patterns. We propose DiSan(Disentangled Sanitization), a privacy-preserving sanitization framework and a built-in component of Intern-Shannon for multi-agent collaboration. DiSan uses a two-stream encoder to factorize text into a source-invariant role subspace that preserves task semantics and a source-identifying style subspace that remains local. Federated proto-type alignment and adversarial regularization enable joint training without centralizing raw text. Experiments show that identifier-level masking is insufficient: masking 19.2% of tokens reduces TF-IDF stylometric attribution by only 18.6%. By contrast, DiSan reduces answer-level PII exposure by 20 times while maintaining 83% answer faithfulness on a distributed multi-agent RAG benchmark, and lowers Enron stylometric attribution by 73.2% under TF-IDF and 70.6% under a neural probe.

---


### 147. [Beyond Monolingual Deep Research: Evaluating Agents and Retrievers with Cross-Lingual BrowseComp-Plus](https://arxiv.org/abs/2606.15345)

**<font color=#1a73e8>作者：</font>** Yuheng Lu, Qingcheng Zeng, Heli Qi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research agents are increasingly evaluated on their ability to search for evidence, reason over retrieved sources, and produce grounded answers. Existing browsing benchmarks, however, largely assume that the user's query and the supporting evidence are written in the same language, leaving open whether agentic search systems can operate when relevant evidence appears in another language. We introduce XBCP (Cross-lingual BrowseComp-Plus), a controlled benchmark that preserves the English question-and-answer space of BrowseComp-Plus but varies the languages of the supporting documents. XBCP instantiates two complementary settings: in the cross-lingual setting, each query is paired with evidence in a single assigned language. In the multilingual setting, the full evidence corpus is distributed equally and randomly across 12 languages spanning high-resource and low-resource regimes. We evaluate four deep research agents using sparse and dense multilingual retrievers, measuring answer accuracy, evidence recall, search behavior, calibration, citation fidelity, and oracle retrieval. Results reveal substantial degradation when evidence is translated. Even strong, dense retrievers lose evidence recall, and agents become less calibrated and cite evidence less reliably. Notably, accuracy remains lower even when all gold evidence is supplied directly. These findings suggest that cross-lingual deep research exposes both retrieval failures and an independent, agent-side difficulty in integrating language-mismatched evidence.

---


### 148. [DYNA-PRUNER: Input-Adaptive Data-Model Co-Pruning for Efficient and Scalable Spatio-Temporal Media Prediction](https://arxiv.org/abs/2606.15346)

**<font color=#1a73e8>作者：</font>** Fuyan Zhang, Yuqi Li, Yingli Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal prediction supports radar/satellite nowcasting and city-scale traffic monitoring, but modern models are often too expensive for real-time deployment. This stems from a mismatch between dense computation and strong input-dependent redundancy (e.g., calm seas or clear skies). To enable automated, resource-aware architecture optimization in scalable media analysis, we propose Dyna-Pruner, an end-to-end framework for input-dependent co-pruning of data and model structure. A shared-importance synchronization mechanism generates coupled masks that prune redundant regions and their corresponding computational units (e.g., convolutional filters), yielding per-sample sparse sub-networks at inference time. Experiments on WeatherBench, SEVIR, and TaxiBJ show seamless integration with CNN, RNN, and Transformer backbones, reducing FLOPs by up to $70\%$ and achieving a $2.5\times$ speedup on NVIDIA Jetson AGX Orin with negligible accuracy loss ($<1\%$).

---


### 149. [Facial Affect Analysis for Service-Oriented Systems: Advances, Challenges, and Future Visions](https://arxiv.org/abs/2606.15351)

**<font color=#1a73e8>作者：</font>** Spyridon Georgiou, Aggelos Psiris, Thomas Lagkas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial Affect Analysis (FAA) is evolving from a stand-alone recognition task into a reusable perception capability for Service-Oriented Software Ecosystems (SoSE). This paper preserves the FAA methodological core while reframing recent advances through systems-engineering requirements for composable and dependable services. We review representative progress in static and dynamic expression analysis, action-unit and micro-expression modeling, and modern CNN, Transformer, graph, and hybrid architectures, then interpret these advances by their operational fit in edge, cloud, and hybrid service pipelines. The synthesis emphasizes SoSE concerns that determine deployability: service contracts for uncertainty-aware outputs, latency and availability envelopes, lifecycle monitoring and recalibration, governance-aware integration, and interoperability across independently evolving components. Our analysis shows that benchmark gains alone are insufficient for SoSE readiness; robustness under shift, intervention stability, fairness, privacy posture, and runtime guarantees are equally critical. We conclude with a roadmap for treating FAA as an operational service component with explicit interfaces, measurable quality attributes, and accountable lifecycle management.

---


### 150. [Sustainable Face Recognition on Low-Power Devices with VQ-VAE Embeddings](https://arxiv.org/abs/2606.15355)

**<font color=#1a73e8>作者：</font>** Christos Chronis, Georgios Th. Papadopoulos, Iraklis Varlamis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition has become a cornerstone of modern AI applications, yet conventional approaches often rely on computationally intensive models deployed in cloud environments, leading to increased network traffic, high energy consumption, and a heavy carbon footprint. This work introduces a sustainable, edge-deployable face recognition framework based on Vector-Quantized Variational Autoencoders (VQ-VAE), which generates compact and semantically rich latent representations of facial images. By leveraging the compression capacity and reconstruction quality of VQ-VAE embeddings on the edge and combining them with the power of pre-trained face embeddings in a knowledge distillation setup, our system achieves comparable accuracy to state-of-the-art face embedding models while significantly reducing memory and computation requirements on the edge, making it suitable for low-power edge devices. The integration of VQ-VAE compression minimizes network overhead while keeping the matching accuracy high by retaining only the most informative facial features in the latent space. As a result, the reconstructed images preserve the key identity characteristics, improving the robustness and overall performance of the face embeddings.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
